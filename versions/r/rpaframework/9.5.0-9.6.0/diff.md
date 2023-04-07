# Comparing `tmp/rpaframework-9.5.0.tar.gz` & `tmp/rpaframework-9.6.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rpaframework-9.5.0.tar", max compression
+gzip compressed data, was "rpaframework-9.6.0.tar", max compression
```

## Comparing `rpaframework-9.5.0.tar` & `rpaframework-9.6.0.tar`

### file list

```diff
@@ -1,185 +1,185 @@
--rw-r--r--   0        0        0    11358 2020-12-01 11:26:02.718478 rpaframework-9.5.0/LICENSE
--rw-r--r--   0        0        0    11140 2021-01-14 14:55:48.563849 rpaframework-9.5.0/README.rst
--rw-r--r--   0        0        0     4232 2021-04-12 11:54:26.223886 rpaframework-9.5.0/pyproject.toml
--rw-r--r--   0        0        0    14825 2021-04-12 11:47:38.848630 rpaframework-9.5.0/src/RPA/Archive.py
--rw-r--r--   0        0        0      368 2020-12-16 08:48:57.421895 rpaframework-9.5.0/src/RPA/Browser/Playwright.py
--rw-r--r--   0        0        0    70708 2021-03-11 19:02:47.482481 rpaframework-9.5.0/src/RPA/Browser/Selenium.py
--rw-r--r--   0        0        0      360 2020-12-16 08:48:57.422594 rpaframework-9.5.0/src/RPA/Browser/__init__.py
--rw-r--r--   0        0        0    35202 2021-03-11 19:02:47.483357 rpaframework-9.5.0/src/RPA/Cloud/AWS.py
--rw-r--r--   0        0        0    27963 2020-11-12 07:52:10.585160 rpaframework-9.5.0/src/RPA/Cloud/Azure.py
--rw-r--r--   0        0        0    76561 2021-04-02 14:38:41.206910 rpaframework-9.5.0/src/RPA/Cloud/Google.py
--rw-r--r--   0        0        0        0 2020-10-23 07:05:52.733078 rpaframework-9.5.0/src/RPA/Cloud/__init__.py
--rw-r--r--   0        0        0       39 2021-03-11 19:02:47.483598 rpaframework-9.5.0/src/RPA/Cloud/objects/__init__.py
--rw-r--r--   0        0        0    16713 2021-03-11 19:02:47.483819 rpaframework-9.5.0/src/RPA/Cloud/objects/textract.py
--rw-r--r--   0        0        0    10426 2021-03-23 08:16:22.888450 rpaframework-9.5.0/src/RPA/Crypto.py
--rw-r--r--   0        0        0    21569 2021-02-03 13:50:58.297963 rpaframework-9.5.0/src/RPA/Database.py
--rw-r--r--   0        0        0     2717 2020-11-06 11:59:00.094414 rpaframework-9.5.0/src/RPA/Desktop/Clipboard.py
--rw-r--r--   0        0        0     7071 2021-01-19 11:58:25.777538 rpaframework-9.5.0/src/RPA/Desktop/OperatingSystem.py
--rw-r--r--   0        0        0    69405 2021-03-11 19:02:47.484416 rpaframework-9.5.0/src/RPA/Desktop/Windows.py
--rw-r--r--   0        0        0    12573 2021-02-26 19:40:11.899295 rpaframework-9.5.0/src/RPA/Desktop/__init__.py
--rw-r--r--   0        0        0      431 2020-12-29 15:51:02.241337 rpaframework-9.5.0/src/RPA/Desktop/keywords/__init__.py
--rw-r--r--   0        0        0     6454 2021-01-28 13:25:34.156945 rpaframework-9.5.0/src/RPA/Desktop/keywords/application.py
--rw-r--r--   0        0        0     2398 2020-12-21 09:17:25.192808 rpaframework-9.5.0/src/RPA/Desktop/keywords/clipboard.py
--rw-r--r--   0        0        0      692 2020-12-29 15:47:09.728000 rpaframework-9.5.0/src/RPA/Desktop/keywords/context.py
--rw-r--r--   0        0        0    11587 2020-12-21 09:17:25.193116 rpaframework-9.5.0/src/RPA/Desktop/keywords/finder.py
--rw-r--r--   0        0        0     3523 2020-12-21 09:17:25.193345 rpaframework-9.5.0/src/RPA/Desktop/keywords/keyboard.py
--rw-r--r--   0        0        0     7583 2020-12-21 09:17:25.193578 rpaframework-9.5.0/src/RPA/Desktop/keywords/mouse.py
--rw-r--r--   0        0        0     8575 2020-12-21 09:17:25.193845 rpaframework-9.5.0/src/RPA/Desktop/keywords/screen.py
--rw-r--r--   0        0        0     2171 2020-12-21 09:17:25.194063 rpaframework-9.5.0/src/RPA/Desktop/keywords/text.py
--rw-r--r--   0        0        0     1089 2020-12-01 11:26:02.723589 rpaframework-9.5.0/src/RPA/Desktop/utils.py
--rw-r--r--   0        0        0    28108 2021-03-31 11:27:20.376883 rpaframework-9.5.0/src/RPA/Dialogs.py
--rw-r--r--   0        0        0    23114 2021-04-01 13:24:42.156897 rpaframework-9.5.0/src/RPA/Email/Exchange.py
--rw-r--r--   0        0        0    46973 2021-03-25 21:53:27.672897 rpaframework-9.5.0/src/RPA/Email/ImapSmtp.py
--rw-r--r--   0        0        0        0 2020-10-23 07:05:51.544036 rpaframework-9.5.0/src/RPA/Email/__init__.py
--rw-r--r--   0        0        0    11648 2020-12-21 09:17:25.194863 rpaframework-9.5.0/src/RPA/Excel/Application.py
--rw-r--r--   0        0        0    27603 2021-04-12 11:47:38.850462 rpaframework-9.5.0/src/RPA/Excel/Files.py
--rw-r--r--   0        0        0        0 2020-10-23 07:05:51.579258 rpaframework-9.5.0/src/RPA/Excel/__init__.py
--rw-r--r--   0        0        0     8321 2020-11-12 07:52:10.590868 rpaframework-9.5.0/src/RPA/FTP.py
--rw-r--r--   0        0        0    21264 2020-12-21 09:17:25.195762 rpaframework-9.5.0/src/RPA/FileSystem.py
--rw-r--r--   0        0        0     5137 2021-04-12 11:47:38.851873 rpaframework-9.5.0/src/RPA/HTTP.py
--rw-r--r--   0        0        0    16629 2020-12-01 11:26:02.724196 rpaframework-9.5.0/src/RPA/Images.py
--rw-r--r--   0        0        0    11770 2021-04-12 09:24:32.637754 rpaframework-9.5.0/src/RPA/JSON.py
--rw-r--r--   0        0        0    11526 2020-11-06 11:59:00.100328 rpaframework-9.5.0/src/RPA/Netsuite.py
--rw-r--r--   0        0        0     6065 2020-11-06 11:59:00.100566 rpaframework-9.5.0/src/RPA/Notifier.py
--rw-r--r--   0        0        0     8214 2021-02-26 19:40:11.903707 rpaframework-9.5.0/src/RPA/Outlook/Application.py
--rw-r--r--   0        0        0        0 2020-10-23 07:05:51.966200 rpaframework-9.5.0/src/RPA/Outlook/__init__.py
--rw-r--r--   0        0        0    30895 2021-03-29 19:11:37.750040 rpaframework-9.5.0/src/RPA/Robocloud/Items.py
--rw-r--r--   0        0        0    17140 2021-03-23 08:16:22.891411 rpaframework-9.5.0/src/RPA/Robocloud/Secrets.py
--rw-r--r--   0        0        0        0 2020-10-23 07:05:52.213509 rpaframework-9.5.0/src/RPA/Robocloud/__init__.py
--rw-r--r--   0        0        0      231 2021-03-11 19:02:47.486410 rpaframework-9.5.0/src/RPA/RobotLogListener.py
--rw-r--r--   0        0        0      819 2021-01-14 14:55:48.568983 rpaframework-9.5.0/src/RPA/SAP.py
--rw-r--r--   0        0        0    20783 2020-11-06 11:59:00.103116 rpaframework-9.5.0/src/RPA/Salesforce.py
--rw-r--r--   0        0        0     1252 2020-11-05 07:45:17.430644 rpaframework-9.5.0/src/RPA/Slack.py
--rw-r--r--   0        0        0    52178 2021-04-12 11:47:38.853438 rpaframework-9.5.0/src/RPA/Tables.py
--rw-r--r--   0        0        0    30390 2021-03-23 08:16:22.892382 rpaframework-9.5.0/src/RPA/Tasks.py
--rw-r--r--   0        0        0    11396 2020-11-12 07:52:10.595023 rpaframework-9.5.0/src/RPA/Twitter.py
--rw-r--r--   0        0        0     6884 2021-03-11 19:02:47.487950 rpaframework-9.5.0/src/RPA/Word/Application.py
--rw-r--r--   0        0        0        0 2020-10-23 07:05:52.154223 rpaframework-9.5.0/src/RPA/Word/__init__.py
--rw-r--r--   0        0        0        0 2020-10-23 07:05:52.479827 rpaframework-9.5.0/src/RPA/includes/__init__.py
--rw-r--r--   0        0        0     2449 2020-10-13 08:55:20.157538 rpaframework-9.5.0/src/RPA/includes/dialog_styles.css
--rw-r--r--   0        0        0     4983 2021-01-14 14:55:48.569618 rpaframework-9.5.0/src/RPA/scripts/crypto.py
--rw-r--r--   0        0        0     2943 2021-01-14 14:55:48.569947 rpaframework-9.5.0/src/RPA/scripts/google_authenticate.py
--rw-r--r--   0        0        0     4920 2021-03-25 10:07:02.990286 rpaframework-9.5.0/src/RPA/scripts/robocorp_cloud.py
--rw-r--r--   0        0        0      591 2021-01-19 11:58:25.779370 rpaframework-9.5.0/tests/python/__init__.py
--rw-r--r--   0        0        0     1838 2021-03-11 19:02:47.488247 rpaframework-9.5.0/tests/python/test_browser.py
--rw-r--r--   0        0        0     5881 2021-01-14 14:55:48.570194 rpaframework-9.5.0/tests/python/test_crypto.py
--rw-r--r--   0        0        0      991 2020-10-13 08:55:20.158020 rpaframework-9.5.0/tests/python/test_dialogs.py
--rw-r--r--   0        0        0     8768 2021-04-12 11:47:38.853781 rpaframework-9.5.0/tests/python/test_excel.py
--rw-r--r--   0        0        0     2747 2020-06-26 06:52:09.555747 rpaframework-9.5.0/tests/python/test_exchange.py
--rw-r--r--   0        0        0     4890 2020-10-21 09:47:35.867918 rpaframework-9.5.0/tests/python/test_images.py
--rw-r--r--   0        0        0     3878 2021-01-29 12:06:44.876154 rpaframework-9.5.0/tests/python/test_imapsmtp.py
--rw-r--r--   0        0        0     1598 2021-01-25 16:05:09.836625 rpaframework-9.5.0/tests/python/test_json.py
--rw-r--r--   0        0        0    16036 2020-10-21 09:47:35.868201 rpaframework-9.5.0/tests/python/test_robocloud_items.py
--rw-r--r--   0        0        0     8942 2021-03-23 08:16:22.892772 rpaframework-9.5.0/tests/python/test_roboloud_secrets.py
--rw-r--r--   0        0        0    16062 2021-04-12 11:47:38.854406 rpaframework-9.5.0/tests/python/test_tables.py
--rw-r--r--   0        0        0       12 2020-06-26 06:52:09.557224 rpaframework-9.5.0/tests/resources/.gitignore
--rw-r--r--   0        0        0      721 2020-06-26 06:52:09.583434 rpaframework-9.5.0/tests/resources/CustomLibrary.py
--rw-r--r--   0        0        0     2070 2020-06-26 06:52:09.583531 rpaframework-9.5.0/tests/resources/FilePreparer.py
--rw-r--r--   0        0        0      391 2020-09-24 08:03:29.761654 rpaframework-9.5.0/tests/resources/alert.html
--rw-r--r--   0        0        0    32590 2020-06-26 06:52:09.584169 rpaframework-9.5.0/tests/resources/approved.png
--rw-r--r--   0        0        0    40502 2020-10-28 17:54:51.951208 rpaframework-9.5.0/tests/resources/bigdata.json
--rw-r--r--   0        0        0     2853 2021-01-19 11:58:25.780422 rpaframework-9.5.0/tests/resources/browser_docs.html
--rw-r--r--   0        0        0   252993 2021-04-12 11:47:38.855831 rpaframework-9.5.0/tests/resources/cacert.pem
--rw-r--r--   0        0        0      117 2020-10-28 17:54:51.951505 rpaframework-9.5.0/tests/resources/customers.json
--rw-r--r--   0        0        0     2443 2020-10-27 11:09:07.254444 rpaframework-9.5.0/tests/resources/dialogs.css
--rw-r--r--   0        0        0       51 2020-07-20 06:25:57.502534 rpaframework-9.5.0/tests/resources/easy.csv
--rw-r--r--   0        0        0     8192 2020-06-26 06:52:09.584408 rpaframework-9.5.0/tests/resources/example.xls
--rw-r--r--   0        0        0     6659 2020-06-26 06:52:09.584558 rpaframework-9.5.0/tests/resources/example.xlsx
--rw-r--r--   0        0        0       68 2021-03-11 19:02:47.490425 rpaframework-9.5.0/tests/resources/extra.csv
--rw-r--r--   0        0        0    60740 2020-06-26 06:52:09.586448 rpaframework-9.5.0/tests/resources/faces.jpeg
--rw-r--r--   0        0        0     1158 2020-06-26 06:52:09.586624 rpaframework-9.5.0/tests/resources/generated.pdf
--rw-r--r--   0        0        0    12744 2020-07-20 06:25:57.502691 rpaframework-9.5.0/tests/resources/hard.csv
--rw-r--r--   0        0        0     1823 2020-06-26 06:52:09.587105 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Backspace.jpg
--rw-r--r--   0        0        0     1595 2020-06-26 06:52:09.587228 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Clear.jpg
--rw-r--r--   0        0        0     1129 2020-06-26 06:52:09.587334 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Clear_all_memory.jpg
--rw-r--r--   0        0        0     1906 2020-06-26 06:52:09.587422 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Clear_entry.jpg
--rw-r--r--   0        0        0     1421 2020-06-26 06:52:09.587517 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Close_Calculator.jpg
--rw-r--r--   0        0        0     1488 2020-06-26 06:52:09.587638 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Decimal_Separator.jpg
--rw-r--r--   0        0        0     5737 2020-06-26 06:52:09.587778 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Display_controls.jpg
--rw-r--r--   0        0        0     7923 2020-06-26 06:52:09.588077 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Display_is_825.jpg
--rw-r--r--   0        0        0     1596 2020-06-26 06:52:09.588180 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Divide_by.jpg
--rw-r--r--   0        0        0     1974 2020-06-26 06:52:09.588279 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Eight.jpg
--rw-r--r--   0        0        0     1643 2020-06-26 06:52:09.588370 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Equals.jpg
--rw-r--r--   0        0        0     2481 2020-06-26 06:52:09.588484 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Expression_is_330__4.jpg
--rw-r--r--   0        0        0     1885 2020-06-26 06:52:09.588581 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Five.jpg
--rw-r--r--   0        0        0     1898 2020-06-26 06:52:09.588678 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Four.jpg
--rw-r--r--   0        0        0     1447 2020-06-26 06:52:09.588773 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Keep_on_top.jpg
--rw-r--r--   0        0        0     1339 2020-06-26 06:52:09.588871 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Maximize_Calculator.jpg
--rw-r--r--   0        0        0     1374 2020-06-26 06:52:09.589007 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Memory_Add.jpg
--rw-r--r--   0        0        0     1147 2020-06-26 06:52:09.589100 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Memory_Recall.jpg
--rw-r--r--   0        0        0     1475 2020-06-26 06:52:09.589197 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Memory_Store.jpg
--rw-r--r--   0        0        0     1291 2020-06-26 06:52:09.589288 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Memory_Subtract.jpg
--rw-r--r--   0        0        0     4163 2020-06-26 06:52:09.589404 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Memory_controls.jpg
--rw-r--r--   0        0        0     1280 2020-06-26 06:52:09.589510 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Minimize_Calculator.jpg
--rw-r--r--   0        0        0     1451 2020-06-26 06:52:09.589615 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Minus.jpg
--rw-r--r--   0        0        0     1855 2020-06-26 06:52:09.589708 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Multiply_by.jpg
--rw-r--r--   0        0        0     1790 2020-06-26 06:52:09.589840 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Nine.jpg
--rw-r--r--   0        0        0    18176 2020-06-26 06:52:09.590036 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Number_pad.jpg
--rw-r--r--   0        0        0     1742 2020-06-26 06:52:09.590144 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_One.jpg
--rw-r--r--   0        0        0     1422 2020-06-26 06:52:09.590240 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Open_Navigation.jpg
--rw-r--r--   0        0        0     1613 2020-06-26 06:52:09.590331 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Open_history_flyout.jpg
--rw-r--r--   0        0        0     1054 2020-06-26 06:52:09.590429 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Open_memory_flyout.jpg
--rw-r--r--   0        0        0     1956 2020-06-26 06:52:09.590573 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Percent.jpg
--rw-r--r--   0        0        0     1556 2020-06-26 06:52:09.590728 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Plus.jpg
--rw-r--r--   0        0        0     1981 2020-06-26 06:52:09.590906 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Positive_Negative.jpg
--rw-r--r--   0        0        0     1895 2020-06-26 06:52:09.591071 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Reciprocal.jpg
--rw-r--r--   0        0        0     1785 2020-06-26 06:52:09.591304 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Seven.jpg
--rw-r--r--   0        0        0     1770 2020-06-26 06:52:09.591511 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Six.jpg
--rw-r--r--   0        0        0     1844 2020-06-26 06:52:09.591751 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Square.jpg
--rw-r--r--   0        0        0     1920 2020-06-26 06:52:09.591924 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Square_root.jpg
--rw-r--r--   0        0        0     3404 2020-06-26 06:52:09.592049 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Standard_Calculator_mode.jpg
--rw-r--r--   0        0        0     4710 2020-06-26 06:52:09.592189 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Standard_functions.jpg
--rw-r--r--   0        0        0     6171 2020-06-26 06:52:09.592301 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Standard_operators.jpg
--rw-r--r--   0        0        0     1806 2020-06-26 06:52:09.592455 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Three.jpg
--rw-r--r--   0        0        0     1871 2020-06-26 06:52:09.592566 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Two.jpg
--rw-r--r--   0        0        0     1865 2020-06-26 06:52:09.592771 rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Zero.jpg
--rw-r--r--   0        0        0   231617 2020-06-26 06:52:09.595190 rpaframework-9.5.0/tests/resources/images/source.png
--rw-r--r--   0        0        0   181232 2020-06-26 06:52:09.598080 rpaframework-9.5.0/tests/resources/invoice.png
--rw-r--r--   0        0        0    88188 2020-06-26 06:52:09.598552 rpaframework-9.5.0/tests/resources/invoice.xml
--rw-r--r--   0        0        0      663 2020-06-29 15:25:35.873637 rpaframework-9.5.0/tests/resources/locators.json
--rw-r--r--   0        0        0      164 2020-06-26 06:52:09.598998 rpaframework-9.5.0/tests/resources/order.template
--rw-r--r--   0        0        0    12288 2020-09-24 17:49:44.005155 rpaframework-9.5.0/tests/resources/orders.db
--rw-r--r--   0        0        0     1202 2020-10-13 08:55:20.158186 rpaframework-9.5.0/tests/resources/questionform.json
--rw-r--r--   0        0        0      289 2020-10-13 08:55:20.159101 rpaframework-9.5.0/tests/resources/questionform_files.json
--rw-r--r--   0        0        0       40 2020-09-24 17:49:44.005413 rpaframework-9.5.0/tests/resources/script.sql
--rw-r--r--   0        0        0      535 2020-10-28 14:59:33.623467 rpaframework-9.5.0/tests/resources/secrets.json
--rw-r--r--   0        0        0      160 2020-09-24 17:49:44.005619 rpaframework-9.5.0/tests/resources/sqllite3_init.sql
--rw-r--r--   0        0        0     1231 2020-07-20 06:25:57.502878 rpaframework-9.5.0/tests/resources/tasks_schema.json
--rw-r--r--   0        0        0  1438220 2020-06-26 06:52:09.615190 rpaframework-9.5.0/tests/resources/test.flac
--rw-r--r--   0        0        0   320926 2020-06-26 06:52:09.618980 rpaframework-9.5.0/tests/resources/test.mp3
--rw-r--r--   0        0        0   611113 2020-06-26 06:52:09.624822 rpaframework-9.5.0/tests/resources/test.mp4
--rw-r--r--   0        0        0    49393 2020-06-26 06:52:09.625327 rpaframework-9.5.0/tests/resources/test_image_for_face_recognition.jpg
--rw-r--r--   0        0        0   300032 2020-08-31 09:40:32.878973 rpaframework-9.5.0/tests/resources/testarchive.tar
--rw-r--r--   0        0        0   256212 2020-08-31 09:40:12.315393 rpaframework-9.5.0/tests/resources/testarchive.tar.gz
--rw-r--r--   0        0        0   255290 2020-08-31 09:39:47.643874 rpaframework-9.5.0/tests/resources/testarchive.zip
--rw-r--r--   0        0        0   155349 2020-06-26 06:52:09.628929 rpaframework-9.5.0/tests/resources/vero2.pdf
--rw-r--r--   0        0        0     2577 2020-06-26 06:52:09.629097 rpaframework-9.5.0/tests/resources/wikipedia_science.txt
--rw-r--r--   0        0        0     6659 2020-07-20 06:25:57.503054 rpaframework-9.5.0/tests/resources/wrong_extension.xls
--rw-r--r--   0        0        0     8192 2020-07-20 06:25:57.503251 rpaframework-9.5.0/tests/resources/wrong_extension.xlsx
--rw-r--r--   0        0        0      525 2020-06-26 06:52:09.629423 rpaframework-9.5.0/tests/robot/test_application_word.robot
--rw-r--r--   0        0        0     6995 2021-04-12 11:47:38.857096 rpaframework-9.5.0/tests/robot/test_archive.robot
--rw-r--r--   0        0        0     3044 2020-12-16 08:48:57.426644 rpaframework-9.5.0/tests/robot/test_browser.robot
--rw-r--r--   0        0        0     1225 2020-06-26 06:52:09.629739 rpaframework-9.5.0/tests/robot/test_clipboard.robot
--rw-r--r--   0        0        0      834 2020-11-03 12:24:20.364383 rpaframework-9.5.0/tests/robot/test_cloud_aws.robot
--rwxr-xr-x   0        0        0     2520 2020-12-01 15:26:51.129230 rpaframework-9.5.0/tests/robot/test_cloud_google.robot
--rw-r--r--   0        0        0      686 2021-01-14 14:55:48.587343 rpaframework-9.5.0/tests/robot/test_crypto.robot
--rw-r--r--   0        0        0     1385 2021-01-19 13:39:35.591704 rpaframework-9.5.0/tests/robot/test_crypto_cli.robot
--rw-r--r--   0        0        0     2562 2020-10-18 10:19:40.488481 rpaframework-9.5.0/tests/robot/test_database.robot
--rw-r--r--   0        0        0     3733 2021-01-28 13:25:34.159946 rpaframework-9.5.0/tests/robot/test_desktop.robot
--rw-r--r--   0        0        0     1223 2020-10-27 11:24:06.231413 rpaframework-9.5.0/tests/robot/test_dialogs.robot
--rw-r--r--   0        0        0     4181 2020-12-08 12:41:38.520934 rpaframework-9.5.0/tests/robot/test_email.robot
--rw-r--r--   0        0        0      962 2020-06-26 06:52:09.630089 rpaframework-9.5.0/tests/robot/test_excel.robot
--rw-r--r--   0        0        0      680 2020-06-26 06:52:09.630190 rpaframework-9.5.0/tests/robot/test_exchange.robot
--rw-r--r--   0        0        0    11428 2021-03-11 19:02:47.491131 rpaframework-9.5.0/tests/robot/test_files.robot
--rw-r--r--   0        0        0     1352 2021-04-12 11:47:38.857233 rpaframework-9.5.0/tests/robot/test_http.robot
--rw-r--r--   0        0        0     2624 2021-01-25 16:05:09.837805 rpaframework-9.5.0/tests/robot/test_json.robot
--rw-r--r--   0        0        0      868 2020-06-26 06:52:09.630677 rpaframework-9.5.0/tests/robot/test_robocloud_items.robot
--rw-r--r--   0        0        0      799 2020-11-05 07:45:17.432829 rpaframework-9.5.0/tests/robot/test_robocloud_secrets.robot
--rw-r--r--   0        0        0      601 2020-06-26 06:52:09.630877 rpaframework-9.5.0/tests/robot/test_robotloglistener.robot
--rw-r--r--   0        0        0     2103 2020-06-26 06:52:09.631347 rpaframework-9.5.0/tests/robot/test_salesforce.robot
--rw-r--r--   0        0        0     1272 2020-08-26 11:53:41.167443 rpaframework-9.5.0/tests/robot/test_tables.robot
--rw-r--r--   0        0        0      710 2020-06-26 06:52:09.631656 rpaframework-9.5.0/tests/robot/test_tasks.robot
--rw-r--r--   0        0        0      669 2020-07-20 07:17:06.775218 rpaframework-9.5.0/tests/robot/test_tasks_schema.robot
--rwxr-xr-x   0        0        0     1342 2020-06-26 06:52:09.632027 rpaframework-9.5.0/tests/scripts/prepare_files.py
--rw-r--r--   0        0        0    15188 2021-04-12 12:10:23.282913 rpaframework-9.5.0/setup.py
--rw-r--r--   0        0        0    15604 2021-04-12 12:10:23.283527 rpaframework-9.5.0/PKG-INFO
+-rw-r--r--   0        0        0    11358 2020-12-01 11:26:02.718478 rpaframework-9.6.0/LICENSE
+-rw-r--r--   0        0        0    11140 2021-01-14 14:55:48.563849 rpaframework-9.6.0/README.rst
+-rw-r--r--   0        0        0     4232 2021-04-20 09:58:29.264406 rpaframework-9.6.0/pyproject.toml
+-rw-r--r--   0        0        0    14825 2021-04-12 11:47:38.848630 rpaframework-9.6.0/src/RPA/Archive.py
+-rw-r--r--   0        0        0      368 2020-12-16 08:48:57.421895 rpaframework-9.6.0/src/RPA/Browser/Playwright.py
+-rw-r--r--   0        0        0    70708 2021-03-11 19:02:47.482481 rpaframework-9.6.0/src/RPA/Browser/Selenium.py
+-rw-r--r--   0        0        0      360 2020-12-16 08:48:57.422594 rpaframework-9.6.0/src/RPA/Browser/__init__.py
+-rw-r--r--   0        0        0    35202 2021-03-11 19:02:47.483357 rpaframework-9.6.0/src/RPA/Cloud/AWS.py
+-rw-r--r--   0        0        0    27963 2020-11-12 07:52:10.585160 rpaframework-9.6.0/src/RPA/Cloud/Azure.py
+-rw-r--r--   0        0        0    76561 2021-04-02 14:38:41.206910 rpaframework-9.6.0/src/RPA/Cloud/Google.py
+-rw-r--r--   0        0        0        0 2020-10-23 07:05:52.733078 rpaframework-9.6.0/src/RPA/Cloud/__init__.py
+-rw-r--r--   0        0        0       39 2021-03-11 19:02:47.483598 rpaframework-9.6.0/src/RPA/Cloud/objects/__init__.py
+-rw-r--r--   0        0        0    16713 2021-03-11 19:02:47.483819 rpaframework-9.6.0/src/RPA/Cloud/objects/textract.py
+-rw-r--r--   0        0        0    10426 2021-03-23 08:16:22.888450 rpaframework-9.6.0/src/RPA/Crypto.py
+-rw-r--r--   0        0        0    21569 2021-02-03 13:50:58.297963 rpaframework-9.6.0/src/RPA/Database.py
+-rw-r--r--   0        0        0     2717 2020-11-06 11:59:00.094414 rpaframework-9.6.0/src/RPA/Desktop/Clipboard.py
+-rw-r--r--   0        0        0     7071 2021-01-19 11:58:25.777538 rpaframework-9.6.0/src/RPA/Desktop/OperatingSystem.py
+-rw-r--r--   0        0        0    69405 2021-03-11 19:02:47.484416 rpaframework-9.6.0/src/RPA/Desktop/Windows.py
+-rw-r--r--   0        0        0    12573 2021-02-26 19:40:11.899295 rpaframework-9.6.0/src/RPA/Desktop/__init__.py
+-rw-r--r--   0        0        0      431 2020-12-29 15:51:02.241337 rpaframework-9.6.0/src/RPA/Desktop/keywords/__init__.py
+-rw-r--r--   0        0        0     6454 2021-01-28 13:25:34.156945 rpaframework-9.6.0/src/RPA/Desktop/keywords/application.py
+-rw-r--r--   0        0        0     2398 2020-12-21 09:17:25.192808 rpaframework-9.6.0/src/RPA/Desktop/keywords/clipboard.py
+-rw-r--r--   0        0        0      692 2020-12-29 15:47:09.728000 rpaframework-9.6.0/src/RPA/Desktop/keywords/context.py
+-rw-r--r--   0        0        0    11587 2020-12-21 09:17:25.193116 rpaframework-9.6.0/src/RPA/Desktop/keywords/finder.py
+-rw-r--r--   0        0        0     3523 2020-12-21 09:17:25.193345 rpaframework-9.6.0/src/RPA/Desktop/keywords/keyboard.py
+-rw-r--r--   0        0        0     7583 2020-12-21 09:17:25.193578 rpaframework-9.6.0/src/RPA/Desktop/keywords/mouse.py
+-rw-r--r--   0        0        0     8575 2020-12-21 09:17:25.193845 rpaframework-9.6.0/src/RPA/Desktop/keywords/screen.py
+-rw-r--r--   0        0        0     2171 2020-12-21 09:17:25.194063 rpaframework-9.6.0/src/RPA/Desktop/keywords/text.py
+-rw-r--r--   0        0        0     1089 2020-12-01 11:26:02.723589 rpaframework-9.6.0/src/RPA/Desktop/utils.py
+-rw-r--r--   0        0        0    28108 2021-03-31 11:27:20.376883 rpaframework-9.6.0/src/RPA/Dialogs.py
+-rw-r--r--   0        0        0    23114 2021-04-01 13:24:42.156897 rpaframework-9.6.0/src/RPA/Email/Exchange.py
+-rw-r--r--   0        0        0    47476 2021-04-20 12:15:55.646202 rpaframework-9.6.0/src/RPA/Email/ImapSmtp.py
+-rw-r--r--   0        0        0        0 2020-10-23 07:05:51.544036 rpaframework-9.6.0/src/RPA/Email/__init__.py
+-rw-r--r--   0        0        0    11648 2020-12-21 09:17:25.194863 rpaframework-9.6.0/src/RPA/Excel/Application.py
+-rw-r--r--   0        0        0    27678 2021-04-20 09:57:20.265758 rpaframework-9.6.0/src/RPA/Excel/Files.py
+-rw-r--r--   0        0        0        0 2020-10-23 07:05:51.579258 rpaframework-9.6.0/src/RPA/Excel/__init__.py
+-rw-r--r--   0        0        0     8321 2020-11-12 07:52:10.590868 rpaframework-9.6.0/src/RPA/FTP.py
+-rw-r--r--   0        0        0    21368 2021-04-20 09:57:20.267704 rpaframework-9.6.0/src/RPA/FileSystem.py
+-rw-r--r--   0        0        0     5137 2021-04-12 11:47:38.851873 rpaframework-9.6.0/src/RPA/HTTP.py
+-rw-r--r--   0        0        0    16629 2020-12-01 11:26:02.724196 rpaframework-9.6.0/src/RPA/Images.py
+-rw-r--r--   0        0        0    11770 2021-04-12 09:24:32.637754 rpaframework-9.6.0/src/RPA/JSON.py
+-rw-r--r--   0        0        0    11526 2020-11-06 11:59:00.100328 rpaframework-9.6.0/src/RPA/Netsuite.py
+-rw-r--r--   0        0        0     6065 2020-11-06 11:59:00.100566 rpaframework-9.6.0/src/RPA/Notifier.py
+-rw-r--r--   0        0        0     8214 2021-02-26 19:40:11.903707 rpaframework-9.6.0/src/RPA/Outlook/Application.py
+-rw-r--r--   0        0        0        0 2020-10-23 07:05:51.966200 rpaframework-9.6.0/src/RPA/Outlook/__init__.py
+-rw-r--r--   0        0        0    30895 2021-03-29 19:11:37.750040 rpaframework-9.6.0/src/RPA/Robocloud/Items.py
+-rw-r--r--   0        0        0    17140 2021-03-23 08:16:22.891411 rpaframework-9.6.0/src/RPA/Robocloud/Secrets.py
+-rw-r--r--   0        0        0        0 2020-10-23 07:05:52.213509 rpaframework-9.6.0/src/RPA/Robocloud/__init__.py
+-rw-r--r--   0        0        0      231 2021-03-11 19:02:47.486410 rpaframework-9.6.0/src/RPA/RobotLogListener.py
+-rw-r--r--   0        0        0      819 2021-01-14 14:55:48.568983 rpaframework-9.6.0/src/RPA/SAP.py
+-rw-r--r--   0        0        0    20783 2020-11-06 11:59:00.103116 rpaframework-9.6.0/src/RPA/Salesforce.py
+-rw-r--r--   0        0        0     1252 2020-11-05 07:45:17.430644 rpaframework-9.6.0/src/RPA/Slack.py
+-rw-r--r--   0        0        0    52178 2021-04-12 11:47:38.853438 rpaframework-9.6.0/src/RPA/Tables.py
+-rw-r--r--   0        0        0    30390 2021-03-23 08:16:22.892382 rpaframework-9.6.0/src/RPA/Tasks.py
+-rw-r--r--   0        0        0    11396 2020-11-12 07:52:10.595023 rpaframework-9.6.0/src/RPA/Twitter.py
+-rw-r--r--   0        0        0     6834 2021-04-20 09:57:20.268887 rpaframework-9.6.0/src/RPA/Word/Application.py
+-rw-r--r--   0        0        0        0 2020-10-23 07:05:52.154223 rpaframework-9.6.0/src/RPA/Word/__init__.py
+-rw-r--r--   0        0        0        0 2020-10-23 07:05:52.479827 rpaframework-9.6.0/src/RPA/includes/__init__.py
+-rw-r--r--   0        0        0     2449 2020-10-13 08:55:20.157538 rpaframework-9.6.0/src/RPA/includes/dialog_styles.css
+-rw-r--r--   0        0        0     4983 2021-01-14 14:55:48.569618 rpaframework-9.6.0/src/RPA/scripts/crypto.py
+-rw-r--r--   0        0        0     2943 2021-01-14 14:55:48.569947 rpaframework-9.6.0/src/RPA/scripts/google_authenticate.py
+-rw-r--r--   0        0        0     4920 2021-03-25 10:07:02.990286 rpaframework-9.6.0/src/RPA/scripts/robocorp_cloud.py
+-rw-r--r--   0        0        0      591 2021-01-19 11:58:25.779370 rpaframework-9.6.0/tests/python/__init__.py
+-rw-r--r--   0        0        0     1838 2021-03-11 19:02:47.488247 rpaframework-9.6.0/tests/python/test_browser.py
+-rw-r--r--   0        0        0     5881 2021-01-14 14:55:48.570194 rpaframework-9.6.0/tests/python/test_crypto.py
+-rw-r--r--   0        0        0      991 2020-10-13 08:55:20.158020 rpaframework-9.6.0/tests/python/test_dialogs.py
+-rw-r--r--   0        0        0     8768 2021-04-12 11:47:38.853781 rpaframework-9.6.0/tests/python/test_excel.py
+-rw-r--r--   0        0        0     2747 2020-06-26 06:52:09.555747 rpaframework-9.6.0/tests/python/test_exchange.py
+-rw-r--r--   0        0        0     4890 2020-10-21 09:47:35.867918 rpaframework-9.6.0/tests/python/test_images.py
+-rw-r--r--   0        0        0     3878 2021-01-29 12:06:44.876154 rpaframework-9.6.0/tests/python/test_imapsmtp.py
+-rw-r--r--   0        0        0     1598 2021-01-25 16:05:09.836625 rpaframework-9.6.0/tests/python/test_json.py
+-rw-r--r--   0        0        0    16036 2020-10-21 09:47:35.868201 rpaframework-9.6.0/tests/python/test_robocloud_items.py
+-rw-r--r--   0        0        0     8942 2021-03-23 08:16:22.892772 rpaframework-9.6.0/tests/python/test_roboloud_secrets.py
+-rw-r--r--   0        0        0    16062 2021-04-12 11:47:38.854406 rpaframework-9.6.0/tests/python/test_tables.py
+-rw-r--r--   0        0        0       12 2020-06-26 06:52:09.557224 rpaframework-9.6.0/tests/resources/.gitignore
+-rw-r--r--   0        0        0      721 2020-06-26 06:52:09.583434 rpaframework-9.6.0/tests/resources/CustomLibrary.py
+-rw-r--r--   0        0        0     2070 2020-06-26 06:52:09.583531 rpaframework-9.6.0/tests/resources/FilePreparer.py
+-rw-r--r--   0        0        0      391 2020-09-24 08:03:29.761654 rpaframework-9.6.0/tests/resources/alert.html
+-rw-r--r--   0        0        0    32590 2020-06-26 06:52:09.584169 rpaframework-9.6.0/tests/resources/approved.png
+-rw-r--r--   0        0        0    40502 2020-10-28 17:54:51.951208 rpaframework-9.6.0/tests/resources/bigdata.json
+-rw-r--r--   0        0        0     2853 2021-01-19 11:58:25.780422 rpaframework-9.6.0/tests/resources/browser_docs.html
+-rw-r--r--   0        0        0   252993 2021-04-12 11:47:38.855831 rpaframework-9.6.0/tests/resources/cacert.pem
+-rw-r--r--   0        0        0      117 2020-10-28 17:54:51.951505 rpaframework-9.6.0/tests/resources/customers.json
+-rw-r--r--   0        0        0     2443 2020-10-27 11:09:07.254444 rpaframework-9.6.0/tests/resources/dialogs.css
+-rw-r--r--   0        0        0       51 2020-07-20 06:25:57.502534 rpaframework-9.6.0/tests/resources/easy.csv
+-rw-r--r--   0        0        0     8192 2020-06-26 06:52:09.584408 rpaframework-9.6.0/tests/resources/example.xls
+-rw-r--r--   0        0        0     6659 2020-06-26 06:52:09.584558 rpaframework-9.6.0/tests/resources/example.xlsx
+-rw-r--r--   0        0        0       68 2021-03-11 19:02:47.490425 rpaframework-9.6.0/tests/resources/extra.csv
+-rw-r--r--   0        0        0    60740 2020-06-26 06:52:09.586448 rpaframework-9.6.0/tests/resources/faces.jpeg
+-rw-r--r--   0        0        0     1158 2020-06-26 06:52:09.586624 rpaframework-9.6.0/tests/resources/generated.pdf
+-rw-r--r--   0        0        0    12744 2020-07-20 06:25:57.502691 rpaframework-9.6.0/tests/resources/hard.csv
+-rw-r--r--   0        0        0     1823 2020-06-26 06:52:09.587105 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Backspace.jpg
+-rw-r--r--   0        0        0     1595 2020-06-26 06:52:09.587228 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Clear.jpg
+-rw-r--r--   0        0        0     1129 2020-06-26 06:52:09.587334 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Clear_all_memory.jpg
+-rw-r--r--   0        0        0     1906 2020-06-26 06:52:09.587422 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Clear_entry.jpg
+-rw-r--r--   0        0        0     1421 2020-06-26 06:52:09.587517 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Close_Calculator.jpg
+-rw-r--r--   0        0        0     1488 2020-06-26 06:52:09.587638 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Decimal_Separator.jpg
+-rw-r--r--   0        0        0     5737 2020-06-26 06:52:09.587778 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Display_controls.jpg
+-rw-r--r--   0        0        0     7923 2020-06-26 06:52:09.588077 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Display_is_825.jpg
+-rw-r--r--   0        0        0     1596 2020-06-26 06:52:09.588180 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Divide_by.jpg
+-rw-r--r--   0        0        0     1974 2020-06-26 06:52:09.588279 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Eight.jpg
+-rw-r--r--   0        0        0     1643 2020-06-26 06:52:09.588370 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Equals.jpg
+-rw-r--r--   0        0        0     2481 2020-06-26 06:52:09.588484 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Expression_is_330__4.jpg
+-rw-r--r--   0        0        0     1885 2020-06-26 06:52:09.588581 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Five.jpg
+-rw-r--r--   0        0        0     1898 2020-06-26 06:52:09.588678 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Four.jpg
+-rw-r--r--   0        0        0     1447 2020-06-26 06:52:09.588773 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Keep_on_top.jpg
+-rw-r--r--   0        0        0     1339 2020-06-26 06:52:09.588871 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Maximize_Calculator.jpg
+-rw-r--r--   0        0        0     1374 2020-06-26 06:52:09.589007 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Memory_Add.jpg
+-rw-r--r--   0        0        0     1147 2020-06-26 06:52:09.589100 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Memory_Recall.jpg
+-rw-r--r--   0        0        0     1475 2020-06-26 06:52:09.589197 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Memory_Store.jpg
+-rw-r--r--   0        0        0     1291 2020-06-26 06:52:09.589288 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Memory_Subtract.jpg
+-rw-r--r--   0        0        0     4163 2020-06-26 06:52:09.589404 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Memory_controls.jpg
+-rw-r--r--   0        0        0     1280 2020-06-26 06:52:09.589510 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Minimize_Calculator.jpg
+-rw-r--r--   0        0        0     1451 2020-06-26 06:52:09.589615 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Minus.jpg
+-rw-r--r--   0        0        0     1855 2020-06-26 06:52:09.589708 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Multiply_by.jpg
+-rw-r--r--   0        0        0     1790 2020-06-26 06:52:09.589840 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Nine.jpg
+-rw-r--r--   0        0        0    18176 2020-06-26 06:52:09.590036 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Number_pad.jpg
+-rw-r--r--   0        0        0     1742 2020-06-26 06:52:09.590144 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_One.jpg
+-rw-r--r--   0        0        0     1422 2020-06-26 06:52:09.590240 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Open_Navigation.jpg
+-rw-r--r--   0        0        0     1613 2020-06-26 06:52:09.590331 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Open_history_flyout.jpg
+-rw-r--r--   0        0        0     1054 2020-06-26 06:52:09.590429 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Open_memory_flyout.jpg
+-rw-r--r--   0        0        0     1956 2020-06-26 06:52:09.590573 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Percent.jpg
+-rw-r--r--   0        0        0     1556 2020-06-26 06:52:09.590728 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Plus.jpg
+-rw-r--r--   0        0        0     1981 2020-06-26 06:52:09.590906 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Positive_Negative.jpg
+-rw-r--r--   0        0        0     1895 2020-06-26 06:52:09.591071 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Reciprocal.jpg
+-rw-r--r--   0        0        0     1785 2020-06-26 06:52:09.591304 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Seven.jpg
+-rw-r--r--   0        0        0     1770 2020-06-26 06:52:09.591511 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Six.jpg
+-rw-r--r--   0        0        0     1844 2020-06-26 06:52:09.591751 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Square.jpg
+-rw-r--r--   0        0        0     1920 2020-06-26 06:52:09.591924 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Square_root.jpg
+-rw-r--r--   0        0        0     3404 2020-06-26 06:52:09.592049 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Standard_Calculator_mode.jpg
+-rw-r--r--   0        0        0     4710 2020-06-26 06:52:09.592189 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Standard_functions.jpg
+-rw-r--r--   0        0        0     6171 2020-06-26 06:52:09.592301 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Standard_operators.jpg
+-rw-r--r--   0        0        0     1806 2020-06-26 06:52:09.592455 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Three.jpg
+-rw-r--r--   0        0        0     1871 2020-06-26 06:52:09.592566 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Two.jpg
+-rw-r--r--   0        0        0     1865 2020-06-26 06:52:09.592771 rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Zero.jpg
+-rw-r--r--   0        0        0   231617 2020-06-26 06:52:09.595190 rpaframework-9.6.0/tests/resources/images/source.png
+-rw-r--r--   0        0        0   181232 2020-06-26 06:52:09.598080 rpaframework-9.6.0/tests/resources/invoice.png
+-rw-r--r--   0        0        0    88188 2020-06-26 06:52:09.598552 rpaframework-9.6.0/tests/resources/invoice.xml
+-rw-r--r--   0        0        0      663 2020-06-29 15:25:35.873637 rpaframework-9.6.0/tests/resources/locators.json
+-rw-r--r--   0        0        0      164 2020-06-26 06:52:09.598998 rpaframework-9.6.0/tests/resources/order.template
+-rw-r--r--   0        0        0    12288 2020-09-24 17:49:44.005155 rpaframework-9.6.0/tests/resources/orders.db
+-rw-r--r--   0        0        0     1202 2020-10-13 08:55:20.158186 rpaframework-9.6.0/tests/resources/questionform.json
+-rw-r--r--   0        0        0      289 2020-10-13 08:55:20.159101 rpaframework-9.6.0/tests/resources/questionform_files.json
+-rw-r--r--   0        0        0       40 2020-09-24 17:49:44.005413 rpaframework-9.6.0/tests/resources/script.sql
+-rw-r--r--   0        0        0      535 2020-10-28 14:59:33.623467 rpaframework-9.6.0/tests/resources/secrets.json
+-rw-r--r--   0        0        0      160 2020-09-24 17:49:44.005619 rpaframework-9.6.0/tests/resources/sqllite3_init.sql
+-rw-r--r--   0        0        0     1231 2020-07-20 06:25:57.502878 rpaframework-9.6.0/tests/resources/tasks_schema.json
+-rw-r--r--   0        0        0  1438220 2020-06-26 06:52:09.615190 rpaframework-9.6.0/tests/resources/test.flac
+-rw-r--r--   0        0        0   320926 2020-06-26 06:52:09.618980 rpaframework-9.6.0/tests/resources/test.mp3
+-rw-r--r--   0        0        0   611113 2020-06-26 06:52:09.624822 rpaframework-9.6.0/tests/resources/test.mp4
+-rw-r--r--   0        0        0    49393 2020-06-26 06:52:09.625327 rpaframework-9.6.0/tests/resources/test_image_for_face_recognition.jpg
+-rw-r--r--   0        0        0   300032 2020-08-31 09:40:32.878973 rpaframework-9.6.0/tests/resources/testarchive.tar
+-rw-r--r--   0        0        0   256212 2020-08-31 09:40:12.315393 rpaframework-9.6.0/tests/resources/testarchive.tar.gz
+-rw-r--r--   0        0        0   255290 2020-08-31 09:39:47.643874 rpaframework-9.6.0/tests/resources/testarchive.zip
+-rw-r--r--   0        0        0   155349 2020-06-26 06:52:09.628929 rpaframework-9.6.0/tests/resources/vero2.pdf
+-rw-r--r--   0        0        0     2577 2020-06-26 06:52:09.629097 rpaframework-9.6.0/tests/resources/wikipedia_science.txt
+-rw-r--r--   0        0        0     6659 2020-07-20 06:25:57.503054 rpaframework-9.6.0/tests/resources/wrong_extension.xls
+-rw-r--r--   0        0        0     8192 2020-07-20 06:25:57.503251 rpaframework-9.6.0/tests/resources/wrong_extension.xlsx
+-rw-r--r--   0        0        0      525 2020-06-26 06:52:09.629423 rpaframework-9.6.0/tests/robot/test_application_word.robot
+-rw-r--r--   0        0        0     6995 2021-04-12 11:47:38.857096 rpaframework-9.6.0/tests/robot/test_archive.robot
+-rw-r--r--   0        0        0     3044 2020-12-16 08:48:57.426644 rpaframework-9.6.0/tests/robot/test_browser.robot
+-rw-r--r--   0        0        0     1225 2020-06-26 06:52:09.629739 rpaframework-9.6.0/tests/robot/test_clipboard.robot
+-rw-r--r--   0        0        0      834 2020-11-03 12:24:20.364383 rpaframework-9.6.0/tests/robot/test_cloud_aws.robot
+-rwxr-xr-x   0        0        0     2520 2021-04-20 09:57:15.505694 rpaframework-9.6.0/tests/robot/test_cloud_google.robot
+-rw-r--r--   0        0        0      686 2021-01-14 14:55:48.587343 rpaframework-9.6.0/tests/robot/test_crypto.robot
+-rw-r--r--   0        0        0     1385 2021-01-19 13:39:35.591704 rpaframework-9.6.0/tests/robot/test_crypto_cli.robot
+-rw-r--r--   0        0        0     2562 2020-10-18 10:19:40.488481 rpaframework-9.6.0/tests/robot/test_database.robot
+-rw-r--r--   0        0        0     3733 2021-01-28 13:25:34.159946 rpaframework-9.6.0/tests/robot/test_desktop.robot
+-rw-r--r--   0        0        0     1223 2020-10-27 11:24:06.231413 rpaframework-9.6.0/tests/robot/test_dialogs.robot
+-rw-r--r--   0        0        0     4181 2020-12-08 12:41:38.520934 rpaframework-9.6.0/tests/robot/test_email.robot
+-rw-r--r--   0        0        0      962 2020-06-26 06:52:09.630089 rpaframework-9.6.0/tests/robot/test_excel.robot
+-rw-r--r--   0        0        0      680 2020-06-26 06:52:09.630190 rpaframework-9.6.0/tests/robot/test_exchange.robot
+-rw-r--r--   0        0        0    11428 2021-03-11 19:02:47.491131 rpaframework-9.6.0/tests/robot/test_files.robot
+-rw-r--r--   0        0        0     1352 2021-04-12 11:47:38.857233 rpaframework-9.6.0/tests/robot/test_http.robot
+-rw-r--r--   0        0        0     2624 2021-01-25 16:05:09.837805 rpaframework-9.6.0/tests/robot/test_json.robot
+-rw-r--r--   0        0        0      868 2020-06-26 06:52:09.630677 rpaframework-9.6.0/tests/robot/test_robocloud_items.robot
+-rw-r--r--   0        0        0      799 2020-11-05 07:45:17.432829 rpaframework-9.6.0/tests/robot/test_robocloud_secrets.robot
+-rw-r--r--   0        0        0      601 2020-06-26 06:52:09.630877 rpaframework-9.6.0/tests/robot/test_robotloglistener.robot
+-rw-r--r--   0        0        0     2103 2020-06-26 06:52:09.631347 rpaframework-9.6.0/tests/robot/test_salesforce.robot
+-rw-r--r--   0        0        0     1272 2020-08-26 11:53:41.167443 rpaframework-9.6.0/tests/robot/test_tables.robot
+-rw-r--r--   0        0        0      710 2020-06-26 06:52:09.631656 rpaframework-9.6.0/tests/robot/test_tasks.robot
+-rw-r--r--   0        0        0      669 2020-07-20 07:17:06.775218 rpaframework-9.6.0/tests/robot/test_tasks_schema.robot
+-rwxr-xr-x   0        0        0     1342 2020-06-26 06:52:09.632027 rpaframework-9.6.0/tests/scripts/prepare_files.py
+-rw-r--r--   0        0        0    15188 2021-04-20 12:28:16.720358 rpaframework-9.6.0/setup.py
+-rw-r--r--   0        0        0    15604 2021-04-20 12:28:16.720975 rpaframework-9.6.0/PKG-INFO
```

### Comparing `rpaframework-9.5.0/LICENSE` & `rpaframework-9.6.0/LICENSE`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/README.rst` & `rpaframework-9.6.0/README.rst`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/pyproject.toml` & `rpaframework-9.6.0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "rpaframework"
-version = "9.5.0"
+version = "9.6.0"
 description = "A collection of tools and libraries for RPA"
 authors = [
 	"RPA Framework <rpafw@robocorp.com>",
 ]
 license = "Apache-2.0"
 readme = "README.rst"
 
@@ -41,15 +41,15 @@
 rpaframework-recognition = { version = "^0.7.0", optional = true }
 jsonpath-ng = "^1.5.2"
 robotframework = ">=4.0.0,!=4.0.1,<5.0.0"
 robotframework-sapguilibrary = { version = "^1.1", platform = "win32" }
 robotframework-seleniumlibrary = "^5.1.0"
 robotframework-seleniumtestability = "^1.1.0"
 robotframework-requests = "^0.7.0"
-robotframework-browser = { version = "^2.5.0", optional = true,  python = ">=3.7,<4.0" }
+robotframework-browser = { version = "^4.3.0", optional = true,  python = ">=3.7,<4.0" }
 pywinauto = { version = "^0.6.8", platform = "win32", python = "!=3.8.1,!=3.7.6" }
 pywin32 = { version = "^300", platform = "win32", python = "!=3.8.1,!=3.7.6" }
 comtypes = { version = "1.1.7", platform = "win32" }
 robotframework-pythonlibcore = "^2.1.0"
 pynput-robocorp-fork = "^2.0.0"
 python-xlib = { version = ">=0.17", platform = "linux" }
 psutil = { version = "^5.7.0", platform = "win32" }
@@ -70,15 +70,15 @@
 google-cloud-language = { version = "^1.3.0", optional = true }
 google-cloud-speech = { version = "^1.3.2", optional = true }
 google-cloud-storage = { version = "^1.28.1", optional = true }
 google-cloud-texttospeech = { version = "^1.0.1", optional = true }
 google-cloud-translate = { version = "^2.0.1", optional = true }
 google-cloud-videointelligence = { version = "^1.14.0", optional = true }
 google-cloud-vision = { version = "^1.0.0", optional = true }
-grpcio = { version = "1.33.2", optional = true }
+grpcio = { version = "1.37.0", optional = true }
 graphviz = "^0.13.2"
 notifiers = "^1.2.1"
 cryptography = "^3.3.1"
 mss = "^6.0.0"
 chardet = "^3.0.0"
 PySocks = ">=1.5.6,!=1.5.7,<2.0.0"
 selenium = "^3.141.0"
```

### Comparing `rpaframework-9.5.0/src/RPA/Archive.py` & `rpaframework-9.6.0/src/RPA/Archive.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Browser/Selenium.py` & `rpaframework-9.6.0/src/RPA/Browser/Selenium.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Cloud/AWS.py` & `rpaframework-9.6.0/src/RPA/Cloud/AWS.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Cloud/Azure.py` & `rpaframework-9.6.0/src/RPA/Cloud/Azure.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Cloud/Google.py` & `rpaframework-9.6.0/src/RPA/Cloud/Google.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Cloud/objects/textract.py` & `rpaframework-9.6.0/src/RPA/Cloud/objects/textract.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Crypto.py` & `rpaframework-9.6.0/src/RPA/Crypto.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Database.py` & `rpaframework-9.6.0/src/RPA/Database.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/Clipboard.py` & `rpaframework-9.6.0/src/RPA/Desktop/Clipboard.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/OperatingSystem.py` & `rpaframework-9.6.0/src/RPA/Desktop/OperatingSystem.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/Windows.py` & `rpaframework-9.6.0/src/RPA/Desktop/Windows.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/__init__.py` & `rpaframework-9.6.0/src/RPA/Desktop/__init__.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/keywords/application.py` & `rpaframework-9.6.0/src/RPA/Desktop/keywords/application.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/keywords/clipboard.py` & `rpaframework-9.6.0/src/RPA/Desktop/keywords/clipboard.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/keywords/context.py` & `rpaframework-9.6.0/src/RPA/Desktop/keywords/context.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/keywords/finder.py` & `rpaframework-9.6.0/src/RPA/Desktop/keywords/finder.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/keywords/keyboard.py` & `rpaframework-9.6.0/src/RPA/Desktop/keywords/keyboard.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/keywords/mouse.py` & `rpaframework-9.6.0/src/RPA/Desktop/keywords/mouse.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/keywords/screen.py` & `rpaframework-9.6.0/src/RPA/Desktop/keywords/screen.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/keywords/text.py` & `rpaframework-9.6.0/src/RPA/Desktop/keywords/text.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Desktop/utils.py` & `rpaframework-9.6.0/src/RPA/Desktop/utils.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Dialogs.py` & `rpaframework-9.6.0/src/RPA/Dialogs.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Email/Exchange.py` & `rpaframework-9.6.0/src/RPA/Email/Exchange.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Email/ImapSmtp.py` & `rpaframework-9.6.0/src/RPA/Email/ImapSmtp.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+import base64
 from enum import Enum
 from functools import wraps
 
 from io import StringIO
 import logging
 import os
 import re
@@ -20,15 +21,15 @@
 from email.mime.text import MIMEText  # pylint: disable=E0611
 
 from pathlib import Path
 from imaplib import IMAP4_SSL
 from smtplib import SMTP, SMTP_SSL, ssl
 from smtplib import SMTPConnectError, SMTPNotSupportedError, SMTPServerDisconnected
 
-from typing import Any
+from typing import Any, Union
 
 from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError
 from RPA.RobotLogListener import RobotLogListener
 
 
 class Action(Enum):
     """Possible email actions."""
@@ -778,20 +779,22 @@
 
             ${numsaved}  Save Attachments   SUBJECT "rpa task"
             ...          target_folder=${CURDIR}${/}messages  overwrite=True
         """  # noqa: E501
         attachments_saved = []
         messages = self.list_messages(criterion)
         for msg in messages:
-            attachments_saved.append(
+            attachments_saved.extend(
                 self.save_attachment(msg, target_folder, overwrite)
             )
-        return attachments_saved if len(attachments_saved) > 0 else False
+        return attachments_saved
 
-    def save_attachment(self, message, target_folder, overwrite):
+    def save_attachment(
+        self, message: Union[dict, Message], target_folder: str, overwrite: bool
+    ):
         # pylint: disable=C0301
         """Save mail attachment into local folder
 
         :param message: message item
         :param target_folder: local folder for saving attachments to (needs to exist),
             defaults to user's home directory if None
         :param overwrite: overwrite existing file is True, defaults to False
@@ -804,36 +807,44 @@
             FOR  ${email}  IN  @{emails}
                 Run Keyword If   ${email}[Has-Attachments] == True
                 ...              Save Attachment  ${email}  target_folder=${CURDIR}  overwrite=True
             END
         """  # noqa: E501
         if target_folder is None:
             target_folder = os.path.expanduser("~")
-        self._save_attachment(message, target_folder, overwrite)
+        return self._save_attachment(message, target_folder, overwrite)
 
     def _save_attachment(self, message, target_folder, overwrite):
         attachments_saved = []
         msg = message["Message"] if isinstance(message, dict) else message
         for part in msg.walk():
             content_maintype = part.get_content_maintype()
             content_disposition = part.get("Content-Disposition")
             if content_maintype != "multipart" and content_disposition is not None:
-                filename = Path(part.get_filename()).name
-                if bool(filename):
-                    filepath = Path(target_folder) / filename
+                filename = part.get_filename()
+                if filename:
+                    transfer_encoding = part.get_all("Content-Transfer-Encoding")
+                    if transfer_encoding and transfer_encoding[0] == "base64":
+                        filename_parts = filename.split("?")
+                        if len(filename_parts) > 1:
+                            filename = base64.b64decode(filename_parts[3]).decode(
+                                filename_parts[1]
+                            )
+                    filepath = Path(target_folder) / Path(filename).name
                     if not filepath.exists() or overwrite:
                         self.logger.info(
                             "Saving attachment: %s",
                             filename,
                         )
                         with open(filepath, "wb") as f:
                             f.write(part.get_payload(decode=True))
-                            attachments_saved.append(filepath)
+                            attachments_saved.append(str(filepath))
                     elif filepath.exists() and not overwrite:
                         self.logger.warning("Did not overwrite file: %s", filepath)
+        return attachments_saved
 
     def _save_eml_file(self, message, target_folder, overwrite):
         emlfile = Path(target_folder) / f"{message['Mail-Id']}.eml"
         if not emlfile.exists() or overwrite:
             with open(emlfile, "wb") as f:
                 f.write(message["bytes"])
         elif emlfile.exists() and not overwrite:
```

### Comparing `rpaframework-9.5.0/src/RPA/Excel/Application.py` & `rpaframework-9.6.0/src/RPA/Excel/Application.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Excel/Files.py` & `rpaframework-9.6.0/src/RPA/Excel/Files.py`

 * *Files 1% similar despite different names*

```diff
@@ -197,14 +197,16 @@
             f"Failed to open Excel file ({path}), "
             "verify that the path and extension are correct"
         )
 
     def create_workbook(self, path=None, fmt="xlsx"):
         """Create and open a new Excel workbook.
 
+        Automatically also creates a new worksheet with the name "Sheet".
+
         :param path: Default save path for workbook
         :param fmt:  Format of workbook, i.e. xlsx or xls
         """
         if self.workbook:
             self.close_workbook()
 
         fmt = str(fmt).lower().strip()
```

### Comparing `rpaframework-9.5.0/src/RPA/FTP.py` & `rpaframework-9.6.0/src/RPA/FTP.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/FileSystem.py` & `rpaframework-9.6.0/src/RPA/FileSystem.py`

 * *Files 0% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 
 class File(NamedTuple):
     """Robot Framework -friendly container for files."""
 
     path: str
     name: str
     size: int
-    mtime: str
+    mtime: float
 
     def __str__(self):
         return self.path
 
     def __fspath__(self):
         # os.PathLike interface
         return self.path
@@ -154,21 +154,23 @@
         return sorted(matches)
 
     def list_files_in_directory(self, path=None):
         """Lists all the files in the given directory, relative to it.
 
         :param path:    base directory for search, defaults to current working dir
         """
+        path = path or Path.cwd()
         return self.find_files(Path(path, "*"), include_dirs=False)
 
     def list_directories_in_directory(self, path=None):
         """Lists all the directories in the given directory, relative to it.
 
         :param path:    base directory for search, defaults to current working dir
         """
+        path = path or Path.cwd()
         return self.find_files(Path(path, "*"), include_files=False)
 
     def log_directory_tree(self, path=None):
         """Logs all the files in the directory recursively.
 
         :param path:    base directory to start from, defaults to current working dir
         """
@@ -223,14 +225,15 @@
         return not self.does_directory_exist(path)
 
     def is_directory_empty(self, path=None):
         """Returns True if the given directory has no files or subdirectories.
 
         :param path:    path to inspected directory
         """
+        path = path or Path.cwd()
         if self.does_directory_not_exist(path):
             raise NotADirectoryError(f"Not a valid directory: {path}")
 
         return not bool(self.find_files(Path(path, "*")))
 
     def is_directory_not_empty(self, path=None):
         """Returns True if the given directory has any files or subdirectories.
```

### Comparing `rpaframework-9.5.0/src/RPA/HTTP.py` & `rpaframework-9.6.0/src/RPA/HTTP.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Images.py` & `rpaframework-9.6.0/src/RPA/Images.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/JSON.py` & `rpaframework-9.6.0/src/RPA/JSON.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Netsuite.py` & `rpaframework-9.6.0/src/RPA/Netsuite.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Notifier.py` & `rpaframework-9.6.0/src/RPA/Notifier.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Outlook/Application.py` & `rpaframework-9.6.0/src/RPA/Outlook/Application.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Robocloud/Items.py` & `rpaframework-9.6.0/src/RPA/Robocloud/Items.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Robocloud/Secrets.py` & `rpaframework-9.6.0/src/RPA/Robocloud/Secrets.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/SAP.py` & `rpaframework-9.6.0/src/RPA/SAP.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Salesforce.py` & `rpaframework-9.6.0/src/RPA/Salesforce.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Slack.py` & `rpaframework-9.6.0/src/RPA/Slack.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Tables.py` & `rpaframework-9.6.0/src/RPA/Tables.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Tasks.py` & `rpaframework-9.6.0/src/RPA/Tasks.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Twitter.py` & `rpaframework-9.6.0/src/RPA/Twitter.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/Word/Application.py` & `rpaframework-9.6.0/src/RPA/Word/Application.py`

 * *Files 3% similar despite different names*

```diff
@@ -92,28 +92,32 @@
     def quit_application(self, save_changes: bool = False) -> None:
         """Quit the application."""
         if self.app is not None:
             self.close_document(save_changes)
             self.app.Quit()
             self.app = None
 
-    def open_file(self, filename: str = None) -> None:
+    def open_file(self, filename: str, read_only: bool = True) -> None:
         """Open Word document with filename.
 
-        :param filename: Word document filepath, defaults to None
+        :param filename: Word document path
         """
-        if filename is not None:
-            word_filepath = str(Path(filename).resolve())
-            self.logger.info("Opening document: %s", word_filepath)
-            doc = self.app.Documents.Open(word_filepath, False, True, None)
-            doc.Activate()
-            self.app.ActiveWindow.View.ReadingLayout = False
-            self.filename = word_filepath
-        else:
-            self.logger.warning("Filename was not given.")
+        path = str(Path(filename).resolve())
+        self.logger.info("Opening document: %s", path)
+
+        doc = self.app.Documents.Open(
+            FileName=path,
+            ConfirmConversions=False,
+            ReadOnly=read_only,
+            AddToRecentFiles=False,
+        )
+
+        doc.Activate()
+        self.app.ActiveWindow.View.ReadingLayout = False
+        self.filename = path
 
     def create_new_document(self) -> None:
         """Create new document for Word application"""
         if self.app:
             self.app.Documents.Add()
 
     def export_to_pdf(self, filename: str) -> None:
```

### Comparing `rpaframework-9.5.0/src/RPA/includes/dialog_styles.css` & `rpaframework-9.6.0/src/RPA/includes/dialog_styles.css`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/scripts/crypto.py` & `rpaframework-9.6.0/src/RPA/scripts/crypto.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/scripts/google_authenticate.py` & `rpaframework-9.6.0/src/RPA/scripts/google_authenticate.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/src/RPA/scripts/robocorp_cloud.py` & `rpaframework-9.6.0/src/RPA/scripts/robocorp_cloud.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/__init__.py` & `rpaframework-9.6.0/tests/python/__init__.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/test_browser.py` & `rpaframework-9.6.0/tests/python/test_browser.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/test_crypto.py` & `rpaframework-9.6.0/tests/python/test_crypto.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/test_dialogs.py` & `rpaframework-9.6.0/tests/python/test_dialogs.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/test_excel.py` & `rpaframework-9.6.0/tests/python/test_excel.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/test_exchange.py` & `rpaframework-9.6.0/tests/python/test_exchange.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/test_images.py` & `rpaframework-9.6.0/tests/python/test_images.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/test_imapsmtp.py` & `rpaframework-9.6.0/tests/python/test_imapsmtp.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/test_json.py` & `rpaframework-9.6.0/tests/python/test_json.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/test_robocloud_items.py` & `rpaframework-9.6.0/tests/python/test_robocloud_items.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/test_roboloud_secrets.py` & `rpaframework-9.6.0/tests/python/test_roboloud_secrets.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/python/test_tables.py` & `rpaframework-9.6.0/tests/python/test_tables.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/CustomLibrary.py` & `rpaframework-9.6.0/tests/resources/CustomLibrary.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/FilePreparer.py` & `rpaframework-9.6.0/tests/resources/FilePreparer.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/approved.png` & `rpaframework-9.6.0/tests/resources/approved.png`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/bigdata.json` & `rpaframework-9.6.0/tests/resources/bigdata.json`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/browser_docs.html` & `rpaframework-9.6.0/tests/resources/browser_docs.html`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/cacert.pem` & `rpaframework-9.6.0/tests/resources/cacert.pem`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/dialogs.css` & `rpaframework-9.6.0/tests/resources/dialogs.css`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/example.xls` & `rpaframework-9.6.0/tests/resources/example.xls`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/example.xlsx` & `rpaframework-9.6.0/tests/resources/example.xlsx`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/faces.jpeg` & `rpaframework-9.6.0/tests/resources/faces.jpeg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/generated.pdf` & `rpaframework-9.6.0/tests/resources/generated.pdf`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/hard.csv` & `rpaframework-9.6.0/tests/resources/hard.csv`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Backspace.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Backspace.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Clear.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Clear.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Clear_all_memory.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Clear_all_memory.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Clear_entry.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Clear_entry.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Close_Calculator.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Close_Calculator.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Decimal_Separator.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Decimal_Separator.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Display_controls.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Display_controls.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Display_is_825.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Display_is_825.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Divide_by.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Divide_by.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Eight.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Eight.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Equals.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Equals.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Expression_is_330__4.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Expression_is_330__4.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Five.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Five.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Four.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Four.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Keep_on_top.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Keep_on_top.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Maximize_Calculator.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Maximize_Calculator.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Memory_Add.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Memory_Add.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Memory_Recall.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Memory_Recall.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Memory_Store.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Memory_Store.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Memory_Subtract.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Memory_Subtract.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Memory_controls.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Memory_controls.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Minimize_Calculator.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Minimize_Calculator.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Minus.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Minus.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Multiply_by.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Multiply_by.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Nine.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Nine.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Number_pad.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Number_pad.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_One.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_One.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Open_Navigation.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Open_Navigation.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Open_history_flyout.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Open_history_flyout.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Open_memory_flyout.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Open_memory_flyout.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Percent.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Percent.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Plus.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Plus.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Positive_Negative.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Positive_Negative.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Reciprocal.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Reciprocal.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Seven.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Seven.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Six.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Six.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Square.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Square.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Square_root.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Square_root.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Standard_Calculator_mode.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Standard_Calculator_mode.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Standard_functions.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Standard_functions.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Standard_operators.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Standard_operators.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Three.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Three.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Two.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Two.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/locator_Calculator_ctrl_Zero.jpg` & `rpaframework-9.6.0/tests/resources/images/locator_Calculator_ctrl_Zero.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/images/source.png` & `rpaframework-9.6.0/tests/resources/images/source.png`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/invoice.png` & `rpaframework-9.6.0/tests/resources/invoice.png`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/invoice.xml` & `rpaframework-9.6.0/tests/resources/invoice.xml`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/locators.json` & `rpaframework-9.6.0/tests/resources/locators.json`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/orders.db` & `rpaframework-9.6.0/tests/resources/orders.db`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/questionform.json` & `rpaframework-9.6.0/tests/resources/questionform.json`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/secrets.json` & `rpaframework-9.6.0/tests/resources/secrets.json`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/tasks_schema.json` & `rpaframework-9.6.0/tests/resources/tasks_schema.json`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/test.flac` & `rpaframework-9.6.0/tests/resources/test.flac`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/test.mp3` & `rpaframework-9.6.0/tests/resources/test.mp3`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/test.mp4` & `rpaframework-9.6.0/tests/resources/test.mp4`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/test_image_for_face_recognition.jpg` & `rpaframework-9.6.0/tests/resources/test_image_for_face_recognition.jpg`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/testarchive.tar` & `rpaframework-9.6.0/tests/resources/testarchive.tar`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/testarchive.tar.gz` & `rpaframework-9.6.0/tests/resources/testarchive.tar.gz`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/testarchive.zip` & `rpaframework-9.6.0/tests/resources/testarchive.zip`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/vero2.pdf` & `rpaframework-9.6.0/tests/resources/vero2.pdf`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/wikipedia_science.txt` & `rpaframework-9.6.0/tests/resources/wikipedia_science.txt`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/wrong_extension.xls` & `rpaframework-9.6.0/tests/resources/wrong_extension.xls`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/resources/wrong_extension.xlsx` & `rpaframework-9.6.0/tests/resources/wrong_extension.xlsx`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_application_word.robot` & `rpaframework-9.6.0/tests/robot/test_application_word.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_archive.robot` & `rpaframework-9.6.0/tests/robot/test_archive.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_browser.robot` & `rpaframework-9.6.0/tests/robot/test_browser.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_clipboard.robot` & `rpaframework-9.6.0/tests/robot/test_clipboard.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_cloud_aws.robot` & `rpaframework-9.6.0/tests/robot/test_cloud_aws.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_cloud_google.robot` & `rpaframework-9.6.0/tests/robot/test_cloud_google.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_crypto.robot` & `rpaframework-9.6.0/tests/robot/test_crypto.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_crypto_cli.robot` & `rpaframework-9.6.0/tests/robot/test_crypto_cli.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_database.robot` & `rpaframework-9.6.0/tests/robot/test_database.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_desktop.robot` & `rpaframework-9.6.0/tests/robot/test_desktop.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_dialogs.robot` & `rpaframework-9.6.0/tests/robot/test_dialogs.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_email.robot` & `rpaframework-9.6.0/tests/robot/test_email.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_excel.robot` & `rpaframework-9.6.0/tests/robot/test_excel.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_exchange.robot` & `rpaframework-9.6.0/tests/robot/test_exchange.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_files.robot` & `rpaframework-9.6.0/tests/robot/test_files.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_http.robot` & `rpaframework-9.6.0/tests/robot/test_http.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_json.robot` & `rpaframework-9.6.0/tests/robot/test_json.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_robocloud_items.robot` & `rpaframework-9.6.0/tests/robot/test_robocloud_items.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_robocloud_secrets.robot` & `rpaframework-9.6.0/tests/robot/test_robocloud_secrets.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_robotloglistener.robot` & `rpaframework-9.6.0/tests/robot/test_robotloglistener.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_salesforce.robot` & `rpaframework-9.6.0/tests/robot/test_salesforce.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_tables.robot` & `rpaframework-9.6.0/tests/robot/test_tables.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_tasks.robot` & `rpaframework-9.6.0/tests/robot/test_tasks.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/robot/test_tasks_schema.robot` & `rpaframework-9.6.0/tests/robot/test_tasks_schema.robot`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/tests/scripts/prepare_files.py` & `rpaframework-9.6.0/tests/scripts/prepare_files.py`

 * *Files identical despite different names*

### Comparing `rpaframework-9.5.0/setup.py` & `rpaframework-9.6.0/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -73,26 +73,26 @@
             'google-cloud-language>=1.3.0,<2.0.0',
             'google-cloud-speech>=1.3.2,<2.0.0',
             'google-cloud-storage>=1.28.1,<2.0.0',
             'google-cloud-texttospeech>=1.0.1,<2.0.0',
             'google-cloud-translate>=2.0.1,<3.0.0',
             'google-cloud-videointelligence>=1.14.0,<2.0.0',
             'google-cloud-vision>=1.0.0,<2.0.0',
-            'grpcio==1.33.2'],
- 'playwright': ['grpcio==1.33.2'],
- 'playwright:python_version >= "3.7" and python_version < "4.0"': ['robotframework-browser>=2.5.0,<3.0.0']}
+            'grpcio==1.37.0'],
+ 'playwright': ['grpcio==1.37.0'],
+ 'playwright:python_version >= "3.7" and python_version < "4.0"': ['robotframework-browser>=4.3.0,<5.0.0']}
 
 entry_points = \
 {'console_scripts': ['rpa-crypto = RPA.scripts.crypto:main',
                      'rpa-google-oauth = RPA.scripts.google_authenticate:main',
                      'use-robocorp-vault = RPA.scripts.robocorp_cloud:main']}
 
 setup_kwargs = {
     'name': 'rpaframework',
-    'version': '9.5.0',
+    'version': '9.6.0',
     'description': 'A collection of tools and libraries for RPA',
     'long_description': 'RPA Framework\n=============\n\n.. contents:: Table of Contents\n   :local:\n   :depth: 1\n\n.. include-marker\n\nIntroduction\n------------\n\n`RPA Framework` is a collection of open-source libraries and tools for\nRobotic Process Automation (RPA), and it is designed to be used with both\n`Robot Framework`_ and Python_. The goal is to offer well-documented and\nactively maintained core libraries for Software Robot Developers.\n\nLearn more about RPA at `Robocorp Documentation`_.\n\n**The project is:**\n\n- 100% Open Source\n- Sponsored by Robocorp_\n- Optimized for `Robocorp Cloud`_ and `Robocorp Lab`_\n- Accepting external contributions\n\n.. _Robot Framework: https://robotframework.org\n.. _Robot Framework Foundation: https://robotframework.org/foundation/\n.. _Python: https://python.org\n.. _Robocorp: https://robocorp.com\n.. _Robocorp Documentation: https://robocorp.com/docs/\n.. _Robocorp Cloud: https://robocorp.com/docs/product-manuals/robocorp-cloud/robocorp-cloud\n.. _Robocorp Lab: https://robocorp.com/docs/product-manuals/robocorp-lab/robocorp-lab-overview\n\nLinks\n^^^^^\n\n- Homepage: `<https://www.github.com/robocorp/rpaframework/>`_\n- Documentation: `<https://rpaframework.org/>`_\n- PyPI: `<https://pypi.org/project/rpaframework/>`_\n- Release notes: `<https://rpaframework.org/releasenotes.html>`_\n\n------------\n\n.. image:: https://github.com/robocorp/rpaframework/workflows/main/badge.svg\n   :target: https://github.com/robocorp/rpaframework/actions?query=workflow%3Amain\n   :alt: Status\n\n.. image:: https://img.shields.io/pypi/v/rpaframework.svg?label=version\n   :target: https://pypi.python.org/pypi/rpaframework\n   :alt: Latest version\n\n.. image:: https://img.shields.io/pypi/l/rpaframework.svg\n   :target: http://www.apache.org/licenses/LICENSE-2.0.html\n   :alt: License\n\nLibraries\n---------\n\nThe RPA Framework project currently includes the following libraries:\n\n+----------------------------+----------------------------------------------+\n| `Archive`_                 | Archiving TAR and ZIP files                  |\n+----------------------------+----------------------------------------------+\n| `Browser.Selenium`_        | Control browsers and automate the web        |\n+----------------------------+----------------------------------------------+\n| `Browser.Playwright`_      | Newer way to control browsers                |\n+----------------------------+----------------------------------------------+\n| `Cloud.AWS`_               | Use Amazon AWS services                      |\n+----------------------------+----------------------------------------------+\n| `Cloud.Azure`_             | Use Microsoft Azure services                 |\n+----------------------------+----------------------------------------------+\n| `Cloud.Google`_            | Use Google Cloud services                    |\n+----------------------------+----------------------------------------------+\n| `Crypto`_                  | Common hashing and encryption operations     |\n+----------------------------+----------------------------------------------+\n| `Database`_                | Interact with databases                      |\n+----------------------------+----------------------------------------------+\n| `Desktop`_                 | Cross-platform desktop automation            |\n+----------------------------+----------------------------------------------+\n| `Desktop.Clipboard`_       | Interact with the system clipboard           |\n+----------------------------+----------------------------------------------+\n| `Desktop.OperatingSystem`_ | Read OS information and manipulate processes |\n+----------------------------+----------------------------------------------+\n| `Desktop.Windows`_         | Automate Windows desktop applications        |\n+----------------------------+----------------------------------------------+\n| `Dialogs`_                 | Request user input during executions         |\n+----------------------------+----------------------------------------------+\n| `Email.Exchange`_          | E-Mail operations (Exchange protocol)        |\n+----------------------------+----------------------------------------------+\n| `Email.ImapSmtp`_          | E-Mail operations (IMAP & SMTP)              |\n+----------------------------+----------------------------------------------+\n| `Excel.Application`_       | Control the Excel desktop application        |\n+----------------------------+----------------------------------------------+\n| `Excel.Files`_             | Manipulate Excel files directly              |\n+----------------------------+----------------------------------------------+\n| `FileSystem`_              | Read and manipulate files and paths          |\n+----------------------------+----------------------------------------------+\n| `FTP`_                     | Interact with FTP servers                    |\n+----------------------------+----------------------------------------------+\n| `HTTP`_                    | Interact directly with web APIs              |\n+----------------------------+----------------------------------------------+\n| `Images`_                  | Manipulate images                            |\n+----------------------------+----------------------------------------------+\n| `JSON`_                    | Manipulate JSON objects                      |\n+----------------------------+----------------------------------------------+\n| `Notifier`_                | Notify messages using different services     |\n+----------------------------+----------------------------------------------+\n| `Outlook.Application`_     | Control the Outlook desktop application      |\n+----------------------------+----------------------------------------------+\n| `PDF`_                     | Read and create PDF documents                |\n+----------------------------+----------------------------------------------+\n| `Robocloud.Items`_         | Use the Robocloud Work Items API             |\n+----------------------------+----------------------------------------------+\n| `Robocloud.Secrets`_       | Use the Robocloud Secrets API                |\n+----------------------------+----------------------------------------------+\n| `Salesforce`_              | Salesforce operations                        |\n+----------------------------+----------------------------------------------+\n| `SAP`_                     | Control SAP GUI desktop client               |\n+----------------------------+----------------------------------------------+\n| `Tables`_                  | Manipulate, sort, and filter tabular data    |\n+----------------------------+----------------------------------------------+\n| `Tasks`_                   | Control task execution                       |\n+----------------------------+----------------------------------------------+\n| `Twitter`_                 | Twitter API interface                        |\n+----------------------------+----------------------------------------------+\n| `Word.Application`_        | Control the Word desktop application         |\n+----------------------------+----------------------------------------------+\n\n.. _Archive: https://rpaframework.org/libraries/archive/\n.. _Browser.Playwright: https://rpaframework.org/libraries/browser_playwright/\n.. _Browser.Selenium: https://rpaframework.org/libraries/browser_selenium/\n.. _Cloud.AWS: https://rpaframework.org/libraries/cloud_aws/\n.. _Cloud.Azure: https://rpaframework.org/libraries/cloud_azure/\n.. _Cloud.Google: https://rpaframework.org/libraries/cloud_google/\n.. _Crypto: https://rpaframework.org/libraries/crypto/\n.. _Database: https://rpaframework.org/libraries/database/\n.. _Desktop: https://rpaframework.org/libraries/desktop/\n.. _Desktop.Clipboard: https://rpaframework.org/libraries/desktop_clipboard/\n.. _Desktop.Operatingsystem: https://rpaframework.org/libraries/desktop_operatingsystem/\n.. _Desktop.Windows: https://rpaframework.org/libraries/desktop_windows/\n.. _Dialogs: https://rpaframework.org/libraries/dialogs/\n.. _Email.Exchange: https://rpaframework.org/libraries/email_exchange/\n.. _Email.ImapSmtp: https://rpaframework.org/libraries/email_imapsmtp/\n.. _Excel.Application: https://rpaframework.org/libraries/excel_application/\n.. _Excel.Files: https://rpaframework.org/libraries/excel_files/\n.. _FileSystem: https://rpaframework.org/libraries/filesystem/\n.. _FTP: https://rpaframework.org/libraries/ftp/\n.. _HTTP: https://rpaframework.org/libraries/http/\n.. _Images: https://rpaframework.org/libraries/images/\n.. _JSON: https://rpaframework.org/libraries/json/\n.. _Notifier: https://rpaframework.org/libraries/notifier/\n.. _Outlook.Application: https://rpaframework.org/libraries/outlook_application/\n.. _PDF: https://rpaframework.org/libraries/pdf/\n.. _Robocloud.Items: https://rpaframework.org/libraries/robocloud_items/\n.. _Robocloud.Secrets: https://rpaframework.org/libraries/robocloud_secrets/\n.. _Salesforce: https://rpaframework.org/libraries/salesforce/\n.. _SAP: https://rpaframework.org/libraries/sap/\n.. _Tables: https://rpaframework.org/libraries/tables/\n.. _Tasks: https://rpaframework.org/libraries/tasks/\n.. _Twitter: https://rpaframework.org/libraries/twitter/\n.. _Word.Application: https://rpaframework.org/libraries/word_application/\n\nInstallation\n------------\n\nIf you already have Python_ and `pip <http://pip-installer.org>`_ installed,\nyou can use:\n\n``pip install rpaframework``\n\nTo install all extra packages, you can use:\n\n``pip install rpaframework[aws,cv,google]``\n\n.. note:: Python 3.6 or higher is required\n\nExample\n-------\n\nAfter installation the libraries can be directly imported inside\n`Robot Framework`_:\n\n.. code:: robotframework\n\n    *** Settings ***\n    Library    RPA.Browser.Selenium\n\n    *** Tasks ***\n    Login as user\n        Open available browser    https://example.com\n        Input text    id:user-name    ${USERNAME}\n        Input text    id:password     ${PASSWORD}\n\nThe libraries are also available inside Python_:\n\n.. code:: python\n\n    from RPA.Browser.Selenium import Selenium\n\n    lib = Selenium()\n\n    lib.open_available_browser("https://example.com")\n    lib.input_text("id:user-name", username)\n    lib.input_text("id:password", password)\n\nSupport and contact\n-------------------\n\n- `rpaframework.org <https://rpaframework.org/>`_ for library documentation\n- `Robocorp Documentation`_ for guides and tutorials\n- **#rpaframework** channel in `Robot Framework Slack`_ if you\n  have open questions or want to contribute\n- `Robocorp Forum`_ for discussions about RPA\n- Communicate with your fellow Software Robot Developers and Robocorp experts\n  at `Robocorp Developers Slack`_\n\n.. _Robot Framework Slack: https://robotframework-slack-invite.herokuapp.com/\n.. _Robocorp Forum: https://forum.robocorp.com\n.. _Robocorp Developers Slack: https://robocorp-developers.slack.com\n\nContributing\n------------\n\nFound a bug? Missing a critical feature? Interested in contributing?\nHead over to the `Contribution guide <https://rpaframework.org/contributing/guide.html>`_\nto see where to get started.\n\nLicense\n-------\n\nThis project is open-source and licensed under the terms of the\n`Apache License 2.0 <http://apache.org/licenses/LICENSE-2.0>`_.\n',
     'author': 'RPA Framework',
     'author_email': 'rpafw@robocorp.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': 'https://rpaframework.org/',
```

### Comparing `rpaframework-9.5.0/PKG-INFO` & `rpaframework-9.6.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rpaframework
-Version: 9.5.0
+Version: 9.6.0
 Summary: A collection of tools and libraries for RPA
 Home-page: https://rpaframework.org/
 License: Apache-2.0
 Keywords: robotframework,rpa,automation
 Author: RPA Framework
 Author-email: rpafw@robocorp.com
 Requires-Python: >=3.6,<4.0
@@ -42,29 +42,29 @@
 Requires-Dist: google-cloud-speech (>=1.3.2,<2.0.0); extra == "google"
 Requires-Dist: google-cloud-storage (>=1.28.1,<2.0.0); extra == "google"
 Requires-Dist: google-cloud-texttospeech (>=1.0.1,<2.0.0); extra == "google"
 Requires-Dist: google-cloud-translate (>=2.0.1,<3.0.0); extra == "google"
 Requires-Dist: google-cloud-videointelligence (>=1.14.0,<2.0.0); extra == "google"
 Requires-Dist: google-cloud-vision (>=1.0.0,<2.0.0); extra == "google"
 Requires-Dist: graphviz (>=0.13.2,<0.14.0)
-Requires-Dist: grpcio (==1.33.2); extra == "playwright" or extra == "google"
+Requires-Dist: grpcio (==1.37.0); extra == "playwright" or extra == "google"
 Requires-Dist: jsonpath-ng (>=1.5.2,<2.0.0)
 Requires-Dist: mss (>=6.0.0,<7.0.0)
 Requires-Dist: netsuitesdk (>=1.1.0,<2.0.0)
 Requires-Dist: notifiers (>=1.2.1,<2.0.0)
 Requires-Dist: openpyxl (>=3.0.3,<4.0.0)
 Requires-Dist: pillow (>=8.0.1,<9.0.0)
 Requires-Dist: psutil (>=5.7.0,<6.0.0); sys_platform == "win32"
 Requires-Dist: pynput-robocorp-fork (>=2.0.0,<3.0.0)
 Requires-Dist: pyperclip (>=1.8.0,<2.0.0)
 Requires-Dist: python-xlib (>=0.17); sys_platform == "linux"
 Requires-Dist: pywin32 (>=300,<301); python_version < "3.7.6" and sys_platform == "win32" or python_version > "3.7.6" and python_version < "3.8.1" and sys_platform == "win32" or python_version > "3.8.1" and sys_platform == "win32"
 Requires-Dist: pywinauto (>=0.6.8,<0.7.0); python_version < "3.7.6" and sys_platform == "win32" or python_version > "3.7.6" and python_version < "3.8.1" and sys_platform == "win32" or python_version > "3.8.1" and sys_platform == "win32"
 Requires-Dist: robotframework (>=4.0.0,!=4.0.1,<5.0.0)
-Requires-Dist: robotframework-browser (>=2.5.0,<3.0.0); (python_version >= "3.7" and python_version < "4.0") and (extra == "playwright")
+Requires-Dist: robotframework-browser (>=4.3.0,<5.0.0); (python_version >= "3.7" and python_version < "4.0") and (extra == "playwright")
 Requires-Dist: robotframework-pythonlibcore (>=2.1.0,<3.0.0)
 Requires-Dist: robotframework-requests (>=0.7.0,<0.8.0)
 Requires-Dist: robotframework-sapguilibrary (>=1.1,<2.0); sys_platform == "win32"
 Requires-Dist: robotframework-seleniumlibrary (>=5.1.0,<6.0.0)
 Requires-Dist: robotframework-seleniumtestability (>=1.1.0,<2.0.0)
 Requires-Dist: rpaframework-core (>=6.2.0,<7.0.0)
 Requires-Dist: rpaframework-pdf (>=0.5.0,<0.6.0)
```

