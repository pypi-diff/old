# Comparing `tmp/netsuite_python-1.2.3.tar.gz` & `tmp/netsuite_python-1.2.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "netsuite_python-1.2.3.tar", last modified: Mon Feb 27 17:54:43 2023, max compression
+gzip compressed data, was "netsuite_python-1.2.4.tar", last modified: Thu Apr  6 19:33:55 2023, max compression
```

## Comparing `netsuite_python-1.2.3.tar` & `netsuite_python-1.2.4.tar`

### file list

```diff
@@ -1,97 +1,99 @@
-drwxrwxrwx   0        0        0        0 2023-02-27 17:54:43.844761 netsuite_python-1.2.3/
--rw-rw-rw-   0        0        0    11792 2023-02-27 17:54:43.844761 netsuite_python-1.2.3/PKG-INFO
--rw-rw-rw-   0        0        0    11461 2023-02-01 21:44:48.000000 netsuite_python-1.2.3/README.md
-drwxrwxrwx   0        0        0        0 2023-02-27 17:54:43.782362 netsuite_python-1.2.3/netsuite/
--rw-rw-rw-   0        0        0     6534 2023-02-20 19:06:16.000000 netsuite_python-1.2.3/netsuite/Netsuite.py
--rw-rw-rw-   0        0        0      494 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/NetsuiteToken.py
--rw-rw-rw-   0        0        0       74 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/__init__.py
--rw-rw-rw-   0        0        0      243 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/exceptions.py
--rw-rw-rw-   0        0        0     3921 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/module_loading.py
-drwxrwxrwx   0        0        0        0 2023-02-27 17:54:43.783362 netsuite_python-1.2.3/netsuite/scripts/
--rw-rw-rw-   0        0        0        0 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/scripts/__init__.py
--rw-rw-rw-   0        0        0     5255 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/scripts/cli.py
--rw-rw-rw-   0        0        0     5387 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/settings.py
-drwxrwxrwx   0        0        0        0 2023-02-27 17:54:43.786362 netsuite_python-1.2.3/netsuite/storages/
--rw-rw-rw-   0        0        0      324 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/storages/BaseStorage.py
--rw-rw-rw-   0        0        0      653 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/storages/InMemoryStorage.py
--rw-rw-rw-   0        0        0     1594 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/storages/JSONStorage.py
--rw-rw-rw-   0        0        0      119 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/storages/__init__.py
-drwxrwxrwx   0        0        0        0 2023-02-27 17:54:43.790362 netsuite_python-1.2.3/netsuite/swagger_client/
--rw-rw-rw-   0        0        0     7014 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/__init__.py
-drwxrwxrwx   0        0        0        0 2023-02-27 17:54:43.794362 netsuite_python-1.2.3/netsuite/swagger_client/api/
--rw-rw-rw-   0        0        0      286 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/api/__init__.py
--rw-rw-rw-   0        0        0    39267 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/api/contact_api.py
--rw-rw-rw-   0        0        0    68525 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/api/customer_api.py
--rw-rw-rw-   0        0        0    40005 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/api/message_api.py
--rw-rw-rw-   0        0        0     5582 2023-02-27 17:54:28.000000 netsuite_python-1.2.3/netsuite/swagger_client/api/query_api.py
--rw-rw-rw-   0        0        0    25621 2023-02-17 17:39:39.000000 netsuite_python-1.2.3/netsuite/swagger_client/api_client.py
--rw-rw-rw-   0        0        0     8466 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/configuration.py
-drwxrwxrwx   0        0        0        0 2023-02-27 17:54:43.839363 netsuite_python-1.2.3/netsuite/swagger_client/models/
--rw-rw-rw-   0        0        0     6150 2023-02-13 16:56:23.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/__init__.py
--rw-rw-rw-   0        0        0   124906 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/contact.py
--rw-rw-rw-   0        0        0     6811 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/contact_collection.py
--rw-rw-rw-   0        0        0     4007 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/contact_custom_form.py
--rw-rw-rw-   0        0        0   499116 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer.py
--rw-rw-rw-   0        0        0    15732 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_address_book_address_book_address.py
--rw-rw-rw-   0        0        0     6914 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_address_book_collection.py
--rw-rw-rw-   0        0        0    11388 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_address_book_element.py
--rw-rw-rw-   0        0        0     4156 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_alcohol_recipient_type.py
--rw-rw-rw-   0        0        0     6852 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_campaigns_collection.py
--rw-rw-rw-   0        0        0     3925 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_campaigns_element.py
--rw-rw-rw-   0        0        0     6842 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_collection.py
--rw-rw-rw-   0        0        0     6945 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_contact_roles_collection.py
--rw-rw-rw-   0        0        0     9153 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_contact_roles_element.py
--rw-rw-rw-   0        0        0     4090 2023-02-25 18:03:44.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_custom_form.py
--rw-rw-rw-   0        0        0     4098 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_email_preference.py
--rw-rw-rw-   0        0        0     4200 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_global_subscription_status.py
--rw-rw-rw-   0        0        0     6945 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_group_pricing_collection.py
--rw-rw-rw-   0        0        0     5317 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_group_pricing_element.py
--rw-rw-rw-   0        0        0     6914 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_item_pricing_collection.py
--rw-rw-rw-   0        0        0     6011 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_item_pricing_element.py
--rw-rw-rw-   0        0        0     4558 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_language.py
--rw-rw-rw-   0        0        0     4142 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_negative_number_format.py
--rw-rw-rw-   0        0        0     4066 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_number_format.py
--rw-rw-rw-   0        0        0     4089 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_shipping_carrier.py
--rw-rw-rw-   0        0        0     4082 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_symbol_placement.py
--rw-rw-rw-   0        0        0     4120 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customer_third_party_carrier.py
--rw-rw-rw-   0        0        0     5848 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/customeraddress_bookaddress_book_address_country.py
--rw-rw-rw-   0        0        0    22360 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/message.py
--rw-rw-rw-   0        0        0     7064 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/message_collection.py
--rw-rw-rw-   0        0        0     5678 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/ns_error.py
--rw-rw-rw-   0        0        0     8174 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/ns_error_oerror_details.py
--rw-rw-rw-   0        0        0     3563 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/ns_link.py
--rw-rw-rw-   0        0        0     4994 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/ns_resource.py
--rw-rw-rw-   0        0        0     6614 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/ns_resource_collection.py
--rw-rw-rw-   0        0        0     2531 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_company.py
--rw-rw-rw-   0        0        0     2599 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_course_attended.py
--rw-rw-rw-   0        0        0     2611 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_energy_eff_attended.py
--rw-rw-rw-   0        0        0     2627 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_hitachi_course_attended.py
--rw-rw-rw-   0        0        0     2607 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_hp_course_attended.py
--rw-rw-rw-   0        0        0     2611 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_pv_course_atteneded.py
--rw-rw-rw-   0        0        0     2611 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_sol_course_attended.py
--rw-rw-rw-   0        0        0     2607 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_unvent_hot_water_g3.py
--rw-rw-rw-   0        0        0     2623 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_water_regulations1999.py
--rw-rw-rw-   0        0        0     2603 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_course_attended.py
--rw-rw-rw-   0        0        0     2615 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_energy_eff_attended.py
--rw-rw-rw-   0        0        0     2631 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_hitachi_course_attended.py
--rw-rw-rw-   0        0        0     2611 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_hp_course_attended.py
--rw-rw-rw-   0        0        0     2615 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_pv_course_atteneded.py
--rw-rw-rw-   0        0        0     2615 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_sol_course_attended.py
--rw-rw-rw-   0        0        0     2611 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_unvent_hot_water_g3.py
--rw-rw-rw-   0        0        0     2627 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_water_regulations1999.py
--rw-rw-rw-   0        0        0     2595 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_item_pricing_element_item.py
--rw-rw-rw-   0        0        0     2622 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofmessage_author.py
--rw-rw-rw-   0        0        0     2622 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofmessage_entity.py
--rw-rw-rw-   0        0        0     2662 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofmessage_primary_recipient.py
--rw-rw-rw-   0        0        0     2634 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofmessage_recipient.py
--rw-rw-rw-   0        0        0    13258 2023-02-12 19:28:31.000000 netsuite_python-1.2.3/netsuite/swagger_client/rest.py
--rw-rw-rw-   0        0        0     1823 2023-02-25 19:42:59.000000 netsuite_python-1.2.3/netsuite/swagger_client/rest_client.py
-drwxrwxrwx   0        0        0        0 2023-02-27 17:54:43.843349 netsuite_python-1.2.3/netsuite_python.egg-info/
--rw-rw-rw-   0        0        0    11792 2023-02-27 17:54:43.000000 netsuite_python-1.2.3/netsuite_python.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     4667 2023-02-27 17:54:43.000000 netsuite_python-1.2.3/netsuite_python.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-02-27 17:54:43.000000 netsuite_python-1.2.3/netsuite_python.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       55 2023-02-27 17:54:43.000000 netsuite_python-1.2.3/netsuite_python.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       79 2023-02-27 17:54:43.000000 netsuite_python-1.2.3/netsuite_python.egg-info/requires.txt
--rw-rw-rw-   0        0        0        9 2023-02-27 17:54:43.000000 netsuite_python-1.2.3/netsuite_python.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-02-27 17:54:43.844761 netsuite_python-1.2.3/setup.cfg
--rw-rw-rw-   0        0        0      959 2023-02-27 17:54:37.000000 netsuite_python-1.2.3/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:55.221751 netsuite_python-1.2.4/
+-rw-rw-rw-   0        0        0    11792 2023-04-06 19:33:55.221751 netsuite_python-1.2.4/PKG-INFO
+-rw-rw-rw-   0        0        0    11461 2023-02-01 21:44:48.000000 netsuite_python-1.2.4/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:55.079815 netsuite_python-1.2.4/netsuite/
+-rw-rw-rw-   0        0        0     6813 2023-04-06 19:31:47.000000 netsuite_python-1.2.4/netsuite/Netsuite.py
+-rw-rw-rw-   0        0        0      494 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/NetsuiteToken.py
+-rw-rw-rw-   0        0        0       74 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/__init__.py
+-rw-rw-rw-   0        0        0      243 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/exceptions.py
+-rw-rw-rw-   0        0        0     3921 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/module_loading.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:55.082815 netsuite_python-1.2.4/netsuite/scripts/
+-rw-rw-rw-   0        0        0        0 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/scripts/__init__.py
+-rw-rw-rw-   0        0        0     5255 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/scripts/cli.py
+-rw-rw-rw-   0        0        0     5387 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/settings.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:55.088815 netsuite_python-1.2.4/netsuite/storages/
+-rw-rw-rw-   0        0        0      324 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/storages/BaseStorage.py
+-rw-rw-rw-   0        0        0      653 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/storages/InMemoryStorage.py
+-rw-rw-rw-   0        0        0     1594 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/storages/JSONStorage.py
+-rw-rw-rw-   0        0        0      119 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/storages/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:55.099815 netsuite_python-1.2.4/netsuite/swagger_client/
+-rw-rw-rw-   0        0        0     7078 2023-04-06 19:32:28.000000 netsuite_python-1.2.4/netsuite/swagger_client/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:55.110816 netsuite_python-1.2.4/netsuite/swagger_client/api/
+-rw-rw-rw-   0        0        0      350 2023-04-06 19:32:00.000000 netsuite_python-1.2.4/netsuite/swagger_client/api/__init__.py
+-rw-rw-rw-   0        0        0    39267 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/api/contact_api.py
+-rw-rw-rw-   0        0        0    68525 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/api/customer_api.py
+-rw-rw-rw-   0        0        0    40005 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/api/message_api.py
+-rw-rw-rw-   0        0        0     5582 2023-02-27 17:54:28.000000 netsuite_python-1.2.4/netsuite/swagger_client/api/query_api.py
+-rw-rw-rw-   0        0        0     2289 2023-04-06 18:45:16.000000 netsuite_python-1.2.4/netsuite/swagger_client/api/restlet_api.py
+-rw-rw-rw-   0        0        0    25621 2023-02-17 17:39:39.000000 netsuite_python-1.2.4/netsuite/swagger_client/api_client.py
+-rw-rw-rw-   0        0        0     8466 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/configuration.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:55.215750 netsuite_python-1.2.4/netsuite/swagger_client/models/
+-rw-rw-rw-   0        0        0     6150 2023-02-13 16:56:23.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/__init__.py
+-rw-rw-rw-   0        0        0   124906 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/contact.py
+-rw-rw-rw-   0        0        0     6811 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/contact_collection.py
+-rw-rw-rw-   0        0        0     4007 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/contact_custom_form.py
+-rw-rw-rw-   0        0        0   499116 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer.py
+-rw-rw-rw-   0        0        0    15732 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_address_book_address_book_address.py
+-rw-rw-rw-   0        0        0     6914 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_address_book_collection.py
+-rw-rw-rw-   0        0        0    11388 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_address_book_element.py
+-rw-rw-rw-   0        0        0     4156 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_alcohol_recipient_type.py
+-rw-rw-rw-   0        0        0     6852 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_campaigns_collection.py
+-rw-rw-rw-   0        0        0     3925 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_campaigns_element.py
+-rw-rw-rw-   0        0        0     6842 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_collection.py
+-rw-rw-rw-   0        0        0     6945 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_contact_roles_collection.py
+-rw-rw-rw-   0        0        0     9153 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_contact_roles_element.py
+-rw-rw-rw-   0        0        0     4090 2023-02-25 18:03:44.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_custom_form.py
+-rw-rw-rw-   0        0        0     4098 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_email_preference.py
+-rw-rw-rw-   0        0        0     4200 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_global_subscription_status.py
+-rw-rw-rw-   0        0        0     6945 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_group_pricing_collection.py
+-rw-rw-rw-   0        0        0     5317 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_group_pricing_element.py
+-rw-rw-rw-   0        0        0     6914 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_item_pricing_collection.py
+-rw-rw-rw-   0        0        0     6011 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_item_pricing_element.py
+-rw-rw-rw-   0        0        0     4558 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_language.py
+-rw-rw-rw-   0        0        0     4142 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_negative_number_format.py
+-rw-rw-rw-   0        0        0     4066 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_number_format.py
+-rw-rw-rw-   0        0        0     4089 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_shipping_carrier.py
+-rw-rw-rw-   0        0        0     4082 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_symbol_placement.py
+-rw-rw-rw-   0        0        0     4120 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customer_third_party_carrier.py
+-rw-rw-rw-   0        0        0     5848 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/customeraddress_bookaddress_book_address_country.py
+-rw-rw-rw-   0        0        0    22360 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/message.py
+-rw-rw-rw-   0        0        0     7064 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/message_collection.py
+-rw-rw-rw-   0        0        0     5678 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/ns_error.py
+-rw-rw-rw-   0        0        0     8174 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/ns_error_oerror_details.py
+-rw-rw-rw-   0        0        0     3563 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/ns_link.py
+-rw-rw-rw-   0        0        0     4994 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/ns_resource.py
+-rw-rw-rw-   0        0        0     6614 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/ns_resource_collection.py
+-rw-rw-rw-   0        0        0     2531 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_company.py
+-rw-rw-rw-   0        0        0     2599 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_course_attended.py
+-rw-rw-rw-   0        0        0     2611 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_energy_eff_attended.py
+-rw-rw-rw-   0        0        0     2627 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_hitachi_course_attended.py
+-rw-rw-rw-   0        0        0     2607 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_hp_course_attended.py
+-rw-rw-rw-   0        0        0     2611 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_pv_course_atteneded.py
+-rw-rw-rw-   0        0        0     2611 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_sol_course_attended.py
+-rw-rw-rw-   0        0        0     2607 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_unvent_hot_water_g3.py
+-rw-rw-rw-   0        0        0     2623 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_water_regulations1999.py
+-rw-rw-rw-   0        0        0     2603 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_course_attended.py
+-rw-rw-rw-   0        0        0     2615 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_energy_eff_attended.py
+-rw-rw-rw-   0        0        0     2631 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_hitachi_course_attended.py
+-rw-rw-rw-   0        0        0     2611 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_hp_course_attended.py
+-rw-rw-rw-   0        0        0     2615 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_pv_course_atteneded.py
+-rw-rw-rw-   0        0        0     2615 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_sol_course_attended.py
+-rw-rw-rw-   0        0        0     2611 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_unvent_hot_water_g3.py
+-rw-rw-rw-   0        0        0     2627 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_water_regulations1999.py
+-rw-rw-rw-   0        0        0     2595 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_item_pricing_element_item.py
+-rw-rw-rw-   0        0        0     2622 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofmessage_author.py
+-rw-rw-rw-   0        0        0     2622 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofmessage_entity.py
+-rw-rw-rw-   0        0        0     2662 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofmessage_primary_recipient.py
+-rw-rw-rw-   0        0        0     2634 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofmessage_recipient.py
+-rw-rw-rw-   0        0        0    13258 2023-02-12 19:28:31.000000 netsuite_python-1.2.4/netsuite/swagger_client/rest.py
+-rw-rw-rw-   0        0        0     1823 2023-02-25 19:42:59.000000 netsuite_python-1.2.4/netsuite/swagger_client/rest_client.py
+-rw-rw-rw-   0        0        0     1098 2023-04-06 18:22:16.000000 netsuite_python-1.2.4/netsuite/swagger_client/restlet_client.py
+drwxrwxrwx   0        0        0        0 2023-04-06 19:33:55.220750 netsuite_python-1.2.4/netsuite_python.egg-info/
+-rw-rw-rw-   0        0        0    11792 2023-04-06 19:33:54.000000 netsuite_python-1.2.4/netsuite_python.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     4752 2023-04-06 19:33:54.000000 netsuite_python-1.2.4/netsuite_python.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 19:33:54.000000 netsuite_python-1.2.4/netsuite_python.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       55 2023-04-06 19:33:54.000000 netsuite_python-1.2.4/netsuite_python.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       79 2023-04-06 19:33:54.000000 netsuite_python-1.2.4/netsuite_python.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        9 2023-04-06 19:33:54.000000 netsuite_python-1.2.4/netsuite_python.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 19:33:55.221751 netsuite_python-1.2.4/setup.cfg
+-rw-rw-rw-   0        0        0      959 2023-04-06 19:32:57.000000 netsuite_python-1.2.4/setup.py
```

### Comparing `netsuite_python-1.2.3/PKG-INFO` & `netsuite_python-1.2.4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: netsuite_python
-Version: 1.2.3
+Version: 1.2.4
 Summary: Python SDK for Netsuite API with Django Integration
 Home-page: https://bitbucket.org/theapiguys/netsuite_python
 Author: Will @ TheAPIGuys
 Author-email: will@theapiguys.com
 License: UNKNOWN
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
```

### Comparing `netsuite_python-1.2.3/README.md` & `netsuite_python-1.2.4/README.md`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/Netsuite.py` & `netsuite_python-1.2.4/netsuite/Netsuite.py`

 * *Files 7% similar despite different names*

```diff
@@ -2,24 +2,26 @@
 import pathlib
 import jwt
 from datetime import datetime, timedelta
 from pathlib import Path
 import requests
 from netsuite.NetsuiteToken import NetsuiteToken
 from netsuite.swagger_client.rest_client import RestClient, QueryClient
+from netsuite.swagger_client.restlet_client import RestletClient
 from netsuite.settings import APISettings
 from netsuite.storages import BaseStorage, JSONStorage
 
 
 class Netsuite:
     app_name: str = None
     storage: BaseStorage = None
     api_settings: APISettings
     rest_client = None
     query_client = None
+    restlet_client = None
 
     def __init__(self, config: dict = None, config_file: Path = None):
         if config and config_file:
             raise ValueError("You can only load settings from one source")
         if config_file:
             with open(config_file, 'r') as f:
                 config = json.load(f)
@@ -69,27 +71,33 @@
             self.query_client = QueryClient(self)
             # if self.token.access_token is not None:
                 # self.get_customer_categories()
                 # self.get_status_dict()
         return self.query_client
 
     @property
+    def RESTLET_CLIENT(self):
+        if not self.restlet_client:
+            self.restlet_client = RestletClient(self)
+        return self.restlet_client
+
+    @property
     def token(self) -> NetsuiteToken:
         return self.storage.get_token(self.app_name)
 
     def save_token(self, token):
         self.storage.save_token(self.app_name, token)
 
     def get_jwt(self):
         private_key = ""
         with open(self.netsuite_key_path, "rb") as pemfile:
             private_key = pemfile.read()
         payload = {
             "iss": f"{self.api_settings.CLIENT_ID}",
-            "scope": "rest_webservices",
+            "scope": "restlets, rest_webservices",
             "aud": f"{self.access_token_url}",
             "exp": (datetime.now() + timedelta(seconds=3600)).timestamp(),
             "iat": datetime.now().timestamp()
         }
 
         headers = {
             "typ": "JWT",
```

### Comparing `netsuite_python-1.2.3/netsuite/module_loading.py` & `netsuite_python-1.2.4/netsuite/module_loading.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/scripts/cli.py` & `netsuite_python-1.2.4/netsuite/scripts/cli.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/settings.py` & `netsuite_python-1.2.4/netsuite/settings.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/storages/InMemoryStorage.py` & `netsuite_python-1.2.4/netsuite/storages/InMemoryStorage.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/storages/JSONStorage.py` & `netsuite_python-1.2.4/netsuite/storages/JSONStorage.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/__init__.py` & `netsuite_python-1.2.4/netsuite/swagger_client/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,14 +15,15 @@
 from __future__ import absolute_import
 
 # import apis into sdk package
 from netsuite.swagger_client.api.contact_api import ContactApi
 from netsuite.swagger_client.api.customer_api import CustomerApi
 from netsuite.swagger_client.api.query_api import QueryApi
 from netsuite.swagger_client.api.message_api import MessageApi
+from netsuite.swagger_client.api.restlet_api import RestletApi
 # import ApiClient
 from netsuite.swagger_client.api_client import ApiClient
 from netsuite.swagger_client.configuration import Configuration
 # import models into sdk package
 from netsuite.swagger_client.models.contact import Contact
 from netsuite.swagger_client.models.contact_collection import ContactCollection
 from netsuite.swagger_client.models.contact_custom_form import ContactCustomForm
```

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/api/contact_api.py` & `netsuite_python-1.2.4/netsuite/swagger_client/api/contact_api.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/api/customer_api.py` & `netsuite_python-1.2.4/netsuite/swagger_client/api/customer_api.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/api/message_api.py` & `netsuite_python-1.2.4/netsuite/swagger_client/api/message_api.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/api/query_api.py` & `netsuite_python-1.2.4/netsuite/swagger_client/api/query_api.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/api_client.py` & `netsuite_python-1.2.4/netsuite/swagger_client/api_client.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/configuration.py` & `netsuite_python-1.2.4/netsuite/swagger_client/configuration.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/__init__.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/__init__.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/contact.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/contact.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/contact_collection.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/contact_collection.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/contact_custom_form.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/contact_custom_form.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_address_book_address_book_address.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_address_book_address_book_address.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_address_book_collection.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_address_book_collection.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_address_book_element.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_address_book_element.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_alcohol_recipient_type.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_alcohol_recipient_type.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_campaigns_collection.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_campaigns_collection.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_campaigns_element.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_campaigns_element.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_collection.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_collection.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_contact_roles_collection.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_contact_roles_collection.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_contact_roles_element.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_contact_roles_element.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_custom_form.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_custom_form.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_email_preference.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_email_preference.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_global_subscription_status.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_global_subscription_status.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_group_pricing_collection.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_group_pricing_collection.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_group_pricing_element.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_group_pricing_element.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_item_pricing_collection.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_item_pricing_collection.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_item_pricing_element.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_item_pricing_element.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_language.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_language.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_negative_number_format.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_negative_number_format.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_number_format.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_number_format.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_shipping_carrier.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_shipping_carrier.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_symbol_placement.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_symbol_placement.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customer_third_party_carrier.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customer_third_party_carrier.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/customeraddress_bookaddress_book_address_country.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/customeraddress_bookaddress_book_address_country.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/message.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/message.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/message_collection.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/message_collection.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/ns_error.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/ns_error.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/ns_error_oerror_details.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/ns_error_oerror_details.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/ns_link.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/ns_link.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/ns_resource.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/ns_resource.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/ns_resource_collection.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/ns_resource_collection.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_company.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_company.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_course_attended.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_course_attended.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_energy_eff_attended.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_energy_eff_attended.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_hitachi_course_attended.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_hitachi_course_attended.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_hp_course_attended.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_hp_course_attended.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_pv_course_atteneded.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_pv_course_atteneded.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_sol_course_attended.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_sol_course_attended.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_unvent_hot_water_g3.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_unvent_hot_water_g3.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcontact_custentity_water_regulations1999.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcontact_custentity_water_regulations1999.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_course_attended.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_course_attended.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_energy_eff_attended.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_energy_eff_attended.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_hitachi_course_attended.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_hitachi_course_attended.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_hp_course_attended.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_hp_course_attended.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_pv_course_atteneded.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_pv_course_atteneded.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_sol_course_attended.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_sol_course_attended.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_unvent_hot_water_g3.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_unvent_hot_water_g3.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_custentity_water_regulations1999.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_custentity_water_regulations1999.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofcustomer_item_pricing_element_item.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofcustomer_item_pricing_element_item.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofmessage_author.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofmessage_author.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofmessage_entity.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofmessage_entity.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofmessage_primary_recipient.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofmessage_primary_recipient.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/models/one_ofmessage_recipient.py` & `netsuite_python-1.2.4/netsuite/swagger_client/models/one_ofmessage_recipient.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/rest.py` & `netsuite_python-1.2.4/netsuite/swagger_client/rest.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite/swagger_client/rest_client.py` & `netsuite_python-1.2.4/netsuite/swagger_client/rest_client.py`

 * *Files identical despite different names*

### Comparing `netsuite_python-1.2.3/netsuite_python.egg-info/PKG-INFO` & `netsuite_python-1.2.4/netsuite_python.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: netsuite-python
-Version: 1.2.3
+Version: 1.2.4
 Summary: Python SDK for Netsuite API with Django Integration
 Home-page: https://bitbucket.org/theapiguys/netsuite_python
 Author: Will @ TheAPIGuys
 Author-email: will@theapiguys.com
 License: UNKNOWN
 Platform: UNKNOWN
 Description-Content-Type: text/markdown
```

### Comparing `netsuite_python-1.2.3/netsuite_python.egg-info/SOURCES.txt` & `netsuite_python-1.2.4/netsuite_python.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -13,19 +13,21 @@
 netsuite/storages/JSONStorage.py
 netsuite/storages/__init__.py
 netsuite/swagger_client/__init__.py
 netsuite/swagger_client/api_client.py
 netsuite/swagger_client/configuration.py
 netsuite/swagger_client/rest.py
 netsuite/swagger_client/rest_client.py
+netsuite/swagger_client/restlet_client.py
 netsuite/swagger_client/api/__init__.py
 netsuite/swagger_client/api/contact_api.py
 netsuite/swagger_client/api/customer_api.py
 netsuite/swagger_client/api/message_api.py
 netsuite/swagger_client/api/query_api.py
+netsuite/swagger_client/api/restlet_api.py
 netsuite/swagger_client/models/__init__.py
 netsuite/swagger_client/models/contact.py
 netsuite/swagger_client/models/contact_collection.py
 netsuite/swagger_client/models/contact_custom_form.py
 netsuite/swagger_client/models/customer.py
 netsuite/swagger_client/models/customer_address_book_address_book_address.py
 netsuite/swagger_client/models/customer_address_book_collection.py
```

### Comparing `netsuite_python-1.2.3/setup.py` & `netsuite_python-1.2.4/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 from pathlib import Path
 this_directory = Path(__file__).parent
 long_description = (this_directory / "README.md").read_text()
 
 setup(
     name='netsuite_python',
-    version='1.2.3',
+    version='1.2.4',
     description='Python SDK for Netsuite API with Django Integration',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://bitbucket.org/theapiguys/netsuite_python',
     readme="README.md",
     author='Will @ TheAPIGuys',
     author_email='will@theapiguys.com',
```

