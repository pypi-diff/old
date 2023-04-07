# Comparing `tmp/edgeimpulse_api-1.22.0.tar.gz` & `tmp/edgeimpulse_api-1.22.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "edgeimpulse_api-1.22.0.tar", max compression
+gzip compressed data, was "edgeimpulse_api-1.22.1.tar", max compression
```

## Comparing `edgeimpulse_api-1.22.0.tar` & `edgeimpulse_api-1.22.1.tar`

### file list

```diff
@@ -1,686 +1,1374 @@
--rw-r--r--   0        0        0      377 2023-04-04 07:09:11.361655 edgeimpulse_api-1.22.0/README.md
--rw-r--r--   0        0        0    64616 2023-04-04 08:07:37.107825 edgeimpulse_api-1.22.0/edgeimpulse_api/__init__.py
--rw-r--r--   0        0        0     2752 2023-04-04 08:06:33.844421 edgeimpulse_api-1.22.0/edgeimpulse_api/api/__init__.py
--rw-r--r--   0        0        0   161969 2023-04-04 08:06:33.022719 edgeimpulse_api-1.22.0/edgeimpulse_api/api/admin_api.py
--rw-r--r--   0        0        0   282240 2023-04-04 08:06:33.096063 edgeimpulse_api-1.22.0/edgeimpulse_api/api/allows_read_only_api.py
--rw-r--r--   0        0        0    11231 2023-04-04 08:06:33.159617 edgeimpulse_api-1.22.0/edgeimpulse_api/api/auth_api.py
--rw-r--r--   0        0        0     6235 2023-04-04 08:06:33.183017 edgeimpulse_api-1.22.0/edgeimpulse_api/api/cdn_api.py
--rw-r--r--   0        0        0    19852 2023-04-04 08:06:33.201450 edgeimpulse_api-1.22.0/edgeimpulse_api/api/classify_api.py
--rw-r--r--   0        0        0     7426 2023-04-04 08:06:33.227326 edgeimpulse_api-1.22.0/edgeimpulse_api/api/content_disposition_inline_api.py
--rw-r--r--   0        0        0    72480 2023-04-04 08:06:33.282625 edgeimpulse_api-1.22.0/edgeimpulse_api/api/deployment_api.py
--rw-r--r--   0        0        0    38974 2023-04-04 08:06:33.305311 edgeimpulse_api-1.22.0/edgeimpulse_api/api/devices_api.py
--rw-r--r--   0        0        0   122864 2023-04-04 08:06:33.259986 edgeimpulse_api-1.22.0/edgeimpulse_api/api/dsp_api.py
--rw-r--r--   0        0        0     6435 2023-04-04 08:06:33.322602 edgeimpulse_api-1.22.0/edgeimpulse_api/api/export_api.py
--rw-r--r--   0        0        0    11921 2023-04-04 08:06:33.343417 edgeimpulse_api-1.22.0/edgeimpulse_api/api/health_api.py
--rw-r--r--   0        0        0    49621 2023-04-04 08:06:33.357010 edgeimpulse_api-1.22.0/edgeimpulse_api/api/impulse_api.py
--rw-r--r--   0        0        0   231500 2023-04-04 08:06:33.384725 edgeimpulse_api-1.22.0/edgeimpulse_api/api/jobs_api.py
--rw-r--r--   0        0        0   134972 2023-04-04 08:06:33.411294 edgeimpulse_api-1.22.0/edgeimpulse_api/api/learn_api.py
--rw-r--r--   0        0        0     6605 2023-04-04 08:06:33.434302 edgeimpulse_api-1.22.0/edgeimpulse_api/api/login_api.py
--rw-r--r--   0        0        0    12006 2023-04-04 08:06:33.449604 edgeimpulse_api-1.22.0/edgeimpulse_api/api/metrics_api.py
--rw-r--r--   0        0        0    67457 2023-04-04 08:06:33.460214 edgeimpulse_api-1.22.0/edgeimpulse_api/api/optimization_api.py
--rw-r--r--   0        0        0   300920 2023-04-04 08:06:33.474661 edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_allow_developer_profile_api.py
--rw-r--r--   0        0        0    63058 2023-04-04 08:06:33.490763 edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_allow_guest_access_api.py
--rw-r--r--   0        0        0   141131 2023-04-04 08:06:33.504842 edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_blocks_api.py
--rw-r--r--   0        0        0    91908 2023-04-04 08:06:33.520957 edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_create_project_api.py
--rw-r--r--   0        0        0   240681 2023-04-04 08:06:33.540667 edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_data_api.py
--rw-r--r--   0        0        0    58218 2023-04-04 08:06:33.557297 edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_jobs_api.py
--rw-r--r--   0        0        0    47178 2023-04-04 08:06:33.568145 edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_pipelines_api.py
--rw-r--r--   0        0        0    45490 2023-04-04 08:06:33.580236 edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_portals_api.py
--rw-r--r--   0        0        0   178330 2023-04-04 08:06:33.592704 edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_requires_admin_api.py
--rw-r--r--   0        0        0    88200 2023-04-04 08:06:33.606621 edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_requires_whitelabel_admin_api.py
--rw-r--r--   0        0        0   212216 2023-04-04 08:06:33.622748 edgeimpulse_api-1.22.0/edgeimpulse_api/api/organizations_api.py
--rw-r--r--   0        0        0    54671 2023-04-04 08:06:33.641933 edgeimpulse_api-1.22.0/edgeimpulse_api/api/performance_calibration_api.py
--rw-r--r--   0        0        0   220399 2023-04-04 08:06:33.657072 edgeimpulse_api-1.22.0/edgeimpulse_api/api/projects_api.py
--rw-r--r--   0        0        0   324953 2023-04-04 08:06:33.680694 edgeimpulse_api-1.22.0/edgeimpulse_api/api/raw_data_api.py
--rw-r--r--   0        0        0   252278 2023-04-04 08:06:33.702854 edgeimpulse_api-1.22.0/edgeimpulse_api/api/requires_sudo_api.py
--rw-r--r--   0        0        0     7730 2023-04-04 08:06:33.719474 edgeimpulse_api-1.22.0/edgeimpulse_api/api/requires_third_party_auth_api_key_api.py
--rw-r--r--   0        0        0    13690 2023-04-04 08:06:33.727656 edgeimpulse_api-1.22.0/edgeimpulse_api/api/supports_range_api.py
--rw-r--r--   0        0        0    35671 2023-04-04 08:06:33.739375 edgeimpulse_api-1.22.0/edgeimpulse_api/api/themes_api.py
--rw-r--r--   0        0        0    43486 2023-04-04 08:06:33.750184 edgeimpulse_api-1.22.0/edgeimpulse_api/api/third_party_auth_api.py
--rw-r--r--   0        0        0    45393 2023-04-04 08:06:33.765888 edgeimpulse_api-1.22.0/edgeimpulse_api/api/upload_portal_api.py
--rw-r--r--   0        0        0   197621 2023-04-04 08:06:33.776739 edgeimpulse_api-1.22.0/edgeimpulse_api/api/user_api.py
--rw-r--r--   0        0        0    42135 2023-04-04 08:06:33.794848 edgeimpulse_api-1.22.0/edgeimpulse_api/api/whitelabels_api.py
--rw-r--r--   0        0        0    29331 2023-04-04 08:06:33.854304 edgeimpulse_api-1.22.0/edgeimpulse_api/api_client.py
--rw-r--r--   0        0        0    15659 2023-04-04 08:06:33.831466 edgeimpulse_api-1.22.0/edgeimpulse_api/configuration.py
--rw-r--r--   0        0        0     5113 2023-04-04 08:06:33.849539 edgeimpulse_api-1.22.0/edgeimpulse_api/exceptions.py
--rw-r--r--   0        0        0    61411 2023-04-04 08:06:51.092099 edgeimpulse_api-1.22.0/edgeimpulse_api/models/__init__.py
--rw-r--r--   0        0        0     2892 2023-04-04 08:06:51.067247 edgeimpulse_api-1.22.0/edgeimpulse_api/models/activate_user_by_third_party_activation_code_request.py
--rw-r--r--   0        0        0     1877 2023-04-04 08:06:51.072352 edgeimpulse_api-1.22.0/edgeimpulse_api/models/activate_user_request.py
--rw-r--r--   0        0        0     2605 2023-04-04 08:06:49.904157 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_api_key_request.py
--rw-r--r--   0        0        0     1958 2023-04-04 08:06:50.326503 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_collaborator_request.py
--rw-r--r--   0        0        0     2218 2023-04-04 08:06:51.653936 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_hmac_key_request.py
--rw-r--r--   0        0        0     2427 2023-04-04 08:06:51.570977 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_member_request.py
--rw-r--r--   0        0        0     2413 2023-04-04 08:06:50.668659 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_api_key_request.py
--rw-r--r--   0        0        0     2725 2023-04-04 08:06:51.107983 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_bucket_request.py
--rw-r--r--   0        0        0     2264 2023-04-04 08:06:51.282019 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_deploy_block_response.py
--rw-r--r--   0        0        0     2811 2023-04-04 08:06:51.017417 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_dsp_block_request.py
--rw-r--r--   0        0        0     2243 2023-04-04 08:06:51.391803 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_dsp_block_response.py
--rw-r--r--   0        0        0     2049 2023-04-04 08:06:51.050570 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_secret_request.py
--rw-r--r--   0        0        0     2261 2023-04-04 08:06:51.411858 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_secret_response.py
--rw-r--r--   0        0        0     1944 2023-04-04 08:06:50.896698 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_secret_response_all_of.py
--rw-r--r--   0        0        0     3829 2023-04-04 08:06:50.451864 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_transfer_learning_block_request.py
--rw-r--r--   0        0        0     2334 2023-04-04 08:06:51.366300 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_transfer_learning_block_response.py
--rw-r--r--   0        0        0     4587 2023-04-04 08:06:50.046682 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_transformation_block_request.py
--rw-r--r--   0        0        0     2320 2023-04-04 08:06:52.248947 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_transformation_block_response.py
--rw-r--r--   0        0        0     1996 2023-04-04 08:06:50.578956 edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_transformation_block_response_all_of.py
--rw-r--r--   0        0        0     1956 2023-04-04 08:06:51.639831 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_add_or_update_sso_domain_id_ps_request.py
--rw-r--r--   0        0        0     1982 2023-04-04 08:06:51.932742 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_add_project_user_request.py
--rw-r--r--   0        0        0     3871 2023-04-04 08:06:52.540990 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_api_organization.py
--rw-r--r--   0        0        0     2391 2023-04-04 08:06:50.364432 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_api_organization_all_of.py
--rw-r--r--   0        0        0     3454 2023-04-04 08:06:51.261371 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_api_project.py
--rw-r--r--   0        0        0     6133 2023-04-04 08:06:50.573825 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_api_user.py
--rw-r--r--   0        0        0     4948 2023-04-04 08:06:51.891872 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_api_user_all_of.py
--rw-r--r--   0        0        0     2257 2023-04-04 08:06:51.394027 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_create_organization_request.py
--rw-r--r--   0        0        0     2212 2023-04-04 08:06:51.606507 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_metrics_response.py
--rw-r--r--   0        0        0     1905 2023-04-04 08:06:51.315591 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_metrics_response_all_of.py
--rw-r--r--   0        0        0     3041 2023-04-04 08:06:51.199118 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_organizations_response.py
--rw-r--r--   0        0        0     2741 2023-04-04 08:06:52.634686 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_organizations_response_all_of.py
--rw-r--r--   0        0        0     2863 2023-04-04 08:06:51.220810 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_organizations_response_all_of_organizations.py
--rw-r--r--   0        0        0     2238 2023-04-04 08:06:51.061178 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_sso_domain_id_ps_response.py
--rw-r--r--   0        0        0     1942 2023-04-04 08:06:51.192599 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_sso_domain_id_ps_response_all_of.py
--rw-r--r--   0        0        0     2909 2023-04-04 08:06:51.681284 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_sso_settings_response.py
--rw-r--r--   0        0        0     2609 2023-04-04 08:06:51.463094 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_sso_settings_response_all_of.py
--rw-r--r--   0        0        0     2091 2023-04-04 08:06:50.872268 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_sso_settings_response_all_of_sso_whitelist.py
--rw-r--r--   0        0        0     2203 2023-04-04 08:06:51.769970 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_ids_response.py
--rw-r--r--   0        0        0     1896 2023-04-04 08:06:51.660607 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_ids_response_all_of.py
--rw-r--r--   0        0        0     2240 2023-04-04 08:06:52.399317 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_metrics_response.py
--rw-r--r--   0        0        0     1933 2023-04-04 08:06:50.544488 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_metrics_response_all_of.py
--rw-r--r--   0        0        0     2447 2023-04-04 08:06:50.008844 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_response.py
--rw-r--r--   0        0        0     2123 2023-04-04 08:06:51.211051 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_response_all_of.py
--rw-r--r--   0        0        0     2802 2023-04-04 08:06:50.753225 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_users_response.py
--rw-r--r--   0        0        0     2495 2023-04-04 08:06:52.378158 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_users_response_all_of.py
--rw-r--r--   0        0        0     3082 2023-04-04 08:06:51.225989 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_users_response_all_of_users.py
--rw-r--r--   0        0        0     2440 2023-04-04 08:06:51.304101 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_list_projects.py
--rw-r--r--   0        0        0     2831 2023-04-04 08:06:51.286681 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_list_projects_response.py
--rw-r--r--   0        0        0     6067 2023-04-04 08:06:50.885036 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_organization_info_response.py
--rw-r--r--   0        0        0     1969 2023-04-04 08:06:51.455231 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_organization_info_response_all_of.py
--rw-r--r--   0        0        0     2723 2023-04-04 08:06:52.696592 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_update_organization_request.py
--rw-r--r--   0        0        0     2125 2023-04-04 08:06:52.704635 edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_update_user_request.py
--rw-r--r--   0        0        0     2520 2023-04-04 08:06:51.604239 edgeimpulse_api-1.22.0/edgeimpulse_api/models/akida_edge_learning_config.py
--rw-r--r--   0        0        0     3625 2023-04-04 08:06:50.249907 edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_model_metadata.py
--rw-r--r--   0        0        0     2146 2023-04-04 08:06:50.918393 edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_model_metadata_clusters_inner.py
--rw-r--r--   0        0        0     4006 2023-04-04 08:06:52.333737 edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_model_metadata_response.py
--rw-r--r--   0        0        0     4074 2023-04-04 08:06:50.379123 edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_response.py
--rw-r--r--   0        0        0     3807 2023-04-04 08:06:51.444223 edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_response_all_of.py
--rw-r--r--   0        0        0     2039 2023-04-04 08:06:50.689142 edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_response_all_of_axes.py
--rw-r--r--   0        0        0     3024 2023-04-04 08:06:51.551814 edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_trained_features_response.py
--rw-r--r--   0        0        0     2724 2023-04-04 08:06:51.663695 edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_trained_features_response_all_of.py
--rw-r--r--   0        0        0     2370 2023-04-04 08:06:50.405820 edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_trained_features_response_all_of_data.py
--rw-r--r--   0        0        0      506 2023-04-04 08:06:51.222698 edgeimpulse_api-1.22.0/edgeimpulse_api/models/augmentation_policy_image_enum.py
--rw-r--r--   0        0        0     3630 2023-04-04 08:06:50.893114 edgeimpulse_api-1.22.0/edgeimpulse_api/models/augmentation_policy_spectrogram.py
--rw-r--r--   0        0        0     1890 2023-04-04 08:06:50.242539 edgeimpulse_api-1.22.0/edgeimpulse_api/models/autotune_dsp_request.py
--rw-r--r--   0        0        0     2039 2023-04-04 08:06:51.494239 edgeimpulse_api-1.22.0/edgeimpulse_api/models/bounding_box.py
--rw-r--r--   0        0        0     2146 2023-04-04 08:06:50.281786 edgeimpulse_api-1.22.0/edgeimpulse_api/models/bounding_box_with_score.py
--rw-r--r--   0        0        0     2192 2023-04-04 08:06:50.908258 edgeimpulse_api-1.22.0/edgeimpulse_api/models/build_on_device_model_request.py
--rw-r--r--   0        0        0     2428 2023-04-04 08:06:50.305045 edgeimpulse_api-1.22.0/edgeimpulse_api/models/build_organization_on_device_model_request.py
--rw-r--r--   0        0        0     2036 2023-04-04 08:06:50.709537 edgeimpulse_api-1.22.0/edgeimpulse_api/models/change_password_request.py
--rw-r--r--   0        0        0     3302 2023-04-04 08:06:51.372509 edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_job_response.py
--rw-r--r--   0        0        0     2995 2023-04-04 08:06:52.566012 edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_job_response_all_of.py
--rw-r--r--   0        0        0     3023 2023-04-04 08:06:51.510212 edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_job_response_all_of_result.py
--rw-r--r--   0        0        0     3927 2023-04-04 08:06:50.284821 edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_sample_response.py
--rw-r--r--   0        0        0     3639 2023-04-04 08:06:50.229209 edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_sample_response_all_of.py
--rw-r--r--   0        0        0     4778 2023-04-04 08:06:50.798326 edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_sample_response_classification.py
--rw-r--r--   0        0        0     2592 2023-04-04 08:06:50.270163 edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_sample_response_classification_details.py
--rw-r--r--   0        0        0     2999 2023-04-04 08:06:51.348760 edgeimpulse_api-1.22.0/edgeimpulse_api/models/convert_user_request.py
--rw-r--r--   0        0        0     2178 2023-04-04 08:06:51.564728 edgeimpulse_api-1.22.0/edgeimpulse_api/models/count_samples_response.py
--rw-r--r--   0        0        0     1854 2023-04-04 08:06:50.074072 edgeimpulse_api-1.22.0/edgeimpulse_api/models/count_samples_response_all_of.py
--rw-r--r--   0        0        0     2250 2023-04-04 08:06:51.438406 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_block_version_response.py
--rw-r--r--   0        0        0     1933 2023-04-04 08:06:52.337999 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_block_version_response_all_of.py
--rw-r--r--   0        0        0     2399 2023-04-04 08:06:50.839337 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_developer_profile_response.py
--rw-r--r--   0        0        0     2120 2023-04-04 08:06:50.038159 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_developer_profile_response_all_of.py
--rw-r--r--   0        0        0     2382 2023-04-04 08:06:51.385694 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_device_request.py
--rw-r--r--   0        0        0     2486 2023-04-04 08:06:50.330803 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_evaluation_user_response.py
--rw-r--r--   0        0        0     2180 2023-04-04 08:06:51.002658 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_evaluation_user_response_all_of.py
--rw-r--r--   0        0        0     2595 2023-04-04 08:06:50.679294 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_portal_request.py
--rw-r--r--   0        0        0     2825 2023-04-04 08:06:51.749358 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_portal_response.py
--rw-r--r--   0        0        0     2546 2023-04-04 08:06:50.553721 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_portal_response_all_of.py
--rw-r--r--   0        0        0     1985 2023-04-04 08:06:51.998635 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_request.py
--rw-r--r--   0        0        0     2449 2023-04-04 08:06:51.884676 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_response.py
--rw-r--r--   0        0        0     2143 2023-04-04 08:06:51.696082 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_response_all_of.py
--rw-r--r--   0        0        0     2180 2023-04-04 08:06:50.890351 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_pipeline_response.py
--rw-r--r--   0        0        0     2249 2023-04-04 08:06:49.872145 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_project_request.py
--rw-r--r--   0        0        0     2373 2023-04-04 08:06:50.966140 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_project_response.py
--rw-r--r--   0        0        0     2067 2023-04-04 08:06:52.152556 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_project_response_all_of.py
--rw-r--r--   0        0        0     2271 2023-04-04 08:06:51.942067 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_signed_upload_link_request.py
--rw-r--r--   0        0        0     2409 2023-04-04 08:06:51.720360 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_signed_upload_link_response.py
--rw-r--r--   0        0        0     2130 2023-04-04 08:06:50.354735 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_signed_upload_link_response_all_of.py
--rw-r--r--   0        0        0     2408 2023-04-04 08:06:52.468519 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_third_party_auth_request.py
--rw-r--r--   0        0        0     2445 2023-04-04 08:06:50.390354 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_third_party_auth_response.py
--rw-r--r--   0        0        0     2139 2023-04-04 08:06:50.109569 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_third_party_auth_response_all_of.py
--rw-r--r--   0        0        0     3830 2023-04-04 08:06:50.898208 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_request.py
--rw-r--r--   0        0        0     2388 2023-04-04 08:06:50.639238 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_response.py
--rw-r--r--   0        0        0     2109 2023-04-04 08:06:50.734576 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_response_all_of.py
--rw-r--r--   0        0        0     2914 2023-04-04 08:06:51.159101 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_third_party_request.py
--rw-r--r--   0        0        0     2667 2023-04-04 08:06:52.265694 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_third_party_response.py
--rw-r--r--   0        0        0     2388 2023-04-04 08:06:50.905866 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_third_party_response_all_of.py
--rw-r--r--   0        0        0     4152 2023-04-04 08:06:50.033081 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_whitelabel_request.py
--rw-r--r--   0        0        0     2433 2023-04-04 08:06:50.931163 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_whitelabel_response.py
--rw-r--r--   0        0        0     2116 2023-04-04 08:06:50.279320 edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_whitelabel_response_all_of.py
--rw-r--r--   0        0        0     2046 2023-04-04 08:06:52.513091 edgeimpulse_api-1.22.0/edgeimpulse_api/models/crop_sample_request.py
--rw-r--r--   0        0        0     2243 2023-04-04 08:06:51.389750 edgeimpulse_api-1.22.0/edgeimpulse_api/models/crop_sample_response.py
--rw-r--r--   0        0        0     1938 2023-04-04 08:06:50.876960 edgeimpulse_api-1.22.0/edgeimpulse_api/models/crop_sample_response_all_of.py
--rw-r--r--   0        0        0     3287 2023-04-04 08:06:51.472447 edgeimpulse_api-1.22.0/edgeimpulse_api/models/data_explorer_predictions_response.py
--rw-r--r--   0        0        0     2998 2023-04-04 08:06:50.298681 edgeimpulse_api-1.22.0/edgeimpulse_api/models/data_explorer_predictions_response_all_of.py
--rw-r--r--   0        0        0     2833 2023-04-04 08:06:52.206452 edgeimpulse_api-1.22.0/edgeimpulse_api/models/data_explorer_settings.py
--rw-r--r--   0        0        0     2144 2023-04-04 08:06:52.665547 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dataset_ratio_data.py
--rw-r--r--   0        0        0     2106 2023-04-04 08:06:51.156846 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dataset_ratio_data_ratio.py
--rw-r--r--   0        0        0     1893 2023-04-04 08:06:50.207735 edgeimpulse_api-1.22.0/edgeimpulse_api/models/delete_portal_file_request.py
--rw-r--r--   0        0        0     2225 2023-04-04 08:06:50.706399 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dependency_data.py
--rw-r--r--   0        0        0     2275 2023-04-04 08:06:51.173118 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_input_audio.py
--rw-r--r--   0        0        0     2150 2023-04-04 08:06:50.972452 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_input_image.py
--rw-r--r--   0        0        0     2150 2023-04-04 08:06:52.349447 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_input_other.py
--rw-r--r--   0        0        0     2479 2023-04-04 08:06:51.683372 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_input_time_series.py
--rw-r--r--   0        0        0     2339 2023-04-04 08:06:51.545565 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_model_classification.py
--rw-r--r--   0        0        0     2775 2023-04-04 08:06:51.478462 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_model_object_detection.py
--rw-r--r--   0        0        0     2195 2023-04-04 08:06:50.994451 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_model_regression.py
--rw-r--r--   0        0        0     4334 2023-04-04 08:06:51.945940 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_request.py
--rw-r--r--   0        0        0     2828 2023-04-04 08:06:50.854463 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_request_model_info.py
--rw-r--r--   0        0        0     6911 2023-04-04 08:06:52.689086 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_request_model_info_input.py
--rw-r--r--   0        0        0     6241 2023-04-04 08:06:52.296651 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_request_model_info_model.py
--rw-r--r--   0        0        0     5406 2023-04-04 08:06:51.028915 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deployment_target.py
--rw-r--r--   0        0        0     1921 2023-04-04 08:06:51.599339 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deployment_target_badge.py
--rw-r--r--   0        0        0      657 2023-04-04 08:06:50.252676 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deployment_target_engine.py
--rw-r--r--   0        0        0     2697 2023-04-04 08:06:51.523829 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deployment_targets_response.py
--rw-r--r--   0        0        0     2390 2023-04-04 08:06:50.809740 edgeimpulse_api-1.22.0/edgeimpulse_api/models/deployment_targets_response_all_of.py
--rw-r--r--   0        0        0     1978 2023-04-04 08:06:51.165349 edgeimpulse_api-1.22.0/edgeimpulse_api/models/development_board.py
--rw-r--r--   0        0        0     2826 2023-04-04 08:06:50.987109 edgeimpulse_api-1.22.0/edgeimpulse_api/models/development_boards_response.py
--rw-r--r--   0        0        0     2526 2023-04-04 08:06:50.308654 edgeimpulse_api-1.22.0/edgeimpulse_api/models/development_boards_response_all_of.py
--rw-r--r--   0        0        0     2025 2023-04-04 08:06:52.680726 edgeimpulse_api-1.22.0/edgeimpulse_api/models/development_keys.py
--rw-r--r--   0        0        0     2395 2023-04-04 08:06:52.044189 edgeimpulse_api-1.22.0/edgeimpulse_api/models/development_keys_response.py
--rw-r--r--   0        0        0     3672 2023-04-04 08:06:50.724196 edgeimpulse_api-1.22.0/edgeimpulse_api/models/device.py
--rw-r--r--   0        0        0     2194 2023-04-04 08:06:50.982570 edgeimpulse_api-1.22.0/edgeimpulse_api/models/device_name_response.py
--rw-r--r--   0        0        0     1915 2023-04-04 08:06:51.203886 edgeimpulse_api-1.22.0/edgeimpulse_api/models/device_name_response_all_of.py
--rw-r--r--   0        0        0     2226 2023-04-04 08:06:51.876878 edgeimpulse_api-1.22.0/edgeimpulse_api/models/device_sensors_inner.py
--rw-r--r--   0        0        0     2089 2023-04-04 08:06:50.925542 edgeimpulse_api-1.22.0/edgeimpulse_api/models/download.py
--rw-r--r--   0        0        0     1907 2023-04-04 08:06:50.846896 edgeimpulse_api-1.22.0/edgeimpulse_api/models/download_portal_file_request.py
--rw-r--r--   0        0        0     2255 2023-04-04 08:06:51.596380 edgeimpulse_api-1.22.0/edgeimpulse_api/models/download_portal_file_response.py
--rw-r--r--   0        0        0     1949 2023-04-04 08:06:52.300519 edgeimpulse_api-1.22.0/edgeimpulse_api/models/download_portal_file_response_all_of.py
--rw-r--r--   0        0        0     2719 2023-04-04 08:06:51.718012 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_autotuner_results.py
--rw-r--r--   0        0        0     2412 2023-04-04 08:06:51.218925 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_autotuner_results_all_of.py
--rw-r--r--   0        0        0     1963 2023-04-04 08:06:51.351954 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_autotuner_results_all_of_results.py
--rw-r--r--   0        0        0     2865 2023-04-04 08:06:50.255645 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_block.py
--rw-r--r--   0        0        0     1829 2023-04-04 08:06:49.881673 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_config_request.py
--rw-r--r--   0        0        0     3087 2023-04-04 08:06:51.517604 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_config_response.py
--rw-r--r--   0        0        0     2808 2023-04-04 08:06:51.486193 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_config_response_all_of.py
--rw-r--r--   0        0        0     3011 2023-04-04 08:06:50.792791 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_importance_response.py
--rw-r--r--   0        0        0     2723 2023-04-04 08:06:50.434826 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_importance_response_all_of.py
--rw-r--r--   0        0        0     2053 2023-04-04 08:06:50.272193 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_importance_response_all_of_features.py
--rw-r--r--   0        0        0     2567 2023-04-04 08:06:51.730100 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_importance_response_all_of_labels.py
--rw-r--r--   0        0        0     2211 2023-04-04 08:06:50.662750 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_labels_response.py
--rw-r--r--   0        0        0     1915 2023-04-04 08:06:49.850140 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_labels_response_all_of.py
--rw-r--r--   0        0        0     2289 2023-04-04 08:06:51.120686 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_group.py
--rw-r--r--   0        0        0     3623 2023-04-04 08:06:51.474473 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_group_item.py
--rw-r--r--   0        0        0     2185 2023-04-04 08:06:50.356902 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_group_item_select_options_inner.py
--rw-r--r--   0        0        0     2190 2023-04-04 08:06:50.564498 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_group_item_show_if.py
--rw-r--r--   0        0        0     4405 2023-04-04 08:06:51.952730 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_info.py
--rw-r--r--   0        0        0     2205 2023-04-04 08:06:51.648072 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_info_features.py
--rw-r--r--   0        0        0     1880 2023-04-04 08:06:50.984573 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_info_performance.py
--rw-r--r--   0        0        0     5139 2023-04-04 08:06:51.620077 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_metadata.py
--rw-r--r--   0        0        0     2020 2023-04-04 08:06:51.378841 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_metadata_included_samples_inner.py
--rw-r--r--   0        0        0     2561 2023-04-04 08:06:52.670524 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_metadata_output_config.py
--rw-r--r--   0        0        0     2526 2023-04-04 08:06:50.558710 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_metadata_output_config_shape.py
--rw-r--r--   0        0        0     5497 2023-04-04 08:06:51.622478 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_metadata_response.py
--rw-r--r--   0        0        0     3014 2023-04-04 08:06:51.327428 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_performance_all_variants_response.py
--rw-r--r--   0        0        0     2724 2023-04-04 08:06:50.289729 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_performance_all_variants_response_all_of.py
--rw-r--r--   0        0        0     2273 2023-04-04 08:06:51.530364 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_performance_all_variants_response_all_of_performance.py
--rw-r--r--   0        0        0     4634 2023-04-04 08:06:52.686050 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_graph.py
--rw-r--r--   0        0        0     1894 2023-04-04 08:06:50.702543 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_graph_axis_labels.py
--rw-r--r--   0        0        0     2146 2023-04-04 08:06:51.150313 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_request_without_features.py
--rw-r--r--   0        0        0     2025 2023-04-04 08:06:50.541395 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_request_without_features_read_only.py
--rw-r--r--   0        0        0     3497 2023-04-04 08:06:51.355563 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_response.py
--rw-r--r--   0        0        0     3218 2023-04-04 08:06:50.061607 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_response_all_of.py
--rw-r--r--   0        0        0     1964 2023-04-04 08:06:52.436997 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_response_all_of_performance.py
--rw-r--r--   0        0        0     4126 2023-04-04 08:06:50.245815 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_response_with_sample.py
--rw-r--r--   0        0        0     3859 2023-04-04 08:06:52.440958 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_response_with_sample_all_of.py
--rw-r--r--   0        0        0     3337 2023-04-04 08:06:50.584332 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_sample_features_response.py
--rw-r--r--   0        0        0     3037 2023-04-04 08:06:51.231188 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_sample_features_response_all_of.py
--rw-r--r--   0        0        0     2743 2023-04-04 08:06:51.573934 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_sample_features_response_all_of_data.py
--rw-r--r--   0        0        0     2208 2023-04-04 08:06:51.712074 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_sample_features_response_all_of_sample.py
--rw-r--r--   0        0        0     3348 2023-04-04 08:06:50.401622 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_trained_features_response.py
--rw-r--r--   0        0        0     3048 2023-04-04 08:06:50.861042 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_trained_features_response_all_of.py
--rw-r--r--   0        0        0     2768 2023-04-04 08:06:51.247615 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_trained_features_response_all_of_data.py
--rw-r--r--   0        0        0     2200 2023-04-04 08:06:50.338995 edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_trained_features_response_all_of_sample.py
--rw-r--r--   0        0        0     1888 2023-04-04 08:06:52.114388 edgeimpulse_api-1.22.0/edgeimpulse_api/models/edit_sample_label_request.py
--rw-r--r--   0        0        0     2651 2023-04-04 08:06:51.026219 edgeimpulse_api-1.22.0/edgeimpulse_api/models/evaluate_job_response.py
--rw-r--r--   0        0        0     2344 2023-04-04 08:06:50.616716 edgeimpulse_api-1.22.0/edgeimpulse_api/models/evaluate_job_response_all_of.py
--rw-r--r--   0        0        0     2094 2023-04-04 08:06:50.194966 edgeimpulse_api-1.22.0/edgeimpulse_api/models/evaluate_result_value.py
--rw-r--r--   0        0        0     2506 2023-04-04 08:06:50.432798 edgeimpulse_api-1.22.0/edgeimpulse_api/models/export_get_url_response.py
--rw-r--r--   0        0        0     2239 2023-04-04 08:06:50.050425 edgeimpulse_api-1.22.0/edgeimpulse_api/models/export_get_url_response_all_of.py
--rw-r--r--   0        0        0     2368 2023-04-04 08:06:50.482267 edgeimpulse_api-1.22.0/edgeimpulse_api/models/export_original_data_request.py
--rw-r--r--   0        0        0     2016 2023-04-04 08:06:51.408022 edgeimpulse_api-1.22.0/edgeimpulse_api/models/export_wav_data_request.py
--rw-r--r--   0        0        0     2201 2023-04-04 08:06:51.533485 edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_segment_sample_request.py
--rw-r--r--   0        0        0     2799 2023-04-04 08:06:52.583242 edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_segment_sample_response.py
--rw-r--r--   0        0        0     2492 2023-04-04 08:06:51.249896 edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_segment_sample_response_all_of.py
--rw-r--r--   0        0        0     2085 2023-04-04 08:06:51.277765 edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_segment_sample_response_all_of_segments.py
--rw-r--r--   0        0        0     2660 2023-04-04 08:06:50.729527 edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_user_response.py
--rw-r--r--   0        0        0     2353 2023-04-04 08:06:52.595970 edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_user_response_all_of.py
--rw-r--r--   0        0        0     2317 2023-04-04 08:06:50.549271 edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_user_response_all_of_users.py
--rw-r--r--   0        0        0     2502 2023-04-04 08:06:51.400304 edgeimpulse_api-1.22.0/edgeimpulse_api/models/generate_features_request.py
--rw-r--r--   0        0        0     2078 2023-04-04 08:06:50.571464 edgeimpulse_api-1.22.0/edgeimpulse_api/models/generic_api_response.py
--rw-r--r--   0        0        0     2693 2023-04-04 08:06:51.974081 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_all_third_party_auth_response.py
--rw-r--r--   0        0        0     2386 2023-04-04 08:06:52.347380 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_all_third_party_auth_response_all_of.py
--rw-r--r--   0        0        0     2708 2023-04-04 08:06:50.998548 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_all_whitelabels_response.py
--rw-r--r--   0        0        0     2401 2023-04-04 08:06:50.068109 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_all_whitelabels_response_all_of.py
--rw-r--r--   0        0        0     3395 2023-04-04 08:06:50.656313 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_data_explorer_features_response.py
--rw-r--r--   0        0        0     3117 2023-04-04 08:06:51.162208 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_data_explorer_features_response_all_of.py
--rw-r--r--   0        0        0     3747 2023-04-04 08:06:52.587810 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_data_explorer_settings_response.py
--rw-r--r--   0        0        0     2397 2023-04-04 08:06:51.978031 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_data_explorer_settings_response_all_of.py
--rw-r--r--   0        0        0     2344 2023-04-04 08:06:51.541517 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_deployment_response.py
--rw-r--r--   0        0        0     2066 2023-04-04 08:06:52.451864 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_deployment_response_all_of.py
--rw-r--r--   0        0        0     2429 2023-04-04 08:06:51.235627 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_device_response.py
--rw-r--r--   0        0        0     2132 2023-04-04 08:06:51.879016 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_device_response_all_of.py
--rw-r--r--   0        0        0     3925 2023-04-04 08:06:51.842846 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_impulse_blocks_response.py
--rw-r--r--   0        0        0     3625 2023-04-04 08:06:50.394285 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_impulse_blocks_response_all_of.py
--rw-r--r--   0        0        0     2449 2023-04-04 08:06:49.988767 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_impulse_response.py
--rw-r--r--   0        0        0     2152 2023-04-04 08:06:51.689708 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_impulse_response_all_of.py
--rw-r--r--   0        0        0     2369 2023-04-04 08:06:51.113696 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_job_response.py
--rw-r--r--   0        0        0     2072 2023-04-04 08:06:51.722393 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_job_response_all_of.py
--rw-r--r--   0        0        0     2680 2023-04-04 08:06:51.928505 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_jwt_token_request.py
--rw-r--r--   0        0        0     2461 2023-04-04 08:06:50.863956 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_jwt_token_response.py
--rw-r--r--   0        0        0     2182 2023-04-04 08:06:50.745907 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_jwt_token_response_all_of.py
--rw-r--r--   0        0        0     2972 2023-04-04 08:06:50.226835 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_last_deployment_build_response.py
--rw-r--r--   0        0        0     2694 2023-04-04 08:06:51.122462 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_last_deployment_build_response_all_of.py
--rw-r--r--   0        0        0     2864 2023-04-04 08:06:52.036227 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_last_deployment_build_response_all_of_last_build.py
--rw-r--r--   0        0        0     2567 2023-04-04 08:06:52.630810 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_notes_response.py
--rw-r--r--   0        0        0     2260 2023-04-04 08:06:51.699867 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_notes_response_all_of.py
--rw-r--r--   0        0        0     2556 2023-04-04 08:06:52.648729 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_data_item_response.py
--rw-r--r--   0        0        0     2232 2023-04-04 08:06:52.201790 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_data_item_response_all_of.py
--rw-r--r--   0        0        0     2571 2023-04-04 08:06:51.268161 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_dataset_response.py
--rw-r--r--   0        0        0     2247 2023-04-04 08:06:51.333525 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_dataset_response_all_of.py
--rw-r--r--   0        0        0     2598 2023-04-04 08:06:51.705134 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_pipelines_response.py
--rw-r--r--   0        0        0     2274 2023-04-04 08:06:50.232958 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_pipelines_response_all_of.py
--rw-r--r--   0        0        0     3665 2023-04-04 08:06:52.291807 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_portal_response.py
--rw-r--r--   0        0        0     3386 2023-04-04 08:06:50.370944 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_portal_response_all_of.py
--rw-r--r--   0        0        0     2318 2023-04-04 08:06:50.775473 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_projects_data_count_response.py
--rw-r--r--   0        0        0     2900 2023-04-04 08:06:50.184611 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_ground_truth_response.py
--rw-r--r--   0        0        0     2593 2023-04-04 08:06:51.095843 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_ground_truth_response_all_of.py
--rw-r--r--   0        0        0     3007 2023-04-04 08:06:51.197557 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_parameter_sets_response.py
--rw-r--r--   0        0        0     2707 2023-04-04 08:06:50.319802 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_parameter_sets_response_all_of.py
--rw-r--r--   0        0        0     2717 2023-04-04 08:06:50.094339 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_parameters_response.py
--rw-r--r--   0        0        0     2420 2023-04-04 08:06:52.257182 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_parameters_response_all_of.py
--rw-r--r--   0        0        0     2917 2023-04-04 08:06:50.603874 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_raw_result_response.py
--rw-r--r--   0        0        0     2610 2023-04-04 08:06:51.032122 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_raw_result_response_all_of.py
--rw-r--r--   0        0        0     3146 2023-04-04 08:06:49.843103 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_status_response.py
--rw-r--r--   0        0        0     2879 2023-04-04 08:06:51.101116 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_status_response_all_of.py
--rw-r--r--   0        0        0     3756 2023-04-04 08:06:51.205953 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_pretrained_model_response.py
--rw-r--r--   0        0        0     3478 2023-04-04 08:06:51.691347 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_pretrained_model_response_all_of.py
--rw-r--r--   0        0        0     3856 2023-04-04 08:06:50.591172 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_pretrained_model_response_all_of_model.py
--rw-r--r--   0        0        0     2973 2023-04-04 08:06:51.046466 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_pretrained_model_response_all_of_model_info.py
--rw-r--r--   0        0        0     3053 2023-04-04 08:06:50.581565 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_pretrained_model_response_all_of_model_profile_info.py
--rw-r--r--   0        0        0     2392 2023-04-04 08:06:50.652264 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_public_metrics_response.py
--rw-r--r--   0        0        0     2068 2023-04-04 08:06:51.405490 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_public_metrics_response_all_of.py
--rw-r--r--   0        0        0     2762 2023-04-04 08:06:51.229253 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_sample_metadata_response.py
--rw-r--r--   0        0        0     3039 2023-04-04 08:06:52.657202 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_sample_response.py
--rw-r--r--   0        0        0     2457 2023-04-04 08:06:51.766195 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_syntiant_posterior_response.py
--rw-r--r--   0        0        0     2179 2023-04-04 08:06:51.724053 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_syntiant_posterior_response_all_of.py
--rw-r--r--   0        0        0     2409 2023-04-04 08:06:51.006657 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_theme_response.py
--rw-r--r--   0        0        0     2112 2023-04-04 08:06:50.929487 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_theme_response_all_of.py
--rw-r--r--   0        0        0     2587 2023-04-04 08:06:50.856968 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_themes_response.py
--rw-r--r--   0        0        0     2280 2023-04-04 08:06:52.285803 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_themes_response_all_of.py
--rw-r--r--   0        0        0     2490 2023-04-04 08:06:51.431870 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_third_party_auth_response.py
--rw-r--r--   0        0        0     2166 2023-04-04 08:06:50.324299 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_third_party_auth_response_all_of.py
--rw-r--r--   0        0        0     2698 2023-04-04 08:06:51.428932 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_user_need_to_set_password_response.py
--rw-r--r--   0        0        0     2431 2023-04-04 08:06:51.380751 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_user_need_to_set_password_response_all_of.py
--rw-r--r--   0        0        0     7198 2023-04-04 08:06:50.594479 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_user_response.py
--rw-r--r--   0        0        0     5558 2023-04-04 08:06:51.298568 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_user_response_all_of.py
--rw-r--r--   0        0        0     2204 2023-04-04 08:06:51.949272 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_user_response_all_of_whitelabels.py
--rw-r--r--   0        0        0     2302 2023-04-04 08:06:51.112050 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_whitelabel_domain_response.py
--rw-r--r--   0        0        0     2016 2023-04-04 08:06:51.103463 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_whitelabel_domain_response_all_of.py
--rw-r--r--   0        0        0     2509 2023-04-04 08:06:51.275036 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_whitelabel_response.py
--rw-r--r--   0        0        0     2212 2023-04-04 08:06:51.452373 edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_whitelabel_response_all_of.py
--rw-r--r--   0        0        0     2771 2023-04-04 08:06:50.695377 edgeimpulse_api-1.22.0/edgeimpulse_api/models/has_data_explorer_features_response.py
--rw-r--r--   0        0        0     2493 2023-04-04 08:06:51.561675 edgeimpulse_api-1.22.0/edgeimpulse_api/models/has_data_explorer_features_response_all_of.py
--rw-r--r--   0        0        0     3733 2023-04-04 08:06:50.493067 edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse.py
--rw-r--r--   0        0        0     6718 2023-04-04 08:06:50.428850 edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse_block_version.py
--rw-r--r--   0        0        0     6809 2023-04-04 08:06:51.601610 edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse_dsp_block.py
--rw-r--r--   0        0        0     1962 2023-04-04 08:06:51.667685 edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse_dsp_block_organization.py
--rw-r--r--   0        0        0     8971 2023-04-04 08:06:51.513384 edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse_input_block.py
--rw-r--r--   0        0        0     5607 2023-04-04 08:06:51.239600 edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse_learn_block.py
--rw-r--r--   0        0        0     2458 2023-04-04 08:06:52.619078 edgeimpulse_api-1.22.0/edgeimpulse_api/models/input_block.py
--rw-r--r--   0        0        0     2451 2023-04-04 08:06:51.180470 edgeimpulse_api-1.22.0/edgeimpulse_api/models/invite_organization_member_request.py
--rw-r--r--   0        0        0     3430 2023-04-04 08:06:50.869153 edgeimpulse_api-1.22.0/edgeimpulse_api/models/job.py
--rw-r--r--   0        0        0     2708 2023-04-04 08:06:51.614013 edgeimpulse_api-1.22.0/edgeimpulse_api/models/job_summary_response.py
--rw-r--r--   0        0        0     2401 2023-04-04 08:06:50.125911 edgeimpulse_api-1.22.0/edgeimpulse_api/models/job_summary_response_all_of.py
--rw-r--r--   0        0        0     2084 2023-04-04 08:06:52.306395 edgeimpulse_api-1.22.0/edgeimpulse_api/models/job_summary_response_all_of_summary.py
--rw-r--r--   0        0        0     2505 2023-04-04 08:06:52.491993 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_layer.py
--rw-r--r--   0        0        0     2088 2023-04-04 08:06:52.552928 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_layer_input.py
--rw-r--r--   0        0        0     2096 2023-04-04 08:06:51.716273 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_layer_output.py
--rw-r--r--   0        0        0     5184 2023-04-04 08:06:51.521704 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_metadata.py
--rw-r--r--   0        0        0     4917 2023-04-04 08:06:51.754478 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_metadata_all_of.py
--rw-r--r--   0        0        0     4787 2023-04-04 08:06:51.169829 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_metadata_metrics.py
--rw-r--r--   0        0        0     3223 2023-04-04 08:06:51.547277 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_metadata_metrics_on_device_performance_inner.py
--rw-r--r--   0        0        0     2492 2023-04-04 08:06:51.498221 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_metadata_metrics_on_device_performance_inner_tflite.py
--rw-r--r--   0        0        0      562 2023-04-04 08:06:51.672011 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_type_enum.py
--rw-r--r--   0        0        0     9301 2023-04-04 08:06:49.890854 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_response.py
--rw-r--r--   0        0        0     9034 2023-04-04 08:06:50.645810 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_response_all_of.py
--rw-r--r--   0        0        0     3387 2023-04-04 08:06:51.677345 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_visual_layer.py
--rw-r--r--   0        0        0     2310 2023-04-04 08:06:51.435734 edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_visual_layer_type.py
--rw-r--r--   0        0        0     2524 2023-04-04 08:06:50.000845 edgeimpulse_api-1.22.0/edgeimpulse_api/models/last_modification_date_response.py
--rw-r--r--   0        0        0     2234 2023-04-04 08:06:50.444833 edgeimpulse_api-1.22.0/edgeimpulse_api/models/last_modification_date_response_all_of.py
--rw-r--r--   0        0        0     2628 2023-04-04 08:06:51.464862 edgeimpulse_api-1.22.0/edgeimpulse_api/models/latency_device.py
--rw-r--r--   0        0        0     2419 2023-04-04 08:06:50.262823 edgeimpulse_api-1.22.0/edgeimpulse_api/models/learn_block.py
--rw-r--r--   0        0        0      883 2023-04-04 08:06:51.759965 edgeimpulse_api-1.22.0/edgeimpulse_api/models/learn_block_type.py
--rw-r--r--   0        0        0     2783 2023-04-04 08:06:51.645616 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_api_keys_response.py
--rw-r--r--   0        0        0     2483 2023-04-04 08:06:50.302879 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_api_keys_response_all_of.py
--rw-r--r--   0        0        0     2677 2023-04-04 08:06:51.757044 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_api_keys_response_all_of_api_keys.py
--rw-r--r--   0        0        0     2625 2023-04-04 08:06:51.496086 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_devices_response.py
--rw-r--r--   0        0        0     2328 2023-04-04 08:06:49.862333 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_devices_response_all_of.py
--rw-r--r--   0        0        0     2721 2023-04-04 08:06:50.779044 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_email_response.py
--rw-r--r--   0        0        0     2421 2023-04-04 08:06:51.118299 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_email_response_all_of.py
--rw-r--r--   0        0        0     2913 2023-04-04 08:06:51.289719 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_email_response_all_of_emails.py
--rw-r--r--   0        0        0     2808 2023-04-04 08:06:51.701934 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_hmac_keys_response.py
--rw-r--r--   0        0        0     2508 2023-04-04 08:06:51.201350 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_hmac_keys_response_all_of.py
--rw-r--r--   0        0        0     2376 2023-04-04 08:06:50.957047 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_hmac_keys_response_all_of_hmac_keys.py
--rw-r--r--   0        0        0     2740 2023-04-04 08:06:49.993180 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_jobs_response.py
--rw-r--r--   0        0        0     2440 2023-04-04 08:06:51.021039 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_jobs_response_all_of.py
--rw-r--r--   0        0        0     2195 2023-04-04 08:06:51.313078 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_models_response.py
--rw-r--r--   0        0        0     1905 2023-04-04 08:06:52.678063 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_models_response_all_of.py
--rw-r--r--   0        0        0     2916 2023-04-04 08:06:52.243167 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_api_keys_response.py
--rw-r--r--   0        0        0     2616 2023-04-04 08:06:50.473000 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_api_keys_response_all_of.py
--rw-r--r--   0        0        0     2755 2023-04-04 08:06:50.686735 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_api_keys_response_all_of_api_keys.py
--rw-r--r--   0        0        0     2852 2023-04-04 08:06:50.682443 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_response.py
--rw-r--r--   0        0        0     2545 2023-04-04 08:06:52.608539 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_response_all_of.py
--rw-r--r--   0        0        0     2914 2023-04-04 08:06:52.500496 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_response_all_of_buckets.py
--rw-r--r--   0        0        0     2897 2023-04-04 08:06:51.446063 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_user_response.py
--rw-r--r--   0        0        0     2590 2023-04-04 08:06:51.255189 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_user_response_all_of.py
--rw-r--r--   0        0        0     3034 2023-04-04 08:06:50.629097 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_user_response_all_of_buckets.py
--rw-r--r--   0        0        0     3305 2023-04-04 08:06:51.543825 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_data_response.py
--rw-r--r--   0        0        0     3026 2023-04-04 08:06:50.351887 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_data_response_all_of.py
--rw-r--r--   0        0        0     3425 2023-04-04 08:06:52.645552 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_data_response_all_of_data.py
--rw-r--r--   0        0        0     2882 2023-04-04 08:06:52.269301 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_deploy_blocks_response.py
--rw-r--r--   0        0        0     2582 2023-04-04 08:06:50.335642 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_deploy_blocks_response_all_of.py
--rw-r--r--   0        0        0     2819 2023-04-04 08:06:50.879030 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_dsp_blocks_response.py
--rw-r--r--   0        0        0     2519 2023-04-04 08:06:52.056004 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_dsp_blocks_response_all_of.py
--rw-r--r--   0        0        0     3348 2023-04-04 08:06:50.765444 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_files_response.py
--rw-r--r--   0        0        0     3069 2023-04-04 08:06:51.505027 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_files_response_all_of.py
--rw-r--r--   0        0        0     2787 2023-04-04 08:06:50.759548 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_pipelines_response.py
--rw-r--r--   0        0        0     2480 2023-04-04 08:06:50.295363 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_pipelines_response_all_of.py
--rw-r--r--   0        0        0     2852 2023-04-04 08:06:51.283945 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_portals_response.py
--rw-r--r--   0        0        0     2545 2023-04-04 08:06:51.519503 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_portals_response_all_of.py
--rw-r--r--   0        0        0     2739 2023-04-04 08:06:52.162074 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_portals_response_all_of_portals.py
--rw-r--r--   0        0        0     3444 2023-04-04 08:06:50.552574 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_projects_data_response.py
--rw-r--r--   0        0        0     3137 2023-04-04 08:06:50.732022 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_projects_data_response_all_of.py
--rw-r--r--   0        0        0     2266 2023-04-04 08:06:50.989732 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_projects_data_response_all_of_projects.py
--rw-r--r--   0        0        0     2718 2023-04-04 08:06:51.272003 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_projects_response.py
--rw-r--r--   0        0        0     2411 2023-04-04 08:06:50.944924 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_projects_response_all_of.py
--rw-r--r--   0        0        0     2852 2023-04-04 08:06:50.215207 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_secrets_response.py
--rw-r--r--   0        0        0     2545 2023-04-04 08:06:50.247835 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_secrets_response_all_of.py
--rw-r--r--   0        0        0     2260 2023-04-04 08:06:52.010035 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_secrets_response_all_of_secrets.py
--rw-r--r--   0        0        0     3098 2023-04-04 08:06:50.635999 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_transfer_learning_blocks_response.py
--rw-r--r--   0        0        0     2798 2023-04-04 08:06:52.281179 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_transfer_learning_blocks_response_all_of.py
--rw-r--r--   0        0        0     3050 2023-04-04 08:06:51.075848 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_transformation_blocks_response.py
--rw-r--r--   0        0        0     2750 2023-04-04 08:06:51.382514 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_transformation_blocks_response_all_of.py
--rw-r--r--   0        0        0     2781 2023-04-04 08:06:51.557329 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organizations_response.py
--rw-r--r--   0        0        0     2481 2023-04-04 08:06:52.700062 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organizations_response_all_of.py
--rw-r--r--   0        0        0     1932 2023-04-04 08:06:50.953633 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_portal_files_in_folder_request.py
--rw-r--r--   0        0        0     2708 2023-04-04 08:06:51.665980 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_portal_files_in_folder_response.py
--rw-r--r--   0        0        0     2411 2023-04-04 08:06:51.040620 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_portal_files_in_folder_response_all_of.py
--rw-r--r--   0        0        0     2285 2023-04-04 08:06:51.416145 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_projects.py
--rw-r--r--   0        0        0     2676 2023-04-04 08:06:52.692496 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_projects_response.py
--rw-r--r--   0        0        0     2548 2023-04-04 08:06:51.195163 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_public_projects.py
--rw-r--r--   0        0        0     2939 2023-04-04 08:06:50.547958 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_public_projects_response.py
--rw-r--r--   0        0        0     2810 2023-04-04 08:06:51.476052 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_public_versions_response.py
--rw-r--r--   0        0        0     2503 2023-04-04 08:06:51.410073 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_public_versions_response_all_of.py
--rw-r--r--   0        0        0     2285 2023-04-04 08:06:52.344114 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_public_versions_response_all_of_versions.py
--rw-r--r--   0        0        0     2749 2023-04-04 08:06:50.513040 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_samples_response.py
--rw-r--r--   0        0        0     2449 2023-04-04 08:06:50.932891 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_samples_response_all_of.py
--rw-r--r--   0        0        0     3928 2023-04-04 08:06:50.828090 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_versions_response.py
--rw-r--r--   0        0        0     3628 2023-04-04 08:06:50.274820 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_versions_response_all_of.py
--rw-r--r--   0        0        0     2348 2023-04-04 08:06:52.620965 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_versions_response_all_of_bucket.py
--rw-r--r--   0        0        0     2048 2023-04-04 08:06:50.718990 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_versions_response_all_of_custom_learn_blocks.py
--rw-r--r--   0        0        0     3955 2023-04-04 08:06:50.676878 edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_versions_response_all_of_versions.py
--rw-r--r--   0        0        0     2895 2023-04-04 08:06:52.302824 edgeimpulse_api-1.22.0/edgeimpulse_api/models/log_stdout_response.py
--rw-r--r--   0        0        0     2595 2023-04-04 08:06:52.495426 edgeimpulse_api-1.22.0/edgeimpulse_api/models/log_stdout_response_all_of.py
--rw-r--r--   0        0        0     2436 2023-04-04 08:06:50.788816 edgeimpulse_api-1.22.0/edgeimpulse_api/models/log_stdout_response_all_of_stdout.py
--rw-r--r--   0        0        0     2186 2023-04-04 08:06:51.011744 edgeimpulse_api-1.22.0/edgeimpulse_api/models/log_website_pageview_request.py
--rw-r--r--   0        0        0     2212 2023-04-04 08:06:50.155422 edgeimpulse_api-1.22.0/edgeimpulse_api/models/login_response.py
--rw-r--r--   0        0        0     1906 2023-04-04 08:06:51.609290 edgeimpulse_api-1.22.0/edgeimpulse_api/models/login_response_all_of.py
--rw-r--r--   0        0        0     2516 2023-04-04 08:06:51.901112 edgeimpulse_api-1.22.0/edgeimpulse_api/models/model_prediction.py
--rw-r--r--   0        0        0     5041 2023-04-04 08:06:52.563124 edgeimpulse_api-1.22.0/edgeimpulse_api/models/model_variant_stats.py
--rw-r--r--   0        0        0     2123 2023-04-04 08:06:51.396477 edgeimpulse_api-1.22.0/edgeimpulse_api/models/move_raw_data_request.py
--rw-r--r--   0        0        0     2682 2023-04-04 08:06:52.507147 edgeimpulse_api-1.22.0/edgeimpulse_api/models/note.py
--rw-r--r--   0        0        0     2216 2023-04-04 08:06:51.402442 edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_auto_label_request.py
--rw-r--r--   0        0        0     2989 2023-04-04 08:06:51.346690 edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_auto_label_response.py
--rw-r--r--   0        0        0     2700 2023-04-04 08:06:50.546632 edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_auto_label_response_all_of.py
--rw-r--r--   0        0        0     2270 2023-04-04 08:06:52.592475 edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_auto_label_response_all_of_results.py
--rw-r--r--   0        0        0     2363 2023-04-04 08:06:51.714155 edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_label_queue_count_response.py
--rw-r--r--   0        0        0     2046 2023-04-04 08:06:50.784001 edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_label_queue_count_response_all_of.py
--rw-r--r--   0        0        0     2882 2023-04-04 08:06:52.668311 edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_label_queue_response.py
--rw-r--r--   0        0        0     2575 2023-04-04 08:06:51.907702 edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_label_queue_response_all_of.py
--rw-r--r--   0        0        0      621 2023-04-04 08:06:52.239651 edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_last_layer.py
--rw-r--r--   0        0        0     6413 2023-04-04 08:06:51.582987 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_config.py
--rw-r--r--   0        0        0     6866 2023-04-04 08:06:52.661966 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_config_response.py
--rw-r--r--   0        0        0     1915 2023-04-04 08:06:51.492266 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_config_response_all_of.py
--rw-r--r--   0        0        0     2062 2023-04-04 08:06:51.482840 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_config_target_device.py
--rw-r--r--   0        0        0     2266 2023-04-04 08:06:50.088887 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_dsp_parameters_response.py
--rw-r--r--   0        0        0     1959 2023-04-04 08:06:52.432697 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_dsp_parameters_response_all_of.py
--rw-r--r--   0        0        0     2751 2023-04-04 08:06:52.407319 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_space_response.py
--rw-r--r--   0        0        0     2451 2023-04-04 08:06:49.979209 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_space_response_all_of.py
--rw-r--r--   0        0        0     4892 2023-04-04 08:06:50.611343 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_state_response.py
--rw-r--r--   0        0        0     4613 2023-04-04 08:06:51.038241 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_state_response_all_of.py
--rw-r--r--   0        0        0     3414 2023-04-04 08:06:50.666550 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_state_response_all_of_status.py
--rw-r--r--   0        0        0     2361 2023-04-04 08:06:52.080548 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_state_response_all_of_workers.py
--rw-r--r--   0        0        0     2755 2023-04-04 08:06:51.686064 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_transfer_learning_models_response.py
--rw-r--r--   0        0        0     2458 2023-04-04 08:06:52.642330 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_transfer_learning_models_response_all_of.py
--rw-r--r--   0        0        0     4677 2023-04-04 08:06:51.115756 edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_transfer_learning_models_response_all_of_models.py
--rw-r--r--   0        0        0     3769 2023-04-04 08:06:50.737752 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization.py
--rw-r--r--   0        0        0     2354 2023-04-04 08:06:51.674670 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_add_data_folder_request.py
--rw-r--r--   0        0        0     2493 2023-04-04 08:06:52.709386 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_add_data_folder_response.py
--rw-r--r--   0        0        0     2204 2023-04-04 08:06:52.639672 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_add_data_folder_response_all_of.py
--rw-r--r--   0        0        0     8195 2023-04-04 08:06:51.738726 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project.py
--rw-r--r--   0        0        0     4773 2023-04-04 08:06:51.213750 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_request.py
--rw-r--r--   0        0        0     2538 2023-04-04 08:06:50.344461 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_response.py
--rw-r--r--   0        0        0     2232 2023-04-04 08:06:52.663766 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_response_all_of.py
--rw-r--r--   0        0        0     2699 2023-04-04 08:06:52.712196 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_status_response.py
--rw-r--r--   0        0        0     2402 2023-04-04 08:06:51.186663 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_status_response_all_of.py
--rw-r--r--   0        0        0     2496 2023-04-04 08:06:50.671787 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_transformation_summary.py
--rw-r--r--   0        0        0     8922 2023-04-04 08:06:51.292413 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_with_files.py
--rw-r--r--   0        0        0     2553 2023-04-04 08:06:51.611129 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_with_files_all_of.py
--rw-r--r--   0        0        0     2881 2023-04-04 08:06:52.653318 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_with_files_all_of_files.py
--rw-r--r--   0        0        0     3471 2023-04-04 08:06:50.805315 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_data_item.py
--rw-r--r--   0        0        0     2098 2023-04-04 08:06:50.771436 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_data_item_files_inner.py
--rw-r--r--   0        0        0     2512 2023-04-04 08:06:51.745240 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_dataset.py
--rw-r--r--   0        0        0     4684 2023-04-04 08:06:50.198579 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_deploy_block.py
--rw-r--r--   0        0        0     3641 2023-04-04 08:06:51.580159 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_dsp_block.py
--rw-r--r--   0        0        0     3032 2023-04-04 08:06:51.726161 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_get_create_projects_response.py
--rw-r--r--   0        0        0     2732 2023-04-04 08:06:50.887649 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_get_create_projects_response_all_of.py
--rw-r--r--   0        0        0     5304 2023-04-04 08:06:52.354496 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_get_create_projects_response_all_of_jobs.py
--rw-r--r--   0        0        0     5933 2023-04-04 08:06:51.320739 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_info_response.py
--rw-r--r--   0        0        0     5643 2023-04-04 08:06:51.442181 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_info_response_all_of.py
--rw-r--r--   0        0        0     2453 2023-04-04 08:06:50.217939 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_info_response_all_of_default_compute_limits.py
--rw-r--r--   0        0        0     2595 2023-04-04 08:06:51.526296 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_info_response_all_of_entitlement_limits.py
--rw-r--r--   0        0        0     2634 2023-04-04 08:06:51.252184 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_metrics_response.py
--rw-r--r--   0        0        0     2310 2023-04-04 08:06:50.398057 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_metrics_response_all_of.py
--rw-r--r--   0        0        0     3486 2023-04-04 08:06:50.438232 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_metrics_response_all_of_metrics.py
--rw-r--r--   0        0        0     6109 2023-04-04 08:06:51.687920 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline.py
--rw-r--r--   0        0        0     2590 2023-04-04 08:06:51.413596 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_feeding_into_dataset.py
--rw-r--r--   0        0        0     2270 2023-04-04 08:06:52.510266 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_feeding_into_project.py
--rw-r--r--   0        0        0     2309 2023-04-04 08:06:50.968004 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_item_count.py
--rw-r--r--   0        0        0     4104 2023-04-04 08:06:51.265165 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_run.py
--rw-r--r--   0        0        0     4810 2023-04-04 08:06:50.749593 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_run_step.py
--rw-r--r--   0        0        0     4410 2023-04-04 08:06:51.869548 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_step.py
--rw-r--r--   0        0        0     2346 2023-04-04 08:06:50.699130 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_projects_data_batch_disable_response.py
--rw-r--r--   0        0        0     2339 2023-04-04 08:06:52.365200 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_projects_data_batch_enable_response.py
--rw-r--r--   0        0        0     2032 2023-04-04 08:06:51.375592 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_projects_data_batch_request.py
--rw-r--r--   0        0        0     4409 2023-04-04 08:06:50.866407 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_transfer_learning_block.py
--rw-r--r--   0        0        0      611 2023-04-04 08:06:51.959487 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_transfer_learning_operates_on.py
--rw-r--r--   0        0        0     5163 2023-04-04 08:06:51.466915 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_transformation_block.py
--rw-r--r--   0        0        0     3884 2023-04-04 08:06:49.853804 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_update_pipeline_body.py
--rw-r--r--   0        0        0     3375 2023-04-04 08:06:52.537533 edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_user.py
--rw-r--r--   0        0        0     2099 2023-04-04 08:06:50.133621 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_detection.py
--rw-r--r--   0        0        0     3429 2023-04-04 08:06:51.176539 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_false_positive.py
--rw-r--r--   0        0        0     3765 2023-04-04 08:06:51.144535 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_ground_truth.py
--rw-r--r--   0        0        0     2472 2023-04-04 08:06:50.164817 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_ground_truth_samples_inner.py
--rw-r--r--   0        0        0     4875 2023-04-04 08:06:50.100879 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_parameter_set.py
--rw-r--r--   0        0        0     2250 2023-04-04 08:06:51.586634 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_parameter_set_aggregate_stats.py
--rw-r--r--   0        0        0     4087 2023-04-04 08:06:50.341045 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_parameter_set_stats_inner.py
--rw-r--r--   0        0        0     3002 2023-04-04 08:06:52.674945 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_parameters.py
--rw-r--r--   0        0        0     2580 2023-04-04 08:06:50.975610 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_parameters_standard.py
--rw-r--r--   0        0        0     2245 2023-04-04 08:06:51.309489 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_raw_detection.py
--rw-r--r--   0        0        0     2361 2023-04-04 08:06:51.797158 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_save_parameter_set_request.py
--rw-r--r--   0        0        0     2407 2023-04-04 08:06:51.616778 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_upload_labeled_audio_response.py
--rw-r--r--   0        0        0     2101 2023-04-04 08:06:50.554922 edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_upload_labeled_audio_response_all_of.py
--rw-r--r--   0        0        0     2206 2023-04-04 08:06:51.733136 edgeimpulse_api-1.22.0/edgeimpulse_api/models/portal_file.py
--rw-r--r--   0        0        0     2408 2023-04-04 08:06:50.807315 edgeimpulse_api-1.22.0/edgeimpulse_api/models/portal_info_response.py
--rw-r--r--   0        0        0     2661 2023-04-04 08:06:51.245139 edgeimpulse_api-1.22.0/edgeimpulse_api/models/pretrained_model_tensor.py
--rw-r--r--   0        0        0     2950 2023-04-04 08:06:51.568476 edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_info.py
--rw-r--r--   0        0        0     2635 2023-04-04 08:06:51.182818 edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_info_memory.py
--rw-r--r--   0        0        0     1913 2023-04-04 08:06:51.488823 edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_info_memory_eon.py
--rw-r--r--   0        0        0     2060 2023-04-04 08:06:51.167361 edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_info_memory_tflite.py
--rw-r--r--   0        0        0     4330 2023-04-04 08:06:52.178226 edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_table.py
--rw-r--r--   0        0        0     2775 2023-04-04 08:06:50.964235 edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_table_mcu.py
--rw-r--r--   0        0        0     2560 2023-04-04 08:06:51.241603 edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_table_mcu_memory.py
--rw-r--r--   0        0        0     2245 2023-04-04 08:06:51.070273 edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_table_mpu.py
--rw-r--r--   0        0        0     2196 2023-04-04 08:06:51.963601 edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_tf_lite_request.py
--rw-r--r--   0        0        0     3287 2023-04-04 08:06:51.449027 edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_tf_lite_response.py
--rw-r--r--   0        0        0     6134 2023-04-04 08:06:52.627465 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project.py
--rw-r--r--   0        0        0     3266 2023-04-04 08:06:50.874657 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_collaborator.py
--rw-r--r--   0        0        0     1890 2023-04-04 08:06:51.626050 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_collaborator_all_of.py
--rw-r--r--   0        0        0     2411 2023-04-04 08:06:52.253314 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_data_axes_summary_response.py
--rw-r--r--   0        0        0     2111 2023-04-04 08:06:50.129509 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_data_axes_summary_response_all_of.py
--rw-r--r--   0        0        0     2276 2023-04-04 08:06:51.190012 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_data_interval_response.py
--rw-r--r--   0        0        0     1959 2023-04-04 08:06:50.658936 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_data_interval_response_all_of.py
--rw-r--r--   0        0        0     2230 2023-04-04 08:06:50.293406 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_data_summary.py
--rw-r--r--   0        0        0     6310 2023-04-04 08:06:51.924415 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_deployment_target.py
--rw-r--r--   0        0        0     2701 2023-04-04 08:06:52.549587 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_deployment_target_all_of.py
--rw-r--r--   0        0        0     2775 2023-04-04 08:06:51.370144 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_deployment_targets_response.py
--rw-r--r--   0        0        0     2468 2023-04-04 08:06:50.224490 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_deployment_targets_response_all_of.py
--rw-r--r--   0        0        0     2675 2023-04-04 08:06:50.257532 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_downloads_response.py
--rw-r--r--   0        0        0     2368 2023-04-04 08:06:51.125299 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_downloads_response_all_of.py
--rw-r--r--   0        0        0    13741 2023-04-04 08:06:52.636311 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response.py
--rw-r--r--   0        0        0    13474 2023-04-04 08:06:52.659725 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of.py
--rw-r--r--   0        0        0     3125 2023-04-04 08:06:49.934222 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_acquisition_settings.py
--rw-r--r--   0        0        0     2718 2023-04-04 08:06:52.527319 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_compute_time.py
--rw-r--r--   0        0        0     2992 2023-04-04 08:06:51.368295 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_data_summary_per_category.py
--rw-r--r--   0        0        0     2803 2023-04-04 08:06:50.621796 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_deploy_settings.py
--rw-r--r--   0        0        0     2334 2023-04-04 08:06:52.147328 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_experiments.py
--rw-r--r--   0        0        0     2280 2023-04-04 08:06:52.316619 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_impulse.py
--rw-r--r--   0        0        0     2721 2023-04-04 08:06:51.363970 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_performance.py
--rw-r--r--   0        0        0     1972 2023-04-04 08:06:52.498087 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_readme.py
--rw-r--r--   0        0        0     2220 2023-04-04 08:06:51.553997 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_show_getting_started_wizard.py
--rw-r--r--   0        0        0     2730 2023-04-04 08:06:50.600079 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_urls.py
--rw-r--r--   0        0        0     2473 2023-04-04 08:06:50.407609 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_summary_response.py
--rw-r--r--   0        0        0     2167 2023-04-04 08:06:50.801981 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_summary_response_all_of.py
--rw-r--r--   0        0        0     3549 2023-04-04 08:06:50.159425 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_private_data.py
--rw-r--r--   0        0        0     4391 2023-04-04 08:06:50.147289 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_public_data.py
--rw-r--r--   0        0        0     1923 2023-04-04 08:06:51.340091 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_public_data_readme.py
--rw-r--r--   0        0        0     2399 2023-04-04 08:06:52.503373 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_sample_metadata.py
--rw-r--r--   0        0        0     2311 2023-04-04 08:06:50.978933 edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_version_request.py
--rw-r--r--   0        0        0     2659 2023-04-04 08:06:50.414962 edgeimpulse_api-1.22.0/edgeimpulse_api/models/raw_sample_data.py
--rw-r--r--   0        0        0     3435 2023-04-04 08:06:52.622841 edgeimpulse_api-1.22.0/edgeimpulse_api/models/raw_sample_payload.py
--rw-r--r--   0        0        0     2532 2023-04-04 08:06:52.683557 edgeimpulse_api-1.22.0/edgeimpulse_api/models/rebalance_dataset_response.py
--rw-r--r--   0        0        0     1979 2023-04-04 08:06:51.209071 edgeimpulse_api-1.22.0/edgeimpulse_api/models/remove_collaborator_request.py
--rw-r--r--   0        0        0     1800 2023-04-04 08:06:51.592754 edgeimpulse_api-1.22.0/edgeimpulse_api/models/remove_member_request.py
--rw-r--r--   0        0        0     1862 2023-04-04 08:06:51.083075 edgeimpulse_api-1.22.0/edgeimpulse_api/models/rename_device_request.py
--rw-r--r--   0        0        0     2076 2023-04-04 08:06:50.927794 edgeimpulse_api-1.22.0/edgeimpulse_api/models/rename_portal_file_request.py
--rw-r--r--   0        0        0     1862 2023-04-04 08:06:52.615127 edgeimpulse_api-1.22.0/edgeimpulse_api/models/rename_sample_request.py
--rw-r--r--   0        0        0     1868 2023-04-04 08:06:50.266863 edgeimpulse_api-1.22.0/edgeimpulse_api/models/request_reset_password_request.py
--rw-r--r--   0        0        0     2026 2023-04-04 08:06:52.633071 edgeimpulse_api-1.22.0/edgeimpulse_api/models/reset_password_request.py
--rw-r--r--   0        0        0     1980 2023-04-04 08:06:51.318277 edgeimpulse_api-1.22.0/edgeimpulse_api/models/restore_project_from_public_request.py
--rw-r--r--   0        0        0     2260 2023-04-04 08:06:52.480798 edgeimpulse_api-1.22.0/edgeimpulse_api/models/restore_project_request.py
--rw-r--r--   0        0        0     2664 2023-04-04 08:06:52.579079 edgeimpulse_api-1.22.0/edgeimpulse_api/models/run_organization_pipeline_response.py
--rw-r--r--   0        0        0     2347 2023-04-04 08:06:50.221569 edgeimpulse_api-1.22.0/edgeimpulse_api/models/run_organization_pipeline_response_all_of.py
--rw-r--r--   0        0        0     9632 2023-04-04 08:06:51.679458 edgeimpulse_api-1.22.0/edgeimpulse_api/models/sample.py
--rw-r--r--   0        0        0     2438 2023-04-04 08:06:50.458129 edgeimpulse_api-1.22.0/edgeimpulse_api/models/sample_bounding_boxes_request.py
--rw-r--r--   0        0        0     1995 2023-04-04 08:06:50.328395 edgeimpulse_api-1.22.0/edgeimpulse_api/models/sample_metadata.py
--rw-r--r--   0        0        0     2751 2023-04-04 08:06:50.360456 edgeimpulse_api-1.22.0/edgeimpulse_api/models/save_pretrained_model_request.py
--rw-r--r--   0        0        0     3322 2023-04-04 08:06:51.154452 edgeimpulse_api-1.22.0/edgeimpulse_api/models/score_trial_response.py
--rw-r--r--   0        0        0     2998 2023-04-04 08:06:52.706394 edgeimpulse_api-1.22.0/edgeimpulse_api/models/score_trial_response_all_of.py
--rw-r--r--   0        0        0     2235 2023-04-04 08:06:51.064337 edgeimpulse_api-1.22.0/edgeimpulse_api/models/score_trial_response_all_of_latency.py
--rw-r--r--   0        0        0     1909 2023-04-04 08:06:52.341167 edgeimpulse_api-1.22.0/edgeimpulse_api/models/score_trial_response_all_of_ram.py
--rw-r--r--   0        0        0     2400 2023-04-04 08:06:50.692544 edgeimpulse_api-1.22.0/edgeimpulse_api/models/segment_sample_request.py
--rw-r--r--   0        0        0     2050 2023-04-04 08:06:52.651306 edgeimpulse_api-1.22.0/edgeimpulse_api/models/segment_sample_request_segments_inner.py
--rw-r--r--   0        0        0     3359 2023-04-04 08:06:51.501521 edgeimpulse_api-1.22.0/edgeimpulse_api/models/send_user_feedback_request.py
--rw-r--r--   0        0        0     1976 2023-04-04 08:06:50.346459 edgeimpulse_api-1.22.0/edgeimpulse_api/models/sensor.py
--rw-r--r--   0        0        0     2137 2023-04-04 08:06:52.246481 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_anomaly_parameter_request.py
--rw-r--r--   0        0        0     7420 2023-04-04 08:06:50.488984 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_keras_parameter_request.py
--rw-r--r--   0        0        0     1888 2023-04-04 08:06:52.617272 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_member_datasets_request.py
--rw-r--r--   0        0        0     2044 2023-04-04 08:06:51.873240 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_member_role_request.py
--rw-r--r--   0        0        0     2214 2023-04-04 08:06:52.212301 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_optimize_space_request.py
--rw-r--r--   0        0        0     2249 2023-04-04 08:06:52.261087 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_optimize_space_request_all_of.py
--rw-r--r--   0        0        0     1918 2023-04-04 08:06:52.702455 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_organization_data_dataset_request.py
--rw-r--r--   0        0        0     1969 2023-04-04 08:06:50.950395 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_project_compute_time_request.py
--rw-r--r--   0        0        0     2006 2023-04-04 08:06:51.360610 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_project_dsp_file_size_request.py
--rw-r--r--   0        0        0     1914 2023-04-04 08:06:50.550986 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_sample_metadata_request.py
--rw-r--r--   0        0        0     1910 2023-04-04 08:06:51.294503 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_syntiant_posterior_request.py
--rw-r--r--   0        0        0     2135 2023-04-04 08:06:51.055173 edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_user_password_request.py
--rw-r--r--   0        0        0     2531 2023-04-04 08:06:50.588610 edgeimpulse_api-1.22.0/edgeimpulse_api/models/socket_token_response.py
--rw-r--r--   0        0        0     2234 2023-04-04 08:06:51.859947 edgeimpulse_api-1.22.0/edgeimpulse_api/models/socket_token_response_all_of.py
--rw-r--r--   0        0        0     2054 2023-04-04 08:06:49.996964 edgeimpulse_api-1.22.0/edgeimpulse_api/models/socket_token_response_all_of_token.py
--rw-r--r--   0        0        0     1966 2023-04-04 08:06:50.664749 edgeimpulse_api-1.22.0/edgeimpulse_api/models/split_sample_in_frames_request.py
--rw-r--r--   0        0        0     2105 2023-04-04 08:06:50.456452 edgeimpulse_api-1.22.0/edgeimpulse_api/models/staff_info.py
--rw-r--r--   0        0        0     2221 2023-04-04 08:06:51.460871 edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_job_response.py
--rw-r--r--   0        0        0     1904 2023-04-04 08:06:50.080108 edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_job_response_all_of.py
--rw-r--r--   0        0        0     2878 2023-04-04 08:06:51.178489 edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_performance_calibration_request.py
--rw-r--r--   0        0        0     2833 2023-04-04 08:06:51.710524 edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_sampling_request.py
--rw-r--r--   0        0        0     2184 2023-04-04 08:06:51.656513 edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_sampling_response.py
--rw-r--r--   0        0        0     1887 2023-04-04 08:06:51.343487 edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_sampling_response_all_of.py
--rw-r--r--   0        0        0     2487 2023-04-04 08:06:51.336642 edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_training_request_anomaly.py
--rw-r--r--   0        0        0     1962 2023-04-04 08:06:50.236661 edgeimpulse_api-1.22.0/edgeimpulse_api/models/store_segment_length_request.py
--rw-r--r--   0        0        0     2639 2023-04-04 08:06:52.235433 edgeimpulse_api-1.22.0/edgeimpulse_api/models/structured_classify_result.py
--rw-r--r--   0        0        0     2428 2023-04-04 08:06:49.968583 edgeimpulse_api-1.22.0/edgeimpulse_api/models/test_pretrained_model_request.py
--rw-r--r--   0        0        0     3069 2023-04-04 08:06:52.322235 edgeimpulse_api-1.22.0/edgeimpulse_api/models/test_pretrained_model_response.py
--rw-r--r--   0        0        0     2779 2023-04-04 08:06:51.578316 edgeimpulse_api-1.22.0/edgeimpulse_api/models/test_pretrained_model_response_all_of.py
--rw-r--r--   0        0        0     3246 2023-04-04 08:06:50.567669 edgeimpulse_api-1.22.0/edgeimpulse_api/models/theme.py
--rw-r--r--   0        0        0     2234 2023-04-04 08:06:51.233200 edgeimpulse_api-1.22.0/edgeimpulse_api/models/theme_colors.py
--rw-r--r--   0        0        0     2759 2023-04-04 08:06:50.960203 edgeimpulse_api-1.22.0/edgeimpulse_api/models/theme_favicon.py
--rw-r--r--   0        0        0     2581 2023-04-04 08:06:51.080208 edgeimpulse_api-1.22.0/edgeimpulse_api/models/theme_logos.py
--rw-r--r--   0        0        0     2240 2023-04-04 08:06:50.900927 edgeimpulse_api-1.22.0/edgeimpulse_api/models/third_party_auth.py
--rw-r--r--   0        0        0     2026 2023-04-04 08:06:50.910554 edgeimpulse_api-1.22.0/edgeimpulse_api/models/track_objects_request.py
--rw-r--r--   0        0        0     2731 2023-04-04 08:06:51.469676 edgeimpulse_api-1.22.0/edgeimpulse_api/models/track_objects_response.py
--rw-r--r--   0        0        0     2431 2023-04-04 08:06:50.813052 edgeimpulse_api-1.22.0/edgeimpulse_api/models/track_objects_response_all_of.py
--rw-r--r--   0        0        0     4605 2023-04-04 08:06:50.742830 edgeimpulse_api-1.22.0/edgeimpulse_api/models/transfer_learning_model.py
--rw-r--r--   0        0        0     2007 2023-04-04 08:06:50.425400 edgeimpulse_api-1.22.0/edgeimpulse_api/models/transfer_ownership_organization_request.py
--rw-r--r--   0        0        0     2580 2023-04-04 08:06:51.969485 edgeimpulse_api-1.22.0/edgeimpulse_api/models/transformation_block_additional_mount_point.py
--rw-r--r--   0        0        0      588 2023-04-04 08:06:52.015816 edgeimpulse_api-1.22.0/edgeimpulse_api/models/transformation_job_status_enum.py
--rw-r--r--   0        0        0     2573 2023-04-04 08:06:51.537335 edgeimpulse_api-1.22.0/edgeimpulse_api/models/tuner_create_trial_impulse.py
--rw-r--r--   0        0        0     2565 2023-04-04 08:06:50.083026 edgeimpulse_api-1.22.0/edgeimpulse_api/models/tuner_space_impulse.py
--rw-r--r--   0        0        0     3656 2023-04-04 08:06:52.517486 edgeimpulse_api-1.22.0/edgeimpulse_api/models/tuner_trial.py
--rw-r--r--   0        0        0     2299 2023-04-04 08:06:50.962266 edgeimpulse_api-1.22.0/edgeimpulse_api/models/tuner_trial_blocks_inner.py
--rw-r--r--   0        0        0     2023 2023-04-04 08:06:50.755902 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_job_request.py
--rw-r--r--   0        0        0     2276 2023-04-04 08:06:50.851508 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_add_collaborator_request.py
--rw-r--r--   0        0        0     2812 2023-04-04 08:06:51.539672 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_bucket_request.py
--rw-r--r--   0        0        0     2573 2023-04-04 08:06:52.389533 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_create_empty_project_request.py
--rw-r--r--   0        0        0     2423 2023-04-04 08:06:49.951613 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_create_project_request.py
--rw-r--r--   0        0        0     2153 2023-04-04 08:06:52.273349 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_data_item_request.py
--rw-r--r--   0        0        0     2047 2023-04-04 08:06:52.612474 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_dataset_request.py
--rw-r--r--   0        0        0     2876 2023-04-04 08:06:52.637414 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_dsp_block_request.py
--rw-r--r--   0        0        0     2719 2023-04-04 08:06:50.921788 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_portal_response.py
--rw-r--r--   0        0        0     2440 2023-04-04 08:06:51.576532 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_portal_response_all_of.py
--rw-r--r--   0        0        0     2577 2023-04-04 08:06:51.708760 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_request.py
--rw-r--r--   0        0        0     3905 2023-04-04 08:06:52.074390 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_transfer_learning_block_request.py
--rw-r--r--   0        0        0     4729 2023-04-04 08:06:52.278757 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_transformation_block_request.py
--rw-r--r--   0        0        0     7721 2023-04-04 08:06:51.458190 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_project_request.py
--rw-r--r--   0        0        0     1872 2023-04-04 08:06:51.043354 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_project_tags_request.py
--rw-r--r--   0        0        0     2254 2023-04-04 08:06:50.613924 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_theme_colors_request.py
--rw-r--r--   0        0        0     2724 2023-04-04 08:06:50.607070 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_theme_logos_request.py
--rw-r--r--   0        0        0     2200 2023-04-04 08:06:51.658792 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_third_party_auth_request.py
--rw-r--r--   0        0        0     2272 2023-04-04 08:06:50.496466 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_user_request.py
--rw-r--r--   0        0        0     1881 2023-04-04 08:06:51.119495 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_version_request.py
--rw-r--r--   0        0        0     2120 2023-04-04 08:06:52.558301 edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_whitelabel_deployment_targets_request.py
--rw-r--r--   0        0        0     2163 2023-04-04 08:06:51.425600 edgeimpulse_api-1.22.0/edgeimpulse_api/models/upload_asset_response.py
--rw-r--r--   0        0        0     1877 2023-04-04 08:06:50.894715 edgeimpulse_api-1.22.0/edgeimpulse_api/models/upload_asset_response_all_of.py
--rw-r--r--   0        0        0     2194 2023-04-04 08:06:50.055847 edgeimpulse_api-1.22.0/edgeimpulse_api/models/upload_readme_image_response.py
--rw-r--r--   0        0        0     2180 2023-04-04 08:06:51.507671 edgeimpulse_api-1.22.0/edgeimpulse_api/models/upload_user_photo_response.py
--rw-r--r--   0        0        0     1867 2023-04-04 08:06:51.549337 edgeimpulse_api-1.22.0/edgeimpulse_api/models/upload_user_photo_response_all_of.py
--rw-r--r--   0        0        0     3051 2023-04-04 08:06:50.239856 edgeimpulse_api-1.22.0/edgeimpulse_api/models/user.py
--rw-r--r--   0        0        0     1986 2023-04-04 08:06:50.786506 edgeimpulse_api-1.22.0/edgeimpulse_api/models/user_by_third_party_activation_request.py
--rw-r--r--   0        0        0     2187 2023-04-04 08:06:52.570895 edgeimpulse_api-1.22.0/edgeimpulse_api/models/user_experiment.py
--rw-r--r--   0        0        0     2704 2023-04-04 08:06:51.117110 edgeimpulse_api-1.22.0/edgeimpulse_api/models/user_organization.py
--rw-r--r--   0        0        0     1839 2023-04-04 08:06:51.566637 edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_dsp_block_url_request.py
--rw-r--r--   0        0        0     2599 2023-04-04 08:06:52.311062 edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_dsp_block_url_response.py
--rw-r--r--   0        0        0     2302 2023-04-04 08:06:51.693241 edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_dsp_block_url_response_all_of.py
--rw-r--r--   0        0        0     2402 2023-04-04 08:06:52.192737 edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_dsp_block_url_response_all_of_block.py
--rw-r--r--   0        0        0     2703 2023-04-04 08:06:50.970080 edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_organization_bucket_request.py
--rw-r--r--   0        0        0     2892 2023-04-04 08:06:51.670040 edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_organization_bucket_response.py
--rw-r--r--   0        0        0     2592 2023-04-04 08:06:52.574463 edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_organization_bucket_response_all_of.py
--rw-r--r--   0        0        0     2182 2023-04-04 08:06:49.847494 edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_organization_bucket_response_all_of_files.py
--rw-r--r--   0        0        0     1932 2023-04-04 08:06:51.939926 edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_reset_password_request.py
--rw-r--r--   0        0        0     3213 2023-04-04 08:06:51.515497 edgeimpulse_api-1.22.0/edgeimpulse_api/models/whitelabel.py
--rw-r--r--   0        0        0     2529 2023-04-04 08:06:49.917938 edgeimpulse_api-1.22.0/edgeimpulse_api/models/whitelabel_admin_create_organization_request.py
--rw-r--r--   0        0        0     2880 2023-04-04 08:06:52.546445 edgeimpulse_api-1.22.0/edgeimpulse_api/models/window_settings_response.py
--rw-r--r--   0        0        0     2580 2023-04-04 08:06:50.025286 edgeimpulse_api-1.22.0/edgeimpulse_api/models/window_settings_response_all_of.py
--rw-r--r--   0        0        0     2843 2023-04-04 08:06:50.203779 edgeimpulse_api-1.22.0/edgeimpulse_api/models/window_settings_response_all_of_window_settings.py
--rw-r--r--   0        0        0    12674 2023-04-04 08:06:33.866534 edgeimpulse_api-1.22.0/edgeimpulse_api/rest.py
--rw-r--r--   0        0        0      975 2023-04-04 08:07:37.104483 edgeimpulse_api-1.22.0/pyproject.toml
--rw-r--r--   0        0        0     1413 1970-01-01 00:00:00.000000 edgeimpulse_api-1.22.0/PKG-INFO
+-rw-r--r--   0        0        0      377 2023-04-06 11:23:10.745510 edgeimpulse_api-1.22.1/README.md
+-rw-r--r--   0        0        0    65087 2023-04-07 09:56:15.026481 edgeimpulse_api-1.22.1/edgeimpulse_api/__init__.py
+-rw-r--r--   0        0        0     2752 2023-04-07 08:12:18.020484 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__init__.py
+-rw-r--r--   0        0        0     3281 2023-04-07 09:56:59.150122 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0        0        0   107561 2023-04-07 09:56:59.163326 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/admin_api.cpython-38.pyc
+-rw-r--r--   0        0        0   192963 2023-04-07 09:57:01.839418 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/allows_read_only_api.cpython-38.pyc
+-rw-r--r--   0        0        0     8702 2023-04-07 09:57:01.954214 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/auth_api.cpython-38.pyc
+-rw-r--r--   0        0        0     5257 2023-04-07 09:57:01.961092 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/cdn_api.cpython-38.pyc
+-rw-r--r--   0        0        0    20127 2023-04-07 09:57:01.967637 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/classify_api.cpython-38.pyc
+-rw-r--r--   0        0        0     6209 2023-04-07 09:57:01.981556 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/content_disposition_inline_api.cpython-38.pyc
+-rw-r--r--   0        0        0    49343 2023-04-07 09:57:02.049425 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/deployment_api.cpython-38.pyc
+-rw-r--r--   0        0        0    26830 2023-04-07 09:57:02.081324 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/devices_api.cpython-38.pyc
+-rw-r--r--   0        0        0    86893 2023-04-07 09:57:01.994962 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/dsp_api.cpython-38.pyc
+-rw-r--r--   0        0        0     5434 2023-04-07 09:57:02.099050 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/export_api.cpython-38.pyc
+-rw-r--r--   0        0        0     8845 2023-04-07 09:57:02.104287 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/health_api.cpython-38.pyc
+-rw-r--r--   0        0        0    33606 2023-04-07 09:57:02.116513 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/impulse_api.cpython-38.pyc
+-rw-r--r--   0        0        0   152546 2023-04-07 09:57:02.152217 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/jobs_api.cpython-38.pyc
+-rw-r--r--   0        0        0    90094 2023-04-07 09:57:02.250350 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/learn_api.cpython-38.pyc
+-rw-r--r--   0        0        0     5356 2023-04-07 09:57:02.310439 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/login_api.cpython-38.pyc
+-rw-r--r--   0        0        0     9169 2023-04-07 09:57:02.316079 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/metrics_api.cpython-38.pyc
+-rw-r--r--   0        0        0    45312 2023-04-07 09:57:02.327495 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/optimization_api.cpython-38.pyc
+-rw-r--r--   0        0        0   199032 2023-04-07 09:57:02.427596 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/organization_allow_developer_profile_api.cpython-38.pyc
+-rw-r--r--   0        0        0    42571 2023-04-07 09:57:02.567993 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/organization_allow_guest_access_api.cpython-38.pyc
+-rw-r--r--   0        0        0    93099 2023-04-07 09:57:02.609017 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/organization_blocks_api.cpython-38.pyc
+-rw-r--r--   0        0        0    61865 2023-04-07 09:57:02.676479 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/organization_create_project_api.cpython-38.pyc
+-rw-r--r--   0        0        0   156620 2023-04-07 09:57:02.744753 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/organization_data_api.cpython-38.pyc
+-rw-r--r--   0        0        0    39259 2023-04-07 09:57:02.860387 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/organization_jobs_api.cpython-38.pyc
+-rw-r--r--   0        0        0    32132 2023-04-07 09:57:02.890660 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/organization_pipelines_api.cpython-38.pyc
+-rw-r--r--   0        0        0    31172 2023-04-07 09:57:02.913557 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/organization_portals_api.cpython-38.pyc
+-rw-r--r--   0        0        0   117899 2023-04-07 09:57:02.944332 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/organization_requires_admin_api.cpython-38.pyc
+-rw-r--r--   0        0        0    59324 2023-04-07 09:57:03.016310 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/organization_requires_whitelabel_admin_api.cpython-38.pyc
+-rw-r--r--   0        0        0   139642 2023-04-07 09:57:03.119239 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/organizations_api.cpython-38.pyc
+-rw-r--r--   0        0        0    37722 2023-04-07 09:57:03.203238 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/performance_calibration_api.cpython-38.pyc
+-rw-r--r--   0        0        0   146351 2023-04-07 09:57:03.236868 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/projects_api.cpython-38.pyc
+-rw-r--r--   0        0        0   207459 2023-04-07 09:57:03.334478 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/raw_data_api.cpython-38.pyc
+-rw-r--r--   0        0        0   167494 2023-04-07 09:57:03.506136 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/requires_sudo_api.cpython-38.pyc
+-rw-r--r--   0        0        0     6411 2023-04-07 09:57:03.609645 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/requires_third_party_auth_api_key_api.cpython-38.pyc
+-rw-r--r--   0        0        0    10264 2023-04-07 09:57:03.618253 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/supports_range_api.cpython-38.pyc
+-rw-r--r--   0        0        0    24531 2023-04-07 09:57:03.651192 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/themes_api.cpython-38.pyc
+-rw-r--r--   0        0        0    30222 2023-04-07 09:57:03.670437 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/third_party_auth_api.cpython-38.pyc
+-rw-r--r--   0        0        0    31335 2023-04-07 09:57:03.692275 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/upload_portal_api.cpython-38.pyc
+-rw-r--r--   0        0        0   131673 2023-04-07 09:57:03.807690 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/user_api.cpython-38.pyc
+-rw-r--r--   0        0        0    28940 2023-04-07 09:57:03.893023 edgeimpulse_api-1.22.1/edgeimpulse_api/api/__pycache__/whitelabels_api.cpython-38.pyc
+-rw-r--r--   0        0        0   161969 2023-04-07 08:12:16.747314 edgeimpulse_api-1.22.1/edgeimpulse_api/api/admin_api.py
+-rw-r--r--   0        0        0   290132 2023-04-07 09:50:46.259678 edgeimpulse_api-1.22.1/edgeimpulse_api/api/allows_read_only_api.py
+-rw-r--r--   0        0        0    11231 2023-04-07 08:12:16.799964 edgeimpulse_api-1.22.1/edgeimpulse_api/api/auth_api.py
+-rw-r--r--   0        0        0     6235 2023-04-07 08:12:16.815092 edgeimpulse_api-1.22.1/edgeimpulse_api/api/cdn_api.py
+-rw-r--r--   0        0        0    27785 2023-04-07 09:50:46.260403 edgeimpulse_api-1.22.1/edgeimpulse_api/api/classify_api.py
+-rw-r--r--   0        0        0     7426 2023-04-07 08:12:16.863802 edgeimpulse_api-1.22.1/edgeimpulse_api/api/content_disposition_inline_api.py
+-rw-r--r--   0        0        0    72480 2023-04-07 08:12:16.938795 edgeimpulse_api-1.22.1/edgeimpulse_api/api/deployment_api.py
+-rw-r--r--   0        0        0    38974 2023-04-07 08:12:16.981257 edgeimpulse_api-1.22.1/edgeimpulse_api/api/devices_api.py
+-rw-r--r--   0        0        0   130256 2023-04-07 09:50:46.261452 edgeimpulse_api-1.22.1/edgeimpulse_api/api/dsp_api.py
+-rw-r--r--   0        0        0     6435 2023-04-07 08:12:17.014643 edgeimpulse_api-1.22.1/edgeimpulse_api/api/export_api.py
+-rw-r--r--   0        0        0    11921 2023-04-07 08:12:17.057090 edgeimpulse_api-1.22.1/edgeimpulse_api/api/health_api.py
+-rw-r--r--   0        0        0    49621 2023-04-07 08:12:17.072772 edgeimpulse_api-1.22.1/edgeimpulse_api/api/impulse_api.py
+-rw-r--r--   0        0        0   231500 2023-04-07 08:12:17.122320 edgeimpulse_api-1.22.1/edgeimpulse_api/api/jobs_api.py
+-rw-r--r--   0        0        0   134972 2023-04-07 08:12:17.163899 edgeimpulse_api-1.22.1/edgeimpulse_api/api/learn_api.py
+-rw-r--r--   0        0        0     6605 2023-04-07 08:12:17.191346 edgeimpulse_api-1.22.1/edgeimpulse_api/api/login_api.py
+-rw-r--r--   0        0        0    12006 2023-04-07 08:12:17.203407 edgeimpulse_api-1.22.1/edgeimpulse_api/api/metrics_api.py
+-rw-r--r--   0        0        0    67457 2023-04-07 08:12:17.216378 edgeimpulse_api-1.22.1/edgeimpulse_api/api/optimization_api.py
+-rw-r--r--   0        0        0   300920 2023-04-07 08:12:17.234336 edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_allow_developer_profile_api.py
+-rw-r--r--   0        0        0    63058 2023-04-07 08:12:17.252056 edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_allow_guest_access_api.py
+-rw-r--r--   0        0        0   141131 2023-04-07 08:12:17.265583 edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_blocks_api.py
+-rw-r--r--   0        0        0    91908 2023-04-07 08:12:17.283734 edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_create_project_api.py
+-rw-r--r--   0        0        0   240681 2023-04-07 08:12:17.301814 edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_data_api.py
+-rw-r--r--   0        0        0    58218 2023-04-07 08:12:17.321646 edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_jobs_api.py
+-rw-r--r--   0        0        0    47178 2023-04-07 08:12:17.337723 edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_pipelines_api.py
+-rw-r--r--   0        0        0    45490 2023-04-07 08:12:17.351351 edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_portals_api.py
+-rw-r--r--   0        0        0   178330 2023-04-07 08:12:17.372297 edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_requires_admin_api.py
+-rw-r--r--   0        0        0    88200 2023-04-07 08:12:17.392681 edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_requires_whitelabel_admin_api.py
+-rw-r--r--   0        0        0   212216 2023-04-07 08:12:17.412089 edgeimpulse_api-1.22.1/edgeimpulse_api/api/organizations_api.py
+-rw-r--r--   0        0        0    54671 2023-04-07 08:12:17.431590 edgeimpulse_api-1.22.1/edgeimpulse_api/api/performance_calibration_api.py
+-rw-r--r--   0        0        0   220399 2023-04-07 08:12:17.468737 edgeimpulse_api-1.22.1/edgeimpulse_api/api/projects_api.py
+-rw-r--r--   0        0        0   324953 2023-04-07 08:12:17.521822 edgeimpulse_api-1.22.1/edgeimpulse_api/api/raw_data_api.py
+-rw-r--r--   0        0        0   252278 2023-04-07 08:12:17.556097 edgeimpulse_api-1.22.1/edgeimpulse_api/api/requires_sudo_api.py
+-rw-r--r--   0        0        0     7730 2023-04-07 08:12:17.577183 edgeimpulse_api-1.22.1/edgeimpulse_api/api/requires_third_party_auth_api_key_api.py
+-rw-r--r--   0        0        0    13690 2023-04-07 08:12:17.588363 edgeimpulse_api-1.22.1/edgeimpulse_api/api/supports_range_api.py
+-rw-r--r--   0        0        0    35671 2023-04-07 08:12:17.618115 edgeimpulse_api-1.22.1/edgeimpulse_api/api/themes_api.py
+-rw-r--r--   0        0        0    43486 2023-04-07 08:12:17.658471 edgeimpulse_api-1.22.1/edgeimpulse_api/api/third_party_auth_api.py
+-rw-r--r--   0        0        0    45393 2023-04-07 08:12:17.690235 edgeimpulse_api-1.22.1/edgeimpulse_api/api/upload_portal_api.py
+-rw-r--r--   0        0        0   197621 2023-04-07 08:12:17.735655 edgeimpulse_api-1.22.1/edgeimpulse_api/api/user_api.py
+-rw-r--r--   0        0        0    42135 2023-04-07 08:12:17.813305 edgeimpulse_api-1.22.1/edgeimpulse_api/api/whitelabels_api.py
+-rw-r--r--   0        0        0    29331 2023-04-07 08:12:18.307478 edgeimpulse_api-1.22.1/edgeimpulse_api/api_client.py
+-rw-r--r--   0        0        0    15659 2023-04-07 08:12:17.943301 edgeimpulse_api-1.22.1/edgeimpulse_api/configuration.py
+-rw-r--r--   0        0        0     5113 2023-04-07 08:12:18.160338 edgeimpulse_api-1.22.1/edgeimpulse_api/exceptions.py
+-rw-r--r--   0        0        0    61882 2023-04-07 09:50:46.262350 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__init__.py
+-rw-r--r--   0        0        0    72915 2023-04-07 09:56:59.293916 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0        0        0     3459 2023-04-07 09:56:59.298643 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/activate_user_by_third_party_activation_code_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2499 2023-04-07 09:56:59.317986 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/activate_user_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3162 2023-04-07 09:56:59.320812 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_api_key_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2563 2023-04-07 09:56:59.326402 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_collaborator_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2731 2023-04-07 09:56:59.328840 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_hmac_key_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3034 2023-04-07 09:56:59.334053 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_member_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3101 2023-04-07 09:56:59.338579 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_api_key_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3129 2023-04-07 09:56:59.342396 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_bucket_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2930 2023-04-07 09:56:59.346728 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_deploy_block_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3167 2023-04-07 09:56:59.349747 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_dsp_block_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2897 2023-04-07 09:56:59.357925 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_dsp_block_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2622 2023-04-07 09:56:59.360833 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_secret_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2893 2023-04-07 09:56:59.363834 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_secret_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2635 2023-04-07 09:56:59.366660 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_secret_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     4104 2023-04-07 09:56:59.369665 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_transfer_learning_block_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3041 2023-04-07 09:56:59.412089 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_transfer_learning_block_response.cpython-38.pyc
+-rw-r--r--   0        0        0     4645 2023-04-07 09:56:59.415019 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_transformation_block_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3018 2023-04-07 09:56:59.423017 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_transformation_block_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2724 2023-04-07 09:56:59.425776 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/add_organization_transformation_block_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2654 2023-04-07 09:56:59.428027 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_add_or_update_sso_domain_id_ps_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2650 2023-04-07 09:56:59.430424 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_add_project_user_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3932 2023-04-07 09:56:59.432987 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_api_organization.cpython-38.pyc
+-rw-r--r--   0        0        0     2956 2023-04-07 09:56:59.459037 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_api_organization_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3624 2023-04-07 09:56:59.462806 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_api_project.cpython-38.pyc
+-rw-r--r--   0        0        0     5440 2023-04-07 09:56:59.467723 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_api_user.cpython-38.pyc
+-rw-r--r--   0        0        0     4783 2023-04-07 09:56:59.482010 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_api_user_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2871 2023-04-07 09:56:59.487352 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_create_organization_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2833 2023-04-07 09:56:59.490242 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_metrics_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2559 2023-04-07 09:56:59.492973 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_metrics_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3492 2023-04-07 09:56:59.496951 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_organizations_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3264 2023-04-07 09:56:59.505308 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_organizations_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3411 2023-04-07 09:56:59.499218 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_organizations_response_all_of_organizations.cpython-38.pyc
+-rw-r--r--   0        0        0     2886 2023-04-07 09:56:59.509008 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_sso_domain_id_ps_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2632 2023-04-07 09:56:59.512129 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_sso_domain_id_ps_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3386 2023-04-07 09:56:59.514536 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_sso_settings_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3143 2023-04-07 09:56:59.522490 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_sso_settings_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2801 2023-04-07 09:56:59.516017 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_sso_settings_response_all_of_sso_whitelist.cpython-38.pyc
+-rw-r--r--   0        0        0     2837 2023-04-07 09:56:59.525109 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_user_ids_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2563 2023-04-07 09:56:59.528049 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_user_ids_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2878 2023-04-07 09:56:59.531464 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_user_metrics_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2604 2023-04-07 09:56:59.533996 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_user_metrics_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2904 2023-04-07 09:56:59.536435 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_user_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2610 2023-04-07 09:56:59.539397 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_user_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3306 2023-04-07 09:56:59.553113 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_users_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3042 2023-04-07 09:56:59.560360 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_users_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3569 2023-04-07 09:56:59.555665 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_get_users_response_all_of_users.cpython-38.pyc
+-rw-r--r--   0        0        0     2947 2023-04-07 09:56:59.562956 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_list_projects.cpython-38.pyc
+-rw-r--r--   0        0        0     3334 2023-04-07 09:56:59.566267 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_list_projects_response.cpython-38.pyc
+-rw-r--r--   0        0        0     5182 2023-04-07 09:56:59.570957 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_organization_info_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2642 2023-04-07 09:56:59.595399 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_organization_info_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3210 2023-04-07 09:56:59.597990 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_update_organization_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2730 2023-04-07 09:56:59.601311 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/admin_update_user_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3022 2023-04-07 09:56:59.605229 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/akida_edge_learning_config.cpython-38.pyc
+-rw-r--r--   0        0        0     3928 2023-04-07 09:56:59.608707 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/anomaly_model_metadata.cpython-38.pyc
+-rw-r--r--   0        0        0     2803 2023-04-07 09:56:59.610739 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/anomaly_model_metadata_clusters_inner.cpython-38.pyc
+-rw-r--r--   0        0        0     4296 2023-04-07 09:56:59.616576 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/anomaly_model_metadata_response.cpython-38.pyc
+-rw-r--r--   0        0        0     4083 2023-04-07 09:56:59.620217 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/anomaly_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3920 2023-04-07 09:56:59.629501 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/anomaly_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2606 2023-04-07 09:56:59.622155 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/anomaly_response_all_of_axes.cpython-38.pyc
+-rw-r--r--   0        0        0     3533 2023-04-07 09:56:59.634132 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/anomaly_trained_features_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3298 2023-04-07 09:56:59.639528 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/anomaly_trained_features_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3086 2023-04-07 09:56:59.636101 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/anomaly_trained_features_response_all_of_data.cpython-38.pyc
+-rw-r--r--   0        0        0      814 2023-04-07 09:56:59.642714 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/augmentation_policy_image_enum.cpython-38.pyc
+-rw-r--r--   0        0        0     4035 2023-04-07 09:56:59.648995 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/augmentation_policy_spectrogram.cpython-38.pyc
+-rw-r--r--   0        0        0     2510 2023-04-07 09:56:59.653746 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/autotune_dsp_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2541 2023-04-07 09:56:59.656353 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/bounding_box.cpython-38.pyc
+-rw-r--r--   0        0        0     2672 2023-04-07 09:56:59.659291 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/bounding_box_with_score.cpython-38.pyc
+-rw-r--r--   0        0        0     2821 2023-04-07 09:56:59.662047 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/build_on_device_model_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3060 2023-04-07 09:56:59.671058 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/build_organization_on_device_model_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2584 2023-04-07 09:56:59.673901 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/change_password_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3746 2023-04-07 09:56:59.676888 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/classify_job_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3482 2023-04-07 09:56:59.726395 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/classify_job_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3770 2023-04-07 09:56:59.679533 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/classify_job_response_all_of_accuracy.cpython-38.pyc
+-rw-r--r--   0        0        0     2745 2023-04-07 09:56:59.682313 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/classify_job_response_all_of_accuracy_total_summary.cpython-38.pyc
+-rw-r--r--   0        0        0     3554 2023-04-07 09:56:59.729449 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/classify_job_response_page.cpython-38.pyc
+-rw-r--r--   0        0        0     3290 2023-04-07 09:56:59.732226 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/classify_job_response_page_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3977 2023-04-07 09:56:59.734725 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/classify_sample_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3768 2023-04-07 09:56:59.745831 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/classify_sample_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     4678 2023-04-07 09:56:59.694366 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/classify_sample_response_classification.cpython-38.pyc
+-rw-r--r--   0        0        0     3224 2023-04-07 09:56:59.696511 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/classify_sample_response_classification_details.cpython-38.pyc
+-rw-r--r--   0        0        0     3397 2023-04-07 09:56:59.748310 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/convert_user_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2777 2023-04-07 09:56:59.752007 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/count_samples_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2483 2023-04-07 09:56:59.755684 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/count_samples_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2870 2023-04-07 09:56:59.758046 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_block_version_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2612 2023-04-07 09:56:59.760749 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_block_version_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2978 2023-04-07 09:56:59.763274 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_developer_profile_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2790 2023-04-07 09:56:59.767181 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_developer_profile_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2882 2023-04-07 09:56:59.770721 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_device_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3045 2023-04-07 09:56:59.773908 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_evaluation_user_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2812 2023-04-07 09:56:59.778659 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_evaluation_user_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3137 2023-04-07 09:56:59.781795 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_organization_portal_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3305 2023-04-07 09:56:59.784935 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_organization_portal_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3132 2023-04-07 09:56:59.789090 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_organization_portal_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2600 2023-04-07 09:56:59.792038 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_organization_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3037 2023-04-07 09:56:59.794477 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_organization_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2804 2023-04-07 09:56:59.797230 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_organization_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2796 2023-04-07 09:56:59.801363 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_pipeline_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2784 2023-04-07 09:56:59.803825 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_project_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2941 2023-04-07 09:56:59.806344 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_project_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2708 2023-04-07 09:56:59.809051 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_project_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2830 2023-04-07 09:56:59.813794 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_signed_upload_link_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2977 2023-04-07 09:56:59.816873 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_signed_upload_link_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2803 2023-04-07 09:56:59.819737 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_signed_upload_link_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2920 2023-04-07 09:56:59.823944 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_third_party_auth_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3016 2023-04-07 09:56:59.827935 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_third_party_auth_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2768 2023-04-07 09:56:59.831244 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_third_party_auth_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3897 2023-04-07 09:56:59.835492 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_user_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2918 2023-04-07 09:56:59.839641 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_user_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2744 2023-04-07 09:56:59.842571 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_user_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3399 2023-04-07 09:56:59.846691 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_user_third_party_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3323 2023-04-07 09:56:59.849494 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_user_third_party_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3140 2023-04-07 09:56:59.852080 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_user_third_party_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     4080 2023-04-07 09:56:59.855249 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_whitelabel_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3005 2023-04-07 09:56:59.860784 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_whitelabel_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2752 2023-04-07 09:56:59.864297 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/create_whitelabel_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2597 2023-04-07 09:56:59.867673 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/crop_sample_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2781 2023-04-07 09:56:59.871300 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/crop_sample_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2539 2023-04-07 09:56:59.873936 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/crop_sample_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3829 2023-04-07 09:56:59.935832 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/data_explorer_predictions_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3611 2023-04-07 09:56:59.939260 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/data_explorer_predictions_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3417 2023-04-07 09:56:59.942293 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/data_explorer_settings.cpython-38.pyc
+-rw-r--r--   0        0        0     2594 2023-04-07 09:56:59.946282 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dataset_ratio_data.cpython-38.pyc
+-rw-r--r--   0        0        0     2689 2023-04-07 09:56:59.948255 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dataset_ratio_data_ratio.cpython-38.pyc
+-rw-r--r--   0        0        0     2532 2023-04-07 09:56:59.951202 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/delete_portal_file_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2696 2023-04-07 09:56:59.624657 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dependency_data.cpython-38.pyc
+-rw-r--r--   0        0        0     2980 2023-04-07 09:56:59.953736 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deploy_pretrained_model_input_audio.cpython-38.pyc
+-rw-r--r--   0        0        0     2897 2023-04-07 09:56:59.957805 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deploy_pretrained_model_input_image.cpython-38.pyc
+-rw-r--r--   0        0        0     2897 2023-04-07 09:56:59.960403 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deploy_pretrained_model_input_other.cpython-38.pyc
+-rw-r--r--   0        0        0     3161 2023-04-07 09:56:59.962901 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deploy_pretrained_model_input_time_series.cpython-38.pyc
+-rw-r--r--   0        0        0     3124 2023-04-07 09:56:59.965821 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deploy_pretrained_model_model_classification.cpython-38.pyc
+-rw-r--r--   0        0        0     3468 2023-04-07 09:56:59.969827 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deploy_pretrained_model_model_object_detection.cpython-38.pyc
+-rw-r--r--   0        0        0     2967 2023-04-07 09:56:59.972870 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deploy_pretrained_model_model_regression.cpython-38.pyc
+-rw-r--r--   0        0        0     4507 2023-04-07 09:56:59.975508 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deploy_pretrained_model_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3066 2023-04-07 09:56:59.977860 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deploy_pretrained_model_request_model_info.cpython-38.pyc
+-rw-r--r--   0        0        0     5383 2023-04-07 09:56:59.981309 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deploy_pretrained_model_request_model_info_input.cpython-38.pyc
+-rw-r--r--   0        0        0     5029 2023-04-07 09:56:59.985567 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deploy_pretrained_model_request_model_info_model.cpython-38.pyc
+-rw-r--r--   0        0        0     4708 2023-04-07 09:56:59.990785 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deployment_target.cpython-38.pyc
+-rw-r--r--   0        0        0     2495 2023-04-07 09:56:59.994339 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deployment_target_badge.cpython-38.pyc
+-rw-r--r--   0        0        0      959 2023-04-07 09:56:59.663681 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deployment_target_engine.cpython-38.pyc
+-rw-r--r--   0        0        0     3232 2023-04-07 09:57:00.000206 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deployment_targets_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2963 2023-04-07 09:57:00.002894 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/deployment_targets_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2531 2023-04-07 09:57:00.005139 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/development_board.cpython-38.pyc
+-rw-r--r--   0        0        0     3279 2023-04-07 09:57:00.007970 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/development_boards_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3036 2023-04-07 09:57:00.012564 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/development_boards_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2581 2023-04-07 09:57:00.016144 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/development_keys.cpython-38.pyc
+-rw-r--r--   0        0        0     2908 2023-04-07 09:57:00.019163 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/development_keys_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3748 2023-04-07 09:57:00.023016 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/device.cpython-38.pyc
+-rw-r--r--   0        0        0     2750 2023-04-07 09:57:00.030246 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/device_name_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2571 2023-04-07 09:57:00.037884 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/device_name_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2773 2023-04-07 09:57:00.024987 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/device_sensors_inner.cpython-38.pyc
+-rw-r--r--   0        0        0     2535 2023-04-07 09:57:00.042362 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/download.cpython-38.pyc
+-rw-r--r--   0        0        0     2554 2023-04-07 09:57:00.047569 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/download_portal_file_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2863 2023-04-07 09:57:00.050737 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/download_portal_file_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2625 2023-04-07 09:57:00.054521 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/download_portal_file_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3209 2023-04-07 09:57:00.058148 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_autotuner_results.cpython-38.pyc
+-rw-r--r--   0        0        0     2940 2023-04-07 09:57:00.064437 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_autotuner_results_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2601 2023-04-07 09:57:00.060385 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_autotuner_results_all_of_results.cpython-38.pyc
+-rw-r--r--   0        0        0     3046 2023-04-07 09:56:59.876353 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_block.cpython-38.pyc
+-rw-r--r--   0        0        0     2435 2023-04-07 09:56:59.880782 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_config_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3402 2023-04-07 09:56:59.885329 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_config_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3218 2023-04-07 09:56:59.912364 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_config_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3481 2023-04-07 09:57:00.068422 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_feature_importance_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3264 2023-04-07 09:57:00.076564 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_feature_importance_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2725 2023-04-07 09:57:00.072487 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_feature_importance_response_all_of_features.cpython-38.pyc
+-rw-r--r--   0        0        0     3154 2023-04-07 09:57:00.070603 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_feature_importance_response_all_of_labels.cpython-38.pyc
+-rw-r--r--   0        0        0     2830 2023-04-07 09:57:00.079171 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_feature_labels_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2576 2023-04-07 09:57:00.082787 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_feature_labels_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2761 2023-04-07 09:56:59.887468 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_group.cpython-38.pyc
+-rw-r--r--   0        0        0     3648 2023-04-07 09:56:59.889597 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_group_item.cpython-38.pyc
+-rw-r--r--   0        0        0     2798 2023-04-07 09:56:59.891374 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_group_item_select_options_inner.cpython-38.pyc
+-rw-r--r--   0        0        0     2794 2023-04-07 09:56:59.894209 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_group_item_show_if.cpython-38.pyc
+-rw-r--r--   0        0        0     4004 2023-04-07 09:56:59.900746 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_info.cpython-38.pyc
+-rw-r--r--   0        0        0     2776 2023-04-07 09:56:59.902912 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_info_features.cpython-38.pyc
+-rw-r--r--   0        0        0     2457 2023-04-07 09:56:59.906483 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_info_performance.cpython-38.pyc
+-rw-r--r--   0        0        0     4797 2023-04-07 09:56:59.917024 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_metadata.cpython-38.pyc
+-rw-r--r--   0        0        0     2657 2023-04-07 09:56:59.919178 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_metadata_included_samples_inner.cpython-38.pyc
+-rw-r--r--   0        0        0     3084 2023-04-07 09:56:59.921926 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_metadata_output_config.cpython-38.pyc
+-rw-r--r--   0        0        0     3053 2023-04-07 09:56:59.923890 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_metadata_output_config_shape.cpython-38.pyc
+-rw-r--r--   0        0        0     5119 2023-04-07 09:56:59.930181 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_metadata_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3512 2023-04-07 09:57:00.086842 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_performance_all_variants_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3297 2023-04-07 09:57:00.092548 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_performance_all_variants_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2975 2023-04-07 09:57:00.089017 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_performance_all_variants_response_all_of_performance.cpython-38.pyc
+-rw-r--r--   0        0        0     4394 2023-04-07 09:57:00.096700 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_run_graph.cpython-38.pyc
+-rw-r--r--   0        0        0     2525 2023-04-07 09:57:00.099019 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_run_graph_axis_labels.cpython-38.pyc
+-rw-r--r--   0        0        0     3195 2023-04-07 09:57:00.105234 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_run_request_with_features.cpython-38.pyc
+-rw-r--r--   0        0        0     2796 2023-04-07 09:57:00.109482 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_run_request_without_features.cpython-38.pyc
+-rw-r--r--   0        0        0     2731 2023-04-07 09:57:00.112238 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_run_request_without_features_read_only.cpython-38.pyc
+-rw-r--r--   0        0        0     3690 2023-04-07 09:57:00.115127 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_run_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3501 2023-04-07 09:57:00.122423 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_run_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2592 2023-04-07 09:57:00.117531 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_run_response_all_of_performance.cpython-38.pyc
+-rw-r--r--   0        0        0     4111 2023-04-07 09:57:00.125680 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_run_response_with_sample.cpython-38.pyc
+-rw-r--r--   0        0        0     3948 2023-04-07 09:57:00.130747 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_run_response_with_sample_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3742 2023-04-07 09:57:00.134185 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_sample_features_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3507 2023-04-07 09:57:00.142384 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_sample_features_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3231 2023-04-07 09:57:00.136217 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_sample_features_response_all_of_data.cpython-38.pyc
+-rw-r--r--   0        0        0     2849 2023-04-07 09:57:00.138089 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_sample_features_response_all_of_sample.cpython-38.pyc
+-rw-r--r--   0        0        0     3757 2023-04-07 09:57:00.146923 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_trained_features_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3522 2023-04-07 09:57:00.157474 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_trained_features_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3259 2023-04-07 09:57:00.149591 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_trained_features_response_all_of_data.cpython-38.pyc
+-rw-r--r--   0        0        0     2835 2023-04-07 09:57:00.151551 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/dsp_trained_features_response_all_of_sample.cpython-38.pyc
+-rw-r--r--   0        0        0     2520 2023-04-07 09:57:00.160103 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/edit_sample_label_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3163 2023-04-07 09:57:00.162239 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/evaluate_job_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2894 2023-04-07 09:57:00.169400 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/evaluate_job_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2673 2023-04-07 09:57:00.165351 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/evaluate_result_value.cpython-38.pyc
+-rw-r--r--   0        0        0     2975 2023-04-07 09:57:00.173331 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/export_get_url_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2828 2023-04-07 09:57:00.176939 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/export_get_url_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2889 2023-04-07 09:57:00.179702 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/export_original_data_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2626 2023-04-07 09:57:00.182400 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/export_wav_data_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2776 2023-04-07 09:57:00.185608 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/find_segment_sample_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3305 2023-04-07 09:57:00.188338 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/find_segment_sample_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3036 2023-04-07 09:57:00.193411 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/find_segment_sample_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2747 2023-04-07 09:57:00.190230 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/find_segment_sample_response_all_of_segments.cpython-38.pyc
+-rw-r--r--   0        0        0     3156 2023-04-07 09:57:00.196746 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/find_user_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2887 2023-04-07 09:57:00.203925 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/find_user_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2862 2023-04-07 09:57:00.199716 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/find_user_response_all_of_users.cpython-38.pyc
+-rw-r--r--   0        0        0     2960 2023-04-07 09:57:00.207199 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/generate_features_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2682 2023-04-07 09:57:00.210334 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/generic_api_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3264 2023-04-07 09:57:00.212949 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_all_third_party_auth_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2995 2023-04-07 09:57:00.218649 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_all_third_party_auth_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3218 2023-04-07 09:57:00.222549 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_all_whitelabels_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2949 2023-04-07 09:57:00.229772 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_all_whitelabels_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3705 2023-04-07 09:57:00.233344 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_data_explorer_features_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3507 2023-04-07 09:57:00.244023 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_data_explorer_features_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     4189 2023-04-07 09:57:00.246972 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_data_explorer_settings_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3086 2023-04-07 09:57:00.250100 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_data_explorer_settings_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2895 2023-04-07 09:57:00.252553 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_deployment_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2692 2023-04-07 09:57:00.255172 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_deployment_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2871 2023-04-07 09:57:00.259101 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_device_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2615 2023-04-07 09:57:00.262383 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_device_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3964 2023-04-07 09:57:00.265479 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_impulse_blocks_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3721 2023-04-07 09:57:00.277136 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_impulse_blocks_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2886 2023-04-07 09:57:00.281124 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_impulse_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2630 2023-04-07 09:57:00.295190 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_impulse_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2826 2023-04-07 09:57:00.307923 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_job_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2570 2023-04-07 09:57:00.314115 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_job_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3172 2023-04-07 09:57:00.297809 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_jwt_token_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2957 2023-04-07 09:57:00.302233 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_jwt_token_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2783 2023-04-07 09:57:00.305287 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_jwt_token_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3359 2023-04-07 09:57:00.318086 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_last_deployment_build_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3164 2023-04-07 09:57:00.324612 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_last_deployment_build_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3470 2023-04-07 09:57:00.320394 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_last_deployment_build_response_all_of_last_build.cpython-38.pyc
+-rw-r--r--   0        0        0     3085 2023-04-07 09:57:00.329005 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_notes_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2816 2023-04-07 09:57:00.337986 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_notes_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3042 2023-04-07 09:57:00.341615 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_organization_data_item_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2748 2023-04-07 09:57:00.355057 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_organization_data_item_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3030 2023-04-07 09:57:00.358868 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_organization_dataset_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2736 2023-04-07 09:57:00.361841 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_organization_dataset_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3055 2023-04-07 09:57:00.364239 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_organization_pipelines_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2761 2023-04-07 09:57:00.413757 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_organization_pipelines_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3888 2023-04-07 09:57:00.416393 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_organization_portal_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3715 2023-04-07 09:57:00.420974 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_organization_portal_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3000 2023-04-07 09:57:00.425004 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_organization_projects_data_count_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3516 2023-04-07 09:57:00.427947 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_performance_calibration_ground_truth_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3247 2023-04-07 09:57:00.438625 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_performance_calibration_ground_truth_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3582 2023-04-07 09:57:00.442520 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_performance_calibration_parameter_sets_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3339 2023-04-07 09:57:00.471165 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_performance_calibration_parameter_sets_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3239 2023-04-07 09:57:00.473670 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_performance_calibration_parameters_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2983 2023-04-07 09:57:00.476960 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_performance_calibration_parameters_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3498 2023-04-07 09:57:00.480462 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_performance_calibration_raw_result_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3229 2023-04-07 09:57:00.486828 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_performance_calibration_raw_result_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3503 2023-04-07 09:57:00.489223 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_performance_calibration_status_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3349 2023-04-07 09:57:00.498009 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_performance_calibration_status_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3838 2023-04-07 09:57:00.501974 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_pretrained_model_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3643 2023-04-07 09:57:00.548103 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_pretrained_model_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3922 2023-04-07 09:57:00.504214 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_pretrained_model_response_all_of_model.cpython-38.pyc
+-rw-r--r--   0        0        0     3178 2023-04-07 09:57:00.543893 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_pretrained_model_response_all_of_model_info.cpython-38.pyc
+-rw-r--r--   0        0        0     3238 2023-04-07 09:57:00.506500 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_pretrained_model_response_all_of_model_profile_info.cpython-38.pyc
+-rw-r--r--   0        0        0     2927 2023-04-07 09:57:00.553230 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_public_metrics_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2638 2023-04-07 09:57:00.557909 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_public_metrics_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3279 2023-04-07 09:57:00.560913 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_sample_metadata_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3222 2023-04-07 09:57:00.568626 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_sample_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3009 2023-04-07 09:57:00.572325 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_syntiant_posterior_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2806 2023-04-07 09:57:00.575303 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_syntiant_posterior_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2856 2023-04-07 09:57:00.577760 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_theme_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2600 2023-04-07 09:57:00.598021 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_theme_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3101 2023-04-07 09:57:00.600741 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_themes_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2832 2023-04-07 09:57:00.603592 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_themes_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2964 2023-04-07 09:57:00.607102 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_third_party_auth_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2670 2023-04-07 09:57:00.611135 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_third_party_auth_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3228 2023-04-07 09:57:00.614009 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_user_need_to_set_password_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3075 2023-04-07 09:57:00.618498 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_user_need_to_set_password_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     6162 2023-04-07 09:57:00.622357 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_user_response.cpython-38.pyc
+-rw-r--r--   0        0        0     5171 2023-04-07 09:57:00.630804 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_user_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2778 2023-04-07 09:57:00.624662 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_user_response_all_of_whitelabels.cpython-38.pyc
+-rw-r--r--   0        0        0     2883 2023-04-07 09:57:00.634358 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_whitelabel_domain_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2674 2023-04-07 09:57:00.638549 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_whitelabel_domain_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2931 2023-04-07 09:57:00.641435 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_whitelabel_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2675 2023-04-07 09:57:00.644130 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/get_whitelabel_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3172 2023-04-07 09:57:00.647566 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/has_data_explorer_features_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2969 2023-04-07 09:57:00.651048 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/has_data_explorer_features_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3670 2023-04-07 09:57:00.283366 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/impulse.cpython-38.pyc
+-rw-r--r--   0        0        0     6336 2023-04-07 09:57:00.654137 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/impulse_block_version.cpython-38.pyc
+-rw-r--r--   0        0        0     6043 2023-04-07 09:57:00.285822 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/impulse_dsp_block.cpython-38.pyc
+-rw-r--r--   0        0        0     2600 2023-04-07 09:57:00.287670 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/impulse_dsp_block_organization.cpython-38.pyc
+-rw-r--r--   0        0        0     7998 2023-04-07 09:57:00.236435 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/impulse_input_block.cpython-38.pyc
+-rw-r--r--   0        0        0     5397 2023-04-07 09:56:59.699942 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/impulse_learn_block.cpython-38.pyc
+-rw-r--r--   0        0        0     2954 2023-04-07 09:57:00.267562 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/input_block.cpython-38.pyc
+-rw-r--r--   0        0        0     3158 2023-04-07 09:57:00.659774 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/invite_organization_member_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3633 2023-04-07 09:57:00.310015 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/job.cpython-38.pyc
+-rw-r--r--   0        0        0     3194 2023-04-07 09:57:00.662879 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/job_summary_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2925 2023-04-07 09:57:00.669798 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/job_summary_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2724 2023-04-07 09:57:00.664744 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/job_summary_response_all_of_summary.cpython-38.pyc
+-rw-r--r--   0        0        0     2730 2023-04-07 09:57:00.672437 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_model_layer.cpython-38.pyc
+-rw-r--r--   0        0        0     2656 2023-04-07 09:57:00.674402 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_model_layer_input.cpython-38.pyc
+-rw-r--r--   0        0        0     2668 2023-04-07 09:57:00.677430 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_model_layer_output.cpython-38.pyc
+-rw-r--r--   0        0        0     5011 2023-04-07 09:57:00.682293 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_model_metadata.cpython-38.pyc
+-rw-r--r--   0        0        0     4853 2023-04-07 09:57:00.696576 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_model_metadata_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     4783 2023-04-07 09:57:00.684612 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_model_metadata_metrics.cpython-38.pyc
+-rw-r--r--   0        0        0     3382 2023-04-07 09:57:00.686616 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_model_metadata_metrics_on_device_performance_inner.cpython-38.pyc
+-rw-r--r--   0        0        0     3100 2023-04-07 09:57:00.688650 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_model_metadata_metrics_on_device_performance_inner_tflite.cpython-38.pyc
+-rw-r--r--   0        0        0      861 2023-04-07 09:56:59.666041 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_model_type_enum.cpython-38.pyc
+-rw-r--r--   0        0        0     7417 2023-04-07 09:57:00.701308 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_response.cpython-38.pyc
+-rw-r--r--   0        0        0     7278 2023-04-07 09:57:00.719973 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3653 2023-04-07 09:57:00.703847 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_visual_layer.cpython-38.pyc
+-rw-r--r--   0        0        0     2611 2023-04-07 09:57:00.705700 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/keras_visual_layer_type.cpython-38.pyc
+-rw-r--r--   0        0        0     3033 2023-04-07 09:57:00.724843 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/last_modification_date_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2803 2023-04-07 09:57:00.727543 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/last_modification_date_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2916 2023-04-07 09:57:00.729955 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/latency_device.cpython-38.pyc
+-rw-r--r--   0        0        0     2816 2023-04-07 09:57:00.271812 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/learn_block.cpython-38.pyc
+-rw-r--r--   0        0        0     1177 2023-04-07 09:56:59.701852 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/learn_block_type.cpython-38.pyc
+-rw-r--r--   0        0        0     3265 2023-04-07 09:57:00.733887 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_api_keys_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3030 2023-04-07 09:57:00.741351 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_api_keys_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3301 2023-04-07 09:57:00.737292 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_api_keys_response_all_of_api_keys.cpython-38.pyc
+-rw-r--r--   0        0        0     3139 2023-04-07 09:57:00.743844 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_devices_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2888 2023-04-07 09:57:00.747520 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_devices_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3199 2023-04-07 09:57:00.750508 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_email_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2966 2023-04-07 09:57:00.757902 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_email_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3267 2023-04-07 09:57:00.752616 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_email_response_all_of_emails.cpython-38.pyc
+-rw-r--r--   0        0        0     3285 2023-04-07 09:57:00.761168 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_hmac_keys_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3050 2023-04-07 09:57:00.766920 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_hmac_keys_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2945 2023-04-07 09:57:00.763190 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_hmac_keys_response_all_of_hmac_keys.cpython-38.pyc
+-rw-r--r--   0        0        0     3217 2023-04-07 09:57:00.769730 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_jobs_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2989 2023-04-07 09:57:00.774809 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_jobs_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2787 2023-04-07 09:57:00.777557 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_models_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2567 2023-04-07 09:57:00.780143 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_models_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3447 2023-04-07 09:57:00.783593 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_api_keys_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3212 2023-04-07 09:57:00.790370 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_api_keys_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3423 2023-04-07 09:57:00.786169 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_api_keys_response_all_of_api_keys.cpython-38.pyc
+-rw-r--r--   0        0        0     3391 2023-04-07 09:57:00.793589 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_buckets_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3122 2023-04-07 09:57:00.801756 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_buckets_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3397 2023-04-07 09:57:00.796980 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_buckets_response_all_of_buckets.cpython-38.pyc
+-rw-r--r--   0        0        0     3453 2023-04-07 09:57:00.804283 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_buckets_user_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3184 2023-04-07 09:57:00.812006 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_buckets_user_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3490 2023-04-07 09:57:00.806940 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_buckets_user_response_all_of_buckets.cpython-38.pyc
+-rw-r--r--   0        0        0     3656 2023-04-07 09:57:00.814825 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_data_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3472 2023-04-07 09:57:00.824010 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_data_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3656 2023-04-07 09:57:00.818048 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_data_response_all_of_data.cpython-38.pyc
+-rw-r--r--   0        0        0     3425 2023-04-07 09:57:00.827485 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_deploy_blocks_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3182 2023-04-07 09:57:00.836564 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_deploy_blocks_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3374 2023-04-07 09:57:00.839695 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_dsp_blocks_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3131 2023-04-07 09:57:00.850201 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_dsp_blocks_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3668 2023-04-07 09:57:00.853817 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_files_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3485 2023-04-07 09:57:00.857770 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_files_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3343 2023-04-07 09:57:00.861269 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_pipelines_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3074 2023-04-07 09:57:00.865456 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_pipelines_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3391 2023-04-07 09:57:00.868187 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_portals_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3122 2023-04-07 09:57:00.876322 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_portals_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3253 2023-04-07 09:57:00.870329 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_portals_response_all_of_portals.cpython-38.pyc
+-rw-r--r--   0        0        0     3801 2023-04-07 09:57:00.879906 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_projects_data_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3537 2023-04-07 09:57:00.885559 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_projects_data_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2926 2023-04-07 09:57:00.881851 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_projects_data_response_all_of_projects.cpython-38.pyc
+-rw-r--r--   0        0        0     3290 2023-04-07 09:57:00.888084 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_projects_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3021 2023-04-07 09:57:00.892278 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_projects_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3391 2023-04-07 09:57:00.895030 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_secrets_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3122 2023-04-07 09:57:00.902928 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_secrets_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2897 2023-04-07 09:57:00.897232 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_secrets_response_all_of_secrets.cpython-38.pyc
+-rw-r--r--   0        0        0     3598 2023-04-07 09:57:00.905885 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_transfer_learning_blocks_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3355 2023-04-07 09:57:00.913810 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_transfer_learning_blocks_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3561 2023-04-07 09:57:00.918234 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_transformation_blocks_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3318 2023-04-07 09:57:00.925944 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organization_transformation_blocks_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3259 2023-04-07 09:57:00.929598 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organizations_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3026 2023-04-07 09:57:00.932523 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_organizations_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2595 2023-04-07 09:57:00.934898 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_portal_files_in_folder_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3297 2023-04-07 09:57:00.937443 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_portal_files_in_folder_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3046 2023-04-07 09:57:00.944932 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_portal_files_in_folder_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2782 2023-04-07 09:57:00.947499 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_projects.cpython-38.pyc
+-rw-r--r--   0        0        0     3174 2023-04-07 09:57:00.950457 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_projects_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3022 2023-04-07 09:57:00.954072 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_public_projects.cpython-38.pyc
+-rw-r--r--   0        0        0     3409 2023-04-07 09:57:00.963752 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_public_projects_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3320 2023-04-07 09:57:00.968033 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_public_versions_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3051 2023-04-07 09:57:00.973458 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_public_versions_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2873 2023-04-07 09:57:00.970049 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_public_versions_response_all_of_versions.cpython-38.pyc
+-rw-r--r--   0        0        0     3237 2023-04-07 09:57:00.976584 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_samples_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2994 2023-04-07 09:57:00.979996 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_samples_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     4058 2023-04-07 09:57:00.982768 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_versions_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3823 2023-04-07 09:57:00.996971 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_versions_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2912 2023-04-07 09:57:00.990072 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_versions_response_all_of_bucket.cpython-38.pyc
+-rw-r--r--   0        0        0     2726 2023-04-07 09:57:00.984733 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_versions_response_all_of_custom_learn_blocks.cpython-38.pyc
+-rw-r--r--   0        0        0     3842 2023-04-07 09:57:00.987516 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/list_versions_response_all_of_versions.cpython-38.pyc
+-rw-r--r--   0        0        0     3352 2023-04-07 09:57:01.000646 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/log_stdout_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3117 2023-04-07 09:57:01.007082 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/log_stdout_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3113 2023-04-07 09:57:01.003298 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/log_stdout_response_all_of_stdout.cpython-38.pyc
+-rw-r--r--   0        0        0     2747 2023-04-07 09:57:01.009883 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/log_website_pageview_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2760 2023-04-07 09:57:01.012907 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/login_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2522 2023-04-07 09:57:01.015639 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/login_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2961 2023-04-07 09:56:59.686213 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/model_prediction.cpython-38.pyc
+-rw-r--r--   0        0        0     3114 2023-04-07 09:56:59.691227 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/model_result.cpython-38.pyc
+-rw-r--r--   0        0        0     4585 2023-04-07 09:57:00.163977 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/model_variant_stats.cpython-38.pyc
+-rw-r--r--   0        0        0     2796 2023-04-07 09:57:01.018057 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/move_raw_data_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3040 2023-04-07 09:57:00.331896 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/note.cpython-38.pyc
+-rw-r--r--   0        0        0     2951 2023-04-07 09:57:01.020968 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/object_detection_auto_label_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3506 2023-04-07 09:57:01.025175 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/object_detection_auto_label_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3283 2023-04-07 09:57:01.031320 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/object_detection_auto_label_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2910 2023-04-07 09:57:01.027284 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/object_detection_auto_label_response_all_of_results.cpython-38.pyc
+-rw-r--r--   0        0        0     3017 2023-04-07 09:57:01.035224 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/object_detection_label_queue_count_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2749 2023-04-07 09:57:01.038558 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/object_detection_label_queue_count_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3428 2023-04-07 09:57:01.041199 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/object_detection_label_queue_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3159 2023-04-07 09:57:01.045176 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/object_detection_label_queue_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0      926 2023-04-07 09:56:59.372808 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/object_detection_last_layer.cpython-38.pyc
+-rw-r--r--   0        0        0     5938 2023-04-07 09:57:01.048354 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_config.cpython-38.pyc
+-rw-r--r--   0        0        0     6318 2023-04-07 09:57:01.060891 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_config_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2574 2023-04-07 09:57:01.066703 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_config_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2684 2023-04-07 09:57:01.050353 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_config_target_device.cpython-38.pyc
+-rw-r--r--   0        0        0     2902 2023-04-07 09:57:01.069336 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_dsp_parameters_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2628 2023-04-07 09:57:01.072194 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_dsp_parameters_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3252 2023-04-07 09:57:01.075897 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_space_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3019 2023-04-07 09:57:01.081251 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_space_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     4667 2023-04-07 09:57:01.084266 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_state_response.cpython-38.pyc
+-rw-r--r--   0        0        0     4489 2023-04-07 09:57:01.104005 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_state_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3643 2023-04-07 09:57:01.087611 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_state_response_all_of_status.cpython-38.pyc
+-rw-r--r--   0        0        0     3067 2023-04-07 09:57:01.091309 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_state_response_all_of_workers.cpython-38.pyc
+-rw-r--r--   0        0        0     3240 2023-04-07 09:57:01.108852 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_transfer_learning_models_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2984 2023-04-07 09:57:01.115780 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_transfer_learning_models_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     4222 2023-04-07 09:57:01.111982 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/optimize_transfer_learning_models_response_all_of_models.cpython-38.pyc
+-rw-r--r--   0        0        0     3800 2023-04-07 09:56:59.573272 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization.cpython-38.pyc
+-rw-r--r--   0        0        0     2910 2023-04-07 09:57:01.118150 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_add_data_folder_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3079 2023-04-07 09:57:01.121190 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_add_data_folder_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2851 2023-04-07 09:57:01.125148 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_add_data_folder_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     6679 2023-04-07 09:57:00.386623 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_create_project.cpython-38.pyc
+-rw-r--r--   0        0        0     4658 2023-04-07 09:57:01.128467 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_create_project_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3108 2023-04-07 09:57:01.134043 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_create_project_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2868 2023-04-07 09:57:01.137368 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_create_project_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3203 2023-04-07 09:57:01.140107 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_create_project_status_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2947 2023-04-07 09:57:01.154144 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_create_project_status_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3024 2023-04-07 09:57:00.388657 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_create_project_transformation_summary.cpython-38.pyc
+-rw-r--r--   0        0        0     7359 2023-04-07 09:57:01.143073 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_create_project_with_files.cpython-38.pyc
+-rw-r--r--   0        0        0     3161 2023-04-07 09:57:01.156844 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_create_project_with_files_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3340 2023-04-07 09:57:01.145152 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_create_project_with_files_all_of_files.cpython-38.pyc
+-rw-r--r--   0        0        0     3667 2023-04-07 09:57:00.343969 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_data_item.cpython-38.pyc
+-rw-r--r--   0        0        0     2718 2023-04-07 09:57:00.346050 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_data_item_files_inner.cpython-38.pyc
+-rw-r--r--   0        0        0     2951 2023-04-07 09:56:59.576897 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_dataset.cpython-38.pyc
+-rw-r--r--   0        0        0     4423 2023-04-07 09:57:00.830748 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_deploy_block.cpython-38.pyc
+-rw-r--r--   0        0        0     3621 2023-04-07 09:57:00.844512 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_dsp_block.cpython-38.pyc
+-rw-r--r--   0        0        0     3586 2023-04-07 09:57:01.160114 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_get_create_projects_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3343 2023-04-07 09:57:01.168313 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_get_create_projects_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     4919 2023-04-07 09:57:01.162519 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_get_create_projects_response_all_of_jobs.cpython-38.pyc
+-rw-r--r--   0        0        0     5048 2023-04-07 09:57:01.172715 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_info_response.cpython-38.pyc
+-rw-r--r--   0        0        0     4839 2023-04-07 09:57:01.176697 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_info_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3027 2023-04-07 09:56:59.581412 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_info_response_all_of_default_compute_limits.cpython-38.pyc
+-rw-r--r--   0        0        0     3112 2023-04-07 09:56:59.584399 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_info_response_all_of_entitlement_limits.cpython-38.pyc
+-rw-r--r--   0        0        0     3040 2023-04-07 09:57:01.179749 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_metrics_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2746 2023-04-07 09:57:01.186628 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_metrics_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3754 2023-04-07 09:57:01.182624 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_metrics_response_all_of_metrics.cpython-38.pyc
+-rw-r--r--   0        0        0     5212 2023-04-07 09:57:00.366784 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_pipeline.cpython-38.pyc
+-rw-r--r--   0        0        0     3034 2023-04-07 09:57:00.370400 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_pipeline_feeding_into_dataset.cpython-38.pyc
+-rw-r--r--   0        0        0     2878 2023-04-07 09:57:00.374179 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_pipeline_feeding_into_project.cpython-38.pyc
+-rw-r--r--   0        0        0     2785 2023-04-07 09:57:00.379948 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_pipeline_item_count.cpython-38.pyc
+-rw-r--r--   0        0        0     3925 2023-04-07 09:57:00.377313 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_pipeline_run.cpython-38.pyc
+-rw-r--r--   0        0        0     4546 2023-04-07 09:57:00.383762 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_pipeline_run_step.cpython-38.pyc
+-rw-r--r--   0        0        0     4306 2023-04-07 09:57:00.405526 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_pipeline_step.cpython-38.pyc
+-rw-r--r--   0        0        0     3044 2023-04-07 09:57:01.188917 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_projects_data_batch_disable_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3033 2023-04-07 09:57:01.191953 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_projects_data_batch_enable_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2738 2023-04-07 09:57:01.195707 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_projects_data_batch_request.cpython-38.pyc
+-rw-r--r--   0        0        0     4381 2023-04-07 09:57:00.908732 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_transfer_learning_block.cpython-38.pyc
+-rw-r--r--   0        0        0      931 2023-04-07 09:56:59.407539 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_transfer_learning_operates_on.cpython-38.pyc
+-rw-r--r--   0        0        0     4897 2023-04-07 09:57:00.920818 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_transformation_block.cpython-38.pyc
+-rw-r--r--   0        0        0     4204 2023-04-07 09:57:01.198681 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_update_pipeline_body.cpython-38.pyc
+-rw-r--r--   0        0        0     3625 2023-04-07 09:56:59.435098 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/organization_user.cpython-38.pyc
+-rw-r--r--   0        0        0     2748 2023-04-07 09:57:00.447413 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_detection.cpython-38.pyc
+-rw-r--r--   0        0        0     3998 2023-04-07 09:57:00.456868 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_false_positive.cpython-38.pyc
+-rw-r--r--   0        0        0     4238 2023-04-07 09:57:00.431206 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_ground_truth.cpython-38.pyc
+-rw-r--r--   0        0        0     3110 2023-04-07 09:57:00.433549 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_ground_truth_samples_inner.cpython-38.pyc
+-rw-r--r--   0        0        0     4590 2023-04-07 09:57:00.445445 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_parameter_set.cpython-38.pyc
+-rw-r--r--   0        0        0     2884 2023-04-07 09:57:00.450181 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_parameter_set_aggregate_stats.cpython-38.pyc
+-rw-r--r--   0        0        0     4191 2023-04-07 09:57:00.454327 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_parameter_set_stats_inner.cpython-38.pyc
+-rw-r--r--   0        0        0     3457 2023-04-07 09:57:00.462442 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_parameters.cpython-38.pyc
+-rw-r--r--   0        0        0     3081 2023-04-07 09:57:00.465737 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_parameters_standard.cpython-38.pyc
+-rw-r--r--   0        0        0     2889 2023-04-07 09:57:00.482468 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_raw_detection.cpython-38.pyc
+-rw-r--r--   0        0        0     2872 2023-04-07 09:57:01.202591 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_save_parameter_set_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3101 2023-04-07 09:57:01.206345 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_upload_labeled_audio_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2853 2023-04-07 09:57:01.209360 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/performance_calibration_upload_labeled_audio_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2729 2023-04-07 09:57:00.940070 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/portal_file.cpython-38.pyc
+-rw-r--r--   0        0        0     2831 2023-04-07 09:57:01.211903 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/portal_info_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3195 2023-04-07 09:57:00.538516 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/pretrained_model_tensor.cpython-38.pyc
+-rw-r--r--   0        0        0     3160 2023-04-07 09:57:00.508639 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/profile_model_info.cpython-38.pyc
+-rw-r--r--   0        0        0     2937 2023-04-07 09:57:00.511068 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/profile_model_info_memory.cpython-38.pyc
+-rw-r--r--   0        0        0     2532 2023-04-07 09:57:00.514988 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/profile_model_info_memory_eon.cpython-38.pyc
+-rw-r--r--   0        0        0     2667 2023-04-07 09:57:00.518069 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/profile_model_info_memory_tflite.cpython-38.pyc
+-rw-r--r--   0        0        0     3616 2023-04-07 09:57:00.523689 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/profile_model_table.cpython-38.pyc
+-rw-r--r--   0        0        0     3088 2023-04-07 09:57:00.526183 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/profile_model_table_mcu.cpython-38.pyc
+-rw-r--r--   0        0        0     2829 2023-04-07 09:57:00.528277 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/profile_model_table_mcu_memory.cpython-38.pyc
+-rw-r--r--   0        0        0     2781 2023-04-07 09:57:00.531988 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/profile_model_table_mpu.cpython-38.pyc
+-rw-r--r--   0        0        0     2753 2023-04-07 09:57:01.215124 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/profile_tf_lite_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3435 2023-04-07 09:57:01.219782 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/profile_tf_lite_response.cpython-38.pyc
+-rw-r--r--   0        0        0     5498 2023-04-07 09:56:59.444208 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project.cpython-38.pyc
+-rw-r--r--   0        0        0     3382 2023-04-07 09:56:59.447376 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_collaborator.cpython-38.pyc
+-rw-r--r--   0        0        0     2527 2023-04-07 09:57:01.223372 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_collaborator_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3030 2023-04-07 09:57:01.225654 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_data_axes_summary_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2790 2023-04-07 09:57:01.229590 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_data_axes_summary_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2890 2023-04-07 09:57:01.232521 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_data_interval_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2622 2023-04-07 09:57:01.235200 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_data_interval_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2792 2023-04-07 09:57:01.237557 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_data_summary.cpython-38.pyc
+-rw-r--r--   0        0        0     5359 2023-04-07 09:57:01.240837 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_deployment_target.cpython-38.pyc
+-rw-r--r--   0        0        0     3163 2023-04-07 09:57:01.246760 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_deployment_target_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3339 2023-04-07 09:57:01.249474 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_deployment_targets_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3070 2023-04-07 09:57:01.252241 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_deployment_targets_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3197 2023-04-07 09:57:01.255838 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_downloads_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2928 2023-04-07 09:57:01.258837 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_downloads_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     9046 2023-04-07 09:57:01.262585 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response.cpython-38.pyc
+-rw-r--r--   0        0        0     8883 2023-04-07 09:57:01.300615 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3617 2023-04-07 09:57:01.264972 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response_all_of_acquisition_settings.cpython-38.pyc
+-rw-r--r--   0        0        0     3190 2023-04-07 09:57:01.269083 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response_all_of_compute_time.cpython-38.pyc
+-rw-r--r--   0        0        0     3081 2023-04-07 09:57:01.271798 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response_all_of_data_summary_per_category.cpython-38.pyc
+-rw-r--r--   0        0        0     3398 2023-04-07 09:57:01.274288 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response_all_of_deploy_settings.cpython-38.pyc
+-rw-r--r--   0        0        0     2933 2023-04-07 09:56:59.587167 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response_all_of_experiments.cpython-38.pyc
+-rw-r--r--   0        0        0     2842 2023-04-07 09:57:01.277267 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response_all_of_impulse.cpython-38.pyc
+-rw-r--r--   0        0        0     3168 2023-04-07 09:57:01.279676 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response_all_of_performance.cpython-38.pyc
+-rw-r--r--   0        0        0     2594 2023-04-07 09:56:59.590852 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response_all_of_readme.cpython-38.pyc
+-rw-r--r--   0        0        0     2941 2023-04-07 09:57:01.283889 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response_all_of_show_getting_started_wizard.cpython-38.pyc
+-rw-r--r--   0        0        0     3177 2023-04-07 09:57:01.287461 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_response_all_of_urls.cpython-38.pyc
+-rw-r--r--   0        0        0     3022 2023-04-07 09:57:01.305661 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_summary_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2774 2023-04-07 09:57:01.308823 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_info_summary_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3709 2023-04-07 09:57:01.311925 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_private_data.cpython-38.pyc
+-rw-r--r--   0        0        0     4325 2023-04-07 09:57:00.956391 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_public_data.cpython-38.pyc
+-rw-r--r--   0        0        0     2515 2023-04-07 09:57:00.958214 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_public_data_readme.cpython-38.pyc
+-rw-r--r--   0        0        0     2935 2023-04-07 09:57:01.316220 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_sample_metadata.cpython-38.pyc
+-rw-r--r--   0        0        0     2863 2023-04-07 09:57:01.319033 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/project_version_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2861 2023-04-07 09:56:59.736631 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/raw_sample_data.cpython-38.pyc
+-rw-r--r--   0        0        0     3762 2023-04-07 09:56:59.739117 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/raw_sample_payload.cpython-38.pyc
+-rw-r--r--   0        0        0     2995 2023-04-07 09:57:01.322475 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/rebalance_dataset_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2596 2023-04-07 09:57:01.326983 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/remove_collaborator_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2412 2023-04-07 09:57:01.329719 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/remove_member_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2484 2023-04-07 09:57:01.332061 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/rename_device_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2629 2023-04-07 09:57:01.334761 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/rename_portal_file_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2484 2023-04-07 09:57:01.338674 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/rename_sample_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2504 2023-04-07 09:57:01.341263 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/request_reset_password_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2584 2023-04-07 09:57:01.343890 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/reset_password_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2642 2023-04-07 09:57:01.347648 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/restore_project_from_public_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2763 2023-04-07 09:57:01.351771 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/restore_project_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3085 2023-04-07 09:57:01.354911 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/run_organization_pipeline_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2817 2023-04-07 09:57:01.357763 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/run_organization_pipeline_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     8008 2023-04-07 09:56:59.713102 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/sample.cpython-38.pyc
+-rw-r--r--   0        0        0     2964 2023-04-07 09:57:01.360933 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/sample_bounding_boxes_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2590 2023-04-07 09:57:00.563500 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/sample_metadata.cpython-38.pyc
+-rw-r--r--   0        0        0     2943 2023-04-07 09:57:01.364914 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/save_pretrained_model_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3301 2023-04-07 09:57:01.367725 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/score_trial_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3012 2023-04-07 09:57:01.377141 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/score_trial_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2782 2023-04-07 09:57:01.369726 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/score_trial_response_all_of_latency.cpython-38.pyc
+-rw-r--r--   0        0        0     2528 2023-04-07 09:57:01.372707 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/score_trial_response_all_of_ram.cpython-38.pyc
+-rw-r--r--   0        0        0     2896 2023-04-07 09:57:01.380128 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/segment_sample_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2690 2023-04-07 09:57:01.382064 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/segment_sample_request_segments_inner.cpython-38.pyc
+-rw-r--r--   0        0        0     3723 2023-04-07 09:57:01.386184 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/send_user_feedback_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2509 2023-04-07 09:56:59.716455 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/sensor.cpython-38.pyc
+-rw-r--r--   0        0        0     2742 2023-04-07 09:57:01.390406 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_anomaly_parameter_request.cpython-38.pyc
+-rw-r--r--   0        0        0     6318 2023-04-07 09:57:01.393387 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_keras_parameter_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2521 2023-04-07 09:57:01.397510 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_member_datasets_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2728 2023-04-07 09:57:01.401088 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_member_role_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2688 2023-04-07 09:57:01.403935 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_optimize_space_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2745 2023-04-07 09:57:01.406364 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_optimize_space_request_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2573 2023-04-07 09:57:01.408691 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_organization_data_dataset_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2618 2023-04-07 09:57:01.412395 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_project_compute_time_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2643 2023-04-07 09:57:01.415010 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_project_dsp_file_size_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2554 2023-04-07 09:57:01.417319 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_sample_metadata_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2549 2023-04-07 09:57:01.419829 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_syntiant_posterior_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2649 2023-04-07 09:57:01.422164 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/set_user_password_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2966 2023-04-07 09:57:01.425857 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/socket_token_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2710 2023-04-07 09:57:01.432741 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/socket_token_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2677 2023-04-07 09:57:01.428790 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/socket_token_response_all_of_token.cpython-38.pyc
+-rw-r--r--   0        0        0     2637 2023-04-07 09:57:01.436337 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/split_sample_in_frames_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2597 2023-04-07 09:56:59.438637 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/staff_info.cpython-38.pyc
+-rw-r--r--   0        0        0     2800 2023-04-07 09:57:01.439079 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/start_job_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2542 2023-04-07 09:57:01.441835 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/start_job_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3338 2023-04-07 09:57:00.492477 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/start_performance_calibration_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3385 2023-04-07 09:57:01.444420 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/start_sampling_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2801 2023-04-07 09:57:01.448730 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/start_sampling_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2545 2023-04-07 09:57:01.451722 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/start_sampling_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3039 2023-04-07 09:57:01.454357 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/start_training_request_anomaly.cpython-38.pyc
+-rw-r--r--   0        0        0     2584 2023-04-07 09:57:01.457334 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/store_segment_length_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3225 2023-04-07 09:56:59.707498 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/structured_classify_result.cpython-38.pyc
+-rw-r--r--   0        0        0     2831 2023-04-07 09:57:01.460423 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/test_pretrained_model_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3536 2023-04-07 09:57:01.463180 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/test_pretrained_model_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3326 2023-04-07 09:57:01.466175 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/test_pretrained_model_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3167 2023-04-07 09:57:00.579837 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/theme.cpython-38.pyc
+-rw-r--r--   0        0        0     2670 2023-04-07 09:57:00.583410 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/theme_colors.cpython-38.pyc
+-rw-r--r--   0        0        0     2874 2023-04-07 09:57:00.587413 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/theme_favicon.cpython-38.pyc
+-rw-r--r--   0        0        0     2832 2023-04-07 09:57:00.592413 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/theme_logos.cpython-38.pyc
+-rw-r--r--   0        0        0     2723 2023-04-07 09:57:00.214827 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/third_party_auth.cpython-38.pyc
+-rw-r--r--   0        0        0     2564 2023-04-07 09:57:01.468747 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/track_objects_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3196 2023-04-07 09:57:01.473182 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/track_objects_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2953 2023-04-07 09:57:01.476539 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/track_objects_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     4438 2023-04-07 09:57:00.710434 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/transfer_learning_model.cpython-38.pyc
+-rw-r--r--   0        0        0     2672 2023-04-07 09:57:01.478970 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/transfer_ownership_organization_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3271 2023-04-07 09:56:59.416990 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/transformation_block_additional_mount_point.cpython-38.pyc
+-rw-r--r--   0        0        0      896 2023-04-07 09:57:00.392563 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/transformation_job_status_enum.cpython-38.pyc
+-rw-r--r--   0        0        0     2959 2023-04-07 09:57:01.482207 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/tuner_create_trial_impulse.cpython-38.pyc
+-rw-r--r--   0        0        0     3015 2023-04-07 09:57:01.054151 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/tuner_space_impulse.cpython-38.pyc
+-rw-r--r--   0        0        0     3684 2023-04-07 09:57:01.094415 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/tuner_trial.cpython-38.pyc
+-rw-r--r--   0        0        0     2835 2023-04-07 09:57:01.096438 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/tuner_trial_blocks_inner.cpython-38.pyc
+-rw-r--r--   0        0        0     2617 2023-04-07 09:57:01.486384 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_job_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2924 2023-04-07 09:57:01.488989 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_add_collaborator_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3156 2023-04-07 09:57:01.491533 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_bucket_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3184 2023-04-07 09:57:01.496318 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_create_empty_project_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3022 2023-04-07 09:57:01.499552 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_create_project_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2777 2023-04-07 09:57:01.502164 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_data_item_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2710 2023-04-07 09:57:01.505081 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_dataset_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3210 2023-04-07 09:57:01.508948 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_dsp_block_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3216 2023-04-07 09:57:01.513719 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_portal_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3043 2023-04-07 09:57:01.516935 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_portal_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3060 2023-04-07 09:57:01.519847 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_request.cpython-38.pyc
+-rw-r--r--   0        0        0     4192 2023-04-07 09:57:01.524406 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_transfer_learning_block_request.cpython-38.pyc
+-rw-r--r--   0        0        0     4720 2023-04-07 09:57:01.528714 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_organization_transformation_block_request.cpython-38.pyc
+-rw-r--r--   0        0        0     6483 2023-04-07 09:57:01.533398 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_project_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2517 2023-04-07 09:57:01.539845 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_project_tags_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2780 2023-04-07 09:57:01.542398 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_theme_colors_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3068 2023-04-07 09:57:01.545659 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_theme_logos_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2756 2023-04-07 09:57:01.549616 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_third_party_auth_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2824 2023-04-07 09:57:01.552868 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_user_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2486 2023-04-07 09:57:01.555853 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_version_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2844 2023-04-07 09:57:01.559283 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/update_whitelabel_deployment_targets_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2739 2023-04-07 09:57:01.563400 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/upload_asset_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2524 2023-04-07 09:57:01.566599 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/upload_asset_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2811 2023-04-07 09:57:01.569992 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/upload_readme_image_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2789 2023-04-07 09:57:01.576393 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/upload_user_photo_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2515 2023-04-07 09:57:01.579336 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/upload_user_photo_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3148 2023-04-07 09:57:01.291619 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/user.cpython-38.pyc
+-rw-r--r--   0        0        0     2641 2023-04-07 09:57:01.583830 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/user_by_third_party_activation_request.cpython-38.pyc
+-rw-r--r--   0        0        0     2698 2023-04-07 09:56:59.470446 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/user_experiment.cpython-38.pyc
+-rw-r--r--   0        0        0     3060 2023-04-07 09:56:59.475151 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/user_organization.cpython-38.pyc
+-rw-r--r--   0        0        0     2470 2023-04-07 09:57:01.586723 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/verify_dsp_block_url_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3054 2023-04-07 09:57:01.589190 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/verify_dsp_block_url_response.cpython-38.pyc
+-rw-r--r--   0        0        0     2798 2023-04-07 09:57:01.594825 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/verify_dsp_block_url_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2915 2023-04-07 09:57:01.591114 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/verify_dsp_block_url_response_all_of_block.cpython-38.pyc
+-rw-r--r--   0        0        0     3156 2023-04-07 09:57:01.598881 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/verify_organization_bucket_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3440 2023-04-07 09:57:01.602645 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/verify_organization_bucket_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3207 2023-04-07 09:57:01.610645 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/verify_organization_bucket_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     2852 2023-04-07 09:57:01.604584 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/verify_organization_bucket_response_all_of_files.cpython-38.pyc
+-rw-r--r--   0        0        0     2545 2023-04-07 09:57:01.614747 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/verify_reset_password_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3293 2023-04-07 09:57:00.225388 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/whitelabel.cpython-38.pyc
+-rw-r--r--   0        0        0     3132 2023-04-07 09:57:01.617863 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/whitelabel_admin_create_organization_request.cpython-38.pyc
+-rw-r--r--   0        0        0     3317 2023-04-07 09:57:01.620935 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/window_settings_response.cpython-38.pyc
+-rw-r--r--   0        0        0     3074 2023-04-07 09:57:01.627885 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/window_settings_response_all_of.cpython-38.pyc
+-rw-r--r--   0        0        0     3227 2023-04-07 09:57:01.623538 edgeimpulse_api-1.22.1/edgeimpulse_api/models/__pycache__/window_settings_response_all_of_window_settings.cpython-38.pyc
+-rw-r--r--   0        0        0     2892 2023-04-07 08:12:35.005021 edgeimpulse_api-1.22.1/edgeimpulse_api/models/activate_user_by_third_party_activation_code_request.py
+-rw-r--r--   0        0        0     1877 2023-04-07 08:12:35.007873 edgeimpulse_api-1.22.1/edgeimpulse_api/models/activate_user_request.py
+-rw-r--r--   0        0        0     2605 2023-04-07 08:12:34.422081 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_api_key_request.py
+-rw-r--r--   0        0        0     1958 2023-04-07 08:12:34.595190 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_collaborator_request.py
+-rw-r--r--   0        0        0     2218 2023-04-07 08:12:35.442302 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_hmac_key_request.py
+-rw-r--r--   0        0        0     2427 2023-04-07 08:12:35.387262 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_member_request.py
+-rw-r--r--   0        0        0     2413 2023-04-07 08:12:34.781415 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_api_key_request.py
+-rw-r--r--   0        0        0     2725 2023-04-07 08:12:35.035396 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_bucket_request.py
+-rw-r--r--   0        0        0     2264 2023-04-07 08:12:35.164661 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_deploy_block_response.py
+-rw-r--r--   0        0        0     2811 2023-04-07 08:12:34.984819 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_dsp_block_request.py
+-rw-r--r--   0        0        0     2243 2023-04-07 08:12:35.242902 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_dsp_block_response.py
+-rw-r--r--   0        0        0     2049 2023-04-07 08:12:34.999375 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_secret_request.py
+-rw-r--r--   0        0        0     2261 2023-04-07 08:12:35.260705 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_secret_response.py
+-rw-r--r--   0        0        0     1944 2023-04-07 08:12:34.921308 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_secret_response_all_of.py
+-rw-r--r--   0        0        0     3829 2023-04-07 08:12:34.667102 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_transfer_learning_block_request.py
+-rw-r--r--   0        0        0     2334 2023-04-07 08:12:35.205035 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_transfer_learning_block_response.py
+-rw-r--r--   0        0        0     4587 2023-04-07 08:12:34.457230 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_transformation_block_request.py
+-rw-r--r--   0        0        0     2320 2023-04-07 08:12:35.659496 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_transformation_block_response.py
+-rw-r--r--   0        0        0     1996 2023-04-07 08:12:34.719022 edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_transformation_block_response_all_of.py
+-rw-r--r--   0        0        0     1956 2023-04-07 08:12:35.438684 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_add_or_update_sso_domain_id_ps_request.py
+-rw-r--r--   0        0        0     1982 2023-04-07 08:12:35.591274 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_add_project_user_request.py
+-rw-r--r--   0        0        0     3871 2023-04-07 08:12:35.782086 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_api_organization.py
+-rw-r--r--   0        0        0     2391 2023-04-07 08:12:34.624708 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_api_organization_all_of.py
+-rw-r--r--   0        0        0     3454 2023-04-07 08:12:35.155151 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_api_project.py
+-rw-r--r--   0        0        0     6133 2023-04-07 08:12:34.717574 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_api_user.py
+-rw-r--r--   0        0        0     4948 2023-04-07 08:12:35.582350 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_api_user_all_of.py
+-rw-r--r--   0        0        0     2257 2023-04-07 08:12:35.246114 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_create_organization_request.py
+-rw-r--r--   0        0        0     2212 2023-04-07 08:12:35.417833 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_metrics_response.py
+-rw-r--r--   0        0        0     1905 2023-04-07 08:12:35.188672 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_metrics_response_all_of.py
+-rw-r--r--   0        0        0     3041 2023-04-07 08:12:35.084321 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_organizations_response.py
+-rw-r--r--   0        0        0     2741 2023-04-07 08:12:35.851750 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_organizations_response_all_of.py
+-rw-r--r--   0        0        0     2863 2023-04-07 08:12:35.126320 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_organizations_response_all_of_organizations.py
+-rw-r--r--   0        0        0     2238 2023-04-07 08:12:35.002163 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_sso_domain_id_ps_response.py
+-rw-r--r--   0        0        0     1942 2023-04-07 08:12:35.077622 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_sso_domain_id_ps_response_all_of.py
+-rw-r--r--   0        0        0     2909 2023-04-07 08:12:35.465207 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_sso_settings_response.py
+-rw-r--r--   0        0        0     2609 2023-04-07 08:12:35.301390 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_sso_settings_response_all_of.py
+-rw-r--r--   0        0        0     2091 2023-04-07 08:12:34.896214 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_sso_settings_response_all_of_sso_whitelist.py
+-rw-r--r--   0        0        0     2203 2023-04-07 08:12:35.561198 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_ids_response.py
+-rw-r--r--   0        0        0     1896 2023-04-07 08:12:35.448764 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_ids_response_all_of.py
+-rw-r--r--   0        0        0     2240 2023-04-07 08:12:35.735931 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_metrics_response.py
+-rw-r--r--   0        0        0     1933 2023-04-07 08:12:34.689061 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_metrics_response_all_of.py
+-rw-r--r--   0        0        0     2447 2023-04-07 08:12:34.449922 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_response.py
+-rw-r--r--   0        0        0     2123 2023-04-07 08:12:35.112846 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_response_all_of.py
+-rw-r--r--   0        0        0     2802 2023-04-07 08:12:34.826075 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_users_response.py
+-rw-r--r--   0        0        0     2495 2023-04-07 08:12:35.726476 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_users_response_all_of.py
+-rw-r--r--   0        0        0     3082 2023-04-07 08:12:35.131320 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_users_response_all_of_users.py
+-rw-r--r--   0        0        0     2440 2023-04-07 08:12:35.183013 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_list_projects.py
+-rw-r--r--   0        0        0     2831 2023-04-07 08:12:35.169798 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_list_projects_response.py
+-rw-r--r--   0        0        0     6067 2023-04-07 08:12:34.906945 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_organization_info_response.py
+-rw-r--r--   0        0        0     1969 2023-04-07 08:12:35.294252 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_organization_info_response_all_of.py
+-rw-r--r--   0        0        0     2723 2023-04-07 08:12:35.899018 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_update_organization_request.py
+-rw-r--r--   0        0        0     2125 2023-04-07 08:12:35.908012 edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_update_user_request.py
+-rw-r--r--   0        0        0     2520 2023-04-07 08:12:35.416103 edgeimpulse_api-1.22.1/edgeimpulse_api/models/akida_edge_learning_config.py
+-rw-r--r--   0        0        0     3625 2023-04-07 08:12:34.540550 edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_model_metadata.py
+-rw-r--r--   0        0        0     2146 2023-04-07 08:12:34.930061 edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_model_metadata_clusters_inner.py
+-rw-r--r--   0        0        0     4006 2023-04-07 08:12:35.701528 edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_model_metadata_response.py
+-rw-r--r--   0        0        0     4074 2023-04-07 08:12:34.627517 edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_response.py
+-rw-r--r--   0        0        0     3807 2023-04-07 08:12:35.288296 edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_response_all_of.py
+-rw-r--r--   0        0        0     2039 2023-04-07 08:12:34.792291 edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_response_all_of_axes.py
+-rw-r--r--   0        0        0     3024 2023-04-07 08:12:35.378173 edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_trained_features_response.py
+-rw-r--r--   0        0        0     2724 2023-04-07 08:12:35.450199 edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_trained_features_response_all_of.py
+-rw-r--r--   0        0        0     2370 2023-04-07 08:12:34.641763 edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_trained_features_response_all_of_data.py
+-rw-r--r--   0        0        0      506 2023-04-07 08:12:35.129224 edgeimpulse_api-1.22.1/edgeimpulse_api/models/augmentation_policy_image_enum.py
+-rw-r--r--   0        0        0     3630 2023-04-07 08:12:34.911316 edgeimpulse_api-1.22.1/edgeimpulse_api/models/augmentation_policy_spectrogram.py
+-rw-r--r--   0        0        0     1890 2023-04-07 08:12:34.536443 edgeimpulse_api-1.22.1/edgeimpulse_api/models/autotune_dsp_request.py
+-rw-r--r--   0        0        0     2039 2023-04-07 08:12:35.323080 edgeimpulse_api-1.22.1/edgeimpulse_api/models/bounding_box.py
+-rw-r--r--   0        0        0     2146 2023-04-07 08:12:34.552598 edgeimpulse_api-1.22.1/edgeimpulse_api/models/bounding_box_with_score.py
+-rw-r--r--   0        0        0     2192 2023-04-07 08:12:34.927385 edgeimpulse_api-1.22.1/edgeimpulse_api/models/build_on_device_model_request.py
+-rw-r--r--   0        0        0     2428 2023-04-07 08:12:34.582178 edgeimpulse_api-1.22.1/edgeimpulse_api/models/build_organization_on_device_model_request.py
+-rw-r--r--   0        0        0     2036 2023-04-07 08:12:34.809171 edgeimpulse_api-1.22.1/edgeimpulse_api/models/change_password_request.py
+-rw-r--r--   0        0        0     3696 2023-04-07 09:50:46.262786 edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_job_response.py
+-rw-r--r--   0        0        0     3389 2023-04-07 09:50:46.263162 edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_job_response_all_of.py
+-rw-r--r--   0        0        0     3764 2023-04-07 09:50:46.263457 edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_job_response_all_of_accuracy.py
+-rw-r--r--   0        0        0     2050 2023-04-07 09:50:46.263788 edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_job_response_all_of_accuracy_total_summary.py
+-rw-r--r--   0        0        0     3250 2023-04-07 09:50:46.264174 edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_job_response_page.py
+-rw-r--r--   0        0        0     2943 2023-04-07 09:50:46.264759 edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_job_response_page_all_of.py
+-rw-r--r--   0        0        0     3927 2023-04-07 08:12:34.559810 edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_sample_response.py
+-rw-r--r--   0        0        0     3639 2023-04-07 08:12:34.526254 edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_sample_response_all_of.py
+-rw-r--r--   0        0        0     4778 2023-04-07 08:12:34.852738 edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_sample_response_classification.py
+-rw-r--r--   0        0        0     2592 2023-04-07 08:12:34.548050 edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_sample_response_classification_details.py
+-rw-r--r--   0        0        0     2999 2023-04-07 08:12:35.198506 edgeimpulse_api-1.22.1/edgeimpulse_api/models/convert_user_request.py
+-rw-r--r--   0        0        0     2178 2023-04-07 08:12:35.383068 edgeimpulse_api-1.22.1/edgeimpulse_api/models/count_samples_response.py
+-rw-r--r--   0        0        0     1854 2023-04-07 08:12:34.471613 edgeimpulse_api-1.22.1/edgeimpulse_api/models/count_samples_response_all_of.py
+-rw-r--r--   0        0        0     2250 2023-04-07 08:12:35.276377 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_block_version_response.py
+-rw-r--r--   0        0        0     1933 2023-04-07 08:12:35.703647 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_block_version_response_all_of.py
+-rw-r--r--   0        0        0     2399 2023-04-07 08:12:34.868013 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_developer_profile_response.py
+-rw-r--r--   0        0        0     2120 2023-04-07 08:12:34.454057 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_developer_profile_response_all_of.py
+-rw-r--r--   0        0        0     2382 2023-04-07 08:12:35.239113 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_device_request.py
+-rw-r--r--   0        0        0     2486 2023-04-07 08:12:34.605483 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_evaluation_user_response.py
+-rw-r--r--   0        0        0     2180 2023-04-07 08:12:34.977667 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_evaluation_user_response_all_of.py
+-rw-r--r--   0        0        0     2595 2023-04-07 08:12:34.786666 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_portal_request.py
+-rw-r--r--   0        0        0     2825 2023-04-07 08:12:35.547711 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_portal_response.py
+-rw-r--r--   0        0        0     2546 2023-04-07 08:12:34.701491 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_portal_response_all_of.py
+-rw-r--r--   0        0        0     1985 2023-04-07 08:12:35.612371 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_request.py
+-rw-r--r--   0        0        0     2449 2023-04-07 08:12:35.581114 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_response.py
+-rw-r--r--   0        0        0     2143 2023-04-07 08:12:35.481879 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_response_all_of.py
+-rw-r--r--   0        0        0     2180 2023-04-07 08:12:34.909978 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_pipeline_response.py
+-rw-r--r--   0        0        0     2249 2023-04-07 08:12:34.416628 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_project_request.py
+-rw-r--r--   0        0        0     2373 2023-04-07 08:12:34.955334 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_project_response.py
+-rw-r--r--   0        0        0     2067 2023-04-07 08:12:35.633712 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_project_response_all_of.py
+-rw-r--r--   0        0        0     2271 2023-04-07 08:12:35.593711 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_signed_upload_link_request.py
+-rw-r--r--   0        0        0     2409 2023-04-07 08:12:35.506052 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_signed_upload_link_response.py
+-rw-r--r--   0        0        0     2130 2023-04-07 08:12:34.616683 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_signed_upload_link_response_all_of.py
+-rw-r--r--   0        0        0     2408 2023-04-07 08:12:35.751305 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_third_party_auth_request.py
+-rw-r--r--   0        0        0     2445 2023-04-07 08:12:34.628610 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_third_party_auth_response.py
+-rw-r--r--   0        0        0     2139 2023-04-07 08:12:34.480617 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_third_party_auth_response_all_of.py
+-rw-r--r--   0        0        0     3830 2023-04-07 08:12:34.923684 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_request.py
+-rw-r--r--   0        0        0     2388 2023-04-07 08:12:34.759746 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_response.py
+-rw-r--r--   0        0        0     2109 2023-04-07 08:12:34.816506 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_response_all_of.py
+-rw-r--r--   0        0        0     2914 2023-04-07 08:12:35.061745 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_third_party_request.py
+-rw-r--r--   0        0        0     2667 2023-04-07 08:12:35.666584 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_third_party_response.py
+-rw-r--r--   0        0        0     2388 2023-04-07 08:12:34.926243 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_third_party_response_all_of.py
+-rw-r--r--   0        0        0     4152 2023-04-07 08:12:34.452788 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_whitelabel_request.py
+-rw-r--r--   0        0        0     2433 2023-04-07 08:12:34.937469 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_whitelabel_response.py
+-rw-r--r--   0        0        0     2116 2023-04-07 08:12:34.551534 edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_whitelabel_response_all_of.py
+-rw-r--r--   0        0        0     2046 2023-04-07 08:12:35.775628 edgeimpulse_api-1.22.1/edgeimpulse_api/models/crop_sample_request.py
+-rw-r--r--   0        0        0     2243 2023-04-07 08:12:35.241495 edgeimpulse_api-1.22.1/edgeimpulse_api/models/crop_sample_response.py
+-rw-r--r--   0        0        0     1938 2023-04-07 08:12:34.900557 edgeimpulse_api-1.22.1/edgeimpulse_api/models/crop_sample_response_all_of.py
+-rw-r--r--   0        0        0     3287 2023-04-07 08:12:35.312197 edgeimpulse_api-1.22.1/edgeimpulse_api/models/data_explorer_predictions_response.py
+-rw-r--r--   0        0        0     2998 2023-04-07 08:12:34.577435 edgeimpulse_api-1.22.1/edgeimpulse_api/models/data_explorer_predictions_response_all_of.py
+-rw-r--r--   0        0        0     2833 2023-04-07 08:12:35.650273 edgeimpulse_api-1.22.1/edgeimpulse_api/models/data_explorer_settings.py
+-rw-r--r--   0        0        0     2144 2023-04-07 08:12:35.878123 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dataset_ratio_data.py
+-rw-r--r--   0        0        0     2106 2023-04-07 08:12:35.060276 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dataset_ratio_data_ratio.py
+-rw-r--r--   0        0        0     1893 2023-04-07 08:12:34.510053 edgeimpulse_api-1.22.1/edgeimpulse_api/models/delete_portal_file_request.py
+-rw-r--r--   0        0        0     2225 2023-04-07 08:12:34.805577 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dependency_data.py
+-rw-r--r--   0        0        0     2275 2023-04-07 08:12:35.068523 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_input_audio.py
+-rw-r--r--   0        0        0     2150 2023-04-07 08:12:34.959209 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_input_image.py
+-rw-r--r--   0        0        0     2150 2023-04-07 08:12:35.720049 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_input_other.py
+-rw-r--r--   0        0        0     2479 2023-04-07 08:12:35.467568 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_input_time_series.py
+-rw-r--r--   0        0        0     2339 2023-04-07 08:12:35.374079 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_model_classification.py
+-rw-r--r--   0        0        0     2775 2023-04-07 08:12:35.317092 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_model_object_detection.py
+-rw-r--r--   0        0        0     2195 2023-04-07 08:12:34.970453 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_model_regression.py
+-rw-r--r--   0        0        0     4334 2023-04-07 08:12:35.595421 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_request.py
+-rw-r--r--   0        0        0     2828 2023-04-07 08:12:34.881188 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_request_model_info.py
+-rw-r--r--   0        0        0     6911 2023-04-07 08:12:35.895608 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_request_model_info_input.py
+-rw-r--r--   0        0        0     6241 2023-04-07 08:12:35.686421 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_request_model_info_model.py
+-rw-r--r--   0        0        0     5406 2023-04-07 08:12:34.990679 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deployment_target.py
+-rw-r--r--   0        0        0     1921 2023-04-07 08:12:35.412138 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deployment_target_badge.py
+-rw-r--r--   0        0        0      657 2023-04-07 08:12:34.541855 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deployment_target_engine.py
+-rw-r--r--   0        0        0     2697 2023-04-07 08:12:35.355171 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deployment_targets_response.py
+-rw-r--r--   0        0        0     2390 2023-04-07 08:12:34.861716 edgeimpulse_api-1.22.1/edgeimpulse_api/models/deployment_targets_response_all_of.py
+-rw-r--r--   0        0        0     1978 2023-04-07 08:12:35.064510 edgeimpulse_api-1.22.1/edgeimpulse_api/models/development_board.py
+-rw-r--r--   0        0        0     2826 2023-04-07 08:12:34.965411 edgeimpulse_api-1.22.1/edgeimpulse_api/models/development_boards_response.py
+-rw-r--r--   0        0        0     2526 2023-04-07 08:12:34.588739 edgeimpulse_api-1.22.1/edgeimpulse_api/models/development_boards_response_all_of.py
+-rw-r--r--   0        0        0     2025 2023-04-07 08:12:35.888054 edgeimpulse_api-1.22.1/edgeimpulse_api/models/development_keys.py
+-rw-r--r--   0        0        0     2395 2023-04-07 08:12:35.620205 edgeimpulse_api-1.22.1/edgeimpulse_api/models/development_keys_response.py
+-rw-r--r--   0        0        0     3672 2023-04-07 08:12:34.812065 edgeimpulse_api-1.22.1/edgeimpulse_api/models/device.py
+-rw-r--r--   0        0        0     2194 2023-04-07 08:12:34.962960 edgeimpulse_api-1.22.1/edgeimpulse_api/models/device_name_response.py
+-rw-r--r--   0        0        0     1915 2023-04-07 08:12:35.100157 edgeimpulse_api-1.22.1/edgeimpulse_api/models/device_name_response_all_of.py
+-rw-r--r--   0        0        0     2226 2023-04-07 08:12:35.578769 edgeimpulse_api-1.22.1/edgeimpulse_api/models/device_sensors_inner.py
+-rw-r--r--   0        0        0     2089 2023-04-07 08:12:34.932770 edgeimpulse_api-1.22.1/edgeimpulse_api/models/download.py
+-rw-r--r--   0        0        0     1907 2023-04-07 08:12:34.869313 edgeimpulse_api-1.22.1/edgeimpulse_api/models/download_portal_file_request.py
+-rw-r--r--   0        0        0     2255 2023-04-07 08:12:35.410336 edgeimpulse_api-1.22.1/edgeimpulse_api/models/download_portal_file_response.py
+-rw-r--r--   0        0        0     1949 2023-04-07 08:12:35.689520 edgeimpulse_api-1.22.1/edgeimpulse_api/models/download_portal_file_response_all_of.py
+-rw-r--r--   0        0        0     2719 2023-04-07 08:12:35.500016 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_autotuner_results.py
+-rw-r--r--   0        0        0     2412 2023-04-07 08:12:35.121823 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_autotuner_results_all_of.py
+-rw-r--r--   0        0        0     1963 2023-04-07 08:12:35.199680 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_autotuner_results_all_of_results.py
+-rw-r--r--   0        0        0     2865 2023-04-07 08:12:34.543173 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_block.py
+-rw-r--r--   0        0        0     1829 2023-04-07 08:12:34.418010 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_config_request.py
+-rw-r--r--   0        0        0     3087 2023-04-07 08:12:35.349241 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_config_response.py
+-rw-r--r--   0        0        0     2808 2023-04-07 08:12:35.319453 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_config_response_all_of.py
+-rw-r--r--   0        0        0     3011 2023-04-07 08:12:34.849811 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_importance_response.py
+-rw-r--r--   0        0        0     2723 2023-04-07 08:12:34.651212 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_importance_response_all_of.py
+-rw-r--r--   0        0        0     2053 2023-04-07 08:12:34.549196 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_importance_response_all_of_features.py
+-rw-r--r--   0        0        0     2567 2023-04-07 08:12:35.522024 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_importance_response_all_of_labels.py
+-rw-r--r--   0        0        0     2211 2023-04-07 08:12:34.775279 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_labels_response.py
+-rw-r--r--   0        0        0     1915 2023-04-07 08:12:34.411679 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_labels_response_all_of.py
+-rw-r--r--   0        0        0     2289 2023-04-07 08:12:35.052384 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_group.py
+-rw-r--r--   0        0        0     3623 2023-04-07 08:12:35.313969 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_group_item.py
+-rw-r--r--   0        0        0     2185 2023-04-07 08:12:34.618148 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_group_item_select_options_inner.py
+-rw-r--r--   0        0        0     2190 2023-04-07 08:12:34.710501 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_group_item_show_if.py
+-rw-r--r--   0        0        0     4405 2023-04-07 08:12:35.599728 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_info.py
+-rw-r--r--   0        0        0     2205 2023-04-07 08:12:35.441072 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_info_features.py
+-rw-r--r--   0        0        0     1880 2023-04-07 08:12:34.964103 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_info_performance.py
+-rw-r--r--   0        0        0     5139 2023-04-07 08:12:35.434671 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_metadata.py
+-rw-r--r--   0        0        0     2020 2023-04-07 08:12:35.233559 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_metadata_included_samples_inner.py
+-rw-r--r--   0        0        0     2561 2023-04-07 08:12:35.880690 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_metadata_output_config.py
+-rw-r--r--   0        0        0     2526 2023-04-07 08:12:34.709046 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_metadata_output_config_shape.py
+-rw-r--r--   0        0        0     5497 2023-04-07 08:12:35.436163 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_metadata_response.py
+-rw-r--r--   0        0        0     3014 2023-04-07 08:12:35.192109 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_performance_all_variants_response.py
+-rw-r--r--   0        0        0     2724 2023-04-07 08:12:34.564306 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_performance_all_variants_response_all_of.py
+-rw-r--r--   0        0        0     2273 2023-04-07 08:12:35.360018 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_performance_all_variants_response_all_of_performance.py
+-rw-r--r--   0        0        0     4634 2023-04-07 08:12:35.892238 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_graph.py
+-rw-r--r--   0        0        0     1894 2023-04-07 08:12:34.801024 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_graph_axis_labels.py
+-rw-r--r--   0        0        0     2672 2023-04-07 09:50:46.265152 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_request_with_features.py
+-rw-r--r--   0        0        0     2146 2023-04-07 08:12:35.057593 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_request_without_features.py
+-rw-r--r--   0        0        0     2025 2023-04-07 08:12:34.687556 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_request_without_features_read_only.py
+-rw-r--r--   0        0        0     3508 2023-04-07 09:50:46.265557 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_response.py
+-rw-r--r--   0        0        0     3229 2023-04-07 09:50:46.266142 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_response_all_of.py
+-rw-r--r--   0        0        0     1964 2023-04-07 08:12:35.745660 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_response_all_of_performance.py
+-rw-r--r--   0        0        0     4137 2023-04-07 09:50:46.266745 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_response_with_sample.py
+-rw-r--r--   0        0        0     3870 2023-04-07 09:50:46.267575 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_response_with_sample_all_of.py
+-rw-r--r--   0        0        0     3337 2023-04-07 08:12:34.722011 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_sample_features_response.py
+-rw-r--r--   0        0        0     3037 2023-04-07 08:12:35.135564 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_sample_features_response_all_of.py
+-rw-r--r--   0        0        0     2743 2023-04-07 08:12:35.388815 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_sample_features_response_all_of_data.py
+-rw-r--r--   0        0        0     2208 2023-04-07 08:12:35.492176 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_sample_features_response_all_of_sample.py
+-rw-r--r--   0        0        0     3348 2023-04-07 08:12:34.639315 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_trained_features_response.py
+-rw-r--r--   0        0        0     3048 2023-04-07 08:12:34.886747 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_trained_features_response_all_of.py
+-rw-r--r--   0        0        0     2768 2023-04-07 08:12:35.146243 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_trained_features_response_all_of_data.py
+-rw-r--r--   0        0        0     2200 2023-04-07 08:12:34.610910 edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_trained_features_response_all_of_sample.py
+-rw-r--r--   0        0        0     1888 2023-04-07 08:12:35.631353 edgeimpulse_api-1.22.1/edgeimpulse_api/models/edit_sample_label_request.py
+-rw-r--r--   0        0        0     2651 2023-04-07 08:12:34.989142 edgeimpulse_api-1.22.1/edgeimpulse_api/models/evaluate_job_response.py
+-rw-r--r--   0        0        0     2344 2023-04-07 08:12:34.751884 edgeimpulse_api-1.22.1/edgeimpulse_api/models/evaluate_job_response_all_of.py
+-rw-r--r--   0        0        0     2094 2023-04-07 08:12:34.505859 edgeimpulse_api-1.22.1/edgeimpulse_api/models/evaluate_result_value.py
+-rw-r--r--   0        0        0     2506 2023-04-07 08:12:34.649711 edgeimpulse_api-1.22.1/edgeimpulse_api/models/export_get_url_response.py
+-rw-r--r--   0        0        0     2239 2023-04-07 08:12:34.462313 edgeimpulse_api-1.22.1/edgeimpulse_api/models/export_get_url_response_all_of.py
+-rw-r--r--   0        0        0     2368 2023-04-07 08:12:34.675301 edgeimpulse_api-1.22.1/edgeimpulse_api/models/export_original_data_request.py
+-rw-r--r--   0        0        0     2016 2023-04-07 08:12:35.257018 edgeimpulse_api-1.22.1/edgeimpulse_api/models/export_wav_data_request.py
+-rw-r--r--   0        0        0     2201 2023-04-07 08:12:35.363490 edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_segment_sample_request.py
+-rw-r--r--   0        0        0     2799 2023-04-07 08:12:35.814663 edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_segment_sample_response.py
+-rw-r--r--   0        0        0     2492 2023-04-07 08:12:35.147523 edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_segment_sample_response_all_of.py
+-rw-r--r--   0        0        0     2085 2023-04-07 08:12:35.163359 edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_segment_sample_response_all_of_segments.py
+-rw-r--r--   0        0        0     2660 2023-04-07 08:12:34.813387 edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_user_response.py
+-rw-r--r--   0        0        0     2353 2023-04-07 08:12:35.821956 edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_user_response_all_of.py
+-rw-r--r--   0        0        0     2317 2023-04-07 08:12:34.694129 edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_user_response_all_of_users.py
+-rw-r--r--   0        0        0     2502 2023-04-07 08:12:35.251676 edgeimpulse_api-1.22.1/edgeimpulse_api/models/generate_features_request.py
+-rw-r--r--   0        0        0     2078 2023-04-07 08:12:34.715206 edgeimpulse_api-1.22.1/edgeimpulse_api/models/generic_api_response.py
+-rw-r--r--   0        0        0     2693 2023-04-07 08:12:35.609901 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_all_third_party_auth_response.py
+-rw-r--r--   0        0        0     2386 2023-04-07 08:12:35.717182 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_all_third_party_auth_response_all_of.py
+-rw-r--r--   0        0        0     2708 2023-04-07 08:12:34.975375 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_all_whitelabels_response.py
+-rw-r--r--   0        0        0     2401 2023-04-07 08:12:34.470383 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_all_whitelabels_response_all_of.py
+-rw-r--r--   0        0        0     3395 2023-04-07 08:12:34.771787 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_data_explorer_features_response.py
+-rw-r--r--   0        0        0     3117 2023-04-07 08:12:35.063222 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_data_explorer_features_response_all_of.py
+-rw-r--r--   0        0        0     3747 2023-04-07 08:12:35.817727 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_data_explorer_settings_response.py
+-rw-r--r--   0        0        0     2397 2023-04-07 08:12:35.611057 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_data_explorer_settings_response_all_of.py
+-rw-r--r--   0        0        0     2344 2023-04-07 08:12:35.368019 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_deployment_response.py
+-rw-r--r--   0        0        0     2066 2023-04-07 08:12:35.748697 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_deployment_response_all_of.py
+-rw-r--r--   0        0        0     2429 2023-04-07 08:12:35.137870 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_device_response.py
+-rw-r--r--   0        0        0     2132 2023-04-07 08:12:35.579956 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_device_response_all_of.py
+-rw-r--r--   0        0        0     3925 2023-04-07 08:12:35.570279 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_impulse_blocks_response.py
+-rw-r--r--   0        0        0     3625 2023-04-07 08:12:34.630563 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_impulse_blocks_response_all_of.py
+-rw-r--r--   0        0        0     2449 2023-04-07 08:12:34.431331 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_impulse_response.py
+-rw-r--r--   0        0        0     2152 2023-04-07 08:12:35.471712 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_impulse_response_all_of.py
+-rw-r--r--   0        0        0     2369 2023-04-07 08:12:35.042865 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_job_response.py
+-rw-r--r--   0        0        0     2072 2023-04-07 08:12:35.507653 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_job_response_all_of.py
+-rw-r--r--   0        0        0     2680 2023-04-07 08:12:35.590089 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_jwt_token_request.py
+-rw-r--r--   0        0        0     2461 2023-04-07 08:12:34.888496 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_jwt_token_response.py
+-rw-r--r--   0        0        0     2182 2023-04-07 08:12:34.823254 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_jwt_token_response_all_of.py
+-rw-r--r--   0        0        0     2972 2023-04-07 08:12:34.525041 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_last_deployment_build_response.py
+-rw-r--r--   0        0        0     2694 2023-04-07 08:12:35.053648 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_last_deployment_build_response_all_of.py
+-rw-r--r--   0        0        0     2864 2023-04-07 08:12:35.617856 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_last_deployment_build_response_all_of_last_build.py
+-rw-r--r--   0        0        0     2567 2023-04-07 08:12:35.849310 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_notes_response.py
+-rw-r--r--   0        0        0     2260 2023-04-07 08:12:35.483731 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_notes_response_all_of.py
+-rw-r--r--   0        0        0     2556 2023-04-07 08:12:35.862450 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_data_item_response.py
+-rw-r--r--   0        0        0     2232 2023-04-07 08:12:35.648775 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_data_item_response_all_of.py
+-rw-r--r--   0        0        0     2571 2023-04-07 08:12:35.158205 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_dataset_response.py
+-rw-r--r--   0        0        0     2247 2023-04-07 08:12:35.193106 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_dataset_response_all_of.py
+-rw-r--r--   0        0        0     2598 2023-04-07 08:12:35.488328 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_pipelines_response.py
+-rw-r--r--   0        0        0     2274 2023-04-07 08:12:34.530195 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_pipelines_response_all_of.py
+-rw-r--r--   0        0        0     3665 2023-04-07 08:12:35.681752 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_portal_response.py
+-rw-r--r--   0        0        0     3386 2023-04-07 08:12:34.626337 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_portal_response_all_of.py
+-rw-r--r--   0        0        0     2318 2023-04-07 08:12:34.836228 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_projects_data_count_response.py
+-rw-r--r--   0        0        0     2900 2023-04-07 08:12:34.504758 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_ground_truth_response.py
+-rw-r--r--   0        0        0     2593 2023-04-07 08:12:35.030675 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_ground_truth_response_all_of.py
+-rw-r--r--   0        0        0     3007 2023-04-07 08:12:35.080750 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_parameter_sets_response.py
+-rw-r--r--   0        0        0     2707 2023-04-07 08:12:34.591683 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_parameter_sets_response_all_of.py
+-rw-r--r--   0        0        0     2717 2023-04-07 08:12:34.478064 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_parameters_response.py
+-rw-r--r--   0        0        0     2420 2023-04-07 08:12:35.662532 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_parameters_response_all_of.py
+-rw-r--r--   0        0        0     2917 2023-04-07 08:12:34.729961 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_raw_result_response.py
+-rw-r--r--   0        0        0     2610 2023-04-07 08:12:34.992166 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_raw_result_response_all_of.py
+-rw-r--r--   0        0        0     3146 2023-04-07 08:12:34.408609 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_status_response.py
+-rw-r--r--   0        0        0     2879 2023-04-07 08:12:35.032424 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_status_response_all_of.py
+-rw-r--r--   0        0        0     3756 2023-04-07 08:12:35.104823 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_pretrained_model_response.py
+-rw-r--r--   0        0        0     3478 2023-04-07 08:12:35.474058 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_pretrained_model_response_all_of.py
+-rw-r--r--   0        0        0     3856 2023-04-07 08:12:34.724932 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_pretrained_model_response_all_of_model.py
+-rw-r--r--   0        0        0     2973 2023-04-07 08:12:34.998190 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_pretrained_model_response_all_of_model_info.py
+-rw-r--r--   0        0        0     3053 2023-04-07 08:12:34.720495 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_pretrained_model_response_all_of_model_profile_info.py
+-rw-r--r--   0        0        0     2392 2023-04-07 08:12:34.768859 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_public_metrics_response.py
+-rw-r--r--   0        0        0     2068 2023-04-07 08:12:35.254937 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_public_metrics_response_all_of.py
+-rw-r--r--   0        0        0     2762 2023-04-07 08:12:35.134351 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_sample_metadata_response.py
+-rw-r--r--   0        0        0     3039 2023-04-07 08:12:35.868338 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_sample_response.py
+-rw-r--r--   0        0        0     2457 2023-04-07 08:12:35.559836 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_syntiant_posterior_response.py
+-rw-r--r--   0        0        0     2179 2023-04-07 08:12:35.509349 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_syntiant_posterior_response_all_of.py
+-rw-r--r--   0        0        0     2409 2023-04-07 08:12:34.980488 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_theme_response.py
+-rw-r--r--   0        0        0     2112 2023-04-07 08:12:34.935449 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_theme_response_all_of.py
+-rw-r--r--   0        0        0     2587 2023-04-07 08:12:34.884034 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_themes_response.py
+-rw-r--r--   0        0        0     2280 2023-04-07 08:12:35.679011 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_themes_response_all_of.py
+-rw-r--r--   0        0        0     2490 2023-04-07 08:12:35.273640 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_third_party_auth_response.py
+-rw-r--r--   0        0        0     2166 2023-04-07 08:12:34.593151 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_third_party_auth_response_all_of.py
+-rw-r--r--   0        0        0     2698 2023-04-07 08:12:35.269767 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_user_need_to_set_password_response.py
+-rw-r--r--   0        0        0     2431 2023-04-07 08:12:35.236464 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_user_need_to_set_password_response_all_of.py
+-rw-r--r--   0        0        0     7198 2023-04-07 08:12:34.726543 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_user_response.py
+-rw-r--r--   0        0        0     5558 2023-04-07 08:12:35.178842 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_user_response_all_of.py
+-rw-r--r--   0        0        0     2204 2023-04-07 08:12:35.597856 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_user_response_all_of_whitelabels.py
+-rw-r--r--   0        0        0     2302 2023-04-07 08:12:35.039649 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_whitelabel_domain_response.py
+-rw-r--r--   0        0        0     2016 2023-04-07 08:12:35.033795 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_whitelabel_domain_response_all_of.py
+-rw-r--r--   0        0        0     2509 2023-04-07 08:12:35.161202 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_whitelabel_response.py
+-rw-r--r--   0        0        0     2212 2023-04-07 08:12:35.292892 edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_whitelabel_response_all_of.py
+-rw-r--r--   0        0        0     2771 2023-04-07 08:12:34.795235 edgeimpulse_api-1.22.1/edgeimpulse_api/models/has_data_explorer_features_response.py
+-rw-r--r--   0        0        0     2493 2023-04-07 08:12:35.381804 edgeimpulse_api-1.22.1/edgeimpulse_api/models/has_data_explorer_features_response_all_of.py
+-rw-r--r--   0        0        0     3733 2023-04-07 08:12:34.678199 edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse.py
+-rw-r--r--   0        0        0     6718 2023-04-07 08:12:34.648062 edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse_block_version.py
+-rw-r--r--   0        0        0     6809 2023-04-07 08:12:35.413871 edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse_dsp_block.py
+-rw-r--r--   0        0        0     1962 2023-04-07 08:12:35.452897 edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse_dsp_block_organization.py
+-rw-r--r--   0        0        0     8971 2023-04-07 08:12:35.345511 edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse_input_block.py
+-rw-r--r--   0        0        0     5607 2023-04-07 08:12:35.139850 edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse_learn_block.py
+-rw-r--r--   0        0        0     2458 2023-04-07 08:12:35.830078 edgeimpulse_api-1.22.1/edgeimpulse_api/models/input_block.py
+-rw-r--r--   0        0        0     2451 2023-04-07 08:12:35.071777 edgeimpulse_api-1.22.1/edgeimpulse_api/models/invite_organization_member_request.py
+-rw-r--r--   0        0        0     3430 2023-04-07 08:12:34.894486 edgeimpulse_api-1.22.1/edgeimpulse_api/models/job.py
+-rw-r--r--   0        0        0     2708 2023-04-07 08:12:35.430508 edgeimpulse_api-1.22.1/edgeimpulse_api/models/job_summary_response.py
+-rw-r--r--   0        0        0     2401 2023-04-07 08:12:34.482443 edgeimpulse_api-1.22.1/edgeimpulse_api/models/job_summary_response_all_of.py
+-rw-r--r--   0        0        0     2084 2023-04-07 08:12:35.692583 edgeimpulse_api-1.22.1/edgeimpulse_api/models/job_summary_response_all_of_summary.py
+-rw-r--r--   0        0        0     2505 2023-04-07 08:12:35.759054 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_layer.py
+-rw-r--r--   0        0        0     2088 2023-04-07 08:12:35.788035 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_layer_input.py
+-rw-r--r--   0        0        0     2096 2023-04-07 08:12:35.495716 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_layer_output.py
+-rw-r--r--   0        0        0     5184 2023-04-07 08:12:35.353670 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_metadata.py
+-rw-r--r--   0        0        0     4917 2023-04-07 08:12:35.549200 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_metadata_all_of.py
+-rw-r--r--   0        0        0     4787 2023-04-07 08:12:35.067369 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_metadata_metrics.py
+-rw-r--r--   0        0        0     3223 2023-04-07 08:12:35.375602 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_metadata_metrics_on_device_performance_inner.py
+-rw-r--r--   0        0        0     2492 2023-04-07 08:12:35.325950 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_metadata_metrics_on_device_performance_inner_tflite.py
+-rw-r--r--   0        0        0      562 2023-04-07 08:12:35.455451 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_type_enum.py
+-rw-r--r--   0        0        0     9301 2023-04-07 08:12:34.419718 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_response.py
+-rw-r--r--   0        0        0     9034 2023-04-07 08:12:34.764142 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_response_all_of.py
+-rw-r--r--   0        0        0     3387 2023-04-07 08:12:35.458614 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_visual_layer.py
+-rw-r--r--   0        0        0     2310 2023-04-07 08:12:35.275125 edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_visual_layer_type.py
+-rw-r--r--   0        0        0     2524 2023-04-07 08:12:34.447898 edgeimpulse_api-1.22.1/edgeimpulse_api/models/last_modification_date_response.py
+-rw-r--r--   0        0        0     2234 2023-04-07 08:12:34.662016 edgeimpulse_api-1.22.1/edgeimpulse_api/models/last_modification_date_response_all_of.py
+-rw-r--r--   0        0        0     2628 2023-04-07 08:12:35.302751 edgeimpulse_api-1.22.1/edgeimpulse_api/models/latency_device.py
+-rw-r--r--   0        0        0     2419 2023-04-07 08:12:34.545781 edgeimpulse_api-1.22.1/edgeimpulse_api/models/learn_block.py
+-rw-r--r--   0        0        0      883 2023-04-07 08:12:35.558230 edgeimpulse_api-1.22.1/edgeimpulse_api/models/learn_block_type.py
+-rw-r--r--   0        0        0     2783 2023-04-07 08:12:35.439915 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_api_keys_response.py
+-rw-r--r--   0        0        0     2483 2023-04-07 08:12:34.579956 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_api_keys_response_all_of.py
+-rw-r--r--   0        0        0     2677 2023-04-07 08:12:35.554308 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_api_keys_response_all_of_api_keys.py
+-rw-r--r--   0        0        0     2625 2023-04-07 08:12:35.324507 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_devices_response.py
+-rw-r--r--   0        0        0     2328 2023-04-07 08:12:34.415352 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_devices_response_all_of.py
+-rw-r--r--   0        0        0     2721 2023-04-07 08:12:34.838036 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_email_response.py
+-rw-r--r--   0        0        0     2421 2023-04-07 08:12:35.048977 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_email_response_all_of.py
+-rw-r--r--   0        0        0     2913 2023-04-07 08:12:35.171307 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_email_response_all_of_emails.py
+-rw-r--r--   0        0        0     2808 2023-04-07 08:12:35.486668 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_hmac_keys_response.py
+-rw-r--r--   0        0        0     2508 2023-04-07 08:12:35.096719 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_hmac_keys_response_all_of.py
+-rw-r--r--   0        0        0     2376 2023-04-07 08:12:34.950043 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_hmac_keys_response_all_of_hmac_keys.py
+-rw-r--r--   0        0        0     2740 2023-04-07 08:12:34.437781 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_jobs_response.py
+-rw-r--r--   0        0        0     2440 2023-04-07 08:12:34.987987 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_jobs_response_all_of.py
+-rw-r--r--   0        0        0     2195 2023-04-07 08:12:35.187550 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_models_response.py
+-rw-r--r--   0        0        0     1905 2023-04-07 08:12:35.886684 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_models_response_all_of.py
+-rw-r--r--   0        0        0     2916 2023-04-07 08:12:35.657028 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_api_keys_response.py
+-rw-r--r--   0        0        0     2616 2023-04-07 08:12:34.673712 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_api_keys_response_all_of.py
+-rw-r--r--   0        0        0     2755 2023-04-07 08:12:34.790790 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_api_keys_response_all_of_api_keys.py
+-rw-r--r--   0        0        0     2852 2023-04-07 08:12:34.788952 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_response.py
+-rw-r--r--   0        0        0     2545 2023-04-07 08:12:35.823305 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_response_all_of.py
+-rw-r--r--   0        0        0     2914 2023-04-07 08:12:35.767928 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_response_all_of_buckets.py
+-rw-r--r--   0        0        0     2897 2023-04-07 08:12:35.290269 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_user_response.py
+-rw-r--r--   0        0        0     2590 2023-04-07 08:12:35.151313 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_user_response_all_of.py
+-rw-r--r--   0        0        0     3034 2023-04-07 08:12:34.755638 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_user_response_all_of_buckets.py
+-rw-r--r--   0        0        0     3305 2023-04-07 08:12:35.370222 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_data_response.py
+-rw-r--r--   0        0        0     3026 2023-04-07 08:12:34.615308 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_data_response_all_of.py
+-rw-r--r--   0        0        0     3425 2023-04-07 08:12:35.860208 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_data_response_all_of_data.py
+-rw-r--r--   0        0        0     2882 2023-04-07 08:12:35.667847 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_deploy_blocks_response.py
+-rw-r--r--   0        0        0     2582 2023-04-07 08:12:34.609548 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_deploy_blocks_response_all_of.py
+-rw-r--r--   0        0        0     2819 2023-04-07 08:12:34.903850 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_dsp_blocks_response.py
+-rw-r--r--   0        0        0     2519 2023-04-07 08:12:35.623242 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_dsp_blocks_response_all_of.py
+-rw-r--r--   0        0        0     3348 2023-04-07 08:12:34.833032 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_files_response.py
+-rw-r--r--   0        0        0     3069 2023-04-07 08:12:35.338522 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_files_response_all_of.py
+-rw-r--r--   0        0        0     2787 2023-04-07 08:12:34.828864 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_pipelines_response.py
+-rw-r--r--   0        0        0     2480 2023-04-07 08:12:34.574914 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_pipelines_response_all_of.py
+-rw-r--r--   0        0        0     2852 2023-04-07 08:12:35.165840 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_portals_response.py
+-rw-r--r--   0        0        0     2545 2023-04-07 08:12:35.352115 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_portals_response_all_of.py
+-rw-r--r--   0        0        0     2739 2023-04-07 08:12:35.635026 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_portals_response_all_of_portals.py
+-rw-r--r--   0        0        0     3444 2023-04-07 08:12:34.700511 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_projects_data_response.py
+-rw-r--r--   0        0        0     3137 2023-04-07 08:12:34.814715 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_projects_data_response_all_of.py
+-rw-r--r--   0        0        0     2266 2023-04-07 08:12:34.966687 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_projects_data_response_all_of_projects.py
+-rw-r--r--   0        0        0     2718 2023-04-07 08:12:35.159411 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_projects_response.py
+-rw-r--r--   0        0        0     2411 2023-04-07 08:12:34.945377 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_projects_response_all_of.py
+-rw-r--r--   0        0        0     2852 2023-04-07 08:12:34.511662 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_secrets_response.py
+-rw-r--r--   0        0        0     2545 2023-04-07 08:12:34.539228 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_secrets_response_all_of.py
+-rw-r--r--   0        0        0     2260 2023-04-07 08:12:35.613561 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_secrets_response_all_of_secrets.py
+-rw-r--r--   0        0        0     3098 2023-04-07 08:12:34.757447 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_transfer_learning_blocks_response.py
+-rw-r--r--   0        0        0     2798 2023-04-07 08:12:35.673891 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_transfer_learning_blocks_response_all_of.py
+-rw-r--r--   0        0        0     3050 2023-04-07 08:12:35.009174 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_transformation_blocks_response.py
+-rw-r--r--   0        0        0     2750 2023-04-07 08:12:35.237931 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_transformation_blocks_response_all_of.py
+-rw-r--r--   0        0        0     2781 2023-04-07 08:12:35.380490 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organizations_response.py
+-rw-r--r--   0        0        0     2481 2023-04-07 08:12:35.900200 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organizations_response_all_of.py
+-rw-r--r--   0        0        0     1932 2023-04-07 08:12:34.948902 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_portal_files_in_folder_request.py
+-rw-r--r--   0        0        0     2708 2023-04-07 08:12:35.451583 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_portal_files_in_folder_response.py
+-rw-r--r--   0        0        0     2411 2023-04-07 08:12:34.995368 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_portal_files_in_folder_response_all_of.py
+-rw-r--r--   0        0        0     2285 2023-04-07 08:12:35.264534 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_projects.py
+-rw-r--r--   0        0        0     2676 2023-04-07 08:12:35.897621 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_projects_response.py
+-rw-r--r--   0        0        0     2548 2023-04-07 08:12:35.079149 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_public_projects.py
+-rw-r--r--   0        0        0     2939 2023-04-07 08:12:34.692443 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_public_projects_response.py
+-rw-r--r--   0        0        0     2810 2023-04-07 08:12:35.315566 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_public_versions_response.py
+-rw-r--r--   0        0        0     2503 2023-04-07 08:12:35.259208 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_public_versions_response_all_of.py
+-rw-r--r--   0        0        0     2285 2023-04-07 08:12:35.708701 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_public_versions_response_all_of_versions.py
+-rw-r--r--   0        0        0     2749 2023-04-07 08:12:34.682528 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_samples_response.py
+-rw-r--r--   0        0        0     2449 2023-04-07 08:12:34.940381 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_samples_response_all_of.py
+-rw-r--r--   0        0        0     3928 2023-04-07 08:12:34.865603 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_versions_response.py
+-rw-r--r--   0        0        0     3628 2023-04-07 08:12:34.550446 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_versions_response_all_of.py
+-rw-r--r--   0        0        0     2348 2023-04-07 08:12:35.833355 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_versions_response_all_of_bucket.py
+-rw-r--r--   0        0        0     2048 2023-04-07 08:12:34.810520 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_versions_response_all_of_custom_learn_blocks.py
+-rw-r--r--   0        0        0     3955 2023-04-07 08:12:34.784323 edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_versions_response_all_of_versions.py
+-rw-r--r--   0        0        0     2895 2023-04-07 08:12:35.691269 edgeimpulse_api-1.22.1/edgeimpulse_api/models/log_stdout_response.py
+-rw-r--r--   0        0        0     2595 2023-04-07 08:12:35.761071 edgeimpulse_api-1.22.1/edgeimpulse_api/models/log_stdout_response_all_of.py
+-rw-r--r--   0        0        0     2436 2023-04-07 08:12:34.847644 edgeimpulse_api-1.22.1/edgeimpulse_api/models/log_stdout_response_all_of_stdout.py
+-rw-r--r--   0        0        0     2186 2023-04-07 08:12:34.982802 edgeimpulse_api-1.22.1/edgeimpulse_api/models/log_website_pageview_request.py
+-rw-r--r--   0        0        0     2212 2023-04-07 08:12:34.499673 edgeimpulse_api-1.22.1/edgeimpulse_api/models/login_response.py
+-rw-r--r--   0        0        0     1906 2023-04-07 08:12:35.419948 edgeimpulse_api-1.22.1/edgeimpulse_api/models/login_response_all_of.py
+-rw-r--r--   0        0        0     2516 2023-04-07 08:12:35.583672 edgeimpulse_api-1.22.1/edgeimpulse_api/models/model_prediction.py
+-rw-r--r--   0        0        0     2890 2023-04-07 09:50:46.268042 edgeimpulse_api-1.22.1/edgeimpulse_api/models/model_result.py
+-rw-r--r--   0        0        0     5041 2023-04-07 08:12:35.799931 edgeimpulse_api-1.22.1/edgeimpulse_api/models/model_variant_stats.py
+-rw-r--r--   0        0        0     2123 2023-04-07 08:12:35.248817 edgeimpulse_api-1.22.1/edgeimpulse_api/models/move_raw_data_request.py
+-rw-r--r--   0        0        0     2682 2023-04-07 08:12:35.771870 edgeimpulse_api-1.22.1/edgeimpulse_api/models/note.py
+-rw-r--r--   0        0        0     2216 2023-04-07 08:12:35.252960 edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_auto_label_request.py
+-rw-r--r--   0        0        0     2989 2023-04-07 08:12:35.197418 edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_auto_label_response.py
+-rw-r--r--   0        0        0     2700 2023-04-07 08:12:34.690507 edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_auto_label_response_all_of.py
+-rw-r--r--   0        0        0     2270 2023-04-07 08:12:35.820667 edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_auto_label_response_all_of_results.py
+-rw-r--r--   0        0        0     2363 2023-04-07 08:12:35.493617 edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_label_queue_count_response.py
+-rw-r--r--   0        0        0     2046 2023-04-07 08:12:34.839558 edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_label_queue_count_response_all_of.py
+-rw-r--r--   0        0        0     2882 2023-04-07 08:12:35.879380 edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_label_queue_response.py
+-rw-r--r--   0        0        0     2575 2023-04-07 08:12:35.585995 edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_label_queue_response_all_of.py
+-rw-r--r--   0        0        0      621 2023-04-07 08:12:35.655809 edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_last_layer.py
+-rw-r--r--   0        0        0     6413 2023-04-07 08:12:35.404584 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_config.py
+-rw-r--r--   0        0        0     6866 2023-04-07 08:12:35.875786 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_config_response.py
+-rw-r--r--   0        0        0     1915 2023-04-07 08:12:35.321749 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_config_response_all_of.py
+-rw-r--r--   0        0        0     2062 2023-04-07 08:12:35.318266 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_config_target_device.py
+-rw-r--r--   0        0        0     2266 2023-04-07 08:12:34.476616 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_dsp_parameters_response.py
+-rw-r--r--   0        0        0     1959 2023-04-07 08:12:35.743537 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_dsp_parameters_response_all_of.py
+-rw-r--r--   0        0        0     2751 2023-04-07 08:12:35.738466 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_space_response.py
+-rw-r--r--   0        0        0     2451 2023-04-07 08:12:34.428347 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_space_response_all_of.py
+-rw-r--r--   0        0        0     4892 2023-04-07 08:12:34.744217 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_state_response.py
+-rw-r--r--   0        0        0     4613 2023-04-07 08:12:34.993713 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_state_response_all_of.py
+-rw-r--r--   0        0        0     3414 2023-04-07 08:12:34.779920 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_state_response_all_of_status.py
+-rw-r--r--   0        0        0     2361 2023-04-07 08:12:35.630126 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_state_response_all_of_workers.py
+-rw-r--r--   0        0        0     2755 2023-04-07 08:12:35.468793 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_transfer_learning_models_response.py
+-rw-r--r--   0        0        0     2458 2023-04-07 08:12:35.856938 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_transfer_learning_models_response_all_of.py
+-rw-r--r--   0        0        0     4677 2023-04-07 08:12:35.044510 edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_transfer_learning_models_response_all_of_models.py
+-rw-r--r--   0        0        0     3769 2023-04-07 08:12:34.818875 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization.py
+-rw-r--r--   0        0        0     2354 2023-04-07 08:12:35.456738 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_add_data_folder_request.py
+-rw-r--r--   0        0        0     2493 2023-04-07 08:12:35.913674 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_add_data_folder_response.py
+-rw-r--r--   0        0        0     2204 2023-04-07 08:12:35.855618 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_add_data_folder_response_all_of.py
+-rw-r--r--   0        0        0     8195 2023-04-07 08:12:35.544273 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project.py
+-rw-r--r--   0        0        0     4773 2023-04-07 08:12:35.115780 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_request.py
+-rw-r--r--   0        0        0     2538 2023-04-07 08:12:34.613111 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_response.py
+-rw-r--r--   0        0        0     2232 2023-04-07 08:12:35.877112 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_response_all_of.py
+-rw-r--r--   0        0        0     2699 2023-04-07 08:12:35.915003 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_status_response.py
+-rw-r--r--   0        0        0     2402 2023-04-07 08:12:35.075134 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_status_response_all_of.py
+-rw-r--r--   0        0        0     2496 2023-04-07 08:12:34.782855 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_transformation_summary.py
+-rw-r--r--   0        0        0     8922 2023-04-07 08:12:35.173144 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_with_files.py
+-rw-r--r--   0        0        0     2553 2023-04-07 08:12:35.426022 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_with_files_all_of.py
+-rw-r--r--   0        0        0     2881 2023-04-07 08:12:35.866801 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_with_files_all_of_files.py
+-rw-r--r--   0        0        0     3471 2023-04-07 08:12:34.858978 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_data_item.py
+-rw-r--r--   0        0        0     2098 2023-04-07 08:12:34.834895 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_data_item_files_inner.py
+-rw-r--r--   0        0        0     2512 2023-04-07 08:12:35.546429 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_dataset.py
+-rw-r--r--   0        0        0     4684 2023-04-07 08:12:34.507560 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_deploy_block.py
+-rw-r--r--   0        0        0     3641 2023-04-07 08:12:35.399537 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_dsp_block.py
+-rw-r--r--   0        0        0     3032 2023-04-07 08:12:35.517491 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_get_create_projects_response.py
+-rw-r--r--   0        0        0     2732 2023-04-07 08:12:34.908623 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_get_create_projects_response_all_of.py
+-rw-r--r--   0        0        0     5304 2023-04-07 08:12:35.723083 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_get_create_projects_response_all_of_jobs.py
+-rw-r--r--   0        0        0     5933 2023-04-07 08:12:35.191041 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_info_response.py
+-rw-r--r--   0        0        0     5643 2023-04-07 08:12:35.282072 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_info_response_all_of.py
+-rw-r--r--   0        0        0     2453 2023-04-07 08:12:34.514942 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_info_response_all_of_default_compute_limits.py
+-rw-r--r--   0        0        0     2595 2023-04-07 08:12:35.356736 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_info_response_all_of_entitlement_limits.py
+-rw-r--r--   0        0        0     2634 2023-04-07 08:12:35.149127 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_metrics_response.py
+-rw-r--r--   0        0        0     2310 2023-04-07 08:12:34.636686 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_metrics_response_all_of.py
+-rw-r--r--   0        0        0     3486 2023-04-07 08:12:34.655024 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_metrics_response_all_of_metrics.py
+-rw-r--r--   0        0        0     6109 2023-04-07 08:12:35.470329 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline.py
+-rw-r--r--   0        0        0     2590 2023-04-07 08:12:35.261875 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_feeding_into_dataset.py
+-rw-r--r--   0        0        0     2270 2023-04-07 08:12:35.774078 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_feeding_into_project.py
+-rw-r--r--   0        0        0     2309 2023-04-07 08:12:34.956566 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_item_count.py
+-rw-r--r--   0        0        0     4104 2023-04-07 08:12:35.157014 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_run.py
+-rw-r--r--   0        0        0     4810 2023-04-07 08:12:34.824818 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_run_step.py
+-rw-r--r--   0        0        0     4410 2023-04-07 08:12:35.572887 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_step.py
+-rw-r--r--   0        0        0     2346 2023-04-07 08:12:34.797534 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_projects_data_batch_disable_response.py
+-rw-r--r--   0        0        0     2339 2023-04-07 08:12:35.724538 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_projects_data_batch_enable_response.py
+-rw-r--r--   0        0        0     2032 2023-04-07 08:12:35.230620 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_projects_data_batch_request.py
+-rw-r--r--   0        0        0     4409 2023-04-07 08:12:34.891012 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_transfer_learning_block.py
+-rw-r--r--   0        0        0      611 2023-04-07 08:12:35.601545 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_transfer_learning_operates_on.py
+-rw-r--r--   0        0        0     5163 2023-04-07 08:12:35.304376 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_transformation_block.py
+-rw-r--r--   0        0        0     3884 2023-04-07 08:12:34.414156 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_update_pipeline_body.py
+-rw-r--r--   0        0        0     3375 2023-04-07 08:12:35.780426 edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_user.py
+-rw-r--r--   0        0        0     2099 2023-04-07 08:12:34.495124 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_detection.py
+-rw-r--r--   0        0        0     3429 2023-04-07 08:12:35.069589 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_false_positive.py
+-rw-r--r--   0        0        0     3765 2023-04-07 08:12:35.056160 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_ground_truth.py
+-rw-r--r--   0        0        0     2472 2023-04-07 08:12:34.503282 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_ground_truth_samples_inner.py
+-rw-r--r--   0        0        0     4875 2023-04-07 08:12:34.479399 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_parameter_set.py
+-rw-r--r--   0        0        0     2250 2023-04-07 08:12:35.407203 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_parameter_set_aggregate_stats.py
+-rw-r--r--   0        0        0     4087 2023-04-07 08:12:34.612033 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_parameter_set_stats_inner.py
+-rw-r--r--   0        0        0     3002 2023-04-07 08:12:35.882485 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_parameters.py
+-rw-r--r--   0        0        0     2580 2023-04-07 08:12:34.960513 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_parameters_standard.py
+-rw-r--r--   0        0        0     2245 2023-04-07 08:12:35.186322 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_raw_detection.py
+-rw-r--r--   0        0        0     2361 2023-04-07 08:12:35.565727 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_save_parameter_set_request.py
+-rw-r--r--   0        0        0     2407 2023-04-07 08:12:35.432803 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_upload_labeled_audio_response.py
+-rw-r--r--   0        0        0     2101 2023-04-07 08:12:34.704309 edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_upload_labeled_audio_response_all_of.py
+-rw-r--r--   0        0        0     2206 2023-04-07 08:12:35.540061 edgeimpulse_api-1.22.1/edgeimpulse_api/models/portal_file.py
+-rw-r--r--   0        0        0     2408 2023-04-07 08:12:34.860287 edgeimpulse_api-1.22.1/edgeimpulse_api/models/portal_info_response.py
+-rw-r--r--   0        0        0     2661 2023-04-07 08:12:35.144933 edgeimpulse_api-1.22.1/edgeimpulse_api/models/pretrained_model_tensor.py
+-rw-r--r--   0        0        0     2950 2023-04-07 08:12:35.385885 edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_info.py
+-rw-r--r--   0        0        0     2635 2023-04-07 08:12:35.073819 edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_info_memory.py
+-rw-r--r--   0        0        0     1913 2023-04-07 08:12:35.320592 edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_info_memory_eon.py
+-rw-r--r--   0        0        0     2060 2023-04-07 08:12:35.066068 edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_info_memory_tflite.py
+-rw-r--r--   0        0        0     4330 2023-04-07 08:12:35.637932 edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_table.py
+-rw-r--r--   0        0        0     2775 2023-04-07 08:12:34.954037 edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_table_mcu.py
+-rw-r--r--   0        0        0     2560 2023-04-07 08:12:35.142851 edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_table_mcu_memory.py
+-rw-r--r--   0        0        0     2245 2023-04-07 08:12:35.006514 edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_table_mpu.py
+-rw-r--r--   0        0        0     2196 2023-04-07 08:12:35.604325 edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_tf_lite_request.py
+-rw-r--r--   0        0        0     3287 2023-04-07 08:12:35.291632 edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_tf_lite_response.py
+-rw-r--r--   0        0        0     6134 2023-04-07 08:12:35.847708 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project.py
+-rw-r--r--   0        0        0     3266 2023-04-07 08:12:34.899031 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_collaborator.py
+-rw-r--r--   0        0        0     1890 2023-04-07 08:12:35.437469 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_collaborator_all_of.py
+-rw-r--r--   0        0        0     2411 2023-04-07 08:12:35.660762 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_data_axes_summary_response.py
+-rw-r--r--   0        0        0     2111 2023-04-07 08:12:34.493441 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_data_axes_summary_response_all_of.py
+-rw-r--r--   0        0        0     2276 2023-04-07 08:12:35.076413 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_data_interval_response.py
+-rw-r--r--   0        0        0     1959 2023-04-07 08:12:34.773391 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_data_interval_response_all_of.py
+-rw-r--r--   0        0        0     2230 2023-04-07 08:12:34.566396 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_data_summary.py
+-rw-r--r--   0        0        0     6310 2023-04-07 08:12:35.588665 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_deployment_target.py
+-rw-r--r--   0        0        0     2701 2023-04-07 08:12:35.785262 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_deployment_target_all_of.py
+-rw-r--r--   0        0        0     2775 2023-04-07 08:12:35.213366 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_deployment_targets_response.py
+-rw-r--r--   0        0        0     2468 2023-04-07 08:12:34.522733 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_deployment_targets_response_all_of.py
+-rw-r--r--   0        0        0     2675 2023-04-07 08:12:34.544458 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_downloads_response.py
+-rw-r--r--   0        0        0     2368 2023-04-07 08:12:35.054915 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_downloads_response_all_of.py
+-rw-r--r--   0        0        0    13741 2023-04-07 08:12:35.853194 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response.py
+-rw-r--r--   0        0        0    13474 2023-04-07 08:12:35.871260 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of.py
+-rw-r--r--   0        0        0     3125 2023-04-07 08:12:34.424519 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_acquisition_settings.py
+-rw-r--r--   0        0        0     2718 2023-04-07 08:12:35.778635 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_compute_time.py
+-rw-r--r--   0        0        0     2992 2023-04-07 08:12:35.206588 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_data_summary_per_category.py
+-rw-r--r--   0        0        0     2803 2023-04-07 08:12:34.753825 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_deploy_settings.py
+-rw-r--r--   0        0        0     2334 2023-04-07 08:12:35.632529 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_experiments.py
+-rw-r--r--   0        0        0     2280 2023-04-07 08:12:35.695124 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_impulse.py
+-rw-r--r--   0        0        0     2721 2023-04-07 08:12:35.203902 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_performance.py
+-rw-r--r--   0        0        0     1972 2023-04-07 08:12:35.765995 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_readme.py
+-rw-r--r--   0        0        0     2220 2023-04-07 08:12:35.379300 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_show_getting_started_wizard.py
+-rw-r--r--   0        0        0     2730 2023-04-07 08:12:34.728404 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_urls.py
+-rw-r--r--   0        0        0     2473 2023-04-07 08:12:34.643457 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_summary_response.py
+-rw-r--r--   0        0        0     2167 2023-04-07 08:12:34.857297 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_summary_response_all_of.py
+-rw-r--r--   0        0        0     3549 2023-04-07 08:12:34.501919 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_private_data.py
+-rw-r--r--   0        0        0     4391 2023-04-07 08:12:34.496694 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_public_data.py
+-rw-r--r--   0        0        0     1923 2023-04-07 08:12:35.195180 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_public_data_readme.py
+-rw-r--r--   0        0        0     2399 2023-04-07 08:12:35.769946 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_sample_metadata.py
+-rw-r--r--   0        0        0     2311 2023-04-07 08:12:34.961838 edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_version_request.py
+-rw-r--r--   0        0        0     2659 2023-04-07 08:12:34.644746 edgeimpulse_api-1.22.1/edgeimpulse_api/models/raw_sample_data.py
+-rw-r--r--   0        0        0     3435 2023-04-07 08:12:35.840876 edgeimpulse_api-1.22.1/edgeimpulse_api/models/raw_sample_payload.py
+-rw-r--r--   0        0        0     2532 2023-04-07 08:12:35.889781 edgeimpulse_api-1.22.1/edgeimpulse_api/models/rebalance_dataset_response.py
+-rw-r--r--   0        0        0     1979 2023-04-07 08:12:35.109838 edgeimpulse_api-1.22.1/edgeimpulse_api/models/remove_collaborator_request.py
+-rw-r--r--   0        0        0     1800 2023-04-07 08:12:35.408460 edgeimpulse_api-1.22.1/edgeimpulse_api/models/remove_member_request.py
+-rw-r--r--   0        0        0     1862 2023-04-07 08:12:35.020414 edgeimpulse_api-1.22.1/edgeimpulse_api/models/rename_device_request.py
+-rw-r--r--   0        0        0     2076 2023-04-07 08:12:34.934162 edgeimpulse_api-1.22.1/edgeimpulse_api/models/rename_portal_file_request.py
+-rw-r--r--   0        0        0     1862 2023-04-07 08:12:35.827326 edgeimpulse_api-1.22.1/edgeimpulse_api/models/rename_sample_request.py
+-rw-r--r--   0        0        0     1868 2023-04-07 08:12:34.546969 edgeimpulse_api-1.22.1/edgeimpulse_api/models/request_reset_password_request.py
+-rw-r--r--   0        0        0     2026 2023-04-07 08:12:35.850517 edgeimpulse_api-1.22.1/edgeimpulse_api/models/reset_password_request.py
+-rw-r--r--   0        0        0     1980 2023-04-07 08:12:35.189825 edgeimpulse_api-1.22.1/edgeimpulse_api/models/restore_project_from_public_request.py
+-rw-r--r--   0        0        0     2260 2023-04-07 08:12:35.757269 edgeimpulse_api-1.22.1/edgeimpulse_api/models/restore_project_request.py
+-rw-r--r--   0        0        0     2664 2023-04-07 08:12:35.813353 edgeimpulse_api-1.22.1/edgeimpulse_api/models/run_organization_pipeline_response.py
+-rw-r--r--   0        0        0     2347 2023-04-07 08:12:34.519333 edgeimpulse_api-1.22.1/edgeimpulse_api/models/run_organization_pipeline_response_all_of.py
+-rw-r--r--   0        0        0     9632 2023-04-07 08:12:35.462441 edgeimpulse_api-1.22.1/edgeimpulse_api/models/sample.py
+-rw-r--r--   0        0        0     2438 2023-04-07 08:12:34.670972 edgeimpulse_api-1.22.1/edgeimpulse_api/models/sample_bounding_boxes_request.py
+-rw-r--r--   0        0        0     1995 2023-04-07 08:12:34.600021 edgeimpulse_api-1.22.1/edgeimpulse_api/models/sample_metadata.py
+-rw-r--r--   0        0        0     2751 2023-04-07 08:12:34.623612 edgeimpulse_api-1.22.1/edgeimpulse_api/models/save_pretrained_model_request.py
+-rw-r--r--   0        0        0     3322 2023-04-07 08:12:35.059010 edgeimpulse_api-1.22.1/edgeimpulse_api/models/score_trial_response.py
+-rw-r--r--   0        0        0     2998 2023-04-07 08:12:35.911162 edgeimpulse_api-1.22.1/edgeimpulse_api/models/score_trial_response_all_of.py
+-rw-r--r--   0        0        0     2235 2023-04-07 08:12:35.003621 edgeimpulse_api-1.22.1/edgeimpulse_api/models/score_trial_response_all_of_latency.py
+-rw-r--r--   0        0        0     1909 2023-04-07 08:12:35.705782 edgeimpulse_api-1.22.1/edgeimpulse_api/models/score_trial_response_all_of_ram.py
+-rw-r--r--   0        0        0     2400 2023-04-07 08:12:34.793716 edgeimpulse_api-1.22.1/edgeimpulse_api/models/segment_sample_request.py
+-rw-r--r--   0        0        0     2050 2023-04-07 08:12:35.865327 edgeimpulse_api-1.22.1/edgeimpulse_api/models/segment_sample_request_segments_inner.py
+-rw-r--r--   0        0        0     3359 2023-04-07 08:12:35.329139 edgeimpulse_api-1.22.1/edgeimpulse_api/models/send_user_feedback_request.py
+-rw-r--r--   0        0        0     1976 2023-04-07 08:12:34.614208 edgeimpulse_api-1.22.1/edgeimpulse_api/models/sensor.py
+-rw-r--r--   0        0        0     2137 2023-04-07 08:12:35.658329 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_anomaly_parameter_request.py
+-rw-r--r--   0        0        0     7420 2023-04-07 08:12:34.677071 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_keras_parameter_request.py
+-rw-r--r--   0        0        0     1888 2023-04-07 08:12:35.828558 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_member_datasets_request.py
+-rw-r--r--   0        0        0     2044 2023-04-07 08:12:35.575136 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_member_role_request.py
+-rw-r--r--   0        0        0     2214 2023-04-07 08:12:35.652289 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_optimize_space_request.py
+-rw-r--r--   0        0        0     2249 2023-04-07 08:12:35.665129 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_optimize_space_request_all_of.py
+-rw-r--r--   0        0        0     1918 2023-04-07 08:12:35.902419 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_organization_data_dataset_request.py
+-rw-r--r--   0        0        0     1969 2023-04-07 08:12:34.947556 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_project_compute_time_request.py
+-rw-r--r--   0        0        0     2006 2023-04-07 08:12:35.202660 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_project_dsp_file_size_request.py
+-rw-r--r--   0        0        0     1914 2023-04-07 08:12:34.699017 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_sample_metadata_request.py
+-rw-r--r--   0        0        0     1910 2023-04-07 08:12:35.176034 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_syntiant_posterior_request.py
+-rw-r--r--   0        0        0     2135 2023-04-07 08:12:35.000700 edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_user_password_request.py
+-rw-r--r--   0        0        0     2531 2023-04-07 08:12:34.723703 edgeimpulse_api-1.22.1/edgeimpulse_api/models/socket_token_response.py
+-rw-r--r--   0        0        0     2234 2023-04-07 08:12:35.571430 edgeimpulse_api-1.22.1/edgeimpulse_api/models/socket_token_response_all_of.py
+-rw-r--r--   0        0        0     2054 2023-04-07 08:12:34.441146 edgeimpulse_api-1.22.1/edgeimpulse_api/models/socket_token_response_all_of_token.py
+-rw-r--r--   0        0        0     1966 2023-04-07 08:12:34.777704 edgeimpulse_api-1.22.1/edgeimpulse_api/models/split_sample_in_frames_request.py
+-rw-r--r--   0        0        0     2105 2023-04-07 08:12:34.669017 edgeimpulse_api-1.22.1/edgeimpulse_api/models/staff_info.py
+-rw-r--r--   0        0        0     2221 2023-04-07 08:12:35.299963 edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_job_response.py
+-rw-r--r--   0        0        0     1904 2023-04-07 08:12:34.472802 edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_job_response_all_of.py
+-rw-r--r--   0        0        0     2878 2023-04-07 08:12:35.070681 edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_performance_calibration_request.py
+-rw-r--r--   0        0        0     2833 2023-04-07 08:12:35.490821 edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_sampling_request.py
+-rw-r--r--   0        0        0     2184 2023-04-07 08:12:35.444310 edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_sampling_response.py
+-rw-r--r--   0        0        0     1887 2023-04-07 08:12:35.196256 edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_sampling_response_all_of.py
+-rw-r--r--   0        0        0     2487 2023-04-07 08:12:35.194114 edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_training_request_anomaly.py
+-rw-r--r--   0        0        0     1962 2023-04-07 08:12:34.533890 edgeimpulse_api-1.22.1/edgeimpulse_api/models/store_segment_length_request.py
+-rw-r--r--   0        0        0     2639 2023-04-07 08:12:35.654858 edgeimpulse_api-1.22.1/edgeimpulse_api/models/structured_classify_result.py
+-rw-r--r--   0        0        0     2428 2023-04-07 08:12:34.427186 edgeimpulse_api-1.22.1/edgeimpulse_api/models/test_pretrained_model_request.py
+-rw-r--r--   0        0        0     3069 2023-04-07 08:12:35.697858 edgeimpulse_api-1.22.1/edgeimpulse_api/models/test_pretrained_model_response.py
+-rw-r--r--   0        0        0     2779 2023-04-07 08:12:35.396378 edgeimpulse_api-1.22.1/edgeimpulse_api/models/test_pretrained_model_response_all_of.py
+-rw-r--r--   0        0        0     3246 2023-04-07 08:12:34.711739 edgeimpulse_api-1.22.1/edgeimpulse_api/models/theme.py
+-rw-r--r--   0        0        0     2234 2023-04-07 08:12:35.136770 edgeimpulse_api-1.22.1/edgeimpulse_api/models/theme_colors.py
+-rw-r--r--   0        0        0     2759 2023-04-07 08:12:34.951363 edgeimpulse_api-1.22.1/edgeimpulse_api/models/theme_favicon.py
+-rw-r--r--   0        0        0     2581 2023-04-07 08:12:35.011147 edgeimpulse_api-1.22.1/edgeimpulse_api/models/theme_logos.py
+-rw-r--r--   0        0        0     2240 2023-04-07 08:12:34.925082 edgeimpulse_api-1.22.1/edgeimpulse_api/models/third_party_auth.py
+-rw-r--r--   0        0        0     2026 2023-04-07 08:12:34.928714 edgeimpulse_api-1.22.1/edgeimpulse_api/models/track_objects_request.py
+-rw-r--r--   0        0        0     2731 2023-04-07 08:12:35.306422 edgeimpulse_api-1.22.1/edgeimpulse_api/models/track_objects_response.py
+-rw-r--r--   0        0        0     2431 2023-04-07 08:12:34.863190 edgeimpulse_api-1.22.1/edgeimpulse_api/models/track_objects_response_all_of.py
+-rw-r--r--   0        0        0     4605 2023-04-07 08:12:34.821530 edgeimpulse_api-1.22.1/edgeimpulse_api/models/transfer_learning_model.py
+-rw-r--r--   0        0        0     2007 2023-04-07 08:12:34.646189 edgeimpulse_api-1.22.1/edgeimpulse_api/models/transfer_ownership_organization_request.py
+-rw-r--r--   0        0        0     2580 2023-04-07 08:12:35.608085 edgeimpulse_api-1.22.1/edgeimpulse_api/models/transformation_block_additional_mount_point.py
+-rw-r--r--   0        0        0      588 2023-04-07 08:12:35.615296 edgeimpulse_api-1.22.1/edgeimpulse_api/models/transformation_job_status_enum.py
+-rw-r--r--   0        0        0     2573 2023-04-07 08:12:35.364670 edgeimpulse_api-1.22.1/edgeimpulse_api/models/tuner_create_trial_impulse.py
+-rw-r--r--   0        0        0     2565 2023-04-07 08:12:34.474487 edgeimpulse_api-1.22.1/edgeimpulse_api/models/tuner_space_impulse.py
+-rw-r--r--   0        0        0     3656 2023-04-07 08:12:35.777010 edgeimpulse_api-1.22.1/edgeimpulse_api/models/tuner_trial.py
+-rw-r--r--   0        0        0     2299 2023-04-07 08:12:34.952816 edgeimpulse_api-1.22.1/edgeimpulse_api/models/tuner_trial_blocks_inner.py
+-rw-r--r--   0        0        0     2023 2023-04-07 08:12:34.827240 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_job_request.py
+-rw-r--r--   0        0        0     2276 2023-04-07 08:12:34.875074 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_add_collaborator_request.py
+-rw-r--r--   0        0        0     2812 2023-04-07 08:12:35.366275 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_bucket_request.py
+-rw-r--r--   0        0        0     2573 2023-04-07 08:12:35.731096 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_create_empty_project_request.py
+-rw-r--r--   0        0        0     2423 2023-04-07 08:12:34.425806 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_create_project_request.py
+-rw-r--r--   0        0        0     2153 2023-04-07 08:12:35.669032 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_data_item_request.py
+-rw-r--r--   0        0        0     2047 2023-04-07 08:12:35.825729 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_dataset_request.py
+-rw-r--r--   0        0        0     2876 2023-04-07 08:12:35.854466 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_dsp_block_request.py
+-rw-r--r--   0        0        0     2719 2023-04-07 08:12:34.931381 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_portal_response.py
+-rw-r--r--   0        0        0     2440 2023-04-07 08:12:35.393672 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_portal_response_all_of.py
+-rw-r--r--   0        0        0     2577 2023-04-07 08:12:35.489672 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_request.py
+-rw-r--r--   0        0        0     3905 2023-04-07 08:12:35.628831 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_transfer_learning_block_request.py
+-rw-r--r--   0        0        0     4729 2023-04-07 08:12:35.670353 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_transformation_block_request.py
+-rw-r--r--   0        0        0     7721 2023-04-07 08:12:35.298372 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_project_request.py
+-rw-r--r--   0        0        0     1872 2023-04-07 08:12:34.996863 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_project_tags_request.py
+-rw-r--r--   0        0        0     2254 2023-04-07 08:12:34.749842 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_theme_colors_request.py
+-rw-r--r--   0        0        0     2724 2023-04-07 08:12:34.739014 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_theme_logos_request.py
+-rw-r--r--   0        0        0     2200 2023-04-07 08:12:35.446520 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_third_party_auth_request.py
+-rw-r--r--   0        0        0     2272 2023-04-07 08:12:34.679601 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_user_request.py
+-rw-r--r--   0        0        0     1881 2023-04-07 08:12:35.050428 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_version_request.py
+-rw-r--r--   0        0        0     2120 2023-04-07 08:12:35.796508 edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_whitelabel_deployment_targets_request.py
+-rw-r--r--   0        0        0     2163 2023-04-07 08:12:35.265898 edgeimpulse_api-1.22.1/edgeimpulse_api/models/upload_asset_response.py
+-rw-r--r--   0        0        0     1877 2023-04-07 08:12:34.916360 edgeimpulse_api-1.22.1/edgeimpulse_api/models/upload_asset_response_all_of.py
+-rw-r--r--   0        0        0     2194 2023-04-07 08:12:34.464141 edgeimpulse_api-1.22.1/edgeimpulse_api/models/upload_readme_image_response.py
+-rw-r--r--   0        0        0     2180 2023-04-07 08:12:35.341508 edgeimpulse_api-1.22.1/edgeimpulse_api/models/upload_user_photo_response.py
+-rw-r--r--   0        0        0     1867 2023-04-07 08:12:35.377009 edgeimpulse_api-1.22.1/edgeimpulse_api/models/upload_user_photo_response_all_of.py
+-rw-r--r--   0        0        0     3051 2023-04-07 08:12:34.535164 edgeimpulse_api-1.22.1/edgeimpulse_api/models/user.py
+-rw-r--r--   0        0        0     1986 2023-04-07 08:12:34.841524 edgeimpulse_api-1.22.1/edgeimpulse_api/models/user_by_third_party_activation_request.py
+-rw-r--r--   0        0        0     2187 2023-04-07 08:12:35.805990 edgeimpulse_api-1.22.1/edgeimpulse_api/models/user_experiment.py
+-rw-r--r--   0        0        0     2704 2023-04-07 08:12:35.047592 edgeimpulse_api-1.22.1/edgeimpulse_api/models/user_organization.py
+-rw-r--r--   0        0        0     1839 2023-04-07 08:12:35.384371 edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_dsp_block_url_request.py
+-rw-r--r--   0        0        0     2599 2023-04-07 08:12:35.693728 edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_dsp_block_url_response.py
+-rw-r--r--   0        0        0     2302 2023-04-07 08:12:35.476410 edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_dsp_block_url_response_all_of.py
+-rw-r--r--   0        0        0     2402 2023-04-07 08:12:35.644888 edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_dsp_block_url_response_all_of_block.py
+-rw-r--r--   0        0        0     2703 2023-04-07 08:12:34.957922 edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_organization_bucket_request.py
+-rw-r--r--   0        0        0     2892 2023-04-07 08:12:35.454165 edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_organization_bucket_response.py
+-rw-r--r--   0        0        0     2592 2023-04-07 08:12:35.809991 edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_organization_bucket_response_all_of.py
+-rw-r--r--   0        0        0     2182 2023-04-07 08:12:34.410151 edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_organization_bucket_response_all_of_files.py
+-rw-r--r--   0        0        0     1932 2023-04-07 08:12:35.592471 edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_reset_password_request.py
+-rw-r--r--   0        0        0     3213 2023-04-07 08:12:35.347049 edgeimpulse_api-1.22.1/edgeimpulse_api/models/whitelabel.py
+-rw-r--r--   0        0        0     2529 2023-04-07 08:12:34.423330 edgeimpulse_api-1.22.1/edgeimpulse_api/models/whitelabel_admin_create_organization_request.py
+-rw-r--r--   0        0        0     2880 2023-04-07 08:12:35.783304 edgeimpulse_api-1.22.1/edgeimpulse_api/models/window_settings_response.py
+-rw-r--r--   0        0        0     2580 2023-04-07 08:12:34.451511 edgeimpulse_api-1.22.1/edgeimpulse_api/models/window_settings_response_all_of.py
+-rw-r--r--   0        0        0     2843 2023-04-07 08:12:34.508948 edgeimpulse_api-1.22.1/edgeimpulse_api/models/window_settings_response_all_of_window_settings.py
+-rw-r--r--   0        0        0    12674 2023-04-07 08:12:18.488216 edgeimpulse_api-1.22.1/edgeimpulse_api/rest.py
+-rw-r--r--   0        0        0      975 2023-04-07 09:56:15.020185 edgeimpulse_api-1.22.1/pyproject.toml
+-rw-r--r--   0        0        0     1413 1970-01-01 00:00:00.000000 edgeimpulse_api-1.22.1/PKG-INFO
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/__init__.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -10,15 +10,15 @@
     The version of the OpenAPI document: 1.0.0
     Generated by: https://openapi-generator.tech
 """
 
 
 from __future__ import absolute_import
 
-__version__ = "1.22.0" #DO_NOT_CHANGE_REPLACED_BY_BUILD_SCRIPT
+__version__ = "1.22.1" #DO_NOT_CHANGE_REPLACED_BY_BUILD_SCRIPT
 
 # import apis into sdk package
 from edgeimpulse_api.api.admin_api import AdminApi
 from edgeimpulse_api.api.allows_read_only_api import AllowsReadOnlyApi
 from edgeimpulse_api.api.auth_api import AuthApi
 from edgeimpulse_api.api.cdn_api import CDNApi
 from edgeimpulse_api.api.classify_api import ClassifyApi
@@ -135,15 +135,18 @@
 from edgeimpulse_api.models.bounding_box import BoundingBox
 from edgeimpulse_api.models.bounding_box_with_score import BoundingBoxWithScore
 from edgeimpulse_api.models.build_on_device_model_request import BuildOnDeviceModelRequest
 from edgeimpulse_api.models.build_organization_on_device_model_request import BuildOrganizationOnDeviceModelRequest
 from edgeimpulse_api.models.change_password_request import ChangePasswordRequest
 from edgeimpulse_api.models.classify_job_response import ClassifyJobResponse
 from edgeimpulse_api.models.classify_job_response_all_of import ClassifyJobResponseAllOf
-from edgeimpulse_api.models.classify_job_response_all_of_result import ClassifyJobResponseAllOfResult
+from edgeimpulse_api.models.classify_job_response_all_of_accuracy import ClassifyJobResponseAllOfAccuracy
+from edgeimpulse_api.models.classify_job_response_all_of_accuracy_total_summary import ClassifyJobResponseAllOfAccuracyTotalSummary
+from edgeimpulse_api.models.classify_job_response_page import ClassifyJobResponsePage
+from edgeimpulse_api.models.classify_job_response_page_all_of import ClassifyJobResponsePageAllOf
 from edgeimpulse_api.models.classify_sample_response import ClassifySampleResponse
 from edgeimpulse_api.models.classify_sample_response_all_of import ClassifySampleResponseAllOf
 from edgeimpulse_api.models.classify_sample_response_classification import ClassifySampleResponseClassification
 from edgeimpulse_api.models.classify_sample_response_classification_details import ClassifySampleResponseClassificationDetails
 from edgeimpulse_api.models.convert_user_request import ConvertUserRequest
 from edgeimpulse_api.models.count_samples_response import CountSamplesResponse
 from edgeimpulse_api.models.count_samples_response_all_of import CountSamplesResponseAllOf
@@ -244,14 +247,15 @@
 from edgeimpulse_api.models.dsp_feature_labels_response import DspFeatureLabelsResponse
 from edgeimpulse_api.models.dsp_feature_labels_response_all_of import DspFeatureLabelsResponseAllOf
 from edgeimpulse_api.models.dsp_performance_all_variants_response import DspPerformanceAllVariantsResponse
 from edgeimpulse_api.models.dsp_performance_all_variants_response_all_of import DspPerformanceAllVariantsResponseAllOf
 from edgeimpulse_api.models.dsp_performance_all_variants_response_all_of_performance import DspPerformanceAllVariantsResponseAllOfPerformance
 from edgeimpulse_api.models.dsp_run_graph import DspRunGraph
 from edgeimpulse_api.models.dsp_run_graph_axis_labels import DspRunGraphAxisLabels
+from edgeimpulse_api.models.dsp_run_request_with_features import DspRunRequestWithFeatures
 from edgeimpulse_api.models.dsp_run_request_without_features import DspRunRequestWithoutFeatures
 from edgeimpulse_api.models.dsp_run_request_without_features_read_only import DspRunRequestWithoutFeaturesReadOnly
 from edgeimpulse_api.models.dsp_run_response import DspRunResponse
 from edgeimpulse_api.models.dsp_run_response_all_of import DspRunResponseAllOf
 from edgeimpulse_api.models.dsp_run_response_all_of_performance import DspRunResponseAllOfPerformance
 from edgeimpulse_api.models.dsp_run_response_with_sample import DspRunResponseWithSample
 from edgeimpulse_api.models.dsp_run_response_with_sample_all_of import DspRunResponseWithSampleAllOf
@@ -455,14 +459,15 @@
 from edgeimpulse_api.models.log_stdout_response import LogStdoutResponse
 from edgeimpulse_api.models.log_stdout_response_all_of import LogStdoutResponseAllOf
 from edgeimpulse_api.models.log_stdout_response_all_of_stdout import LogStdoutResponseAllOfStdout
 from edgeimpulse_api.models.log_website_pageview_request import LogWebsitePageviewRequest
 from edgeimpulse_api.models.login_response import LoginResponse
 from edgeimpulse_api.models.login_response_all_of import LoginResponseAllOf
 from edgeimpulse_api.models.model_prediction import ModelPrediction
+from edgeimpulse_api.models.model_result import ModelResult
 from edgeimpulse_api.models.model_variant_stats import ModelVariantStats
 from edgeimpulse_api.models.move_raw_data_request import MoveRawDataRequest
 from edgeimpulse_api.models.note import Note
 from edgeimpulse_api.models.object_detection_auto_label_request import ObjectDetectionAutoLabelRequest
 from edgeimpulse_api.models.object_detection_auto_label_response import ObjectDetectionAutoLabelResponse
 from edgeimpulse_api.models.object_detection_auto_label_response_all_of import ObjectDetectionAutoLabelResponseAllOf
 from edgeimpulse_api.models.object_detection_auto_label_response_all_of_results import ObjectDetectionAutoLabelResponseAllOfResults
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/__init__.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/__init__.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/admin_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/admin_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/allows_read_only_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/allows_read_only_api.py`

 * *Files 0% similar despite different names*

```diff
@@ -20,14 +20,15 @@
 from pydantic import Field, StrictBool, StrictInt, StrictStr
 
 from typing import Optional
 
 from edgeimpulse_api.models.anomaly_model_metadata_response import AnomalyModelMetadataResponse
 from edgeimpulse_api.models.anomaly_trained_features_response import AnomalyTrainedFeaturesResponse
 from edgeimpulse_api.models.classify_job_response import ClassifyJobResponse
+from edgeimpulse_api.models.classify_job_response_page import ClassifyJobResponsePage
 from edgeimpulse_api.models.classify_sample_response import ClassifySampleResponse
 from edgeimpulse_api.models.count_samples_response import CountSamplesResponse
 from edgeimpulse_api.models.dsp_metadata_response import DSPMetadataResponse
 from edgeimpulse_api.models.data_explorer_predictions_response import DataExplorerPredictionsResponse
 from edgeimpulse_api.models.deployment_target_engine import DeploymentTargetEngine
 from edgeimpulse_api.models.deployment_targets_response import DeploymentTargetsResponse
 from edgeimpulse_api.models.dsp_run_response_with_sample import DspRunResponseWithSample
@@ -1901,21 +1902,23 @@
             _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
             _preload_content=_params.get('_preload_content', True),
             _request_timeout=_params.get('_request_timeout'),
             collection_formats=_collection_formats,
             _request_auth=_params.get('_request_auth'))
 
     @validate_arguments
-    def get_classify_job_result(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], **kwargs) -> ClassifyJobResponse:  # noqa: E501
+    def get_classify_job_result(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], feature_explorer_only : Annotated[Optional[StrictBool], Field(description="Whether to get only the classification results relevant to the feature explorer.")] = None, **kwargs) -> ClassifyJobResponse:  # noqa: E501
         """Classify job result
 
         Get classify job result, containing the result for the complete testing dataset.
 
         :param project_id: Project ID (required)
         :type project_id: int
+        :param feature_explorer_only: Whether to get only the classification results relevant to the feature explorer.
+        :type feature_explorer_only: bool
         :param async_req: Whether to execute the request asynchronously.
         :type async_req: bool, optional
         :param _preload_content: if False, the urllib3.HTTPResponse object will
                                  be returned without reading/decoding response
                                  data. Default is True.
         :type _preload_content: bool, optional
         :param _request_timeout: timeout setting for this request. If one
@@ -1924,24 +1927,26 @@
                                  (connection, read) timeouts.
         :return: Returns the result object.
                  If the method is called asynchronously,
                  returns the request thread.
         :rtype: ClassifyJobResponse
         """
         kwargs['_return_http_data_only'] = True
-        return self._get_classify_job_result_with_http_info(project_id, **kwargs)  # noqa: E501
+        return self._get_classify_job_result_with_http_info(project_id, feature_explorer_only, **kwargs)  # noqa: E501
 
     @validate_arguments
-    def _get_classify_job_result_with_http_info(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], **kwargs):  # noqa: E501
+    def _get_classify_job_result_with_http_info(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], feature_explorer_only : Annotated[Optional[StrictBool], Field(description="Whether to get only the classification results relevant to the feature explorer.")] = None, **kwargs):  # noqa: E501
         """Classify job result 
 
         Get classify job result, containing the result for the complete testing dataset.
 
         :param project_id: Project ID (required)
         :type project_id: int
+        :param feature_explorer_only: Whether to get only the classification results relevant to the feature explorer.
+        :type feature_explorer_only: bool
         :param async_req: Whether to execute the request asynchronously.
         :type async_req: bool, optional
         :param _return_http_data_only: response data without head status code
                                        and headers
         :type _return_http_data_only: bool, optional
         :param _preload_content: if False, the urllib3.HTTPResponse object will
                                  be returned without reading/decoding response
@@ -1961,15 +1966,16 @@
                  returns the request thread.
         :rtype: tuple(ClassifyJobResponse, status_code(int), headers(HTTPHeaderDict))
         """
 
         _params = locals()
 
         _all_params = [
-            'project_id'
+            'project_id',
+            'feature_explorer_only'
         ]
         _all_params.extend(
             [
                 'async_req',
                 '_return_http_data_only',
                 '_preload_content',
                 '_request_timeout',
@@ -1994,14 +2000,16 @@
         # process the path parameters
         _path_params = {}
         if _params['project_id']:
             _path_params['projectId'] = _params['project_id']
 
         # process the query parameters
         _query_params = []
+        if _params.get('feature_explorer_only') is not None:  # noqa: E501
+            _query_params.append(('featureExplorerOnly', _params['feature_explorer_only']))
 
         # process the header parameters
         _header_params = dict(_params.get('_headers', {}))
 
         # process the form parameters
         _form_params = []
         _files = {}
@@ -2025,14 +2033,161 @@
             _path_params,
             _query_params,
             _header_params,
             body=_body_params,
             post_params=_form_params,
             files=_files,
             response_types_map=_response_types_map,
+            auth_settings=_auth_settings,
+            async_req=_params.get('async_req'),
+            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
+            _preload_content=_params.get('_preload_content', True),
+            _request_timeout=_params.get('_request_timeout'),
+            collection_formats=_collection_formats,
+            _request_auth=_params.get('_request_auth'))
+
+    @validate_arguments
+    def get_classify_job_result_page(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], limit : Annotated[Optional[StrictInt], Field(description="Maximum number of results")] = None, offset : Annotated[Optional[StrictInt], Field(description="Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.")] = None, **kwargs) -> ClassifyJobResponsePage:  # noqa: E501
+        """Single page of a classify job result
+
+        Get classify job result, containing the predictions for a given page.
+
+        :param project_id: Project ID (required)
+        :type project_id: int
+        :param limit: Maximum number of results
+        :type limit: int
+        :param offset: Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.
+        :type offset: int
+        :param async_req: Whether to execute the request asynchronously.
+        :type async_req: bool, optional
+        :param _preload_content: if False, the urllib3.HTTPResponse object will
+                                 be returned without reading/decoding response
+                                 data. Default is True.
+        :type _preload_content: bool, optional
+        :param _request_timeout: timeout setting for this request. If one
+                                 number provided, it will be total request
+                                 timeout. It can also be a pair (tuple) of
+                                 (connection, read) timeouts.
+        :return: Returns the result object.
+                 If the method is called asynchronously,
+                 returns the request thread.
+        :rtype: ClassifyJobResponsePage
+        """
+        kwargs['_return_http_data_only'] = True
+        return self._get_classify_job_result_page_with_http_info(project_id, limit, offset, **kwargs)  # noqa: E501
+
+    @validate_arguments
+    def _get_classify_job_result_page_with_http_info(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], limit : Annotated[Optional[StrictInt], Field(description="Maximum number of results")] = None, offset : Annotated[Optional[StrictInt], Field(description="Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.")] = None, **kwargs):  # noqa: E501
+        """Single page of a classify job result 
+
+        Get classify job result, containing the predictions for a given page.
+
+        :param project_id: Project ID (required)
+        :type project_id: int
+        :param limit: Maximum number of results
+        :type limit: int
+        :param offset: Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.
+        :type offset: int
+        :param async_req: Whether to execute the request asynchronously.
+        :type async_req: bool, optional
+        :param _return_http_data_only: response data without head status code
+                                       and headers
+        :type _return_http_data_only: bool, optional
+        :param _preload_content: if False, the urllib3.HTTPResponse object will
+                                 be returned without reading/decoding response
+                                 data. Default is True.
+        :type _preload_content: bool, optional
+        :param _request_timeout: timeout setting for this request. If one
+                                 number provided, it will be total request
+                                 timeout. It can also be a pair (tuple) of
+                                 (connection, read) timeouts.
+        :param _request_auth: set to override the auth_settings for an a single
+                              request; this effectively ignores the authentication
+                              in the spec for a single request.
+        :type _request_auth: dict, optional
+        :type _content_type: string, optional: force content-type for the request
+        :return: Returns the result object.
+                 If the method is called asynchronously,
+                 returns the request thread.
+        :rtype: tuple(ClassifyJobResponsePage, status_code(int), headers(HTTPHeaderDict))
+        """
+
+        _params = locals()
+
+        _all_params = [
+            'project_id',
+            'limit',
+            'offset'
+        ]
+        _all_params.extend(
+            [
+                'async_req',
+                '_return_http_data_only',
+                '_preload_content',
+                '_request_timeout',
+                '_request_auth',
+                '_content_type',
+                '_headers'
+            ]
+        )
+
+        # validate the arguments
+        for _key, _val in _params['kwargs'].items():
+            if _key not in _all_params:
+                raise ApiTypeError(
+                    "Got an unexpected keyword argument '%s'"
+                    " to method get_classify_job_result_page" % _key
+                )
+            _params[_key] = _val
+        del _params['kwargs']
+
+        _collection_formats = {}
+
+        # process the path parameters
+        _path_params = {}
+        if _params['project_id']:
+            _path_params['projectId'] = _params['project_id']
+
+        # process the query parameters
+        _query_params = []
+        if _params.get('limit') is not None:  # noqa: E501
+            _query_params.append(('limit', _params['limit']))
+        if _params.get('offset') is not None:  # noqa: E501
+            _query_params.append(('offset', _params['offset']))
+
+        # process the header parameters
+        _header_params = dict(_params.get('_headers', {}))
+
+        # process the form parameters
+        _form_params = []
+        _files = {}
+
+        # process the body parameter
+        _body_params = None
+
+        # set the HTTP header `Accept`
+        _header_params['Accept'] = self.api_client.select_header_accept(
+            ['application/json'])  # noqa: E501
+
+        # authentication setting
+        _auth_settings = ['ApiKeyAuthentication', 'JWTAuthentication', 'JWTHttpHeaderAuthentication']  # noqa: E501
+
+        _response_types_map = {
+            '200': "ClassifyJobResponsePage",
+        }
+
+        return self.api_client.call_api(
+            '/api/{projectId}/classify/all/result/page', 'GET',
+            _path_params,
+            _query_params,
+            _header_params,
+            body=_body_params,
+            post_params=_form_params,
+            files=_files,
+            response_types_map=_response_types_map,
             auth_settings=_auth_settings,
             async_req=_params.get('async_req'),
             _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
             _preload_content=_params.get('_preload_content', True),
             _request_timeout=_params.get('_request_timeout'),
             collection_formats=_collection_formats,
             _request_auth=_params.get('_request_auth'))
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/auth_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/auth_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/cdn_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/cdn_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/classify_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/classify_api.py`

 * *Files 14% similar despite different names*

```diff
@@ -13,17 +13,20 @@
 from __future__ import absolute_import
 
 import re  # noqa: F401
 
 from pydantic import validate_arguments, ValidationError
 from typing_extensions import Annotated
 
-from pydantic import Field, StrictInt
+from pydantic import Field, StrictBool, StrictInt
+
+from typing import Optional
 
 from edgeimpulse_api.models.classify_job_response import ClassifyJobResponse
+from edgeimpulse_api.models.classify_job_response_page import ClassifyJobResponsePage
 from edgeimpulse_api.models.classify_sample_response import ClassifySampleResponse
 
 from edgeimpulse_api.api_client import ApiClient
 from edgeimpulse_api.exceptions import (  # noqa: F401
     ApiTypeError,
     ApiValueError
 )
@@ -319,21 +322,23 @@
             _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
             _preload_content=_params.get('_preload_content', True),
             _request_timeout=_params.get('_request_timeout'),
             collection_formats=_collection_formats,
             _request_auth=_params.get('_request_auth'))
 
     @validate_arguments
-    def get_classify_job_result(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], **kwargs) -> ClassifyJobResponse:  # noqa: E501
+    def get_classify_job_result(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], feature_explorer_only : Annotated[Optional[StrictBool], Field(description="Whether to get only the classification results relevant to the feature explorer.")] = None, **kwargs) -> ClassifyJobResponse:  # noqa: E501
         """Classify job result
 
         Get classify job result, containing the result for the complete testing dataset.
 
         :param project_id: Project ID (required)
         :type project_id: int
+        :param feature_explorer_only: Whether to get only the classification results relevant to the feature explorer.
+        :type feature_explorer_only: bool
         :param async_req: Whether to execute the request asynchronously.
         :type async_req: bool, optional
         :param _preload_content: if False, the urllib3.HTTPResponse object will
                                  be returned without reading/decoding response
                                  data. Default is True.
         :type _preload_content: bool, optional
         :param _request_timeout: timeout setting for this request. If one
@@ -342,24 +347,26 @@
                                  (connection, read) timeouts.
         :return: Returns the result object.
                  If the method is called asynchronously,
                  returns the request thread.
         :rtype: ClassifyJobResponse
         """
         kwargs['_return_http_data_only'] = True
-        return self._get_classify_job_result_with_http_info(project_id, **kwargs)  # noqa: E501
+        return self._get_classify_job_result_with_http_info(project_id, feature_explorer_only, **kwargs)  # noqa: E501
 
     @validate_arguments
-    def _get_classify_job_result_with_http_info(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], **kwargs):  # noqa: E501
+    def _get_classify_job_result_with_http_info(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], feature_explorer_only : Annotated[Optional[StrictBool], Field(description="Whether to get only the classification results relevant to the feature explorer.")] = None, **kwargs):  # noqa: E501
         """Classify job result 
 
         Get classify job result, containing the result for the complete testing dataset.
 
         :param project_id: Project ID (required)
         :type project_id: int
+        :param feature_explorer_only: Whether to get only the classification results relevant to the feature explorer.
+        :type feature_explorer_only: bool
         :param async_req: Whether to execute the request asynchronously.
         :type async_req: bool, optional
         :param _return_http_data_only: response data without head status code
                                        and headers
         :type _return_http_data_only: bool, optional
         :param _preload_content: if False, the urllib3.HTTPResponse object will
                                  be returned without reading/decoding response
@@ -379,15 +386,16 @@
                  returns the request thread.
         :rtype: tuple(ClassifyJobResponse, status_code(int), headers(HTTPHeaderDict))
         """
 
         _params = locals()
 
         _all_params = [
-            'project_id'
+            'project_id',
+            'feature_explorer_only'
         ]
         _all_params.extend(
             [
                 'async_req',
                 '_return_http_data_only',
                 '_preload_content',
                 '_request_timeout',
@@ -412,14 +420,16 @@
         # process the path parameters
         _path_params = {}
         if _params['project_id']:
             _path_params['projectId'] = _params['project_id']
 
         # process the query parameters
         _query_params = []
+        if _params.get('feature_explorer_only') is not None:  # noqa: E501
+            _query_params.append(('featureExplorerOnly', _params['feature_explorer_only']))
 
         # process the header parameters
         _header_params = dict(_params.get('_headers', {}))
 
         # process the form parameters
         _form_params = []
         _files = {}
@@ -443,14 +453,161 @@
             _path_params,
             _query_params,
             _header_params,
             body=_body_params,
             post_params=_form_params,
             files=_files,
             response_types_map=_response_types_map,
+            auth_settings=_auth_settings,
+            async_req=_params.get('async_req'),
+            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
+            _preload_content=_params.get('_preload_content', True),
+            _request_timeout=_params.get('_request_timeout'),
+            collection_formats=_collection_formats,
+            _request_auth=_params.get('_request_auth'))
+
+    @validate_arguments
+    def get_classify_job_result_page(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], limit : Annotated[Optional[StrictInt], Field(description="Maximum number of results")] = None, offset : Annotated[Optional[StrictInt], Field(description="Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.")] = None, **kwargs) -> ClassifyJobResponsePage:  # noqa: E501
+        """Single page of a classify job result
+
+        Get classify job result, containing the predictions for a given page.
+
+        :param project_id: Project ID (required)
+        :type project_id: int
+        :param limit: Maximum number of results
+        :type limit: int
+        :param offset: Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.
+        :type offset: int
+        :param async_req: Whether to execute the request asynchronously.
+        :type async_req: bool, optional
+        :param _preload_content: if False, the urllib3.HTTPResponse object will
+                                 be returned without reading/decoding response
+                                 data. Default is True.
+        :type _preload_content: bool, optional
+        :param _request_timeout: timeout setting for this request. If one
+                                 number provided, it will be total request
+                                 timeout. It can also be a pair (tuple) of
+                                 (connection, read) timeouts.
+        :return: Returns the result object.
+                 If the method is called asynchronously,
+                 returns the request thread.
+        :rtype: ClassifyJobResponsePage
+        """
+        kwargs['_return_http_data_only'] = True
+        return self._get_classify_job_result_page_with_http_info(project_id, limit, offset, **kwargs)  # noqa: E501
+
+    @validate_arguments
+    def _get_classify_job_result_page_with_http_info(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], limit : Annotated[Optional[StrictInt], Field(description="Maximum number of results")] = None, offset : Annotated[Optional[StrictInt], Field(description="Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.")] = None, **kwargs):  # noqa: E501
+        """Single page of a classify job result 
+
+        Get classify job result, containing the predictions for a given page.
+
+        :param project_id: Project ID (required)
+        :type project_id: int
+        :param limit: Maximum number of results
+        :type limit: int
+        :param offset: Offset in results, can be used in conjunction with LimitResultsParameter to implement paging.
+        :type offset: int
+        :param async_req: Whether to execute the request asynchronously.
+        :type async_req: bool, optional
+        :param _return_http_data_only: response data without head status code
+                                       and headers
+        :type _return_http_data_only: bool, optional
+        :param _preload_content: if False, the urllib3.HTTPResponse object will
+                                 be returned without reading/decoding response
+                                 data. Default is True.
+        :type _preload_content: bool, optional
+        :param _request_timeout: timeout setting for this request. If one
+                                 number provided, it will be total request
+                                 timeout. It can also be a pair (tuple) of
+                                 (connection, read) timeouts.
+        :param _request_auth: set to override the auth_settings for an a single
+                              request; this effectively ignores the authentication
+                              in the spec for a single request.
+        :type _request_auth: dict, optional
+        :type _content_type: string, optional: force content-type for the request
+        :return: Returns the result object.
+                 If the method is called asynchronously,
+                 returns the request thread.
+        :rtype: tuple(ClassifyJobResponsePage, status_code(int), headers(HTTPHeaderDict))
+        """
+
+        _params = locals()
+
+        _all_params = [
+            'project_id',
+            'limit',
+            'offset'
+        ]
+        _all_params.extend(
+            [
+                'async_req',
+                '_return_http_data_only',
+                '_preload_content',
+                '_request_timeout',
+                '_request_auth',
+                '_content_type',
+                '_headers'
+            ]
+        )
+
+        # validate the arguments
+        for _key, _val in _params['kwargs'].items():
+            if _key not in _all_params:
+                raise ApiTypeError(
+                    "Got an unexpected keyword argument '%s'"
+                    " to method get_classify_job_result_page" % _key
+                )
+            _params[_key] = _val
+        del _params['kwargs']
+
+        _collection_formats = {}
+
+        # process the path parameters
+        _path_params = {}
+        if _params['project_id']:
+            _path_params['projectId'] = _params['project_id']
+
+        # process the query parameters
+        _query_params = []
+        if _params.get('limit') is not None:  # noqa: E501
+            _query_params.append(('limit', _params['limit']))
+        if _params.get('offset') is not None:  # noqa: E501
+            _query_params.append(('offset', _params['offset']))
+
+        # process the header parameters
+        _header_params = dict(_params.get('_headers', {}))
+
+        # process the form parameters
+        _form_params = []
+        _files = {}
+
+        # process the body parameter
+        _body_params = None
+
+        # set the HTTP header `Accept`
+        _header_params['Accept'] = self.api_client.select_header_accept(
+            ['application/json'])  # noqa: E501
+
+        # authentication setting
+        _auth_settings = ['ApiKeyAuthentication', 'JWTAuthentication', 'JWTHttpHeaderAuthentication']  # noqa: E501
+
+        _response_types_map = {
+            '200': "ClassifyJobResponsePage",
+        }
+
+        return self.api_client.call_api(
+            '/api/{projectId}/classify/all/result/page', 'GET',
+            _path_params,
+            _query_params,
+            _header_params,
+            body=_body_params,
+            post_params=_form_params,
+            files=_files,
+            response_types_map=_response_types_map,
             auth_settings=_auth_settings,
             async_req=_params.get('async_req'),
             _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
             _preload_content=_params.get('_preload_content', True),
             _request_timeout=_params.get('_request_timeout'),
             collection_formats=_collection_formats,
             _request_auth=_params.get('_request_auth'))
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/content_disposition_inline_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/content_disposition_inline_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/deployment_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/deployment_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/devices_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/devices_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/dsp_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/dsp_api.py`

 * *Files 1% similar despite different names*

```diff
@@ -24,16 +24,18 @@
 from edgeimpulse_api.models.dsp_config_request import DSPConfigRequest
 from edgeimpulse_api.models.dsp_config_response import DSPConfigResponse
 from edgeimpulse_api.models.dsp_metadata_response import DSPMetadataResponse
 from edgeimpulse_api.models.dsp_autotuner_results import DspAutotunerResults
 from edgeimpulse_api.models.dsp_feature_importance_response import DspFeatureImportanceResponse
 from edgeimpulse_api.models.dsp_feature_labels_response import DspFeatureLabelsResponse
 from edgeimpulse_api.models.dsp_performance_all_variants_response import DspPerformanceAllVariantsResponse
+from edgeimpulse_api.models.dsp_run_request_with_features import DspRunRequestWithFeatures
 from edgeimpulse_api.models.dsp_run_request_without_features import DspRunRequestWithoutFeatures
 from edgeimpulse_api.models.dsp_run_request_without_features_read_only import DspRunRequestWithoutFeaturesReadOnly
+from edgeimpulse_api.models.dsp_run_response import DspRunResponse
 from edgeimpulse_api.models.dsp_run_response_with_sample import DspRunResponseWithSample
 from edgeimpulse_api.models.dsp_sample_features_response import DspSampleFeaturesResponse
 from edgeimpulse_api.models.dsp_trained_features_response import DspTrainedFeaturesResponse
 from edgeimpulse_api.models.generic_api_response import GenericApiResponse
 from edgeimpulse_api.models.get_sample_response import GetSampleResponse
 from edgeimpulse_api.models.start_job_response import StartJobResponse
 
@@ -1949,14 +1951,168 @@
             _path_params,
             _query_params,
             _header_params,
             body=_body_params,
             post_params=_form_params,
             files=_files,
             response_types_map=_response_types_map,
+            auth_settings=_auth_settings,
+            async_req=_params.get('async_req'),
+            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
+            _preload_content=_params.get('_preload_content', True),
+            _request_timeout=_params.get('_request_timeout'),
+            collection_formats=_collection_formats,
+            _request_auth=_params.get('_request_auth'))
+
+    @validate_arguments
+    def run_dsp_on_features_array(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], dsp_id : Annotated[StrictInt, Field(..., description="DSP Block ID, use the impulse functions to retrieve the ID")], dsp_run_request_with_features : DspRunRequestWithFeatures, **kwargs) -> DspRunResponse:  # noqa: E501
+        """Get processed sample (from features array)
+
+        Takes in a features array and runs it through the DSP block. This data should have the same frequency as set in the input block in your impulse.
+
+        :param project_id: Project ID (required)
+        :type project_id: int
+        :param dsp_id: DSP Block ID, use the impulse functions to retrieve the ID (required)
+        :type dsp_id: int
+        :param dsp_run_request_with_features: (required)
+        :type dsp_run_request_with_features: DspRunRequestWithFeatures
+        :param async_req: Whether to execute the request asynchronously.
+        :type async_req: bool, optional
+        :param _preload_content: if False, the urllib3.HTTPResponse object will
+                                 be returned without reading/decoding response
+                                 data. Default is True.
+        :type _preload_content: bool, optional
+        :param _request_timeout: timeout setting for this request. If one
+                                 number provided, it will be total request
+                                 timeout. It can also be a pair (tuple) of
+                                 (connection, read) timeouts.
+        :return: Returns the result object.
+                 If the method is called asynchronously,
+                 returns the request thread.
+        :rtype: DspRunResponse
+        """
+        kwargs['_return_http_data_only'] = True
+        return self._run_dsp_on_features_array_with_http_info(project_id, dsp_id, dsp_run_request_with_features, **kwargs)  # noqa: E501
+
+    @validate_arguments
+    def _run_dsp_on_features_array_with_http_info(self, project_id : Annotated[StrictInt, Field(..., description="Project ID")], dsp_id : Annotated[StrictInt, Field(..., description="DSP Block ID, use the impulse functions to retrieve the ID")], dsp_run_request_with_features : DspRunRequestWithFeatures, **kwargs):  # noqa: E501
+        """Get processed sample (from features array) 
+
+        Takes in a features array and runs it through the DSP block. This data should have the same frequency as set in the input block in your impulse.
+
+        :param project_id: Project ID (required)
+        :type project_id: int
+        :param dsp_id: DSP Block ID, use the impulse functions to retrieve the ID (required)
+        :type dsp_id: int
+        :param dsp_run_request_with_features: (required)
+        :type dsp_run_request_with_features: DspRunRequestWithFeatures
+        :param async_req: Whether to execute the request asynchronously.
+        :type async_req: bool, optional
+        :param _return_http_data_only: response data without head status code
+                                       and headers
+        :type _return_http_data_only: bool, optional
+        :param _preload_content: if False, the urllib3.HTTPResponse object will
+                                 be returned without reading/decoding response
+                                 data. Default is True.
+        :type _preload_content: bool, optional
+        :param _request_timeout: timeout setting for this request. If one
+                                 number provided, it will be total request
+                                 timeout. It can also be a pair (tuple) of
+                                 (connection, read) timeouts.
+        :param _request_auth: set to override the auth_settings for an a single
+                              request; this effectively ignores the authentication
+                              in the spec for a single request.
+        :type _request_auth: dict, optional
+        :type _content_type: string, optional: force content-type for the request
+        :return: Returns the result object.
+                 If the method is called asynchronously,
+                 returns the request thread.
+        :rtype: tuple(DspRunResponse, status_code(int), headers(HTTPHeaderDict))
+        """
+
+        _params = locals()
+
+        _all_params = [
+            'project_id',
+            'dsp_id',
+            'dsp_run_request_with_features'
+        ]
+        _all_params.extend(
+            [
+                'async_req',
+                '_return_http_data_only',
+                '_preload_content',
+                '_request_timeout',
+                '_request_auth',
+                '_content_type',
+                '_headers'
+            ]
+        )
+
+        # validate the arguments
+        for _key, _val in _params['kwargs'].items():
+            if _key not in _all_params:
+                raise ApiTypeError(
+                    "Got an unexpected keyword argument '%s'"
+                    " to method run_dsp_on_features_array" % _key
+                )
+            _params[_key] = _val
+        del _params['kwargs']
+
+        _collection_formats = {}
+
+        # process the path parameters
+        _path_params = {}
+        if _params['project_id']:
+            _path_params['projectId'] = _params['project_id']
+        if _params['dsp_id']:
+            _path_params['dspId'] = _params['dsp_id']
+
+        # process the query parameters
+        _query_params = []
+
+        # process the header parameters
+        _header_params = dict(_params.get('_headers', {}))
+
+        # process the form parameters
+        _form_params = []
+        _files = {}
+
+        # process the body parameter
+        _body_params = None
+        if _params['dsp_run_request_with_features']:
+            _body_params = _params['dsp_run_request_with_features']
+
+        # set the HTTP header `Accept`
+        _header_params['Accept'] = self.api_client.select_header_accept(
+            ['application/json'])  # noqa: E501
+
+        # set the HTTP header `Content-Type`
+        _content_types_list = _params.get('_content_type',
+            self.api_client.select_header_content_type(
+                ['application/json']))
+        if _content_types_list:
+                _header_params['Content-Type'] = _content_types_list
+
+        # authentication setting
+        _auth_settings = ['ApiKeyAuthentication', 'JWTAuthentication', 'JWTHttpHeaderAuthentication']  # noqa: E501
+
+        _response_types_map = {
+            '200': "DspRunResponse",
+        }
+
+        return self.api_client.call_api(
+            '/api/{projectId}/dsp/{dspId}/run', 'POST',
+            _path_params,
+            _query_params,
+            _header_params,
+            body=_body_params,
+            post_params=_form_params,
+            files=_files,
+            response_types_map=_response_types_map,
             auth_settings=_auth_settings,
             async_req=_params.get('async_req'),
             _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
             _preload_content=_params.get('_preload_content', True),
             _request_timeout=_params.get('_request_timeout'),
             collection_formats=_collection_formats,
             _request_auth=_params.get('_request_auth'))
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/export_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/export_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/health_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/health_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/impulse_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/impulse_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/jobs_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/jobs_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/learn_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/learn_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/login_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/login_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/metrics_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/metrics_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/optimization_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/optimization_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_allow_developer_profile_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_allow_developer_profile_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_allow_guest_access_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_allow_guest_access_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_blocks_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_blocks_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_create_project_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_create_project_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_data_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_data_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_jobs_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_jobs_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_pipelines_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_pipelines_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_portals_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_portals_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_requires_admin_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_requires_admin_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/organization_requires_whitelabel_admin_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/organization_requires_whitelabel_admin_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/organizations_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/organizations_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/performance_calibration_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/performance_calibration_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/projects_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/projects_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/raw_data_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/raw_data_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/requires_sudo_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/requires_sudo_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/requires_third_party_auth_api_key_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/requires_third_party_auth_api_key_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/supports_range_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/supports_range_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/themes_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/themes_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/third_party_auth_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/third_party_auth_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/upload_portal_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/upload_portal_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/user_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/user_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api/whitelabels_api.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api/whitelabels_api.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/api_client.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/api_client.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/configuration.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/configuration.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/exceptions.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/exceptions.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/__init__.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -82,15 +82,18 @@
 from edgeimpulse_api.models.bounding_box import BoundingBox
 from edgeimpulse_api.models.bounding_box_with_score import BoundingBoxWithScore
 from edgeimpulse_api.models.build_on_device_model_request import BuildOnDeviceModelRequest
 from edgeimpulse_api.models.build_organization_on_device_model_request import BuildOrganizationOnDeviceModelRequest
 from edgeimpulse_api.models.change_password_request import ChangePasswordRequest
 from edgeimpulse_api.models.classify_job_response import ClassifyJobResponse
 from edgeimpulse_api.models.classify_job_response_all_of import ClassifyJobResponseAllOf
-from edgeimpulse_api.models.classify_job_response_all_of_result import ClassifyJobResponseAllOfResult
+from edgeimpulse_api.models.classify_job_response_all_of_accuracy import ClassifyJobResponseAllOfAccuracy
+from edgeimpulse_api.models.classify_job_response_all_of_accuracy_total_summary import ClassifyJobResponseAllOfAccuracyTotalSummary
+from edgeimpulse_api.models.classify_job_response_page import ClassifyJobResponsePage
+from edgeimpulse_api.models.classify_job_response_page_all_of import ClassifyJobResponsePageAllOf
 from edgeimpulse_api.models.classify_sample_response import ClassifySampleResponse
 from edgeimpulse_api.models.classify_sample_response_all_of import ClassifySampleResponseAllOf
 from edgeimpulse_api.models.classify_sample_response_classification import ClassifySampleResponseClassification
 from edgeimpulse_api.models.classify_sample_response_classification_details import ClassifySampleResponseClassificationDetails
 from edgeimpulse_api.models.convert_user_request import ConvertUserRequest
 from edgeimpulse_api.models.count_samples_response import CountSamplesResponse
 from edgeimpulse_api.models.count_samples_response_all_of import CountSamplesResponseAllOf
@@ -191,14 +194,15 @@
 from edgeimpulse_api.models.dsp_feature_labels_response import DspFeatureLabelsResponse
 from edgeimpulse_api.models.dsp_feature_labels_response_all_of import DspFeatureLabelsResponseAllOf
 from edgeimpulse_api.models.dsp_performance_all_variants_response import DspPerformanceAllVariantsResponse
 from edgeimpulse_api.models.dsp_performance_all_variants_response_all_of import DspPerformanceAllVariantsResponseAllOf
 from edgeimpulse_api.models.dsp_performance_all_variants_response_all_of_performance import DspPerformanceAllVariantsResponseAllOfPerformance
 from edgeimpulse_api.models.dsp_run_graph import DspRunGraph
 from edgeimpulse_api.models.dsp_run_graph_axis_labels import DspRunGraphAxisLabels
+from edgeimpulse_api.models.dsp_run_request_with_features import DspRunRequestWithFeatures
 from edgeimpulse_api.models.dsp_run_request_without_features import DspRunRequestWithoutFeatures
 from edgeimpulse_api.models.dsp_run_request_without_features_read_only import DspRunRequestWithoutFeaturesReadOnly
 from edgeimpulse_api.models.dsp_run_response import DspRunResponse
 from edgeimpulse_api.models.dsp_run_response_all_of import DspRunResponseAllOf
 from edgeimpulse_api.models.dsp_run_response_all_of_performance import DspRunResponseAllOfPerformance
 from edgeimpulse_api.models.dsp_run_response_with_sample import DspRunResponseWithSample
 from edgeimpulse_api.models.dsp_run_response_with_sample_all_of import DspRunResponseWithSampleAllOf
@@ -402,14 +406,15 @@
 from edgeimpulse_api.models.log_stdout_response import LogStdoutResponse
 from edgeimpulse_api.models.log_stdout_response_all_of import LogStdoutResponseAllOf
 from edgeimpulse_api.models.log_stdout_response_all_of_stdout import LogStdoutResponseAllOfStdout
 from edgeimpulse_api.models.log_website_pageview_request import LogWebsitePageviewRequest
 from edgeimpulse_api.models.login_response import LoginResponse
 from edgeimpulse_api.models.login_response_all_of import LoginResponseAllOf
 from edgeimpulse_api.models.model_prediction import ModelPrediction
+from edgeimpulse_api.models.model_result import ModelResult
 from edgeimpulse_api.models.model_variant_stats import ModelVariantStats
 from edgeimpulse_api.models.move_raw_data_request import MoveRawDataRequest
 from edgeimpulse_api.models.note import Note
 from edgeimpulse_api.models.object_detection_auto_label_request import ObjectDetectionAutoLabelRequest
 from edgeimpulse_api.models.object_detection_auto_label_response import ObjectDetectionAutoLabelResponse
 from edgeimpulse_api.models.object_detection_auto_label_response_all_of import ObjectDetectionAutoLabelResponseAllOf
 from edgeimpulse_api.models.object_detection_auto_label_response_all_of_results import ObjectDetectionAutoLabelResponseAllOfResults
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/activate_user_by_third_party_activation_code_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/activate_user_by_third_party_activation_code_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/activate_user_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/activate_user_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_api_key_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_api_key_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_collaborator_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_collaborator_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_hmac_key_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_hmac_key_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_member_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_member_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_api_key_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_api_key_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_bucket_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_bucket_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_deploy_block_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_deploy_block_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_dsp_block_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_dsp_block_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_dsp_block_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_dsp_block_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_secret_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_secret_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_secret_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_secret_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_secret_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_secret_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_transfer_learning_block_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_transfer_learning_block_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_transfer_learning_block_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_transfer_learning_block_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_transformation_block_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_transformation_block_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_transformation_block_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_transformation_block_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/add_organization_transformation_block_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/add_organization_transformation_block_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_add_or_update_sso_domain_id_ps_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_add_or_update_sso_domain_id_ps_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_add_project_user_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_add_project_user_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_api_organization.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_api_organization.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_api_organization_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_api_organization_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_api_project.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_api_project.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_api_user.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_api_user.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_api_user_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_api_user_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_create_organization_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_create_organization_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_metrics_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_metrics_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_metrics_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_metrics_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_organizations_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_organizations_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_organizations_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_organizations_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_organizations_response_all_of_organizations.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_organizations_response_all_of_organizations.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_sso_domain_id_ps_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_sso_domain_id_ps_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_sso_domain_id_ps_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_sso_domain_id_ps_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_sso_settings_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_sso_settings_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_sso_settings_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_sso_settings_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_sso_settings_response_all_of_sso_whitelist.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_sso_settings_response_all_of_sso_whitelist.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_ids_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_ids_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_ids_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_ids_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_metrics_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_metrics_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_metrics_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_metrics_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_user_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_user_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_users_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_users_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_users_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_users_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_get_users_response_all_of_users.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_get_users_response_all_of_users.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_list_projects.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_list_projects.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_list_projects_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_list_projects_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_organization_info_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_organization_info_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_organization_info_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_organization_info_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_update_organization_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_update_organization_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/admin_update_user_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/admin_update_user_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/akida_edge_learning_config.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/akida_edge_learning_config.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_model_metadata.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_model_metadata.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_model_metadata_clusters_inner.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_model_metadata_clusters_inner.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_model_metadata_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_model_metadata_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_response_all_of_axes.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_response_all_of_axes.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_trained_features_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_trained_features_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_trained_features_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_trained_features_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/anomaly_trained_features_response_all_of_data.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/anomaly_trained_features_response_all_of_data.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/augmentation_policy_spectrogram.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/augmentation_policy_spectrogram.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/autotune_dsp_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/autotune_dsp_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/bounding_box.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/bounding_box.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/bounding_box_with_score.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/bounding_box_with_score.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/build_on_device_model_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/build_on_device_model_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/build_organization_on_device_model_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/build_organization_on_device_model_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/change_password_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/change_password_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_job_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_job_response.py`

 * *Files 8% similar despite different names*

```diff
@@ -15,23 +15,25 @@
 import pprint
 import re  # noqa: F401
 import json
 
 
 from typing import List, Optional
 from pydantic import BaseModel, Field, StrictBool, StrictStr
-from edgeimpulse_api.models.classify_job_response_all_of_result import ClassifyJobResponseAllOfResult
+from edgeimpulse_api.models.classify_job_response_all_of_accuracy import ClassifyJobResponseAllOfAccuracy
 from edgeimpulse_api.models.model_prediction import ModelPrediction
+from edgeimpulse_api.models.model_result import ModelResult
 
 class ClassifyJobResponse(BaseModel):
     success: StrictBool = Field(..., description="Whether the operation succeeded")
     error: Optional[StrictStr] = Field(None, description="Optional error description (set if 'success' was false)")
-    result: List[ClassifyJobResponseAllOfResult] = ...
+    result: List[ModelResult] = ...
     predictions: List[ModelPrediction] = ...
-    __properties = ["success", "error", "result", "predictions"]
+    accuracy: ClassifyJobResponseAllOfAccuracy = ...
+    __properties = ["success", "error", "result", "predictions", "accuracy"]
 
     class Config:
         allow_population_by_field_name = True
         validate_assignment = True
 
     def to_str(self) -> str:
         """Returns the string representation of the model using alias"""
@@ -62,26 +64,30 @@
         # override the default output from pydantic by calling `to_dict()` of each item in predictions (list)
         _items = []
         if self.predictions:
             for _item in self.predictions:
                 if _item:
                     _items.append(_item.to_dict())
             _dict['predictions'] = _items
+        # override the default output from pydantic by calling `to_dict()` of accuracy
+        if self.accuracy:
+            _dict['accuracy'] = self.accuracy.to_dict()
         return _dict
 
     @classmethod
     def from_dict(cls, obj: dict) -> ClassifyJobResponse:
         """Create an instance of ClassifyJobResponse from a dict"""
         if obj is None:
             return None
 
         if type(obj) is not dict:
             return ClassifyJobResponse.parse_obj(obj)
 
         _obj = ClassifyJobResponse.parse_obj({
             "success": obj.get("success"),
             "error": obj.get("error"),
-            "result": [ClassifyJobResponseAllOfResult.from_dict(_item) for _item in obj.get("result")] if obj.get("result") is not None else None,
-            "predictions": [ModelPrediction.from_dict(_item) for _item in obj.get("predictions")] if obj.get("predictions") is not None else None
+            "result": [ModelResult.from_dict(_item) for _item in obj.get("result")] if obj.get("result") is not None else None,
+            "predictions": [ModelPrediction.from_dict(_item) for _item in obj.get("predictions")] if obj.get("predictions") is not None else None,
+            "accuracy": ClassifyJobResponseAllOfAccuracy.from_dict(obj.get("accuracy")) if obj.get("accuracy") is not None else None
         })
         return _obj
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_job_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_job_response_all_of.py`

 * *Files 12% similar despite different names*

```diff
@@ -15,21 +15,23 @@
 import pprint
 import re  # noqa: F401
 import json
 
 
 from typing import List
 from pydantic import BaseModel
-from edgeimpulse_api.models.classify_job_response_all_of_result import ClassifyJobResponseAllOfResult
+from edgeimpulse_api.models.classify_job_response_all_of_accuracy import ClassifyJobResponseAllOfAccuracy
 from edgeimpulse_api.models.model_prediction import ModelPrediction
+from edgeimpulse_api.models.model_result import ModelResult
 
 class ClassifyJobResponseAllOf(BaseModel):
-    result: List[ClassifyJobResponseAllOfResult] = ...
+    result: List[ModelResult] = ...
     predictions: List[ModelPrediction] = ...
-    __properties = ["result", "predictions"]
+    accuracy: ClassifyJobResponseAllOfAccuracy = ...
+    __properties = ["result", "predictions", "accuracy"]
 
     class Config:
         allow_population_by_field_name = True
         validate_assignment = True
 
     def to_str(self) -> str:
         """Returns the string representation of the model using alias"""
@@ -60,24 +62,28 @@
         # override the default output from pydantic by calling `to_dict()` of each item in predictions (list)
         _items = []
         if self.predictions:
             for _item in self.predictions:
                 if _item:
                     _items.append(_item.to_dict())
             _dict['predictions'] = _items
+        # override the default output from pydantic by calling `to_dict()` of accuracy
+        if self.accuracy:
+            _dict['accuracy'] = self.accuracy.to_dict()
         return _dict
 
     @classmethod
     def from_dict(cls, obj: dict) -> ClassifyJobResponseAllOf:
         """Create an instance of ClassifyJobResponseAllOf from a dict"""
         if obj is None:
             return None
 
         if type(obj) is not dict:
             return ClassifyJobResponseAllOf.parse_obj(obj)
 
         _obj = ClassifyJobResponseAllOf.parse_obj({
-            "result": [ClassifyJobResponseAllOfResult.from_dict(_item) for _item in obj.get("result")] if obj.get("result") is not None else None,
-            "predictions": [ModelPrediction.from_dict(_item) for _item in obj.get("predictions")] if obj.get("predictions") is not None else None
+            "result": [ModelResult.from_dict(_item) for _item in obj.get("result")] if obj.get("result") is not None else None,
+            "predictions": [ModelPrediction.from_dict(_item) for _item in obj.get("predictions")] if obj.get("predictions") is not None else None,
+            "accuracy": ClassifyJobResponseAllOfAccuracy.from_dict(obj.get("accuracy")) if obj.get("accuracy") is not None else None
         })
         return _obj
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_job_response_all_of_result.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/model_result.py`

 * *Files 10% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 
 
 from typing import List
 from pydantic import BaseModel, Field, StrictInt
 from edgeimpulse_api.models.classify_sample_response_classification import ClassifySampleResponseClassification
 from edgeimpulse_api.models.sample import Sample
 
-class ClassifyJobResponseAllOfResult(BaseModel):
+class ModelResult(BaseModel):
     sample_id: StrictInt = Field(..., alias="sampleId")
     sample: Sample = ...
     classifications: List[ClassifySampleResponseClassification] = ...
     __properties = ["sampleId", "sample", "classifications"]
 
     class Config:
         allow_population_by_field_name = True
@@ -37,16 +37,16 @@
         return pprint.pformat(self.dict(by_alias=True))
 
     def to_json(self) -> str:
         """Returns the JSON representation of the model using alias"""
         return json.dumps(self.to_dict())
 
     @classmethod
-    def from_json(cls, json_str: str) -> ClassifyJobResponseAllOfResult:
-        """Create an instance of ClassifyJobResponseAllOfResult from a JSON string"""
+    def from_json(cls, json_str: str) -> ModelResult:
+        """Create an instance of ModelResult from a JSON string"""
         return cls.from_dict(json.loads(json_str))
 
     def to_dict(self):
         """Returns the dictionary representation of the model using alias"""
         _dict = self.dict(by_alias=True,
                           exclude={
                           },
@@ -60,22 +60,22 @@
             for _item in self.classifications:
                 if _item:
                     _items.append(_item.to_dict())
             _dict['classifications'] = _items
         return _dict
 
     @classmethod
-    def from_dict(cls, obj: dict) -> ClassifyJobResponseAllOfResult:
-        """Create an instance of ClassifyJobResponseAllOfResult from a dict"""
+    def from_dict(cls, obj: dict) -> ModelResult:
+        """Create an instance of ModelResult from a dict"""
         if obj is None:
             return None
 
         if type(obj) is not dict:
-            return ClassifyJobResponseAllOfResult.parse_obj(obj)
+            return ModelResult.parse_obj(obj)
 
-        _obj = ClassifyJobResponseAllOfResult.parse_obj({
+        _obj = ModelResult.parse_obj({
             "sample_id": obj.get("sampleId"),
             "sample": Sample.from_dict(obj.get("sample")) if obj.get("sample") is not None else None,
             "classifications": [ClassifySampleResponseClassification.from_dict(_item) for _item in obj.get("classifications")] if obj.get("classifications") is not None else None
         })
         return _obj
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_sample_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_sample_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_sample_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_sample_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_sample_response_classification.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_sample_response_classification.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/classify_sample_response_classification_details.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/classify_sample_response_classification_details.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/convert_user_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/convert_user_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/count_samples_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/count_samples_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/count_samples_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/count_samples_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_block_version_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_block_version_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_block_version_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_block_version_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_developer_profile_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_developer_profile_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_developer_profile_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_developer_profile_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_device_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_device_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_evaluation_user_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_evaluation_user_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_evaluation_user_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_evaluation_user_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_portal_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_portal_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_portal_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_portal_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_portal_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_portal_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_organization_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_organization_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_pipeline_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_pipeline_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_project_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_project_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_project_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_project_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_project_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_project_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_signed_upload_link_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_signed_upload_link_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_signed_upload_link_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_signed_upload_link_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_signed_upload_link_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_signed_upload_link_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_third_party_auth_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_third_party_auth_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_third_party_auth_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_third_party_auth_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_third_party_auth_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_third_party_auth_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_third_party_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_third_party_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_third_party_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_third_party_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_user_third_party_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_user_third_party_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_whitelabel_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_whitelabel_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_whitelabel_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_whitelabel_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/create_whitelabel_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/create_whitelabel_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/crop_sample_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/crop_sample_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/crop_sample_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/crop_sample_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/crop_sample_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/crop_sample_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/data_explorer_predictions_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/data_explorer_predictions_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/data_explorer_predictions_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/data_explorer_predictions_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/data_explorer_settings.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/data_explorer_settings.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dataset_ratio_data.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dataset_ratio_data.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dataset_ratio_data_ratio.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dataset_ratio_data_ratio.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/delete_portal_file_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/delete_portal_file_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dependency_data.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dependency_data.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_input_audio.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_input_audio.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_input_image.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_input_image.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_input_other.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_input_other.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_input_time_series.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_input_time_series.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_model_classification.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_model_classification.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_model_object_detection.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_model_object_detection.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_model_regression.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_model_regression.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_request_model_info.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_request_model_info.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_request_model_info_input.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_request_model_info_input.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deploy_pretrained_model_request_model_info_model.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deploy_pretrained_model_request_model_info_model.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deployment_target.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deployment_target.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deployment_target_badge.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deployment_target_badge.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deployment_target_engine.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deployment_target_engine.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deployment_targets_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deployment_targets_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/deployment_targets_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/deployment_targets_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/development_board.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/development_board.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/development_boards_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/development_boards_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/development_boards_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/development_boards_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/development_keys.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/development_keys.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/development_keys_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/development_keys_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/device.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/device.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/device_name_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/device_name_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/device_name_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/device_name_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/device_sensors_inner.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/device_sensors_inner.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/download.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/download.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/download_portal_file_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/download_portal_file_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/download_portal_file_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/download_portal_file_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/download_portal_file_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/download_portal_file_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_autotuner_results.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_autotuner_results.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_autotuner_results_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_autotuner_results_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_autotuner_results_all_of_results.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_autotuner_results_all_of_results.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_block.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_block.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_config_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_config_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_config_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_config_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_config_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_config_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_importance_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_importance_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_importance_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_importance_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_importance_response_all_of_features.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_importance_response_all_of_features.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_importance_response_all_of_labels.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_importance_response_all_of_labels.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_labels_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_labels_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_feature_labels_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_feature_labels_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_group.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_group.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_group_item.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_group_item.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_group_item_select_options_inner.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_group_item_select_options_inner.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_group_item_show_if.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_group_item_show_if.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_info.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_info.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_info_features.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_info_features.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_info_performance.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_info_performance.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_metadata.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_metadata.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_metadata_included_samples_inner.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_metadata_included_samples_inner.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_metadata_output_config.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_metadata_output_config.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_metadata_output_config_shape.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_metadata_output_config_shape.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_metadata_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_metadata_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_performance_all_variants_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_performance_all_variants_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_performance_all_variants_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_performance_all_variants_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_performance_all_variants_response_all_of_performance.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_performance_all_variants_response_all_of_performance.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_graph.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_graph.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_graph_axis_labels.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_graph_axis_labels.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_request_without_features.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_request_without_features.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_request_without_features_read_only.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_request_without_features_read_only.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_response.py`

 * *Files 4% similar despite different names*

```diff
@@ -23,15 +23,15 @@
 from edgeimpulse_api.models.dsp_run_response_all_of_performance import DspRunResponseAllOfPerformance
 
 class DspRunResponse(BaseModel):
     success: StrictBool = Field(..., description="Whether the operation succeeded")
     error: Optional[StrictStr] = Field(None, description="Optional error description (set if 'success' was false)")
     features: List[float] = Field(..., description="Array of processed features. Laid out according to the names in 'labels'")
     graphs: List[DspRunGraph] = Field(..., description="Graphs to plot to give an insight in how the DSP process ran")
-    labels: List[StrictStr] = Field(..., description="Labels of the feature axes")
+    labels: Optional[List[StrictStr]] = Field(None, description="Labels of the feature axes")
     performance: Optional[DspRunResponseAllOfPerformance] = None
     __properties = ["success", "error", "features", "graphs", "labels", "performance"]
 
     class Config:
         allow_population_by_field_name = True
         validate_assignment = True
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_response_all_of.py`

 * *Files 1% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 from pydantic import BaseModel, Field, StrictStr
 from edgeimpulse_api.models.dsp_run_graph import DspRunGraph
 from edgeimpulse_api.models.dsp_run_response_all_of_performance import DspRunResponseAllOfPerformance
 
 class DspRunResponseAllOf(BaseModel):
     features: List[float] = Field(..., description="Array of processed features. Laid out according to the names in 'labels'")
     graphs: List[DspRunGraph] = Field(..., description="Graphs to plot to give an insight in how the DSP process ran")
-    labels: List[StrictStr] = Field(..., description="Labels of the feature axes")
+    labels: Optional[List[StrictStr]] = Field(None, description="Labels of the feature axes")
     performance: Optional[DspRunResponseAllOfPerformance] = None
     __properties = ["features", "graphs", "labels", "performance"]
 
     class Config:
         allow_population_by_field_name = True
         validate_assignment = True
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_response_all_of_performance.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_response_all_of_performance.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_response_with_sample.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_response_with_sample.py`

 * *Files 2% similar despite different names*

```diff
@@ -24,15 +24,15 @@
 from edgeimpulse_api.models.raw_sample_data import RawSampleData
 
 class DspRunResponseWithSample(BaseModel):
     success: StrictBool = Field(..., description="Whether the operation succeeded")
     error: Optional[StrictStr] = Field(None, description="Optional error description (set if 'success' was false)")
     features: List[float] = Field(..., description="Array of processed features. Laid out according to the names in 'labels'")
     graphs: List[DspRunGraph] = Field(..., description="Graphs to plot to give an insight in how the DSP process ran")
-    labels: List[StrictStr] = Field(..., description="Labels of the feature axes")
+    labels: Optional[List[StrictStr]] = Field(None, description="Labels of the feature axes")
     sample: RawSampleData = ...
     performance: Optional[DspRunResponseAllOfPerformance] = None
     can_profile_performance: StrictBool = Field(..., alias="canProfilePerformance")
     __properties = ["success", "error", "features", "graphs", "labels", "sample", "performance", "canProfilePerformance"]
 
     class Config:
         allow_population_by_field_name = True
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_run_response_with_sample_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_run_response_with_sample_all_of.py`

 * *Files 4% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 from edgeimpulse_api.models.dsp_run_graph import DspRunGraph
 from edgeimpulse_api.models.dsp_run_response_all_of_performance import DspRunResponseAllOfPerformance
 from edgeimpulse_api.models.raw_sample_data import RawSampleData
 
 class DspRunResponseWithSampleAllOf(BaseModel):
     features: List[float] = Field(..., description="Array of processed features. Laid out according to the names in 'labels'")
     graphs: List[DspRunGraph] = Field(..., description="Graphs to plot to give an insight in how the DSP process ran")
-    labels: List[StrictStr] = Field(..., description="Labels of the feature axes")
+    labels: Optional[List[StrictStr]] = Field(None, description="Labels of the feature axes")
     sample: RawSampleData = ...
     performance: Optional[DspRunResponseAllOfPerformance] = None
     can_profile_performance: StrictBool = Field(..., alias="canProfilePerformance")
     __properties = ["features", "graphs", "labels", "sample", "performance", "canProfilePerformance"]
 
     class Config:
         allow_population_by_field_name = True
```

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_sample_features_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_sample_features_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_sample_features_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_sample_features_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_sample_features_response_all_of_data.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_sample_features_response_all_of_data.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_sample_features_response_all_of_sample.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_sample_features_response_all_of_sample.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_trained_features_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_trained_features_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_trained_features_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_trained_features_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_trained_features_response_all_of_data.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_trained_features_response_all_of_data.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/dsp_trained_features_response_all_of_sample.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/dsp_trained_features_response_all_of_sample.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/edit_sample_label_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/edit_sample_label_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/evaluate_job_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/evaluate_job_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/evaluate_job_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/evaluate_job_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/evaluate_result_value.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/evaluate_result_value.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/export_get_url_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/export_get_url_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/export_get_url_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/export_get_url_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/export_original_data_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/export_original_data_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/export_wav_data_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/export_wav_data_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_segment_sample_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_segment_sample_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_segment_sample_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_segment_sample_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_segment_sample_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_segment_sample_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_segment_sample_response_all_of_segments.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_segment_sample_response_all_of_segments.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_user_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_user_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_user_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_user_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/find_user_response_all_of_users.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/find_user_response_all_of_users.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/generate_features_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/generate_features_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/generic_api_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/generic_api_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_all_third_party_auth_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_all_third_party_auth_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_all_third_party_auth_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_all_third_party_auth_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_all_whitelabels_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_all_whitelabels_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_all_whitelabels_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_all_whitelabels_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_data_explorer_features_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_data_explorer_features_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_data_explorer_features_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_data_explorer_features_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_data_explorer_settings_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_data_explorer_settings_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_data_explorer_settings_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_data_explorer_settings_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_deployment_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_deployment_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_deployment_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_deployment_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_device_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_device_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_device_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_device_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_impulse_blocks_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_impulse_blocks_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_impulse_blocks_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_impulse_blocks_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_impulse_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_impulse_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_impulse_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_impulse_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_job_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_job_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_job_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_job_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_jwt_token_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_jwt_token_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_jwt_token_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_jwt_token_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_jwt_token_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_jwt_token_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_last_deployment_build_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_last_deployment_build_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_last_deployment_build_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_last_deployment_build_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_last_deployment_build_response_all_of_last_build.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_last_deployment_build_response_all_of_last_build.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_notes_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_notes_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_notes_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_notes_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_data_item_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_data_item_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_data_item_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_data_item_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_dataset_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_dataset_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_dataset_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_dataset_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_pipelines_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_pipelines_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_pipelines_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_pipelines_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_portal_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_portal_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_portal_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_portal_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_organization_projects_data_count_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_organization_projects_data_count_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_ground_truth_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_ground_truth_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_ground_truth_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_ground_truth_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_parameter_sets_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_parameter_sets_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_parameter_sets_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_parameter_sets_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_parameters_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_parameters_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_parameters_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_parameters_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_raw_result_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_raw_result_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_raw_result_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_raw_result_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_status_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_status_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_performance_calibration_status_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_performance_calibration_status_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_pretrained_model_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_pretrained_model_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_pretrained_model_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_pretrained_model_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_pretrained_model_response_all_of_model.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_pretrained_model_response_all_of_model.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_pretrained_model_response_all_of_model_info.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_pretrained_model_response_all_of_model_info.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_pretrained_model_response_all_of_model_profile_info.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_pretrained_model_response_all_of_model_profile_info.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_public_metrics_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_public_metrics_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_public_metrics_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_public_metrics_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_sample_metadata_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_sample_metadata_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_sample_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_sample_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_syntiant_posterior_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_syntiant_posterior_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_syntiant_posterior_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_syntiant_posterior_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_theme_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_theme_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_theme_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_theme_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_themes_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_themes_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_themes_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_themes_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_third_party_auth_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_third_party_auth_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_third_party_auth_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_third_party_auth_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_user_need_to_set_password_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_user_need_to_set_password_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_user_need_to_set_password_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_user_need_to_set_password_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_user_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_user_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_user_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_user_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_user_response_all_of_whitelabels.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_user_response_all_of_whitelabels.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_whitelabel_domain_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_whitelabel_domain_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_whitelabel_domain_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_whitelabel_domain_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_whitelabel_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_whitelabel_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/get_whitelabel_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/get_whitelabel_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/has_data_explorer_features_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/has_data_explorer_features_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/has_data_explorer_features_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/has_data_explorer_features_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse_block_version.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse_block_version.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse_dsp_block.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse_dsp_block.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse_dsp_block_organization.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse_dsp_block_organization.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse_input_block.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse_input_block.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/impulse_learn_block.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/impulse_learn_block.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/input_block.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/input_block.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/invite_organization_member_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/invite_organization_member_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/job.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/job.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/job_summary_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/job_summary_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/job_summary_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/job_summary_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/job_summary_response_all_of_summary.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/job_summary_response_all_of_summary.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_layer.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_layer.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_layer_input.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_layer_input.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_layer_output.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_layer_output.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_metadata.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_metadata.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_metadata_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_metadata_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_metadata_metrics.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_metadata_metrics.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_metadata_metrics_on_device_performance_inner.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_metadata_metrics_on_device_performance_inner.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_metadata_metrics_on_device_performance_inner_tflite.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_metadata_metrics_on_device_performance_inner_tflite.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_model_type_enum.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_model_type_enum.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_visual_layer.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_visual_layer.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/keras_visual_layer_type.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/keras_visual_layer_type.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/last_modification_date_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/last_modification_date_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/last_modification_date_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/last_modification_date_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/latency_device.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/latency_device.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/learn_block.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/learn_block.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/learn_block_type.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/learn_block_type.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_api_keys_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_api_keys_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_api_keys_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_api_keys_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_api_keys_response_all_of_api_keys.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_api_keys_response_all_of_api_keys.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_devices_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_devices_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_devices_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_devices_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_email_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_email_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_email_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_email_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_email_response_all_of_emails.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_email_response_all_of_emails.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_hmac_keys_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_hmac_keys_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_hmac_keys_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_hmac_keys_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_hmac_keys_response_all_of_hmac_keys.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_hmac_keys_response_all_of_hmac_keys.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_jobs_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_jobs_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_jobs_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_jobs_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_models_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_models_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_models_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_models_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_api_keys_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_api_keys_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_api_keys_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_api_keys_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_api_keys_response_all_of_api_keys.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_api_keys_response_all_of_api_keys.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_response_all_of_buckets.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_response_all_of_buckets.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_user_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_user_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_user_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_user_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_buckets_user_response_all_of_buckets.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_buckets_user_response_all_of_buckets.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_data_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_data_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_data_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_data_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_data_response_all_of_data.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_data_response_all_of_data.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_deploy_blocks_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_deploy_blocks_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_deploy_blocks_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_deploy_blocks_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_dsp_blocks_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_dsp_blocks_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_dsp_blocks_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_dsp_blocks_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_files_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_files_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_files_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_files_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_pipelines_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_pipelines_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_pipelines_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_pipelines_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_portals_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_portals_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_portals_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_portals_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_portals_response_all_of_portals.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_portals_response_all_of_portals.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_projects_data_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_projects_data_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_projects_data_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_projects_data_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_projects_data_response_all_of_projects.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_projects_data_response_all_of_projects.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_projects_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_projects_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_projects_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_projects_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_secrets_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_secrets_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_secrets_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_secrets_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_secrets_response_all_of_secrets.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_secrets_response_all_of_secrets.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_transfer_learning_blocks_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_transfer_learning_blocks_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_transfer_learning_blocks_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_transfer_learning_blocks_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_transformation_blocks_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_transformation_blocks_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organization_transformation_blocks_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organization_transformation_blocks_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organizations_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organizations_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_organizations_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_organizations_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_portal_files_in_folder_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_portal_files_in_folder_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_portal_files_in_folder_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_portal_files_in_folder_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_portal_files_in_folder_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_portal_files_in_folder_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_projects.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_projects.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_projects_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_projects_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_public_projects.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_public_projects.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_public_projects_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_public_projects_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_public_versions_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_public_versions_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_public_versions_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_public_versions_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_public_versions_response_all_of_versions.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_public_versions_response_all_of_versions.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_samples_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_samples_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_samples_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_samples_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_versions_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_versions_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_versions_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_versions_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_versions_response_all_of_bucket.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_versions_response_all_of_bucket.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_versions_response_all_of_custom_learn_blocks.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_versions_response_all_of_custom_learn_blocks.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/list_versions_response_all_of_versions.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/list_versions_response_all_of_versions.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/log_stdout_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/log_stdout_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/log_stdout_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/log_stdout_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/log_stdout_response_all_of_stdout.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/log_stdout_response_all_of_stdout.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/log_website_pageview_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/log_website_pageview_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/login_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/login_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/login_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/login_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/model_prediction.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/model_prediction.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/model_variant_stats.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/model_variant_stats.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/move_raw_data_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/move_raw_data_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/note.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/note.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_auto_label_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_auto_label_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_auto_label_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_auto_label_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_auto_label_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_auto_label_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_auto_label_response_all_of_results.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_auto_label_response_all_of_results.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_label_queue_count_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_label_queue_count_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_label_queue_count_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_label_queue_count_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_label_queue_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_label_queue_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_label_queue_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_label_queue_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/object_detection_last_layer.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/object_detection_last_layer.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_config.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_config.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_config_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_config_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_config_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_config_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_config_target_device.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_config_target_device.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_dsp_parameters_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_dsp_parameters_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_dsp_parameters_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_dsp_parameters_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_space_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_space_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_space_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_space_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_state_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_state_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_state_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_state_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_state_response_all_of_status.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_state_response_all_of_status.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_state_response_all_of_workers.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_state_response_all_of_workers.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_transfer_learning_models_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_transfer_learning_models_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_transfer_learning_models_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_transfer_learning_models_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/optimize_transfer_learning_models_response_all_of_models.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/optimize_transfer_learning_models_response_all_of_models.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_add_data_folder_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_add_data_folder_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_add_data_folder_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_add_data_folder_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_add_data_folder_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_add_data_folder_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_status_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_status_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_status_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_status_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_transformation_summary.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_transformation_summary.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_with_files.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_with_files.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_with_files_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_with_files_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_create_project_with_files_all_of_files.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_create_project_with_files_all_of_files.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_data_item.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_data_item.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_data_item_files_inner.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_data_item_files_inner.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_dataset.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_dataset.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_deploy_block.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_deploy_block.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_dsp_block.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_dsp_block.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_get_create_projects_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_get_create_projects_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_get_create_projects_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_get_create_projects_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_get_create_projects_response_all_of_jobs.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_get_create_projects_response_all_of_jobs.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_info_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_info_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_info_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_info_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_info_response_all_of_default_compute_limits.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_info_response_all_of_default_compute_limits.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_info_response_all_of_entitlement_limits.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_info_response_all_of_entitlement_limits.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_metrics_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_metrics_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_metrics_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_metrics_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_metrics_response_all_of_metrics.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_metrics_response_all_of_metrics.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_feeding_into_dataset.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_feeding_into_dataset.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_feeding_into_project.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_feeding_into_project.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_item_count.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_item_count.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_run.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_run.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_run_step.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_run_step.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_pipeline_step.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_pipeline_step.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_projects_data_batch_disable_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_projects_data_batch_disable_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_projects_data_batch_enable_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_projects_data_batch_enable_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_projects_data_batch_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_projects_data_batch_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_transfer_learning_block.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_transfer_learning_block.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_transfer_learning_operates_on.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_transfer_learning_operates_on.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_transformation_block.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_transformation_block.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_update_pipeline_body.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_update_pipeline_body.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/organization_user.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/organization_user.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_detection.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_detection.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_false_positive.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_false_positive.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_ground_truth.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_ground_truth.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_ground_truth_samples_inner.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_ground_truth_samples_inner.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_parameter_set.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_parameter_set.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_parameter_set_aggregate_stats.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_parameter_set_aggregate_stats.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_parameter_set_stats_inner.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_parameter_set_stats_inner.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_parameters.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_parameters.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_parameters_standard.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_parameters_standard.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_raw_detection.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_raw_detection.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_save_parameter_set_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_save_parameter_set_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_upload_labeled_audio_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_upload_labeled_audio_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/performance_calibration_upload_labeled_audio_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/performance_calibration_upload_labeled_audio_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/portal_file.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/portal_file.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/portal_info_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/portal_info_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/pretrained_model_tensor.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/pretrained_model_tensor.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_info.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_info.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_info_memory.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_info_memory.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_info_memory_eon.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_info_memory_eon.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_info_memory_tflite.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_info_memory_tflite.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_table.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_table.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_table_mcu.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_table_mcu.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_table_mcu_memory.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_table_mcu_memory.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_model_table_mpu.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_model_table_mpu.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_tf_lite_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_tf_lite_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/profile_tf_lite_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/profile_tf_lite_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_collaborator.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_collaborator.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_collaborator_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_collaborator_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_data_axes_summary_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_data_axes_summary_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_data_axes_summary_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_data_axes_summary_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_data_interval_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_data_interval_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_data_interval_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_data_interval_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_data_summary.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_data_summary.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_deployment_target.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_deployment_target.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_deployment_target_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_deployment_target_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_deployment_targets_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_deployment_targets_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_deployment_targets_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_deployment_targets_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_downloads_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_downloads_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_downloads_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_downloads_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_acquisition_settings.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_acquisition_settings.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_compute_time.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_compute_time.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_data_summary_per_category.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_data_summary_per_category.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_deploy_settings.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_deploy_settings.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_experiments.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_experiments.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_impulse.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_impulse.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_performance.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_performance.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_readme.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_readme.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_show_getting_started_wizard.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_show_getting_started_wizard.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_response_all_of_urls.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_response_all_of_urls.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_summary_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_summary_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_info_summary_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_info_summary_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_private_data.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_private_data.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_public_data.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_public_data.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_public_data_readme.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_public_data_readme.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_sample_metadata.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_sample_metadata.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/project_version_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/project_version_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/raw_sample_data.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/raw_sample_data.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/raw_sample_payload.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/raw_sample_payload.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/rebalance_dataset_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/rebalance_dataset_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/remove_collaborator_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/remove_collaborator_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/remove_member_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/remove_member_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/rename_device_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/rename_device_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/rename_portal_file_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/rename_portal_file_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/rename_sample_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/rename_sample_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/request_reset_password_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/request_reset_password_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/reset_password_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/reset_password_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/restore_project_from_public_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/restore_project_from_public_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/restore_project_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/restore_project_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/run_organization_pipeline_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/run_organization_pipeline_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/run_organization_pipeline_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/run_organization_pipeline_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/sample.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/sample.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/sample_bounding_boxes_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/sample_bounding_boxes_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/sample_metadata.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/sample_metadata.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/save_pretrained_model_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/save_pretrained_model_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/score_trial_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/score_trial_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/score_trial_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/score_trial_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/score_trial_response_all_of_latency.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/score_trial_response_all_of_latency.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/score_trial_response_all_of_ram.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/score_trial_response_all_of_ram.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/segment_sample_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/segment_sample_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/segment_sample_request_segments_inner.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/segment_sample_request_segments_inner.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/send_user_feedback_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/send_user_feedback_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/sensor.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/sensor.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_anomaly_parameter_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_anomaly_parameter_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_keras_parameter_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_keras_parameter_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_member_datasets_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_member_datasets_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_member_role_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_member_role_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_optimize_space_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_optimize_space_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_optimize_space_request_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_optimize_space_request_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_organization_data_dataset_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_organization_data_dataset_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_project_compute_time_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_project_compute_time_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_project_dsp_file_size_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_project_dsp_file_size_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_sample_metadata_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_sample_metadata_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_syntiant_posterior_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_syntiant_posterior_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/set_user_password_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/set_user_password_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/socket_token_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/socket_token_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/socket_token_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/socket_token_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/socket_token_response_all_of_token.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/socket_token_response_all_of_token.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/split_sample_in_frames_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/split_sample_in_frames_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/staff_info.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/staff_info.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_job_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_job_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_job_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_job_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_performance_calibration_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_performance_calibration_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_sampling_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_sampling_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_sampling_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_sampling_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_sampling_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_sampling_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/start_training_request_anomaly.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/start_training_request_anomaly.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/store_segment_length_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/store_segment_length_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/structured_classify_result.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/structured_classify_result.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/test_pretrained_model_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/test_pretrained_model_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/test_pretrained_model_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/test_pretrained_model_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/test_pretrained_model_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/test_pretrained_model_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/theme.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/theme.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/theme_colors.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/theme_colors.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/theme_favicon.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/theme_favicon.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/theme_logos.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/theme_logos.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/third_party_auth.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/third_party_auth.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/track_objects_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/track_objects_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/track_objects_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/track_objects_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/track_objects_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/track_objects_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/transfer_learning_model.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/transfer_learning_model.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/transfer_ownership_organization_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/transfer_ownership_organization_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/transformation_block_additional_mount_point.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/transformation_block_additional_mount_point.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/transformation_job_status_enum.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/transformation_job_status_enum.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/tuner_create_trial_impulse.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/tuner_create_trial_impulse.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/tuner_space_impulse.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/tuner_space_impulse.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/tuner_trial.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/tuner_trial.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/tuner_trial_blocks_inner.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/tuner_trial_blocks_inner.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_job_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_job_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_add_collaborator_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_add_collaborator_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_bucket_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_bucket_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_create_empty_project_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_create_empty_project_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_create_project_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_create_project_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_data_item_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_data_item_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_dataset_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_dataset_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_dsp_block_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_dsp_block_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_portal_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_portal_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_portal_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_portal_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_transfer_learning_block_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_transfer_learning_block_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_organization_transformation_block_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_organization_transformation_block_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_project_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_project_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_project_tags_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_project_tags_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_theme_colors_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_theme_colors_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_theme_logos_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_theme_logos_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_third_party_auth_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_third_party_auth_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_user_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_user_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_version_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_version_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/update_whitelabel_deployment_targets_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/update_whitelabel_deployment_targets_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/upload_asset_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/upload_asset_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/upload_asset_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/upload_asset_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/upload_readme_image_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/upload_readme_image_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/upload_user_photo_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/upload_user_photo_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/upload_user_photo_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/upload_user_photo_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/user.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/user.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/user_by_third_party_activation_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/user_by_third_party_activation_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/user_experiment.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/user_experiment.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/user_organization.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/user_organization.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_dsp_block_url_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_dsp_block_url_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_dsp_block_url_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_dsp_block_url_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_dsp_block_url_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_dsp_block_url_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_dsp_block_url_response_all_of_block.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_dsp_block_url_response_all_of_block.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_organization_bucket_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_organization_bucket_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_organization_bucket_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_organization_bucket_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_organization_bucket_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_organization_bucket_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_organization_bucket_response_all_of_files.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_organization_bucket_response_all_of_files.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/verify_reset_password_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/verify_reset_password_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/whitelabel.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/whitelabel.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/whitelabel_admin_create_organization_request.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/whitelabel_admin_create_organization_request.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/window_settings_response.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/window_settings_response.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/window_settings_response_all_of.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/window_settings_response_all_of.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/models/window_settings_response_all_of_window_settings.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/models/window_settings_response_all_of_window_settings.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/edgeimpulse_api/rest.py` & `edgeimpulse_api-1.22.1/edgeimpulse_api/rest.py`

 * *Files identical despite different names*

### Comparing `edgeimpulse_api-1.22.0/pyproject.toml` & `edgeimpulse_api-1.22.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "edgeimpulse-api"
-version = "1.22.0" #DO_NOT_CHANGE_REPLACED_BY_BUILD_SCRIPT
+version = "1.22.1" #DO_NOT_CHANGE_REPLACED_BY_BUILD_SCRIPT
 description = "Python bindings for the Edge Impulse API."
 authors = ["EdgeImpulse Inc. <hello@edgeimpulse.com>"]
 license = "Apache-2.0"
 homepage = "https://edgeimpulse.com"
 documentation = "https://docs.edgeimpulse.com/reference/edge-impulse-api/edge-impulse-api"
 classifiers = [
     "Topic :: Scientific/Engineering :: Artificial Intelligence",
```

### Comparing `edgeimpulse_api-1.22.0/PKG-INFO` & `edgeimpulse_api-1.22.1/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: edgeimpulse-api
-Version: 1.22.0
+Version: 1.22.1
 Summary: Python bindings for the Edge Impulse API.
 Home-page: https://edgeimpulse.com
 License: Apache-2.0
 Author: EdgeImpulse Inc.
 Author-email: hello@edgeimpulse.com
 Requires-Python: >=3.7,<4.0
 Classifier: License :: OSI Approved :: Apache Software License
```

