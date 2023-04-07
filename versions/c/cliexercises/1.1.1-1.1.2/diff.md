# Comparing `tmp/cliexercises-1.1.1.tar.gz` & `tmp/cliexercises-1.1.2.tar.gz`

## Comparing `cliexercises-1.1.1.tar` & `cliexercises-1.1.2.tar`

### file list

```diff
@@ -1,65 +1,65 @@
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/__init__.py
--rw-r--r--   0        0        0      336 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/cli_exercises.css
--rw-r--r--   0        0        0     7258 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/cli_exercises.py
--rw-r--r--   0        0        0    10752 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/questions.json
--rw-r--r--   0        0        0       19 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/user_progress.json
--rw-r--r--   0        0        0      100 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/anchors.txt
--rw-r--r--   0        0        0       61 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/blocks.txt
--rw-r--r--   0        0        0       40 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/colors.txt
--rw-r--r--   0        0        0      151 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/duplicates.txt
--rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/file_size.txt
--rw-r--r--   0        0        0       87 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/fruits.txt
--rw-r--r--   0        0        0       25 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/greeting.txt
--rw-r--r--   0        0        0       76 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/ip.txt
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/nums_1.txt
--rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/nums_2.txt
--rw-r--r--   0        0        0       57 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/purchases.txt
--rw-r--r--   0        0        0      119 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/range.txt
--rw-r--r--   0        0        0      183 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/sample.txt
--rw-r--r--   0        0        0       79 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/table.txt
--rw-r--r--   0        0        0       49 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/timings.txt
--rw-r--r--   0        0        0       69 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/varying_fields.csv
--rw-r--r--   0        0        0       70 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/anchors_to_links.txt
--rw-r--r--   0        0        0       61 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/block_reverse.txt
--rw-r--r--   0        0        0       60 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/char_range.txt
--rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/column_product.txt
--rw-r--r--   0        0        0       59 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/delete_regex_range.txt
--rw-r--r--   0        0        0       61 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/divide_into_two_and_paste.txt
--rw-r--r--   0        0        0        2 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/empty_lines.txt
--rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/except_field_x.csv
--rw-r--r--   0        0        0       33 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/except_first_five_lines.txt
--rw-r--r--   0        0        0       30 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/except_x_or_y.txt
--rw-r--r--   0        0        0       33 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/extract_whole_words.txt
--rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/field_duplicates.txt
--rw-r--r--   0        0        0       17 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/field_serialize.csv
--rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/fifth_ninth_bytes.txt
--rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/filter_fields_align.csv
--rw-r--r--   0        0        0       42 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/first_five_lines.txt
--rw-r--r--   0        0        0       57 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/join_lines.txt
--rw-r--r--   0        0        0       32 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/last_x_chars.txt
--rw-r--r--   0        0        0       70 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/lines_till_first_match.txt
--rw-r--r--   0        0        0       69 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/match_x_and_line_before.txt
--rw-r--r--   0        0        0       27 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/match_x_but_not_y.txt
--rw-r--r--   0        0        0        3 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/max_display_width.txt
--rw-r--r--   0        0        0       55 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/more_than_2_vowels.txt
--rw-r--r--   0        0        0       60 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/multi_replace.txt
--rw-r--r--   0        0        0        3 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/number_of_words.txt
--rw-r--r--   0        0        0       20 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/para_digits.txt
--rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/remove_line_number_range.txt
--rw-r--r--   0        0        0       35 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/replace_except_first_two.txt
--rw-r--r--   0        0        0       69 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/reshape.txt
--rw-r--r--   0        0        0       44 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/retain_only_alnum_space.txt
--rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/sort_column_unique.txt
--rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/sort_general.txt
--rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/sort_human_reverse.txt
--rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/sort_numbers.txt
--rw-r--r--   0        0        0       49 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/sort_version.txt
--rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/sorted_count.txt
--rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/starts_x_ends_y_z.txt
--rw-r--r--   0        0        0       17 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/third_block.txt
--rw-r--r--   0        0        0       32 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/third_first.csv
--rw-r--r--   0        0        0       38 2020-02-02 00:00:00.000000 cliexercises-1.1.1/src/cliexercises/sample_input/expected_output/unique_2_chars.txt
--rw-r--r--   0        0        0     1072 2020-02-02 00:00:00.000000 cliexercises-1.1.1/LICENSE
--rw-r--r--   0        0        0     3696 2020-02-02 00:00:00.000000 cliexercises-1.1.1/README.md
--rw-r--r--   0        0        0      759 2020-02-02 00:00:00.000000 cliexercises-1.1.1/pyproject.toml
--rw-r--r--   0        0        0     4317 2020-02-02 00:00:00.000000 cliexercises-1.1.1/PKG-INFO
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/__init__.py
+-rw-r--r--   0        0        0      336 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/cli_exercises.css
+-rw-r--r--   0        0        0     7371 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/cli_exercises.py
+-rw-r--r--   0        0        0    10752 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/questions.json
+-rw-r--r--   0        0        0       19 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/user_progress.json
+-rw-r--r--   0        0        0      100 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/anchors.txt
+-rw-r--r--   0        0        0       61 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/blocks.txt
+-rw-r--r--   0        0        0       40 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/colors.txt
+-rw-r--r--   0        0        0      151 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/duplicates.txt
+-rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/file_size.txt
+-rw-r--r--   0        0        0       87 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/fruits.txt
+-rw-r--r--   0        0        0       25 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/greeting.txt
+-rw-r--r--   0        0        0       76 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/ip.txt
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/nums_1.txt
+-rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/nums_2.txt
+-rw-r--r--   0        0        0       57 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/purchases.txt
+-rw-r--r--   0        0        0      119 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/range.txt
+-rw-r--r--   0        0        0      183 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/sample.txt
+-rw-r--r--   0        0        0       79 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/table.txt
+-rw-r--r--   0        0        0       49 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/timings.txt
+-rw-r--r--   0        0        0       69 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/varying_fields.csv
+-rw-r--r--   0        0        0       70 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/anchors_to_links.txt
+-rw-r--r--   0        0        0       61 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/block_reverse.txt
+-rw-r--r--   0        0        0       60 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/char_range.txt
+-rw-r--r--   0        0        0        8 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/column_product.txt
+-rw-r--r--   0        0        0       59 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/delete_regex_range.txt
+-rw-r--r--   0        0        0       61 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/divide_into_two_and_paste.txt
+-rw-r--r--   0        0        0        2 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/empty_lines.txt
+-rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/except_field_x.csv
+-rw-r--r--   0        0        0       33 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/except_first_five_lines.txt
+-rw-r--r--   0        0        0       30 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/except_x_or_y.txt
+-rw-r--r--   0        0        0       33 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/extract_whole_words.txt
+-rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/field_duplicates.txt
+-rw-r--r--   0        0        0       17 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/field_serialize.csv
+-rw-r--r--   0        0        0        5 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/fifth_ninth_bytes.txt
+-rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/filter_fields_align.csv
+-rw-r--r--   0        0        0       42 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/first_five_lines.txt
+-rw-r--r--   0        0        0       57 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/join_lines.txt
+-rw-r--r--   0        0        0       32 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/last_x_chars.txt
+-rw-r--r--   0        0        0       70 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/lines_till_first_match.txt
+-rw-r--r--   0        0        0       69 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/match_x_and_line_before.txt
+-rw-r--r--   0        0        0       27 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/match_x_but_not_y.txt
+-rw-r--r--   0        0        0        3 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/max_display_width.txt
+-rw-r--r--   0        0        0       55 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/more_than_2_vowels.txt
+-rw-r--r--   0        0        0       60 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/multi_replace.txt
+-rw-r--r--   0        0        0        3 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/number_of_words.txt
+-rw-r--r--   0        0        0       20 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/para_digits.txt
+-rw-r--r--   0        0        0       54 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/remove_line_number_range.txt
+-rw-r--r--   0        0        0       35 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/replace_except_first_two.txt
+-rw-r--r--   0        0        0       69 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/reshape.txt
+-rw-r--r--   0        0        0       44 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/retain_only_alnum_space.txt
+-rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/sort_column_unique.txt
+-rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/sort_general.txt
+-rw-r--r--   0        0        0       84 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/sort_human_reverse.txt
+-rw-r--r--   0        0        0       13 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/sort_numbers.txt
+-rw-r--r--   0        0        0       49 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/sort_version.txt
+-rw-r--r--   0        0        0       41 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/sorted_count.txt
+-rw-r--r--   0        0        0       39 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/starts_x_ends_y_z.txt
+-rw-r--r--   0        0        0       17 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/third_block.txt
+-rw-r--r--   0        0        0       32 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/third_first.csv
+-rw-r--r--   0        0        0       38 2020-02-02 00:00:00.000000 cliexercises-1.1.2/src/cliexercises/sample_input/expected_output/unique_2_chars.txt
+-rw-r--r--   0        0        0     1072 2020-02-02 00:00:00.000000 cliexercises-1.1.2/LICENSE
+-rw-r--r--   0        0        0     3696 2020-02-02 00:00:00.000000 cliexercises-1.1.2/README.md
+-rw-r--r--   0        0        0      759 2020-02-02 00:00:00.000000 cliexercises-1.1.2/pyproject.toml
+-rw-r--r--   0        0        0     4317 2020-02-02 00:00:00.000000 cliexercises-1.1.2/PKG-INFO
```

### Comparing `cliexercises-1.1.1/src/cliexercises/cli_exercises.py` & `cliexercises-1.1.2/src/cliexercises/cli_exercises.py`

 * *Files 4% similar despite different names*

```diff
@@ -8,42 +8,44 @@
 
 import json
 import subprocess
 from functools import partial
 import os
 from pathlib import Path
 
+SCRIPT_DIR = Path(__file__).parent.resolve()
+
 class CLIExercisesApp(App):
-    CSS_PATH = 'cli_exercises.css'
+    CSS_PATH = SCRIPT_DIR.joinpath('cli_exercises.css')
     BINDINGS = [
         Binding('ctrl+s', 'show_answer', 'Solution', show=True),
         Binding('ctrl+p', 'previous', 'Prev', show=True),
         Binding('ctrl+n', 'next', 'Next', show=True),
         ('ctrl+t', 'toggle_theme', 'Theme'),
         ('ctrl+q', 'app.quit', 'Quit'),
     ]
 
     def __init__(self):
         super().__init__()
 
-        with open('questions.json', encoding='ascii') as f:
+        with open(SCRIPT_DIR.joinpath('questions.json'), encoding='ascii') as f:
             self.questions = tuple(json.load(f).values())
         self.q_idx = 0
         self.q_max_idx = len(self.questions) - 1
 
         self.question = Label(id='question')
         self.sample_input = Label(classes='ip_op')
         self.expected_output = Label(classes='ip_op')
 
         placeholder = 'Type your command here. Press Enter to execute the command.'
         self.user_cmd_input = Input(placeholder=placeholder)
         self.user_cmd_output = Label(id='user_cmd_output')
         self.op_panel = partial(Panel, title='Output', title_align='left')
 
-        self.progress_file = 'user_progress.json'
+        self.progress_file = SCRIPT_DIR.joinpath('user_progress.json')
         try:
             with open(self.progress_file, encoding='ascii') as f:
                 self.user_progress = {int(k): v for k,v in json.load(f).items()}
         except FileNotFoundError:
             self.user_progress = {}
         else:
             for idx in range(self.q_max_idx + 1):
@@ -175,13 +177,13 @@
     def action_toggle_theme(self):
         self.dark = not self.dark
         self.user_progress[-1] = self.dark
         self.write_progress_file()
 
 
 def main():
-    os.chdir(Path(__file__).parent.resolve())
+    os.chdir(SCRIPT_DIR.joinpath('sample_input'))
     app = CLIExercisesApp()
     app.run()
 
 if __name__ == '__main__':
     main()
```

### Comparing `cliexercises-1.1.1/src/cliexercises/questions.json` & `cliexercises-1.1.2/src/cliexercises/questions.json`

 * *Files identical despite different names*

### Comparing `cliexercises-1.1.1/LICENSE` & `cliexercises-1.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `cliexercises-1.1.1/README.md` & `cliexercises-1.1.2/README.md`

 * *Files identical despite different names*

### Comparing `cliexercises-1.1.1/pyproject.toml` & `cliexercises-1.1.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "cliexercises"
-version = "1.1.1"
+version = "1.1.2"
 authors = [
   { name="Sundeep Agarwal", email="learnbyexample.net@gmail.com" },
 ]
 description = "40 beginner to intermediate level questions on CLI text processing tasks"
 readme = "README.md"
 requires-python = ">=3.8"
 classifiers = [
```

### Comparing `cliexercises-1.1.1/PKG-INFO` & `cliexercises-1.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: cliexercises
-Version: 1.1.1
+Version: 1.1.2
 Summary: 40 beginner to intermediate level questions on CLI text processing tasks
 Project-URL: Source, https://github.com/learnbyexample/TUI-apps/tree/main/CLI-Exercises
 Project-URL: Issues, https://github.com/learnbyexample/TUI-apps/issues
 Author-email: Sundeep Agarwal <learnbyexample.net@gmail.com>
 License-File: LICENSE
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

