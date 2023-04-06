# Comparing `tmp/variation-normalizer-0.7.0.dev4.tar.gz` & `tmp/variation-normalizer-0.7.dev0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "variation-normalizer-0.7.0.dev4.tar", last modified: Thu Apr  6 18:11:39 2023, max compression
+gzip compressed data, was "variation-normalizer-0.7.dev0.tar", last modified: Mon Oct  3 15:18:18 2022, max compression
```

## Comparing `variation-normalizer-0.7.0.dev4.tar` & `variation-normalizer-0.7.dev0.tar`

### file list

```diff
@@ -1,266 +1,270 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.820805 variation-normalizer-0.7.0.dev4/
--rw-r--r--   0 runner    (1001) docker     (123)     1062 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     7720 2023-04-06 18:11:39.820805 variation-normalizer-0.7.0.dev4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     6991 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     1356 2023-04-06 18:11:39.820805 variation-normalizer-0.7.0.dev4/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      156 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.732805 variation-normalizer-0.7.0.dev4/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       97 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.740805 variation-normalizer-0.7.0.dev4/tests/classifiers/
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1787 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/classifier_base.py
--rw-r--r--   0 runner    (1001) docker     (123)      545 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_amplification.py
--rw-r--r--   0 runner    (1001) docker     (123)      587 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_coding_dna_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      571 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_coding_dna_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      595 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_coding_dna_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      638 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_coding_dna_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      619 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_coding_dna_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      568 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      647 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_deletion_range.py
--rw-r--r--   0 runner    (1001) docker     (123)      552 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      592 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_duplication.py
--rw-r--r--   0 runner    (1001) docker     (123)      576 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      619 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      603 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      683 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_uncertain_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      616 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_polypeptide_truncation.py
--rw-r--r--   0 runner    (1001) docker     (123)      568 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_protein_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      552 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_protein_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      576 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_protein_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      600 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_protein_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      560 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/classifiers/test_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)    38480 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)     1287 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/test_codon_table.py
--rw-r--r--   0 runner    (1001) docker     (123)    30398 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/test_gnomad_vcf_to_protein.py
--rw-r--r--   0 runner    (1001) docker     (123)   131346 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/test_hgvs_dup_del_mode.py
--rw-r--r--   0 runner    (1001) docker     (123)    54650 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/test_normalize.py
--rw-r--r--   0 runner    (1001) docker     (123)    19325 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/test_to_canonical_variation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.756805 variation-normalizer-0.7.0.dev4/tests/tokenizers/
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      721 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_amplification.py
--rw-r--r--   0 runner    (1001) docker     (123)      674 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_coding_dna_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      727 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_coding_dna_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      757 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_coding_dna_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      740 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_coding_dna_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      714 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_coding_dna_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      660 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_gene.py
--rw-r--r--   0 runner    (1001) docker     (123)      566 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_gene_pair.py
--rw-r--r--   0 runner    (1001) docker     (123)      651 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      705 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_deletion_range.py
--rw-r--r--   0 runner    (1001) docker     (123)      701 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      678 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_duplication.py
--rw-r--r--   0 runner    (1001) docker     (123)      700 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_duplication_range.py
--rw-r--r--   0 runner    (1001) docker     (123)      731 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      718 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      688 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      744 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_uncertain_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)     3999 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_gnomad_vcf.py
--rw-r--r--   0 runner    (1001) docker     (123)      528 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_hgvs.py
--rw-r--r--   0 runner    (1001) docker     (123)      610 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_locus_reference_genomic.py
--rw-r--r--   0 runner    (1001) docker     (123)      709 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_polypeptide_truncation.py
--rw-r--r--   0 runner    (1001) docker     (123)      648 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_protein_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      701 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_protein_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      731 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_protein_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      688 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_protein_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      638 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/test_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1537 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/tokenizers/tokenizer_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.764805 variation-normalizer-0.7.0.dev4/tests/translators/
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      936 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_coding_dna_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      922 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_coding_dna_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      948 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_coding_dna_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)     1025 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_coding_dna_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      994 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_coding_dna_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      902 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      895 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      938 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_duplication.py
--rw-r--r--   0 runner    (1001) docker     (123)      915 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      998 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      955 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)     1070 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_uncertain_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      980 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_polypeptide_truncation.py
--rw-r--r--   0 runner    (1001) docker     (123)      904 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_protein_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      878 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_protein_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      917 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_protein_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      960 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_protein_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      889 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/test_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)     4010 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/translators/translator_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.772805 variation-normalizer-0.7.0.dev4/tests/validators/
--rw-r--r--   0 runner    (1001) docker     (123)       34 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      770 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_coding_dna_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      750 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_coding_dna_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      781 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_coding_dna_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      844 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_coding_dna_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      816 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_coding_dna_subsitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      743 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      721 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      777 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_duplication.py
--rw-r--r--   0 runner    (1001) docker     (123)      754 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      816 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      788 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      849 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_uncertain_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      813 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_polypeptide_truncation.py
--rw-r--r--   0 runner    (1001) docker     (123)      747 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_protein_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_protein_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      758 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_protein_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      798 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_protein_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      736 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/test_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)     3734 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/tests/validators/validator_base.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.780805 variation-normalizer-0.7.0.dev4/variation/
--rw-r--r--   0 runner    (1001) docker     (123)     1386 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.788805 variation-normalizer-0.7.0.dev4/variation/classifiers/
--rw-r--r--   0 runner    (1001) docker     (123)     1657 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      658 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/amplification_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      681 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     3042 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/classify.py
--rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/coding_dna_deletion_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      984 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/coding_dna_delins_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     1020 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/coding_dna_insertion_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     1084 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/coding_dna_silent_mutation_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     1056 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/coding_dna_substitution_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      994 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_deletion_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      983 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_deletion_range_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      914 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_delins_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     1244 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_duplication_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     1006 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_insertion_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     1006 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_silent_mutation_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      980 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_substitution_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     1027 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_uncertain_deletion_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      859 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/polypeptide_truncation_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      840 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/protein_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      980 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/protein_deletion_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      956 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/protein_delins_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      992 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/protein_insertion_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      741 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/protein_termination_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)     3574 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/set_based_classifier.py
--rw-r--r--   0 runner    (1001) docker     (123)      796 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/classifiers/silent_mutation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.788805 variation-normalizer-0.7.0.dev4/variation/data_sources/
--rw-r--r--   0 runner    (1001) docker     (123)       76 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/data_sources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2497 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/data_sources/codon_table.py
--rw-r--r--   0 runner    (1001) docker     (123)    18330 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/gnomad_vcf_to_protein_variation.py
--rw-r--r--   0 runner    (1001) docker     (123)    10787 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/hgvs_dup_del_mode.py
--rw-r--r--   0 runner    (1001) docker     (123)    30464 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/main.py
--rw-r--r--   0 runner    (1001) docker     (123)     4947 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/normalize.py
--rw-r--r--   0 runner    (1001) docker     (123)     4601 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/query.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.792805 variation-normalizer-0.7.0.dev4/variation/schemas/
--rw-r--r--   0 runner    (1001) docker     (123)      427 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/schemas/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      485 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/schemas/app_schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     2098 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/schemas/classification_response_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     4191 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/schemas/hgvs_to_copy_number_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)    11422 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/schemas/normalize_response_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     5355 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/schemas/service_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     4868 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/schemas/to_vrs_response_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)    19195 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/schemas/token_response_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     1197 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/schemas/validation_response_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)     4401 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/schemas/vrs_python_translator_schema.py
--rw-r--r--   0 runner    (1001) docker     (123)    13140 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/to_canonical_variation.py
--rw-r--r--   0 runner    (1001) docker     (123)    19087 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/to_copy_number_variation.py
--rw-r--r--   0 runner    (1001) docker     (123)    10351 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/to_vrs.py
--rw-r--r--   0 runner    (1001) docker     (123)     3488 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/to_vrsatile.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.800805 variation-normalizer-0.7.0.dev4/variation/tokenizers/
--rw-r--r--   0 runner    (1001) docker     (123)     1606 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.800805 variation-normalizer-0.7.0.dev4/variation/tokenizers/caches/
--rw-r--r--   0 runner    (1001) docker     (123)      105 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/caches/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      852 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/caches/nucleotide_cache.py
--rw-r--r--   0 runner    (1001) docker     (123)      718 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/coding_dna_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      550 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/coding_dna_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      580 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/coding_dna_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      768 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/coding_dna_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      759 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/coding_dna_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)     2186 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/deletion_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2149 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/deletion_range_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3614 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/delins_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1595 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/duplication_base.py
--rw-r--r--   0 runner    (1001) docker     (123)      957 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/free_text_categorical.py
--rw-r--r--   0 runner    (1001) docker     (123)     1286 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/gene_pair.py
--rw-r--r--   0 runner    (1001) docker     (123)     2166 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/gene_symbol.py
--rw-r--r--   0 runner    (1001) docker     (123)      699 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)     2312 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_deletion_range.py
--rw-r--r--   0 runner    (1001) docker     (123)      549 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)     5111 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_duplication.py
--rw-r--r--   0 runner    (1001) docker     (123)      563 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      758 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      749 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)     3913 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_uncertain_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)     4674 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/gnomad_vcf.py
--rw-r--r--   0 runner    (1001) docker     (123)     1837 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/hgvs.py
--rw-r--r--   0 runner    (1001) docker     (123)     3129 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/insertion_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2545 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/locus_reference_genomic.py
--rw-r--r--   0 runner    (1001) docker     (123)     1814 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/polypeptide_sequence_variation_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     3664 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/polypeptide_truncation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1081 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/protein_alternate.py
--rw-r--r--   0 runner    (1001) docker     (123)     3714 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/protein_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)     2587 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/protein_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)     2635 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/protein_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)     2856 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/protein_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      915 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/reference_sequence.py
--rw-r--r--   0 runner    (1001) docker     (123)     2779 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)     4538 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/single_nucleotide_variation_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     5115 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/tokenize.py
--rw-r--r--   0 runner    (1001) docker     (123)     7559 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/tokenize_base.py
--rw-r--r--   0 runner    (1001) docker     (123)      380 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/tokenizers/tokenizer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.808805 variation-normalizer-0.7.0.dev4/variation/translators/
--rw-r--r--   0 runner    (1001) docker     (123)     1131 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      700 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/amplification.py
--rw-r--r--   0 runner    (1001) docker     (123)      742 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/coding_dna_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      726 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/coding_dna_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      750 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/coding_dna_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      812 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/coding_dna_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      774 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/coding_dna_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      721 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/genomic_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      762 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/genomic_deletion_range.py
--rw-r--r--   0 runner    (1001) docker     (123)      705 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/genomic_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      843 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/genomic_duplication.py
--rw-r--r--   0 runner    (1001) docker     (123)      729 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/genomic_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      791 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/genomic_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)      753 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/genomic_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      820 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/genomic_uncertain_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      769 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/polypeptide_truncation.py
--rw-r--r--   0 runner    (1001) docker     (123)      721 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/protein_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)      705 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/protein_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)      729 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/protein_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      753 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/protein_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      713 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2407 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/translate.py
--rw-r--r--   0 runner    (1001) docker     (123)     1929 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/translators/translator.py
--rw-r--r--   0 runner    (1001) docker     (123)     6628 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.816805 variation-normalizer-0.7.0.dev4/variation/validators/
--rw-r--r--   0 runner    (1001) docker     (123)     1287 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5293 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/amplification.py
--rw-r--r--   0 runner    (1001) docker     (123)     5848 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/coding_dna_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)     5713 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/coding_dna_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)     2035 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/coding_dna_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)     4281 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/coding_dna_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)     6017 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/coding_dna_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)     4794 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/delins_base.py
--rw-r--r--   0 runner    (1001) docker     (123)    14651 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/duplication_deletion_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2494 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/genomic_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     8386 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/genomic_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)    11708 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/genomic_deletion_range.py
--rw-r--r--   0 runner    (1001) docker     (123)     5449 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/genomic_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)    15408 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/genomic_duplication.py
--rw-r--r--   0 runner    (1001) docker     (123)     1991 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/genomic_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)     4198 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/genomic_silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)     5903 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/genomic_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)    11701 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/genomic_uncertain_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)     7626 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/insertion_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     6324 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/polypeptide_sequence_variation_base.py
--rw-r--r--   0 runner    (1001) docker     (123)      971 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/polypeptide_truncation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1213 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/protein_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     7784 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/protein_deletion.py
--rw-r--r--   0 runner    (1001) docker     (123)     7170 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/protein_delins.py
--rw-r--r--   0 runner    (1001) docker     (123)     7231 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/protein_insertion.py
--rw-r--r--   0 runner    (1001) docker     (123)      961 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/protein_substitution.py
--rw-r--r--   0 runner    (1001) docker     (123)      921 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/silent_mutation.py
--rw-r--r--   0 runner    (1001) docker     (123)     9771 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/single_nucleotide_variation_base.py
--rw-r--r--   0 runner    (1001) docker     (123)     6672 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/validate.py
--rw-r--r--   0 runner    (1001) docker     (123)    30150 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/validators/validator.py
--rw-r--r--   0 runner    (1001) docker     (123)       27 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/version.py
--rw-r--r--   0 runner    (1001) docker     (123)    10889 2023-04-06 18:11:32.000000 variation-normalizer-0.7.0.dev4/variation/vrs_representation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:39.820805 variation-normalizer-0.7.0.dev4/variation_normalizer.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     7720 2023-04-06 18:11:39.000000 variation-normalizer-0.7.0.dev4/variation_normalizer.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    10589 2023-04-06 18:11:39.000000 variation-normalizer-0.7.0.dev4/variation_normalizer.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:11:39.000000 variation-normalizer-0.7.0.dev4/variation_normalizer.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:11:39.000000 variation-normalizer-0.7.0.dev4/variation_normalizer.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      344 2023-04-06 18:11:39.000000 variation-normalizer-0.7.0.dev4/variation_normalizer.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-06 18:11:39.000000 variation-normalizer-0.7.0.dev4/variation_normalizer.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.250050 variation-normalizer-0.7.dev0/
+-rw-r--r--   0 runner    (1001) docker     (121)     1062 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)     7389 2022-10-03 15:18:18.250050 variation-normalizer-0.7.dev0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     6682 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)     1303 2022-10-03 15:18:18.250050 variation-normalizer-0.7.dev0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)      156 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.150050 variation-normalizer-0.7.dev0/tests/
+-rw-r--r--   0 runner    (1001) docker     (121)       97 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.154050 variation-normalizer-0.7.dev0/tests/classifiers/
+-rw-r--r--   0 runner    (1001) docker     (121)       31 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1894 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/classifier_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)      545 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_amplification.py
+-rw-r--r--   0 runner    (1001) docker     (121)      587 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_coding_dna_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      571 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_coding_dna_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      595 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_coding_dna_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      638 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_coding_dna_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      619 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_coding_dna_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      568 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      647 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_deletion_range.py
+-rw-r--r--   0 runner    (1001) docker     (121)      552 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      592 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_duplication.py
+-rw-r--r--   0 runner    (1001) docker     (121)      576 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      619 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      603 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      683 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_uncertain_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      616 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_polypeptide_truncation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      568 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_protein_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      552 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_protein_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      576 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_protein_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      600 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_protein_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      560 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/classifiers/test_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    38453 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1358 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/test_codon_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30116 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/test_gnomad_vcf_to_protein.py
+-rw-r--r--   0 runner    (1001) docker     (121)   131374 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/test_hgvs_dup_del_mode.py
+-rw-r--r--   0 runner    (1001) docker     (121)    51679 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/test_normalize.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19337 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/test_to_canonical_variation.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.158050 variation-normalizer-0.7.dev0/tests/tokenizers/
+-rw-r--r--   0 runner    (1001) docker     (121)       30 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      721 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_amplification.py
+-rw-r--r--   0 runner    (1001) docker     (121)      781 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_coding_dna_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      761 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_coding_dna_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      791 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_coding_dna_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      740 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_coding_dna_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      714 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_coding_dna_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      660 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_gene.py
+-rw-r--r--   0 runner    (1001) docker     (121)      566 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_gene_pair.py
+-rw-r--r--   0 runner    (1001) docker     (121)      758 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      705 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_deletion_range.py
+-rw-r--r--   0 runner    (1001) docker     (121)      735 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      678 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_duplication.py
+-rw-r--r--   0 runner    (1001) docker     (121)      700 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_duplication_range.py
+-rw-r--r--   0 runner    (1001) docker     (121)      765 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      718 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      688 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      744 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_uncertain_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3999 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_gnomad_vcf.py
+-rw-r--r--   0 runner    (1001) docker     (121)      528 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_hgvs.py
+-rw-r--r--   0 runner    (1001) docker     (121)      610 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_locus_reference_genomic.py
+-rw-r--r--   0 runner    (1001) docker     (121)      780 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_polypeptide_truncation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      755 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_protein_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      735 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_protein_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      765 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_protein_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      759 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_protein_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      709 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/test_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1537 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/tokenizers/tokenizer_base.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.162050 variation-normalizer-0.7.dev0/tests/translators/
+-rw-r--r--   0 runner    (1001) docker     (121)       35 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      936 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_coding_dna_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      922 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_coding_dna_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      948 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_coding_dna_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1025 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_coding_dna_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      994 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_coding_dna_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      902 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_genomic_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      895 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_genomic_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      938 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_genomic_duplication.py
+-rw-r--r--   0 runner    (1001) docker     (121)      915 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_genomic_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      998 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_genomic_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      955 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_genomic_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1070 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_genomic_uncertain_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      980 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_polypeptide_truncation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      904 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_protein_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      878 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_protein_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      917 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_protein_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      960 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_protein_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      889 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/test_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4123 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/translators/translator_base.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.166050 variation-normalizer-0.7.dev0/tests/validators/
+-rw-r--r--   0 runner    (1001) docker     (121)       34 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      770 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_coding_dna_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      750 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_coding_dna_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      781 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_coding_dna_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      844 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_coding_dna_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      816 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_coding_dna_subsitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      743 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_genomic_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      721 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_genomic_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      777 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_genomic_duplication.py
+-rw-r--r--   0 runner    (1001) docker     (121)      754 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_genomic_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      816 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_genomic_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      788 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_genomic_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      849 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_genomic_uncertain_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      813 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_polypeptide_truncation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      747 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_protein_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      725 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_protein_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      758 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_protein_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      798 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_protein_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      736 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/test_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3847 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/tests/validators/validator_base.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.166050 variation-normalizer-0.7.dev0/variation/
+-rw-r--r--   0 runner    (1001) docker     (121)     2484 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.170050 variation-normalizer-0.7.dev0/variation/classifiers/
+-rw-r--r--   0 runner    (1001) docker     (121)     1657 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      658 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/amplification_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      681 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3042 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/classify.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1008 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/coding_dna_deletion_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      984 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/coding_dna_delins_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1020 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/coding_dna_insertion_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1084 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/coding_dna_silent_mutation_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1056 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/coding_dna_substitution_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      994 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/genomic_deletion_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      983 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/genomic_deletion_range_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      914 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/genomic_delins_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1244 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/genomic_duplication_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1006 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/genomic_insertion_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1006 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/genomic_silent_mutation_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      980 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/genomic_substitution_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1027 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/genomic_uncertain_deletion_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      859 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/polypeptide_truncation_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      840 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/protein_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      980 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/protein_deletion_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      956 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/protein_delins_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      992 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/protein_insertion_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      741 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/protein_termination_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3574 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/set_based_classifier.py
+-rw-r--r--   0 runner    (1001) docker     (121)      796 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/classifiers/silent_mutation.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.170050 variation-normalizer-0.7.dev0/variation/data/
+-rw-r--r--   0 runner    (1001) docker     (121)      315 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/data/amino_acids.csv
+-rw-r--r--   0 runner    (1001) docker     (121) 24138769 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/data/transcript_mapping.tsv
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.210050 variation-normalizer-0.7.dev0/variation/data_sources/
+-rw-r--r--   0 runner    (1001) docker     (121)       76 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/data_sources/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2673 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/data_sources/codon_table.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17902 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/gnomad_vcf_to_protein_variation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10733 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/hgvs_dup_del_mode.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30406 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/main.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5101 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/normalize.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5289 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/query.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.214050 variation-normalizer-0.7.dev0/variation/schemas/
+-rw-r--r--   0 runner    (1001) docker     (121)      427 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/schemas/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      485 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/schemas/app_schemas.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2098 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/schemas/classification_response_schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4193 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/schemas/hgvs_to_copy_number_schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11422 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/schemas/normalize_response_schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5359 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/schemas/service_schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4868 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/schemas/to_vrs_response_schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19165 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/schemas/token_response_schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1197 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/schemas/validation_response_schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4401 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/schemas/vrs_python_translator_schema.py
+-rw-r--r--   0 runner    (1001) docker     (121)    13308 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/to_canonical_variation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19085 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/to_copy_number_variation.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10501 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/to_vrs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3488 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/to_vrsatile.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.226050 variation-normalizer-0.7.dev0/variation/tokenizers/
+-rw-r--r--   0 runner    (1001) docker     (121)     1606 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.226050 variation-normalizer-0.7.dev0/variation/tokenizers/caches/
+-rw-r--r--   0 runner    (1001) docker     (121)      164 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/caches/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1651 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/caches/amino_acid_cache.py
+-rw-r--r--   0 runner    (1001) docker     (121)      847 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/caches/nucleotide_cache.py
+-rw-r--r--   0 runner    (1001) docker     (121)      570 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/coding_dna_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      550 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/coding_dna_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      580 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/coding_dna_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      768 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/coding_dna_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      759 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/coding_dna_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3246 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/deletion_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2149 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/deletion_range_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3770 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/delins_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1595 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/duplication_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)      957 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/free_text_categorical.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1286 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/gene_pair.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2166 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/gene_symbol.py
+-rw-r--r--   0 runner    (1001) docker     (121)      553 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/genomic_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2312 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/genomic_deletion_range.py
+-rw-r--r--   0 runner    (1001) docker     (121)      549 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/genomic_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5111 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/genomic_duplication.py
+-rw-r--r--   0 runner    (1001) docker     (121)      563 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/genomic_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      758 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/genomic_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      749 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/genomic_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3913 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/genomic_uncertain_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4674 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/gnomad_vcf.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1837 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/hgvs.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3285 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/insertion_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2545 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/locus_reference_genomic.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1885 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/polypeptide_sequence_variation_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3664 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/polypeptide_truncation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1193 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/protein_alternate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2614 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/protein_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2743 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/protein_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2791 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/protein_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2735 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/protein_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      915 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/reference_sequence.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2779 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4538 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/single_nucleotide_variation_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5496 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/tokenize.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7630 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/tokenize_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)      380 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/tokenizers/tokenizer.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.234050 variation-normalizer-0.7.dev0/variation/translators/
+-rw-r--r--   0 runner    (1001) docker     (121)     1131 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      700 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/amplification.py
+-rw-r--r--   0 runner    (1001) docker     (121)      742 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/coding_dna_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      726 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/coding_dna_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      750 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/coding_dna_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      812 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/coding_dna_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      774 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/coding_dna_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      721 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/genomic_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      762 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/genomic_deletion_range.py
+-rw-r--r--   0 runner    (1001) docker     (121)      705 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/genomic_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      843 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/genomic_duplication.py
+-rw-r--r--   0 runner    (1001) docker     (121)      729 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/genomic_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      791 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/genomic_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      753 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/genomic_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      820 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/genomic_uncertain_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      769 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/polypeptide_truncation.py
+-rw-r--r--   0 runner    (1001) docker     (121)      721 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/protein_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      705 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/protein_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)      729 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/protein_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      753 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/protein_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      713 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2407 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/translate.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1929 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/translators/translator.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6624 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.246050 variation-normalizer-0.7.dev0/variation/validators/
+-rw-r--r--   0 runner    (1001) docker     (121)     1287 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5278 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/amplification.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5848 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/coding_dna_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5713 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/coding_dna_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2035 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/coding_dna_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4281 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/coding_dna_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6017 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/coding_dna_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4794 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/delins_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)    14647 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/duplication_deletion_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2486 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/genomic_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8386 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/genomic_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11704 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/genomic_deletion_range.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5449 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/genomic_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15408 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/genomic_duplication.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1991 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/genomic_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4198 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/genomic_silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5903 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/genomic_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11701 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/genomic_uncertain_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7626 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/insertion_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6575 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/polypeptide_sequence_variation_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)      971 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/polypeptide_truncation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1411 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/protein_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7445 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/protein_deletion.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7435 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/protein_delins.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7465 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/protein_insertion.py
+-rw-r--r--   0 runner    (1001) docker     (121)      961 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/protein_substitution.py
+-rw-r--r--   0 runner    (1001) docker     (121)      921 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/silent_mutation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     9771 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/single_nucleotide_variation_base.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7052 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/validate.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30179 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/validators/validator.py
+-rw-r--r--   0 runner    (1001) docker     (121)       25 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/version.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11048 2022-10-03 15:18:09.000000 variation-normalizer-0.7.dev0/variation/vrs_representation.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-03 15:18:18.250050 variation-normalizer-0.7.dev0/variation_normalizer.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     7389 2022-10-03 15:18:18.000000 variation-normalizer-0.7.dev0/variation_normalizer.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)    10706 2022-10-03 15:18:18.000000 variation-normalizer-0.7.dev0/variation_normalizer.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-03 15:18:18.000000 variation-normalizer-0.7.dev0/variation_normalizer.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-03 15:18:18.000000 variation-normalizer-0.7.dev0/variation_normalizer.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)      212 2022-10-03 15:18:18.000000 variation-normalizer-0.7.dev0/variation_normalizer.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       16 2022-10-03 15:18:18.000000 variation-normalizer-0.7.dev0/variation_normalizer.egg-info/top_level.txt
```

### Comparing `variation-normalizer-0.7.0.dev4/LICENSE` & `variation-normalizer-0.7.dev0/LICENSE`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/PKG-INFO` & `variation-normalizer-0.7.dev0/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 Metadata-Version: 2.1
 Name: variation-normalizer
-Version: 0.7.0.dev4
+Version: 0.7.dev0
 Summary: VICC normalization routine for variations
 Home-page: https://github.com/cancervariants/variation-normalization
 Author: VICC
 Author-email: help@cancervariants.org
 License: MIT
-Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Scientific/Engineering :: Bio-Informatics
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
@@ -48,15 +47,15 @@
 
 We are working towards adding more types of variations, coordinates, and representations.
 
 ### Endpoints
 
 The `/to_vrs` endpoint returns a list of validated VRS [Variations](https://vrs.ga4gh.org/en/1.2.0/terms_and_model.html#variation).
 
-The `/normalize` endpoint returns a [Variation Descriptor](https://vrsatile.readthedocs.io/en/latest/value_object_descriptor/vod_index.html#variation-descriptor) containing the MANE Transcript, if one is found. If a genomic query is not given a gene, `normalize` will return its GRCh38 representation. Variation Normalizer relies on [**C**ommon **O**perations **O**n **L**ots-of **Seq**uences Tool (cool-seq-tool)](https://github.com/GenomicMedLab/cool-seq-tool) for retrieving MANE Transcript data. More information on the transcript selection algorithm can be found [here](https://github.com/GenomicMedLab/cool-seq-tool/blob/main/docs/TranscriptSelectionPriority.md).
+The `/normalize` endpoint returns a [Variation Descriptor](https://vrsatile.readthedocs.io/en/latest/value_object_descriptor/vod_index.html#variation-descriptor) containing the MANE Transcript, if one is found. If a genomic query is not given a gene, `normalize` will return its GRCh38 representation. Variation Normalizer relies on [UTA Tools](https://github.com/GenomicMedLab/uta-tools) for retrieving MANE Transcript data. More information on the transcript selection algorithm can be found [here](https://github.com/GenomicMedLab/uta-tools/blob/main/docs/TranscriptSelectionPriority.md).
 
 ## Developer Instructions
 
 Clone the repo:
 ```
 git clone https://github.com/cancervariants/variation-normalization.git
 cd variation-normalization
@@ -107,18 +106,16 @@
 You will want to do the following:\
 (*Might not be ._fkuefgd, so replace with your error message path*)
 ```console
 sudo mv /usr/local/share/seqrepo/2021-01-29._fkuefgd /usr/local/share/seqrepo/2021-01-29
 exit
 ```
 
-Use the `SEQREPO_ROOT_DIR` environment variable to set the path of an already existing SeqRepo directory. The default is `/usr/local/share/seqrepo/latest`.
-
 #### UTA
-Variation Normalizer also uses [**C**ommon **O**perations **O**n **L**ots-of **Seq**uences Tool (cool-seq-tool)](https://github.com/GenomicMedLab/cool-seq-tool) which uses [UTA](https://github.com/biocommons/uta) as the underlying PostgreSQL database.
+Variation Normalizer also uses [UTA Tools](https://github.com/GenomicMedLab/uta-tools) which uses [UTA](https://github.com/biocommons/uta) as the underlying PostgreSQL database.
 
 _The following commands will likely need modification appropriate for the installation environment._
 1. Install [PostgreSQL](https://www.postgresql.org/)
 2. Create user and database.
 
     ```
     $ createuser -U postgres uta_admin
@@ -172,9 +169,7 @@
 ```
 
 ### Testing
 From the _root_ directory of the repository:
 ```
 pytest tests/
 ```
-
-
```

### Comparing `variation-normalizer-0.7.0.dev4/README.md` & `variation-normalizer-0.7.dev0/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -27,15 +27,15 @@
 
 We are working towards adding more types of variations, coordinates, and representations.
 
 ### Endpoints
 
 The `/to_vrs` endpoint returns a list of validated VRS [Variations](https://vrs.ga4gh.org/en/1.2.0/terms_and_model.html#variation).
 
-The `/normalize` endpoint returns a [Variation Descriptor](https://vrsatile.readthedocs.io/en/latest/value_object_descriptor/vod_index.html#variation-descriptor) containing the MANE Transcript, if one is found. If a genomic query is not given a gene, `normalize` will return its GRCh38 representation. Variation Normalizer relies on [**C**ommon **O**perations **O**n **L**ots-of **Seq**uences Tool (cool-seq-tool)](https://github.com/GenomicMedLab/cool-seq-tool) for retrieving MANE Transcript data. More information on the transcript selection algorithm can be found [here](https://github.com/GenomicMedLab/cool-seq-tool/blob/main/docs/TranscriptSelectionPriority.md).
+The `/normalize` endpoint returns a [Variation Descriptor](https://vrsatile.readthedocs.io/en/latest/value_object_descriptor/vod_index.html#variation-descriptor) containing the MANE Transcript, if one is found. If a genomic query is not given a gene, `normalize` will return its GRCh38 representation. Variation Normalizer relies on [UTA Tools](https://github.com/GenomicMedLab/uta-tools) for retrieving MANE Transcript data. More information on the transcript selection algorithm can be found [here](https://github.com/GenomicMedLab/uta-tools/blob/main/docs/TranscriptSelectionPriority.md).
 
 ## Developer Instructions
 
 Clone the repo:
 ```
 git clone https://github.com/cancervariants/variation-normalization.git
 cd variation-normalization
@@ -86,18 +86,16 @@
 You will want to do the following:\
 (*Might not be ._fkuefgd, so replace with your error message path*)
 ```console
 sudo mv /usr/local/share/seqrepo/2021-01-29._fkuefgd /usr/local/share/seqrepo/2021-01-29
 exit
 ```
 
-Use the `SEQREPO_ROOT_DIR` environment variable to set the path of an already existing SeqRepo directory. The default is `/usr/local/share/seqrepo/latest`.
-
 #### UTA
-Variation Normalizer also uses [**C**ommon **O**perations **O**n **L**ots-of **Seq**uences Tool (cool-seq-tool)](https://github.com/GenomicMedLab/cool-seq-tool) which uses [UTA](https://github.com/biocommons/uta) as the underlying PostgreSQL database.
+Variation Normalizer also uses [UTA Tools](https://github.com/GenomicMedLab/uta-tools) which uses [UTA](https://github.com/biocommons/uta) as the underlying PostgreSQL database.
 
 _The following commands will likely need modification appropriate for the installation environment._
 1. Install [PostgreSQL](https://www.postgresql.org/)
 2. Create user and database.
 
     ```
     $ createuser -U postgres uta_admin
```

### Comparing `variation-normalizer-0.7.0.dev4/setup.cfg` & `variation-normalizer-0.7.dev0/setup.cfg`

 * *Files 19% similar despite different names*

```diff
@@ -23,41 +23,37 @@
 zip_safe = False
 include_package_data = True
 install_requires = 
 	biocommons.seqrepo
 	fastapi
 	uvicorn
 	pydantic
-	ga4gh.vrs[extras] >= 0.9.0.dev0
-	gene-normalizer >= 0.2.8
+	ga4gh.vrs[extras] >= 0.8.7dev0
+	gene-normalizer >= 0.2.3
 	pyliftover
 	boto3
-	ga4gh.vrsatile.pydantic >= 0.1.0.dev7
-	cool-seq-tool >= 0.1.11
-	bioutils
+	ga4gh.vrsatile.pydantic >= 0.1.dev3
+	uta-tools >= 0.1.2
 tests_require = 
 	pytest
 	pytest-cov
 	pyyaml
 	pytest-asyncio
 
+[options.package_data]
+variation = 
+	data/amino_acids.csv
+	data/transcript_mapping.tsv
+
 [options.extras_require]
 dev = 
 	pytest
 	pytest-cov
+	pyyaml
 	psycopg2-binary
-	pytest-asyncio
-	flake8
-	flake8-docstrings
-	flake8-quotes
-	flake8-annotations
-	flake8-import-order
-	pre-commit
-	jupyter
-	ipykernel
 
 [tool:pytest]
 addopts = --ignore setup.py --ignore=codebuild/ --doctest-modules --cov-report term-missing --cov .
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/classifier_base.py` & `variation-normalizer-0.7.dev0/tests/classifiers/classifier_base.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,29 +1,31 @@
 """A module for testing classifier classes."""
 import yaml
 from gene.query import QueryHandler as GeneQueryHandler
 
 from variation.tokenizers import Tokenize
-from variation.tokenizers import GeneSymbol
 from tests import PROJECT_ROOT
+from variation.tokenizers.caches import AminoAcidCache
+from variation.tokenizers import GeneSymbol
 
 
 class ClassifierBase:
     """The classifier base class."""
 
     def setUp(self):
         """Set up the test cases."""
         with open(f"{PROJECT_ROOT}/tests/fixtures/classifiers.yml") as stream:
             self.all_fixtures = yaml.safe_load(stream)
         self.fixtures = self.all_fixtures.get(
             self.fixture_name(),
             {"should_match": [], "should_not_match": []}
         )
         self.classifier = self.classifier_instance()
-        self.tokenizer = Tokenize(GeneSymbol(GeneQueryHandler()))
+        self.tokenizer = Tokenize(AminoAcidCache(),
+                                  GeneSymbol(GeneQueryHandler()))
 
     def classifier_instance(self):
         """Check that the classifier_instance method is implemented."""
         raise NotImplementedError()
 
     def fixture_name(self):
         """Check that the fixture_name method is implemented."""
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_amplification.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_amplification.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_coding_dna_deletion.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_coding_dna_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_coding_dna_delins.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_coding_dna_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_coding_dna_insertion.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_coding_dna_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_coding_dna_silent_mutation.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_coding_dna_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_coding_dna_substitution.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_coding_dna_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_deletion.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_deletion_range.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_deletion_range.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_delins.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_duplication.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_duplication.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_insertion.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_silent_mutation.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_substitution.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_genomic_uncertain_deletion.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_genomic_uncertain_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_polypeptide_truncation.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_polypeptide_truncation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_protein_deletion.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_protein_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_protein_delins.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_protein_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_protein_insertion.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_protein_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_protein_substitution.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_protein_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/classifiers/test_silent_mutation.py` & `variation-normalizer-0.7.dev0/tests/classifiers/test_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/conftest.py` & `variation-normalizer-0.7.dev0/tests/conftest.py`

 * *Files 1% similar despite different names*

```diff
@@ -64,15 +64,14 @@
                     "pubmed:9671762",
                     "refseq:NM_000551",
                     "cosmic:VHL",
                     "omim:608537",
                     "vega:OTTHUMG00000128668",
                     "ccds:CCDS2598",
                     "ena.embl:L15409",
-                    "iuphar:3204",
                     "orphanet:120467",
                     "ccds:CCDS2597",
                     "uniprot:P40337"
                 ]
             },
             {
                 "type": "Extension",
@@ -1016,17 +1015,17 @@
 @pytest.fixture(scope="session")
 def braf_amplification(braf_ncbi_seq_loc, braf_gene_context):
     """Create test fixture for BRAF Amplification"""
     params = {
         "id": "normalize.variation:BRAF%20Amplification",
         "type": "VariationDescriptor",
         "variation": {
-            "id": "ga4gh:RCN.tXX8oMzsJx3r9ZlqQlzk_K8Luz-bswdT",
+            "id": "ga4gh:RCN.avsI73-9i6ykDIRB3eB89jeU1lhyBbYt",
             "location": braf_ncbi_seq_loc,
-            "relative_copy_class": "EFO:0030072",
+            "relative_copy_class": "high-level gain",
             "type": "RelativeCopyNumber"
         },
         "molecule_context": "genomic",
         "structural_type": "SO:0001880",
         "gene_context": braf_gene_context
     }
     return VariationDescriptor(**params)
@@ -1035,17 +1034,17 @@
 @pytest.fixture(scope="session")
 def prpf8_amplification(prpf8_ncbi_seq_loc, prpf8_gene_context):
     """Create test fixture for PRPF8 Amplification"""
     params = {
         "id": "normalize.variation:PRPF8%20AMPLIFICATION",
         "type": "VariationDescriptor",
         "variation": {
-            "id": "ga4gh:RCN.DW0vRfIA0aI4AR0epEh_k-qrB2pdpZVw",
+            "id": "ga4gh:RCN.w44H1MxQusrCBDxUoLr30E1iJBMGXF14",
             "location": prpf8_ncbi_seq_loc,
-            "relative_copy_class": "EFO:0030072",
+            "relative_copy_class": "high-level gain",
             "type": "RelativeCopyNumber"
         },
         "molecule_context": "genomic",
         "structural_type": "SO:0001880",
         "gene_context": prpf8_gene_context
     }
     return VariationDescriptor(**params)
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/test_codon_table.py` & `variation-normalizer-0.7.dev0/tests/test_codon_table.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,17 +1,18 @@
 """Module for testing Codon Table class."""
 import pytest
 
 from variation.data_sources.codon_table import CodonTable
+from variation.tokenizers.caches import AminoAcidCache
 
 
 @pytest.fixture(scope="module")
 def test_codon_table():
     """Build codon table test fixture."""
-    return CodonTable()
+    return CodonTable(AminoAcidCache())
 
 
 def test_get_codons(test_codon_table):
     """Test that _get_codons method works correctly."""
     ala_codons = ["GCA", "GCC", "GCG", "GCU"]
     assert test_codon_table.get_codons("A") == ala_codons
     assert test_codon_table.get_codons("a") == ala_codons
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/test_gnomad_vcf_to_protein.py` & `variation-normalizer-0.7.dev0/tests/test_gnomad_vcf_to_protein.py`

 * *Files 2% similar despite different names*

```diff
@@ -794,17 +794,16 @@
     variation = resp.variation_descriptor.dict()["variation"]
     assert variation == kras_g12d
 
 
 @pytest.mark.asyncio
 async def test_silent_mutation(test_handler, vhl_silent):
     """Test that silent queries return correct response"""
-    # https://www.ncbi.nlm.nih.gov/clinvar/variation/379039/?new_evidence=true
-    resp = await test_handler.gnomad_vcf_to_protein("3-10142030-C-C")
-    assertion_checks(resp.variation_descriptor, vhl_silent, "3-10142030-C-C",
+    resp = await test_handler.gnomad_vcf_to_protein("3-10183714-C-C")
+    assertion_checks(resp.variation_descriptor, vhl_silent, "3-10183714-C-C",
                      ignore_id=True)
     assert resp.warnings == []
 
 
 @pytest.mark.asyncio
 async def test_insertion(test_handler, protein_insertion,
                          protein_insertion2):
@@ -847,19 +846,16 @@
     assert resp.warnings == ["BRAF V600E is not a supported gnomad vcf query"]
 
     resp = await test_handler.gnomad_vcf_to_protein("7-140753336-T-G",
                                                     untranslatable_returns_text=True)
     assert resp.variation_descriptor.variation.type == "Text"
     assert resp.variation_descriptor.label == "7-140753336-T-G"
     assert set(resp.warnings) == {
+        "Unable to get transcripts given NC_000007.13 and 140753336",
         "Expected T but found A on NC_000007.14 at position 140753336",
-        "Unable to get MANE data for NM_004333.6 using NC_000007.13 at positions"
-        " 140753335 to 140753335",  # MANE Select
-        "Unable to get MANE data for NM_001374258.1 using NC_000007.13 at positions"
-        " 140753335 to 140753335"  # MANE Plus Clinical
     }
 
     resp = await test_handler.gnomad_vcf_to_protein("20-2-TC-TG",
                                                     untranslatable_returns_text=True)
     assert resp.variation_descriptor.variation.type == "Text"
     assert resp.variation_descriptor.label == "20-2-TC-TG"
     assert resp.warnings == ["Unable to get protein variation for 20-2-TC-TG"]
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/test_hgvs_dup_del_mode.py` & `variation-normalizer-0.7.dev0/tests/test_hgvs_dup_del_mode.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,8 @@
 """Module for testing HGVS Dup Del mode."""
-from copy import deepcopy
-
 import pytest
 from ga4gh.vrsatile.pydantic.vrsatile_models import VariationDescriptor
 
 from tests.conftest import assertion_checks
 
 
 @pytest.fixture(scope="module")
@@ -316,17 +314,17 @@
 
 
 @pytest.fixture(scope="module")
 def genomic_dup1_vrc(genomic_dup1, genomic_dup1_seq_loc):
     """Create a test fixture for genomic dup relative CNV."""
     genomic_dup1["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.UBQCyZ7lHIJN6FoQHp3gURfJSWN31S09",
+        "id": "ga4gh:RCN.qSnPCsf9ylOaecpSBjTkxWFqxmmyYWtL",
         "location": genomic_dup1_seq_loc,
-        "relative_copy_class": "EFO:0030072"
+        "relative_copy_class": "high-level gain"
     }
     return VariationDescriptor(**genomic_dup1)
 
 
 @pytest.fixture(scope="module")
 def genomic_dup1_rse(genomic_dup1, genomic_dup1_seq_loc):
     """Create a test fixture for genomic dup RSE."""
@@ -583,17 +581,17 @@
 
 
 @pytest.fixture(scope="module")
 def genomic_dup2_vrc(genomic_dup2, genomic_dup2_seq_loc):
     """Create a test fixture for genomic dup relative CNV."""
     genomic_dup2["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.ClUoNekweei4SUxyjxeLnxagD6vKQ1w7",
+        "id": "ga4gh:RCN.zizBAY460E_wbra9Y6oCxojd8YCbIfnx",
         "location": genomic_dup2_seq_loc,
-        "relative_copy_class": "EFO:0030070"
+        "relative_copy_class": "low-level gain"
     }
     return VariationDescriptor(**genomic_dup2)
 
 
 @pytest.fixture(scope="module")
 def genomic_dup2_rse(genomic_dup2, genomic_dup2_seq_loc):
     """Create a test fixture for genomic dup RSE."""
@@ -727,19 +725,20 @@
     }
     return VariationDescriptor(**genomic_dup3)
 
 
 @pytest.fixture(scope="module")
 def genomic_dup3_vrc(genomic_dup3, genomic_del3_dup3_loc):
     """Create a test fixture for genomic dup relative cnv."""
+    _id = "ga4gh:RCN.4m1TD2538i7v4NQ_OeJ-pIEhlRpYZ3_y"
     genomic_dup3["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.pkRuYZTdIFaA_b9TPc7Czk56VNj1xGz3",
+        "id": _id,
         "location": genomic_del3_dup3_loc,
-        "relative_copy_class": "EFO:0030070"
+        "relative_copy_class": "low-level gain"
     }
     return VariationDescriptor(**genomic_dup3)
 
 
 @pytest.fixture(scope="module")
 def genomic_dup3_rse_lse(genomic_dup3):
     """Create test fixture for genomic dup rse and lse."""
@@ -781,19 +780,20 @@
         "type": "SequenceLocation"
     }
 
 
 @pytest.fixture(scope="module")
 def genomic_dup3_free_text_vrc(genomic_dup3_free_text, genomic_dup3_free_text_subject):
     """Create a test fixture for genomic dup relative cnv."""
+    _id = "ga4gh:RCN.ReWfNwAnchjIPJQEXM038T9M3OsOO7yK"
     genomic_dup3_free_text["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.roF4IsQUR-ZxU_c4KMw9WoDrRnhfA75O",
+        "id": _id,
         "location": genomic_dup3_free_text_subject,
-        "relative_copy_class": "EFO:0030070"
+        "relative_copy_class": "low-level gain"
     }
     return VariationDescriptor(**genomic_dup3_free_text)
 
 
 @pytest.fixture(scope="module")
 def genomic_dup3_free_text_vac(genomic_dup3_free_text, genomic_dup3_free_text_subject):
     """Create a test fixture for genomic dup absolute cnv."""
@@ -835,19 +835,20 @@
     }
     return params
 
 
 @pytest.fixture(scope="module")
 def genomic_dup4_vrc(genomic_dup4, genoimc_dup4_loc):
     """Create a test fixture for genomic dup relative cnv."""
+    _id = "ga4gh:RCN.uSGvLYzpzivqDzhuKR44DHc5imZJSmoV"
     genomic_dup4["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.cFmUKSZQQ-CuOqG468ZyP_zF63WflwoF",
+        "id": _id,
         "location": genoimc_dup4_loc,
-        "relative_copy_class": "EFO:0030070"
+        "relative_copy_class": "low-level gain"
     }
     return VariationDescriptor(**genomic_dup4)
 
 
 @pytest.fixture(scope="module")
 def genomic_dup4_vac(genomic_dup4, genoimc_dup4_loc):
     """Create a test fixture for genomic dup absolute cnv."""
@@ -902,19 +903,20 @@
         "type": "SequenceLocation"
     }
 
 
 @pytest.fixture(scope="module")
 def genomic_dup4_free_text_vrc(genomic_dup4_free_text, genomic_dup4_free_text_subject):
     """Create a test fixture for genomic dup relative cnv."""
+    _id = "ga4gh:RCN.Cf9r8JDpUC18VkkEv44jf8b8WMqUIRFu"
     genomic_dup4_free_text["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.LB5BaDj-GkVlpVAIG9kJSir1uO4DoZ6X",
+        "id": _id,
         "location": genomic_dup4_free_text_subject,
-        "relative_copy_class": "EFO:0030070"
+        "relative_copy_class": "low-level gain"
     }
     return VariationDescriptor(**genomic_dup4_free_text)
 
 
 @pytest.fixture(scope="module")
 def genomic_dup4_free_text_vac(genomic_dup4_free_text, genomic_dup4_free_text_subject):
     """Create a test fixture for genomic dup absolute cnv."""
@@ -966,19 +968,20 @@
         "location": genomic_dup5_loc,
         "copies": {"type": "Number", "value": 3}
     }
 
 
 def genomic_dup5_rel_cnv(params, genomic_dup5_loc):
     """Create genomic dup4 relative cnv"""
+    _id = "ga4gh:RCN.tr_brFSOfykm3I3ufLQTS9pV8KKjqLhK"
     params["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.1sn-uR3OiG0SbGd-f2IkujiqjcUHzxo3",
+        "id": _id,
         "location": genomic_dup5_loc,
-        "relative_copy_class": "EFO:0030070"
+        "relative_copy_class": "low-level gain"
     }
 
 
 @pytest.fixture(scope="module")
 def genomic_dup5_vrc(genomic_dup5, genomic_dup5_loc):
     """Create a test fixture for genomic dup5 relative cnv."""
     genomic_dup5_rel_cnv(genomic_dup5, genomic_dup5_loc)
@@ -1063,19 +1066,20 @@
         "vrs_ref_allele_seq": None
     }
     return params
 
 
 def genomic_dup6_rel_cnv(params, genoimc_dup6_loc):
     """Create genomic dup6 relative cnv"""
+    _id = "ga4gh:RCN.c5Uq3TFDNpQSyDlbXb0BRonw9AYHHk0H"
     params["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.Mb9dPwnAm_KSrifZ0955Lse7Ubr5PaGG",
+        "id": _id,
         "location": genoimc_dup6_loc,
-        "relative_copy_class": "EFO:0030070"
+        "relative_copy_class": "low-level gain"
     }
 
 
 def genomic_dup6_abs_cnv(params, genoimc_dup6_loc):
     """Create genomic dup6 absolute cnv"""
     _id = "ga4gh:ACN.6q8D5d_ie9MO0HdNEJmRJmGMg8C5LdAM"
     params["variation"] = {
@@ -1197,17 +1201,17 @@
 
 
 @pytest.fixture(scope="module")
 def genomic_del1_vrc(genomic_del1, genomic_del1_seq_loc):
     """Create a test fixture for genomic del relative CNV."""
     genomic_del1["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.89rlJ6oV422qg04Rhb25rhZJF46LUPqR",
+        "id": "ga4gh:RCN.z7MU8QUSR_aeWG7MP161H4jwPGoyo1No",
         "location": genomic_del1_seq_loc,
-        "relative_copy_class": "EFO:0030067"
+        "relative_copy_class": "copy neutral"
     }
     return VariationDescriptor(**genomic_del1)
 
 
 @pytest.fixture(scope="module")
 def genomic_del1_rse(genomic_del1, genomic_del1_seq_loc):
     """Create a test fixture for genomic del RSE."""
@@ -1353,17 +1357,17 @@
 
 
 @pytest.fixture(scope="module")
 def genomic_del2_vrc(genomic_del2, genomic_del2_seq_loc):
     """Create a test fixture for genomic del relative CNV."""
     genomic_del2["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.Ai0Z31nuQtHGJ-0Vl8ARrblr0xiKW9d-",
+        "id": "ga4gh:RCN._19twDngCtP3U-8ED2Kly2HM53I_7CV7",
         "location": genomic_del2_seq_loc,
-        "relative_copy_class": "EFO:0030069"
+        "relative_copy_class": "complete loss"
     }
     return VariationDescriptor(**genomic_del2)
 
 
 @pytest.fixture(scope="module")
 def genomic_del2_rse(genomic_del2, genomic_del2_seq_loc):
     """Create a test fixture for genomic del RSE."""
@@ -1484,19 +1488,20 @@
     }
     return params
 
 
 @pytest.fixture(scope="module")
 def genomic_del3_vrc(genomic_del3, genomic_del3_dup3_loc):
     """Create a test fixture for genomic del relative cnv."""
+    _id = "ga4gh:RCN.dYerC8FSiqcexo8X1n3XUKpAckoAsfOK"
     genomic_del3["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.OPd0F6EMNNugGkKFBbl4f1We0WwtL9uI",
+        "id": _id,
         "location": genomic_del3_dup3_loc,
-        "relative_copy_class": "EFO:0030067"
+        "relative_copy_class": "partial loss"
     }
     return VariationDescriptor(**genomic_del3)
 
 
 @pytest.fixture(scope="module")
 def genomic_del3_vac(genomic_del3, genomic_del3_dup3_loc):
     """Create a test fixture for genomic del absolute cnv."""
@@ -1669,19 +1674,20 @@
         "type": "SequenceLocation"
     }
 
 
 @pytest.fixture(scope="module")
 def genomic_del3_free_text_vrc(genomic_del3_free_text, genomic_del3_free_text_subject):
     """Create a test fixture for genomic del relative cnv."""
+    _id = "ga4gh:RCN.6c0tRlHyFYGSeDEmSyn0nrZJLQDkwVsG"
     genomic_del3_free_text["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.jHNFu709utJ1TkGwQkY1NxmYfRqzof5N",
+        "id": _id,
         "location": genomic_del3_free_text_subject,
-        "relative_copy_class": "EFO:0030067"
+        "relative_copy_class": "partial loss"
     }
     return VariationDescriptor(**genomic_del3_free_text)
 
 
 @pytest.fixture(scope="module")
 def genomic_del3_free_text_vac(genomic_del3_free_text, genomic_del3_free_text_subject):
     """Create a test fixture for genomic del absolute cnv."""
@@ -1723,19 +1729,20 @@
     }
     return params
 
 
 @pytest.fixture(scope="module")
 def genomic_del4_vrc(genomic_del4, genomic_del4_seq_loc):
     """Create a test fixture for genomic del relative cnv."""
+    _id = "ga4gh:RCN.BwZOFAfo5u8TcwbR3DMi8qbIImv96VQU"
     genomic_del4["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.euSDpT11wTt9o9lzlk16lc340OBX2_ij",
+        "id": _id,
         "location": genomic_del4_seq_loc,
-        "relative_copy_class": "EFO:0030067"
+        "relative_copy_class": "partial loss"
     }
     return VariationDescriptor(**genomic_del4)
 
 
 @pytest.fixture(scope="module")
 def genomic_del4_vac(genomic_del4, genomic_del4_seq_loc):
     """Create a test fixture for genomic del absolute cnv."""
@@ -1893,19 +1900,20 @@
         "type": "SequenceLocation"
     }
 
 
 @pytest.fixture(scope="module")
 def genomic_del4_free_text_vrc(genomic_del4_free_text, genomic_del4_free_text_subject):
     """Create a test fixture for genomic del relative cnv."""
+    _id = "ga4gh:RCN.XqfrZ9k9mwDO0cM9duK7ooOih0iR1H2Q"
     genomic_del4_free_text["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.fcVXdxFIjLmULNFOLewLKq9xPvNeVNDm",
+        "id": _id,
         "location": genomic_del4_free_text_subject,
-        "relative_copy_class": "EFO:0030067"
+        "relative_copy_class": "partial loss"
     }
     return VariationDescriptor(**genomic_del4_free_text)
 
 
 @pytest.fixture(scope="module")
 def genomic_del4_free_text_vac(genomic_del4_free_text, genomic_del4_free_text_subject):
     """Create a test fixture for genomic del absolute cnv."""
@@ -1937,15 +1945,15 @@
 @pytest.fixture(scope="module")
 def genomic_uncertain_del_2():
     """Create a genomic uncertain deletion on chr 2 test fixture."""
     params = {
         "id": "normalize.variation:NC_000002.12%3Ag.%28%3F_110104900%29_%28110207160_%3F%29del",  # noqa: E501
         "type": "VariationDescriptor",
         "variation": {
-            "id": "ga4gh:RCN.0saHzDrnktHex2tkYyPxQanKwjLUZQu6",
+            "id": "ga4gh:RCN.7EM-Wsg_7mmAE1LW8cmRI3QwKhJCA24a",
             "location": {
                 "id": "ga4gh:SL.gUeB872FGVaphqoSAfI0gz4KXJvpZKL_",
                 "sequence_id": "ga4gh:SQ.pnAqCRBrTsUoBghSD1yp_jXWSmlbdh4g",
                 "start": {
                     "value": 110104899,
                     "comparator": "<=",
                     "type": "IndefiniteRange"
@@ -1953,15 +1961,15 @@
                 "end": {
                     "value": 110207160,
                     "comparator": ">=",
                     "type": "IndefiniteRange"
                 },
                 "type": "SequenceLocation"
             },
-            "relative_copy_class": "EFO:0030067",
+            "relative_copy_class": "partial loss",
             "type": "RelativeCopyNumber"
         },
         "molecule_context": "genomic",
         "structural_type": "SO:0001743"
     }
     return VariationDescriptor(**params)
 
@@ -1969,15 +1977,15 @@
 @pytest.fixture(scope="module")
 def genomic_uncertain_del_y():
     """Create a genomic uncertain deletion on chr Y test fixture."""
     params = {
         "id": "normalize.variation:NC_000024.10%3Ag.%28%3F_14076802%29_%2857165209_%3F%29del",  # noqa: E501
         "type": "VariationDescriptor",
         "variation": {
-            "id": "ga4gh:RCN.7Nl4T845v9vuVS4PUB8HI4-tLPsEWU6e",
+            "id": "ga4gh:RCN.2q7DKevv8nUh87Sl00Z7l50h047Ti2at",
             "location": {
                 "id": "ga4gh:SL.ykRzA8IFueiCG7oznnN4teL2nXXBshHV",
                 "sequence_id": "ga4gh:SQ.8_liLu1aycC0tPQPFmUaGXJLDs5SbPZ5",
                 "start": {
                     "value": 14076801,
                     "comparator": "<=",
                     "type": "IndefiniteRange"
@@ -1985,15 +1993,15 @@
                 "end": {
                     "value": 57165209,
                     "comparator": ">=",
                     "type": "IndefiniteRange"
                 },
                 "type": "SequenceLocation"
             },
-            "relative_copy_class": "EFO:0030067",
+            "relative_copy_class": "partial loss",
             "type": "RelativeCopyNumber"
         },
         "molecule_context": "genomic",
         "structural_type": "SO:0001743"
     }
     return VariationDescriptor(**params)
 
@@ -2021,19 +2029,20 @@
         "location": genomic_del5_seq_loc,
         "copies": {"type": "Number", "value": 3}
     }
 
 
 def genomic_del5_rel_cnv(params, genomic_del5_seq_loc):
     """Create genomic del5 relative cnv"""
+    _id = "ga4gh:RCN.9rG3a5u3JODwQGVrv1IgAjG6SZgdvraH"
     params["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.P0LWls1SeRF881B-uhomC8B4BHc6Fo2R",
+        "id": _id,
         "location": genomic_del5_seq_loc,
-        "relative_copy_class": "EFO:0030067"
+        "relative_copy_class": "partial loss"
     }
 
 
 @pytest.fixture(scope="module")
 def genomic_del5_vrc(genomic_del5, genomic_del5_seq_loc):
     """Create a test fixture for genomic del relative cnv."""
     genomic_del5_rel_cnv(genomic_del5, genomic_del5_seq_loc)
@@ -2234,19 +2243,20 @@
         "vrs_ref_allele_seq": None
     }
     return params
 
 
 def genomic_del6_rel_cnv(params, genomic_del6_seq_loc):
     """Create genomic del6 relative cnv"""
+    _id = "ga4gh:RCN.zsagK87b_RdK4_QZGMnbNl39LCuJUjAr"
     params["variation"] = {
         "type": "RelativeCopyNumber",
-        "id": "ga4gh:RCN.gQwVlnomQRAffyySAQdj3PYxnEalHrXK",
+        "id": _id,
         "location": genomic_del6_seq_loc,
-        "relative_copy_class": "EFO:0030067"
+        "relative_copy_class": "partial loss"
     }
 
 
 def genomic_del6_abs_cnv(params, genomic_del6_seq_loc):
     """Create genomic del6 absolute cnv"""
     _id = "ga4gh:ACN.ZnnJNutwCrHNzFQamAWXMbLC7PfILmqA"
     params["variation"] = {
@@ -2469,15 +2479,15 @@
     resp = await test_handler.normalize(q, "default")
     assertion_checks(resp.variation_descriptor, genomic_dup1_lse, q)
 
     resp = await test_handler.normalize(q, "absolute_cnv", baseline_copies=2)
     assertion_checks(resp.variation_descriptor, genomic_dup1_vac, q)
 
     resp = await test_handler.normalize(q, "relative_cnv",
-                                        relative_copy_class="EFO:0030072")
+                                        relative_copy_class="high-level gain")
     assertion_checks(resp.variation_descriptor, genomic_dup1_vrc, q)
 
     resp = await test_handler.normalize(q, "repeated_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_dup1_rse, q)
 
     resp = await test_handler.normalize(q, "literal_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_dup1_lse, q)
@@ -2489,15 +2499,15 @@
     resp = await test_handler.normalize(q, "default")
     assertion_checks(resp.variation_descriptor, genomic_dup1_lse, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "absolute_cnv", baseline_copies=2)
     assertion_checks(resp.variation_descriptor, genomic_dup1_vac, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "relative_cnv",
-                                        relative_copy_class="EFO:0030072")
+                                        relative_copy_class="high-level gain")
     assertion_checks(resp.variation_descriptor, genomic_dup1_vrc, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "repeated_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_dup1_rse, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "literal_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_dup1_lse, q, ignore_id=True)
@@ -2614,19 +2624,16 @@
     resp = await test_handler.normalize(q, "default")
     assertion_checks(resp.variation_descriptor, genomic_dup3_vrc, q)
 
     resp = await test_handler.normalize(q, "absolute_cnv", baseline_copies=1)
     assertion_checks(resp.variation_descriptor, genomic_dup3_vac, q)
 
     resp = await test_handler.normalize(q, "relative_cnv",
-                                        relative_copy_class="EFO:0030071")
-    test_var = deepcopy(genomic_dup3_vrc)
-    test_var.variation.relative_copy_class = "EFO:0030071"
-    test_var.variation.id = "ga4gh:RCN.lR7qHx5BeS4yJlaopO8JteBq1AO3Kv9m"
-    assertion_checks(resp.variation_descriptor, test_var, q)
+                                        relative_copy_class="low-level gain")
+    assertion_checks(resp.variation_descriptor, genomic_dup3_vrc, q)
 
     resp = await test_handler.normalize(q, "repeated_seq_expr",
                                         untranslatable_returns_text=True)
     assertion_checks(resp.variation_descriptor, genomic_dup3_rse_lse, q)
 
     resp = await test_handler.normalize(q, "literal_seq_expr",
                                         untranslatable_returns_text=True)
@@ -2930,15 +2937,15 @@
     resp = await test_handler.normalize(q, "default")
     assertion_checks(resp.variation_descriptor, genomic_del1_lse, q)
 
     resp = await test_handler.normalize(q, "absolute_cnv", baseline_copies=2)
     assertion_checks(resp.variation_descriptor, genomic_del1_vac, q)
 
     resp = await test_handler.normalize(q, "relative_cnv",
-                                        relative_copy_class="EFO:0030067")
+                                        relative_copy_class="copy neutral")
     assertion_checks(resp.variation_descriptor, genomic_del1_vrc, q)
 
     resp = await test_handler.normalize(q, "repeated_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_del1_rse, q)
 
     resp = await test_handler.normalize(q, "literal_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_del1_lse, q)
@@ -2947,15 +2954,15 @@
     resp = await test_handler.normalize(q, "default")
     assertion_checks(resp.variation_descriptor, genomic_del1_lse, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "absolute_cnv", baseline_copies=2)
     assertion_checks(resp.variation_descriptor, genomic_del1_vac, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "relative_cnv",
-                                        relative_copy_class="EFO:0030067")
+                                        relative_copy_class="copy neutral")
     assertion_checks(resp.variation_descriptor, genomic_del1_vrc, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "repeated_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_del1_rse, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "literal_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_del1_lse, q, ignore_id=True)
@@ -3015,15 +3022,15 @@
     resp = await test_handler.normalize(q, "default")
     assertion_checks(resp.variation_descriptor, genomic_del2_lse, q)
 
     resp = await test_handler.normalize(q, "absolute_cnv", baseline_copies=2)
     assertion_checks(resp.variation_descriptor, genomic_del2_vac, q)
 
     resp = await test_handler.normalize(q, "relative_cnv",
-                                        relative_copy_class="EFO:0030069")
+                                        relative_copy_class="complete loss")
     assertion_checks(resp.variation_descriptor, genomic_del2_vrc, q)
 
     resp = await test_handler.normalize(q, "repeated_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_del2_rse, q)
 
     resp = await test_handler.normalize(q, "literal_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_del2_lse, q)
@@ -3032,15 +3039,15 @@
     resp = await test_handler.normalize(q, "default")
     assertion_checks(resp.variation_descriptor, genomic_del2_lse, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "absolute_cnv", baseline_copies=2)
     assertion_checks(resp.variation_descriptor, genomic_del2_vac, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "relative_cnv",
-                                        relative_copy_class="EFO:0030069")
+                                        relative_copy_class="complete loss")
     assertion_checks(resp.variation_descriptor, genomic_del2_vrc, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "repeated_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_del2_rse, q, ignore_id=True)
 
     resp = await test_handler.normalize(q, "literal_seq_expr")
     assertion_checks(resp.variation_descriptor, genomic_del2_lse, q, ignore_id=True)
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/test_normalize.py` & `variation-normalizer-0.7.dev0/tests/test_normalize.py`

 * *Files 2% similar despite different names*

```diff
@@ -514,44 +514,14 @@
         "vrs_ref_allele_seq": "TTGAGGGAAAACACAT",
         "gene_context": erbb2_context
     }
     return VariationDescriptor(**params)
 
 
 @pytest.fixture(scope="module")
-def genomic_deletion():
-    """Create test fixture for genomic deletion range with deleted sequence.
-    (CA915940709)
-    """
-    params = {
-        "id": "normalize.variation:NC_000003.12%3Ag.10146527_10146528del",
-        "type": "VariationDescriptor",
-        "variation": {
-            "id": "ga4gh:VA.AoFRR6KWkw6_YfrGAxGkT9SJsXieSk93",
-            "location": {
-                "id": "ga4gh:SL.6D7Wbq7XOvga3y-057BKIra4g9RgAFy9",
-                "end": {"value": 10146528, "type": "Number"},
-                "start": {"value": 10146524, "type": "Number"},
-                "sequence_id": "ga4gh:SQ.Zu7h9AggXxhTaGVsy7h_EZSChSZGcmgX",
-                "type": "SequenceLocation"
-            },
-            "state": {
-                "sequence": "CT",
-                "type": "LiteralSequenceExpression"
-            },
-            "type": "Allele"
-        },
-        "molecule_context": "genomic",
-        "structural_type": "SO:0000159",
-        "vrs_ref_allele_seq": "CTCT"
-    }
-    return VariationDescriptor(**params)
-
-
-@pytest.fixture(scope="module")
 def coding_dna_insertion(limk2_gene_context):
     """Create test fixture for coding DNA insertion."""
     params = {
         "id": "normalize.variation:ENST00000331728.9%3Ac.2049_2050insA",
         "type": "VariationDescriptor",
         "variation": {
             "id": "ga4gh:VA.NuvjUrfrwALQWlI0qkWEiv4IngxNZO8f",
@@ -1113,66 +1083,33 @@
     assert resp.variation_descriptor.id == \
         "normalize.variation:ERBB2%20Leu755_Thr759del"
     resp.variation_descriptor.id = \
         "normalize.variation:NP_004439.2%3Ap.Leu755_Thr759del"
     assertion_checks(resp.variation_descriptor, protein_deletion_np_range,
                      "ERBB2 Leu755_Thr759del")
 
-    resp1 = await test_handler.normalize("EGFR L747_T751del")
-    resp2 = await test_handler.normalize("EGFR L747_T751delLREAT")
-    assert resp1.variation_descriptor.variation.id == \
-        resp2.variation_descriptor.variation.id
-
-    # incorrect deleted sequence
-    resp = await test_handler.normalize("EGFR L747_T751delLREA")
-    assert not resp.variation_descriptor
-
 
 @pytest.mark.asyncio
 async def test_coding_dna_deletion(test_handler, coding_dna_deletion):
     """Test that coding dna deletion normalizes correctly."""
     # https://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=CA645372623  # noqa: E501
     q = "NM_004448.3:c.2264_2278delTGAGGGAAAACACAT"
-    resp1 = await test_handler.normalize(q)
-    assertion_checks(resp1.variation_descriptor, coding_dna_deletion, q)
-
-    # incorrected deleted sequence
-    resp = await test_handler.normalize("NM_004448.3:c.2264_2278delTGAGGGAAAACACTA")
-    assert not resp.variation_descriptor
-
-    resp2 = await test_handler.normalize("NM_004448.3:c.2264_2278del")
-    assert resp1.variation_descriptor.variation.id == resp2.variation_descriptor.variation.id  # noqa: E501
+    resp = await test_handler.normalize(q)
+    assertion_checks(resp.variation_descriptor, coding_dna_deletion, q)
 
     q = "ERBB2 c.2264_2278delTGAGGGAAAACACAT"
     resp = await test_handler.normalize(q)
     assert resp.variation_descriptor.id == \
            "normalize.variation:ERBB2%20c.2264_2278delTGAGGGAAAACACAT"
     resp.variation_descriptor.id = \
         "normalize.variation:NM_004448.3%3Ac.2264_2278delTGAGGGAAAACACAT"
     assertion_checks(resp.variation_descriptor, coding_dna_deletion, q)
 
 
 @pytest.mark.asyncio
-async def test_genomic_deletion(test_handler, genomic_deletion):
-    """Test that genomic deletion normalizes correctly"""
-    # CA915940709
-    q = "NC_000003.12:g.10146527_10146528del"
-    resp1 = await test_handler.normalize(q)
-    assertion_checks(resp1.variation_descriptor, genomic_deletion, q)
-
-    resp2 = await test_handler.normalize("NC_000003.12:g.10146527_10146528delCT")
-    assert resp1.variation_descriptor.variation.id == \
-        resp2.variation_descriptor.variation.id
-
-    # incorrect deleted sequence
-    resp = await test_handler.normalize("NC_000003.12:g.10146527_10146528delCC")
-    assert not resp.variation_descriptor
-
-
-@pytest.mark.asyncio
 async def test_protein_insertion(test_handler, protein_insertion):
     """Test that protein insertion normalizes correctly."""
     resp = await test_handler.normalize("NP_005219.2:p.Asp770_Asn771insGlyLeu")
     assertion_checks(resp.variation_descriptor, protein_insertion,
                      "NP_005219.2:p.Asp770_Asn771insGlyLeu")
 
     def change_resp(response):
@@ -1273,29 +1210,14 @@
 
     resp = await test_handler.normalize("NC_000002.12:g.73448098_73448100delCTC")
     assert resp
     assert resp.variation_descriptor.variation.state.sequence == "CTC"
     assert resp.variation_descriptor.variation.id == \
         "ga4gh:VA.M0oqztcpIsGcwxeOfxR32Q9_2Xvpu4BE"
 
-    resp = await test_handler.normalize("NG_008212.3:g.5426_5445del")
-    assert resp.variation_descriptor
-
-    # Test ambiguous IUPAC code N
-    for q in [
-        "NC_000017.10:g.7572948_7572949insTTTTTTTTTNNNNN",
-        "NC_000007.13:g.140453136A>N",
-        "NC_000007.13:g.140453135_140453136delinsATN",
-        "NM_007294.3:c.2902_2903insTCN",
-        "NM_004333.4:c.1799T>N",
-        "NM_001289937.1:c.2326_2327delinsCTN"
-    ]:
-        resp = await test_handler.normalize(q)
-        assert resp.variation_descriptor, q
-
 
 @pytest.mark.asyncio
 async def test_no_matches(test_handler):
     """Test no matches work correctly."""
     queries = [
         "braf", "braf v600000932092039e", "NP_000213.1:cp.Leu862=",
         "NP_000213.1:cp.Leu862", "BRAF V600E 33", "NP_004324.2:p.Glu600Val",
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/test_to_canonical_variation.py` & `variation-normalizer-0.7.dev0/tests/test_to_canonical_variation.py`

 * *Files 1% similar despite different names*

```diff
@@ -24,15 +24,15 @@
     }
 
 
 @pytest.fixture(scope="module")
 def variation1_lse(variation1_seq_loc):
     """Create test fixture for NC_000013.11:20189346:GGG:GG"""
     params = {
-        "id": "ga4gh:CAN.tg0nG9q1DMP_J-vcWiaASPW44GMEh47k",
+        "id": "ga4gh:CLV.tg0nG9q1DMP_J-vcWiaASPW44GMEh47k",
         "type": "CanonicalVariation",
         "canonical_context": {
             "id": "ga4gh:VA.jkAILAe4dK4tQ3y2hz-GHtZRAnbVC__T",
             "type": "Allele",
             "location": variation1_seq_loc,
             "state": {
                 "type": "LiteralSequenceExpression",
@@ -43,15 +43,15 @@
     return CanonicalVariation(**params)
 
 
 @pytest.fixture(scope="module")
 def variation_del_lse():
     """Create test fixture for NC_000013.11:20003096:C:"""
     params = {
-        "id": "ga4gh:CAN.6_wBT_bhV-hwjaqDxq3kEs3nyILkF4du",
+        "id": "ga4gh:CLV.6_wBT_bhV-hwjaqDxq3kEs3nyILkF4du",
         "type": "CanonicalVariation",
         "canonical_context": {
             "id": "ga4gh:VA.l55oQYOlWUoYwAxb4trpbqmMNaknTa1U",
             "type": "Allele",
             "location": {
                 "id": "ga4gh:SL.aEhVhpZMgXXidD4yA4wQbqxKPAf2gnjq",
                 "end": {"value": 20003097, "type": "Number"},
@@ -68,15 +68,15 @@
     return CanonicalVariation(**params)
 
 
 @pytest.fixture(scope="module")
 def variation1_abs_cnv(variation1_seq_loc):
     """Create test fixture for variation1 represented as absolute cnv"""
     params = {
-        "id": "ga4gh:CAN.hQ2OOqFOxd_bdXJbZx4-AwJgvQcPZeLq",
+        "id": "ga4gh:CLV.hQ2OOqFOxd_bdXJbZx4-AwJgvQcPZeLq",
         "type": "CanonicalVariation",
         "canonical_context": {
             "id": "ga4gh:ACN.p_KPDMw49gN0frUAlt_FRBN7Ls4vToZu",
             "type": "AbsoluteCopyNumber",
             "location": variation1_seq_loc,
             "copies": {"type": "Number", "value": 2}
         }
@@ -84,31 +84,31 @@
     return CanonicalVariation(**params)
 
 
 @pytest.fixture(scope="module")
 def variation1_rel_cnv(variation1_seq_loc):
     """Create test fixture for variation1 represented as relative cnv"""
     params = {
-        "id": "ga4gh:CAN.YIYLpl8tuoDp9ckZ-1f1QQJ5q0-i3q-J",
+        "id": "ga4gh:CLV.Ue8qumkG57LEqjS2_xXeW9PVDuKDKdd0",
         "type": "CanonicalVariation",
         "canonical_context": {
-            "id": "ga4gh:RCN.0DNPg6rTfM6GLGrUSF_pLl3VM_3sQl2z",
+            "id": "ga4gh:RCN.FEoHs6XOuAI0Lx5mJfKN4LF4iLpmeJZu",
             "type": "RelativeCopyNumber",
             "location": variation1_seq_loc,
-            "relative_copy_class": "EFO:0030069"
+            "relative_copy_class": "complete loss"
         }
     }
     return CanonicalVariation(**params)
 
 
 @pytest.fixture(scope="module")
 def variation1_rse(variation1_seq_loc):
     """Create test fixture for variation1 represented as RSE"""
     params = {
-        "id": "ga4gh:CAN.oizMWSwBdIddFvs_vA8YqxR7YWupBMrF",
+        "id": "ga4gh:CLV.oizMWSwBdIddFvs_vA8YqxR7YWupBMrF",
         "type": "CanonicalVariation",
         "canonical_context": {
             "id": "ga4gh:VA.91WFk_XWzbzUEI-SfYZip8r1g7I5wqBo",
             "type": "Allele",
             "location": variation1_seq_loc,
             "state": {
                 "type": "RepeatedSequenceExpression",
@@ -127,37 +127,37 @@
     return CanonicalVariation(**params)
 
 
 @pytest.fixture(scope="module")
 def variation2(braf_v600e_genomic_sub):
     """Create test fixture for NC_000007.14:140753335:A:T"""
     params = {
-        "id": "ga4gh:CAN.dP6z4p7SoGJFmlFQcjOQo2d1mXuo1QiY",
+        "id": "ga4gh:CLV.dP6z4p7SoGJFmlFQcjOQo2d1mXuo1QiY",
         "type": "CanonicalVariation",
         "canonical_context": braf_v600e_genomic_sub
     }
     return CanonicalVariation(**params)
 
 
 @pytest.fixture(scope="module")
 def variation3_lse(grch38_genomic_insertion_variation):
     """Create test fixture for NC_000017.10:g.37880993_37880994insGCTTACGTGATG"""
     params = {
-        "id": "ga4gh:CAN.8Pi46FGQsmKIb-6Q0NYKQh0baDBOMvFF",
+        "id": "ga4gh:CLV.8Pi46FGQsmKIb-6Q0NYKQh0baDBOMvFF",
         "type": "CanonicalVariation",
         "canonical_context": grch38_genomic_insertion_variation
     }
     return CanonicalVariation(**params)
 
 
 @pytest.fixture(scope="module")
 def variation3_abs_cnv(grch38_genomic_insertion_seq_loc):
     """Create test fixture for variation3 represented as absolute cnv"""
     params = {
-        "id": "ga4gh:CAN.DzOrKfPgfowNyivzu3WP48H8iPFiLdd1",
+        "id": "ga4gh:CLV.DzOrKfPgfowNyivzu3WP48H8iPFiLdd1",
         "type": "CanonicalVariation",
         "canonical_context": {
             "id": "ga4gh:ACN.e_Nd4RGisOcOmrWVklM-3gGZIo6jSnml",
             "type": "AbsoluteCopyNumber",
             "location": grch38_genomic_insertion_seq_loc,
             "copies": {"type": "Number", "value": 2}
         }
@@ -165,31 +165,31 @@
     return CanonicalVariation(**params)
 
 
 @pytest.fixture(scope="module")
 def variation3_rel_cnv(grch38_genomic_insertion_seq_loc):
     """Create test fixture for variation3 represented as relative cnv"""
     params = {
-        "id": "ga4gh:CAN.wdQ6AQqEUxX9cV7rImNqOMq6r_freYfZ",
+        "id": "ga4gh:CLV.3VhMDipw7_25RSuPvtz-DCYhzjQCoED7",
         "type": "CanonicalVariation",
         "canonical_context": {
-            "id": "ga4gh:RCN.A9ykWRgv47k6MJx8aNQLfn0-LyTlPliO",
+            "id": "ga4gh:RCN.XOeH_PqiR6pkFMmHewn9SjxZEOOZoXVp",
             "type": "RelativeCopyNumber",
             "location": grch38_genomic_insertion_seq_loc,
-            "relative_copy_class": "EFO:0030072"
+            "relative_copy_class": "high-level gain"
         }
     }
     return CanonicalVariation(**params)
 
 
 @pytest.fixture(scope="module")
 def variation3_rse(grch38_genomic_insertion_seq_loc):
     """Create test fixture for variation3 represented as RSE"""
     params = {
-        "id": "ga4gh:CAN.Ohalqu5SLmNmwjaE00v26KskGfggXwjq",
+        "id": "ga4gh:CLV.Ohalqu5SLmNmwjaE00v26KskGfggXwjq",
         "type": "CanonicalVariation",
         "canonical_context": {
             "id": "ga4gh:VA.j6BnT9kvqTO_BQCjTsOzhcnjiwNlhMHv",
             "type": "Allele",
             "location": grch38_genomic_insertion_seq_loc,
             "state": {
                 "type": "RepeatedSequenceExpression",
@@ -208,15 +208,15 @@
     return CanonicalVariation(**params)
 
 
 @pytest.fixture(scope="module")
 def variation4():
     """Create test fixture for NC_000001.11:g.2229202_2229203insCTC"""
     params = {
-        "id": "ga4gh:CAN.azUwFImJO4pTH6rSRx6UItCoxJcTvxln",
+        "id": "ga4gh:CLV.azUwFImJO4pTH6rSRx6UItCoxJcTvxln",
         "type": "CanonicalVariation",
         "canonical_context": {
             "id": "ga4gh:VA.M9Ekcss52lqr1IoX3wZeLTxVsrPW1MSq",
             "type": "Allele",
             "location": {
                 "id": "ga4gh:SL.UdTlDoFUhChBvTu2PXFg_QHA8QsxAy0m",
                 "type": "SequenceLocation",
@@ -284,15 +284,15 @@
         q, fmt="hgvs", do_liftover=True, hgvs_dup_del_mode="absolute_cnv",
         baseline_copies=3)
     assert resp.canonical_variation == variation1_abs_cnv
     assert resp.warnings == []
 
     resp = await test_handler.to_canonical_variation(
         q, fmt="hgvs", do_liftover=True, hgvs_dup_del_mode="relative_cnv",
-        relative_copy_class="EFO:0030069")
+        relative_copy_class="complete loss")
     assert resp.canonical_variation == variation1_rel_cnv
     assert resp.warnings == []
 
     resp = await test_handler.to_canonical_variation(
         q, fmt="hgvs", do_liftover=True, hgvs_dup_del_mode="repeated_seq_expr")
     assert resp.canonical_variation == variation1_rse
     assert resp.warnings == []
@@ -380,15 +380,15 @@
         q, fmt="hgvs", do_liftover=True, hgvs_dup_del_mode="absolute_cnv",
         baseline_copies=1)
     assert resp.canonical_variation == variation3_abs_cnv
     assert resp.warnings == []
 
     resp = await test_handler.to_canonical_variation(
         q, fmt="hgvs", do_liftover=True, hgvs_dup_del_mode="relative_cnv",
-        relative_copy_class="EFO:0030072")
+        relative_copy_class="high-level gain")
     assert resp.canonical_variation == variation3_rel_cnv
     assert resp.warnings == []
 
     resp = await test_handler.to_canonical_variation(
         q, fmt="hgvs", do_liftover=True, hgvs_dup_del_mode="repeated_seq_expr")
     assert resp.canonical_variation == variation3_rse
     assert resp.warnings == []
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_amplification.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_amplification.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_coding_dna_deletion.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_coding_dna_insertion.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,21 +1,22 @@
-"""A module for testing Coding DNA Deletion Tokenization."""
+"""A module for testing Coding DNA Insertion Tokenization."""
 import unittest
 
-from variation.tokenizers import CodingDNADeletion
+from variation.tokenizers.caches import AminoAcidCache, NucleotideCache
+from variation.tokenizers import CodingDNAInsertion
 from .tokenizer_base import TokenizerBase
 
 
-class TestCodingDNADeletionTokenizer(TokenizerBase, unittest.TestCase):
-    """A class for testing Coding DNA Deletion Tokenization."""
+class TestCodingDNAInsertionTokenizer(TokenizerBase, unittest.TestCase):
+    """A class for testing Coding DNA Insertion Tokenization."""
 
     def tokenizer_instance(self):
-        """Return Coding DNA Deletion instance."""
-        return CodingDNADeletion()
+        """Return Coding DNA Insertion instance."""
+        return CodingDNAInsertion(AminoAcidCache(), NucleotideCache())
 
     def token_type(self):
-        """Return Coding DNA deletion token type."""
-        return "CodingDNADeletion"
+        """Return Coding DNA insertion token type."""
+        return "CodingDNAInsertion"
 
     def fixture_name(self):
-        """Return the fixture name for Coding DNA Deletion."""
-        return "coding_dna_deletion"
+        """Return the fixture name for Coding DNA Insertion."""
+        return "coding_dna_insertion"
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_coding_dna_delins.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_coding_dna_delins.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 """A module for testing Coding DNA DelIns tokenization."""
 import unittest
 
-from variation.tokenizers.caches import NucleotideCache
+from variation.tokenizers.caches import AminoAcidCache, NucleotideCache
 from variation.tokenizers import CodingDNADelIns
 from .tokenizer_base import TokenizerBase
 
 
 class TestCodingDNADelInsTokenizer(TokenizerBase, unittest.TestCase):
     """A class for testing Coding DNA DelIns Tokenization."""
 
     def tokenizer_instance(self):
         """Return Coding DNA DelIns instance."""
-        return CodingDNADelIns(NucleotideCache())
+        return CodingDNADelIns(AminoAcidCache(), NucleotideCache())
 
     def token_type(self):
         """Return DNA coding delins token type."""
         return "CodingDNADelIns"
 
     def fixture_name(self):
         """Return the fixture name for DNA coding delins."""
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_coding_dna_insertion.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_coding_dna_deletion.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,22 +1,22 @@
-"""A module for testing Coding DNA Insertion Tokenization."""
+"""A module for testing Coding DNA Deletion Tokenization."""
 import unittest
 
-from variation.tokenizers.caches import NucleotideCache
-from variation.tokenizers import CodingDNAInsertion
+from variation.tokenizers.caches import AminoAcidCache, NucleotideCache
+from variation.tokenizers import CodingDNADeletion
 from .tokenizer_base import TokenizerBase
 
 
-class TestCodingDNAInsertionTokenizer(TokenizerBase, unittest.TestCase):
-    """A class for testing Coding DNA Insertion Tokenization."""
+class TestCodingDNADeletionTokenizer(TokenizerBase, unittest.TestCase):
+    """A class for testing Coding DNA Deletion Tokenization."""
 
     def tokenizer_instance(self):
-        """Return Coding DNA Insertion instance."""
-        return CodingDNAInsertion(NucleotideCache())
+        """Return Coding DNA Deletion instance."""
+        return CodingDNADeletion(AminoAcidCache(), NucleotideCache())
 
     def token_type(self):
-        """Return Coding DNA insertion token type."""
-        return "CodingDNAInsertion"
+        """Return Coding DNA deletion token type."""
+        return "CodingDNADeletion"
 
     def fixture_name(self):
-        """Return the fixture name for Coding DNA Insertion."""
-        return "coding_dna_insertion"
+        """Return the fixture name for Coding DNA Deletion."""
+        return "coding_dna_deletion"
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_coding_dna_silent_mutation.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_coding_dna_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_coding_dna_substitution.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_coding_dna_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_gene.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_gene.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_gene_pair.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_gene_pair.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_deletion.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_deletion.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,20 +1,21 @@
 """A module for testing Genomic Deletion Tokenization."""
 import unittest
 
+from variation.tokenizers.caches import AminoAcidCache, NucleotideCache
 from variation.tokenizers import GenomicDeletion
 from .tokenizer_base import TokenizerBase
 
 
 class TestGenomicDeletionTokenizer(TokenizerBase, unittest.TestCase):
     """A class for testing Coding DNA Deletion Tokenization."""
 
     def tokenizer_instance(self):
         """Return Genomic Deletion instance."""
-        return GenomicDeletion()
+        return GenomicDeletion(AminoAcidCache(), NucleotideCache())
 
     def token_type(self):
         """Return genomic deletion token type."""
         return "GenomicDeletion"
 
     def fixture_name(self):
         """Return the fixture name for Genomic Deletion."""
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_deletion_range.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_deletion_range.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_delins.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_delins.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 """A module for testing Genomic DelIns tokenization."""
 import unittest
 
-from variation.tokenizers.caches import NucleotideCache
+from variation.tokenizers.caches import AminoAcidCache, NucleotideCache
 from variation.tokenizers import GenomicDelIns
 from .tokenizer_base import TokenizerBase
 
 
 class TestGenomicDelInsTokenizer(TokenizerBase, unittest.TestCase):
     """A class for testing Genomic DelIns Tokenization."""
 
     def tokenizer_instance(self):
         """Return Genomic DelIns instance."""
-        return GenomicDelIns(NucleotideCache())
+        return GenomicDelIns(AminoAcidCache(), NucleotideCache())
 
     def token_type(self):
         """Return genomic delins token type."""
         return "GenomicDelIns"
 
     def fixture_name(self):
         """Return the fixture name for genomic delins."""
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_duplication.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_duplication.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_duplication_range.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_duplication_range.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_insertion.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_insertion.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 """A module for testing Genomic Insertion Tokenization."""
 import unittest
 
-from variation.tokenizers.caches import NucleotideCache
+from variation.tokenizers.caches import AminoAcidCache, NucleotideCache
 from variation.tokenizers import GenomicInsertion
 from .tokenizer_base import TokenizerBase
 
 
 class TestGenomicInsertionTokenizer(TokenizerBase, unittest.TestCase):
     """A class for testing Genomic Insertion Tokenization."""
 
     def tokenizer_instance(self):
         """Return Genomic Insertion instance."""
-        return GenomicInsertion(NucleotideCache())
+        return GenomicInsertion(AminoAcidCache(), NucleotideCache())
 
     def token_type(self):
         """Return genomic insertion token type."""
         return "GenomicInsertion"
 
     def fixture_name(self):
         """Return the fixture name for Genomic Insertion."""
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_silent_mutation.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_substitution.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_genomic_uncertain_deletion.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_genomic_uncertain_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_gnomad_vcf.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_gnomad_vcf.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_hgvs.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_hgvs.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_locus_reference_genomic.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_locus_reference_genomic.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_polypeptide_truncation.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_polypeptide_truncation.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,20 +1,21 @@
 """A module for testing Polypeptide Truncation tokenization."""
 import unittest
 
+from variation.tokenizers.caches import AminoAcidCache
 from variation.tokenizers import PolypeptideTruncation
 from .tokenizer_base import TokenizerBase
 
 
 class TestPolypeptideTruncationTokenizer(TokenizerBase, unittest.TestCase):
     """A class for testing Polypeptide Truncation  Tokenization."""
 
     def tokenizer_instance(self):
         """Return Polypeptide Truncation instance."""
-        return PolypeptideTruncation()
+        return PolypeptideTruncation(AminoAcidCache())
 
     def token_type(self):
         """Return Polypeptide Truncation token type."""
         return "PolypeptideTruncation"
 
     def fixture_name(self):
         """Return the fixture name for Polypeptide Truncation."""
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_protein_deletion.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_protein_deletion.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,20 +1,21 @@
 """A module for testing Protein Deletion Tokenization."""
 import unittest
 
+from variation.tokenizers.caches import AminoAcidCache, NucleotideCache
 from variation.tokenizers import ProteinDeletion
 from .tokenizer_base import TokenizerBase
 
 
 class TestProteinDeletionTokenizer(TokenizerBase, unittest.TestCase):
     """A class for testing Protein Deletion Tokenization."""
 
     def tokenizer_instance(self):
         """Return Protein Deletion instance."""
-        return ProteinDeletion()
+        return ProteinDeletion(AminoAcidCache(), NucleotideCache())
 
     def token_type(self):
         """Return protein deletion token type."""
         return "ProteinDeletion"
 
     def fixture_name(self):
         """Return the fixture name for protein deletion."""
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_protein_delins.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_protein_delins.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 """A module for testing Protein DelIns tokenization."""
 import unittest
 
-from variation.tokenizers.caches import NucleotideCache
+from variation.tokenizers.caches import AminoAcidCache, NucleotideCache
 from variation.tokenizers import ProteinDelIns
 from .tokenizer_base import TokenizerBase
 
 
 class TestProteinDelInsTokenizer(TokenizerBase, unittest.TestCase):
     """A class for testing Protein DelIns Tokenization."""
 
     def tokenizer_instance(self):
         """Return Protein DelIns instance."""
-        return ProteinDelIns(NucleotideCache())
+        return ProteinDelIns(AminoAcidCache(), NucleotideCache())
 
     def token_type(self):
         """Return protein delins token type."""
         return "ProteinDelIns"
 
     def fixture_name(self):
         """Return the fixture name for protein delins."""
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_protein_insertion.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_protein_insertion.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 """A module for testing Protein Insertion Tokenization."""
 import unittest
 
 from variation.tokenizers import ProteinInsertion
-from variation.tokenizers.caches import NucleotideCache
+from variation.tokenizers.caches import AminoAcidCache, NucleotideCache
 from .tokenizer_base import TokenizerBase
 
 
 class TestProteinInsertionTokenizer(TokenizerBase, unittest.TestCase):
     """A class for testing Protein Insertion Tokenization."""
 
     def tokenizer_instance(self):
         """Return Protein Insertion instance."""
-        return ProteinInsertion(NucleotideCache())
+        return ProteinInsertion(AminoAcidCache(), NucleotideCache())
 
     def token_type(self):
         """Return protein insertion token type."""
         return "ProteinInsertion"
 
     def fixture_name(self):
         """Return the fixture name for protein insertion."""
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_protein_substitution.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/test_protein_substitution.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,20 +1,21 @@
 """A module for testing Protein Substitution tokenization."""
 import unittest
 
+from variation.tokenizers.caches import AminoAcidCache
 from variation.tokenizers import ProteinSubstitution
 from .tokenizer_base import TokenizerBase
 
 
 class TestProteinSubstitutionTokenizer(TokenizerBase, unittest.TestCase):
     """A class for testing Protein Substitution Tokenization."""
 
     def tokenizer_instance(self):
         """Return protein substitution instance."""
-        return ProteinSubstitution()
+        return ProteinSubstitution(AminoAcidCache())
 
     def token_type(self):
         """Return protein substitution token type."""
         return "ProteinSubstitution"
 
     def fixture_name(self):
         """Return the fixture name for protein substitution."""
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/test_silent_mutation.py` & `variation-normalizer-0.7.dev0/tests/validators/test_silent_mutation.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,21 +1,22 @@
-"""A module for testing Silent Mutation tokenization."""
+"""Module for testing Silent Mutation Validator."""
 import unittest
 
-from variation.tokenizers import SilentMutation
-from .tokenizer_base import TokenizerBase
+from variation.validators import SilentMutation
+from variation.classifiers import SilentMutationClassifier
+from .validator_base import ValidatorBase
 
 
-class TestSilentMutationTokenizer(TokenizerBase, unittest.TestCase):
-    """A class for testing Silent Mutation Tokenization."""
+class TestSilentMutationValidator(ValidatorBase, unittest.TestCase):
+    """A class to test the Silent Mutation Validator."""
 
-    def tokenizer_instance(self):
+    def validator_instance(self):
         """Return Silent Mutation instance."""
-        return SilentMutation()
+        return SilentMutation(*self.aa_params)
 
-    def token_type(self):
-        """Return Silent Mutation token type."""
-        return "SilentMutation"
+    def classifier_instance(self):
+        """Return the Silent Mutation classifier instance."""
+        return SilentMutationClassifier()
 
     def fixture_name(self):
         """Return the fixture name for Silent Mutation."""
         return "silent_mutation"
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/tokenizers/tokenizer_base.py` & `variation-normalizer-0.7.dev0/tests/tokenizers/tokenizer_base.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_coding_dna_deletion.py` & `variation-normalizer-0.7.dev0/tests/translators/test_coding_dna_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_coding_dna_delins.py` & `variation-normalizer-0.7.dev0/tests/translators/test_coding_dna_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_coding_dna_insertion.py` & `variation-normalizer-0.7.dev0/tests/translators/test_coding_dna_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_coding_dna_silent_mutation.py` & `variation-normalizer-0.7.dev0/tests/translators/test_coding_dna_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_coding_dna_substitution.py` & `variation-normalizer-0.7.dev0/tests/translators/test_coding_dna_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_deletion.py` & `variation-normalizer-0.7.dev0/tests/translators/test_genomic_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_delins.py` & `variation-normalizer-0.7.dev0/tests/translators/test_genomic_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_duplication.py` & `variation-normalizer-0.7.dev0/tests/translators/test_genomic_duplication.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_insertion.py` & `variation-normalizer-0.7.dev0/tests/translators/test_genomic_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_silent_mutation.py` & `variation-normalizer-0.7.dev0/tests/translators/test_genomic_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_substitution.py` & `variation-normalizer-0.7.dev0/tests/translators/test_genomic_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_genomic_uncertain_deletion.py` & `variation-normalizer-0.7.dev0/tests/translators/test_genomic_uncertain_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_polypeptide_truncation.py` & `variation-normalizer-0.7.dev0/tests/translators/test_polypeptide_truncation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_protein_deletion.py` & `variation-normalizer-0.7.dev0/tests/translators/test_protein_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_protein_delins.py` & `variation-normalizer-0.7.dev0/tests/translators/test_protein_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_protein_insertion.py` & `variation-normalizer-0.7.dev0/tests/translators/test_protein_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_protein_substitution.py` & `variation-normalizer-0.7.dev0/tests/translators/test_protein_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/test_silent_mutation.py` & `variation-normalizer-0.7.dev0/tests/translators/test_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/translators/translator_base.py` & `variation-normalizer-0.7.dev0/tests/translators/translator_base.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,47 +1,49 @@
 """A module for testing translator classes."""
 import yaml
-from biocommons.seqrepo import SeqRepo
+from ga4gh.vrs.dataproxy import SeqRepoDataProxy
 from ga4gh.vrs.extras.translator import Translator
 from gene.query import QueryHandler as GeneQueryHandler
-from cool_seq_tool import SEQREPO_ROOT_DIR
-from cool_seq_tool.data_sources import TranscriptMappings, SeqRepoAccess, \
+from uta_tools.data_sources import TranscriptMappings, SeqRepoAccess, \
     MANETranscriptMappings, UTADatabase, MANETranscript
 
 from tests import PROJECT_ROOT
 from variation.schemas.app_schemas import Endpoint
 from variation.vrs_representation import VRSRepresentation
 from variation.tokenizers import Tokenize, GeneSymbol
+from variation.tokenizers.caches import AminoAcidCache
 
 
 class TranslatorBase:
     """The translator base class."""
 
     @classmethod
     def setUpClass(cls):
         """Set up the test cases."""
         with open(f"{PROJECT_ROOT}/tests/fixtures/translators.yml") as stream:
             cls.all_fixtures = yaml.safe_load(stream)
+        amino_acid_cache = AminoAcidCache()
         gene_normalizer = GeneQueryHandler()
         gene_symbol = GeneSymbol(gene_normalizer)
-        cls.tokenizer = Tokenize(gene_symbol)
+        cls.tokenizer = Tokenize(amino_acid_cache, gene_symbol)
 
-        sr = SeqRepo(root_dir=SEQREPO_ROOT_DIR)
-        seqrepo_access = SeqRepoAccess(sr)
+        seqrepo_access = SeqRepoAccess()
         transcript_mappings = TranscriptMappings()
         uta = UTADatabase()
-        tlr = Translator(data_proxy=seqrepo_access)
+        dp = SeqRepoDataProxy(seqrepo_access.seqrepo_client)
+        tlr = Translator(data_proxy=dp)
         mane_transcript = MANETranscript(
             seqrepo_access, transcript_mappings, MANETranscriptMappings(), uta,
             gene_normalizer)
-        vrs = VRSRepresentation(seqrepo_access)
+        vrs = VRSRepresentation(dp, seqrepo_access)
 
         cls.aa_params = [
             seqrepo_access, transcript_mappings, gene_symbol,
-            mane_transcript, uta, tlr, gene_normalizer, vrs
+            mane_transcript, uta, tlr, gene_normalizer,
+            vrs, amino_acid_cache
         ]
         cls.params = cls.aa_params[:-1]
 
     def classifier_instance(self):
         """Check that the classifier_instance method is implemented."""
         raise NotImplementedError()
```

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_coding_dna_deletion.py` & `variation-normalizer-0.7.dev0/tests/validators/test_coding_dna_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_coding_dna_delins.py` & `variation-normalizer-0.7.dev0/tests/validators/test_coding_dna_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_coding_dna_insertion.py` & `variation-normalizer-0.7.dev0/tests/validators/test_coding_dna_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_coding_dna_silent_mutation.py` & `variation-normalizer-0.7.dev0/tests/validators/test_coding_dna_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_coding_dna_subsitution.py` & `variation-normalizer-0.7.dev0/tests/validators/test_coding_dna_subsitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_deletion.py` & `variation-normalizer-0.7.dev0/tests/validators/test_genomic_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_delins.py` & `variation-normalizer-0.7.dev0/tests/validators/test_genomic_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_duplication.py` & `variation-normalizer-0.7.dev0/tests/validators/test_genomic_duplication.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_insertion.py` & `variation-normalizer-0.7.dev0/tests/validators/test_genomic_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_silent_mutation.py` & `variation-normalizer-0.7.dev0/tests/validators/test_genomic_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_substitution.py` & `variation-normalizer-0.7.dev0/tests/validators/test_genomic_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_genomic_uncertain_deletion.py` & `variation-normalizer-0.7.dev0/tests/validators/test_genomic_uncertain_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_polypeptide_truncation.py` & `variation-normalizer-0.7.dev0/tests/validators/test_polypeptide_truncation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_protein_deletion.py` & `variation-normalizer-0.7.dev0/tests/validators/test_protein_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_protein_delins.py` & `variation-normalizer-0.7.dev0/tests/validators/test_protein_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_protein_insertion.py` & `variation-normalizer-0.7.dev0/tests/validators/test_protein_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/test_protein_substitution.py` & `variation-normalizer-0.7.dev0/tests/validators/test_protein_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/tests/validators/validator_base.py` & `variation-normalizer-0.7.dev0/tests/validators/validator_base.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,47 +1,49 @@
 """A module for testing validator classes."""
 import yaml
-from biocommons.seqrepo import SeqRepo
+from ga4gh.vrs.dataproxy import SeqRepoDataProxy
 from ga4gh.vrs.extras.translator import Translator
 from gene.query import QueryHandler as GeneQueryHandler
-from cool_seq_tool import SEQREPO_ROOT_DIR
-from cool_seq_tool.data_sources import TranscriptMappings, SeqRepoAccess, \
+from uta_tools.data_sources import TranscriptMappings, SeqRepoAccess, \
     MANETranscriptMappings, UTADatabase, MANETranscript
 
 from tests import PROJECT_ROOT
 from variation.schemas.app_schemas import Endpoint
 from variation.vrs_representation import VRSRepresentation
 from variation.tokenizers import Tokenize, GeneSymbol
+from variation.tokenizers.caches import AminoAcidCache
 
 
 class ValidatorBase:
     """The validator base class."""
 
     @classmethod
     def setUpClass(cls):
         """Set up the test cases."""
         with open(f"{PROJECT_ROOT}/tests/fixtures/validators.yml") as stream:
             cls.all_fixtures = yaml.safe_load(stream)
+        amino_acid_cache = AminoAcidCache()
         gene_normalizer = GeneQueryHandler()
         gene_symbol = GeneSymbol(gene_normalizer)
-        cls.tokenizer = Tokenize(gene_symbol)
+        cls.tokenizer = Tokenize(amino_acid_cache, gene_symbol)
 
-        sr = SeqRepo(root_dir=SEQREPO_ROOT_DIR)
-        seqrepo_access = SeqRepoAccess(sr)
+        seqrepo_access = SeqRepoAccess()
         transcript_mappings = TranscriptMappings()
         uta = UTADatabase()
-        tlr = Translator(data_proxy=seqrepo_access)
+        dp = SeqRepoDataProxy(seqrepo_access.seqrepo_client)
+        tlr = Translator(data_proxy=dp)
         mane_transcript = MANETranscript(
             seqrepo_access, transcript_mappings, MANETranscriptMappings(), uta,
             gene_normalizer)
-        vrs = VRSRepresentation(seqrepo_access)
+        vrs = VRSRepresentation(dp, seqrepo_access)
 
         cls.aa_params = [
             seqrepo_access, transcript_mappings, gene_symbol,
-            mane_transcript, uta, tlr, gene_normalizer, vrs
+            mane_transcript, uta, tlr, gene_normalizer,
+            vrs, amino_acid_cache
         ]
         cls.params = cls.aa_params[:-1]
 
     def classifier_instance(self):
         """Check that the classifier_instance method is implemented."""
         raise NotImplementedError()
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/__init__.py` & `variation-normalizer-0.7.dev0/variation/classifiers/__init__.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/amplification_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/amplification_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/classify.py` & `variation-normalizer-0.7.dev0/variation/classifiers/classify.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/coding_dna_deletion_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/coding_dna_deletion_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/coding_dna_delins_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/coding_dna_delins_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/coding_dna_insertion_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/coding_dna_insertion_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/coding_dna_silent_mutation_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/coding_dna_silent_mutation_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/coding_dna_substitution_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/coding_dna_substitution_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_deletion_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/genomic_deletion_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_deletion_range_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/genomic_deletion_range_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_delins_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/genomic_delins_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_duplication_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/genomic_duplication_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_insertion_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/genomic_insertion_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_silent_mutation_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/genomic_silent_mutation_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_substitution_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/genomic_substitution_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/genomic_uncertain_deletion_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/genomic_uncertain_deletion_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/polypeptide_truncation_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/polypeptide_truncation_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/protein_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/protein_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/protein_deletion_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/protein_deletion_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/protein_delins_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/protein_delins_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/protein_insertion_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/protein_insertion_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/protein_termination_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/protein_termination_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/set_based_classifier.py` & `variation-normalizer-0.7.dev0/variation/classifiers/set_based_classifier.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/classifiers/silent_mutation.py` & `variation-normalizer-0.7.dev0/variation/classifiers/silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/data_sources/codon_table.py` & `variation-normalizer-0.7.dev0/variation/data_sources/codon_table.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,22 +1,26 @@
 """Module for Codon Table."""
 from typing import Dict, List
 
-from bioutils.sequences import aa3_to_aa1
+from variation.tokenizers.caches import AminoAcidCache
 
 
 MULTIPLE_CODONS = {"Leu", "Ser", "Arg"}
 
 
 class CodonTable:
     """Class for codon table data."""
 
-    def __init__(self) -> None:
-        """Initialize codon table class."""
+    def __init__(self, amino_acid_cache: AminoAcidCache) -> None:
+        """Initialize codon table class.
+
+        :param AminoAcidCache amino_acid_cache: Amino acid code data
+        """
         self.table = self._set_codon_table()
+        self.amino_acid_cache = amino_acid_cache
         self._dna_to_rna = {
             "T": "A", "A": "U",
             "G": "C", "C": "G"
         }
 
     @staticmethod
     def _set_codon_table() -> Dict[str, str]:
@@ -45,18 +49,17 @@
 
     def get_codons(self, amino_acid: str) -> List[str]:
         """Return a list of codons for an amino acid.
 
         :param str amino_acid: Amino acid to get codons for
         :return: List of codons
         """
+        amino_acid = amino_acid.upper()
         if len(amino_acid) == 3:
-            amino_acid = aa3_to_aa1(amino_acid.capitalize())
-        else:
-            amino_acid = amino_acid.upper()
+            amino_acid = self.amino_acid_cache.convert_three_to_one(amino_acid)
 
         codons = list()
         for k, v in self.table.items():
             if v == amino_acid:
                 codons.append(k)
         codons.sort()
         return codons
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/gnomad_vcf_to_protein_variation.py` & `variation-normalizer-0.7.dev0/variation/gnomad_vcf_to_protein_variation.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,16 +1,17 @@
 """Module for going from gnomAD VCF to VRS variation on the protein coordinate"""
 from typing import Optional, Tuple, List, Dict
 from urllib.parse import quote
 from datetime import datetime
 
-from cool_seq_tool.data_sources import SeqRepoAccess, UTADatabase, MANETranscript,\
+from uta_tools.data_sources import SeqRepoAccess, UTADatabase, MANETranscript,\
     MANETranscriptMappings
-from cool_seq_tool.schemas import ResidueMode
+from uta_tools.schemas import ResidueMode
 from gene.query import QueryHandler as GeneQueryHandler
+from ga4gh.vrs.dataproxy import SeqRepoDataProxy
 
 from variation.classifiers.classify import Classify
 from variation.data_sources.codon_table import CodonTable
 from variation.hgvs_dup_del_mode import HGVSDupDelMode
 from variation.to_vrsatile import ToVRSATILE
 from variation.tokenizers.tokenize import Tokenize
 from variation.translators.translate import Translate
@@ -24,39 +25,40 @@
     import HGVSDupDelMode as HGVSDupDelModeEnum, NormalizeService, ServiceMeta
 from variation.version import __version__
 
 
 class GnomadVcfToProteinVariation(ToVRSATILE):
     """Class for translating gnomAD VCF representation to protein representation"""
 
-    def __init__(self, seqrepo_access: SeqRepoAccess,
+    def __init__(self, seqrepo_access: SeqRepoAccess, dp: SeqRepoDataProxy,
                  tokenizer: Tokenize, classifier: Classify, validator: Validate,
                  translator: Translate, hgvs_dup_del_mode: HGVSDupDelMode,
                  gene_normalizer: GeneQueryHandler,
                  uta: UTADatabase, mane_transcript: MANETranscript,
                  mane_transcript_mappings: MANETranscriptMappings,
                  codon_table: CodonTable) -> None:
         """Initialize the GnomadVcfToProteinVariation class
 
-        :param SeqRepoAccess seqrepo_access: Access to SeqRepo
+        :param SeqRepoAccess seqrepo_access: Access to SeqRepo via UTA Tools
+        :param SeqRepoDataProxy dp: Access to SeqRepo via VRS Python
         :param Tokenize tokenizer: Tokenizer class for tokenizing
         :param Classify classifier: Classifier class for classifying tokens
         :param Validate validator: Validator class for validating valid inputs
         :param Translate translator: Translating valid inputs
         :param HGVSDupDelMode hgvs_dup_del_mode: Class for handling
             HGVS dup/del expressions
         :parm GeneQueryHandler gene_normalizer: Client for normalizing gene concepts
         :param UTADatabase uta: Access to db containing alignment data
         :param MANETranscript mane_transcript: Access MANE Transcript
             information
         :param MANETranscriptMappings mane_transcript_mappings: Mappings for
             MANE Transcript data
         :param CodonTable codon_table: Codon table data
         """
-        super().__init__(seqrepo_access, tokenizer, classifier, validator,
+        super().__init__(seqrepo_access, dp, tokenizer, classifier, validator,
                          translator, hgvs_dup_del_mode, gene_normalizer)
         self.uta = uta
         self.mane_transcript = mane_transcript
         self.mane_transcript_mappings = mane_transcript_mappings
         self.codon_table = codon_table
 
     async def _get_gnomad_vcf_validations(
@@ -87,15 +89,15 @@
         """Get genomic ac from variation sequence_id
 
         :param Dict variation: VRS variation object
         :return: RefSeq genomic accession
         """
         # genomic ac should always be in 38
         alt_ac = variation["location"]["sequence_id"]
-        aliases = self.seqrepo_access.sr.translate_identifier(
+        aliases = self.seqrepo_access.seqrepo_client.translate_identifier(
             alt_ac, target_namespaces="refseq")
         return aliases[0].split("refseq:")[-1]
 
     def _update_gnomad_vcf_mane_c_pos(
             self, reading_frame: int, mane_c_ac: str,
             mane_c_pos_change: Tuple[int, int], coding_start_site: int,
             warnings: List) -> Optional[Tuple[int, int]]:
@@ -219,16 +221,15 @@
             for i in range(int(len(alt) / 3)):
                 aa_alt += self.codon_table.table[alt[3 * i:(3 * i) + 3]]
             return aa_alt
 
     async def gnomad_vcf_to_protein(
         self, q: str, untranslatable_returns_text: bool = False
     ) -> NormalizeService:
-        """Get MANE protein consequence for gnomad vcf (chr-pos-ref-alt).
-        Assumes using GRCh38 coordinates
+        """Get protein consequence for gnomad vcf
 
         :param str q: gnomad vcf (chr-pos-ref-alt)
         :param bool untranslatable_returns_text: `True` return VRS Text Object when
             unable to translate or normalize query. `False` return `None` when
             unable to translate or normalize query.
         :return: Normalize Service containing variation descriptor and warnings
         """
@@ -237,34 +238,20 @@
         warnings = list()
         if q:
             _id = f"normalize.variation:{quote(' '.join(q.split()))}"
             warnings = list()
             valid_list = list()
             validations = await self._get_gnomad_vcf_validations(q, warnings)
             if validations:
-                validations.valid_results = sorted(validations.valid_results,
-                                                   key=lambda x: x.is_mane_transcript,
-                                                   reverse=True)
-
-                all_warnings = set()
-                checked_valid_results = list()
+                all_warnings = list()
                 for valid_result in validations.valid_results:
                     warnings = list()
                     # all gnomad vcf will be alleles with a literal seq expression
                     variation = valid_result.variation
                     classification_token = valid_result.classification_token
-
-                    # We do not need to check the same variation that has the same
-                    # classification
-                    checked_tuple = (variation["id"], valid_result.identifier,
-                                     valid_result.classification.classification_type.value)  # noqa: E501
-                    if checked_tuple in checked_valid_results:
-                        continue
-
-                    checked_valid_results.append(checked_tuple)
                     alt_ac = self._get_refseq_alt_ac_from_variation(variation)
 
                     # 0-based
                     g_start_pos = None
                     g_end_pos = None
                     if classification_token.alt_type == "deletion":
                         g_start_pos = classification_token.start_pos_del
@@ -275,46 +262,50 @@
                     elif classification_token.alt_type in ["silent_mutation",
                                                            "substitution"]:
                         g_start_pos = classification_token.position
                         g_end_pos = classification_token.position
                         ref_seq, w = self.seqrepo_access.get_reference_sequence(
                             alt_ac, g_start_pos)
                         if not ref_seq:
-                            all_warnings.add(w)
+                            all_warnings.append(w)
                         else:
                             if ref_seq != classification_token.ref_nucleotide:
-                                all_warnings.add(
+                                all_warnings.append(
                                     f"Expected {classification_token.ref_nucleotide}"
                                     f" but found {ref_seq} on {alt_ac} at position"
                                     f" {g_start_pos}"
                                 )
                                 continue
                     else:
-                        all_warnings.add(
+                        all_warnings.append(
                             f"{classification_token.alt_type} alt_type not supported"
                         )
                         continue
 
-                    chromosome = q.split("-")[:-1][0]
-                    mane_data = self.mane_transcript_mappings.get_mane_data_from_chr_pos(  # noqa: E501
-                        chromosome, g_start_pos, g_end_pos)
-                    mane_data_len = len(mane_data)
                     g_start_pos -= 1
                     g_end_pos -= 1
 
+                    transcripts = await self.uta.get_transcripts_from_genomic_pos(
+                        alt_ac, g_start_pos)
+
+                    if not transcripts:
+                        all_warnings.append(f"Unable to get transcripts given {alt_ac}"
+                                            f" and {g_start_pos + 1}")
+                        continue
+                    mane_data = self.mane_transcript_mappings.get_mane_from_transcripts(transcripts)  # noqa: E501
+                    mane_data_len = len(mane_data)
                     for i in range(mane_data_len):
-                        current_mane_data = mane_data[i]
+                        index = mane_data_len - i - 1
+                        current_mane_data = mane_data[index]
                         mane_c_ac = current_mane_data["RefSeq_nuc"]
                         mane_tx_genomic_data = await self.uta.get_mane_c_genomic_data(
                             mane_c_ac, alt_ac, g_start_pos, g_end_pos)
                         if not mane_tx_genomic_data:
-                            all_warnings.add(
-                                f"Unable to get MANE data for {mane_c_ac} using "
-                                f"{alt_ac} at positions {g_start_pos} to {g_end_pos}")
-                            continue
+                            all_warnings.append("Unable to get mane transcript and "
+                                                "genomic data")
 
                         coding_start_site = mane_tx_genomic_data["coding_start_site"]
                         mane_c_pos_change = \
                             self.mane_transcript.get_mane_c_pos_change(
                                 mane_tx_genomic_data, coding_start_site)
 
                         # We use 1-based
@@ -323,15 +314,15 @@
                         if classification_token.alt_type in ["substitution",
                                                              "silent_mutation"]:
                             mane_c_pos_change = self._update_gnomad_vcf_mane_c_pos(
                                 reading_frame, mane_c_ac, mane_c_pos_change,
                                 coding_start_site, warnings)
                             if mane_c_pos_change is None:
                                 if len(warnings) > 0:
-                                    all_warnings.add(warnings[0])
+                                    all_warnings.append(warnings[0])
                                 continue
 
                         mane_p = self.mane_transcript._get_mane_p(
                             current_mane_data,
                             (mane_c_pos_change[0] + 1, mane_c_pos_change[1] + 1)
                         )
                         if mane_p["pos"][0] > mane_p["pos"][1]:
@@ -353,15 +344,15 @@
                                         q, variation, valid_result, _id, warnings,
                                         gene=current_mane_data["HGNC_ID"]))
 
                 if valid_list:
                     vd, warnings = valid_list[0]
                 else:
                     if all_warnings:
-                        vd, warnings = no_variation_resp(q, _id, list(all_warnings),
+                        vd, warnings = no_variation_resp(q, _id, all_warnings,
                                                          untranslatable_returns_text)
                     else:
                         vd, warnings = no_variation_resp(
                             q, _id, [f"Unable to get protein variation for {q}"],
                             untranslatable_returns_text)
             else:
                 vd, warnings = no_variation_resp(q, _id, warnings,
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/hgvs_dup_del_mode.py` & `variation-normalizer-0.7.dev0/variation/hgvs_dup_del_mode.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 """Module for hgvs_dup_del_mode in normalize endpoint."""
 import logging
 from typing import Optional, Dict, Tuple, List
 
 from ga4gh.vrs import models
 from ga4gh.core import ga4gh_identify
-from cool_seq_tool.data_sources import SeqRepoAccess
-from ga4gh.vrsatile.pydantic.vrs_models import RelativeCopyClass
+from uta_tools.data_sources import SeqRepoAccess
 
+from variation.schemas.hgvs_to_copy_number_schema import RelativeCopyClass
 from variation.schemas.normalize_response_schema\
     import HGVSDupDelMode as HGVSDupDelModeEnum
 
 logger = logging.getLogger("variation")
 logger.setLevel(logging.DEBUG)
 
 
@@ -51,16 +51,15 @@
         self, alt_type: str, pos: Tuple[int, int], del_or_dup: str,
         location: Dict, allele: Dict = None, baseline_copies: Optional[int] = None,
         relative_copy_class: Optional[RelativeCopyClass] = None
     ) -> Optional[Dict]:
         """Use default characteristics to return a variation.
         If baseline_copies not provided and endpoints are ambiguous: relative_cnv
             if relative_copy_class not provided:
-                relative_copy_class = `EFO:0030067` (copy number loss) if del,
-                    `EFO:0030070` (copy number gain) if dup
+                relative_copy_class = `partial loss` if del, `low-level gain` if dup
         elif baseline_copies provided: absolute_cnv
             copies are baseline + 1 for dup, baseline - 1 for del
         elif len del or dup > 100bp (use outermost coordinates):
             repeated_seq_expr with a derived_seq_expr subject (Allele)
         else:
             literal_seq_expr (normalized LiteralSequenceExpression Allele)
 
@@ -118,17 +117,17 @@
         :param str del_or_dup: Must be either `del` or `dup`
         :param Dict location: VRS SequenceLocation
         :param Optional[RelativeCopyClass] relative_copy_class: The relative copy class
         :return: Relative copy number variation as a dict
         """
         if not relative_copy_class:
             if del_or_dup == "del":
-                relative_copy_class = RelativeCopyClass.COPY_NUMBER_LOSS.value
+                relative_copy_class = RelativeCopyClass.PARTIAL_LOSS.value
             else:
-                relative_copy_class = RelativeCopyClass.COPY_NUMBER_GAIN.value
+                relative_copy_class = RelativeCopyClass.LOW_LEVEL_GAIN.value
         variation = {
             "type": "RelativeCopyNumber",
             "location": location,
             "relative_copy_class": relative_copy_class
         }
         variation["id"] = ga4gh_identify(models.RelativeCopyNumber(**variation))
         return variation
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/main.py` & `variation-normalizer-0.7.dev0/variation/main.py`

 * *Files 2% similar despite different names*

```diff
@@ -188,15 +188,15 @@
         separated by commas
     :return: TranslateIdentifierService data
     """
     aliases = []
     warnings = None
     identifier = identifier.strip()
     try:
-        aliases = query_handler._seqrepo_access.sr.translate_identifier(
+        aliases = query_handler._seqrepo_access.seqrepo_client.translate_identifier(
             identifier, target_namespaces=target_namespaces)
     except KeyError:
         warnings = [f"Identifier, {identifier}, does not exist in SeqRepo"]
     except Exception as e:
         warnings = [f"SeqRepo could not translate identifier, {identifier}:"
                     f" {e}"]
 
@@ -260,19 +260,19 @@
         ),
         vrs_python_meta_=VrsPythonMeta(
             version=pkg_resources.get_distribution("ga4gh.vrs").version
         )
     )
 
 
-g_to_p_summary = "Given GRCh38 gnomAD VCF, return VRSATILE object on MANE protein coordinate."  # noqa: E501
+g_to_p_summary = "Given gnomad VCF, return VRSATILE object on protein coordinate."
 g_to_p_response_description = "A response to a validly-formed query."
 g_to_p_description = \
     "Return VRSATILE object on protein coordinate for variation provided."
-q_description = "GRCh38 gnomAD VCF (chr-pos-ref-alt) to normalize to MANE protein variation."  # noqa: E501
+q_description = "gnomad VCF to normalize to protein variation."
 
 
 @app.get("/variation/gnomad_vcf_to_protein",
          summary=g_to_p_summary,
          response_description=g_to_p_response_description,
          description=g_to_p_description,
          response_model=NormalizeService,
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/normalize.py` & `variation-normalizer-0.7.dev0/variation/normalize.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 """Module for Variation Normalization."""
 from typing import Optional
 from urllib.parse import quote
 from datetime import datetime
 
 from gene.query import QueryHandler as GeneQueryHandler
-from cool_seq_tool.data_sources import SeqRepoAccess, UTADatabase
+from uta_tools.data_sources import SeqRepoAccess, UTADatabase
+from ga4gh.vrs.dataproxy import SeqRepoDataProxy
 
 from variation.classifiers.classify import Classify
 from variation.to_vrsatile import ToVRSATILE
 from variation.hgvs_dup_del_mode import HGVSDupDelMode
 from variation.tokenizers.tokenize import Tokenize
 from variation.translators.translate import Translate
 from variation.utils import get_mane_valid_result, no_variation_entered, \
@@ -20,31 +21,32 @@
 from variation.schemas.hgvs_to_copy_number_schema import RelativeCopyClass
 from variation.version import __version__
 
 
 class Normalize(ToVRSATILE):
     """The Normalize class used to normalize a given variation."""
 
-    def __init__(self, seqrepo_access: SeqRepoAccess,
+    def __init__(self, seqrepo_access: SeqRepoAccess, dp: SeqRepoDataProxy,
                  tokenizer: Tokenize, classifier: Classify, validator: Validate,
                  translator: Translate, hgvs_dup_del_mode: HGVSDupDelMode,
                  gene_normalizer: GeneQueryHandler, uta: UTADatabase) -> None:
         """Initialize Normalize class.
 
-        :param SeqRepoAccess seqrepo_access: Access to SeqRepo
+        :param SeqRepoAccess seqrepo_access: Access to SeqRepo via UTA Tools
+        :param SeqRepoDataProxy dp: Access to SeqRepo via VRS Python
         :param Tokenize tokenizer: Tokenizer class for tokenizing
         :param Classify classifier: Classifier class for classifying tokens
         :param Validate validator: Validator class for validating valid inputs
         :param Translate translator: Translating valid inputs
         :param HGVSDupDelMode hgvs_dup_del_mode: Class for handling
             HGVS dup/del expressions
         :parm GeneQueryHandler gene_normalizer: Client for normalizing gene concepts
         :param UTADatabase uta: Access to db containing alignment data
         """
-        super().__init__(seqrepo_access, tokenizer, classifier, validator,
+        super().__init__(seqrepo_access, dp, tokenizer, classifier, validator,
                          translator, hgvs_dup_del_mode, gene_normalizer)
         self.uta = uta
 
     async def normalize(
         self, q: str,
         hgvs_dup_del_mode: Optional[HGVSDupDelModeEnum] = HGVSDupDelModeEnum.DEFAULT,
         baseline_copies: Optional[int] = None,
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/query.py` & `variation-normalizer-0.7.dev0/variation/query.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,18 +1,20 @@
 """This module provides methods for handling queries."""
 from typing import Optional
 from os import environ
 
 from gene.query import QueryHandler as GeneQueryHandler
+from ga4gh.vrs.dataproxy import SeqRepoDataProxy
 from ga4gh.vrs.extras.translator import Translator
-from cool_seq_tool import TRANSCRIPT_MAPPINGS_PATH, LRG_REFSEQGENE_PATH, \
-    MANE_SUMMARY_PATH, CoolSeqTool
+from uta_tools import SEQREPO_DATA_PATH, TRANSCRIPT_MAPPINGS_PATH, \
+    LRG_REFSEQGENE_PATH, MANE_SUMMARY_PATH, UTATools
 
-from variation import UTA_DB_URL
+from variation import AMINO_ACID_PATH, UTA_DB_URL
 from variation.tokenizers import GeneSymbol
+from variation.tokenizers.caches import AminoAcidCache
 from variation.hgvs_dup_del_mode import HGVSDupDelMode
 from variation.to_vrs import VRSRepresentation, ToVRS
 from variation.classifiers import Classify
 from variation.tokenizers import Tokenize
 from variation.validators import Validate
 from variation.translators import Translate
 from variation.data_sources import CodonTable
@@ -25,67 +27,76 @@
 
 class QueryHandler:
     """Class for initializing handlers that make app queries."""
 
     def __init__(self,
                  dynamodb_url: str = "",
                  dynamodb_region: str = "us-east-2",
+                 seqrepo_data_path: str = None,
+                 amino_acids_file_path: str = AMINO_ACID_PATH,
                  transcript_file_path: str = None,
                  refseq_file_path: str = None,
                  mane_data_path: str = None,
                  uta_db_url: str = UTA_DB_URL,
                  uta_db_pwd: Optional[str] = None) -> None:
         """Initialize QueryHandler instance.
         :param str dynamodb_url: URL to gene-normalizer database source.
         :param str dynamodb_region: AWS default region for gene-normalizer.
+        :param str seqrepo_data_path: Path to seqrepo data directory
+        :param str amino_acids_file_path: Path to amino acids file
         :param str transcript_file_path: Path to transcript mappings file
         :param str refseq_file_path: Path to refseq gene symbol file
         :param str mane_data_path: Path to refseq mane data file
         :param str uta_db_url: URL for UTA database
         :param Optional[str] uta_db_pwd: Password for UTA database user
         """
+        if not seqrepo_data_path:
+            seqrepo_data_path = environ.get("SEQREPO_DATA_PATH", SEQREPO_DATA_PATH)
         if not transcript_file_path:
             transcript_file_path = environ.get("TRANSCRIPT_MAPPINGS_PATH",
                                                TRANSCRIPT_MAPPINGS_PATH)
         if not refseq_file_path:
             refseq_file_path = environ.get("LRG_REFSEQGENE_PATH", LRG_REFSEQGENE_PATH)
         if not mane_data_path:
             mane_data_path = environ.get("MANE_SUMMARY_PATH", MANE_SUMMARY_PATH)
-        cool_seq_tool = CoolSeqTool(transcript_file_path=transcript_file_path,
-                                    lrg_refseqgene_path=refseq_file_path,
-                                    mane_data_path=mane_data_path,
-                                    db_url=uta_db_url, db_pwd=uta_db_pwd)
-        self._seqrepo_access = cool_seq_tool.seqrepo_access
+        uta_tools = UTATools(seqrepo_data_path=seqrepo_data_path,
+                             transcript_file_path=transcript_file_path,
+                             lrg_refseqgene_path=refseq_file_path,
+                             mane_data_path=mane_data_path,
+                             db_url=uta_db_url, db_pwd=uta_db_pwd)
+        self._seqrepo_access = uta_tools.seqrepo_access
 
-        vrs_representation = VRSRepresentation(self._seqrepo_access)
+        dp = SeqRepoDataProxy(self._seqrepo_access.seqrepo_client)
 
+        vrs_representation = VRSRepresentation(dp, self._seqrepo_access)
+
+        amino_acid_cache = AminoAcidCache(amino_acids_file_path=amino_acids_file_path)
         gene_normalizer = GeneQueryHandler(db_url=dynamodb_url,
                                            db_region=dynamodb_region)
         gene_symbol = GeneSymbol(gene_normalizer)
-        tokenizer = Tokenize(gene_symbol)
+        tokenizer = Tokenize(amino_acid_cache, gene_symbol)
         classifier = Classify()
-        uta_db = cool_seq_tool.uta_db
-        mane_transcript = cool_seq_tool.mane_transcript
-        transcript_mappings = cool_seq_tool.transcript_mappings
-        self._tlr = Translator(data_proxy=self._seqrepo_access)
+        uta_db = uta_tools.uta_db
+        mane_transcript = uta_tools.mane_transcript
+        transcript_mappings = uta_tools.transcript_mappings
+        self._tlr = Translator(data_proxy=dp)
         validator = Validate(
             self._seqrepo_access, transcript_mappings, gene_symbol, mane_transcript,
-            uta_db, self._tlr, gene_normalizer, vrs_representation
+            uta_db, self._tlr, amino_acid_cache, gene_normalizer, vrs_representation
         )
         translator = Translate()
         hgvs_dup_del_mode = HGVSDupDelMode(self._seqrepo_access)
-        to_vrs_params = [self._seqrepo_access, tokenizer,
-                         classifier, validator, translator, hgvs_dup_del_mode,
-                         gene_normalizer]
+        to_vrs_params = [self._seqrepo_access, dp, tokenizer, classifier, validator,
+                         translator, hgvs_dup_del_mode, gene_normalizer]
         self.to_vrs_handler = ToVRS(*to_vrs_params)
         self.to_vrsatile_handler = ToVRSATILE(*to_vrs_params)
         self.normalize_handler = Normalize(*to_vrs_params + [uta_db])
 
-        codon_table = CodonTable()
-        mane_transcript_mappings = cool_seq_tool.mane_transcript_mappings
+        codon_table = CodonTable(amino_acid_cache)
+        mane_transcript_mappings = uta_tools.mane_transcript_mappings
         to_protein_params = to_vrs_params + [uta_db,
                                              mane_transcript, mane_transcript_mappings,
                                              codon_table]
         self.gnomad_vcf_to_protein_handler = GnomadVcfToProteinVariation(
             *to_protein_params)
         self.to_canonical_handler = ToCanonicalVariation(
             *to_vrs_params + [self._tlr, uta_db])
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/schemas/classification_response_schema.py` & `variation-normalizer-0.7.dev0/variation/schemas/classification_response_schema.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/schemas/hgvs_to_copy_number_schema.py` & `variation-normalizer-0.7.dev0/variation/schemas/hgvs_to_copy_number_schema.py`

 * *Files 2% similar despite different names*

```diff
@@ -85,15 +85,15 @@
                     "location": {
                         "id": "ga4gh:SL.KefUQwlqEBGtzoNO-MzOozx7_H1uP-fD",
                         "type": "SequenceLocation",
                         "sequence_id": "ga4gh:SQ.Zu7h9AggXxhTaGVsy7h_EZSChSZGcmgX",
                         "start": {"type": "Number", "value": 49531260},
                         "end": {"type": "Number", "value": 49531262}
                     },
-                    "relative_copy_class": "EFO:0030069"
+                    "relative_copy_class": "complete loss"
                 },
                 "service_meta_": {
                     "name": "variation-normalizer",
                     "version": "0.2.17",
                     "response_datetime": "2022-01-26T22:23:41.821673",
                     "url": "https://github.com/cancervariants/variation-normalization"
                 }
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/schemas/normalize_response_schema.py` & `variation-normalizer-0.7.dev0/variation/schemas/normalize_response_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -250,15 +250,15 @@
                 schema.pop("title", None)
             for prop in schema.get("properties", {}).values():
                 prop.pop("title", None)
             schema["example"] = {
                 "query": "NC_000007.14:140753335:A:T",
                 "warnings": [],
                 "canonical_variation": {
-                    "id": "ga4gh:CAN.dP6z4p7SoGJFmlFQcjOQo2d1mXuo1QiY",
+                    "id": "ga4gh:CLV.dP6z4p7SoGJFmlFQcjOQo2d1mXuo1QiY",
                     "type": "CanonicalVariation",
                     "canonical_context": {
                         "id": "ga4gh:VA.3xFHF399HGbG1JUf5uwcj3oWVKZJ70oX",
                         "type": "Allele",
                         "location": {
                             "id": "ga4gh:SL.WBLxdkoypnRME6b8tJtlOWqZKU1ruqY1",
                             "type": "SequenceLocation",
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/schemas/service_schema.py` & `variation-normalizer-0.7.dev0/variation/schemas/service_schema.py`

 * *Files 2% similar despite different names*

```diff
@@ -129,15 +129,15 @@
                     "location": {
                         "id": "ga4gh:SL.po-AExwyqkstDx3JWYn6plIlxn5eojv4",
                         "type": "SequenceLocation",
                         "sequence_id": "ga4gh:SQ.F-LrLMe1SRpfUZHkQmvkVKFEGaoDeHul",
                         "start": {"type": "Number", "value": 140713327},
                         "end": {"type": "Number", "value": 140924929}
                     },
-                    "relative_copy_class": "EFO:0030072"
+                    "relative_copy_class": "high-level gain"
                 },
                 "service_meta_": {
                     "version": "0.7.dev0",
                     "response_datetime": "2022-09-29T15:08:18.696882",
                     "name": "variation-normalizer",
                     "url": "https://github.com/cancervariants/variation-normalization"
                 }
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/schemas/to_vrs_response_schema.py` & `variation-normalizer-0.7.dev0/variation/schemas/to_vrs_response_schema.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/schemas/token_response_schema.py` & `variation-normalizer-0.7.dev0/variation/schemas/token_response_schema.py`

 * *Files 0% similar despite different names*

```diff
@@ -505,15 +505,14 @@
     """A sequence change between the translation initiation (start) and
     termination (stop) codon where, compared to a reference sequence, one or
     more amino acids are not present (deleted) - varnomen.hgvs.org
     """
 
     start_aa_del: str
     end_aa_del: Optional[str]
-    deleted_aa: Optional[str]
     coordinate_type = CoordinateType.PROTEIN
     token_type = "ProteinDeletion"
     so_id = SequenceOntology.PROTEIN_DELETION
     molecule_context = "protein"
 
 
 class CodingDNADeletionToken(Deletion):
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/schemas/validation_response_schema.py` & `variation-normalizer-0.7.dev0/variation/schemas/validation_response_schema.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/schemas/vrs_python_translator_schema.py` & `variation-normalizer-0.7.dev0/variation/schemas/vrs_python_translator_schema.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/to_canonical_variation.py` & `variation-normalizer-0.7.dev0/variation/to_canonical_variation.py`

 * *Files 2% similar despite different names*

```diff
@@ -3,17 +3,18 @@
 from datetime import datetime
 
 import python_jsonschema_objects
 from ga4gh.vrsatile.pydantic.vrs_models import Text, VRSTypes
 from ga4gh.vrsatile.pydantic.vrsatile_models import CanonicalVariation
 from ga4gh.vrs import models
 from ga4gh.core import ga4gh_identify
+from ga4gh.vrs.dataproxy import SeqRepoDataProxy
 from ga4gh.vrs.extras.translator import Translator
-from cool_seq_tool.schemas import Assembly
-from cool_seq_tool.data_sources import UTADatabase, SeqRepoAccess
+from uta_tools.schemas import Assembly
+from uta_tools.data_sources import UTADatabase, SeqRepoAccess
 from gene.query import QueryHandler as GeneQueryHandler
 
 from variation.classifiers.classify import Classify
 from variation.hgvs_dup_del_mode import HGVSDupDelMode
 from variation.schemas.app_schemas import Endpoint
 from variation.schemas.normalize_response_schema import ServiceMeta, \
     ToCanonicalVariationFmt, ToCanonicalVariationService
@@ -28,32 +29,33 @@
 from variation.validators.validate import Validate
 from variation.version import __version__
 
 
 class ToCanonicalVariation(ToVRS):
     """Class for translating to canonical variation"""
 
-    def __init__(self, seqrepo_access: SeqRepoAccess,
+    def __init__(self, seqrepo_access: SeqRepoAccess, dp: SeqRepoDataProxy,
                  tokenizer: Tokenize, classifier: Classify, validator: Validate,
                  translator: Translate, hgvs_dup_del_mode: HGVSDupDelMode,
                  gene_normalizer: GeneQueryHandler,
                  tlr: Translator, uta: UTADatabase) -> None:
         """Initialize the to canonical variation class
 
-        :param SeqRepoAccess seqrepo_access: Access to SeqRepo via cool-seq-tool
+        :param SeqRepoAccess seqrepo_access: Access to SeqRepo via UTA Tools
+        :param SeqRepoDataProxy dp: Access to SeqRepo via VRS Python
         :param Tokenize tokenizer: Tokenizer class for tokenizing
         :param Classify classifier: Classifier class for classifying tokens
         :param Validate validator: Validator class for validating valid inputs
         :param Translate translator: Translating valid inputs
         :param HGVSDupDelMode hgvs_dup_del_mode: Class for handling
             HGVS dup/del expressions
         :param Translator tlr: Class for translating nomenclatures to and from VRS
         :param UTADatabase uta: Access to UTA queries
         """
-        super().__init__(seqrepo_access, tokenizer, classifier, validator,
+        super().__init__(seqrepo_access, dp, tokenizer, classifier, validator,
                          translator, hgvs_dup_del_mode, gene_normalizer)
         self.tlr = tlr
         self.uta = uta
 
     async def to_canonical_variation(
         self, q: str,
         fmt: ToCanonicalVariationFmt,
@@ -166,15 +168,15 @@
             end_pos = start_pos + int(deleted_seq)
 
         if do_liftover:
             newest_assembly_acs = await self.uta.get_newest_assembly_ac(ac)
             if not newest_assembly_acs:
                 warnings.append(f"Unable to get newest assemblies for {ac}")
                 return variation, None
-            new_ac = newest_assembly_acs[0]
+            new_ac = newest_assembly_acs[0][0]
             if new_ac != ac:
                 ac = new_ac
                 chromosome, warning = self.seqrepo_access.ac_to_chromosome(ac)
                 if not chromosome:
                     warnings.append(warning)
                     return variation, warnings
                 chromosome = f"chr{chromosome}"
@@ -196,15 +198,16 @@
             warnings.append(f"vrs-python translator raised error: {e}")
         except KeyError as e:
             warnings.append(f"vrs-python translator raised error: "
                             f"seqrepo could not translate identifier {e}")
         else:
             # Validate SPDI
             try:
-                sequence = self.seqrepo_access.sr.fetch(ac, start_pos, end=end_pos)
+                sequence = self.seqrepo_access.seqrepo_client.fetch(
+                    ac, start_pos, end=end_pos)
             except ValueError as e:
                 warnings.append(str(e))
             else:
                 if not sequence:
                     warnings.append(f"Position, {start_pos}, does not exist on {ac}")
                 else:
                     if not deleted_seq_is_int and deleted_seq != sequence:
@@ -249,15 +252,15 @@
                 hgvs_classifications.append(c)
         if not hgvs_classifications:
             warnings = [f"{q} is not a supported HGVS expression"]
             return variation, warnings
 
         if hgvs_dup_del_mode == HGVSDupDelModeEnum.RELATIVE_CNV:
             if relative_copy_class:
-                if relative_copy_class.upper() not in VALID_RELATIVE_COPY_CLASS:
+                if relative_copy_class.lower() not in VALID_RELATIVE_COPY_CLASS:
                     return None, [f"{relative_copy_class} is not a valid relative "
                                   f"copy class: {VALID_RELATIVE_COPY_CLASS}"]
         elif hgvs_dup_del_mode == HGVSDupDelModeEnum.ABSOLUTE_CNV:
             if not baseline_copies:
                 return None, [f"{hgvs_dup_del_mode} requires `baseline_copies`"]
         elif not hgvs_dup_del_mode:
             hgvs_dup_del_mode = HGVSDupDelModeEnum.DEFAULT
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/to_copy_number_variation.py` & `variation-normalizer-0.7.dev0/variation/to_copy_number_variation.py`

 * *Files 1% similar despite different names*

```diff
@@ -148,15 +148,15 @@
         :param bool do_liftover: Whether or not to liftover to GRCh38 assembly
         :param bool untranslatable_returns_text: `True` return VRS Text Object when
             unable to translate or normalize query. `False` return `None` when
             unable to translate or normalize query.
         :return: HgvsToRelativeCopyNumberService containing Relative Copy Number
             Variation and warnings
         """
-        if relative_copy_class and relative_copy_class.upper() not in VALID_RELATIVE_COPY_CLASS:  # noqa: E501
+        if relative_copy_class and relative_copy_class.lower() not in VALID_RELATIVE_COPY_CLASS:  # noqa: E501
             return None, [f"{relative_copy_class} is not a valid relative copy class: "
                           f"{VALID_RELATIVE_COPY_CLASS}"]
 
         validations, warnings = await self.get_validations(
             hgvs_expr, endpoint_name=Endpoint.HGVS_TO_RELATIVE_CN,
             hgvs_dup_del_mode=HGVSDupDelModeEnum.RELATIVE_CNV,
             relative_copy_class=relative_copy_class, do_liftover=do_liftover
@@ -255,16 +255,16 @@
 
             if warnings:
                 if untranslatable_returns_text:
                     variation, warnings = self._parsed_to_text(
                         start, end, total_copies, warnings, assembly, chr, accession)
             else:
                 try:
-                    self.seqrepo_access.sr[accession][start - 1]
-                    self.seqrepo_access.sr[accession][end]
+                    self.seqrepo_access.seqrepo_client[accession][start - 1]
+                    self.seqrepo_access.seqrepo_client[accession][end]
                 except ValueError as e:
                     warnings.append(str(e).replace("start", "Position"))
                     if untranslatable_returns_text:
                         variation, warnings = self._parsed_to_text(
                             start, end, total_copies, warnings, assembly, chr,
                             accession)
                 else:
@@ -367,15 +367,15 @@
                             f"gene-normalizer could not find a priority sequence "
                             f"location for gene: {gene_norm_label}")
 
                 if vrs_location:
                     vrs_location.id = ga4gh_identify(vrs_location)
                     vrs_rcn = models.RelativeCopyNumber(
                         location=vrs_location,
-                        relative_copy_class=RelativeCopyClass.HIGH_LEVEL_COPY_NUMBER_GAIN.value)  # noqa: E501
+                        relative_copy_class=RelativeCopyClass.HIGH_LEVEL_GAIN.value)
                     vrs_rcn.id = ga4gh_identify(vrs_rcn)
                     variation = RelativeCopyNumber(**vrs_rcn.as_dict())
             else:
                 warnings.append(f"gene-normalizer returned no match for gene: {gene}")
 
         if not variation and untranslatable_returns_text:
             text_variation = models.Text(definition=amplification_label)
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/to_vrs.py` & `variation-normalizer-0.7.dev0/variation/to_vrs.py`

 * *Files 6% similar despite different names*

```diff
@@ -3,16 +3,17 @@
 from urllib.parse import unquote
 from datetime import datetime
 
 from ga4gh.vrsatile.pydantic.vrs_models import Allele, Haplotype, AbsoluteCopyNumber,\
     VariationSet, Text
 from ga4gh.vrs import models
 from ga4gh.core import ga4gh_identify
-from cool_seq_tool.schemas import ResidueMode
-from cool_seq_tool.data_sources import SeqRepoAccess
+from uta_tools.schemas import ResidueMode
+from uta_tools.data_sources import SeqRepoAccess
+from ga4gh.vrs.dataproxy import SeqRepoDataProxy
 from gene.query import QueryHandler as GeneQueryHandler
 
 from variation.schemas.normalize_response_schema\
     import HGVSDupDelMode as HGVSDupDelModeEnum, ServiceMeta
 from variation.hgvs_dup_del_mode import HGVSDupDelMode
 from variation.schemas.app_schemas import Endpoint
 from variation.schemas.hgvs_to_copy_number_schema import VALID_CLASSIFICATION_TYPES,\
@@ -27,30 +28,31 @@
 from variation.vrs_representation import VRSRepresentation
 from variation.version import __version__
 
 
 class ToVRS(VRSRepresentation):
     """The class for translating variation strings to VRS representations."""
 
-    def __init__(self, seqrepo_access: SeqRepoAccess,
+    def __init__(self, seqrepo_access: SeqRepoAccess, dp: SeqRepoDataProxy,
                  tokenizer: Tokenize, classifier: Classify, validator: Validate,
                  translator: Translate, hgvs_dup_del_mode: HGVSDupDelMode,
                  gene_normalizer: GeneQueryHandler) -> None:
         """Initialize the ToVrsAndVrsatile class.
 
-        :param SeqRepoAccess seqrepo_access: Access to SeqRepo
+        :param SeqRepoAccess seqrepo_access: Access to SeqRepo via UTA Tools
+        :param SeqRepoDataProxy dp: Access to SeqRepo via VRS Python
         :param Tokenize tokenizer: Tokenizer class for tokenizing
         :param Classify classifier: Classifier class for classifying tokens
         :param Validate validator: Validator class for validating valid inputs
         :param Translate translator: Translating valid inputs
         :param HGVSDupDelMode hgvs_dup_del_mode: Class for handling
             HGVS dup/del expressions
         :param GeneQueryHandler gene_normalizer: Client for normalizing gene concepts
         """
-        super().__init__(seqrepo_access)
+        super().__init__(dp, seqrepo_access)
         self.tokenizer = tokenizer
         self.classifier = classifier
         self.validator = validator
         self.translator = translator
         self.hgvs_dup_del_mode = hgvs_dup_del_mode
         self.gene_normalizer = gene_normalizer
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/to_vrsatile.py` & `variation-normalizer-0.7.dev0/variation/to_vrsatile.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/__init__.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/__init__.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/caches/nucleotide_cache.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/caches/nucleotide_cache.py`

 * *Files 0% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 class NucleotideCache:
     """A class to cache nucleotides."""
 
     def __init__(self) -> None:
         """Initialize NucleotideCache class.
         https://varnomen.hgvs.org/bg-material/standards/
         """
-        self.base_nucleotides = {"A", "C", "T", "G", "N"}
+        self.base_nucleotides = {"A", "C", "T", "G"}
         self.nucleotides = {
             "A": ["A"],
             "C": ["C"],
             "T": ["T"],
             "G": ["G"],
             "B": ["C", "G", "T"],
             "D": ["A", "G", "T"],
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/coding_dna_deletion.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/coding_dna_deletion.py`

 * *Files 20% similar despite different names*

```diff
@@ -5,14 +5,10 @@
 from variation.tokenizers.deletion_base import DeletionBase
 
 
 class CodingDNADeletion(DeletionBase):
     """Class for tokenizing Deletion at the coding dna reference sequence."""
 
     def return_token(self, params: Dict) -> Optional[CodingDNADeletionToken]:
-        """Return coding DNA Deletion token if match
-
-        :param Dict params: Matched parameters for deletion
-        :return: `CodingDNADeletionToken` if on c coordinate, else `None`
-        """
-        if params["coordinate_type"] == "c":
+        """Return coding DNA Deletion token."""
+        if self.parts["coordinate_type"] == "c":
             return CodingDNADeletionToken(**params)
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/coding_dna_delins.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/coding_dna_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/coding_dna_insertion.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/coding_dna_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/coding_dna_silent_mutation.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/coding_dna_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/coding_dna_substitution.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/coding_dna_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/deletion_base.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/deletion_range_base.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,69 +1,69 @@
-"""A module for Deletion Tokenization Base Class."""
+"""A module for tokenizing genomic deletion ranges."""
+from typing import Dict, Optional, List
 from abc import abstractmethod
-from typing import Optional, Dict
-import re
 
-from variation.schemas.token_response_schema import Deletion, TokenMatchType
+from variation.schemas.token_response_schema import TokenMatchType, \
+    DeletionRange
 from .tokenizer import Tokenizer
 
 
-class DeletionBase(Tokenizer):
-    """Class for tokenizing Deletions."""
+class DeletionRangeBase(Tokenizer):
+    """The tokenizer class for genomic deletion range."""
 
-    pattern = r"^(?P<start_pos>\d+)" \
-              r"(_(?P<end_pos>\d+))?del(?P<deleted_seq>[actgn]+)?$"
-    splitter = re.compile(pattern)
+    def __init__(self) -> None:
+        """Initialize the Genomic Deletion Range Class."""
+        self.parts = None
 
-    def match(self, input_string: str) -> Optional[Deletion]:
+    def match(self, input_string: str) -> Optional[DeletionRange]:
         """Return tokens that match the input string.
 
         :param str input_string: Input string
-        :return: Deletion token if a match is found, else `None`
+        :return: DeletionRange token if a match is found
         """
-        parts = {
+        if input_string is None:
+            return None
+
+        self.parts = {
             "token": input_string,
             "input_string": input_string,
             "match_type": TokenMatchType.UNSPECIFIED.value,
-            "start_pos_del": None,
-            "end_pos_del": None,
-            "deleted_sequence": None,
+            "start_pos1_del": None,
+            "start_pos2_del": None,
+            "end_pos1_del": None,
+            "end_pos2_del": None,
             "coordinate_type": None
         }
 
-        input_str_l = str(input_string).lower()
-
-        if input_str_l.startswith("p."):
+        input_string = str(input_string).lower()
+        if not input_string.endswith("del"):
             return None
 
-        if input_str_l.startswith(("c.", "g.")):
-            parts["coordinate_type"] = input_str_l[:1]
-            input_str_l = input_str_l[2:]
-
-        if input_str_l.startswith("(") and input_str_l.endswith(")"):
-            input_str_l = input_str_l[1:-1]
-
-        match = self.splitter.match(input_str_l)
-        if not match:
+        if input_string.startswith("g."):
+            self.parts["coordinate_type"] = "g"
+        elif input_string.startswith("c."):
+            self.parts["coordinate_type"] = "c"
+        elif input_string.startswith("p."):
+            self.parts["coordinate_type"] = "p"
+        else:
             return None
 
-        params = match.groupdict()
+        parts = input_string.split("_")
+        self._get_parts(parts)
+        return self.return_token(self.parts)
 
-        parts["start_pos_del"] = params["start_pos"]
-        parts["end_pos_del"] = params["end_pos"]
-        if parts["start_pos_del"] and parts["end_pos_del"]:
-            if parts["start_pos_del"] > parts["end_pos_del"]:
-                return None
-
-        parts["deleted_sequence"] = \
-            params["deleted_seq"].upper() if params["deleted_seq"] else None
+    @abstractmethod
+    def _get_parts(self, parts: List) -> None:
+        """Set `self.parts` for genomic deletion range
 
-        return self.return_token(parts)
+        :param List parts: Parts of input string
+        """
+        raise NotImplementedError
 
     @abstractmethod
-    def return_token(self, params: Dict[str, str]) -> Optional[Deletion]:
+    def return_token(self, params: Dict[str, str]) -> Optional[DeletionRange]:
         """Return token instance.
 
-        :param Dict params: Params for Deletion token
-        :return: Deletion token
+        :param Dict params: Params for DeletionRange token
+        :return: DeletionRange token
         """
         raise NotImplementedError
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/deletion_range_base.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/protein_insertion.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,69 +1,81 @@
-"""A module for tokenizing genomic deletion ranges."""
-from typing import Dict, Optional, List
-from abc import abstractmethod
+"""A module for Protein Insertion Tokenization Class."""
+from typing import List, Optional
 
-from variation.schemas.token_response_schema import TokenMatchType, \
-    DeletionRange
-from .tokenizer import Tokenizer
+from pydantic.error_wrappers import ValidationError
 
+from variation.schemas.token_response_schema import ProteinInsertionToken, \
+    TokenMatchType
+from .caches import AminoAcidCache, NucleotideCache
+from .tokenizer import Tokenizer
+from .tokenize_base import TokenizeBase
 
-class DeletionRangeBase(Tokenizer):
-    """The tokenizer class for genomic deletion range."""
 
-    def __init__(self) -> None:
-        """Initialize the Genomic Deletion Range Class."""
-        self.parts = None
+class ProteinInsertion(Tokenizer):
+    """Class for tokenizing Insertions on the protein reference sequence."""
 
-    def match(self, input_string: str) -> Optional[DeletionRange]:
-        """Return tokens that match the input string.
+    def __init__(self, amino_acid_cache: AminoAcidCache,
+                 nucleotide_cache: NucleotideCache) -> None:
+        """Initialize the Protein Insertion Class.
 
-        :param str input_string: Input string
-        :return: DeletionRange token if a match is found
+        :param AminoAcidCache amino_acid_cache: Valid amino acid codes
+        :param NucleotideCache nucleotide_cache: Valid nucleotides
         """
+        self.parts = None
+        self.tokenize_base = TokenizeBase(amino_acid_cache, nucleotide_cache)
+
+    def match(self, input_string: str) -> Optional[ProteinInsertionToken]:
+        """Return token that match the input string."""
         if input_string is None:
             return None
 
         self.parts = {
+            "used_one_letter": False,
             "token": input_string,
             "input_string": input_string,
             "match_type": TokenMatchType.UNSPECIFIED.value,
-            "start_pos1_del": None,
-            "start_pos2_del": None,
-            "end_pos1_del": None,
-            "end_pos2_del": None,
-            "coordinate_type": None
+            "start_aa_flank": None,
+            "start_pos_flank": None,
+            "end_aa_flank": None,
+            "end_pos_flank": None
         }
 
         input_string = str(input_string).lower()
-        if not input_string.endswith("del"):
+
+        if "c." in input_string or "g." in input_string:
             return None
 
-        if input_string.startswith("g."):
-            self.parts["coordinate_type"] = "g"
-        elif input_string.startswith("c."):
-            self.parts["coordinate_type"] = "c"
-        elif input_string.startswith("p."):
-            self.parts["coordinate_type"] = "p"
-        else:
+        if input_string.startswith("p."):
+            input_string = input_string[2:]
+
+        if input_string.startswith("(") and input_string.endswith(")"):
+            input_string = input_string[1:-1]
+
+        if "ins" not in input_string:
             return None
 
-        parts = input_string.split("_")
+        parts = input_string.split("ins")
         self._get_parts(parts)
-        return self.return_token(self.parts)
 
-    @abstractmethod
+        try:
+            return ProteinInsertionToken(**self.parts)
+        except ValidationError:
+            return None
+
     def _get_parts(self, parts: List) -> None:
-        """Set `self.parts` for genomic deletion range
+        """Get parts for Protein Insertion.
 
         :param List parts: Parts of input string
         """
-        raise NotImplementedError
-
-    @abstractmethod
-    def return_token(self, params: Dict[str, str]) -> Optional[DeletionRange]:
-        """Return token instance.
+        if len(parts) != 2:
+            return
 
-        :param Dict params: Params for DeletionRange token
-        :return: DeletionRange token
-        """
-        raise NotImplementedError
+        range_aa_pos = self.tokenize_base.get_aa_pos_range(parts)
+        if range_aa_pos:
+            self.parts["start_aa_flank"] = range_aa_pos[0]
+            self.parts["end_aa_flank"] = range_aa_pos[1]
+            self.parts["start_pos_flank"] = range_aa_pos[2]
+            self.parts["end_pos_flank"] = range_aa_pos[3]
+            self.parts["used_one_letter"] = range_aa_pos[4]
+        self.parts["inserted_sequence"] = \
+            self.tokenize_base.get_protein_inserted_sequence(
+                parts, self.parts["used_one_letter"])
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/delins_base.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/delins_base.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,27 +1,29 @@
 """A module for DelIns Tokenization Base Class."""
 from abc import abstractmethod
 from typing import Optional, Dict, List
 
 from variation.schemas.token_response_schema import DelIns, TokenMatchType, Token
 from .tokenizer import Tokenizer
-from .caches import NucleotideCache
+from .caches import AminoAcidCache, NucleotideCache
 from .tokenize_base import TokenizeBase
 
 
 class DelInsBase(Tokenizer):
     """Class for tokenizing DelIns."""
 
-    def __init__(self, nucleotide_cache: NucleotideCache) -> None:
+    def __init__(self, amino_acid_cache: AminoAcidCache,
+                 nucleotide_cache: NucleotideCache) -> None:
         """Initialize the DelIns Class.
 
+        :param AminoAcidCache amino_acid_cache: Valid amino acid codes
         :param NucleotideCache nucleotide_cache: Valid nucleotides
         """
         self.parts = None
-        self.tokenize_base = TokenizeBase(nucleotide_cache)
+        self.tokenize_base = TokenizeBase(amino_acid_cache, nucleotide_cache)
 
     def match(self, input_string: str) -> Optional[DelIns]:
         """Return tokens that match the input string."""
         if input_string is None:
             return None
 
         input_string = str(input_string).lower()
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/duplication_base.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/duplication_base.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/free_text_categorical.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/free_text_categorical.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/gene_pair.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/gene_pair.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/gene_symbol.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/gene_symbol.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_deletion.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/genomic_deletion.py`

 * *Files 9% similar despite different names*

```diff
@@ -5,14 +5,10 @@
 from variation.tokenizers.deletion_base import DeletionBase
 
 
 class GenomicDeletion(DeletionBase):
     """Class for tokenizing Deletion at the genomic reference sequence."""
 
     def return_token(self, params: Dict) -> Optional[GenomicDeletionToken]:
-        """Return Genomic Deletion token if match
-
-        :param Dict params: Matched parameters for deletion
-        :return: `GenomicDeletionToken` if on c coordinate, else `None`
-        """
-        if params["coordinate_type"] == "g":
+        """Return Genomic Deletion token."""
+        if self.parts["coordinate_type"] == "g":
             return GenomicDeletionToken(**params)
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_deletion_range.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/genomic_deletion_range.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_delins.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/genomic_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_duplication.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/genomic_duplication.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_insertion.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/genomic_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_silent_mutation.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/genomic_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_substitution.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/genomic_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/genomic_uncertain_deletion.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/genomic_uncertain_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/gnomad_vcf.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/gnomad_vcf.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/hgvs.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/hgvs.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/insertion_base.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/insertion_base.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,27 +1,29 @@
 """A module for Insertion Tokenization Base Class."""
 from abc import abstractmethod
 from typing import Optional, Dict, List
 
 from variation.schemas.token_response_schema import Insertion, TokenMatchType, Token
 from .tokenizer import Tokenizer
-from .caches import NucleotideCache
+from .caches import AminoAcidCache, NucleotideCache
 from .tokenize_base import TokenizeBase
 
 
 class InsertionBase(Tokenizer):
     """Class for tokenizing Insertion."""
 
-    def __init__(self, nucleotide_cache: NucleotideCache) -> None:
+    def __init__(self, amino_acid_cache: AminoAcidCache,
+                 nucleotide_cache: NucleotideCache) -> None:
         """Initialize the Insertion Class.
 
+        :param AminoAcidCache amino_acid_cache: Valid amino acid codes
         :param NucleotideCache nucleotide_cache: Valid nucleotides
         """
         self.parts = None
-        self.tokenize_base = TokenizeBase(nucleotide_cache)
+        self.tokenize_base = TokenizeBase(amino_acid_cache, nucleotide_cache)
 
     def match(self, input_string: str) -> Optional[Insertion]:
         """Return tokens that match the input string."""
         if input_string is None:
             return None
 
         self.parts = {
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/locus_reference_genomic.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/locus_reference_genomic.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/polypeptide_sequence_variation_base.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/polypeptide_sequence_variation_base.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,49 +1,47 @@
 """A module for Polypeptide Sequence Variation Tokenization Base Class."""
 import re
 from abc import abstractmethod
 from typing import List, Optional
 
-from bioutils.sequences import aa3_to_aa1, aa3_to_aa1_lut
-
+from .caches import AminoAcidCache
 from .tokenizer import Tokenizer
 from ..schemas.token_response_schema import Token
 
 
 class PolypeptideSequenceVariationBase(Tokenizer):
     """Class for tokenizing Polypeptide Sequence Variations."""
 
-    def __init__(self) -> None:
-        """Initialize the Polypeptide Sequence Variation Base Class."""
+    def __init__(self, amino_acid_cache: AminoAcidCache) -> None:
+        """Initialize the Polypeptide Sequence Variation Base Class.
+
+        :param AminoAcidCache amino_acid_cache: Valid amino acid codes.
+        """
+        self.amino_acid_cache = amino_acid_cache
         self.splitter = re.compile(r"(\d+)")
         self.psub = None
 
     def _set_psub(self, amino_acid: str, position: int, new_amino_acid: str) -> None:
         """Initialize protein substitution.
 
         :param str amino_acid: Reference amino acid
         :param int position: The position of the amino acid substituted
         :param str new_amino_acid: The new amino_acid
         """
-        for (key, aa_val) in [("amino_acid", amino_acid),
-                              ("new_amino_acid", new_amino_acid)]:
-            if len(aa_val) == 1:
-                self.psub[key] = aa_val.upper()
-            else:
-                try:
-                    self.psub[key] = aa3_to_aa1(aa_val.capitalize())
-                except KeyError:
-                    self.psub[key] = None
+        self.psub["amino_acid"] = amino_acid.upper() if len(amino_acid) == 1 \
+            else self.amino_acid_cache.convert_three_to_one(amino_acid)
         self.psub["position"] = int(position)
+        self.psub["new_amino_acid"] = new_amino_acid.upper() if \
+            len(new_amino_acid) == 1 else \
+            self.amino_acid_cache.convert_three_to_one(new_amino_acid)
 
     def _is_valid_amino_acid(self, amino_acids: List) -> bool:
         """Return whether or not amino acids are valid."""
-        valid = aa3_to_aa1_lut.values()
         for amino_acid_code in amino_acids:
-            if amino_acid_code not in valid:
+            if not self.amino_acid_cache.__contains__(amino_acid_code):
                 return False
         return True
 
     @abstractmethod
     def match(self, input_string: str) -> Optional[Token]:
         """Return tokens that match the input string."""
         raise NotImplementedError
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/polypeptide_truncation.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/polypeptide_truncation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/protein_alternate.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/protein_alternate.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,30 +1,30 @@
 """Module for Protein Alternate classification."""
 import re
 from typing import Optional
 
-from bioutils.sequences import aa3_to_aa1_lut
-
 from variation.schemas.token_response_schema import Token, TokenMatchType
 from .tokenizer import Tokenizer
+from .caches import AminoAcidCache
 
 
 class ProteinAlternate(Tokenizer):
     """The Protein Alternate Tokenization class."""
 
-    def __init__(self) -> None:
+    def __init__(self, amino_acid_cache: AminoAcidCache) -> None:
         """Initialize the Protein Alternate Tokenizer class."""
+        self.__amino_acid_cache = amino_acid_cache
         self.__splitter = re.compile(r"\d+")
 
     def match(self, input_string: str) -> Optional[Token]:
         """Return Protein Alternate tokens if input string matches."""
         potential_protein = self.__splitter.split(input_string)
-        if all((len(potential_protein) == 2,
-                potential_protein[0] in aa3_to_aa1_lut,
-                not potential_protein[1])):
+        if (len(potential_protein) == 2 and  # noqa: W504
+                potential_protein[0] in self.__amino_acid_cache and   # noqa: W504
+                not potential_protein[1]):
             return Token(
                 token=potential_protein[0],
                 token_type="ProteinAlternate",
                 input_string=input_string,
                 match_type=TokenMatchType.UNSPECIFIED
             )
         else:
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/protein_delins.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/protein_delins.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,29 +1,31 @@
 """A module for Protein DelIns Tokenization Class."""
 from typing import List, Optional
 
 from pydantic.error_wrappers import ValidationError
 
 from variation.schemas.token_response_schema import ProteinDelInsToken, \
     TokenMatchType
-from .caches import NucleotideCache
+from .caches import AminoAcidCache, NucleotideCache
 from .tokenizer import Tokenizer
 from .tokenize_base import TokenizeBase
 
 
 class ProteinDelIns(Tokenizer):
     """Class for tokenizing DelIns on the protein reference sequence."""
 
-    def __init__(self, nucleotide_cache: NucleotideCache) -> None:
+    def __init__(self, amino_acid_cache: AminoAcidCache,
+                 nucleotide_cache: NucleotideCache) -> None:
         """Initialize the Protein DelIns Class.
 
+        :param AminoAcidCache amino_acid_cache: Valid amino acid codes
         :param NucleotideCache nucleotide_cache: Valid nucleotides
         """
         self.parts = None
-        self.tokenize_base = TokenizeBase(nucleotide_cache)
+        self.tokenize_base = TokenizeBase(amino_acid_cache, nucleotide_cache)
 
     def match(self, input_string: str) -> Optional[ProteinDelInsToken]:
         """Return token that match the input string."""
         if input_string is None:
             return None
 
         input_string = str(input_string).lower()
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/protein_substitution.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/protein_substitution.py`

 * *Files 6% similar despite different names*

```diff
@@ -17,18 +17,14 @@
             Otherwise, None.
         """
         if input_string is None:
             return None
 
         input_string = str(input_string).lower()
 
-        if input_string.endswith(("*", "ter")):
-            # Handled in polypeptide truncation
-            return None
-
         psub_parts = None
         self.psub = {
             "amino_acid": None,
             "position": None,
             "new_amino_acid": None
         }
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/reference_sequence.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/reference_sequence.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/silent_mutation.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/single_nucleotide_variation_base.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/single_nucleotide_variation_base.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/tokenize.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/tokenize.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 """A module for tokenizing."""
 from typing import Iterable, List
 
 from variation.schemas.token_response_schema import Token, TokenMatchType
+from variation.tokenizers.caches.amino_acid_cache import AminoAcidCache
 from .gene_symbol import GeneSymbol
 from .protein_substitution import ProteinSubstitution
 from .polypeptide_truncation import PolypeptideTruncation
 from .silent_mutation import SilentMutation
 from .coding_dna_substitution import CodingDNASubstitution
 from .genomic_substitution import GenomicSubstitution
 from .coding_dna_silent_mutation import CodingDNASilentMutation
@@ -29,40 +30,41 @@
 from .free_text_categorical import FreeTextCategorical
 from .caches import NucleotideCache
 
 
 class Tokenize:
     """The tokenize class."""
 
-    def __init__(self, gene_symbol: GeneSymbol) -> None:
+    def __init__(self, amino_acid_cache: AminoAcidCache,
+                 gene_symbol: GeneSymbol) -> None:
         """Initialize the tokenize class."""
         nucleotide_cache = NucleotideCache()
         self.tokenizers = (
             HGVS(),
             ReferenceSequence(),
             LocusReferenceGenomic(),
             GnomadVCF(),
             gene_symbol,
             FreeTextCategorical(),
-            ProteinSubstitution(),
-            PolypeptideTruncation(),
-            SilentMutation(),
+            ProteinSubstitution(amino_acid_cache),
+            PolypeptideTruncation(amino_acid_cache),
+            SilentMutation(amino_acid_cache),
             CodingDNASubstitution(),
             GenomicSubstitution(),
             CodingDNASilentMutation(),
             GenomicSilentMutation(),
-            ProteinDelIns(nucleotide_cache),
-            CodingDNADelIns(nucleotide_cache),
-            GenomicDelIns(nucleotide_cache),
-            ProteinDeletion(),
-            CodingDNADeletion(),
-            GenomicDeletion(),
-            ProteinInsertion(nucleotide_cache),
-            CodingDNAInsertion(nucleotide_cache),
-            GenomicInsertion(nucleotide_cache),
+            ProteinDelIns(amino_acid_cache, nucleotide_cache),
+            CodingDNADelIns(amino_acid_cache, nucleotide_cache),
+            GenomicDelIns(amino_acid_cache, nucleotide_cache),
+            ProteinDeletion(amino_acid_cache, nucleotide_cache),
+            CodingDNADeletion(amino_acid_cache, nucleotide_cache),
+            GenomicDeletion(amino_acid_cache, nucleotide_cache),
+            ProteinInsertion(amino_acid_cache, nucleotide_cache),
+            CodingDNAInsertion(amino_acid_cache, nucleotide_cache),
+            GenomicInsertion(amino_acid_cache, nucleotide_cache),
             GenomicUncertainDeletion(),
             GenomicDuplication(),
             GenomicDeletionRange()
         )
 
     def perform(self, search_string: str, warnings: List[str]) -> Iterable[Token]:
         """Return an iterable of tokens for a given search string.
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/tokenizers/tokenize_base.py` & `variation-normalizer-0.7.dev0/variation/tokenizers/tokenize_base.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,25 +1,26 @@
 """Module for commonly used tokenization methods."""
 from typing import Tuple, Optional, Union, List
 import re
 
-from bioutils.sequences import aa3_to_aa1_lut, aa3_to_aa1, aa1_to_aa3
-
-from variation.tokenizers.caches import NucleotideCache
+from variation.tokenizers.caches import NucleotideCache, AminoAcidCache
 
 
 class TokenizeBase:
     """Class for Tokenize methods."""
 
-    def __init__(self, nucleotide_cache: NucleotideCache) -> None:
+    def __init__(self, amino_acid_cache: AminoAcidCache,
+                 nucleotide_cache: NucleotideCache) -> None:
         """Initialize Token Base class.
 
+        :param AminoAcidCache amino_acid_cache: Valid amino acid codes
         :param NucleotideCache nucleotide_cache: Valid nucleotides
         """
         self.nucleotide_cache = nucleotide_cache
+        self.amino_acid_cache = amino_acid_cache
         self.splitter_char_digit = re.compile("([a-zA-Z]+)([0-9]+)")
 
     def get_amino_acid_and_pos(
         self, part: List, used_one_letter: bool
     ) -> Optional[Tuple[str, int, bool]]:
         """Return amino acid and position.
 
@@ -38,27 +39,22 @@
                 (len(char_and_digits[0]) + len(char_and_digits[1])):
             return None
 
         aa = char_and_digits[0]
         if len(aa) == 1:
             if not used_one_letter:
                 used_one_letter = True
-
-            try:
-                tmp_aa = aa1_to_aa3(aa.upper())
-            except KeyError:
-                tmp_aa = None
+            tmp_aa = \
+                self.amino_acid_cache.amino_acid_code_conversion[aa.upper()]
         else:
-            if aa.capitalize() in aa3_to_aa1_lut:
-                tmp_aa = aa
-            else:
-                tmp_aa = None
+            tmp_aa = aa
         pos = char_and_digits[1]
 
-        if not tmp_aa or not pos.isdigit():
+        if not self.amino_acid_cache.__contains__(tmp_aa) \
+                or not pos.isdigit():
             return None
         return aa.upper(), pos, used_one_letter
 
     def get_protein_inserted_sequence(self, parts: List,
                                       used_one_letter: bool) -> Optional[str]:
         """Return inserted sequence for protein reference sequence.
 
@@ -71,31 +67,29 @@
         inserted_sequence = ""
         if used_one_letter:
             for i in range(len(parts[1])):
                 aa = parts[1][i:i + 1]
                 if len(aa) != 1:
                     return None
                 try:
-                    aa3_to_aa1_lut[aa1_to_aa3(aa.upper())]
+                    self.amino_acid_cache.amino_acid_code_conversion[aa.upper()]  # noqa: E501
                 except KeyError:
                     return None
                 else:
                     inserted_sequence += aa.upper()
         else:
             for i in range(0, len(parts[1]), 3):
                 aa = parts[1][i:i + 3]
-                if all((len(aa) != 3, aa not in aa3_to_aa1_lut, aa != "ter")):
-                    return None
-
-                try:
-                    inserted_sequence += aa3_to_aa1(aa.capitalize())
-                except KeyError:
-                    return None
+                if len(aa) != 3 or not self.amino_acid_cache.__contains__(aa):
+                    if aa != "ter":
+                        return None
+                inserted_sequence += \
+                    self.amino_acid_cache.convert_three_to_one(aa)
 
-        if not inserted_sequence:
+        if inserted_sequence == "":
             return None
         return inserted_sequence
 
     def get_aa_pos_range(self,
                          parts: List) -> Optional[Tuple[str, str, str, int, bool]]:
         """Get amino acid(s) and positions(s) for protein reference sequence.
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/__init__.py` & `variation-normalizer-0.7.dev0/variation/translators/__init__.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/amplification.py` & `variation-normalizer-0.7.dev0/variation/translators/amplification.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/coding_dna_deletion.py` & `variation-normalizer-0.7.dev0/variation/translators/coding_dna_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/coding_dna_delins.py` & `variation-normalizer-0.7.dev0/variation/translators/coding_dna_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/coding_dna_insertion.py` & `variation-normalizer-0.7.dev0/variation/translators/coding_dna_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/coding_dna_silent_mutation.py` & `variation-normalizer-0.7.dev0/variation/translators/coding_dna_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/coding_dna_substitution.py` & `variation-normalizer-0.7.dev0/variation/translators/coding_dna_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/genomic_deletion.py` & `variation-normalizer-0.7.dev0/variation/translators/genomic_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/genomic_deletion_range.py` & `variation-normalizer-0.7.dev0/variation/translators/genomic_deletion_range.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/genomic_delins.py` & `variation-normalizer-0.7.dev0/variation/translators/genomic_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/genomic_duplication.py` & `variation-normalizer-0.7.dev0/variation/translators/genomic_duplication.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/genomic_insertion.py` & `variation-normalizer-0.7.dev0/variation/translators/genomic_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/genomic_silent_mutation.py` & `variation-normalizer-0.7.dev0/variation/translators/genomic_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/genomic_substitution.py` & `variation-normalizer-0.7.dev0/variation/translators/genomic_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/genomic_uncertain_deletion.py` & `variation-normalizer-0.7.dev0/variation/translators/genomic_uncertain_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/polypeptide_truncation.py` & `variation-normalizer-0.7.dev0/variation/translators/polypeptide_truncation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/protein_deletion.py` & `variation-normalizer-0.7.dev0/variation/translators/protein_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/protein_delins.py` & `variation-normalizer-0.7.dev0/variation/translators/protein_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/protein_insertion.py` & `variation-normalizer-0.7.dev0/variation/translators/protein_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/protein_substitution.py` & `variation-normalizer-0.7.dev0/variation/translators/protein_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/silent_mutation.py` & `variation-normalizer-0.7.dev0/variation/translators/silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/translate.py` & `variation-normalizer-0.7.dev0/variation/translators/translate.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/translators/translator.py` & `variation-normalizer-0.7.dev0/variation/translators/translator.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/utils.py` & `variation-normalizer-0.7.dev0/variation/utils.py`

 * *Files 0% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 from typing import List, Tuple, Optional, Dict
 import re
 
 from ga4gh.vrsatile.pydantic.vrs_models import Text
 from ga4gh.vrsatile.pydantic.vrsatile_models import VariationDescriptor, GeneDescriptor
 from ga4gh.core import ga4gh_identify
 from ga4gh.vrs import models
-from cool_seq_tool.data_sources import SeqRepoAccess
+from uta_tools.data_sources import SeqRepoAccess
 
 from variation.schemas.classification_response_schema import ClassificationType
 from variation.schemas.validation_response_schema import ValidationSummary, \
     ValidationResult
 from variation.schemas.token_response_schema import Token
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/__init__.py` & `variation-normalizer-0.7.dev0/variation/validators/__init__.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/amplification.py` & `variation-normalizer-0.7.dev0/variation/validators/amplification.py`

 * *Files 1% similar despite different names*

```diff
@@ -57,17 +57,16 @@
             if gene_match_tokens:
                 gene_match_token = gene_match_tokens[0]
                 gene = gene_match_token.token
                 gene_descriptor = gene_match_token.gene_descriptor
                 seq_loc = get_priority_sequence_location(
                     gene_descriptor, self.seqrepo_access)
                 if seq_loc:
-                    rcn = self.vrs.to_rel_cnv(
-                        models.SequenceLocation(**seq_loc),
-                        RelativeCopyClass.HIGH_LEVEL_COPY_NUMBER_GAIN)
+                    rcn = self.vrs.to_rel_cnv(models.SequenceLocation(**seq_loc),
+                                              RelativeCopyClass.HIGH_LEVEL_GAIN)
                 else:
                     errors.append(f"No SequenceLocation found for gene: {gene}")
             else:
                 errors.append("No gene_tokens found")
 
             self.add_validation_result(rcn, valid_variations, results, classification,
                                        s, None, gene_tokens, errors)
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/coding_dna_deletion.py` & `variation-normalizer-0.7.dev0/variation/validators/coding_dna_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/coding_dna_delins.py` & `variation-normalizer-0.7.dev0/variation/validators/coding_dna_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/coding_dna_insertion.py` & `variation-normalizer-0.7.dev0/variation/validators/coding_dna_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/coding_dna_silent_mutation.py` & `variation-normalizer-0.7.dev0/variation/validators/coding_dna_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/coding_dna_substitution.py` & `variation-normalizer-0.7.dev0/variation/validators/coding_dna_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/delins_base.py` & `variation-normalizer-0.7.dev0/variation/validators/delins_base.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/duplication_deletion_base.py` & `variation-normalizer-0.7.dev0/variation/validators/duplication_deletion_base.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import logging
 from typing import Optional, List, Dict, Tuple, Union
 
 from ga4gh.vrsatile.pydantic.vrs_models import RelativeCopyClass
 from ga4gh.vrs import models
 from ga4gh.vrs.extras.translator import Translator
 from gene.query import QueryHandler as GeneQueryHandler
-from cool_seq_tool.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
+from uta_tools.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
     MANETranscript
 
 from variation.schemas.classification_response_schema import Classification, \
     ClassificationType
 from variation.schemas.app_schemas import Endpoint
 from variation.schemas.token_response_schema import Token, GeneMatchToken
 from variation.validators.validator import Validator
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/genomic_base.py` & `variation-normalizer-0.7.dev0/variation/validators/genomic_base.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,27 +1,27 @@
 """Module for Genomic Validation methods."""
 import logging
 from typing import List, Optional
 
-from cool_seq_tool.data_sources import UTADatabase, SeqRepoAccess
+from uta_tools.data_sources import UTADatabase, SeqRepoAccess
 
 from variation.schemas.classification_response_schema import Classification
 
 
 logger = logging.getLogger("variation")
 logger.setLevel(logging.DEBUG)
 
 
 class GenomicBase:
     """Genomic Base class for validation methods."""
 
     def __init__(self, seqrepo_access: SeqRepoAccess, uta: UTADatabase) -> None:
         """Initialize the Genomic base class.
 
-        :param SeqRepoAccess seqrepo_access: Access to seqrepo
+        :param SeqRepoDataProxy dp: Access to seqrepo data
         :param UTADatabase uta: Access to UTA queries
         """
         self.seqrepo_access = seqrepo_access
         self.uta = uta
 
     """The Genomic Base class."""
     async def get_nc_accessions(self, classification: Classification) -> List[str]:
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/genomic_deletion.py` & `variation-normalizer-0.7.dev0/variation/validators/genomic_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/genomic_deletion_range.py` & `variation-normalizer-0.7.dev0/variation/validators/genomic_deletion_range.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 import logging
 from typing import List, Optional, Dict, Tuple, Union
 
 from ga4gh.vrsatile.pydantic.vrs_models import RelativeCopyClass
 from ga4gh.vrs.extras.translator import Translator
 from ga4gh.vrs import models
 from gene.query import QueryHandler as GeneQueryHandler
-from cool_seq_tool.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
+from uta_tools.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
     MANETranscript
 
 from variation.schemas.classification_response_schema import \
     ClassificationType, Classification
 from variation.schemas.app_schemas import Endpoint
 from variation.schemas.token_response_schema import Token
 from variation.schemas.token_response_schema import GeneMatchToken
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/genomic_delins.py` & `variation-normalizer-0.7.dev0/variation/validators/genomic_delins.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/genomic_duplication.py` & `variation-normalizer-0.7.dev0/variation/validators/genomic_duplication.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/genomic_insertion.py` & `variation-normalizer-0.7.dev0/variation/validators/genomic_insertion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/genomic_silent_mutation.py` & `variation-normalizer-0.7.dev0/variation/validators/genomic_silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/genomic_substitution.py` & `variation-normalizer-0.7.dev0/variation/validators/genomic_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/genomic_uncertain_deletion.py` & `variation-normalizer-0.7.dev0/variation/validators/genomic_uncertain_deletion.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/insertion_base.py` & `variation-normalizer-0.7.dev0/variation/validators/insertion_base.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/polypeptide_sequence_variation_base.py` & `variation-normalizer-0.7.dev0/variation/validators/protein_deletion.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,58 +1,65 @@
-"""The module for Polypeptide Sequence Variation Validation."""
+"""The module for Protein Deletion Validation."""
 import logging
-from typing import List, Optional, Dict
+from typing import Dict, List, Optional
 
+from ga4gh.vrsatile.pydantic.vrs_models import RelativeCopyClass
 from gene.query import QueryHandler as GeneQueryHandler
 from ga4gh.vrs.extras.translator import Translator
-from ga4gh.vrsatile.pydantic.vrs_models import RelativeCopyClass
-from cool_seq_tool.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
+from uta_tools.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
     MANETranscript
 
+from variation.schemas.classification_response_schema import \
+    Classification, ClassificationType
+from variation.schemas.normalize_response_schema\
+    import HGVSDupDelMode as HGVSDupDelModeEnum
 from variation.schemas.app_schemas import Endpoint
+from variation.schemas.token_response_schema import Token
+from variation.validators.validator import Validator
 from variation.schemas.token_response_schema import GeneMatchToken
 from variation.tokenizers import GeneSymbol
-from variation.schemas.classification_response_schema import Classification
-from variation.schemas.normalize_response_schema\
-    import HGVSDupDelMode as HGVSDupDelModeEnum
+from variation.tokenizers.caches import AminoAcidCache
 from variation.vrs_representation import VRSRepresentation
-from .validator import Validator
 from .protein_base import ProteinBase
 
 logger = logging.getLogger("variation")
 logger.setLevel(logging.DEBUG)
 
 
-class PolypeptideSequenceVariationBase(Validator):
-    """The Polypeptide Sequence Variation Validator Base class."""
+class ProteinDeletion(Validator):
+    """The Protein Deletion Validator class."""
 
     def __init__(self, seq_repo_access: SeqRepoAccess,
                  transcript_mappings: TranscriptMappings,
                  gene_symbol: GeneSymbol,
                  mane_transcript: MANETranscript,
                  uta: UTADatabase, tlr: Translator,
-                 gene_normalizer: GeneQueryHandler, vrs: VRSRepresentation) -> None:
+                 gene_normalizer: GeneQueryHandler, vrs: VRSRepresentation,
+                 amino_acid_cache: AminoAcidCache) \
+            -> None:
         """Initialize the validator.
 
         :param SeqRepoAccess seq_repo_access: Access to SeqRepo data
         :param TranscriptMappings transcript_mappings: Access to transcript
             mappings
         :param GeneSymbol gene_symbol: Gene symbol tokenizer
         :param MANETranscript mane_transcript: Access MANE Transcript
             information
         :param UTADatabase uta: Access to UTA queries
         :param Translator tlr: Class for translating nomenclatures to and from VRS
         :param GeneQueryHandler gene_normalizer: Access to gene-normalizer
         :param VRSRepresentation vrs: Class for creating VRS objects
+        :param AminoAcidCache amino_acid_cache: Amino Acid codes and conversions
         """
         super().__init__(
             seq_repo_access, transcript_mappings, gene_symbol, mane_transcript,
             uta, tlr, gene_normalizer, vrs
         )
-        self.protein_base = ProteinBase(seq_repo_access)
+        self._amino_acid_cache = amino_acid_cache
+        self.protein_base = ProteinBase(seq_repo_access, amino_acid_cache)
         self.mane_transcript = mane_transcript
 
     async def get_transcripts(self, gene_tokens: List, classification: Classification,
                               errors: List) -> Optional[List[str]]:
         """Get transcript accessions for a given classification.
 
         :param List gene_tokens: A list of gene tokens
@@ -92,41 +99,62 @@
         :param Optional[RelativeCopyClass] relative_copy_class: The relative copy class
         :param bool do_liftover: Whether or not to liftover to GRCh38 assembly
         """
         valid_alleles = list()
         for s in classification_tokens:
             for t in transcripts:
                 errors = list()
-
                 t = self.get_accession(t, classification)
                 allele = self.vrs.to_vrs_allele(
-                    t, s.position, s.position, s.coordinate_type,
-                    s.alt_type, errors, alt=s.alt_protein)
+                    t, s.start_pos_del, s.end_pos_del, s.coordinate_type,
+                    s.alt_type, errors)
 
                 if not errors:
-                    self.protein_base.check_ref_aa(t, s.ref_protein, s.position, errors)
+                    # Check ref start/end protein matches expected
+                    self.protein_base.check_ref_aa(
+                        t, s.start_aa_del, s.start_pos_del, errors
+                    )
+
+                    if not errors and s.end_aa_del:
+                        self.protein_base.check_ref_aa(
+                            t, s.end_aa_del, s.end_pos_del, errors
+                        )
 
                 if not errors and endpoint_name == Endpoint.NORMALIZE:
                     mane = await self.mane_transcript.get_mane_transcript(
-                        t, s.position, s.coordinate_type, end_pos=s.position,
-                        ref=s.ref_protein, try_longest_compatible=True
-                    )
-
+                        t, s.start_pos_del, s.coordinate_type, end_pos=s.end_pos_del,
+                        try_longest_compatible=True)
                     self.add_mane_data(mane, mane_data_found, s.coordinate_type,
-                                       s.alt_type, s, alt=s.alt_protein)
+                                       s.alt_type, s)
 
                 self.add_validation_result(allele, valid_alleles, results,
                                            classification, s, t, gene_tokens, errors)
+
                 if is_identifier:
                     break
 
         if endpoint_name == Endpoint.NORMALIZE:
             self.add_mane_to_validation_results(mane_data_found, valid_alleles, results,
                                                 classification, gene_tokens)
 
     def get_gene_tokens(self, classification: Classification) -> List[GeneMatchToken]:
         """Return gene tokens for a classification.
 
         :param Classification classification: The classification for tokens
         :return: A list of Gene Match Tokens in the classification
         """
         return self.get_protein_gene_symbol_tokens(classification)
+
+    def variation_name(self) -> str:
+        """Return the variation name."""
+        return "protein deletion"
+
+    def is_token_instance(self, t: Token) -> bool:
+        """Check that token is Protein DelIns."""
+        return t.token_type == "ProteinDeletion"
+
+    def validates_classification_type(
+            self, classification_type: ClassificationType) -> bool:
+        """Return whether or not the classification type is
+        Protein Deletion.
+        """
+        return classification_type == ClassificationType.PROTEIN_DELETION
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/polypeptide_truncation.py` & `variation-normalizer-0.7.dev0/variation/validators/polypeptide_truncation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/protein_deletion.py` & `variation-normalizer-0.7.dev0/variation/validators/protein_insertion.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,60 +1,64 @@
-"""The module for Protein Deletion Validation."""
+"""The module for Protein Insertion Validation."""
 import logging
-from typing import Dict, List, Optional
+from typing import List, Optional, Dict
 
 from ga4gh.vrsatile.pydantic.vrs_models import RelativeCopyClass
-from gene.query import QueryHandler as GeneQueryHandler
 from ga4gh.vrs.extras.translator import Translator
-from cool_seq_tool.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
+from gene.query import QueryHandler as GeneQueryHandler
+from uta_tools.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
     MANETranscript
 
 from variation.schemas.classification_response_schema import \
-    Classification, ClassificationType
-from variation.schemas.normalize_response_schema\
-    import HGVSDupDelMode as HGVSDupDelModeEnum
-from variation.schemas.app_schemas import Endpoint
+    ClassificationType, Classification
 from variation.schemas.token_response_schema import Token
+from variation.schemas.app_schemas import Endpoint
 from variation.validators.validator import Validator
 from variation.schemas.token_response_schema import GeneMatchToken
 from variation.tokenizers import GeneSymbol
+from variation.tokenizers.caches import AminoAcidCache
+from variation.schemas.normalize_response_schema\
+    import HGVSDupDelMode as HGVSDupDelModeEnum
 from variation.vrs_representation import VRSRepresentation
 from .protein_base import ProteinBase
 
+
 logger = logging.getLogger("variation")
 logger.setLevel(logging.DEBUG)
 
 
-class ProteinDeletion(Validator):
-    """The Protein Deletion Validator class."""
+class ProteinInsertion(Validator):
+    """The Protein Insertion Validator class."""
 
-    def __init__(self, seq_repo_access: SeqRepoAccess,
-                 transcript_mappings: TranscriptMappings,
-                 gene_symbol: GeneSymbol,
-                 mane_transcript: MANETranscript,
-                 uta: UTADatabase, tlr: Translator,
-                 gene_normalizer: GeneQueryHandler, vrs: VRSRepresentation) -> None:
+    def __init__(
+        self, seq_repo_access: SeqRepoAccess, transcript_mappings: TranscriptMappings,
+        gene_symbol: GeneSymbol, mane_transcript: MANETranscript, uta: UTADatabase,
+        tlr: Translator, gene_normalizer: GeneQueryHandler,
+        vrs: VRSRepresentation, amino_acid_cache: AminoAcidCache
+    ) -> None:
         """Initialize the validator.
 
         :param SeqRepoAccess seq_repo_access: Access to SeqRepo data
         :param TranscriptMappings transcript_mappings: Access to transcript
             mappings
         :param GeneSymbol gene_symbol: Gene symbol tokenizer
         :param MANETranscript mane_transcript: Access MANE Transcript
             information
         :param UTADatabase uta: Access to UTA queries
         :param Translator tlr: Class for translating nomenclatures to and from VRS
         :param GeneQueryHandler gene_normalizer: Access to gene-normalizer
         :param VRSRepresentation vrs: Class for creating VRS objects
+        :param AminoAcidCache amino_acid_cache: Amino Acid codes and conversions
         """
         super().__init__(
             seq_repo_access, transcript_mappings, gene_symbol, mane_transcript,
             uta, tlr, gene_normalizer, vrs
         )
-        self.protein_base = ProteinBase(seq_repo_access)
+        self._amino_acid_cache = amino_acid_cache
+        self.protein_base = ProteinBase(seq_repo_access, amino_acid_cache)
         self.mane_transcript = mane_transcript
 
     async def get_transcripts(self, gene_tokens: List, classification: Classification,
                               errors: List) -> Optional[List[str]]:
         """Get transcript accessions for a given classification.
 
         :param List gene_tokens: A list of gene tokens
@@ -96,47 +100,36 @@
         """
         valid_alleles = list()
         for s in classification_tokens:
             for t in transcripts:
                 errors = list()
                 t = self.get_accession(t, classification)
                 allele = self.vrs.to_vrs_allele(
-                    t, s.start_pos_del, s.end_pos_del, s.coordinate_type,
-                    s.alt_type, errors)
+                    t, s.start_pos_flank, s.end_pos_flank,
+                    s.coordinate_type, s.alt_type, errors,
+                    alt=s.inserted_sequence
+                )
 
                 if not errors:
                     # Check ref start/end protein matches expected
                     self.protein_base.check_ref_aa(
-                        t, s.start_aa_del, s.start_pos_del, errors
+                        t, s.start_aa_flank, s.start_pos_flank, errors
                     )
 
-                    if not errors and s.end_aa_del:
+                    if not errors:
                         self.protein_base.check_ref_aa(
-                            t, s.end_aa_del, s.end_pos_del, errors
+                            t, s.end_aa_flank, s.end_pos_flank, errors
                         )
 
-                    if not errors and s.deleted_aa:
-                        try:
-                            ref = self.seqrepo_access.sr.fetch(
-                                t, s.start_pos_del - 1, s.end_pos_del
-                            )
-                        except (KeyError, ValueError) as e:
-                            errors.append(str(e))
-                        else:
-                            if ref != s.deleted_aa:
-                                errors.append(
-                                    f"Needed to find {s.deleted_aa} but found {ref}"
-                                )
-
                 if not errors and endpoint_name == Endpoint.NORMALIZE:
                     mane = await self.mane_transcript.get_mane_transcript(
-                        t, s.start_pos_del, s.coordinate_type, end_pos=s.end_pos_del,
-                        try_longest_compatible=True)
+                        t, s.start_pos_flank, s.coordinate_type,
+                        end_pos=s.end_pos_flank, try_longest_compatible=True)
                     self.add_mane_data(mane, mane_data_found, s.coordinate_type,
-                                       s.alt_type, s)
+                                       s.alt_type, s, alt=s.inserted_sequence)
 
                 self.add_validation_result(allele, valid_alleles, results,
                                            classification, s, t, gene_tokens, errors)
 
                 if is_identifier:
                     break
 
@@ -150,19 +143,20 @@
         :param Classification classification: The classification for tokens
         :return: A list of Gene Match Tokens in the classification
         """
         return self.get_protein_gene_symbol_tokens(classification)
 
     def variation_name(self) -> str:
         """Return the variation name."""
-        return "protein deletion"
+        return "protein insertion"
 
     def is_token_instance(self, t: Token) -> bool:
-        """Check that token is Protein DelIns."""
-        return t.token_type == "ProteinDeletion"
+        """Check that token is Protein Insertion."""
+        return t.token_type == "ProteinInsertion"
 
     def validates_classification_type(
-            self, classification_type: ClassificationType) -> bool:
+        self, classification_type: ClassificationType
+    ) -> bool:
         """Return whether or not the classification type is
-        Protein Deletion.
+        Protein Insertion.
         """
-        return classification_type == ClassificationType.PROTEIN_DELETION
+        return classification_type == ClassificationType.PROTEIN_INSERTION
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/protein_delins.py` & `variation-normalizer-0.7.dev0/variation/validators/protein_delins.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,24 +1,25 @@
 """The module for Protein DelIns Validation."""
 from typing import List, Optional, Dict
 import logging
 
 from ga4gh.vrsatile.pydantic.vrs_models import RelativeCopyClass
 from ga4gh.vrs.extras.translator import Translator
 from gene.query import QueryHandler as GeneQueryHandler
-from cool_seq_tool.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
+from uta_tools.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
     MANETranscript
 
 from variation.schemas.classification_response_schema import \
     ClassificationType, Classification
 from variation.schemas.app_schemas import Endpoint
 from variation.schemas.token_response_schema import Token
 from variation.validators.validator import Validator
 from variation.schemas.token_response_schema import GeneMatchToken
 from variation.tokenizers import GeneSymbol
+from variation.tokenizers.caches import AminoAcidCache
 from variation.schemas.normalize_response_schema\
     import HGVSDupDelMode as HGVSDupDelModeEnum
 from variation.vrs_representation import VRSRepresentation
 from .protein_base import ProteinBase
 
 logger = logging.getLogger("variation")
 logger.setLevel(logging.DEBUG)
@@ -28,33 +29,37 @@
     """The Protein DelIns Validator class."""
 
     def __init__(self, seq_repo_access: SeqRepoAccess,
                  transcript_mappings: TranscriptMappings,
                  gene_symbol: GeneSymbol,
                  mane_transcript: MANETranscript,
                  uta: UTADatabase, tlr: Translator,
-                 gene_normalizer: GeneQueryHandler, vrs: VRSRepresentation) -> None:
+                 gene_normalizer: GeneQueryHandler, vrs: VRSRepresentation,
+                 amino_acid_cache: AminoAcidCache) \
+            -> None:
         """Initialize the validator.
 
         :param SeqRepoAccess seq_repo_access: Access to SeqRepo data
         :param TranscriptMappings transcript_mappings: Access to transcript
             mappings
         :param GeneSymbol gene_symbol: Gene symbol tokenizer
         :param MANETranscript mane_transcript: Access MANE Transcript
             information
         :param UTADatabase uta: Access to UTA queries
         :param Translator tlr: Class for translating nomenclatures to and from VRS
         :param GeneQueryHandler gene_normalizer: Access to gene-normalizer
         :param VRSRepresentation vrs: Class for creating VRS objects
+        :param AminoAcidCache amino_acid_cache: Amino Acid codes and conversions
         """
         super().__init__(
             seq_repo_access, transcript_mappings, gene_symbol, mane_transcript,
             uta, tlr, gene_normalizer, vrs
         )
-        self.protein_base = ProteinBase(seq_repo_access)
+        self._amino_acid_cache = amino_acid_cache
+        self.protein_base = ProteinBase(seq_repo_access, amino_acid_cache)
         self.mane_transcript = mane_transcript
 
     async def get_transcripts(self, gene_tokens: List, classification: Classification,
                               errors: List) -> Optional[List[str]]:
         """Get transcript accessions for a given classification.
 
         :param List gene_tokens: A list of gene tokens
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/protein_insertion.py` & `variation-normalizer-0.7.dev0/variation/validators/polypeptide_sequence_variation_base.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,61 +1,62 @@
-"""The module for Protein Insertion Validation."""
+"""The module for Polypeptide Sequence Variation Validation."""
 import logging
 from typing import List, Optional, Dict
 
-from ga4gh.vrsatile.pydantic.vrs_models import RelativeCopyClass
-from ga4gh.vrs.extras.translator import Translator
 from gene.query import QueryHandler as GeneQueryHandler
-from cool_seq_tool.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
+from ga4gh.vrs.extras.translator import Translator
+from ga4gh.vrsatile.pydantic.vrs_models import RelativeCopyClass
+from uta_tools.data_sources import SeqRepoAccess, TranscriptMappings, UTADatabase, \
     MANETranscript
 
-from variation.schemas.classification_response_schema import \
-    ClassificationType, Classification
-from variation.schemas.token_response_schema import Token
 from variation.schemas.app_schemas import Endpoint
-from variation.validators.validator import Validator
 from variation.schemas.token_response_schema import GeneMatchToken
 from variation.tokenizers import GeneSymbol
+from variation.tokenizers.caches import AminoAcidCache
+from variation.schemas.classification_response_schema import Classification
 from variation.schemas.normalize_response_schema\
     import HGVSDupDelMode as HGVSDupDelModeEnum
 from variation.vrs_representation import VRSRepresentation
+from .validator import Validator
 from .protein_base import ProteinBase
 
-
 logger = logging.getLogger("variation")
 logger.setLevel(logging.DEBUG)
 
 
-class ProteinInsertion(Validator):
-    """The Protein Insertion Validator class."""
+class PolypeptideSequenceVariationBase(Validator):
+    """The Polypeptide Sequence Variation Validator Base class."""
 
-    def __init__(
-        self, seq_repo_access: SeqRepoAccess, transcript_mappings: TranscriptMappings,
-        gene_symbol: GeneSymbol, mane_transcript: MANETranscript, uta: UTADatabase,
-        tlr: Translator, gene_normalizer: GeneQueryHandler,
-        vrs: VRSRepresentation
-    ) -> None:
+    def __init__(self, seq_repo_access: SeqRepoAccess,
+                 transcript_mappings: TranscriptMappings,
+                 gene_symbol: GeneSymbol,
+                 mane_transcript: MANETranscript,
+                 uta: UTADatabase, tlr: Translator,
+                 gene_normalizer: GeneQueryHandler, vrs: VRSRepresentation,
+                 amino_acid_cache: AminoAcidCache) -> None:
         """Initialize the validator.
 
         :param SeqRepoAccess seq_repo_access: Access to SeqRepo data
         :param TranscriptMappings transcript_mappings: Access to transcript
             mappings
         :param GeneSymbol gene_symbol: Gene symbol tokenizer
         :param MANETranscript mane_transcript: Access MANE Transcript
             information
         :param UTADatabase uta: Access to UTA queries
         :param Translator tlr: Class for translating nomenclatures to and from VRS
         :param GeneQueryHandler gene_normalizer: Access to gene-normalizer
         :param VRSRepresentation vrs: Class for creating VRS objects
+        :param AminoAcidCache amino_acid_cache: Amino Acid codes and conversions
         """
         super().__init__(
             seq_repo_access, transcript_mappings, gene_symbol, mane_transcript,
             uta, tlr, gene_normalizer, vrs
         )
-        self.protein_base = ProteinBase(seq_repo_access)
+        self._amino_acid_cache = amino_acid_cache
+        self.protein_base = ProteinBase(seq_repo_access, amino_acid_cache)
         self.mane_transcript = mane_transcript
 
     async def get_transcripts(self, gene_tokens: List, classification: Classification,
                               errors: List) -> Optional[List[str]]:
         """Get transcript accessions for a given classification.
 
         :param List gene_tokens: A list of gene tokens
@@ -95,65 +96,41 @@
         :param Optional[RelativeCopyClass] relative_copy_class: The relative copy class
         :param bool do_liftover: Whether or not to liftover to GRCh38 assembly
         """
         valid_alleles = list()
         for s in classification_tokens:
             for t in transcripts:
                 errors = list()
+
                 t = self.get_accession(t, classification)
                 allele = self.vrs.to_vrs_allele(
-                    t, s.start_pos_flank, s.end_pos_flank,
-                    s.coordinate_type, s.alt_type, errors,
-                    alt=s.inserted_sequence
-                )
+                    t, s.position, s.position, s.coordinate_type,
+                    s.alt_type, errors, alt=s.alt_protein)
 
                 if not errors:
-                    # Check ref start/end protein matches expected
-                    self.protein_base.check_ref_aa(
-                        t, s.start_aa_flank, s.start_pos_flank, errors
-                    )
-
-                    if not errors:
-                        self.protein_base.check_ref_aa(
-                            t, s.end_aa_flank, s.end_pos_flank, errors
-                        )
+                    self.protein_base.check_ref_aa(t, s.ref_protein, s.position, errors)
 
                 if not errors and endpoint_name == Endpoint.NORMALIZE:
                     mane = await self.mane_transcript.get_mane_transcript(
-                        t, s.start_pos_flank, s.coordinate_type,
-                        end_pos=s.end_pos_flank, try_longest_compatible=True)
+                        t, s.position, s.coordinate_type, end_pos=s.position,
+                        ref=s.ref_protein, try_longest_compatible=True
+                    )
+
                     self.add_mane_data(mane, mane_data_found, s.coordinate_type,
-                                       s.alt_type, s, alt=s.inserted_sequence)
+                                       s.alt_type, s, alt=s.alt_protein)
 
                 self.add_validation_result(allele, valid_alleles, results,
                                            classification, s, t, gene_tokens, errors)
-
                 if is_identifier:
                     break
 
         if endpoint_name == Endpoint.NORMALIZE:
             self.add_mane_to_validation_results(mane_data_found, valid_alleles, results,
                                                 classification, gene_tokens)
 
     def get_gene_tokens(self, classification: Classification) -> List[GeneMatchToken]:
         """Return gene tokens for a classification.
 
         :param Classification classification: The classification for tokens
         :return: A list of Gene Match Tokens in the classification
         """
         return self.get_protein_gene_symbol_tokens(classification)
-
-    def variation_name(self) -> str:
-        """Return the variation name."""
-        return "protein insertion"
-
-    def is_token_instance(self, t: Token) -> bool:
-        """Check that token is Protein Insertion."""
-        return t.token_type == "ProteinInsertion"
-
-    def validates_classification_type(
-        self, classification_type: ClassificationType
-    ) -> bool:
-        """Return whether or not the classification type is
-        Protein Insertion.
-        """
-        return classification_type == ClassificationType.PROTEIN_INSERTION
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/protein_substitution.py` & `variation-normalizer-0.7.dev0/variation/validators/protein_substitution.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/silent_mutation.py` & `variation-normalizer-0.7.dev0/variation/validators/silent_mutation.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/single_nucleotide_variation_base.py` & `variation-normalizer-0.7.dev0/variation/validators/single_nucleotide_variation_base.py`

 * *Files identical despite different names*

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/validate.py` & `variation-normalizer-0.7.dev0/variation/validators/validate.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,23 +1,24 @@
 """Module for Validation."""
 from typing import List, Optional
 
 from ga4gh.vrsatile.pydantic.vrs_models import RelativeCopyClass
 from ga4gh.vrs.extras.translator import Translator
 from gene.query import QueryHandler as GeneQueryHandler
-from cool_seq_tool.data_sources import TranscriptMappings, SeqRepoAccess, UTADatabase, \
+from uta_tools.data_sources import TranscriptMappings, SeqRepoAccess, UTADatabase, \
     MANETranscript
 
 from variation.schemas.normalize_response_schema\
     import HGVSDupDelMode as HGVSDupDelModeEnum
 from variation.vrs_representation import VRSRepresentation
 from variation.schemas.app_schemas import Endpoint
 from variation.schemas.validation_response_schema import ValidationSummary
 from variation.schemas.classification_response_schema import Classification
 from variation.tokenizers import GeneSymbol
+from variation.tokenizers.caches import AminoAcidCache
 from .protein_substitution import ProteinSubstitution
 from .polypeptide_truncation import PolypeptideTruncation
 from .silent_mutation import SilentMutation
 from .coding_dna_substitution import CodingDNASubstitution
 from .coding_dna_silent_mutation import CodingDNASilentMutation
 from .genomic_silent_mutation import GenomicSilentMutation
 from .genomic_substitution import GenomicSubstitution
@@ -40,47 +41,52 @@
     """The validation class."""
 
     def __init__(self, seqrepo_access: SeqRepoAccess,
                  transcript_mappings: TranscriptMappings,
                  gene_symbol: GeneSymbol,
                  mane_transcript: MANETranscript,
                  uta: UTADatabase, tlr: Translator,
+                 amino_acid_cache: AminoAcidCache,
                  gene_normalizer: GeneQueryHandler, vrs: VRSRepresentation) -> None:
         """Initialize the validate class.
 
         :param SeqRepoAccess seqrepo_access: Access to SeqRepo data
         :param TranscriptMappings transcript_mappings: Access to transcript
             mappings
         :param GeneSymbol gene_symbol: Gene symbol tokenizer
         :param MANETranscript mane_transcript: Access MANE Transcript
             information
         :param UTADatabase uta: Access to UTA queries
         :param Translator tlr: Class for translating nomenclatures to and from VRS
+        :param AminoAcidCache amino_acid_cache: Amino Acid codes and conversions
         :param GeneQueryHandler gene_normalizer: Access to gene-normalizer
         :param VRSRepresentation vrs: Class for representing VRS objects
+        :param amino_acid_cache: Amino Acid codes and conversions
         """
         params = [
             seqrepo_access, transcript_mappings, gene_symbol,
             mane_transcript, uta, tlr, gene_normalizer, vrs
         ]
+        protein_params = params[:]
+        protein_params.append(amino_acid_cache)
         self.validators = [
-            ProteinSubstitution(*params),
-            PolypeptideTruncation(*params),
-            SilentMutation(*params),
+            ProteinSubstitution(*protein_params),
+            PolypeptideTruncation(*protein_params),
+            SilentMutation(*protein_params),
             CodingDNASubstitution(*params),
             GenomicSubstitution(*params),
             CodingDNASilentMutation(*params),
             GenomicSilentMutation(*params),
-            ProteinDelIns(*params),
+            ProteinDelIns(*protein_params),
             CodingDNADelIns(*params),
             GenomicDelIns(*params),
-            ProteinDeletion(*params),
+            ProteinDeletion(*protein_params),
             CodingDNADeletion(*params),
             GenomicDeletion(*params),
-            ProteinInsertion(*params),
+            ProteinInsertion(*protein_params),
             CodingDNAInsertion(*params),
             GenomicInsertion(*params),
             GenomicDeletionRange(*params),
             GenomicUncertainDeletion(*params),
             GenomicDuplication(*params),
             Amplification(*params)
         ]
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/validators/validator.py` & `variation-normalizer-0.7.dev0/variation/validators/validator.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,16 +3,16 @@
 from typing import List, Optional, Dict, Tuple
 from abc import ABC, abstractmethod
 import logging
 
 from ga4gh.vrsatile.pydantic.vrs_models import RelativeCopyClass
 from gene.query import QueryHandler as GeneQueryHandler
 from ga4gh.vrs.extras.translator import Translator
-from cool_seq_tool.data_sources import SeqRepoAccess, TranscriptMappings, \
-    MANETranscript, UTADatabase
+from uta_tools.data_sources import SeqRepoAccess, TranscriptMappings, MANETranscript, \
+    UTADatabase
 
 from variation.schemas.classification_response_schema import Classification, \
     ClassificationType
 from variation.schemas.app_schemas import Endpoint
 from variation.schemas.token_response_schema import GeneMatchToken, Token, \
     GenomicSubstitutionToken
 from variation.schemas.validation_response_schema import ValidationResult
@@ -662,17 +662,17 @@
 
     def _is_grch38_assembly(self, t: str) -> bool:
         """Return whether or not accession is GRCh38 assembly.
 
         :param str t: Accession
         :return: `True` if accession is GRCh38 assembly. `False` otherwise
         """
-        translated_identifiers, _ = self.seqrepo_access.translate_identifier(t)
+        translated_identifiers, w = self.seqrepo_access.translate_identifier(t)
         if translated_identifiers:
-            return bool([a for a in translated_identifiers if a.startswith("GRCh38")])
+            return "GRCh38" in ([a for a in translated_identifiers if a.startswith("GRCh")] or [None])[0]  # noqa: E501
         return False
 
     async def add_genomic_liftover_to_results(
         self, grch38: Dict, errors: List, alt: str, valid_alleles: List, results: List,
         classification: Classification, s: Token, t: str, gene_tokens: List
     ) -> None:
         """Add genomic liftover data to results if genomic GRCh38 variation found
```

### Comparing `variation-normalizer-0.7.0.dev4/variation/vrs_representation.py` & `variation-normalizer-0.7.dev0/variation/vrs_representation.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,26 +1,29 @@
 """Module for generating VRS objects"""
 from typing import List, Optional, Tuple, Union, Dict
 
 from ga4gh.vrsatile.pydantic.vrs_models import CURIE, RelativeCopyClass
+from ga4gh.vrs.dataproxy import SeqRepoDataProxy
 from ga4gh.vrs import models, normalize
 from ga4gh.core import ga4gh_identify
-from cool_seq_tool.data_sources import SeqRepoAccess
+from uta_tools.data_sources import SeqRepoAccess
 from bioutils.accessions import coerce_namespace
 
 
 class VRSRepresentation:
     """Class for representing VRS objects"""
 
-    def __init__(self, seqrepo_access: SeqRepoAccess) -> None:
+    def __init__(self, dp: SeqRepoDataProxy, seqrepo_access: SeqRepoAccess) -> None:
         """Initialize the VRSRepresentation class
 
-        :param SeqRepoAccess seqrepo_access: Access to SeqRepo
+        :param SeqRepoAccess seqrepo_access: Access to SeqRepo via UTA Tools
+        :param SeqRepoDataProxy dp: Access to SeqRepo via VRS Python
         """
         self.seqrepo_access = seqrepo_access
+        self.dp = dp
 
     @staticmethod
     def get_start_end(
             coordinate: str, start: int, end: int, cds_start: int,
             errors: List) -> Optional[Tuple[int, int]]:
         """Get start and end coordinates.
 
@@ -140,15 +143,15 @@
             errors.append(f"Unable to get sequence location: {e}")
             return None
         allele = models.Allele(location=location, state=sstate, type="Allele")
         # Ambiguous regions do not get normalized
         if alt_type not in ["uncertain_deletion", "uncertain_duplication",
                             "duplication_range", "deletion_range"]:
             try:
-                allele = normalize(allele, self.seqrepo_access)
+                allele = normalize(allele, self.dp)
             except (KeyError, AttributeError) as e:
                 errors.append(f"vrs-python unable to normalize allele: {e}")
                 return None
 
         if not allele:
             errors.append("Unable to get allele")
             return None
```

### Comparing `variation-normalizer-0.7.0.dev4/variation_normalizer.egg-info/PKG-INFO` & `variation-normalizer-0.7.dev0/variation_normalizer.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,16 +1,15 @@
 Metadata-Version: 2.1
 Name: variation-normalizer
-Version: 0.7.0.dev4
+Version: 0.7.dev0
 Summary: VICC normalization routine for variations
 Home-page: https://github.com/cancervariants/variation-normalization
 Author: VICC
 Author-email: help@cancervariants.org
 License: MIT
-Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Scientific/Engineering :: Bio-Informatics
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
@@ -48,15 +47,15 @@
 
 We are working towards adding more types of variations, coordinates, and representations.
 
 ### Endpoints
 
 The `/to_vrs` endpoint returns a list of validated VRS [Variations](https://vrs.ga4gh.org/en/1.2.0/terms_and_model.html#variation).
 
-The `/normalize` endpoint returns a [Variation Descriptor](https://vrsatile.readthedocs.io/en/latest/value_object_descriptor/vod_index.html#variation-descriptor) containing the MANE Transcript, if one is found. If a genomic query is not given a gene, `normalize` will return its GRCh38 representation. Variation Normalizer relies on [**C**ommon **O**perations **O**n **L**ots-of **Seq**uences Tool (cool-seq-tool)](https://github.com/GenomicMedLab/cool-seq-tool) for retrieving MANE Transcript data. More information on the transcript selection algorithm can be found [here](https://github.com/GenomicMedLab/cool-seq-tool/blob/main/docs/TranscriptSelectionPriority.md).
+The `/normalize` endpoint returns a [Variation Descriptor](https://vrsatile.readthedocs.io/en/latest/value_object_descriptor/vod_index.html#variation-descriptor) containing the MANE Transcript, if one is found. If a genomic query is not given a gene, `normalize` will return its GRCh38 representation. Variation Normalizer relies on [UTA Tools](https://github.com/GenomicMedLab/uta-tools) for retrieving MANE Transcript data. More information on the transcript selection algorithm can be found [here](https://github.com/GenomicMedLab/uta-tools/blob/main/docs/TranscriptSelectionPriority.md).
 
 ## Developer Instructions
 
 Clone the repo:
 ```
 git clone https://github.com/cancervariants/variation-normalization.git
 cd variation-normalization
@@ -107,18 +106,16 @@
 You will want to do the following:\
 (*Might not be ._fkuefgd, so replace with your error message path*)
 ```console
 sudo mv /usr/local/share/seqrepo/2021-01-29._fkuefgd /usr/local/share/seqrepo/2021-01-29
 exit
 ```
 
-Use the `SEQREPO_ROOT_DIR` environment variable to set the path of an already existing SeqRepo directory. The default is `/usr/local/share/seqrepo/latest`.
-
 #### UTA
-Variation Normalizer also uses [**C**ommon **O**perations **O**n **L**ots-of **Seq**uences Tool (cool-seq-tool)](https://github.com/GenomicMedLab/cool-seq-tool) which uses [UTA](https://github.com/biocommons/uta) as the underlying PostgreSQL database.
+Variation Normalizer also uses [UTA Tools](https://github.com/GenomicMedLab/uta-tools) which uses [UTA](https://github.com/biocommons/uta) as the underlying PostgreSQL database.
 
 _The following commands will likely need modification appropriate for the installation environment._
 1. Install [PostgreSQL](https://www.postgresql.org/)
 2. Create user and database.
 
     ```
     $ createuser -U postgres uta_admin
@@ -172,9 +169,7 @@
 ```
 
 ### Testing
 From the _root_ directory of the repository:
 ```
 pytest tests/
 ```
-
-
```

### Comparing `variation-normalizer-0.7.0.dev4/variation_normalizer.egg-info/SOURCES.txt` & `variation-normalizer-0.7.dev0/variation_normalizer.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -133,14 +133,16 @@
 variation/classifiers/protein_classifier.py
 variation/classifiers/protein_deletion_classifier.py
 variation/classifiers/protein_delins_classifier.py
 variation/classifiers/protein_insertion_classifier.py
 variation/classifiers/protein_termination_classifier.py
 variation/classifiers/set_based_classifier.py
 variation/classifiers/silent_mutation.py
+variation/data/amino_acids.csv
+variation/data/transcript_mapping.tsv
 variation/data_sources/__init__.py
 variation/data_sources/codon_table.py
 variation/schemas/__init__.py
 variation/schemas/app_schemas.py
 variation/schemas/classification_response_schema.py
 variation/schemas/hgvs_to_copy_number_schema.py
 variation/schemas/normalize_response_schema.py
@@ -184,14 +186,15 @@
 variation/tokenizers/reference_sequence.py
 variation/tokenizers/silent_mutation.py
 variation/tokenizers/single_nucleotide_variation_base.py
 variation/tokenizers/tokenize.py
 variation/tokenizers/tokenize_base.py
 variation/tokenizers/tokenizer.py
 variation/tokenizers/caches/__init__.py
+variation/tokenizers/caches/amino_acid_cache.py
 variation/tokenizers/caches/nucleotide_cache.py
 variation/translators/__init__.py
 variation/translators/amplification.py
 variation/translators/coding_dna_deletion.py
 variation/translators/coding_dna_delins.py
 variation/translators/coding_dna_insertion.py
 variation/translators/coding_dna_silent_mutation.py
```

