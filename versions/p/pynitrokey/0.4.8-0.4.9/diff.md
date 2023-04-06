# Comparing `tmp/pynitrokey-0.4.8.tar.gz` & `tmp/pynitrokey-0.4.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pynitrokey-0.4.8.tar", last modified: Thu Dec  9 07:33:01 2021, max compression
+gzip compressed data, was "pynitrokey-0.4.9.tar", last modified: Sat Dec 11 13:29:28 2021, max compression
```

## Comparing `pynitrokey-0.4.8.tar` & `pynitrokey-0.4.9.tar`

### file list

```diff
@@ -1,134 +1,134 @@
--rw-r--r--   0        0        0      192 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/.editorconfig
--rw-r--r--   0        0        0       78 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/.envrc
--rw-r--r--   0        0        0      217 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/.flake8
--rw-r--r--   0        0        0      207 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/.gitignore
--rw-r--r--   0        0        0     1701 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/.gitlab-ci.yml
--rw-r--r--   0        0        0     4080 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/CHANGELOG-parent.md
--rw-r--r--   0        0        0      129 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/Dockerfile
--rw-r--r--   0        0        0    10255 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/LICENSE-APACHE
--rw-r--r--   0        0        0     1023 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/LICENSE-MIT
--rw-r--r--   0        0        0      180 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/MAINTAINERS.md
--rw-r--r--   0        0        0     3619 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/Makefile
--rw-r--r--   0        0        0     5298 2021-12-09 07:32:24.742140 pynitrokey-0.4.8/README-parent.md
--rw-r--r--   0        0        0     4409 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/README.md
--rw-r--r--   0        0        0      198 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/RELEASE.md
--rwxr-xr-x   0        0        0      628 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/build-wine.sh
--rw-r--r--   0        0        0      130 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/ci-requirements.txt
--rw-r--r--   0        0        0      127 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/ci-scripts/.pypirc_tamplate
--rwxr-xr-x   0        0        0      263 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/ci-scripts/copy_common_scripts_key.sh
--rw-r--r--   0        0        0      177 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/dev-requirements.txt
--rwxr-xr-x   0        0        0     3888 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/interactive_test.sh
--rw-r--r--   0        0        0      369 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/mypy.ini
--rw-r--r--   0        0        0    77481 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/nethsm-scheme.json
--rw-r--r--   0        0        0      362 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/nitropy.py
--rw-r--r--   0        0        0        6 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/VERSION
--rw-r--r--   0        0        0      669 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/__init__.py
--rw-r--r--   0        0        0     2327 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/__init__.py
--rw-r--r--   0        0        0     4496 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/_patches.py
--rw-r--r--   0        0        0    23571 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/fido2.py
--rw-r--r--   0        0        0     1994 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/monitor.py
--rw-r--r--   0        0        0    35459 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/nethsm.py
--rw-r--r--   0        0        0     4449 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/nk3/__init__.py
--rw-r--r--   0        0        0     6696 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/nk3/test.py
--rw-r--r--   0        0        0     5130 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/pro.py
--rw-r--r--   0        0        0     5636 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/program.py
--rw-r--r--   0        0        0     4815 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/start.py
--rw-r--r--   0        0        0     1402 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/storage.py
--rw-r--r--   0        0        0     5838 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/cli/update.py
--rw-r--r--   0        0        0     1420 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/confconsts.py
--rw-r--r--   0        0        0      802 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/exceptions.py
--rw-r--r--   0        0        0     1588 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/fido2/__init__.py
--rw-r--r--   0        0        0    17464 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/fido2/client.py
--rw-r--r--   0        0        0     1656 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/fido2/commands.py
--rw-r--r--   0        0        0     8401 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/fido2/dfu.py
--rw-r--r--   0        0        0      507 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/fido2/enums.py
--rw-r--r--   0        0        0     8884 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/fido2/operations.py
--rw-r--r--   0        0        0     7334 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/helpers.py
--rw-r--r--   0        0        0    22954 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/libnk.py
--rw-r--r--   0        0        0    31517 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/nethsm/__init__.py
--rw-r--r--   0        0        0     1025 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/nethsm/client/__init__.py
--rw-r--r--   0        0        0      228 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/nethsm/client/api/__init__.py
--rw-r--r--   0        0        0   212360 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/nethsm/client/api/default_api.py
--rw-r--r--   0        0        0    37075 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/nethsm/client/api_client.py
--rw-r--r--   0        0        0      477 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/nethsm/client/apis/__init__.py
--rw-r--r--   0        0        0    17053 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/nethsm/client/configuration.py
--rw-r--r--   0        0        0     5267 2021-12-09 07:32:24.746140 pynitrokey-0.4.8/pynitrokey/nethsm/client/exceptions.py
--rw-r--r--   0        0        0      348 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/__init__.py
--rw-r--r--   0        0        0     6922 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/backup_passphrase_config.py
--rw-r--r--   0        0        0     7022 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/base64.py
--rw-r--r--   0        0        0     6869 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/decrypt_data.py
--rw-r--r--   0        0        0     7486 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/decrypt_mode.py
--rw-r--r--   0        0        0     7149 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/decrypt_request_data.py
--rw-r--r--   0        0        0     8092 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/distinguished_name.py
--rw-r--r--   0        0        0     6880 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/health_state_data.py
--rw-r--r--   0        0        0     7074 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/id.py
--rw-r--r--   0        0        0     6856 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/info_data.py
--rw-r--r--   0        0        0     7553 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_generate_request_data.py
--rw-r--r--   0        0        0     6795 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_item.py
--rw-r--r--   0        0        0     7066 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_list.py
--rw-r--r--   0        0        0     8972 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_mechanism.py
--rw-r--r--   0        0        0     7113 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_mechanisms.py
--rw-r--r--   0        0        0     7129 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_private_data.py
--rw-r--r--   0        0        0     6988 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_public_data.py
--rw-r--r--   0        0        0     7310 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_type.py
--rw-r--r--   0        0        0     7176 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/log_level.py
--rw-r--r--   0        0        0     7196 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/logging_config.py
--rw-r--r--   0        0        0     7049 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/network_config.py
--rw-r--r--   0        0        0     6975 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/passphrase.py
--rw-r--r--   0        0        0     7437 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/private_key.py
--rw-r--r--   0        0        0     7391 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/provision_request_data.py
--rw-r--r--   0        0        0     7606 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/public_key.py
--rw-r--r--   0        0        0     6846 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/random_data.py
--rw-r--r--   0        0        0     6827 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/random_request_data.py
--rw-r--r--   0        0        0     6863 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/sign_data.py
--rw-r--r--   0        0        0     7512 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/sign_mode.py
--rw-r--r--   0        0        0     7111 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/sign_request_data.py
--rw-r--r--   0        0        0     7052 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/switch.py
--rw-r--r--   0        0        0     7378 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/system_info.py
--rw-r--r--   0        0        0     7190 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/system_state.py
--rw-r--r--   0        0        0     6764 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/system_update_data.py
--rw-r--r--   0        0        0     6700 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/time_config.py
--rw-r--r--   0        0        0     6866 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/unattended_boot_config.py
--rw-r--r--   0        0        0     6922 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/unlock_passphrase_config.py
--rw-r--r--   0        0        0     6912 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/unlock_request_data.py
--rw-r--r--   0        0        0     7010 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_data.py
--rw-r--r--   0        0        0     6804 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_item.py
--rw-r--r--   0        0        0     7075 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_list.py
--rw-r--r--   0        0        0     6922 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_passphrase_post_data.py
--rw-r--r--   0        0        0     7319 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_post_data.py
--rw-r--r--   0        0        0     7228 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_role.py
--rw-r--r--   0        0        0    74670 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/model_utils.py
--rw-r--r--   0        0        0     3425 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/models/__init__.py
--rw-r--r--   0        0        0    12710 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nethsm/client/rest.py
--rw-r--r--   0        0        0      635 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nk3/__init__.py
--rw-r--r--   0        0        0     1079 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nk3/base.py
--rw-r--r--   0        0        0     4104 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nk3/device.py
--rw-r--r--   0        0        0    26938 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nk_headers/NK_C_API__3.4.0.h
--rw-r--r--   0        0        0    26938 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nk_headers/NK_C_API__3.4.1.h
--rw-r--r--   0        0        0    33094 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nk_headers/NK_C_API__3.5.0.h
--rw-r--r--   0        0        0    35717 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/nk_headers/NK_C_API__3.6.0.h
--rw-r--r--   0        0        0        2 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/start/__init__.py
--rw-r--r--   0        0        0    28407 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/start/gnuk_token.py
--rw-r--r--   0        0        0     1898 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/start/kdf_calc.py
--rw-r--r--   0        0        0     3093 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/start/rsa.py
--rw-r--r--   0        0        0     1081 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/start/rsa_pub_key.py
--rw-r--r--   0        0        0     2609 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/start/threaded_log.py
--rwxr-xr-x   0        0        0    20801 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/start/upgrade_by_passwd.py
--rwxr-xr-x   0        0        0     1994 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/start/usb_strings.py
--rw-r--r--   0        0        0      355 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/stubs/fido2/__init__.pyi
--rw-r--r--   0        0        0      379 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/stubs/fido2/attestation.pyi
--rw-r--r--   0        0        0     1058 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/stubs/fido2/client.pyi
--rw-r--r--   0        0        0      410 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/stubs/fido2/ctap.pyi
--rw-r--r--   0        0        0      498 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/stubs/fido2/ctap1.pyi
--rw-r--r--   0        0        0      758 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/stubs/fido2/ctap2.pyi
--rw-r--r--   0        0        0     1038 2021-12-09 07:32:24.750140 pynitrokey-0.4.8/pynitrokey/stubs/fido2/hid/__init__.pyi
--rw-r--r--   0        0        0      664 2021-12-09 07:32:24.754139 pynitrokey-0.4.8/pynitrokey/stubs/fido2/hid/base.pyi
--rw-r--r--   0        0        0     1432 2021-12-09 07:32:24.754139 pynitrokey-0.4.8/pynitrokey/stubs/fido2/server.pyi
--rw-r--r--   0        0        0      819 2021-12-09 07:32:24.754139 pynitrokey-0.4.8/pynitrokey/stubs/fido2/webauthn.pyi
--rw-r--r--   0        0        0      945 2021-12-09 07:32:24.754139 pynitrokey-0.4.8/pyproject.toml
--rw-r--r--   0        0        0      626 2021-12-09 07:32:24.754139 pynitrokey-0.4.8/win_setup.py
--rw-r--r--   0        0        0      369 2021-12-09 07:32:24.754139 pynitrokey-0.4.8/wine-build/Dockerfile
--rw-r--r--   0        0        0     3263 2021-12-09 07:32:24.754139 pynitrokey-0.4.8/wine-build/build-wine-docker.sh
--rwxr-xr-x   0        0        0       54 2021-12-09 07:32:24.754139 pynitrokey-0.4.8/wine-build/entrypoint.sh
--rw-r--r--   0        0        0     1219 2021-12-09 07:32:24.754139 pynitrokey-0.4.8/wine-build/nitropy.spec.tmpl
--rw-r--r--   0        0        0     5392 1970-01-01 00:00:00.000000 pynitrokey-0.4.8/PKG-INFO
+-rw-r--r--   0        0        0      192 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/.editorconfig
+-rw-r--r--   0        0        0       78 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/.envrc
+-rw-r--r--   0        0        0      217 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/.flake8
+-rw-r--r--   0        0        0      207 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/.gitignore
+-rw-r--r--   0        0        0     1701 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/.gitlab-ci.yml
+-rw-r--r--   0        0        0     4080 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/CHANGELOG-parent.md
+-rw-r--r--   0        0        0      129 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/Dockerfile
+-rw-r--r--   0        0        0    10255 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/LICENSE-APACHE
+-rw-r--r--   0        0        0     1023 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/LICENSE-MIT
+-rw-r--r--   0        0        0      180 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/MAINTAINERS.md
+-rw-r--r--   0        0        0     3619 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/Makefile
+-rw-r--r--   0        0        0     5298 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/README-parent.md
+-rw-r--r--   0        0        0     4409 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/README.md
+-rw-r--r--   0        0        0      198 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/RELEASE.md
+-rwxr-xr-x   0        0        0      628 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/build-wine.sh
+-rw-r--r--   0        0        0      130 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/ci-requirements.txt
+-rw-r--r--   0        0        0      127 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/ci-scripts/.pypirc_tamplate
+-rwxr-xr-x   0        0        0      263 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/ci-scripts/copy_common_scripts_key.sh
+-rw-r--r--   0        0        0      177 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/dev-requirements.txt
+-rwxr-xr-x   0        0        0     3888 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/interactive_test.sh
+-rw-r--r--   0        0        0      369 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/mypy.ini
+-rw-r--r--   0        0        0    77481 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/nethsm-scheme.json
+-rw-r--r--   0        0        0      362 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/nitropy.py
+-rw-r--r--   0        0        0        6 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/pynitrokey/VERSION
+-rw-r--r--   0        0        0      669 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/pynitrokey/__init__.py
+-rw-r--r--   0        0        0     2327 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/pynitrokey/cli/__init__.py
+-rw-r--r--   0        0        0     4496 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/pynitrokey/cli/_patches.py
+-rw-r--r--   0        0        0    23581 2021-12-11 13:28:55.197020 pynitrokey-0.4.9/pynitrokey/cli/fido2.py
+-rw-r--r--   0        0        0     1994 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/cli/monitor.py
+-rw-r--r--   0        0        0    35459 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/cli/nethsm.py
+-rw-r--r--   0        0        0     4490 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/cli/nk3/__init__.py
+-rw-r--r--   0        0        0     6659 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/cli/nk3/test.py
+-rw-r--r--   0        0        0     5130 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/cli/pro.py
+-rw-r--r--   0        0        0     5636 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/cli/program.py
+-rw-r--r--   0        0        0     4815 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/cli/start.py
+-rw-r--r--   0        0        0     1402 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/cli/storage.py
+-rw-r--r--   0        0        0     5838 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/cli/update.py
+-rw-r--r--   0        0        0     1420 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/confconsts.py
+-rw-r--r--   0        0        0      802 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/exceptions.py
+-rw-r--r--   0        0        0     1588 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/fido2/__init__.py
+-rw-r--r--   0        0        0    17540 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/fido2/client.py
+-rw-r--r--   0        0        0     1656 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/fido2/commands.py
+-rw-r--r--   0        0        0     8401 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/fido2/dfu.py
+-rw-r--r--   0        0        0      507 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/fido2/enums.py
+-rw-r--r--   0        0        0     8884 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/fido2/operations.py
+-rw-r--r--   0        0        0     7334 2021-12-11 13:28:55.201020 pynitrokey-0.4.9/pynitrokey/helpers.py
+-rw-r--r--   0        0        0    22954 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/libnk.py
+-rw-r--r--   0        0        0    31517 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/__init__.py
+-rw-r--r--   0        0        0     1025 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/__init__.py
+-rw-r--r--   0        0        0      228 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/api/__init__.py
+-rw-r--r--   0        0        0   212360 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/api/default_api.py
+-rw-r--r--   0        0        0    37075 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/api_client.py
+-rw-r--r--   0        0        0      477 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/apis/__init__.py
+-rw-r--r--   0        0        0    17053 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/configuration.py
+-rw-r--r--   0        0        0     5267 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/exceptions.py
+-rw-r--r--   0        0        0      348 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/__init__.py
+-rw-r--r--   0        0        0     6922 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/backup_passphrase_config.py
+-rw-r--r--   0        0        0     7022 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/base64.py
+-rw-r--r--   0        0        0     6869 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/decrypt_data.py
+-rw-r--r--   0        0        0     7486 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/decrypt_mode.py
+-rw-r--r--   0        0        0     7149 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/decrypt_request_data.py
+-rw-r--r--   0        0        0     8092 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/distinguished_name.py
+-rw-r--r--   0        0        0     6880 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/health_state_data.py
+-rw-r--r--   0        0        0     7074 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/id.py
+-rw-r--r--   0        0        0     6856 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/info_data.py
+-rw-r--r--   0        0        0     7553 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_generate_request_data.py
+-rw-r--r--   0        0        0     6795 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_item.py
+-rw-r--r--   0        0        0     7066 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_list.py
+-rw-r--r--   0        0        0     8972 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_mechanism.py
+-rw-r--r--   0        0        0     7113 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_mechanisms.py
+-rw-r--r--   0        0        0     7129 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_private_data.py
+-rw-r--r--   0        0        0     6988 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_public_data.py
+-rw-r--r--   0        0        0     7310 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_type.py
+-rw-r--r--   0        0        0     7176 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/log_level.py
+-rw-r--r--   0        0        0     7196 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/logging_config.py
+-rw-r--r--   0        0        0     7049 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/network_config.py
+-rw-r--r--   0        0        0     6975 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/passphrase.py
+-rw-r--r--   0        0        0     7437 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/private_key.py
+-rw-r--r--   0        0        0     7391 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/provision_request_data.py
+-rw-r--r--   0        0        0     7606 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/public_key.py
+-rw-r--r--   0        0        0     6846 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/random_data.py
+-rw-r--r--   0        0        0     6827 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/random_request_data.py
+-rw-r--r--   0        0        0     6863 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/sign_data.py
+-rw-r--r--   0        0        0     7512 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/sign_mode.py
+-rw-r--r--   0        0        0     7111 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/sign_request_data.py
+-rw-r--r--   0        0        0     7052 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/switch.py
+-rw-r--r--   0        0        0     7378 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/system_info.py
+-rw-r--r--   0        0        0     7190 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/system_state.py
+-rw-r--r--   0        0        0     6764 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/system_update_data.py
+-rw-r--r--   0        0        0     6700 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/time_config.py
+-rw-r--r--   0        0        0     6866 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/unattended_boot_config.py
+-rw-r--r--   0        0        0     6922 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/unlock_passphrase_config.py
+-rw-r--r--   0        0        0     6912 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/unlock_request_data.py
+-rw-r--r--   0        0        0     7010 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_data.py
+-rw-r--r--   0        0        0     6804 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_item.py
+-rw-r--r--   0        0        0     7075 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_list.py
+-rw-r--r--   0        0        0     6922 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_passphrase_post_data.py
+-rw-r--r--   0        0        0     7319 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_post_data.py
+-rw-r--r--   0        0        0     7228 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_role.py
+-rw-r--r--   0        0        0    74670 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/model_utils.py
+-rw-r--r--   0        0        0     3425 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/models/__init__.py
+-rw-r--r--   0        0        0    12710 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nethsm/client/rest.py
+-rw-r--r--   0        0        0      728 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nk3/__init__.py
+-rw-r--r--   0        0        0     1079 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nk3/base.py
+-rw-r--r--   0        0        0     4616 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nk3/device.py
+-rw-r--r--   0        0        0    26938 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nk_headers/NK_C_API__3.4.0.h
+-rw-r--r--   0        0        0    26938 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nk_headers/NK_C_API__3.4.1.h
+-rw-r--r--   0        0        0    33094 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nk_headers/NK_C_API__3.5.0.h
+-rw-r--r--   0        0        0    35717 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/nk_headers/NK_C_API__3.6.0.h
+-rw-r--r--   0        0        0        2 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/start/__init__.py
+-rw-r--r--   0        0        0    28407 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/start/gnuk_token.py
+-rw-r--r--   0        0        0     1898 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/start/kdf_calc.py
+-rw-r--r--   0        0        0     3093 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/start/rsa.py
+-rw-r--r--   0        0        0     1081 2021-12-11 13:28:55.209020 pynitrokey-0.4.9/pynitrokey/start/rsa_pub_key.py
+-rw-r--r--   0        0        0     2609 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/start/threaded_log.py
+-rwxr-xr-x   0        0        0    20801 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/start/upgrade_by_passwd.py
+-rwxr-xr-x   0        0        0     1994 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/start/usb_strings.py
+-rw-r--r--   0        0        0      355 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/stubs/fido2/__init__.pyi
+-rw-r--r--   0        0        0      379 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/stubs/fido2/attestation.pyi
+-rw-r--r--   0        0        0     1058 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/stubs/fido2/client.pyi
+-rw-r--r--   0        0        0      410 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/stubs/fido2/ctap.pyi
+-rw-r--r--   0        0        0      498 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/stubs/fido2/ctap1.pyi
+-rw-r--r--   0        0        0      758 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/stubs/fido2/ctap2.pyi
+-rw-r--r--   0        0        0     1038 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/stubs/fido2/hid/__init__.pyi
+-rw-r--r--   0        0        0      664 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/stubs/fido2/hid/base.pyi
+-rw-r--r--   0        0        0     1432 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/stubs/fido2/server.pyi
+-rw-r--r--   0        0        0      819 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pynitrokey/stubs/fido2/webauthn.pyi
+-rw-r--r--   0        0        0      945 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/pyproject.toml
+-rw-r--r--   0        0        0      626 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/win_setup.py
+-rw-r--r--   0        0        0      369 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/wine-build/Dockerfile
+-rw-r--r--   0        0        0     3263 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/wine-build/build-wine-docker.sh
+-rwxr-xr-x   0        0        0       54 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/wine-build/entrypoint.sh
+-rw-r--r--   0        0        0     1219 2021-12-11 13:28:55.213020 pynitrokey-0.4.9/wine-build/nitropy.spec.tmpl
+-rw-r--r--   0        0        0     5392 1970-01-01 00:00:00.000000 pynitrokey-0.4.9/PKG-INFO
```

### Comparing `pynitrokey-0.4.8/.gitlab-ci.yml` & `pynitrokey-0.4.9/.gitlab-ci.yml`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/CHANGELOG-parent.md` & `pynitrokey-0.4.9/CHANGELOG-parent.md`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/LICENSE-APACHE` & `pynitrokey-0.4.9/LICENSE-APACHE`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/LICENSE-MIT` & `pynitrokey-0.4.9/LICENSE-MIT`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/Makefile` & `pynitrokey-0.4.9/Makefile`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/README-parent.md` & `pynitrokey-0.4.9/README-parent.md`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/README.md` & `pynitrokey-0.4.9/README.md`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/build-wine.sh` & `pynitrokey-0.4.9/build-wine.sh`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/interactive_test.sh` & `pynitrokey-0.4.9/interactive_test.sh`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/nethsm-scheme.json` & `pynitrokey-0.4.9/nethsm-scheme.json`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/__init__.py` & `pynitrokey-0.4.9/pynitrokey/__init__.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/__init__.py` & `pynitrokey-0.4.9/pynitrokey/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/_patches.py` & `pynitrokey-0.4.9/pynitrokey/cli/_patches.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/fido2.py` & `pynitrokey-0.4.9/pynitrokey/cli/fido2.py`

 * *Files 0% similar despite different names*

```diff
@@ -630,15 +630,15 @@
         "e1f40563be291c30bc3cc381a7ef46b89ef972bdb048b716b0a888043cf9072a": "Nitrokey FIDO2 Dev 2.x ",
         "ad8fd1d16f59104b9e06ef323cc03f777ed5303cd421a101c9cb00bb3fdf722d": "Nitrokey 3",
         "44fa598fdc98681dc5c8659a804c40bd6e53f8e54a781608b0651d47a53e1c8a": "Nitrokey 3 Dev",
     }
 
     a_hex = cert
     if a_hex in hashdb:
-        local_print(f"found device: {hashdb[a_hex]}")
+        local_print(f"found device: {hashdb[a_hex]} ({a_hex})")
     else:
         local_print(f"unknown fingerprint! {a_hex}")
 
 
 @click.command()
 @click.option(
     "-s",
```

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/monitor.py` & `pynitrokey-0.4.9/pynitrokey/cli/monitor.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/nethsm.py` & `pynitrokey-0.4.9/pynitrokey/cli/nethsm.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/nk3/__init__.py` & `pynitrokey-0.4.9/pynitrokey/cli/nk3/__init__.py`

 * *Files 7% similar despite different names*

```diff
@@ -9,40 +9,44 @@
 
 from typing import List, Optional, TypeVar
 
 import click
 
 from pynitrokey.helpers import local_critical, local_print
 from pynitrokey.nk3 import list as list_nk3
+from pynitrokey.nk3 import open as open_nk3
 from pynitrokey.nk3.base import Nitrokey3Base
 from pynitrokey.nk3.device import Nitrokey3Device
 
 T = TypeVar("T", bound="Nitrokey3Base")
 
 
 class Context:
     def __init__(self, path: Optional[str]) -> None:
         self.path = path
 
     def list(self) -> List[Nitrokey3Base]:
-        devices = []
-        for device in list_nk3():
-            if not self.path or self.path == device.path:
-                devices.append(device)
-        return devices
+        if self.path:
+            device = open_nk3(self.path)
+            if device:
+                return [device]
+            else:
+                return []
+        else:
+            return list_nk3()
 
     def _select_unique(self, name: str, devices: List[T]) -> T:
         if len(devices) == 0:
             msg = f"No {name} device found"
             if self.path:
                 msg += f" at path {self.path}"
-            raise click.ClickException(msg)
+            local_critical(msg)
 
         if len(devices) > 1:
-            raise click.ClickException(
+            local_critical(
                 f"Multiple {name} devices found -- use the --path option to select one"
             )
 
         return devices[0]
 
     def connect(self) -> Nitrokey3Base:
         return self._select_unique("Nitrokey 3", self.list())
@@ -99,15 +103,14 @@
             rng = device.rng()
             local_print(rng[:length].hex())
             length -= len(rng)
 
 
 @nk3.command()
 @click.option(
-    "-p",
     "--pin",
     "pin",
     help="The FIDO2 PIN of the device (if enabled)",
 )
 @click.pass_obj
 def test(ctx: Context, pin: Optional[str]) -> None:
     """Run some tests on all connected Nitrokey 3 devices."""
```

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/nk3/test.py` & `pynitrokey-0.4.9/pynitrokey/cli/nk3/test.py`

 * *Files 2% similar despite different names*

```diff
@@ -188,15 +188,14 @@
         results.append(result)
 
         idx = str(i + 1).rjust(idx_len)
         name = test_case.name.ljust(name_len)
         status = result.status.name.ljust(status_len)
         msg = ""
         if result.data:
-            print(repr(result.data))
             msg = str(result.data)
         elif result.exc_info[1]:
             logger.error(
                 f"An exception occured during the execution of the test {test_case.name}:",
                 exc_info=result.exc_info,
             )
             msg = str(result.exc_info[1])
```

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/pro.py` & `pynitrokey-0.4.9/pynitrokey/cli/pro.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/program.py` & `pynitrokey-0.4.9/pynitrokey/cli/program.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/start.py` & `pynitrokey-0.4.9/pynitrokey/cli/start.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/storage.py` & `pynitrokey-0.4.9/pynitrokey/cli/storage.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/cli/update.py` & `pynitrokey-0.4.9/pynitrokey/cli/update.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/confconsts.py` & `pynitrokey-0.4.9/pynitrokey/confconsts.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/exceptions.py` & `pynitrokey-0.4.9/pynitrokey/exceptions.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/fido2/__init__.py` & `pynitrokey-0.4.9/pynitrokey/fido2/__init__.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/fido2/client.py` & `pynitrokey-0.4.9/pynitrokey/fido2/client.py`

 * *Files 1% similar despite different names*

```diff
@@ -63,27 +63,30 @@
         """option to reboot after programming"""
         try:
             self.exchange(SoloBootloader.reboot)
         except OSError:
             pass
 
     def find_device(self, dev=None, solo_serial: str = None):
+        devices = []
         if dev is None:
-            devices = list(CtapHidDevice.list_devices())
             if solo_serial is not None:
                 if solo_serial.startswith("device="):
                     solo_serial = solo_serial.split("=")[1]
                     dev = open_device(solo_serial)
                 else:
+                    devices = list(CtapHidDevice.list_devices())
                     devices = [
                         d for d in devices if d.descriptor.serial_number == solo_serial
                     ]
-            if dev is None and len(devices) > 1:
+            else:
+                devices = list(CtapHidDevice.list_devices())
+            if len(devices) > 1:
                 raise pynitrokey.exceptions.NonUniqueDeviceError
-            if dev is None and len(devices) > 0:
+            if len(devices) > 0:
                 dev = devices[0]
         if dev is None:
             raise RuntimeError("No FIDO device found")
         self.dev = dev
 
         self.ctap1 = CTAP1(dev)
```

### Comparing `pynitrokey-0.4.8/pynitrokey/fido2/commands.py` & `pynitrokey-0.4.9/pynitrokey/fido2/commands.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/fido2/dfu.py` & `pynitrokey-0.4.9/pynitrokey/fido2/dfu.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/fido2/operations.py` & `pynitrokey-0.4.9/pynitrokey/fido2/operations.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/helpers.py` & `pynitrokey-0.4.9/pynitrokey/helpers.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/libnk.py` & `pynitrokey-0.4.9/pynitrokey/libnk.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/__init__.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/__init__.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/__init__.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/__init__.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/api/default_api.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/api/default_api.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/api_client.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/api_client.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/configuration.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/configuration.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/exceptions.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/exceptions.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/backup_passphrase_config.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/backup_passphrase_config.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/base64.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/base64.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/decrypt_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/decrypt_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/decrypt_mode.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/decrypt_mode.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/decrypt_request_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/decrypt_request_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/distinguished_name.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/distinguished_name.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/health_state_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/health_state_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/id.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/id.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/info_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/info_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_generate_request_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_generate_request_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_item.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_item.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_list.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_list.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_mechanism.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_mechanism.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_mechanisms.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_mechanisms.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_private_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_private_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_public_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_public_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/key_type.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/key_type.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/log_level.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/log_level.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/logging_config.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/logging_config.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/network_config.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/network_config.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/passphrase.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/passphrase.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/private_key.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/private_key.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/provision_request_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/provision_request_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/public_key.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/public_key.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/random_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/random_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/random_request_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/random_request_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/sign_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/sign_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/sign_mode.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/sign_mode.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/sign_request_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/sign_request_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/switch.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/switch.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/system_info.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/system_info.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/system_state.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/system_state.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/system_update_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/system_update_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/time_config.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/time_config.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/unattended_boot_config.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/unattended_boot_config.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/unlock_passphrase_config.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/unlock_passphrase_config.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/unlock_request_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/unlock_request_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_item.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_item.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_list.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_list.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_passphrase_post_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_passphrase_post_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_post_data.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_post_data.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model/user_role.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model/user_role.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/model_utils.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/model_utils.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/models/__init__.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/models/__init__.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nethsm/client/rest.py` & `pynitrokey-0.4.9/pynitrokey/nethsm/client/rest.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nk3/__init__.py` & `pynitrokey-0.4.9/pynitrokey/nk3/__init__.py`

 * *Files 17% similar despite different names*

```diff
@@ -3,20 +3,23 @@
 # Copyright 2021 Nitrokey Developers
 #
 # Licensed under the Apache License, Version 2.0, <LICENSE-APACHE or
 # http://apache.org/licenses/LICENSE-2.0> or the MIT license <LICENSE-MIT or
 # http://opensource.org/licenses/MIT>, at your option. This file may not be
 # copied, modified, or distributed except according to those terms.
 
-from typing import List
+from typing import List, Optional
 
 from .base import Nitrokey3Base
+from .device import Nitrokey3Device
 
 VID_NITROKEY = 0x20A0
 PID_NITROKEY3_DEVICE = 0x42B2
 PID_NITROKEY3_BOOTLOADER = 0x42DD
 
 
 def list() -> List[Nitrokey3Base]:
-    from .device import Nitrokey3Device
-
     return [device for device in Nitrokey3Device.list()]
+
+
+def open(path: str) -> Optional[Nitrokey3Base]:
+    return Nitrokey3Device.open(path)
```

### Comparing `pynitrokey-0.4.8/pynitrokey/nk3/base.py` & `pynitrokey-0.4.9/pynitrokey/nk3/base.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nk3/device.py` & `pynitrokey-0.4.9/pynitrokey/nk3/device.py`

 * *Files 13% similar despite different names*

```diff
@@ -5,26 +5,28 @@
 # Licensed under the Apache License, Version 2.0, <LICENSE-APACHE or
 # http://apache.org/licenses/LICENSE-2.0> or the MIT license <LICENSE-MIT or
 # http://opensource.org/licenses/MIT>, at your option. This file may not be
 # copied, modified, or distributed except according to those terms.
 
 import enum
 import logging
+import sys
 from enum import Enum
 from typing import List, Optional
 
-from fido2.hid import CtapHidDevice
+from fido2.hid import CtapHidDevice, open_device
 
-from . import PID_NITROKEY3_DEVICE, VID_NITROKEY
 from .base import Nitrokey3Base
 
 RNG_LEN = 57
 UUID_LEN = 16
 VERSION_LEN = 4
 
+logger = logging.getLogger(__name__)
+
 
 @enum.unique
 class Command(Enum):
     """Vendor-specific CTAPHID commands for the Nitrokey 3."""
 
     UPDATE = 0x51
     REBOOT = 0x53
@@ -52,23 +54,25 @@
         return f"v{self.major}.{self.minor}.{self.patch}"
 
 
 class Nitrokey3Device(Nitrokey3Base):
     """A Nitrokey 3 device running the firmware."""
 
     def __init__(self, device: CtapHidDevice) -> None:
+        from . import PID_NITROKEY3_DEVICE, VID_NITROKEY
+
         (vid, pid) = (device.descriptor.vid, device.descriptor.pid)
         if (vid, pid) != (VID_NITROKEY, PID_NITROKEY3_DEVICE):
             raise ValueError(
                 "Not a Nitrokey 3 device: expected VID:PID "
                 f"{VID_NITROKEY:x}:{PID_NITROKEY3_DEVICE:x}, got {vid:x}:{pid:x}"
             )
 
         self.device = device
-        self.logger = logging.getLogger(f"{__name__}.{device.descriptor.path}")
+        self.logger = logger.getChild(device.descriptor.path)
 
     @property
     def path(self) -> str:
         return self.device.descriptor.path
 
     @property
     def name(self) -> str:
@@ -125,7 +129,20 @@
         for device in CtapHidDevice.list_devices():
             try:
                 devices.append(Nitrokey3Device(device))
             except ValueError:
                 # not a Nitrokey 3 device, skip
                 pass
         return devices
+
+    @staticmethod
+    def open(path: str) -> Optional["Nitrokey3Device"]:
+        try:
+            device = open_device(path)
+        except Exception:
+            logger.warn(f"No CTAPHID device at path {path}", exc_info=sys.exc_info())
+            return None
+        try:
+            return Nitrokey3Device(device)
+        except ValueError:
+            logger.warn(f"No Nitrokey 3 device at path {path}", exc_info=sys.exc_info())
+            return None
```

### Comparing `pynitrokey-0.4.8/pynitrokey/nk_headers/NK_C_API__3.4.0.h` & `pynitrokey-0.4.9/pynitrokey/nk_headers/NK_C_API__3.4.0.h`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nk_headers/NK_C_API__3.4.1.h` & `pynitrokey-0.4.9/pynitrokey/nk_headers/NK_C_API__3.4.1.h`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nk_headers/NK_C_API__3.5.0.h` & `pynitrokey-0.4.9/pynitrokey/nk_headers/NK_C_API__3.5.0.h`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/nk_headers/NK_C_API__3.6.0.h` & `pynitrokey-0.4.9/pynitrokey/nk_headers/NK_C_API__3.6.0.h`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/start/gnuk_token.py` & `pynitrokey-0.4.9/pynitrokey/start/gnuk_token.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/start/kdf_calc.py` & `pynitrokey-0.4.9/pynitrokey/start/kdf_calc.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/start/rsa.py` & `pynitrokey-0.4.9/pynitrokey/start/rsa.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/start/rsa_pub_key.py` & `pynitrokey-0.4.9/pynitrokey/start/rsa_pub_key.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/start/threaded_log.py` & `pynitrokey-0.4.9/pynitrokey/start/threaded_log.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/start/upgrade_by_passwd.py` & `pynitrokey-0.4.9/pynitrokey/start/upgrade_by_passwd.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/start/usb_strings.py` & `pynitrokey-0.4.9/pynitrokey/start/usb_strings.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/stubs/fido2/client.pyi` & `pynitrokey-0.4.9/pynitrokey/stubs/fido2/client.pyi`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/stubs/fido2/ctap2.pyi` & `pynitrokey-0.4.9/pynitrokey/stubs/fido2/ctap2.pyi`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/stubs/fido2/hid/__init__.pyi` & `pynitrokey-0.4.9/pynitrokey/stubs/fido2/hid/__init__.pyi`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/stubs/fido2/hid/base.pyi` & `pynitrokey-0.4.9/pynitrokey/stubs/fido2/hid/base.pyi`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/stubs/fido2/server.pyi` & `pynitrokey-0.4.9/pynitrokey/stubs/fido2/server.pyi`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pynitrokey/stubs/fido2/webauthn.pyi` & `pynitrokey-0.4.9/pynitrokey/stubs/fido2/webauthn.pyi`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/pyproject.toml` & `pynitrokey-0.4.9/pyproject.toml`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/win_setup.py` & `pynitrokey-0.4.9/win_setup.py`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/wine-build/build-wine-docker.sh` & `pynitrokey-0.4.9/wine-build/build-wine-docker.sh`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/wine-build/nitropy.spec.tmpl` & `pynitrokey-0.4.9/wine-build/nitropy.spec.tmpl`

 * *Files identical despite different names*

### Comparing `pynitrokey-0.4.8/PKG-INFO` & `pynitrokey-0.4.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pynitrokey
-Version: 0.4.8
+Version: 0.4.9
 Summary: Python Library for Nitrokey FIDO2 & Nitrokey Start.
 Home-page: https://github.com/Nitrokey/pynitrokey
 Author: Nitrokey
 Author-email: pypi@nitrokey.com
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 Classifier: License :: OSI Approved :: MIT License
```

