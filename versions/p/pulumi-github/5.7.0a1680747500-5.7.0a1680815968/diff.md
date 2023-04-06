# Comparing `tmp/pulumi_github-5.7.0a1680747500.tar.gz` & `tmp/pulumi_github-5.7.0a1680815968.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pulumi_github-5.7.0a1680747500.tar", last modified: Thu Apr  6 02:22:59 2023, max compression
+gzip compressed data, was "pulumi_github-5.7.0a1680815968.tar", last modified: Thu Apr  6 21:24:05 2023, max compression
```

## Comparing `pulumi_github-5.7.0a1680747500.tar` & `pulumi_github-5.7.0a1680815968.tar`

### file list

```diff
@@ -1,121 +1,125 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 02:22:59.396641 pulumi_github-5.7.0a1680747500/
--rw-r--r--   0 runner    (1001) docker     (123)     2885 2023-04-06 02:22:59.396641 pulumi_github-5.7.0a1680747500/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2542 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 02:22:59.396641 pulumi_github-5.7.0a1680747500/pulumi_github/
--rw-r--r--   0 runner    (1001) docker     (123)    15071 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    55545 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/_inputs.py
--rw-r--r--   0 runner    (1001) docker     (123)     8081 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/_utilities.py
--rw-r--r--   0 runner    (1001) docker     (123)    19178 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_environment_secret.py
--rw-r--r--   0 runner    (1001) docker     (123)    16013 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_environment_variable.py
--rw-r--r--   0 runner    (1001) docker     (123)     9151 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_organization_oidc_subject_claim_customization_template.py
--rw-r--r--   0 runner    (1001) docker     (123)    20745 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_organization_permissions.py
--rw-r--r--   0 runner    (1001) docker     (123)    22394 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_organization_secret.py
--rw-r--r--   0 runner    (1001) docker     (123)    10898 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_organization_secret_repositories.py
--rw-r--r--   0 runner    (1001) docker     (123)    16244 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_organization_variable.py
--rw-r--r--   0 runner    (1001) docker     (123)     9995 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_repository_access_level.py
--rw-r--r--   0 runner    (1001) docker     (123)    14803 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_repository_oidc_subject_claim_customization_template.py
--rw-r--r--   0 runner    (1001) docker     (123)    16292 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_repository_permissions.py
--rw-r--r--   0 runner    (1001) docker     (123)    23259 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_runner_group.py
--rw-r--r--   0 runner    (1001) docker     (123)    15530 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_secret.py
--rw-r--r--   0 runner    (1001) docker     (123)    12596 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/actions_variable.py
--rw-r--r--   0 runner    (1001) docker     (123)    10615 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/app_installation_repositories.py
--rw-r--r--   0 runner    (1001) docker     (123)    11169 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/app_installation_repository.py
--rw-r--r--   0 runner    (1001) docker     (123)    16865 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/branch.py
--rw-r--r--   0 runner    (1001) docker     (123)    12115 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/branch_default.py
--rw-r--r--   0 runner    (1001) docker     (123)    44058 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/branch_protection.py
--rw-r--r--   0 runner    (1001) docker     (123)    31424 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/branch_protection_v3.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 02:22:59.396641 pulumi_github-5.7.0a1680747500/pulumi_github/config/
--rw-r--r--   0 runner    (1001) docker     (123)      285 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/config/outputs.py
--rw-r--r--   0 runner    (1001) docker     (123)     2371 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/config/vars.py
--rw-r--r--   0 runner    (1001) docker     (123)    18662 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/dependabot_organization_secret.py
--rw-r--r--   0 runner    (1001) docker     (123)     9223 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/dependabot_organization_secret_repositories.py
--rw-r--r--   0 runner    (1001) docker     (123)    14359 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/dependabot_secret.py
--rw-r--r--   0 runner    (1001) docker     (123)    10110 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/emu_group_mapping.py
--rw-r--r--   0 runner    (1001) docker     (123)    14476 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/enterprise_organization.py
--rw-r--r--   0 runner    (1001) docker     (123)     4989 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_environment_secrets.py
--rw-r--r--   0 runner    (1001) docker     (123)     5143 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_environment_variables.py
--rw-r--r--   0 runner    (1001) docker     (123)     3137 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_organization_oidc_subject_claim_customization_template.py
--rw-r--r--   0 runner    (1001) docker     (123)     3141 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_organization_registration_token.py
--rw-r--r--   0 runner    (1001) docker     (123)     2549 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_organization_secrets.py
--rw-r--r--   0 runner    (1001) docker     (123)     2611 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_organization_variables.py
--rw-r--r--   0 runner    (1001) docker     (123)     4327 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_public_key.py
--rw-r--r--   0 runner    (1001) docker     (123)     4374 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_registration_token.py
--rw-r--r--   0 runner    (1001) docker     (123)     5164 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_repository_oidc_subject_claim_customization_template.py
--rw-r--r--   0 runner    (1001) docker     (123)     4213 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_secrets.py
--rw-r--r--   0 runner    (1001) docker     (123)     4304 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_variables.py
--rw-r--r--   0 runner    (1001) docker     (123)     4738 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_branch.py
--rw-r--r--   0 runner    (1001) docker     (123)     5236 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_collaborators.py
--rw-r--r--   0 runner    (1001) docker     (123)     2608 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_dependabot_organization_secrets.py
--rw-r--r--   0 runner    (1001) docker     (123)     3372 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_dependabot_public_key.py
--rw-r--r--   0 runner    (1001) docker     (123)     4321 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_dependabot_secrets.py
--rw-r--r--   0 runner    (1001) docker     (123)     4647 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_enterprise.py
--rw-r--r--   0 runner    (1001) docker     (123)     2662 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_external_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     4071 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_github_app.py
--rw-r--r--   0 runner    (1001) docker     (123)    14508 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_ip_ranges.py
--rw-r--r--   0 runner    (1001) docker     (123)     5557 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_membership.py
--rw-r--r--   0 runner    (1001) docker     (123)     6129 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_organization.py
--rw-r--r--   0 runner    (1001) docker     (123)     2795 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_organization_ip_allow_list.py
--rw-r--r--   0 runner    (1001) docker     (123)     2622 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_organization_team_sync_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     6941 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_organization_teams.py
--rw-r--r--   0 runner    (1001) docker     (123)     2574 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_organization_webhooks.py
--rw-r--r--   0 runner    (1001) docker     (123)     4319 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_ref.py
--rw-r--r--   0 runner    (1001) docker     (123)    13103 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_release.py
--rw-r--r--   0 runner    (1001) docker     (123)     7590 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_repositories.py
--rw-r--r--   0 runner    (1001) docker     (123)    20234 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_repository.py
--rw-r--r--   0 runner    (1001) docker     (123)     6121 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_branches.py
--rw-r--r--   0 runner    (1001) docker     (123)     3758 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_deploy_keys.py
--rw-r--r--   0 runner    (1001) docker     (123)     7793 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_file.py
--rw-r--r--   0 runner    (1001) docker     (123)     6319 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_milestone.py
--rw-r--r--   0 runner    (1001) docker     (123)    11966 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_pull_request.py
--rw-r--r--   0 runner    (1001) docker     (123)     9795 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_pull_requests.py
--rw-r--r--   0 runner    (1001) docker     (123)     4255 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_teams.py
--rw-r--r--   0 runner    (1001) docker     (123)     3647 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_webhooks.py
--rw-r--r--   0 runner    (1001) docker     (123)     8735 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_team.py
--rw-r--r--   0 runner    (1001) docker     (123)     5400 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_tree.py
--rw-r--r--   0 runner    (1001) docker     (123)    11971 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_user.py
--rw-r--r--   0 runner    (1001) docker     (123)     4651 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/get_users.py
--rw-r--r--   0 runner    (1001) docker     (123)    20918 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/issue.py
--rw-r--r--   0 runner    (1001) docker     (123)    13277 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/issue_label.py
--rw-r--r--   0 runner    (1001) docker     (123)     9894 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/membership.py
--rw-r--r--   0 runner    (1001) docker     (123)     6674 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/organization_block.py
--rw-r--r--   0 runner    (1001) docker     (123)     8955 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/organization_project.py
--rw-r--r--   0 runner    (1001) docker     (123)     6958 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/organization_security_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    79808 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/organization_settings.py
--rw-r--r--   0 runner    (1001) docker     (123)    15058 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/organization_webhook.py
--rw-r--r--   0 runner    (1001) docker     (123)    95767 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/outputs.py
--rw-r--r--   0 runner    (1001) docker     (123)    15743 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/project_card.py
--rw-r--r--   0 runner    (1001) docker     (123)     9660 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/project_column.py
--rw-r--r--   0 runner    (1001) docker     (123)    14143 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/provider.py
--rw-r--r--   0 runner    (1001) docker     (123)       43 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/pulumi-plugin.json
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)    28755 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/release.py
--rw-r--r--   0 runner    (1001) docker     (123)   107291 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/repository.py
--rw-r--r--   0 runner    (1001) docker     (123)    17151 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/repository_autolink_reference.py
--rw-r--r--   0 runner    (1001) docker     (123)    20477 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/repository_collaborator.py
--rw-r--r--   0 runner    (1001) docker     (123)    13699 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/repository_deploy_key.py
--rw-r--r--   0 runner    (1001) docker     (123)    17882 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/repository_environment.py
--rw-r--r--   0 runner    (1001) docker     (123)    26214 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/repository_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    17109 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/repository_milestone.py
--rw-r--r--   0 runner    (1001) docker     (123)    11063 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/repository_project.py
--rw-r--r--   0 runner    (1001) docker     (123)    28682 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/repository_pull_request.py
--rw-r--r--   0 runner    (1001) docker     (123)    10676 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/repository_tag_protection.py
--rw-r--r--   0 runner    (1001) docker     (123)    17190 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/repository_webhook.py
--rw-r--r--   0 runner    (1001) docker     (123)    22137 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/team.py
--rw-r--r--   0 runner    (1001) docker     (123)    11019 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/team_members.py
--rw-r--r--   0 runner    (1001) docker     (123)    11623 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/team_membership.py
--rw-r--r--   0 runner    (1001) docker     (123)    14611 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/team_repository.py
--rw-r--r--   0 runner    (1001) docker     (123)    16613 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/team_settings.py
--rw-r--r--   0 runner    (1001) docker     (123)    10810 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/team_sync_group_mapping.py
--rw-r--r--   0 runner    (1001) docker     (123)     9761 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/user_gpg_key.py
--rw-r--r--   0 runner    (1001) docker     (123)     8960 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/user_invitation_accepter.py
--rw-r--r--   0 runner    (1001) docker     (123)     9854 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github/user_ssh_key.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 02:22:59.396641 pulumi_github-5.7.0a1680747500/pulumi_github.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2885 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4418 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/pulumi_github.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 02:22:59.396641 pulumi_github-5.7.0a1680747500/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2124 2023-04-06 02:22:59.000000 pulumi_github-5.7.0a1680747500/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:05.080604 pulumi_github-5.7.0a1680815968/
+-rw-r--r--   0 runner    (1001) docker     (123)     2885 2023-04-06 21:24:05.080604 pulumi_github-5.7.0a1680815968/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2542 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:05.080604 pulumi_github-5.7.0a1680815968/pulumi_github/
+-rw-r--r--   0 runner    (1001) docker     (123)    15450 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    63092 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/_inputs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8081 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/_utilities.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19178 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_environment_secret.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16013 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_environment_variable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9151 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_organization_oidc_subject_claim_customization_template.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20745 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_organization_permissions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22394 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_organization_secret.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10898 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_organization_secret_repositories.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16244 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_organization_variable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9995 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_repository_access_level.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14803 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_repository_oidc_subject_claim_customization_template.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16292 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_repository_permissions.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25998 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_runner_group.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15530 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_secret.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12596 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/actions_variable.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10615 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/app_installation_repositories.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11169 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/app_installation_repository.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16865 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/branch.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12115 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/branch_default.py
+-rw-r--r--   0 runner    (1001) docker     (123)    44058 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/branch_protection.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31972 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/branch_protection_v3.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:05.080604 pulumi_github-5.7.0a1680815968/pulumi_github/config/
+-rw-r--r--   0 runner    (1001) docker     (123)      285 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1069 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/config/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2371 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/config/vars.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18662 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/dependabot_organization_secret.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9223 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/dependabot_organization_secret_repositories.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14359 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/dependabot_secret.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10110 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/emu_group_mapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14476 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/enterprise_organization.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4989 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_environment_secrets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5143 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_environment_variables.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3137 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_organization_oidc_subject_claim_customization_template.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3085 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_organization_public_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3141 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_organization_registration_token.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2549 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_organization_secrets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2611 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_organization_variables.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4327 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_public_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4374 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_registration_token.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5164 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_repository_oidc_subject_claim_customization_template.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4213 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_secrets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4304 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_variables.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4738 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_branch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5236 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_collaborators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3137 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_dependabot_organization_public_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2608 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_dependabot_organization_secrets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3372 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_dependabot_public_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4321 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_dependabot_secrets.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4647 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_enterprise.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2662 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_external_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4071 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_github_app.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14508 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_ip_ranges.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5557 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_membership.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7246 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_organization.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2795 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_organization_ip_allow_list.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2622 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_organization_team_sync_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6941 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_organization_teams.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2574 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_organization_webhooks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4319 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_ref.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13103 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_release.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7590 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_repositories.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20234 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_repository.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6121 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_branches.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3758 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_deploy_keys.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8219 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6319 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_milestone.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11966 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_pull_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9795 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_pull_requests.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4255 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_teams.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3647 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_webhooks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2151 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_ssh_keys.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8735 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_team.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5400 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_tree.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11971 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_user.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5157 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/get_users.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20918 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/issue.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13277 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/issue_label.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9894 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/membership.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6674 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/organization_block.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8955 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/organization_project.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6958 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/organization_security_manager.py
+-rw-r--r--   0 runner    (1001) docker     (123)    79808 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/organization_settings.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15058 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/organization_webhook.py
+-rw-r--r--   0 runner    (1001) docker     (123)   102405 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/outputs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15743 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/project_card.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9660 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/project_column.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14143 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/provider.py
+-rw-r--r--   0 runner    (1001) docker     (123)       43 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/pulumi-plugin.json
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)    28755 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/release.py
+-rw-r--r--   0 runner    (1001) docker     (123)   107291 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16391 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository_autolink_reference.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21061 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository_collaborator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17395 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository_collaborators.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13699 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository_deploy_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17882 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository_environment.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27314 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17109 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository_milestone.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11063 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository_project.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28682 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository_pull_request.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10676 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository_tag_protection.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17190 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/repository_webhook.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22137 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/team.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11019 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/team_members.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11623 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/team_membership.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15177 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/team_repository.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16613 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/team_settings.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10810 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/team_sync_group_mapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9761 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/user_gpg_key.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8960 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/user_invitation_accepter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9854 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/pulumi_github/user_ssh_key.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 21:24:05.080604 pulumi_github-5.7.0a1680815968/pulumi_github.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2885 2023-04-06 21:24:05.000000 pulumi_github-5.7.0a1680815968/pulumi_github.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4599 2023-04-06 21:24:05.000000 pulumi_github-5.7.0a1680815968/pulumi_github.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 21:24:05.000000 pulumi_github-5.7.0a1680815968/pulumi_github.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 21:24:05.000000 pulumi_github-5.7.0a1680815968/pulumi_github.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)       49 2023-04-06 21:24:05.000000 pulumi_github-5.7.0a1680815968/pulumi_github.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-04-06 21:24:05.000000 pulumi_github-5.7.0a1680815968/pulumi_github.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 21:24:05.080604 pulumi_github-5.7.0a1680815968/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2124 2023-04-06 21:24:04.000000 pulumi_github-5.7.0a1680815968/setup.py
```

### Comparing `pulumi_github-5.7.0a1680747500/PKG-INFO` & `pulumi_github-5.7.0a1680815968/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi_github
-Version: 5.7.0a1680747500
+Version: 5.7.0a1680815968
 Summary: A Pulumi package for creating and managing github cloud resources.
 Home-page: https://pulumi.io
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-github
 Keywords: pulumi github
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
```

### Comparing `pulumi_github-5.7.0a1680747500/README.md` & `pulumi_github-5.7.0a1680815968/README.md`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/__init__.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -28,24 +28,26 @@
 from .dependabot_organization_secret_repositories import *
 from .dependabot_secret import *
 from .emu_group_mapping import *
 from .enterprise_organization import *
 from .get_actions_environment_secrets import *
 from .get_actions_environment_variables import *
 from .get_actions_organization_oidc_subject_claim_customization_template import *
+from .get_actions_organization_public_key import *
 from .get_actions_organization_registration_token import *
 from .get_actions_organization_secrets import *
 from .get_actions_organization_variables import *
 from .get_actions_public_key import *
 from .get_actions_registration_token import *
 from .get_actions_repository_oidc_subject_claim_customization_template import *
 from .get_actions_secrets import *
 from .get_actions_variables import *
 from .get_branch import *
 from .get_collaborators import *
+from .get_dependabot_organization_public_key import *
 from .get_dependabot_organization_secrets import *
 from .get_dependabot_public_key import *
 from .get_dependabot_secrets import *
 from .get_enterprise import *
 from .get_external_groups import *
 from .get_github_app import *
 from .get_ip_ranges import *
@@ -63,14 +65,15 @@
 from .get_repository_deploy_keys import *
 from .get_repository_file import *
 from .get_repository_milestone import *
 from .get_repository_pull_request import *
 from .get_repository_pull_requests import *
 from .get_repository_teams import *
 from .get_repository_webhooks import *
+from .get_ssh_keys import *
 from .get_team import *
 from .get_tree import *
 from .get_user import *
 from .get_users import *
 from .issue import *
 from .issue_label import *
 from .membership import *
@@ -82,14 +85,15 @@
 from .project_card import *
 from .project_column import *
 from .provider import *
 from .release import *
 from .repository import *
 from .repository_autolink_reference import *
 from .repository_collaborator import *
+from .repository_collaborators import *
 from .repository_deploy_key import *
 from .repository_environment import *
 from .repository_file import *
 from .repository_milestone import *
 from .repository_project import *
 from .repository_pull_request import *
 from .repository_tag_protection import *
@@ -418,14 +422,22 @@
   "fqn": "pulumi_github",
   "classes": {
    "github:index/repositoryCollaborator:RepositoryCollaborator": "RepositoryCollaborator"
   }
  },
  {
   "pkg": "github",
+  "mod": "index/repositoryCollaborators",
+  "fqn": "pulumi_github",
+  "classes": {
+   "github:index/repositoryCollaborators:RepositoryCollaborators": "RepositoryCollaborators"
+  }
+ },
+ {
+  "pkg": "github",
   "mod": "index/repositoryDeployKey",
   "fqn": "pulumi_github",
   "classes": {
    "github:index/repositoryDeployKey:RepositoryDeployKey": "RepositoryDeployKey"
   }
  },
  {
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/_inputs.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/_inputs.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,18 +12,21 @@
 __all__ = [
     'ActionsOrganizationPermissionsAllowedActionsConfigArgs',
     'ActionsOrganizationPermissionsEnabledRepositoriesConfigArgs',
     'ActionsRepositoryPermissionsAllowedActionsConfigArgs',
     'BranchProtectionRequiredPullRequestReviewArgs',
     'BranchProtectionRequiredStatusCheckArgs',
     'BranchProtectionV3RequiredPullRequestReviewsArgs',
+    'BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowancesArgs',
     'BranchProtectionV3RequiredStatusChecksArgs',
     'BranchProtectionV3RestrictionsArgs',
     'OrganizationWebhookConfigurationArgs',
     'ProviderAppAuthArgs',
+    'RepositoryCollaboratorsTeamArgs',
+    'RepositoryCollaboratorsUserArgs',
     'RepositoryEnvironmentDeploymentBranchPolicyArgs',
     'RepositoryEnvironmentReviewerArgs',
     'RepositoryPagesArgs',
     'RepositoryPagesSourceArgs',
     'RepositorySecurityAndAnalysisArgs',
     'RepositorySecurityAndAnalysisAdvancedSecurityArgs',
     'RepositorySecurityAndAnalysisSecretScanningArgs',
@@ -324,28 +327,32 @@
     def strict(self, value: Optional[pulumi.Input[bool]]):
         pulumi.set(self, "strict", value)
 
 
 @pulumi.input_type
 class BranchProtectionV3RequiredPullRequestReviewsArgs:
     def __init__(__self__, *,
+                 bypass_pull_request_allowances: Optional[pulumi.Input['BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowancesArgs']] = None,
                  dismiss_stale_reviews: Optional[pulumi.Input[bool]] = None,
                  dismissal_teams: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                  dismissal_users: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                  include_admins: Optional[pulumi.Input[bool]] = None,
                  require_code_owner_reviews: Optional[pulumi.Input[bool]] = None,
                  required_approving_review_count: Optional[pulumi.Input[int]] = None):
         """
+        :param pulumi.Input['BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowancesArgs'] bypass_pull_request_allowances: Allow specific users, teams, or apps to bypass pull request requirements. See Bypass Pull Request Allowances below for details.
         :param pulumi.Input[bool] dismiss_stale_reviews: Dismiss approved reviews automatically when a new commit is pushed. Defaults to `false`.
         :param pulumi.Input[Sequence[pulumi.Input[str]]] dismissal_teams: The list of team slugs with dismissal access.
                Always use `slug` of the team, **not** its name. Each team already **has** to have access to the repository.
         :param pulumi.Input[Sequence[pulumi.Input[str]]] dismissal_users: The list of user logins with dismissal access
         :param pulumi.Input[bool] require_code_owner_reviews: Require an approved review in pull requests including files with a designated code owner. Defaults to `false`.
         :param pulumi.Input[int] required_approving_review_count: Require x number of approvals to satisfy branch protection requirements. If this is specified it must be a number between 0-6. This requirement matches GitHub's API, see the upstream [documentation](https://developer.github.com/v3/repos/branches/#parameters-1) for more information.
         """
+        if bypass_pull_request_allowances is not None:
+            pulumi.set(__self__, "bypass_pull_request_allowances", bypass_pull_request_allowances)
         if dismiss_stale_reviews is not None:
             pulumi.set(__self__, "dismiss_stale_reviews", dismiss_stale_reviews)
         if dismissal_teams is not None:
             pulumi.set(__self__, "dismissal_teams", dismissal_teams)
         if dismissal_users is not None:
             pulumi.set(__self__, "dismissal_users", dismissal_users)
         if include_admins is not None:
@@ -355,14 +362,26 @@
             pulumi.set(__self__, "include_admins", include_admins)
         if require_code_owner_reviews is not None:
             pulumi.set(__self__, "require_code_owner_reviews", require_code_owner_reviews)
         if required_approving_review_count is not None:
             pulumi.set(__self__, "required_approving_review_count", required_approving_review_count)
 
     @property
+    @pulumi.getter(name="bypassPullRequestAllowances")
+    def bypass_pull_request_allowances(self) -> Optional[pulumi.Input['BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowancesArgs']]:
+        """
+        Allow specific users, teams, or apps to bypass pull request requirements. See Bypass Pull Request Allowances below for details.
+        """
+        return pulumi.get(self, "bypass_pull_request_allowances")
+
+    @bypass_pull_request_allowances.setter
+    def bypass_pull_request_allowances(self, value: Optional[pulumi.Input['BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowancesArgs']]):
+        pulumi.set(self, "bypass_pull_request_allowances", value)
+
+    @property
     @pulumi.getter(name="dismissStaleReviews")
     def dismiss_stale_reviews(self) -> Optional[pulumi.Input[bool]]:
         """
         Dismiss approved reviews automatically when a new commit is pushed. Defaults to `false`.
         """
         return pulumi.get(self, "dismiss_stale_reviews")
 
@@ -426,14 +445,69 @@
 
     @required_approving_review_count.setter
     def required_approving_review_count(self, value: Optional[pulumi.Input[int]]):
         pulumi.set(self, "required_approving_review_count", value)
 
 
 @pulumi.input_type
+class BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowancesArgs:
+    def __init__(__self__, *,
+                 apps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
+                 teams: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
+                 users: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
+        """
+        :param pulumi.Input[Sequence[pulumi.Input[str]]] apps: The list of app slugs allowed to bypass pull request requirements.
+        :param pulumi.Input[Sequence[pulumi.Input[str]]] teams: The list of team slugs allowed to bypass pull request requirements.
+        :param pulumi.Input[Sequence[pulumi.Input[str]]] users: The list of user logins allowed to bypass pull request requirements.
+        """
+        if apps is not None:
+            pulumi.set(__self__, "apps", apps)
+        if teams is not None:
+            pulumi.set(__self__, "teams", teams)
+        if users is not None:
+            pulumi.set(__self__, "users", users)
+
+    @property
+    @pulumi.getter
+    def apps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
+        """
+        The list of app slugs allowed to bypass pull request requirements.
+        """
+        return pulumi.get(self, "apps")
+
+    @apps.setter
+    def apps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
+        pulumi.set(self, "apps", value)
+
+    @property
+    @pulumi.getter
+    def teams(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
+        """
+        The list of team slugs allowed to bypass pull request requirements.
+        """
+        return pulumi.get(self, "teams")
+
+    @teams.setter
+    def teams(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
+        pulumi.set(self, "teams", value)
+
+    @property
+    @pulumi.getter
+    def users(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
+        """
+        The list of user logins allowed to bypass pull request requirements.
+        """
+        return pulumi.get(self, "users")
+
+    @users.setter
+    def users(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
+        pulumi.set(self, "users", value)
+
+
+@pulumi.input_type
 class BranchProtectionV3RequiredStatusChecksArgs:
     def __init__(__self__, *,
                  checks: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                  contexts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                  include_admins: Optional[pulumi.Input[bool]] = None,
                  strict: Optional[pulumi.Input[bool]] = None):
         """
@@ -652,14 +726,90 @@
 
     @pem_file.setter
     def pem_file(self, value: pulumi.Input[str]):
         pulumi.set(self, "pem_file", value)
 
 
 @pulumi.input_type
+class RepositoryCollaboratorsTeamArgs:
+    def __init__(__self__, *,
+                 team_id: pulumi.Input[str],
+                 permission: Optional[pulumi.Input[str]] = None):
+        """
+        :param pulumi.Input[str] permission: The permission of the outside collaborators for the repository.
+               Must be one of `pull`, `triage`, `push`, `maintain`, `admin` or the name of an existing [custom repository role](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization) within the organisation. Defaults to `pull`.
+               Must be `push` for personal repositories. Defaults to `push`.
+        """
+        pulumi.set(__self__, "team_id", team_id)
+        if permission is not None:
+            pulumi.set(__self__, "permission", permission)
+
+    @property
+    @pulumi.getter(name="teamId")
+    def team_id(self) -> pulumi.Input[str]:
+        return pulumi.get(self, "team_id")
+
+    @team_id.setter
+    def team_id(self, value: pulumi.Input[str]):
+        pulumi.set(self, "team_id", value)
+
+    @property
+    @pulumi.getter
+    def permission(self) -> Optional[pulumi.Input[str]]:
+        """
+        The permission of the outside collaborators for the repository.
+        Must be one of `pull`, `triage`, `push`, `maintain`, `admin` or the name of an existing [custom repository role](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization) within the organisation. Defaults to `pull`.
+        Must be `push` for personal repositories. Defaults to `push`.
+        """
+        return pulumi.get(self, "permission")
+
+    @permission.setter
+    def permission(self, value: Optional[pulumi.Input[str]]):
+        pulumi.set(self, "permission", value)
+
+
+@pulumi.input_type
+class RepositoryCollaboratorsUserArgs:
+    def __init__(__self__, *,
+                 username: pulumi.Input[str],
+                 permission: Optional[pulumi.Input[str]] = None):
+        """
+        :param pulumi.Input[str] permission: The permission of the outside collaborators for the repository.
+               Must be one of `pull`, `push`, `maintain`, `triage` or `admin` or the name of an existing [custom repository role](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization) within the organization for organization-owned repositories.
+               Must be `push` for personal repositories. Defaults to `push`.
+        """
+        pulumi.set(__self__, "username", username)
+        if permission is not None:
+            pulumi.set(__self__, "permission", permission)
+
+    @property
+    @pulumi.getter
+    def username(self) -> pulumi.Input[str]:
+        return pulumi.get(self, "username")
+
+    @username.setter
+    def username(self, value: pulumi.Input[str]):
+        pulumi.set(self, "username", value)
+
+    @property
+    @pulumi.getter
+    def permission(self) -> Optional[pulumi.Input[str]]:
+        """
+        The permission of the outside collaborators for the repository.
+        Must be one of `pull`, `push`, `maintain`, `triage` or `admin` or the name of an existing [custom repository role](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization) within the organization for organization-owned repositories.
+        Must be `push` for personal repositories. Defaults to `push`.
+        """
+        return pulumi.get(self, "permission")
+
+    @permission.setter
+    def permission(self, value: Optional[pulumi.Input[str]]):
+        pulumi.set(self, "permission", value)
+
+
+@pulumi.input_type
 class RepositoryEnvironmentDeploymentBranchPolicyArgs:
     def __init__(__self__, *,
                  custom_branch_policies: pulumi.Input[bool],
                  protected_branches: pulumi.Input[bool]):
         """
         :param pulumi.Input[bool] custom_branch_policies: Whether only branches that match the specified name patterns can deploy to this environment.
         :param pulumi.Input[bool] protected_branches: Whether only branches with branch protection rules can deploy to this environment.
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/_utilities.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/_utilities.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_environment_secret.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_environment_secret.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_environment_variable.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_environment_variable.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_organization_oidc_subject_claim_customization_template.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_organization_oidc_subject_claim_customization_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_organization_permissions.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_organization_permissions.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_organization_secret.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_organization_secret.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_organization_secret_repositories.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_organization_secret_repositories.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_organization_variable.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_organization_variable.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_repository_access_level.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_repository_access_level.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_repository_oidc_subject_claim_customization_template.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_repository_oidc_subject_claim_customization_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_repository_permissions.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_repository_permissions.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_runner_group.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_runner_group.py`

 * *Files 9% similar despite different names*

```diff
@@ -12,26 +12,34 @@
 __all__ = ['ActionsRunnerGroupArgs', 'ActionsRunnerGroup']
 
 @pulumi.input_type
 class ActionsRunnerGroupArgs:
     def __init__(__self__, *,
                  visibility: pulumi.Input[str],
                  name: Optional[pulumi.Input[str]] = None,
-                 selected_repository_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None):
+                 restricted_to_workflows: Optional[pulumi.Input[bool]] = None,
+                 selected_repository_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
+                 selected_workflows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
         """
         The set of arguments for constructing a ActionsRunnerGroup resource.
         :param pulumi.Input[str] visibility: Visibility of a runner group. Whether the runner group can include `all`, `selected`, or `private` repositories. A value of `private` is not currently supported due to limitations in the GitHub API.
         :param pulumi.Input[str] name: Name of the runner group
+        :param pulumi.Input[bool] restricted_to_workflows: If true, the runner group will be restricted to running only the workflows specified in the selected_workflows array. Defaults to false.
         :param pulumi.Input[Sequence[pulumi.Input[int]]] selected_repository_ids: IDs of the repositories which should be added to the runner group
+        :param pulumi.Input[Sequence[pulumi.Input[str]]] selected_workflows: List of workflows the runner group should be allowed to run. This setting will be ignored unless restricted_to_workflows is set to true.
         """
         pulumi.set(__self__, "visibility", visibility)
         if name is not None:
             pulumi.set(__self__, "name", name)
+        if restricted_to_workflows is not None:
+            pulumi.set(__self__, "restricted_to_workflows", restricted_to_workflows)
         if selected_repository_ids is not None:
             pulumi.set(__self__, "selected_repository_ids", selected_repository_ids)
+        if selected_workflows is not None:
+            pulumi.set(__self__, "selected_workflows", selected_workflows)
 
     @property
     @pulumi.getter
     def visibility(self) -> pulumi.Input[str]:
         """
         Visibility of a runner group. Whether the runner group can include `all`, `selected`, or `private` repositories. A value of `private` is not currently supported due to limitations in the GitHub API.
         """
@@ -50,25 +58,49 @@
         return pulumi.get(self, "name")
 
     @name.setter
     def name(self, value: Optional[pulumi.Input[str]]):
         pulumi.set(self, "name", value)
 
     @property
+    @pulumi.getter(name="restrictedToWorkflows")
+    def restricted_to_workflows(self) -> Optional[pulumi.Input[bool]]:
+        """
+        If true, the runner group will be restricted to running only the workflows specified in the selected_workflows array. Defaults to false.
+        """
+        return pulumi.get(self, "restricted_to_workflows")
+
+    @restricted_to_workflows.setter
+    def restricted_to_workflows(self, value: Optional[pulumi.Input[bool]]):
+        pulumi.set(self, "restricted_to_workflows", value)
+
+    @property
     @pulumi.getter(name="selectedRepositoryIds")
     def selected_repository_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
         """
         IDs of the repositories which should be added to the runner group
         """
         return pulumi.get(self, "selected_repository_ids")
 
     @selected_repository_ids.setter
     def selected_repository_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
         pulumi.set(self, "selected_repository_ids", value)
 
+    @property
+    @pulumi.getter(name="selectedWorkflows")
+    def selected_workflows(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
+        """
+        List of workflows the runner group should be allowed to run. This setting will be ignored unless restricted_to_workflows is set to true.
+        """
+        return pulumi.get(self, "selected_workflows")
+
+    @selected_workflows.setter
+    def selected_workflows(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
+        pulumi.set(self, "selected_workflows", value)
+
 
 @pulumi.input_type
 class _ActionsRunnerGroupState:
     def __init__(__self__, *,
                  allows_public_repositories: Optional[pulumi.Input[bool]] = None,
                  default: Optional[pulumi.Input[bool]] = None,
                  etag: Optional[pulumi.Input[str]] = None,
@@ -252,15 +284,17 @@
 
 class ActionsRunnerGroup(pulumi.CustomResource):
     @overload
     def __init__(__self__,
                  resource_name: str,
                  opts: Optional[pulumi.ResourceOptions] = None,
                  name: Optional[pulumi.Input[str]] = None,
+                 restricted_to_workflows: Optional[pulumi.Input[bool]] = None,
                  selected_repository_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
+                 selected_workflows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                  visibility: Optional[pulumi.Input[str]] = None,
                  __props__=None):
         """
         This resource allows you to create and manage GitHub Actions runner groups within your GitHub enterprise organizations.
         You must have admin access to an organization to use this resource.
 
         ## Example Usage
@@ -282,15 +316,17 @@
         ```sh
          $ pulumi import github:index/actionsRunnerGroup:ActionsRunnerGroup test 7
         ```
 
         :param str resource_name: The name of the resource.
         :param pulumi.ResourceOptions opts: Options for the resource.
         :param pulumi.Input[str] name: Name of the runner group
+        :param pulumi.Input[bool] restricted_to_workflows: If true, the runner group will be restricted to running only the workflows specified in the selected_workflows array. Defaults to false.
         :param pulumi.Input[Sequence[pulumi.Input[int]]] selected_repository_ids: IDs of the repositories which should be added to the runner group
+        :param pulumi.Input[Sequence[pulumi.Input[str]]] selected_workflows: List of workflows the runner group should be allowed to run. This setting will be ignored unless restricted_to_workflows is set to true.
         :param pulumi.Input[str] visibility: Visibility of a runner group. Whether the runner group can include `all`, `selected`, or `private` repositories. A value of `private` is not currently supported due to limitations in the GitHub API.
         """
         ...
     @overload
     def __init__(__self__,
                  resource_name: str,
                  args: ActionsRunnerGroupArgs,
@@ -331,38 +367,40 @@
         else:
             __self__._internal_init(resource_name, *args, **kwargs)
 
     def _internal_init(__self__,
                  resource_name: str,
                  opts: Optional[pulumi.ResourceOptions] = None,
                  name: Optional[pulumi.Input[str]] = None,
+                 restricted_to_workflows: Optional[pulumi.Input[bool]] = None,
                  selected_repository_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
+                 selected_workflows: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                  visibility: Optional[pulumi.Input[str]] = None,
                  __props__=None):
         opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
         if not isinstance(opts, pulumi.ResourceOptions):
             raise TypeError('Expected resource options to be a ResourceOptions instance')
         if opts.id is None:
             if __props__ is not None:
                 raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
             __props__ = ActionsRunnerGroupArgs.__new__(ActionsRunnerGroupArgs)
 
             __props__.__dict__["name"] = name
+            __props__.__dict__["restricted_to_workflows"] = restricted_to_workflows
             __props__.__dict__["selected_repository_ids"] = selected_repository_ids
+            __props__.__dict__["selected_workflows"] = selected_workflows
             if visibility is None and not opts.urn:
                 raise TypeError("Missing required property 'visibility'")
             __props__.__dict__["visibility"] = visibility
             __props__.__dict__["allows_public_repositories"] = None
             __props__.__dict__["default"] = None
             __props__.__dict__["etag"] = None
             __props__.__dict__["inherited"] = None
-            __props__.__dict__["restricted_to_workflows"] = None
             __props__.__dict__["runners_url"] = None
             __props__.__dict__["selected_repositories_url"] = None
-            __props__.__dict__["selected_workflows"] = None
         super(ActionsRunnerGroup, __self__).__init__(
             'github:index/actionsRunnerGroup:ActionsRunnerGroup',
             resource_name,
             __props__,
             opts)
 
     @staticmethod
@@ -454,15 +492,15 @@
         """
         Name of the runner group
         """
         return pulumi.get(self, "name")
 
     @property
     @pulumi.getter(name="restrictedToWorkflows")
-    def restricted_to_workflows(self) -> pulumi.Output[bool]:
+    def restricted_to_workflows(self) -> pulumi.Output[Optional[bool]]:
         """
         If true, the runner group will be restricted to running only the workflows specified in the selected_workflows array. Defaults to false.
         """
         return pulumi.get(self, "restricted_to_workflows")
 
     @property
     @pulumi.getter(name="runnersUrl")
@@ -486,15 +524,15 @@
         """
         IDs of the repositories which should be added to the runner group
         """
         return pulumi.get(self, "selected_repository_ids")
 
     @property
     @pulumi.getter(name="selectedWorkflows")
-    def selected_workflows(self) -> pulumi.Output[Sequence[str]]:
+    def selected_workflows(self) -> pulumi.Output[Optional[Sequence[str]]]:
         """
         List of workflows the runner group should be allowed to run. This setting will be ignored unless restricted_to_workflows is set to true.
         """
         return pulumi.get(self, "selected_workflows")
 
     @property
     @pulumi.getter
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_secret.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_secret.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/actions_variable.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/actions_variable.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/app_installation_repositories.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/app_installation_repositories.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/app_installation_repository.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/app_installation_repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/branch.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/branch.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/branch_default.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/branch_default.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/branch_protection.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/branch_protection.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/branch_protection_v3.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/branch_protection_v3.py`

 * *Files 1% similar despite different names*

```diff
@@ -334,28 +334,33 @@
         ```python
         import pulumi
         import pulumi_github as github
 
         example_repository = github.Repository("exampleRepository")
         example_team = github.Team("exampleTeam")
         # Protect the main branch of the foo repository. Additionally, require that
-        # the "ci/check" check ran by the Github Actions app is passing and only allow 
+        # the "ci/check" check ran by the Github Actions app is passing and only allow
         # the engineers team merge to the branch.
         example_branch_protection_v3 = github.BranchProtectionV3("exampleBranchProtectionV3",
             repository=example_repository.name,
             branch="main",
             enforce_admins=True,
             required_status_checks=github.BranchProtectionV3RequiredStatusChecksArgs(
                 strict=False,
                 checks=["ci/check:824642007264"],
             ),
             required_pull_request_reviews=github.BranchProtectionV3RequiredPullRequestReviewsArgs(
                 dismiss_stale_reviews=True,
                 dismissal_users=["foo-user"],
                 dismissal_teams=[example_team.slug],
+                bypass_pull_request_allowances=github.BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowancesArgs(
+                    users=["foo-user"],
+                    teams=[example_team.slug],
+                    apps=["foo-app"],
+                ),
             ),
             restrictions=github.BranchProtectionV3RestrictionsArgs(
                 users=["foo-user"],
                 teams=[example_team.slug],
                 apps=["foo-app"],
             ))
         example_team_repository = github.TeamRepository("exampleTeamRepository",
@@ -414,28 +419,33 @@
         ```python
         import pulumi
         import pulumi_github as github
 
         example_repository = github.Repository("exampleRepository")
         example_team = github.Team("exampleTeam")
         # Protect the main branch of the foo repository. Additionally, require that
-        # the "ci/check" check ran by the Github Actions app is passing and only allow 
+        # the "ci/check" check ran by the Github Actions app is passing and only allow
         # the engineers team merge to the branch.
         example_branch_protection_v3 = github.BranchProtectionV3("exampleBranchProtectionV3",
             repository=example_repository.name,
             branch="main",
             enforce_admins=True,
             required_status_checks=github.BranchProtectionV3RequiredStatusChecksArgs(
                 strict=False,
                 checks=["ci/check:824642007264"],
             ),
             required_pull_request_reviews=github.BranchProtectionV3RequiredPullRequestReviewsArgs(
                 dismiss_stale_reviews=True,
                 dismissal_users=["foo-user"],
                 dismissal_teams=[example_team.slug],
+                bypass_pull_request_allowances=github.BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowancesArgs(
+                    users=["foo-user"],
+                    teams=[example_team.slug],
+                    apps=["foo-app"],
+                ),
             ),
             restrictions=github.BranchProtectionV3RestrictionsArgs(
                 users=["foo-user"],
                 teams=[example_team.slug],
                 apps=["foo-app"],
             ))
         example_team_repository = github.TeamRepository("exampleTeamRepository",
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/config/outputs.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/config/outputs.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/config/vars.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/config/vars.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/dependabot_organization_secret.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/dependabot_organization_secret.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/dependabot_organization_secret_repositories.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/dependabot_organization_secret_repositories.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/dependabot_secret.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/dependabot_secret.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/emu_group_mapping.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/emu_group_mapping.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/enterprise_organization.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/enterprise_organization.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_environment_secrets.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_environment_secrets.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_environment_variables.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_environment_variables.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_organization_oidc_subject_claim_customization_template.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_organization_oidc_subject_claim_customization_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_organization_registration_token.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_organization_registration_token.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_organization_secrets.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_organization_secrets.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_organization_variables.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_organization_variables.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_public_key.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_public_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_registration_token.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_registration_token.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_repository_oidc_subject_claim_customization_template.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_repository_oidc_subject_claim_customization_template.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_secrets.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_secrets.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_actions_variables.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_actions_variables.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_branch.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_branch.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_collaborators.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_collaborators.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_dependabot_organization_secrets.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_dependabot_organization_secrets.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_dependabot_public_key.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_dependabot_public_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_dependabot_secrets.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_dependabot_secrets.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_enterprise.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_enterprise.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_external_groups.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_external_groups.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_github_app.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_github_app.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_ip_ranges.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_ip_ranges.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_membership.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_membership.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_organization.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_organization.py`

 * *Files 12% similar despite different names*

```diff
@@ -17,26 +17,30 @@
 ]
 
 @pulumi.output_type
 class GetOrganizationResult:
     """
     A collection of values returned by getOrganization.
     """
-    def __init__(__self__, description=None, id=None, login=None, members=None, name=None, node_id=None, orgname=None, plan=None, repositories=None):
+    def __init__(__self__, description=None, id=None, login=None, members=None, name=None, node_id=None, orgname=None, plan=None, repositories=None, users=None):
         if description and not isinstance(description, str):
             raise TypeError("Expected argument 'description' to be a str")
         pulumi.set(__self__, "description", description)
         if id and not isinstance(id, str):
             raise TypeError("Expected argument 'id' to be a str")
         pulumi.set(__self__, "id", id)
         if login and not isinstance(login, str):
             raise TypeError("Expected argument 'login' to be a str")
         pulumi.set(__self__, "login", login)
         if members and not isinstance(members, list):
             raise TypeError("Expected argument 'members' to be a list")
+        if members is not None:
+            warnings.warn("""Use `users` instead by replacing `github_organization.example.members` to `github_organization.example.users[*].login`. Expect this field to be removed in next major version.""", DeprecationWarning)
+            pulumi.log.warn("""members is deprecated: Use `users` instead by replacing `github_organization.example.members` to `github_organization.example.users[*].login`. Expect this field to be removed in next major version.""")
+
         pulumi.set(__self__, "members", members)
         if name and not isinstance(name, str):
             raise TypeError("Expected argument 'name' to be a str")
         pulumi.set(__self__, "name", name)
         if node_id and not isinstance(node_id, str):
             raise TypeError("Expected argument 'node_id' to be a str")
         pulumi.set(__self__, "node_id", node_id)
@@ -45,14 +49,17 @@
         pulumi.set(__self__, "orgname", orgname)
         if plan and not isinstance(plan, str):
             raise TypeError("Expected argument 'plan' to be a str")
         pulumi.set(__self__, "plan", plan)
         if repositories and not isinstance(repositories, list):
             raise TypeError("Expected argument 'repositories' to be a list")
         pulumi.set(__self__, "repositories", repositories)
+        if users and not isinstance(users, list):
+            raise TypeError("Expected argument 'users' to be a list")
+        pulumi.set(__self__, "users", users)
 
     @property
     @pulumi.getter
     def description(self) -> str:
         """
         The description the organization account
         """
@@ -66,23 +73,23 @@
         """
         return pulumi.get(self, "id")
 
     @property
     @pulumi.getter
     def login(self) -> str:
         """
-        The login of the organization account
+        The members login
         """
         return pulumi.get(self, "login")
 
     @property
     @pulumi.getter
     def members(self) -> Sequence[str]:
         """
-        (`list`) A list with the members of the organization
+        **Deprecated**: use `users` instead by replacing `github_organization.example.members` to `github_organization.example.users[*].login` which will give you the same value, expect this field to be removed in next major version
         """
         return pulumi.get(self, "members")
 
     @property
     @pulumi.getter
     def name(self) -> str:
         """
@@ -118,14 +125,22 @@
     @pulumi.getter
     def repositories(self) -> Sequence[str]:
         """
         (`list`) A list with the repositories on the organization
         """
         return pulumi.get(self, "repositories")
 
+    @property
+    @pulumi.getter
+    def users(self) -> Sequence[Mapping[str, str]]:
+        """
+        (`list`) A list with the members of the organization with following fields:
+        """
+        return pulumi.get(self, "users")
+
 
 class AwaitableGetOrganizationResult(GetOrganizationResult):
     # pylint: disable=using-constant-test
     def __await__(self):
         if False:
             yield self
         return GetOrganizationResult(
@@ -133,15 +148,16 @@
             id=self.id,
             login=self.login,
             members=self.members,
             name=self.name,
             node_id=self.node_id,
             orgname=self.orgname,
             plan=self.plan,
-            repositories=self.repositories)
+            repositories=self.repositories,
+            users=self.users)
 
 
 def get_organization(name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationResult:
     """
     Use this data source to retrieve basic information about a GitHub Organization.
 
@@ -167,15 +183,16 @@
         id=__ret__.id,
         login=__ret__.login,
         members=__ret__.members,
         name=__ret__.name,
         node_id=__ret__.node_id,
         orgname=__ret__.orgname,
         plan=__ret__.plan,
-        repositories=__ret__.repositories)
+        repositories=__ret__.repositories,
+        users=__ret__.users)
 
 
 @_utilities.lift_output_func(get_organization)
 def get_organization_output(name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrganizationResult]:
     """
     Use this data source to retrieve basic information about a GitHub Organization.
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_organization_ip_allow_list.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_organization_ip_allow_list.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_organization_team_sync_groups.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_organization_team_sync_groups.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_organization_teams.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_organization_teams.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_organization_webhooks.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_organization_webhooks.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_ref.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_ref.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_release.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_release.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_repositories.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_repositories.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_repository.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_branches.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_branches.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_deploy_keys.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_deploy_keys.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_file.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_file.py`

 * *Files 6% similar despite different names*

```diff
@@ -17,15 +17,15 @@
 ]
 
 @pulumi.output_type
 class GetRepositoryFileResult:
     """
     A collection of values returned by getRepositoryFile.
     """
-    def __init__(__self__, branch=None, commit_author=None, commit_email=None, commit_message=None, commit_sha=None, content=None, file=None, id=None, repository=None, sha=None):
+    def __init__(__self__, branch=None, commit_author=None, commit_email=None, commit_message=None, commit_sha=None, content=None, file=None, id=None, ref=None, repository=None, sha=None):
         if branch and not isinstance(branch, str):
             raise TypeError("Expected argument 'branch' to be a str")
         pulumi.set(__self__, "branch", branch)
         if commit_author and not isinstance(commit_author, str):
             raise TypeError("Expected argument 'commit_author' to be a str")
         pulumi.set(__self__, "commit_author", commit_author)
         if commit_email and not isinstance(commit_email, str):
@@ -42,14 +42,17 @@
         pulumi.set(__self__, "content", content)
         if file and not isinstance(file, str):
             raise TypeError("Expected argument 'file' to be a str")
         pulumi.set(__self__, "file", file)
         if id and not isinstance(id, str):
             raise TypeError("Expected argument 'id' to be a str")
         pulumi.set(__self__, "id", id)
+        if ref and not isinstance(ref, str):
+            raise TypeError("Expected argument 'ref' to be a str")
+        pulumi.set(__self__, "ref", ref)
         if repository and not isinstance(repository, str):
             raise TypeError("Expected argument 'repository' to be a str")
         pulumi.set(__self__, "repository", repository)
         if sha and not isinstance(sha, str):
             raise TypeError("Expected argument 'sha' to be a str")
         pulumi.set(__self__, "sha", sha)
 
@@ -109,14 +112,22 @@
         """
         The provider-assigned unique ID for this managed resource.
         """
         return pulumi.get(self, "id")
 
     @property
     @pulumi.getter
+    def ref(self) -> str:
+        """
+        The name of the commit/branch/tag.
+        """
+        return pulumi.get(self, "ref")
+
+    @property
+    @pulumi.getter
     def repository(self) -> str:
         return pulumi.get(self, "repository")
 
     @property
     @pulumi.getter
     def sha(self) -> str:
         """
@@ -135,14 +146,15 @@
             commit_author=self.commit_author,
             commit_email=self.commit_email,
             commit_message=self.commit_message,
             commit_sha=self.commit_sha,
             content=self.content,
             file=self.file,
             id=self.id,
+            ref=self.ref,
             repository=self.repository,
             sha=self.sha)
 
 
 def get_repository_file(branch: Optional[str] = None,
                         file: Optional[str] = None,
                         repository: Optional[str] = None,
@@ -159,16 +171,16 @@
 
     foo = github.get_repository_file(repository=github_repository["foo"]["name"],
         branch="main",
         file=".gitignore")
     ```
 
 
-    :param str branch: Git branch. Defaults to `main`.
-    :param str file: The path of the file to manage.
+    :param str branch: Git branch. Defaults to the repository's default branch.
+    :param str file: The path of the file to read.
     :param str repository: The repository to read the file from. If an unqualified repo name (without an owner) is passed, the owner will be inferred from the owner of the token used to execute the plan. If a name of the type "owner/repo" (with a slash in the middle) is passed, the owner will be as specified and not the owner of the token.
     """
     __args__ = dict()
     __args__['branch'] = branch
     __args__['file'] = file
     __args__['repository'] = repository
     opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
@@ -179,14 +191,15 @@
         commit_author=__ret__.commit_author,
         commit_email=__ret__.commit_email,
         commit_message=__ret__.commit_message,
         commit_sha=__ret__.commit_sha,
         content=__ret__.content,
         file=__ret__.file,
         id=__ret__.id,
+        ref=__ret__.ref,
         repository=__ret__.repository,
         sha=__ret__.sha)
 
 
 @_utilities.lift_output_func(get_repository_file)
 def get_repository_file_output(branch: Optional[pulumi.Input[Optional[str]]] = None,
                                file: Optional[pulumi.Input[str]] = None,
@@ -204,12 +217,12 @@
 
     foo = github.get_repository_file(repository=github_repository["foo"]["name"],
         branch="main",
         file=".gitignore")
     ```
 
 
-    :param str branch: Git branch. Defaults to `main`.
-    :param str file: The path of the file to manage.
+    :param str branch: Git branch. Defaults to the repository's default branch.
+    :param str file: The path of the file to read.
     :param str repository: The repository to read the file from. If an unqualified repo name (without an owner) is passed, the owner will be inferred from the owner of the token used to execute the plan. If a name of the type "owner/repo" (with a slash in the middle) is passed, the owner will be as specified and not the owner of the token.
     """
     ...
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_milestone.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_milestone.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_pull_request.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_pull_request.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_pull_requests.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_pull_requests.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_teams.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_teams.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_repository_webhooks.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_repository_webhooks.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_team.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_team.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_tree.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_tree.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_user.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_user.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/get_users.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/get_users.py`

 * *Files 20% similar despite different names*

```diff
@@ -17,15 +17,18 @@
 ]
 
 @pulumi.output_type
 class GetUsersResult:
     """
     A collection of values returned by getUsers.
     """
-    def __init__(__self__, id=None, logins=None, node_ids=None, unknown_logins=None, usernames=None):
+    def __init__(__self__, emails=None, id=None, logins=None, node_ids=None, unknown_logins=None, usernames=None):
+        if emails and not isinstance(emails, list):
+            raise TypeError("Expected argument 'emails' to be a list")
+        pulumi.set(__self__, "emails", emails)
         if id and not isinstance(id, str):
             raise TypeError("Expected argument 'id' to be a str")
         pulumi.set(__self__, "id", id)
         if logins and not isinstance(logins, list):
             raise TypeError("Expected argument 'logins' to be a list")
         pulumi.set(__self__, "logins", logins)
         if node_ids and not isinstance(node_ids, list):
@@ -36,14 +39,22 @@
         pulumi.set(__self__, "unknown_logins", unknown_logins)
         if usernames and not isinstance(usernames, list):
             raise TypeError("Expected argument 'usernames' to be a list")
         pulumi.set(__self__, "usernames", usernames)
 
     @property
     @pulumi.getter
+    def emails(self) -> Sequence[str]:
+        """
+        list of the user's publicly visible profile email (will be empty string in case if user decided not to show it).
+        """
+        return pulumi.get(self, "emails")
+
+    @property
+    @pulumi.getter
     def id(self) -> str:
         """
         The provider-assigned unique ID for this managed resource.
         """
         return pulumi.get(self, "id")
 
     @property
@@ -78,14 +89,15 @@
 
 class AwaitableGetUsersResult(GetUsersResult):
     # pylint: disable=using-constant-test
     def __await__(self):
         if False:
             yield self
         return GetUsersResult(
+            emails=self.emails,
             id=self.id,
             logins=self.logins,
             node_ids=self.node_ids,
             unknown_logins=self.unknown_logins,
             usernames=self.usernames)
 
 
@@ -114,14 +126,15 @@
     """
     __args__ = dict()
     __args__['usernames'] = usernames
     opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
     __ret__ = pulumi.runtime.invoke('github:index/getUsers:getUsers', __args__, opts=opts, typ=GetUsersResult).value
 
     return AwaitableGetUsersResult(
+        emails=__ret__.emails,
         id=__ret__.id,
         logins=__ret__.logins,
         node_ids=__ret__.node_ids,
         unknown_logins=__ret__.unknown_logins,
         usernames=__ret__.usernames)
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/issue.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/issue.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/issue_label.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/issue_label.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/membership.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/membership.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/organization_block.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/organization_block.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/organization_project.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/organization_project.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/organization_security_manager.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/organization_security_manager.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/organization_settings.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/organization_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/organization_webhook.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/organization_webhook.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/outputs.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/outputs.py`

 * *Files 3% similar despite different names*

```diff
@@ -13,17 +13,20 @@
 __all__ = [
     'ActionsOrganizationPermissionsAllowedActionsConfig',
     'ActionsOrganizationPermissionsEnabledRepositoriesConfig',
     'ActionsRepositoryPermissionsAllowedActionsConfig',
     'BranchProtectionRequiredPullRequestReview',
     'BranchProtectionRequiredStatusCheck',
     'BranchProtectionV3RequiredPullRequestReviews',
+    'BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowances',
     'BranchProtectionV3RequiredStatusChecks',
     'BranchProtectionV3Restrictions',
     'OrganizationWebhookConfiguration',
+    'RepositoryCollaboratorsTeam',
+    'RepositoryCollaboratorsUser',
     'RepositoryEnvironmentDeploymentBranchPolicy',
     'RepositoryEnvironmentReviewer',
     'RepositoryPages',
     'RepositoryPagesSource',
     'RepositorySecurityAndAnalysis',
     'RepositorySecurityAndAnalysisAdvancedSecurity',
     'RepositorySecurityAndAnalysisSecretScanning',
@@ -374,15 +377,17 @@
 
 
 @pulumi.output_type
 class BranchProtectionV3RequiredPullRequestReviews(dict):
     @staticmethod
     def __key_warning(key: str):
         suggest = None
-        if key == "dismissStaleReviews":
+        if key == "bypassPullRequestAllowances":
+            suggest = "bypass_pull_request_allowances"
+        elif key == "dismissStaleReviews":
             suggest = "dismiss_stale_reviews"
         elif key == "dismissalTeams":
             suggest = "dismissal_teams"
         elif key == "dismissalUsers":
             suggest = "dismissal_users"
         elif key == "includeAdmins":
             suggest = "include_admins"
@@ -399,42 +404,54 @@
         return super().__getitem__(key)
 
     def get(self, key: str, default = None) -> Any:
         BranchProtectionV3RequiredPullRequestReviews.__key_warning(key)
         return super().get(key, default)
 
     def __init__(__self__, *,
+                 bypass_pull_request_allowances: Optional['outputs.BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowances'] = None,
                  dismiss_stale_reviews: Optional[bool] = None,
                  dismissal_teams: Optional[Sequence[str]] = None,
                  dismissal_users: Optional[Sequence[str]] = None,
                  include_admins: Optional[bool] = None,
                  require_code_owner_reviews: Optional[bool] = None,
                  required_approving_review_count: Optional[int] = None):
         """
+        :param 'BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowancesArgs' bypass_pull_request_allowances: Allow specific users, teams, or apps to bypass pull request requirements. See Bypass Pull Request Allowances below for details.
         :param bool dismiss_stale_reviews: Dismiss approved reviews automatically when a new commit is pushed. Defaults to `false`.
         :param Sequence[str] dismissal_teams: The list of team slugs with dismissal access.
                Always use `slug` of the team, **not** its name. Each team already **has** to have access to the repository.
         :param Sequence[str] dismissal_users: The list of user logins with dismissal access
         :param bool require_code_owner_reviews: Require an approved review in pull requests including files with a designated code owner. Defaults to `false`.
         :param int required_approving_review_count: Require x number of approvals to satisfy branch protection requirements. If this is specified it must be a number between 0-6. This requirement matches GitHub's API, see the upstream [documentation](https://developer.github.com/v3/repos/branches/#parameters-1) for more information.
         """
+        if bypass_pull_request_allowances is not None:
+            pulumi.set(__self__, "bypass_pull_request_allowances", bypass_pull_request_allowances)
         if dismiss_stale_reviews is not None:
             pulumi.set(__self__, "dismiss_stale_reviews", dismiss_stale_reviews)
         if dismissal_teams is not None:
             pulumi.set(__self__, "dismissal_teams", dismissal_teams)
         if dismissal_users is not None:
             pulumi.set(__self__, "dismissal_users", dismissal_users)
         if include_admins is not None:
             pulumi.set(__self__, "include_admins", include_admins)
         if require_code_owner_reviews is not None:
             pulumi.set(__self__, "require_code_owner_reviews", require_code_owner_reviews)
         if required_approving_review_count is not None:
             pulumi.set(__self__, "required_approving_review_count", required_approving_review_count)
 
     @property
+    @pulumi.getter(name="bypassPullRequestAllowances")
+    def bypass_pull_request_allowances(self) -> Optional['outputs.BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowances']:
+        """
+        Allow specific users, teams, or apps to bypass pull request requirements. See Bypass Pull Request Allowances below for details.
+        """
+        return pulumi.get(self, "bypass_pull_request_allowances")
+
+    @property
     @pulumi.getter(name="dismissStaleReviews")
     def dismiss_stale_reviews(self) -> Optional[bool]:
         """
         Dismiss approved reviews automatically when a new commit is pushed. Defaults to `false`.
         """
         return pulumi.get(self, "dismiss_stale_reviews")
 
@@ -474,14 +491,57 @@
         """
         Require x number of approvals to satisfy branch protection requirements. If this is specified it must be a number between 0-6. This requirement matches GitHub's API, see the upstream [documentation](https://developer.github.com/v3/repos/branches/#parameters-1) for more information.
         """
         return pulumi.get(self, "required_approving_review_count")
 
 
 @pulumi.output_type
+class BranchProtectionV3RequiredPullRequestReviewsBypassPullRequestAllowances(dict):
+    def __init__(__self__, *,
+                 apps: Optional[Sequence[str]] = None,
+                 teams: Optional[Sequence[str]] = None,
+                 users: Optional[Sequence[str]] = None):
+        """
+        :param Sequence[str] apps: The list of app slugs allowed to bypass pull request requirements.
+        :param Sequence[str] teams: The list of team slugs allowed to bypass pull request requirements.
+        :param Sequence[str] users: The list of user logins allowed to bypass pull request requirements.
+        """
+        if apps is not None:
+            pulumi.set(__self__, "apps", apps)
+        if teams is not None:
+            pulumi.set(__self__, "teams", teams)
+        if users is not None:
+            pulumi.set(__self__, "users", users)
+
+    @property
+    @pulumi.getter
+    def apps(self) -> Optional[Sequence[str]]:
+        """
+        The list of app slugs allowed to bypass pull request requirements.
+        """
+        return pulumi.get(self, "apps")
+
+    @property
+    @pulumi.getter
+    def teams(self) -> Optional[Sequence[str]]:
+        """
+        The list of team slugs allowed to bypass pull request requirements.
+        """
+        return pulumi.get(self, "teams")
+
+    @property
+    @pulumi.getter
+    def users(self) -> Optional[Sequence[str]]:
+        """
+        The list of user logins allowed to bypass pull request requirements.
+        """
+        return pulumi.get(self, "users")
+
+
+@pulumi.output_type
 class BranchProtectionV3RequiredStatusChecks(dict):
     @staticmethod
     def __key_warning(key: str):
         suggest = None
         if key == "includeAdmins":
             suggest = "include_admins"
 
@@ -648,14 +708,91 @@
     @property
     @pulumi.getter
     def secret(self) -> Optional[str]:
         return pulumi.get(self, "secret")
 
 
 @pulumi.output_type
+class RepositoryCollaboratorsTeam(dict):
+    @staticmethod
+    def __key_warning(key: str):
+        suggest = None
+        if key == "teamId":
+            suggest = "team_id"
+
+        if suggest:
+            pulumi.log.warn(f"Key '{key}' not found in RepositoryCollaboratorsTeam. Access the value via the '{suggest}' property getter instead.")
+
+    def __getitem__(self, key: str) -> Any:
+        RepositoryCollaboratorsTeam.__key_warning(key)
+        return super().__getitem__(key)
+
+    def get(self, key: str, default = None) -> Any:
+        RepositoryCollaboratorsTeam.__key_warning(key)
+        return super().get(key, default)
+
+    def __init__(__self__, *,
+                 team_id: str,
+                 permission: Optional[str] = None):
+        """
+        :param str permission: The permission of the outside collaborators for the repository.
+               Must be one of `pull`, `triage`, `push`, `maintain`, `admin` or the name of an existing [custom repository role](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization) within the organisation. Defaults to `pull`.
+               Must be `push` for personal repositories. Defaults to `push`.
+        """
+        pulumi.set(__self__, "team_id", team_id)
+        if permission is not None:
+            pulumi.set(__self__, "permission", permission)
+
+    @property
+    @pulumi.getter(name="teamId")
+    def team_id(self) -> str:
+        return pulumi.get(self, "team_id")
+
+    @property
+    @pulumi.getter
+    def permission(self) -> Optional[str]:
+        """
+        The permission of the outside collaborators for the repository.
+        Must be one of `pull`, `triage`, `push`, `maintain`, `admin` or the name of an existing [custom repository role](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization) within the organisation. Defaults to `pull`.
+        Must be `push` for personal repositories. Defaults to `push`.
+        """
+        return pulumi.get(self, "permission")
+
+
+@pulumi.output_type
+class RepositoryCollaboratorsUser(dict):
+    def __init__(__self__, *,
+                 username: str,
+                 permission: Optional[str] = None):
+        """
+        :param str permission: The permission of the outside collaborators for the repository.
+               Must be one of `pull`, `push`, `maintain`, `triage` or `admin` or the name of an existing [custom repository role](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization) within the organization for organization-owned repositories.
+               Must be `push` for personal repositories. Defaults to `push`.
+        """
+        pulumi.set(__self__, "username", username)
+        if permission is not None:
+            pulumi.set(__self__, "permission", permission)
+
+    @property
+    @pulumi.getter
+    def username(self) -> str:
+        return pulumi.get(self, "username")
+
+    @property
+    @pulumi.getter
+    def permission(self) -> Optional[str]:
+        """
+        The permission of the outside collaborators for the repository.
+        Must be one of `pull`, `push`, `maintain`, `triage` or `admin` or the name of an existing [custom repository role](https://docs.github.com/en/enterprise-cloud@latest/organizations/managing-peoples-access-to-your-organization-with-roles/managing-custom-repository-roles-for-an-organization) within the organization for organization-owned repositories.
+        Must be `push` for personal repositories. Defaults to `push`.
+        """
+        return pulumi.get(self, "permission")
+
+
+@pulumi.output_type
 class RepositoryEnvironmentDeploymentBranchPolicy(dict):
     @staticmethod
     def __key_warning(key: str):
         suggest = None
         if key == "customBranchPolicies":
             suggest = "custom_branch_policies"
         elif key == "protectedBranches":
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/project_card.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/project_card.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/project_column.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/project_column.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/provider.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/provider.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/release.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/release.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/repository.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/repository.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/repository_autolink_reference.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/repository_autolink_reference.py`

 * *Files 2% similar despite different names*

```diff
@@ -194,22 +194,20 @@
             repository=repo.name,
             key_prefix="TICKET-",
             target_url_template="https://example.com/TICKET?query=<num>")
         ```
 
         ## Import
 
-        Autolink references can be imported using the `name` of the repository, combined with the `id` of the autolink reference and a `/` character for separating components, e.g.
+        ### Import by key prefix
 
         ```sh
-         $ pulumi import github:index/repositoryAutolinkReference:RepositoryAutolinkReference auto my-repo/123
+         $ pulumi import github:index/repositoryAutolinkReference:RepositoryAutolinkReference auto oof/OOF-
         ```
 
-         See the GitHub documentation for how to [list all autolinks of a repository](https://docs.github.com/en/rest/repos/autolinks#list-all-autolinks-of-a-repository) to learn the autolink ids to use with the import command.
-
         :param str resource_name: The name of the resource.
         :param pulumi.ResourceOptions opts: Options for the resource.
         :param pulumi.Input[bool] is_alphanumeric: Whether this autolink reference matches alphanumeric characters. If false, this autolink reference only matches numeric characters. Default is true.
         :param pulumi.Input[str] key_prefix: This prefix appended by a number will generate a link any time it is found in an issue, pull request, or commit.
         :param pulumi.Input[str] repository: The repository of the autolink reference.
         :param pulumi.Input[str] target_url_template: The template of the target URL used for the links; must be a valid URL and contain `<num>` for the reference number
         """
@@ -235,22 +233,20 @@
             repository=repo.name,
             key_prefix="TICKET-",
             target_url_template="https://example.com/TICKET?query=<num>")
         ```
 
         ## Import
 
-        Autolink references can be imported using the `name` of the repository, combined with the `id` of the autolink reference and a `/` character for separating components, e.g.
+        ### Import by key prefix
 
         ```sh
-         $ pulumi import github:index/repositoryAutolinkReference:RepositoryAutolinkReference auto my-repo/123
+         $ pulumi import github:index/repositoryAutolinkReference:RepositoryAutolinkReference auto oof/OOF-
         ```
 
-         See the GitHub documentation for how to [list all autolinks of a repository](https://docs.github.com/en/rest/repos/autolinks#list-all-autolinks-of-a-repository) to learn the autolink ids to use with the import command.
-
         :param str resource_name: The name of the resource.
         :param RepositoryAutolinkReferenceArgs args: The arguments to use to populate this resource's properties.
         :param pulumi.ResourceOptions opts: Options for the resource.
         """
         ...
     def __init__(__self__, resource_name: str, *args, **kwargs):
         resource_args, opts = _utilities.get_resource_args_opts(RepositoryAutolinkReferenceArgs, pulumi.ResourceOptions, *args, **kwargs)
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/repository_collaborator.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/repository_collaborator.py`

 * *Files 2% similar despite different names*

```diff
@@ -186,25 +186,31 @@
                  permission_diff_suppression: Optional[pulumi.Input[bool]] = None,
                  repository: Optional[pulumi.Input[str]] = None,
                  username: Optional[pulumi.Input[str]] = None,
                  __props__=None):
         """
         Provides a GitHub repository collaborator resource.
 
+        > Note: RepositoryCollaborator cannot be used in conjunction with RepositoryCollaborators or
+        they will fight over what your policy should be.
+
         This resource allows you to add/remove collaborators from repositories in your
         organization or personal account. For organization repositories, collaborators can
         have explicit (and differing levels of) read, write, or administrator access to
         specific repositories, without giving the user full organization membership.
         For personal repositories, collaborators can only be granted write
-        (implictly includes read) permission.
+        (implicitly includes read) permission.
 
         When applied, an invitation will be sent to the user to become a collaborator
         on a repository. When destroyed, either the invitation will be cancelled or the
         collaborator will be removed from the repository.
 
+        This resource is non-authoritative, for managing ALL collaborators of a repo, use RepositoryCollaborators
+        instead.
+
         Further documentation on GitHub collaborators:
 
         - [Adding outside collaborators to your personal repositories](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/managing-access-to-your-personal-repositories)
         - [Adding outside collaborators to repositories in your organization](https://help.github.com/articles/adding-outside-collaborators-to-repositories-in-your-organization/)
         - [Converting an organization member to an outside collaborator](https://help.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)
 
         ## Example Usage
@@ -242,25 +248,31 @@
     def __init__(__self__,
                  resource_name: str,
                  args: RepositoryCollaboratorArgs,
                  opts: Optional[pulumi.ResourceOptions] = None):
         """
         Provides a GitHub repository collaborator resource.
 
+        > Note: RepositoryCollaborator cannot be used in conjunction with RepositoryCollaborators or
+        they will fight over what your policy should be.
+
         This resource allows you to add/remove collaborators from repositories in your
         organization or personal account. For organization repositories, collaborators can
         have explicit (and differing levels of) read, write, or administrator access to
         specific repositories, without giving the user full organization membership.
         For personal repositories, collaborators can only be granted write
-        (implictly includes read) permission.
+        (implicitly includes read) permission.
 
         When applied, an invitation will be sent to the user to become a collaborator
         on a repository. When destroyed, either the invitation will be cancelled or the
         collaborator will be removed from the repository.
 
+        This resource is non-authoritative, for managing ALL collaborators of a repo, use RepositoryCollaborators
+        instead.
+
         Further documentation on GitHub collaborators:
 
         - [Adding outside collaborators to your personal repositories](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/managing-access-to-your-personal-repositories)
         - [Adding outside collaborators to repositories in your organization](https://help.github.com/articles/adding-outside-collaborators-to-repositories-in-your-organization/)
         - [Converting an organization member to an outside collaborator](https://help.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)
 
         ## Example Usage
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/repository_deploy_key.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/repository_deploy_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/repository_environment.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/repository_environment.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/repository_file.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/repository_file.py`

 * *Files 4% similar despite different names*

```diff
@@ -23,15 +23,15 @@
                  commit_message: Optional[pulumi.Input[str]] = None,
                  overwrite_on_create: Optional[pulumi.Input[bool]] = None):
         """
         The set of arguments for constructing a RepositoryFile resource.
         :param pulumi.Input[str] content: The file content.
         :param pulumi.Input[str] file: The path of the file to manage.
         :param pulumi.Input[str] repository: The repository to create the file in.
-        :param pulumi.Input[str] branch: Git branch (defaults to `main`).
+        :param pulumi.Input[str] branch: Git branch (defaults to the repository's default branch).
                The branch must already exist, it will not be created if it does not already exist.
         :param pulumi.Input[str] commit_author: Committer author name to use. **NOTE:** GitHub app users may omit author and email information so GitHub can verify commits as the GitHub App. This maybe useful when a branch protection rule requires signed commits.
         :param pulumi.Input[str] commit_email: Committer email address to use. **NOTE:** GitHub app users may omit author and email information so GitHub can verify commits as the GitHub App. This may be useful when a branch protection rule requires signed commits.
         :param pulumi.Input[str] commit_message: Commit message when adding or updating the managed file.
         :param pulumi.Input[bool] overwrite_on_create: Enable overwriting existing files
         """
         pulumi.set(__self__, "content", content)
@@ -84,15 +84,15 @@
     def repository(self, value: pulumi.Input[str]):
         pulumi.set(self, "repository", value)
 
     @property
     @pulumi.getter
     def branch(self) -> Optional[pulumi.Input[str]]:
         """
-        Git branch (defaults to `main`).
+        Git branch (defaults to the repository's default branch).
         The branch must already exist, it will not be created if it does not already exist.
         """
         return pulumi.get(self, "branch")
 
     @branch.setter
     def branch(self, value: Optional[pulumi.Input[str]]):
         pulumi.set(self, "branch", value)
@@ -153,27 +153,29 @@
                  commit_author: Optional[pulumi.Input[str]] = None,
                  commit_email: Optional[pulumi.Input[str]] = None,
                  commit_message: Optional[pulumi.Input[str]] = None,
                  commit_sha: Optional[pulumi.Input[str]] = None,
                  content: Optional[pulumi.Input[str]] = None,
                  file: Optional[pulumi.Input[str]] = None,
                  overwrite_on_create: Optional[pulumi.Input[bool]] = None,
+                 ref: Optional[pulumi.Input[str]] = None,
                  repository: Optional[pulumi.Input[str]] = None,
                  sha: Optional[pulumi.Input[str]] = None):
         """
         Input properties used for looking up and filtering RepositoryFile resources.
-        :param pulumi.Input[str] branch: Git branch (defaults to `main`).
+        :param pulumi.Input[str] branch: Git branch (defaults to the repository's default branch).
                The branch must already exist, it will not be created if it does not already exist.
         :param pulumi.Input[str] commit_author: Committer author name to use. **NOTE:** GitHub app users may omit author and email information so GitHub can verify commits as the GitHub App. This maybe useful when a branch protection rule requires signed commits.
         :param pulumi.Input[str] commit_email: Committer email address to use. **NOTE:** GitHub app users may omit author and email information so GitHub can verify commits as the GitHub App. This may be useful when a branch protection rule requires signed commits.
         :param pulumi.Input[str] commit_message: Commit message when adding or updating the managed file.
         :param pulumi.Input[str] commit_sha: The SHA of the commit that modified the file.
         :param pulumi.Input[str] content: The file content.
         :param pulumi.Input[str] file: The path of the file to manage.
         :param pulumi.Input[bool] overwrite_on_create: Enable overwriting existing files
+        :param pulumi.Input[str] ref: The name of the commit/branch/tag.
         :param pulumi.Input[str] repository: The repository to create the file in.
         :param pulumi.Input[str] sha: The SHA blob of the file.
         """
         if branch is not None:
             pulumi.set(__self__, "branch", branch)
         if commit_author is not None:
             pulumi.set(__self__, "commit_author", commit_author)
@@ -185,24 +187,26 @@
             pulumi.set(__self__, "commit_sha", commit_sha)
         if content is not None:
             pulumi.set(__self__, "content", content)
         if file is not None:
             pulumi.set(__self__, "file", file)
         if overwrite_on_create is not None:
             pulumi.set(__self__, "overwrite_on_create", overwrite_on_create)
+        if ref is not None:
+            pulumi.set(__self__, "ref", ref)
         if repository is not None:
             pulumi.set(__self__, "repository", repository)
         if sha is not None:
             pulumi.set(__self__, "sha", sha)
 
     @property
     @pulumi.getter
     def branch(self) -> Optional[pulumi.Input[str]]:
         """
-        Git branch (defaults to `main`).
+        Git branch (defaults to the repository's default branch).
         The branch must already exist, it will not be created if it does not already exist.
         """
         return pulumi.get(self, "branch")
 
     @branch.setter
     def branch(self, value: Optional[pulumi.Input[str]]):
         pulumi.set(self, "branch", value)
@@ -289,14 +293,26 @@
 
     @overwrite_on_create.setter
     def overwrite_on_create(self, value: Optional[pulumi.Input[bool]]):
         pulumi.set(self, "overwrite_on_create", value)
 
     @property
     @pulumi.getter
+    def ref(self) -> Optional[pulumi.Input[str]]:
+        """
+        The name of the commit/branch/tag.
+        """
+        return pulumi.get(self, "ref")
+
+    @ref.setter
+    def ref(self, value: Optional[pulumi.Input[str]]):
+        pulumi.set(self, "ref", value)
+
+    @property
+    @pulumi.getter
     def repository(self) -> Optional[pulumi.Input[str]]:
         """
         The repository to create the file in.
         """
         return pulumi.get(self, "repository")
 
     @repository.setter
@@ -356,23 +372,23 @@
 
         Repository files can be imported using a combination of the `repo` and `file`, e.g.
 
         ```sh
          $ pulumi import github:index/repositoryFile:RepositoryFile gitignore example/.gitignore
         ```
 
-         To import a file from a branch other than main, append `:` and the branch name, e.g.
+         To import a file from a branch other than the default branch, append `:` and the branch name, e.g.
 
         ```sh
          $ pulumi import github:index/repositoryFile:RepositoryFile gitignore example/.gitignore:dev
         ```
 
         :param str resource_name: The name of the resource.
         :param pulumi.ResourceOptions opts: Options for the resource.
-        :param pulumi.Input[str] branch: Git branch (defaults to `main`).
+        :param pulumi.Input[str] branch: Git branch (defaults to the repository's default branch).
                The branch must already exist, it will not be created if it does not already exist.
         :param pulumi.Input[str] commit_author: Committer author name to use. **NOTE:** GitHub app users may omit author and email information so GitHub can verify commits as the GitHub App. This maybe useful when a branch protection rule requires signed commits.
         :param pulumi.Input[str] commit_email: Committer email address to use. **NOTE:** GitHub app users may omit author and email information so GitHub can verify commits as the GitHub App. This may be useful when a branch protection rule requires signed commits.
         :param pulumi.Input[str] commit_message: Commit message when adding or updating the managed file.
         :param pulumi.Input[str] content: The file content.
         :param pulumi.Input[str] file: The path of the file to manage.
         :param pulumi.Input[bool] overwrite_on_create: Enable overwriting existing files
@@ -410,15 +426,15 @@
 
         Repository files can be imported using a combination of the `repo` and `file`, e.g.
 
         ```sh
          $ pulumi import github:index/repositoryFile:RepositoryFile gitignore example/.gitignore
         ```
 
-         To import a file from a branch other than main, append `:` and the branch name, e.g.
+         To import a file from a branch other than the default branch, append `:` and the branch name, e.g.
 
         ```sh
          $ pulumi import github:index/repositoryFile:RepositoryFile gitignore example/.gitignore:dev
         ```
 
         :param str resource_name: The name of the resource.
         :param RepositoryFileArgs args: The arguments to use to populate this resource's properties.
@@ -463,14 +479,15 @@
                 raise TypeError("Missing required property 'file'")
             __props__.__dict__["file"] = file
             __props__.__dict__["overwrite_on_create"] = overwrite_on_create
             if repository is None and not opts.urn:
                 raise TypeError("Missing required property 'repository'")
             __props__.__dict__["repository"] = repository
             __props__.__dict__["commit_sha"] = None
+            __props__.__dict__["ref"] = None
             __props__.__dict__["sha"] = None
         super(RepositoryFile, __self__).__init__(
             'github:index/repositoryFile:RepositoryFile',
             resource_name,
             __props__,
             opts)
 
@@ -482,32 +499,34 @@
             commit_author: Optional[pulumi.Input[str]] = None,
             commit_email: Optional[pulumi.Input[str]] = None,
             commit_message: Optional[pulumi.Input[str]] = None,
             commit_sha: Optional[pulumi.Input[str]] = None,
             content: Optional[pulumi.Input[str]] = None,
             file: Optional[pulumi.Input[str]] = None,
             overwrite_on_create: Optional[pulumi.Input[bool]] = None,
+            ref: Optional[pulumi.Input[str]] = None,
             repository: Optional[pulumi.Input[str]] = None,
             sha: Optional[pulumi.Input[str]] = None) -> 'RepositoryFile':
         """
         Get an existing RepositoryFile resource's state with the given name, id, and optional extra
         properties used to qualify the lookup.
 
         :param str resource_name: The unique name of the resulting resource.
         :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
         :param pulumi.ResourceOptions opts: Options for the resource.
-        :param pulumi.Input[str] branch: Git branch (defaults to `main`).
+        :param pulumi.Input[str] branch: Git branch (defaults to the repository's default branch).
                The branch must already exist, it will not be created if it does not already exist.
         :param pulumi.Input[str] commit_author: Committer author name to use. **NOTE:** GitHub app users may omit author and email information so GitHub can verify commits as the GitHub App. This maybe useful when a branch protection rule requires signed commits.
         :param pulumi.Input[str] commit_email: Committer email address to use. **NOTE:** GitHub app users may omit author and email information so GitHub can verify commits as the GitHub App. This may be useful when a branch protection rule requires signed commits.
         :param pulumi.Input[str] commit_message: Commit message when adding or updating the managed file.
         :param pulumi.Input[str] commit_sha: The SHA of the commit that modified the file.
         :param pulumi.Input[str] content: The file content.
         :param pulumi.Input[str] file: The path of the file to manage.
         :param pulumi.Input[bool] overwrite_on_create: Enable overwriting existing files
+        :param pulumi.Input[str] ref: The name of the commit/branch/tag.
         :param pulumi.Input[str] repository: The repository to create the file in.
         :param pulumi.Input[str] sha: The SHA blob of the file.
         """
         opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))
 
         __props__ = _RepositoryFileState.__new__(_RepositoryFileState)
 
@@ -515,23 +534,24 @@
         __props__.__dict__["commit_author"] = commit_author
         __props__.__dict__["commit_email"] = commit_email
         __props__.__dict__["commit_message"] = commit_message
         __props__.__dict__["commit_sha"] = commit_sha
         __props__.__dict__["content"] = content
         __props__.__dict__["file"] = file
         __props__.__dict__["overwrite_on_create"] = overwrite_on_create
+        __props__.__dict__["ref"] = ref
         __props__.__dict__["repository"] = repository
         __props__.__dict__["sha"] = sha
         return RepositoryFile(resource_name, opts=opts, __props__=__props__)
 
     @property
     @pulumi.getter
     def branch(self) -> pulumi.Output[Optional[str]]:
         """
-        Git branch (defaults to `main`).
+        Git branch (defaults to the repository's default branch).
         The branch must already exist, it will not be created if it does not already exist.
         """
         return pulumi.get(self, "branch")
 
     @property
     @pulumi.getter(name="commitAuthor")
     def commit_author(self) -> pulumi.Output[Optional[str]]:
@@ -586,14 +606,22 @@
         """
         Enable overwriting existing files
         """
         return pulumi.get(self, "overwrite_on_create")
 
     @property
     @pulumi.getter
+    def ref(self) -> pulumi.Output[str]:
+        """
+        The name of the commit/branch/tag.
+        """
+        return pulumi.get(self, "ref")
+
+    @property
+    @pulumi.getter
     def repository(self) -> pulumi.Output[str]:
         """
         The repository to create the file in.
         """
         return pulumi.get(self, "repository")
 
     @property
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/repository_milestone.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/repository_milestone.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/repository_project.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/repository_project.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/repository_pull_request.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/repository_pull_request.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/repository_tag_protection.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/repository_tag_protection.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/repository_webhook.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/repository_webhook.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/team.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/team.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/team_members.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/team_members.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/team_membership.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/team_membership.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/team_repository.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/team_repository.py`

 * *Files 6% similar despite different names*

```diff
@@ -143,24 +143,30 @@
                  resource_name: str,
                  opts: Optional[pulumi.ResourceOptions] = None,
                  permission: Optional[pulumi.Input[str]] = None,
                  repository: Optional[pulumi.Input[str]] = None,
                  team_id: Optional[pulumi.Input[str]] = None,
                  __props__=None):
         """
+        > Note: TeamRepository cannot be used in conjunction with RepositoryCollaborators or
+        they will fight over what your policy should be.
+
         This resource manages relationships between teams and repositories
         in your GitHub organization.
 
         Creating this resource grants a particular team permissions on a
         particular repository.
 
         The repository and the team must both belong to the same organization
         on GitHub. This resource does not actually *create* any repositories;
         to do that, see `Repository`.
 
+        This resource is non-authoritative, for managing ALL collaborators of a repo, use RepositoryCollaborators
+        instead.
+
         ## Example Usage
 
         ```python
         import pulumi
         import pulumi_github as github
 
         # Add a repository to the team
@@ -190,24 +196,30 @@
         ...
     @overload
     def __init__(__self__,
                  resource_name: str,
                  args: TeamRepositoryArgs,
                  opts: Optional[pulumi.ResourceOptions] = None):
         """
+        > Note: TeamRepository cannot be used in conjunction with RepositoryCollaborators or
+        they will fight over what your policy should be.
+
         This resource manages relationships between teams and repositories
         in your GitHub organization.
 
         Creating this resource grants a particular team permissions on a
         particular repository.
 
         The repository and the team must both belong to the same organization
         on GitHub. This resource does not actually *create* any repositories;
         to do that, see `Repository`.
 
+        This resource is non-authoritative, for managing ALL collaborators of a repo, use RepositoryCollaborators
+        instead.
+
         ## Example Usage
 
         ```python
         import pulumi
         import pulumi_github as github
 
         # Add a repository to the team
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/team_settings.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/team_settings.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/team_sync_group_mapping.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/team_sync_group_mapping.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/user_gpg_key.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/user_gpg_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/user_invitation_accepter.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/user_invitation_accepter.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github/user_ssh_key.py` & `pulumi_github-5.7.0a1680815968/pulumi_github/user_ssh_key.py`

 * *Files identical despite different names*

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github.egg-info/PKG-INFO` & `pulumi_github-5.7.0a1680815968/pulumi_github.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pulumi-github
-Version: 5.7.0a1680747500
+Version: 5.7.0a1680815968
 Summary: A Pulumi package for creating and managing github cloud resources.
 Home-page: https://pulumi.io
 License: Apache-2.0
 Project-URL: Repository, https://github.com/pulumi/pulumi-github
 Keywords: pulumi github
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
```

### Comparing `pulumi_github-5.7.0a1680747500/pulumi_github.egg-info/SOURCES.txt` & `pulumi_github-5.7.0a1680815968/pulumi_github.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -26,24 +26,26 @@
 pulumi_github/dependabot_organization_secret_repositories.py
 pulumi_github/dependabot_secret.py
 pulumi_github/emu_group_mapping.py
 pulumi_github/enterprise_organization.py
 pulumi_github/get_actions_environment_secrets.py
 pulumi_github/get_actions_environment_variables.py
 pulumi_github/get_actions_organization_oidc_subject_claim_customization_template.py
+pulumi_github/get_actions_organization_public_key.py
 pulumi_github/get_actions_organization_registration_token.py
 pulumi_github/get_actions_organization_secrets.py
 pulumi_github/get_actions_organization_variables.py
 pulumi_github/get_actions_public_key.py
 pulumi_github/get_actions_registration_token.py
 pulumi_github/get_actions_repository_oidc_subject_claim_customization_template.py
 pulumi_github/get_actions_secrets.py
 pulumi_github/get_actions_variables.py
 pulumi_github/get_branch.py
 pulumi_github/get_collaborators.py
+pulumi_github/get_dependabot_organization_public_key.py
 pulumi_github/get_dependabot_organization_secrets.py
 pulumi_github/get_dependabot_public_key.py
 pulumi_github/get_dependabot_secrets.py
 pulumi_github/get_enterprise.py
 pulumi_github/get_external_groups.py
 pulumi_github/get_github_app.py
 pulumi_github/get_ip_ranges.py
@@ -61,14 +63,15 @@
 pulumi_github/get_repository_deploy_keys.py
 pulumi_github/get_repository_file.py
 pulumi_github/get_repository_milestone.py
 pulumi_github/get_repository_pull_request.py
 pulumi_github/get_repository_pull_requests.py
 pulumi_github/get_repository_teams.py
 pulumi_github/get_repository_webhooks.py
+pulumi_github/get_ssh_keys.py
 pulumi_github/get_team.py
 pulumi_github/get_tree.py
 pulumi_github/get_user.py
 pulumi_github/get_users.py
 pulumi_github/issue.py
 pulumi_github/issue_label.py
 pulumi_github/membership.py
@@ -83,14 +86,15 @@
 pulumi_github/provider.py
 pulumi_github/pulumi-plugin.json
 pulumi_github/py.typed
 pulumi_github/release.py
 pulumi_github/repository.py
 pulumi_github/repository_autolink_reference.py
 pulumi_github/repository_collaborator.py
+pulumi_github/repository_collaborators.py
 pulumi_github/repository_deploy_key.py
 pulumi_github/repository_environment.py
 pulumi_github/repository_file.py
 pulumi_github/repository_milestone.py
 pulumi_github/repository_project.py
 pulumi_github/repository_pull_request.py
 pulumi_github/repository_tag_protection.py
```

### Comparing `pulumi_github-5.7.0a1680747500/setup.py` & `pulumi_github-5.7.0a1680815968/setup.py`

 * *Files 5% similar despite different names*

```diff
@@ -4,16 +4,16 @@
 
 import errno
 from setuptools import setup, find_packages
 from setuptools.command.install import install
 from subprocess import check_call
 
 
-VERSION = "5.7.0a1680747500"
-PLUGIN_VERSION = "5.7.0-alpha.1680747500+e5d900cf"
+VERSION = "5.7.0a1680815968"
+PLUGIN_VERSION = "5.7.0-alpha.1680815968+cd8957eb"
 
 class InstallPluginCommand(install):
     def run(self):
         install.run(self)
         try:
             check_call(['pulumi', 'plugin', 'install', 'resource', 'github', PLUGIN_VERSION])
         except OSError as error:
```

