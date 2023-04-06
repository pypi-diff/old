# Comparing `tmp/learnMSA-1.1.1.tar.gz` & `tmp/learnMSA-1.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "learnMSA-1.1.1.tar", last modified: Wed Feb  1 15:23:18 2023, max compression
+gzip compressed data, was "learnMSA-1.1.2.tar", last modified: Thu Apr  6 07:59:57 2023, max compression
```

## Comparing `learnMSA-1.1.1.tar` & `learnMSA-1.1.2.tar`

### file list

```diff
@@ -1,290 +1,291 @@
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.462408 learnMSA-1.1.1/
--rw-r--r--   0 jovyan   (17731) root         (0)      242 2023-02-01 15:23:18.462172 learnMSA-1.1.1/PKG-INFO
--rw-r--r--   0 jovyan   (17731) root         (0)     3169 2023-01-16 08:38:43.000000 learnMSA-1.1.1/README.md
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.160844 learnMSA-1.1.1/learnMSA/
--rw-r--r--   0 jovyan   (17731) root         (0)       33 2023-01-12 09:31:05.000000 learnMSA-1.1.1/learnMSA/__init__.py
--rw-r--r--   0 jovyan   (17731) root         (0)       21 2023-02-01 15:20:22.000000 learnMSA-1.1.1/learnMSA/_version.py
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.188204 learnMSA-1.1.1/learnMSA/msa_hmm/
--rw-r--r--   0 jovyan   (17731) root         (0)    48746 2023-01-30 14:51:30.000000 learnMSA-1.1.1/learnMSA/msa_hmm/Align.py
--rw-r--r--   0 jovyan   (17731) root         (0)    24031 2023-01-26 10:49:20.000000 learnMSA-1.1.1/learnMSA/msa_hmm/AncProbsLayer.py
--rw-r--r--   0 jovyan   (17731) root         (0)     3555 2023-01-30 14:50:51.000000 learnMSA-1.1.1/learnMSA/msa_hmm/Configuration.py
--rw-r--r--   0 jovyan   (17731) root         (0)     8070 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/DirichletMixture.py
--rw-r--r--   0 jovyan   (17731) root         (0)     6546 2023-01-27 14:42:41.000000 learnMSA-1.1.1/learnMSA/msa_hmm/Emitter.py
--rw-r--r--   0 jovyan   (17731) root         (0)    10866 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/Fasta.py
--rw-r--r--   0 jovyan   (17731) root         (0)     5819 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/Initializers.py
--rw-r--r--   0 jovyan   (17731) root         (0)     7143 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/MsaHmmCell.py
--rw-r--r--   0 jovyan   (17731) root         (0)     3724 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/MsaHmmLayer.py
--rw-r--r--   0 jovyan   (17731) root         (0)     8134 2023-01-16 09:02:45.000000 learnMSA-1.1.1/learnMSA/msa_hmm/Priors.py
--rw-r--r--   0 jovyan   (17731) root         (0)     9873 2023-01-27 12:09:23.000000 learnMSA-1.1.1/learnMSA/msa_hmm/Training.py
--rw-r--r--   0 jovyan   (17731) root         (0)    28382 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/Transitioner.py
--rw-r--r--   0 jovyan   (17731) root         (0)     1119 2023-01-12 09:37:48.000000 learnMSA-1.1.1/learnMSA/msa_hmm/Utility.py
--rw-r--r--   0 jovyan   (17731) root         (0)    14028 2023-01-31 15:32:41.000000 learnMSA-1.1.1/learnMSA/msa_hmm/Visualize.py
--rw-r--r--   0 jovyan   (17731) root         (0)     7844 2023-01-19 09:12:19.000000 learnMSA-1.1.1/learnMSA/msa_hmm/Viterbi.py
--rw-r--r--   0 jovyan   (17731) root         (0)      825 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/__init__.py
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.135774 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.193176 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    53002 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1434 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.198841 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)   518353 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1444 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.204229 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    33749 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      818 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.209407 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    66005 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      828 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.214452 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    35917 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1627 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.219424 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    68449 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1644 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.224409 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    67114 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1444 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.229482 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1745 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      795 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.236644 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1997 2023-01-12 09:32:03.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.241208 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     3913 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1598 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.245221 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     4441 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1609 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.249215 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     3106 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1412 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.253151 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    66005 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      828 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.256982 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)   130517 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      828 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.261123 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    68173 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1641 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.265499 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)   132961 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1644 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.269739 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)   131626 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1444 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.274031 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     9557 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      808 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.278085 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    17621 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      808 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.282126 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    11725 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1609 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.286122 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    20065 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1617 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.289923 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    18730 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1415 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.293636 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     2249 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.297560 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     3005 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.301362 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     4417 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1606 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.305122 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     5449 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1609 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.308898 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     4114 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1412 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.313110 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)   260305 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1444 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.317474 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    17621 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      808 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.321211 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    33749 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      812 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.325015 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    19789 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1610 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.328983 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    36193 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1624 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.332815 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)    34858 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1425 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.336529 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     3761 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.340282 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     6029 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.344088 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     5929 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1606 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.348004 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     8473 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1609 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.351926 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     7138 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)     1412 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.155239 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.356198 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1413 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      789 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.360311 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1529 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.364311 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1565 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.368515 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1565 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.372748 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1637 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      793 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.377049 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1413 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      789 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.381537 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1529 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.385954 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1565 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.390418 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1565 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.394692 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1637 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      793 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.399022 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1601 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      792 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.403274 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1709 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      795 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.407714 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:04.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1673 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      794 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.412022 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1853 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      800 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.416405 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1437 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      789 2022-08-16 08:25:07.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.420591 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1973 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      801 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.424990 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     2453 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.429590 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1541 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.434065 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1589 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.438339 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1589 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.442395 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1685 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      795 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.446448 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1637 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      793 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.450510 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1781 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      795 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.454667 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1733 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      795 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.458744 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/
--rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/checkpoint
--rw-r--r--   0 jovyan   (17731) root         (0)     1973 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/ckpt.data-00000-of-00001
--rw-r--r--   0 jovyan   (17731) root         (0)      801 2023-01-12 09:32:05.000000 learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/ckpt.index
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.460974 learnMSA-1.1.1/learnMSA/run/
--rw-r--r--   0 jovyan   (17731) root         (0)       41 2022-08-17 06:53:42.000000 learnMSA-1.1.1/learnMSA/run/__init__.py
--rw-r--r--   0 jovyan   (17731) root         (0)     3837 2023-02-01 14:58:01.000000 learnMSA-1.1.1/learnMSA/run/console.py
-drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-02-01 15:23:18.168066 learnMSA-1.1.1/learnMSA.egg-info/
--rw-r--r--   0 jovyan   (17731) root         (0)      242 2023-02-01 15:23:17.000000 learnMSA-1.1.1/learnMSA.egg-info/PKG-INFO
--rw-r--r--   0 jovyan   (17731) root         (0)    15554 2023-02-01 15:23:18.000000 learnMSA-1.1.1/learnMSA.egg-info/SOURCES.txt
--rw-r--r--   0 jovyan   (17731) root         (0)        1 2023-02-01 15:23:17.000000 learnMSA-1.1.1/learnMSA.egg-info/dependency_links.txt
--rw-r--r--   0 jovyan   (17731) root         (0)       51 2023-02-01 15:23:17.000000 learnMSA-1.1.1/learnMSA.egg-info/entry_points.txt
--rw-r--r--   0 jovyan   (17731) root         (0)       45 2023-02-01 15:23:17.000000 learnMSA-1.1.1/learnMSA.egg-info/requires.txt
--rw-r--r--   0 jovyan   (17731) root         (0)        9 2023-02-01 15:23:17.000000 learnMSA-1.1.1/learnMSA.egg-info/top_level.txt
--rw-r--r--   0 jovyan   (17731) root         (0)       80 2022-08-09 12:49:25.000000 learnMSA-1.1.1/pyproject.toml
--rw-r--r--   0 jovyan   (17731) root         (0)       38 2023-02-01 15:23:18.462747 learnMSA-1.1.1/setup.cfg
--rw-r--r--   0 jovyan   (17731) root         (0)     1015 2023-02-01 15:12:42.000000 learnMSA-1.1.1/setup.py
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.279234 learnMSA-1.1.2/
+-rw-r--r--   0 jovyan   (17731) root         (0)      242 2023-04-06 07:59:57.278904 learnMSA-1.1.2/PKG-INFO
+-rw-r--r--   0 jovyan   (17731) root         (0)     2987 2023-04-06 07:56:29.000000 learnMSA-1.1.2/README.md
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.922365 learnMSA-1.1.2/learnMSA/
+-rw-r--r--   0 jovyan   (17731) root         (0)       33 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/__init__.py
+-rw-r--r--   0 jovyan   (17731) root         (0)       21 2023-04-06 07:57:56.000000 learnMSA-1.1.2/learnMSA/_version.py
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.950966 learnMSA-1.1.2/learnMSA/msa_hmm/
+-rw-r--r--   0 jovyan   (17731) root         (0)    33748 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/Align.py
+-rw-r--r--   0 jovyan   (17731) root         (0)    28583 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/AlignmentModel.py
+-rw-r--r--   0 jovyan   (17731) root         (0)    25907 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/AncProbsLayer.py
+-rw-r--r--   0 jovyan   (17731) root         (0)     3674 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/Configuration.py
+-rw-r--r--   0 jovyan   (17731) root         (0)     7999 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/DirichletMixture.py
+-rw-r--r--   0 jovyan   (17731) root         (0)     7173 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/Emitter.py
+-rw-r--r--   0 jovyan   (17731) root         (0)    10866 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/Fasta.py
+-rw-r--r--   0 jovyan   (17731) root         (0)     6065 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/Initializers.py
+-rw-r--r--   0 jovyan   (17731) root         (0)     7835 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/MsaHmmCell.py
+-rw-r--r--   0 jovyan   (17731) root         (0)     5289 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/MsaHmmLayer.py
+-rw-r--r--   0 jovyan   (17731) root         (0)     9183 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/Priors.py
+-rw-r--r--   0 jovyan   (17731) root         (0)     9872 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/Training.py
+-rw-r--r--   0 jovyan   (17731) root         (0)    29732 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/Transitioner.py
+-rw-r--r--   0 jovyan   (17731) root         (0)     1119 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/Utility.py
+-rw-r--r--   0 jovyan   (17731) root         (0)    13806 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/Visualize.py
+-rw-r--r--   0 jovyan   (17731) root         (0)     7844 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/Viterbi.py
+-rw-r--r--   0 jovyan   (17731) root         (0)      839 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/__init__.py
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.903710 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.955975 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    53002 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1434 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.961699 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)   518353 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1444 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.967715 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    33749 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      818 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.972623 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    66005 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      828 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.977530 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    35917 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1627 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.982333 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    68449 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1644 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.987319 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    67114 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1444 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.992334 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1745 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      795 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.997180 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1997 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.002153 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     3913 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1598 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.007200 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     4441 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1609 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.012082 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     3106 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1412 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.017093 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    66005 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      828 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.022095 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)   130517 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      828 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.027179 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    68173 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1641 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.032376 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)   132961 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1644 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.037327 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)   131626 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1444 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.042249 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     9557 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      808 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.047126 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    17621 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      808 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.051986 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    11725 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1609 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.056955 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    20065 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1617 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.061797 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    18730 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1415 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.066709 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     2249 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.071599 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     3005 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.076414 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     4417 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1606 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.081247 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     5449 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1609 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.086187 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     4114 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1412 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.091542 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)   260305 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1444 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.096840 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    17621 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      808 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.101826 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    33749 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      812 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.106608 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    19789 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1610 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.111564 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    36193 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1624 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.116511 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)    34858 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1425 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.121325 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     3761 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.126154 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     6029 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.131341 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     5929 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1606 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.136353 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     8473 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1609 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.140425 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     7138 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)     1412 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.917252 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.144655 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1413 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      789 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.148941 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1529 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.153527 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1565 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.158614 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1565 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.163781 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1637 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      793 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.169004 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1413 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      789 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.174120 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1529 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.179368 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1565 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.184731 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1565 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.189847 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1637 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      793 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.195004 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1601 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      792 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.200257 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1709 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      795 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.205407 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1673 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      794 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.210561 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1853 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      800 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.215789 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1437 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      789 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.220887 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1973 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      801 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.226276 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     2453 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      805 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.232624 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1541 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.239683 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1589 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.245362 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1589 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      791 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.251371 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1685 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      795 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.257331 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1637 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      793 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.263304 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1781 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      795 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.269052 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1733 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      795 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.274683 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/
+-rw-r--r--   0 jovyan   (17731) root         (0)       65 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/checkpoint
+-rw-r--r--   0 jovyan   (17731) root         (0)     1973 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/ckpt.data-00000-of-00001
+-rw-r--r--   0 jovyan   (17731) root         (0)      801 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/ckpt.index
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:57.277564 learnMSA-1.1.2/learnMSA/run/
+-rw-r--r--   0 jovyan   (17731) root         (0)       41 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/run/__init__.py
+-rw-r--r--   0 jovyan   (17731) root         (0)     3837 2023-04-06 07:56:29.000000 learnMSA-1.1.2/learnMSA/run/console.py
+drwxr-xr-x   0 jovyan   (17731) root         (0)        0 2023-04-06 07:59:56.929383 learnMSA-1.1.2/learnMSA.egg-info/
+-rw-r--r--   0 jovyan   (17731) root         (0)      242 2023-04-06 07:59:56.000000 learnMSA-1.1.2/learnMSA.egg-info/PKG-INFO
+-rw-r--r--   0 jovyan   (17731) root         (0)    15589 2023-04-06 07:59:56.000000 learnMSA-1.1.2/learnMSA.egg-info/SOURCES.txt
+-rw-r--r--   0 jovyan   (17731) root         (0)        1 2023-04-06 07:59:56.000000 learnMSA-1.1.2/learnMSA.egg-info/dependency_links.txt
+-rw-r--r--   0 jovyan   (17731) root         (0)       51 2023-04-06 07:59:56.000000 learnMSA-1.1.2/learnMSA.egg-info/entry_points.txt
+-rw-r--r--   0 jovyan   (17731) root         (0)       45 2023-04-06 07:59:56.000000 learnMSA-1.1.2/learnMSA.egg-info/requires.txt
+-rw-r--r--   0 jovyan   (17731) root         (0)        9 2023-04-06 07:59:56.000000 learnMSA-1.1.2/learnMSA.egg-info/top_level.txt
+-rw-r--r--   0 jovyan   (17731) root         (0)       80 2023-04-06 07:56:29.000000 learnMSA-1.1.2/pyproject.toml
+-rw-r--r--   0 jovyan   (17731) root         (0)       38 2023-04-06 07:59:57.279583 learnMSA-1.1.2/setup.cfg
+-rw-r--r--   0 jovyan   (17731) root         (0)     1015 2023-04-06 07:56:29.000000 learnMSA-1.1.2/setup.py
```

### Comparing `learnMSA-1.1.1/README.md` & `learnMSA-1.1.2/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 *Our tool is under active development and feedback is very much appreciated.*
 
 # learnMSA: Learning and Aligning large Protein Families
 
 # Introduction
 Multiple sequence alignment formulated as a statistical machine learning problem, where an optimal profile hidden Markov model for a potentially very large family of protein sequences is searched and an alignment is decoded. We use an automatically differentiable variant of the Forward algorithm.
 
-# Installation
+# InstallationlearnM
 
 Choose according to your preference:
 
 ## Using Bioconda
   
   If you haven't done it yet, set up [Bioconda channels](https://bioconda.github.io/) first.
   
@@ -27,23 +27,17 @@
 
 ## Using pip
 
   <code>pip install learnMSA</code>
   
 ## With GPU support
 
-*Optional, but recommended for proteins longer than 100 residues. The instructions above may be sufficient if the cudnn and cudatoolkit packages are already installed on your system.*
+*Optional, but recommended for proteins longer than 100 residues.*
 
-You have to meet the [TensorFlow GPU](https://www.tensorflow.org/install/gpu) requirements. A GPU installation out of the box (including cudnn and cudatoolkit) is possible by typing:
-
-```
-conda create -n learnMSA tensorflow-gpu
-conda activate learnMSA
-pip install learnMSA
-```
+You have to meet the [TensorFlow GPU](https://www.tensorflow.org/install/gpu) requirements. The install instructions above are sufficient if the cudnn and cudatoolkit packages are installed on your system.
 
 LearnMSA will notify you whether it finds any GPUs it can use or it will fall back to CPU.
 
 ## Command line use after installing with Bioconda or pip
 
 <code>learnMSA -i INPUT_FILE -o OUTPUT_FILE</code>
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/AncProbsLayer.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/AncProbsLayer.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,17 +1,20 @@
 import tensorflow as tf
 import numpy as np
+import learnMSA.msa_hmm.Initializers as initializers
 
 """Ancestral Probability Layer
 Learn one or several rate matrices jointly with a downstream model. Amino acid sequences can be smeared towards expected amino acid distributions after
 some amount of evolutionary time has passed under a substitution model. This can help to train models on distantly related sequences.
 """
               
 def inverse_softplus(features):
-    return np.log(np.expm1(features))
+    #cast to float 64 to prevent overflow of large entries
+    features64 = features.astype(np.float64)
+    return np.log(np.expm1(features64)).astype(features.dtype)
 
 def parse_paml(lines, desired_alphabet):
     """Parses the content of a paml file.
     Returns:
         A symmetric exchangeability matrix with zero diagonal and a frequency vector.
     """
     paml_alphabet = "A R N D C Q E G H I L K M F P S T W Y V".split(" ")
@@ -125,17 +128,16 @@
                  trainable_rate_matrices=True,
                  per_matrix_rate=False,
                  matrix_rate_init=None,
                  matrix_rate_l2=0.0,
                  shared_matrix=False,
                  equilibrium_sample=False,
                  transposed=False,
-                 name="AncProbsLayer",
                  **kwargs):
-        super(AncProbsLayer, self).__init__(name=name, **kwargs)
+        super(AncProbsLayer, self).__init__(**kwargs)
         self.num_models = num_models
         self.num_rates = num_rates
         self.num_matrices = num_matrices
         self.rate_init = rate_init
         self.equilibrium_init = equilibrium_init
         self.exchangeability_init = exchangeability_init
         self.trainable_rate_matrices = trainable_rate_matrices
@@ -203,19 +205,22 @@
     
     def make_per_matrix_rate(self):
         return tf.math.softplus(self.per_matrix_rates_kernel)
 
     def call(self, inputs, rate_indices):
         """ Computes anchestral probabilities of the inputs.
         Args:
-            inputs: Input sequences. Shape: (num_model, b, L) or (num_models, b, L, s)
-            rate_indices: Indices that map each input sequences to an evolutionary times. Shape: (num_model, b)
+            inputs: Input sequences. Shape: (num_model, b, L) or (num_models, b, L, s). The latter format (non index)
+                    is only supported for raw amino acid input.
+            rate_indices: Indices that map each input sequences to an evolutionary time. Shape: (num_model, b)
         Returns:
             Ancestral probabilities. Shape: (num_model, b, L, num_matrices*s)
         """
+        rate_indices = tf.identity(rate_indices) #take care of numpy inputs
+        rate_indices.set_shape([self.num_models,None]) #resolves tf 2.12 issues
         input_indices = len(inputs.shape) == 3 
         if input_indices:
             mask = inputs < 20
             only_std_aa_inputs = inputs * tf.cast(mask, inputs.dtype)
             mask = tf.cast(mask, self.dtype)
             mask = tf.expand_dims(mask, -1)
             mask = tf.expand_dims(mask, -1)
@@ -247,14 +252,43 @@
             anc_probs += rest
             num_model, b, L = tf.unstack(tf.shape(inputs))
             anc_probs = tf.reshape(anc_probs, (num_model, b, L, self.num_matrices * 26) )
         else:
             num_model, b, L, _ = tf.unstack(tf.shape(inputs))
             anc_probs = tf.reshape(anc_probs, (num_model, b, L, self.num_matrices * 20) )
         return anc_probs
+        
+    def get_config(self):
+        config = super(AncProbsLayer, self).get_config()
+        config.update({
+             "num_models" : self.num_models,
+             "num_rates" : self.num_rates,
+             "num_matrices" : self.num_matrices,
+             "equilibrium_init" : self.equilibrium_kernel.numpy(),
+             "exchangeability_init" : self.exchangeability_kernel.numpy(),
+             "rate_init" : self.tau_kernel.numpy(),
+             "trainable_rate_matrices" : self.trainable_rate_matrices,
+             "per_matrix_rate" : self.per_matrix_rate,
+             "matrix_rate_init" : self.per_matrix_rates_kernel if self.per_matrix_rate else None,
+             "matrix_rate_l2" : self.matrix_rate_l2,
+             "shared_matrix" : self.shared_matrix,
+             "equilibrium_sample" : self.equilibrium_sample,
+             "transposed" : self.transposed
+        })
+        return config
+    
+    @classmethod
+    def from_config(cls, config):
+        #override numpy arrays with initializers
+        config["equilibrium_init"] = initializers.ConstantInitializer(config["equilibrium_init"])
+        config["exchangeability_init"] = initializers.ConstantInitializer(config["exchangeability_init"])
+        config["rate_init"] = initializers.ConstantInitializer(config["rate_init"])
+        config["matrix_rate_init"] = initializers.ConstantInitializer(config["matrix_rate_init"]) if config["matrix_rate_init"] is not None else None
+        return cls(**config)
+        
 
 # the default rate matrix ("LG")
 LG_paml = ['0.425093 \n', 
            '0.276818 0.751878 \n', 
            '0.395144 0.123954 5.076149 \n', 
            '2.489084 0.534551 0.528768 0.062556 \n', 
            '0.969894 2.807908 1.695752 0.523386 0.084808 \n',
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/Configuration.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/Configuration.py`

 * *Files 3% similar despite different names*

```diff
@@ -56,16 +56,17 @@
         "num_rate_matrices" : 1,
         "per_matrix_rate" : False,
         "matrix_rate_l2" : 0.0,
         "shared_rate_matrix" : False,
         "equilibrium_sample" : False,
         "transposed" : False,
         "encoder_initializer" : initializers.make_default_anc_probs_init(default_num_models),
-        "model_criterion" : "loglik",
+        "model_criterion" : "AIC", #AIC is slightly better than loglik on average over multiple benchmarks
         "encoder_weight_extractor" : None,
+        "experimental_evolve_upper_half" : False,
         "allow_user_keys_in_config" : False
     }
     return default
 
 def assert_config(config):
     assert "num_models" in config
     default = make_default(config["num_models"])
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/DirichletMixture.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/DirichletMixture.py`

 * *Files 2% similar despite different names*

```diff
@@ -44,17 +44,16 @@
                  alphabet_size, 
                  use_dirichlet_process=True,
                  number_of_examples=-1,
                  alpha_init = "random_normal",
                  mix_init = "random_normal",
                  background_init = None,
                  trainable=True,
-                 name="DirichletMixtureLayer",
-                 dtype = tf.float32):
-        super(DirichletMixtureLayer, self).__init__(name=name, dtype=dtype)
+                 **kwargs):
+        super(DirichletMixtureLayer, self).__init__(**kwargs)
         self.num_components = num_components
         self.alphabet_size = alphabet_size
         self.use_dirichlet_process = use_dirichlet_process
         self.number_of_examples = number_of_examples
         self.alpha_init = alpha_init
         self.mix_init = mix_init
         self.background_init = background_init
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/Emitter.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/Emitter.py`

 * *Files 15% similar despite different names*

```diff
@@ -17,18 +17,17 @@
         frozen_insertions: If true, insertions will not be trainable.
     """
     def __init__(self, 
                  emission_init = initializers.make_default_emission_init(),
                  insertion_init = initializers.make_default_insertion_init(),
                  prior = priors.AminoAcidPrior(),
                  frozen_insertions = True,
-                 dtype = tf.float32,
                  **kwargs
                  ):
-        super(ProfileHMMEmitter, self).__init__(name="ProfileHMMEmitter", dtype=dtype, **kwargs)
+        super(ProfileHMMEmitter, self).__init__(**kwargs)
         self.emission_init = [emission_init] if not hasattr(emission_init, '__iter__') else emission_init 
         self.insertion_init = [insertion_init] if not hasattr(insertion_init, '__iter__') else insertion_init 
         self.prior = prior
         self.frozen_insertions = frozen_insertions
         
     def cell_init(self, cell):
         """ Automatically called when the owner cell is created.
@@ -91,15 +90,15 @@
             padding = self.max_num_states - em_mat.shape[0]
             em_mat_pad = tf.pad(em_mat, [[0, padding], [0,0]])
             emission_matrices.append(em_mat_pad)
         B = tf.stack(emission_matrices, axis=0)
         return B
         
     def make_B_amino(self):
-        """ A variant of used for plotting the HMM. Can be overridden for more complex emissions. Per default this is equivalent to make_B
+        """ A variant of make_B used for plotting the HMM. Can be overridden for more complex emissions. Per default this is equivalent to make_B
         """
         return self.make_B()
         
     def call(self, inputs):
         """ 
         Args: 
                 inputs: Shape (k, b, s) (Shape (b, s) works as well if all models should get the same input.)
@@ -107,24 +106,40 @@
                 Shape (k, b, q)
         """
         # batch matmul of k emission matrices with the b x s input matrix 
         # with broadcasting of the inputs
         return tf.matmul(inputs, self.B_transposed)
     
     def get_prior_log_density(self):
-        return self.prior(self.B, self.length)
+        return self.prior(self.make_B(), self.length)
     
     def duplicate(self, model_indices=None):
         if model_indices is None:
             model_indices = range(len(self.emission_init))
         sub_emission_init = [tf.constant_initializer(self.emission_kernel[i].numpy()) for i in model_indices]
         sub_insertion_init = [tf.constant_initializer(self.insertion_kernel[i].numpy()) for i in model_indices]
         emitter_copy = ProfileHMMEmitter(
                              emission_init = sub_emission_init,
                              insertion_init = sub_insertion_init,
                              prior = self.prior,
                              frozen_insertions = self.frozen_insertions,
                              dtype = self.dtype) 
         return emitter_copy
     
+    def get_config(self):
+        config = super(ProfileHMMEmitter, self).get_config()
+        config.update({
+             "emission_init" : [k.numpy() for k in self.emission_kernel],
+             "insertion_init" : [k.numpy() for k in self.insertion_kernel],
+             "prior" : self.prior,
+             "frozen_insertions" : self.frozen_insertions
+        })
+        return config
+    
+    @classmethod
+    def from_config(cls, config):
+        config["emission_init"] = [initializers.ConstantInitializer(k) for k in config["emission_init"]]
+        config["insertion_init"] = [initializers.ConstantInitializer(k) for k in config["insertion_init"]]
+        return cls(**config)
+    
     def __repr__(self):
         return f"ProfileHMMEmitter(\n emission_init={self.emission_init[0]},\n insertion_init={self.insertion_init[0]},\n prior={self.prior},\n frozen_insertions={self.frozen_insertions}, )"
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/Fasta.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/Fasta.py`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/Initializers.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/Initializers.py`

 * *Files 3% similar despite different names*

```diff
@@ -7,18 +7,17 @@
 
 class EmissionInitializer(tf.keras.initializers.Initializer):
 
     def __init__(self, dist):
         self.dist = dist
 
     def __call__(self, shape, dtype=None, **kwargs):
-        assert len(shape) == 2, "EmissionInitializer only supports 2D shapes."
         assert shape[-1] == self.dist.size, f"Last dimension of shape must match the size of the initial distribution. Shape={shape} dist.size={self.dist.size}"
         dist = tf.cast(self.dist, dtype)
-        return tf.reshape(tf.tile(dist, shape[:1]), shape)
+        return tf.reshape(tf.tile(dist, tf.math.reduce_prod(shape[:-1], keepdims=True)), shape)
     
     def __repr__(self):
         return f"DefaultEmission()"
     
 class ConstantInitializer(tf.keras.initializers.Constant):
     def __repr__(self):
         if np.isscalar(self.value):
@@ -90,15 +89,22 @@
         p_exit_desired = 0.5 / (shape[0]-1)
         prob = (tf.nn.softmax(val_z) * (1-p_exit_desired))[:,self.i]
         return tf.math.log(prob)
     
     def __repr__(self):
         return f"DefaultMatchTransition({self.val[self.i]})"
     
-class RandomNormalInitializer(tf.keras.initializers.RandomNormal):
+class RandomNormalInitializer(tf.keras.initializers.Initializer):
+    def __init__(self, mean=0.0, stddev=0.05):
+        self.mean = mean
+        self.stddev = stddev
+    
+    def __call__(self, shape, dtype=None, **kwargs):
+        return tf.random.normal(shape, mean=self.mean, stddev=self.stddev, dtype=dtype if dtype != None else tf.float32)
+        
     def __repr__(self):
         return f"Norm({self.mean}, {self.stddev})"
     
 def make_default_flank_init():
     return ConstantInitializer(0.)
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/MsaHmmCell.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/MsaHmmCell.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,49 +1,51 @@
 import os
 import tensorflow as tf
 import numpy as np
 import learnMSA.msa_hmm.Emitter as emit
 import learnMSA.msa_hmm.Transitioner as trans
 
-
 class MsaHmmCell(tf.keras.layers.Layer):
     """ A general cell for (p)HMM training. It is meant to be used with the generic RNN-layer.
         It computes the likelihood of a batch of sequences, computes a prior value and provides 
         functionality (through the injected emitter and transitioner) to construct the emission- 
         and transition-matricies also used elsewhere e.g. during Viterbi.
         Based on https://github.com/mslehre/classify-seqs/blob/main/HMMCell.py.
     Args:
         length: Model length / number of match states or a list of lengths.
         emitter: An object or a list of objects following the emitter interface (see MultinomialAminoAcidEmitter).
         transitioner: An object following the transitioner interface (see ProfileHMMTransitioner).
         dtype: The datatype of the cell.
     """
     def __init__(self,
                  length, 
-                 emitter = emit.ProfileHMMEmitter(),
-                 transitioner = trans.ProfileHMMTransitioner(),
-                 dtype=tf.float32,
+                 emitter = None,
+                 transitioner = None,
                  **kwargs
                 ):
-        super(MsaHmmCell, self).__init__(name="MsaHmmCell", dtype=dtype, **kwargs)
+        super(MsaHmmCell, self).__init__(**kwargs)
+        if emitter is None:
+            emitter = emit.ProfileHMMEmitter()
+        if transitioner is None:
+            transitioner = trans.ProfileHMMTransitioner()
         self.length = [length] if not hasattr(length, '__iter__') else length 
         self.num_models = len(self.length)
         self.emitter = [emitter] if not hasattr(emitter, '__iter__') else emitter 
         self.transitioner = transitioner
         #number of emitting states, i.e. not counting flanking states and deletions
         self.num_states = [2 * length + 3 for length in self.length]  
         self.num_states_implicit = [num_states + length + 2 
                                     for num_states, length in zip(self.num_states, self.length)]
         self.max_num_states = max(self.num_states)
         self.state_size = (tf.TensorShape([self.max_num_states]), tf.TensorShape([1]))
         self.output_size = tf.TensorShape([self.max_num_states])
         for em in self.emitter:
             em.cell_init(self)
         self.transitioner.cell_init(self)
-        self.epsilon = tf.constant(1e-32, dtype)
+        self.epsilon = tf.constant(1e-32, self.dtype)
         self.reverse = False
             
             
     def build(self, input_shape):
         self.dim = input_shape[-1]
         for em in self.emitter:
             em.build(input_shape)
@@ -54,15 +56,14 @@
     def recurrent_init(self):
         self.transitioner.recurrent_init()
         for em in self.emitter:
             em.recurrent_init()
         self.log_A_dense = self.transitioner.make_log_A()
         self.log_A_dense_t = tf.transpose(self.log_A_dense, [0,2,1])
         self.init_dist = self.make_initial_distribution()
-        self.init = True
     
     
     def make_initial_distribution(self):
         """Constructs the initial state distribution which depends on the transition probabilities.
             See ProfileHMMTransitioner.
         Returns:
             A probability distribution of shape: (1, num_model, q)
@@ -78,25 +79,24 @@
         """
         em_probs = self.emitter[0](inputs)
         for em in self.emitter[1:]:
             em_probs *= em(inputs)
         return em_probs
 
     
-    def call(self, inputs, states, training=None):
+    def call(self, inputs, states, training=None, init=False):
         """ Computes one recurrent step of the Forward DP.
         """
         old_scaled_forward, old_loglik = states
         old_scaled_forward = tf.reshape(old_scaled_forward, (self.num_models, -1, self.max_num_states))
         old_loglik = tf.reshape(old_loglik, (self.num_models, -1, 1))
         inputs = tf.reshape(inputs, (self.num_models, -1, self.dim))
         E = self.emission_probs(inputs)
-        if self.init:
+        if init:
             R = old_scaled_forward
-            self.init = False
         else:
             R = self.transitioner(old_scaled_forward)
         scaled_forward = tf.multiply(E, R, name="scaled_forward")
         S = tf.reduce_sum(scaled_forward, axis=-1, keepdims=True)
         loglik = old_loglik + tf.math.log(S) 
         scaled_forward /= S 
         loglik = tf.reshape(loglik, (-1, 1))
@@ -154,8 +154,29 @@
         return subset_cell
     
     
     #configures the cell for the backward recursion
     def reverse_direction(self):
         self.transitioner.transpose()
         self.reverse = not self.reverse
+        
+    def get_config(self):
+        config = super(MsaHmmCell, self).get_config()
+        config.update({
+             "length" : self.length, 
+             "num_emitters" : len(self.emitter),
+             "transitioner" : self.transitioner
+        })
+        for i, em in enumerate(self.emitter):
+             config[f"emitter_{i}"] = em
+        return config
+    
+    @classmethod
+    def from_config(cls, config):
+        emitter = []
+        for i in range(config["num_emitters"]):
+            emitter.append(config[f"emitter_{i}"])
+            config.pop(f"emitter_{i}")
+        config.pop("num_emitters")
+        config["emitter"] = emitter
+        return cls(**config)
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/Priors.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/Priors.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,30 +1,32 @@
 import os
 import tensorflow as tf
 import learnMSA.msa_hmm.DirichletMixture as dm
 
 
-class AminoAcidPrior():
+class AminoAcidPrior(tf.keras.layers.Layer):
     """The default dirichlet mixture prior for amino acids.
 
     Args:
         comp_count: The number of components in the mixture.
+        epsilon: A small constant for numerical stability.
     """
-    def __init__(self, comp_count=1, epsilon=1e-32):
+    def __init__(self, comp_count=1, epsilon=1e-16, **kwargs):
+        super(AminoAcidPrior, self).__init__(**kwargs)
         self.comp_count = comp_count
         self.epsilon = epsilon
         
     def load(self, dtype):
         prior_path = os.path.dirname(__file__)+"/trained_prior/"
         dtype = dtype if isinstance(dtype, str) else dtype.name
         model_path = prior_path+"_".join([str(self.comp_count), "True", dtype, "_dirichlet/ckpt"])
         model = dm.load_mixture_model(model_path, self.comp_count, 20, trainable=False, dtype=dtype)
         self.emission_dirichlet_mix = model.layers[-1]
         
-    def __call__(self, B, lengths):
+    def call(self, B, lengths):
         """Computes log pdf values for each match state.
         Args:
         B: A stack of k emission matrices. Assumes that the 20 std amino acids are the first 20 positions of the last dimension
             and that the states are ordered the standard way as seen in MsaHmmCell. Shape: (k, q, s)
         Returns:
             A tensor with the log pdf values of this Dirichlet mixture. The models can vary in length. 
             Shorter models will have a zero padding in the output. Shape: (k, max_model_length)
@@ -37,79 +39,89 @@
         B /= tf.reduce_sum(B, axis=-1, keepdims=True) 
         B = tf.reshape(B, (-1, 20))
         prior = self.emission_dirichlet_mix.log_pdf(B)
         prior = tf.reshape(prior, (k, max_model_length))
         prior *= tf.cast(tf.sequence_mask(lengths), B.dtype)
         return prior 
     
+    def get_config(self):
+        config = super(AminoAcidPrior, self).get_config()
+        cell_config = {
+             "comp_count" : self.comp_count,
+             "epsilon" : self.epsilon
+        }
+        config.update(cell_config)
+        return config
+    
     def __repr__(self):
         return f"AminoAcidPrior(comp_count={self.comp_count})"
     
     
-class NullPrior():
+class NullPrior(tf.keras.layers.Layer):
     """NullObject if no prior should be used.
     """
     def load(self, dtype):
         pass
     
-    def __call__(self, B):
+    def call(self, B):
         k = tf.shape(B)[0]
         model_length = int((tf.shape(B)[1]-2)/2)
         return tf.zeros((k, model_length), dtype=B.dtype)
     
     def __repr__(self):
         return f"NullPrior()"
     
     
-class ProfileHMMTransitionPrior():
+class ProfileHMMTransitionPrior(tf.keras.layers.Layer):
     """The default dirichlet mixture prior for profileHMM transitions.
 
     Args:
         match_comp: The number of components for the match prior.
         insert_comp: The number of components for the insert prior.
         delete_comp: The number of components for the delete prior.
         alpha_flank: Favors high probability of staying one of the 3 flanking states.
         alpha_single: Favors high probability for a single main model hit (avoid looping paths).
         alpha_frag: Favors models with high prob. to enter at the first match and exit after the last match.
+        epsilon: A small constant for numerical stability.
     """
     def __init__(self, 
                  match_comp=1, 
                  insert_comp=1, 
                  delete_comp=1,
                  alpha_flank = 7000,
                  alpha_single = 1e9,
-                 alpha_frag = 1e4):
+                 alpha_frag = 1e4,
+                 epsilon=1e-16, 
+                 **kwargs):
+        super(ProfileHMMTransitionPrior, self).__init__(**kwargs)
         self.match_comp = match_comp
         self.insert_comp = insert_comp
         self.delete_comp = delete_comp
         #equivalent to the alpha parameters of a dirichlet mixture -1 .
         #these values are crutial when jointly optimizing the main model with the additional
         #"Plan7" states and transitions
         self.alpha_flank = alpha_flank
         self.alpha_single = alpha_single
         self.alpha_frag = alpha_frag
+        self.epsilon = epsilon
         
     def load(self, dtype):
-        self.alpha_flank = tf.constant(self.alpha_flank, dtype=dtype) 
-        self.alpha_single = tf.constant(self.alpha_single, dtype=dtype) 
-        self.alpha_frag = tf.constant(self.alpha_frag, dtype=dtype) 
-
         prior_path = os.path.dirname(__file__)+"/trained_prior/transition_priors/"
 
         match_model_path = prior_path + "_".join(["match_prior", str(self.match_comp), dtype]) + "/ckpt"
         match_model = dm.load_mixture_model(match_model_path, self.match_comp, 3, trainable=False, dtype=dtype)
         self.match_dirichlet = match_model.layers[-1]
         insert_model_path = prior_path + "_".join(["insert_prior", str(self.insert_comp), dtype]) + "/ckpt"
         insert_model = dm.load_mixture_model(insert_model_path, self.insert_comp, 2, trainable=False, dtype=dtype)
         self.insert_dirichlet = insert_model.layers[-1]
         delete_model_path = prior_path + "_".join(["delete_prior", str(self.delete_comp), dtype]) + "/ckpt"
         delete_model = dm.load_mixture_model(delete_model_path, self.delete_comp, 2, trainable=False, dtype=dtype)
         self.delete_dirichlet = delete_model.layers[-1]
         
-    def __call__(self, probs_list, flank_init_prob):
+    def call(self, probs_list, flank_init_prob):
         """Computes log pdf values for each transition prior.
         Args:
         probs_list: A list of dictionaries that map transition type to probabilities per model.
         flank_init_prob: Flank init probabilities per model.
         Returns:
             A dictionary that maps prior names to lists of prior values per model.
         """
@@ -142,26 +154,42 @@
             flank += self.alpha_flank * log_probs["end_to_right_flank"]
             flank += self.alpha_flank * tf.math.log(flank_init_prob[i])
             flank_prior.append(tf.squeeze(flank))
             #uni-hit
             hit = self.alpha_single * tf.math.log(probs["end_to_right_flank"] + probs["end_to_terminal"]) 
             hit_prior.append(tf.squeeze(hit))
             #uniform entry/exit prior
-            btm = probs["begin_to_match"] / (1- probs["match_to_delete"][0]) #rescale begin_to_match to sum to 1
+            #rescale begin_to_match to sum to 1
+            div = tf.math.maximum(self.epsilon, 1- probs["match_to_delete"][0]) 
+            btm = probs["begin_to_match"] / div
             enex = tf.expand_dims(btm, 1) * tf.expand_dims(probs["match_to_end"], 0)
             enex = tf.linalg.band_part(enex, 0, -1)
-            enex = tf.math.log(1 - enex) 
+            enex = tf.math.log(tf.math.maximum(self.epsilon, 1 - enex))
             enex_prior.append( self.alpha_frag * (tf.reduce_sum(enex) - enex[0, -1]) )
         prior_val = {
             "match_prior" : match_dirichlet,
             "insert_prior" : insert_dirichlet,
             "delete_prior" : delete_dirichlet,
             "flank_prior" : flank_prior,
             "hit_prior" : hit_prior,
             "enex_prior" : enex_prior}
         prior_val = {k : tf.stack(v) for k,v in prior_val.items()}
         return prior_val
     
+    def get_config(self):
+        config = super(ProfileHMMTransitionPrior, self).get_config()
+        cell_config = {
+             "match_comp" : self.match_comp, 
+             "insert_comp" : self.insert_comp, 
+             "delete_comp" : self.delete_comp, 
+             "alpha_flank" : self.alpha_flank, 
+             "alpha_single" : self.alpha_single, 
+             "alpha_frag" : self.alpha_frag, 
+             "epsilon" : self.epsilon
+        }
+        config.update(cell_config)
+        return config
+    
     def __repr__(self):
         return f"ProfileHMMTransitionPrior(match_comp={self.match_comp}, insert_comp={self.insert_comp}, delete_comp={self.delete_comp}, alpha_flank={self.alpha_flank}, alpha_single={self.alpha_single}, alpha_frag={self.alpha_frag})"
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/Training.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/Training.py`

 * *Files 0% similar despite different names*

```diff
@@ -13,15 +13,15 @@
         and sequence indices of shape (b, num_model).
     Args:
         encoder_layers: A list of layers with compatible inputs and outputs and the last output 
                         is compatible with msa_hmm_layer. 
         msa_hmm_layer: An instance of MsaHmmLayer.
     """
     num_models = msa_hmm_layer.cell.num_models
-    sequences = tf.keras.Input(shape=(None,None,), name="sequences", dtype=tf.uint8)
+    sequences = tf.keras.Input(shape=(None,None), name="sequences", dtype=tf.uint8)
     indices = tf.keras.Input(shape=(None,), name="indices", dtype=tf.int64)
     #in the input pipeline, we need the batch dimension to come first to make multi GPU work 
     #we transpose here, because all learnMSA layers require the model dimension to come first
     transposed_sequences = tf.transpose(sequences, [1,0,2])
     transposed_indices = tf.transpose(indices)
     forward_seq = transposed_sequences
     for layer in encoder_layers:
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/Transitioner.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/Transitioner.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,17 @@
 import tensorflow as tf
 import numpy as np
 import learnMSA.msa_hmm.Initializers as initializers
 import learnMSA.msa_hmm.Priors as priors
 import learnMSA.msa_hmm.Configuration as config
+from packaging import version
+if version.parse(tf.__version__) < version.parse("2.11.0"):
+    from tensorflow.python.training.tracking.data_structures import NoDependency #see https://github.com/tensorflow/tensorflow/issues/36916
+else:
+    from tensorflow.python.trackable.data_structures import NoDependency 
 
 class ProfileHMMTransitioner(tf.keras.layers.Layer):
     """ A transitioner defines which transitions between HMM states are allowed, how they are initialized
         and how the transition matrix is represented (dense, sparse, other).
         The transitioner also holds a prior on the transition distributions. 
         This transitioner implements the default profile HMM logic with the additional Plan7 states.
     Args:
@@ -17,22 +22,22 @@
                         by adding "kernel_id" : False
     """
     def __init__(self, 
                 transition_init = initializers.make_default_transition_init(),
                 flank_init = initializers.make_default_flank_init(),
                 prior = priors.ProfileHMMTransitionPrior(),
                 frozen_kernels={},
-                dtype=tf.float32,
                 **kwargs):
-        super(ProfileHMMTransitioner, self).__init__(name="ProfileHMMTransitioner", dtype=dtype, **kwargs)
-        self.transition_init = [transition_init] if isinstance(transition_init, dict) else transition_init 
+        super(ProfileHMMTransitioner, self).__init__(**kwargs)
+        transition_init = [transition_init] if isinstance(transition_init, dict) else transition_init 
+        self.transition_init = NoDependency(transition_init)
         self.flank_init = [flank_init] if not hasattr(flank_init, '__iter__') else flank_init 
         self.prior = prior
         self.frozen_kernels = frozen_kernels
-        self.epsilon = tf.constant(1e-32, dtype)
+        self.epsilon = tf.constant(1e-32, self.dtype)
         self.approx_log_zero = tf.math.log(self.epsilon)
         
     def cell_init(self, cell):
         """ Automatically called when the owner cell is created.
         """
         self.length = cell.length
         assert len(self.length) == len(self.transition_init), \
@@ -314,15 +319,15 @@
         Returns:
                 Shape (k, b, q)
         """
         #batch matmul of k inputs with k matricies
         return tf.matmul(inputs, self.A)
     
     def get_prior_log_densities(self):
-        return self.prior(self.probs, self.make_flank_init_prob())
+        return self.prior(self.make_probs(), self.make_flank_init_prob())
     
     def duplicate(self, model_indices=None):
         if model_indices is None:
             model_indices = range(len(self.transition_init))
         sub_transition_init = []
         sub_flank_init = []
         for i in model_indices:
@@ -378,14 +383,37 @@
         padded_and_stacked = {k : tf.keras.preprocessing.sequence.pad_sequences(arrays, 
                                                                                 dtype=arrays[0].dtype.name, 
                                                                                 padding="post",
                                                                                 value=self.approx_log_zero) 
                               for k,arrays in transposed.items()}
         return padded_and_stacked
     
+    def get_config(self):
+        config = super(ProfileHMMTransitioner, self).get_config()
+        for key in self.transition_kernel[0].keys():
+            config[key] = [self.transition_kernel[i][key].numpy() for i in range(self.num_models)]
+        config.update({
+            "num_models" : len(self.transition_kernel),
+            "flank_init" : [k.numpy() for k in self.flank_init_kernel],
+            "prior" : self.prior,
+            "frozen_kernels" : self.frozen_kernels
+        })
+        return config
+    
+    @classmethod
+    def from_config(cls, config):
+        transition_init = [{} for i in range(config.pop("num_models"))]
+        for key,_ in _make_explicit_transition_kernel_parts(1):
+            kernels = config.pop(key)
+            for i,d in enumerate(transition_init):
+                d[key] = initializers.ConstantInitializer(kernels[i])
+        config["transition_init"] = transition_init
+        config["flank_init"] = [initializers.ConstantInitializer(k) for k in config["flank_init"]]
+        return cls(**config)
+    
     def __repr__(self):
         return f"ProfileHMMTransitioner(\n transition_init={config.as_str(self.transition_init[0], 2, '    ', ' , ')},\n flank_init={self.flank_init[0]},\n prior={self.prior},\n frozen_kernels={self.frozen_kernels})"
     
 
 def _make_explicit_transition_kernel_parts(length): 
     return [("begin_to_match", length), 
              ("match_to_end", length),
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/Utility.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/Utility.py`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/Visualize.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/Visualize.py`

 * *Files 10% similar despite different names*

```diff
@@ -6,26 +6,26 @@
 import numpy as np
 import tensorflow as tf
 from learnMSA import msa_hmm
 import itertools
 import seaborn as sns
 
 
-def plot_logo(alignment, model_index, ax):
-    hmm_cell = alignment.msa_hmm_layer.cell
+def plot_logo(am, model_index, ax):
+    hmm_cell = am.msa_hmm_layer.cell
     hmm_cell.recurrent_init()
     length = hmm_cell.length[model_index]
     
     logomaker_alphabet = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"]
     logomaker_perm = np.array([msa_hmm.fasta.alphabet.index(aa) for aa in logomaker_alphabet], dtype=int)
 
     #reduce to std AA alphabet 
     emissions = hmm_cell.emitter[0].make_B_amino().numpy()[model_index, 1:length+1,:20][:,logomaker_perm]
     background = hmm_cell.emitter[0].make_B_amino().numpy()[model_index, 0, :20][logomaker_perm]
-    #background = hmm_cell.emitter[0].emission_init[model_index]((length,25), dtype=alignment.msa_hmm_layer.dtype)[0, :20]
+    #background = hmm_cell.emitter[0].emission_init[model_index]((length,25), dtype=am.msa_hmm_layer.dtype)[0, :20]
     information_content = tf.keras.losses.KLDivergence(reduction=tf.keras.losses.Reduction.NONE)(
                                                          emissions,
                                                          np.expand_dims(background, 0))
     information_content = tf.expand_dims(information_content, -1).numpy()
 
     information_content_df = pd.DataFrame(information_content * emissions, 
                                           columns=logomaker_alphabet)
@@ -39,30 +39,28 @@
                        width=.8,
                        ax=ax)
 
     # style using Axes methods
     logo.ax.set_ylabel('information content')
     logo.ax.set_xlim([-1, len(information_content_df)])
     
-
-
     
-def plot_hmm(alignment, 
+def plot_hmm(am, 
              model_index,
              ax,
                edge_show_threshold=1e-2, #grey out edges below this threshold (label_probs=False requires adjustment)
                num_aa=3, #print this many of the aminoacids with highest emission probability per match state
                label_probs=True, #label edges with probabilities, label with kernel values otherwise
                seq_indices=[], #index of the sequence, which viterbi sequence is plotted, -1 means no sequence 
                spacing=1.0,
                path_colors=[],
                active_transition_color="#000000",
                inactive_transition_color="#E0E0E0"
                 ):
-    hmm_cell = alignment.msa_hmm_layer.cell
+    hmm_cell = am.msa_hmm_layer.cell
     hmm_cell.recurrent_init()
     length = hmm_cell.length[model_index]
     
     G = nx.DiGraph()
     indices_dict = hmm_cell.transitioner.sparse_transition_indices_explicit[model_index]
     probs = hmm_cell.transitioner.make_probs()[model_index]
     for transition_type, indices in indices_dict.items():
@@ -128,17 +126,17 @@
                                 label_pos=0.6,
                                 font_size=10, 
                                 ax=ax)
     label_pos = {i : (x, y+0.1+0.05*num_aa) for i, (x,y) in pos.items()}
     nx.draw_networkx_labels(G, label_pos, labels=node_labels, font_size=8)
     
     for k, (seq_i, path_color) in enumerate(zip(seq_indices, path_colors)):
-        ds = msa_hmm.train.make_dataset(np.array([seq_i]), alignment.batch_generator, batch_size=1, shuffle=False)
+        ds = msa_hmm.train.make_dataset(np.array([seq_i]), am.batch_generator, batch_size=1, shuffle=False)
         for x, _ in ds:
-            sequence = alignment.encoder_model(x)  
+            sequence = am.encoder_model(x)  
         hidden_seq = msa_hmm.viterbi.viterbi(sequence, hmm_cell).numpy()[model_index]
         hidden_seq = list(hidden_seq[0])
         for i in range(len(hidden_seq)):
             #find silent path parts along delete states
             #match to match
             if (i < len(hidden_seq)-1 and
                 hidden_seq[i] > 0 and 
@@ -180,119 +178,119 @@
                                 min_target_margin=5,
                                 ax=ax)
         
     #make a legend for the hidden paths
     if len(seq_indices) > 0:
         f = lambda c: ax.plot([],[], color=c)[0]
         handles = [f(col) for col in path_colors]
-        labels = [alignment.fasta_file.seq_ids[seq_i] for seq_i in seq_indices]
+        labels = [am.fasta_file.seq_ids[seq_i] for seq_i in seq_indices]
         leg = ax.legend(handles, labels, loc="lower right", prop={'size': 18})
         for line in leg.get_lines():
             line.set_linewidth(8.0)
     plt.subplots_adjust(left=0.4, right=0.6, top=0.9, bottom=0.1)
     
     
-def plot_anc_probs(alignment, 
+def plot_anc_probs(am, 
                    model_index,
                    seqs=[0,1,2], 
                    pos=list(range(6)), 
                    rescale=True, 
                    title="Site-wise ancestral probabilities"):
     n, m = len(seqs), len(pos)
-    ds = msa_hmm.train.make_dataset(alignment.indices[seqs], 
-                                    alignment.batch_generator,
+    ds = msa_hmm.train.make_dataset(am.indices[seqs], 
+                                    am.batch_generator,
                                     batch_size=n, 
                                     shuffle=False)
     for x,_ in ds:
-        ancs = alignment.encoder_model(x).numpy()[model_index]
-    i = [l.name for l in alignment.encoder_model.layers].index("AncProbsLayer")
-    anc_probs_layer = alignment.encoder_model.layers[i]
-    indices = np.stack([alignment.indices]*alignment.msa_hmm_layer.cell.num_models)
+        ancs = am.encoder_model(x).numpy()[model_index]
+    i = [l.name for l in am.encoder_model.layers].index("anc_probs_layer")
+    anc_probs_layer = am.encoder_model.layers[i]
+    indices = np.stack([am.indices]*am.msa_hmm_layer.cell.num_models)
     indices = np.expand_dims(indices, -1)
     tau = anc_probs_layer.make_tau(indices)[model_index]
     if rescale:
         ancs /= np.sum(ancs, -1, keepdims=True)
     f, axes = plt.subplots(n, m, sharey=True)
     axes = axes.flatten()
     f.set_size_inches(3+3*m, 2*n)
     for a,(s,i) in enumerate(itertools.product(seqs, pos)):
         sns.barplot(x=msa_hmm.fasta.alphabet[:20], y=ancs[s,i,:20], ax=axes[a]);
         if a % m == 0:
             axes[a].annotate(f"tau={'%.3f'%tau[s]} ->", (0.3,0.9*axes[a].get_ylim()[1]))
     f.suptitle(title, fontsize=16)
     
     
-def plot_rate_matrices(alignment,
+def plot_rate_matrices(am,
                        model_index,
                        title="normalized rate matrix (1 time unit = 1 expected mutation per site)"):
-    i = [l.name for l in alignment.encoder_model.layers].index("AncProbsLayer")
-    anc_probs_layer = alignment.encoder_model.layers[i]
+    i = [l.name for l in am.encoder_model.layers].index("anc_probs_layer")
+    anc_probs_layer = am.encoder_model.layers[i]
     Q = anc_probs_layer.make_Q()[model_index]
     k = Q.shape[0]
     f, axes = plt.subplots(1, k, sharey=True)
     f.set_size_inches(10*k, 10.5)
     if k > 1:
         axes = axes.flatten()
     else:
         axes = [axes]
     for i,ax in enumerate(axes):
         a = msa_hmm.fasta.alphabet[:20]
         sns.heatmap(Q[i], linewidth=0.5, ax=ax, xticklabels=a, yticklabels=a)
     f.suptitle(title, fontsize=16)
     
     
-def print_and_plot(alignment, 
+def print_and_plot(am, 
                    model_index = None,
                    max_seq = 20, 
                    seqs_to_plot = [0,1,2], 
                    seq_ids = False, 
                    show_model=True, 
                    show_anc_probs=True,
                    show_logo=True,
                    model_filename="", 
                    anc_probs_filename="",
                    logo_filename=""):
     if model_index is None:
-        model_index = alignment.best_model
+        model_index = am.best_model
     # print the alignment
-    msa = alignment.to_string(model_index)
-    i = [l.name for l in alignment.encoder_model.layers].index("AncProbsLayer")
-    anc_probs_layer = alignment.encoder_model.layers[i]
-    ds = msa_hmm.train.make_dataset(alignment.indices, 
-                            alignment.batch_generator,
-                            alignment.batch_size, 
+    msa = am.to_string(model_index)
+    i = [l.name for l in am.encoder_model.layers].index("anc_probs_layer")
+    anc_probs_layer = am.encoder_model.layers[i]
+    ds = msa_hmm.train.make_dataset(am.indices, 
+                            am.batch_generator,
+                            am.batch_size, 
                             shuffle=False)
-    ll = alignment.model.predict(ds)[:,model_index] + alignment.prior[model_index]
+    ll = am.model.predict(ds)[:,model_index] + am.compute_log_prior()[model_index]
     for i,s in enumerate(msa[:max_seq]):
-        indices = np.array([[alignment.indices[i]]]*alignment.msa_hmm_layer.cell.num_models)
+        indices = np.array([[am.indices[i]]]*am.msa_hmm_layer.cell.num_models)
         tau = anc_probs_layer.make_tau(indices)[model_index]
         param_string = "l=%.2f" % (ll[i]) + "_t=%.2f" % tau
         if seq_ids:
-            print(f">{alignment.fasta_file.seq_ids[i]} "+param_string)
+            print(f">{am.fasta_file.seq_ids[am.indices[i]]} "+param_string)
         else:
             print(">"+param_string)
         print(s)
     if len(msa) > max_seq:
         print(len(msa) - max_seq, "sequences omitted.")
     if show_model:
         #plot the model
         fig = plt.figure(frameon=False)
         ax = fig.add_axes([0, 0, 1, 1])
-        plot_hmm(alignment, model_index, ax, 
-                 seq_indices=alignment.indices[seqs_to_plot],
+        plot_hmm(am, model_index, ax, 
+                 seq_indices=am.indices[seqs_to_plot],
                  path_colors=["#CC6600", "#0000cc", "#00cccc"])   
         if model_filename != "":
             plt.savefig(model_filename, bbox_inches='tight')
     if show_anc_probs:
-        plot_anc_probs(alignment, model_index, seqs=seqs_to_plot)
+        plot_anc_probs(am, model_index, seqs=seqs_to_plot)
         if anc_probs_filename != "":
             plt.savefig(anc_probs_filename, bbox_inches='tight')
     if show_logo:
         fig, ax = plt.subplots()
-        plot_logo(alignment, model_index, ax)
+        plot_logo(am, model_index, ax)
         if logo_filename != "":
             plt.savefig(logo_filename, bbox_inches='tight')
         
         
 def plot_sequence_length_distribution(fasta_filename, 
                                      bins=100,
                                      q=0.75):
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/Viterbi.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/Viterbi.py`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/__init__.py` & `learnMSA-1.1.2/learnMSA/msa_hmm/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 import learnMSA.msa_hmm.Viterbi as viterbi
 import learnMSA.msa_hmm.Align as align
-from learnMSA.msa_hmm.Align import Alignment
+from learnMSA.msa_hmm.AlignmentModel import AlignmentModel
 import learnMSA.msa_hmm.Fasta as fasta
 import learnMSA.msa_hmm.Training as train
 import learnMSA.msa_hmm.Emitter as emit
 import learnMSA.msa_hmm.Transitioner as trans
 import learnMSA.msa_hmm.MsaHmmCell as cell
 from learnMSA.msa_hmm.MsaHmmCell import MsaHmmCell
 import learnMSA.msa_hmm.AncProbsLayer as anc_probs
```

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/100_components_prior_pdf/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1024_components_prior_pdf/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_False_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_True_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/128_components_prior_pdf/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_False_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_True_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/1_components_prior_pdf/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_False_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_True_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/256_components_prior_pdf/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_False_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_True_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/32_components_prior_pdf/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_False_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_True_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/3_components_prior_pdf/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/512_components_prior_pdf/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_False_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_True_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/64_components_prior_pdf/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_False_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float32__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_True_float64__dirichlet/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/9_components_prior_pdf/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float32/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_1_float64/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float32/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/delete_prior_2_float64/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float32/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_1_float64/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float32/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_2_float64/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float32/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_3_float64/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float32/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/insert_prior_5_float64/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float32/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_10_float64/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float32/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_1_float64/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float32/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_2_float64/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float32/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_3_float64/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float32/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/ckpt.data-00000-of-00001` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/ckpt.data-00000-of-00001`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/ckpt.index` & `learnMSA-1.1.2/learnMSA/msa_hmm/trained_prior/transition_priors/match_prior_5_float64/ckpt.index`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA/run/console.py` & `learnMSA-1.1.2/learnMSA/run/console.py`

 * *Files identical despite different names*

### Comparing `learnMSA-1.1.1/learnMSA.egg-info/SOURCES.txt` & `learnMSA-1.1.2/learnMSA.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 learnMSA.egg-info/PKG-INFO
 learnMSA.egg-info/SOURCES.txt
 learnMSA.egg-info/dependency_links.txt
 learnMSA.egg-info/entry_points.txt
 learnMSA.egg-info/requires.txt
 learnMSA.egg-info/top_level.txt
 learnMSA/msa_hmm/Align.py
+learnMSA/msa_hmm/AlignmentModel.py
 learnMSA/msa_hmm/AncProbsLayer.py
 learnMSA/msa_hmm/Configuration.py
 learnMSA/msa_hmm/DirichletMixture.py
 learnMSA/msa_hmm/Emitter.py
 learnMSA/msa_hmm/Fasta.py
 learnMSA/msa_hmm/Initializers.py
 learnMSA/msa_hmm/MsaHmmCell.py
```

### Comparing `learnMSA-1.1.1/setup.py` & `learnMSA-1.1.2/setup.py`

 * *Files identical despite different names*

