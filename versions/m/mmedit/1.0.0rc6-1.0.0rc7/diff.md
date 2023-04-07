# Comparing `tmp/mmedit-1.0.0rc6.tar.gz` & `tmp/mmedit-1.0.0rc7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/mmedit-1.0.0rc6.tar", last modified: Fri Mar  3 07:44:39 2023, max compression
+gzip compressed data, was "dist/mmedit-1.0.0rc7.tar", last modified: Fri Apr  7 07:57:26 2023, max compression
```

## Comparing `mmedit-1.0.0rc6.tar` & `mmedit-1.0.0rc7.tar`

### file list

```diff
@@ -1,955 +1,966 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/
--rw-r--r--   0 runner    (1001) docker     (123)      281 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    22057 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    17794 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)     5631 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/basicvsr_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1080 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/celeba.py
--rw-r--r--   0 runner    (1001) docker     (123)      696 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/cifar10_noaug.py
--rw-r--r--   0 runner    (1001) docker     (123)     1025 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/cifar10_nopad.py
--rw-r--r--   0 runner    (1001) docker     (123)      925 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/comp1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     2851 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/deblurring-defocus_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2859 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/deblurring-motion_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1736 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/decompression_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2931 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/denoising-gaussian_color_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2403 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/denoising-gaussian_gray_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1570 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/denoising-real_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3583 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/deraining_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1254 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/ffhq_flip.py
--rw-r--r--   0 runner    (1001) docker     (123)     1184 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/grow_scale_imgs_ffhq_styleganv1.py
--rw-r--r--   0 runner    (1001) docker     (123)     1390 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/imagenet_128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1395 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/imagenet_256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1392 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/imagenet_512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1386 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/imagenet_64.py
--rw-r--r--   0 runner    (1001) docker     (123)     1329 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/imagenet_noaug_128.py
--rw-r--r--   0 runner    (1001) docker     (123)     2833 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/liif_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1170 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/lsun_stylegan.py
--rw-r--r--   0 runner    (1001) docker     (123)     2938 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/paired_imgs_256x256_crop.py
--rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/places.py
--rw-r--r--   0 runner    (1001) docker     (123)     2588 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/sisr_x2_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2537 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/sisr_x3_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     2537 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/sisr_x4_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     3767 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/tdan_test_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1176 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1137 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)     1216 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_flip_512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1283 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_flip_lanczos_resize_256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     3154 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/unpaired_imgs_256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/default_runtime.py
--rw-r--r--   0 runner    (1001) docker     (123)     2047 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/gen_default_runtime.py
--rw-r--r--   0 runner    (1001) docker     (123)      964 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/inpaint_default_runtime.py
--rw-r--r--   0 runner    (1001) docker     (123)      989 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/matting_default_runtime.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/
--rw-r--r--   0 runner    (1001) docker     (123)      783 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_cyclegan.py
--rw-r--r--   0 runner    (1001) docker     (123)     3210 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_deepfillv1.py
--rw-r--r--   0 runner    (1001) docker     (123)     3261 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_deepfillv2.py
--rw-r--r--   0 runner    (1001) docker     (123)     3226 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_edvr.py
--rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_gl.py
--rw-r--r--   0 runner    (1001) docker     (123)     1436 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_glean.py
--rw-r--r--   0 runner    (1001) docker     (123)     3533 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_liif.py
--rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_pconv.py
--rw-r--r--   0 runner    (1001) docker     (123)      817 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_pix2pix.py
--rw-r--r--   0 runner    (1001) docker     (123)      279 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_styleganv1.py
--rw-r--r--   0 runner    (1001) docker     (123)      801 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_styleganv2.py
--rw-r--r--   0 runner    (1001) docker     (123)      846 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_styleganv3.py
--rw-r--r--   0 runner    (1001) docker     (123)     2889 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_tof.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/biggan/
--rw-r--r--   0 runner    (1001) docker     (123)      796 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/biggan/base_biggan_128x128.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/dcgan/
--rw-r--r--   0 runner    (1001) docker     (123)      353 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/dcgan/base_dcgan_128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      340 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/dcgan/base_dcgan_64x64.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/sagan/
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/sagan/base_sagan_128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      671 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/sagan/base_sagan_32x32.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/sngan_proj/
--rw-r--r--   0 runner    (1001) docker     (123)      330 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/sngan_proj/base_sngan_proj_128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      328 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/sngan_proj/base_sngan_proj_32x32.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/aot_gan/
--rw-r--r--   0 runner    (1001) docker     (123)     3876 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/aot_gan/aot-gan_smpgan_4xb4_places-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      655 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/aot_gan/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr/
--rw-r--r--   0 runner    (1001) docker     (123)     3586 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr/basicvsr_2xb4_reds4.py
--rw-r--r--   0 runner    (1001) docker     (123)     2564 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr/basicvsr_2xb4_vimeo90k-bd.py
--rw-r--r--   0 runner    (1001) docker     (123)      425 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr/basicvsr_2xb4_vimeo90k-bi.py
--rw-r--r--   0 runner    (1001) docker     (123)     3143 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/
--rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-decompress-track1.py
--rw-r--r--   0 runner    (1001) docker     (123)      384 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-decompress-track2.py
--rw-r--r--   0 runner    (1001) docker     (123)      384 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-decompress-track3.py
--rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-vsr.py
--rw-r--r--   0 runner    (1001) docker     (123)     1278 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_4xb2-300k_vimeo90k-bd.py
--rw-r--r--   0 runner    (1001) docker     (123)     1278 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_4xb2-300k_vimeo90k-bi.py
--rw-r--r--   0 runner    (1001) docker     (123)     1367 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_8xb1-600k_reds4.py
--rw-r--r--   0 runner    (1001) docker     (123)     5065 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/
--rw-r--r--   0 runner    (1001) docker     (123)     1561 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face-rgb_imagenet1k-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1780 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face_rgb_imagenet1k-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1780 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face_rgb_imagenet1k-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2312 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan_2xb25-500kiters_cifar10-32x32.py
--rw-r--r--   0 runner    (1001) docker     (123)     1706 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan_ajbrock-sn_8xb32-1500kiters_imagenet1k-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1550 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan_cvt-BigGAN-PyTorch-rgb_imagenet1k-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     2818 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/cain/
--rw-r--r--   0 runner    (1001) docker     (123)     4202 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/cain/cain_g1b32_1xb5_vimeo90k-triplet.py
--rw-r--r--   0 runner    (1001) docker     (123)      632 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/cain/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/
--rw-r--r--   0 runner    (1001) docker     (123)     3170 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-250kiters_summer2winter.py
--rw-r--r--   0 runner    (1001) docker     (123)     3116 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-270kiters_horse2zebra.py
--rw-r--r--   0 runner    (1001) docker     (123)     2562 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-80kiters_facades.py
--rw-r--r--   0 runner    (1001) docker     (123)     3147 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-250kiters_summer2winter.py
--rw-r--r--   0 runner    (1001) docker     (123)     3117 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-270kiters_horse2zebra.py
--rw-r--r--   0 runner    (1001) docker     (123)     2563 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-80kiters_facades.py
--rw-r--r--   0 runner    (1001) docker     (123)     3355 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dcgan/
--rw-r--r--   0 runner    (1001) docker     (123)     1432 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dcgan/dcgan_1xb128-300kiters_celeba-cropped-64.py
--rw-r--r--   0 runner    (1001) docker     (123)     1389 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dcgan/dcgan_1xb128-5epoches_lsun-bedroom-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)     1894 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dcgan/dcgan_Glr4e-4_Dlr1e-4_1xb128-5kiters_mnist-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)     1753 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dcgan/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv1/
--rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv1/deepfillv1_4xb4_celeba-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1441 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv1/deepfillv1_8xb2_places-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1003 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv1/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv2/
--rw-r--r--   0 runner    (1001) docker     (123)     1495 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv2/deepfillv2_8xb2_celeba-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1496 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv2/deepfillv2_8xb2_places-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)      998 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv2/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dic/
--rw-r--r--   0 runner    (1001) docker     (123)     1764 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dic/dic_gan-x8c48b6_4xb2-500k_celeba-hq.py
--rw-r--r--   0 runner    (1001) docker     (123)     3864 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dic/dic_x8c48b6_4xb2-150k_celeba-hq.py
--rw-r--r--   0 runner    (1001) docker     (123)     1006 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dic/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dim/
--rw-r--r--   0 runner    (1001) docker     (123)     2655 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dim/dim_stage1-v16_1xb1-1000k_comp1k.py
--rw-r--r--   0 runner    (1001) docker     (123)      851 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dim/dim_stage1-v16_1xb1-1000k_comp1k_online-merge.py
--rw-r--r--   0 runner    (1001) docker     (123)      505 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dim/dim_stage2-v16-pln_1xb1-1000k_comp1k.py
--rw-r--r--   0 runner    (1001) docker     (123)      508 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dim/dim_stage3-v16-pln_1xb1-1000k_comp1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1595 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/dim/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/disco_diffusion/
--rw-r--r--   0 runner    (1001) docker     (123)     1570 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/disco_diffusion/disco-diffusion_adm-u-finetuned_imagenet-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1562 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/disco_diffusion/disco-diffusion_adm-u-finetuned_imagenet-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/disco_diffusion/disco-diffusion_portrait-generator-v001.py
--rw-r--r--   0 runner    (1001) docker     (123)     1278 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/disco_diffusion/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/edsr/
--rw-r--r--   0 runner    (1001) docker     (123)     3885 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/edsr/edsr_x2c64b16_1xb16-300k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     4044 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/edsr/edsr_x3c64b16_1xb16-300k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     3972 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/edsr/edsr_x4c64b16_1xb16-300k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1916 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/edsr/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/edvr/
--rw-r--r--   0 runner    (1001) docker     (123)     1138 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/edvr/edvrl_c128b40_8xb8-lr2e-4-600k_reds4.py
--rw-r--r--   0 runner    (1001) docker     (123)     1005 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/edvr/edvrl_wotsa-c128b40_8xb8-lr2e-4-600k_reds4.py
--rw-r--r--   0 runner    (1001) docker     (123)     1299 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/edvr/edvrm_8xb4-600k_reds.py
--rw-r--r--   0 runner    (1001) docker     (123)     1108 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/edvr/edvrm_wotsa_8xb4-600k_reds.py
--rw-r--r--   0 runner    (1001) docker     (123)     1798 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/edvr/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/eg3d/
--rw-r--r--   0 runner    (1001) docker     (123)     2204 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_afhq-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2346 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_ffhq-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2379 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_shapenet-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1416 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/eg3d/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/esrgan/
--rw-r--r--   0 runner    (1001) docker     (123)     3759 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/esrgan/esrgan_psnr-x4c64b23g32_1xb16-1000k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     2106 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/esrgan/esrgan_x4c64b23g32_1xb16-400k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1424 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/esrgan/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/flavr/
--rw-r--r--   0 runner    (1001) docker     (123)     4502 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/flavr/flavr_in4out1_8xb4_vimeo90k-septuplet.py
--rw-r--r--   0 runner    (1001) docker     (123)      643 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/flavr/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/gca/
--rw-r--r--   0 runner    (1001) docker     (123)     3622 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/gca/baseline_r34_4xb10-200k_comp1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1408 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/gca/baseline_r34_4xb10-dimaug-200k_comp1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     3559 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/gca/gca_r34_4xb10-200k_comp1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1398 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/gca/gca_r34_4xb10-dimaug-200k_comp1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1772 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/gca/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/ggan/
--rw-r--r--   0 runner    (1001) docker     (123)     1616 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/ggan/ggan_dcgan-archi_lr1e-3-1xb128-12Mimgs_celeba-cropped-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)     1626 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/ggan/ggan_dcgan-archi_lr1e-4-1xb64-10Mimgs_celeba-cropped-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1984 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/ggan/ggan_lsgan-archi_lr1e-4-1xb128-20Mimgs_lsun-bedroom-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)     1470 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/ggan/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/glean/
--rw-r--r--   0 runner    (1001) docker     (123)      309 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/glean/glean_in128out1024-fp16_4xb2-300k_ffhq-celeba-hq.py
--rw-r--r--   0 runner    (1001) docker     (123)     4994 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/glean/glean_in128out1024_4xb2-300k_ffhq-celeba-hq.py
--rw-r--r--   0 runner    (1001) docker     (123)      261 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/glean/glean_x16-fp16_2xb8_ffhq.py
--rw-r--r--   0 runner    (1001) docker     (123)     3286 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/glean/glean_x16_2xb8_cat.py
--rw-r--r--   0 runner    (1001) docker     (123)     3299 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/glean/glean_x16_2xb8_ffhq.py
--rw-r--r--   0 runner    (1001) docker     (123)      257 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/glean/glean_x8-fp16_2xb8_cat.py
--rw-r--r--   0 runner    (1001) docker     (123)     3282 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/glean/glean_x8_2xb8_cat.py
--rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/glean/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/global_local/
--rw-r--r--   0 runner    (1001) docker     (123)     1496 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/global_local/gl_8xb12_celeba-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1502 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/global_local/gl_8xb12_places-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1022 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/global_local/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/
--rw-r--r--   0 runner    (1001) docker     (123)      852 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)      858 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)      841 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)     1485 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1384 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1392 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)     2542 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/iconvsr/
--rw-r--r--   0 runner    (1001) docker     (123)      913 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_reds4.py
--rw-r--r--   0 runner    (1001) docker     (123)      960 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_vimeo90k-bd.py
--rw-r--r--   0 runner    (1001) docker     (123)      969 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_vimeo90k-bi.py
--rw-r--r--   0 runner    (1001) docker     (123)     3123 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/iconvsr/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/indexnet/
--rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/indexnet/indexnet_mobv2-dimaug_1xb16-78k_comp1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     3252 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/indexnet/indexnet_mobv2_1xb16-78k_comp1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1056 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/indexnet/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/inst_colorization/
--rw-r--r--   0 runner    (1001) docker     (123)     1523 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/inst_colorization/inst-colorizatioon_full_official_cocostuff-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)      726 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/inst_colorization/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/liif/
--rw-r--r--   0 runner    (1001) docker     (123)      994 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/liif/liif-edsr-norm_c64b16_1xb16-1000k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1084 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/liif/liif-rdn-norm_c64b16_1xb16-1000k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     4523 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/liif/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/lsgan/
--rw-r--r--   0 runner    (1001) docker     (123)     1615 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-3-1xb128-12Mimgs_celeba-cropped-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)     1268 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-4-1xb128-12Mimgs_lsun-bedroom-64x64.py
--rw-r--r--   0 runner    (1001) docker     (123)     1755 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-4-1xb64-10Mimgs_celeba-cropped-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1485 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/lsgan/lsgan_lsgan-archi_lr1e-4-1xb64-10Mimgs_lsun-bedroom-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     2052 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/lsgan/metafile.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/nafnet/
--rw-r--r--   0 runner    (1001) docker     (123)      957 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/nafnet/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     3458 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/nafnet/nafnet_c64eb11128mb1db1111_8xb8-lr1e-3-400k_gopro.py
--rw-r--r--   0 runner    (1001) docker     (123)     3480 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/nafnet/nafnet_c64eb2248mb12db2222_8xb8-lr1e-3-400k_sidd.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/partial_conv/
--rw-r--r--   0 runner    (1001) docker     (123)     1415 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/partial_conv/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1999 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/partial_conv/pconv_stage1_8xb12_places-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1998 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/partial_conv/pconv_stage1_8xb1_celeba-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     2065 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/partial_conv/pconv_stage2_4xb2_celeba-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     2061 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/partial_conv/pconv_stage2_4xb2_places-256x256.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/pggan/
--rw-r--r--   0 runner    (1001) docker     (123)     1309 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/pggan/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     3244 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/pggan/pggan_8xb4-12Mimg_celeba-hq-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     3043 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/pggan/pggan_8xb4-12Mimgs_celeba-cropped-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)      285 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/pggan/pggan_8xb4-12Mimgs_lsun-bedroom-128x128.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/pix2pix/
--rw-r--r--   0 runner    (1001) docker     (123)     2040 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/pix2pix/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2743 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-220kiters_aerial2maps.py
--rw-r--r--   0 runner    (1001) docker     (123)     2743 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-220kiters_maps2aerial.py
--rw-r--r--   0 runner    (1001) docker     (123)     2688 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-80kiters_facades.py
--rw-r--r--   0 runner    (1001) docker     (123)     3149 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_wo-jitter-flip-1xb4-190kiters_edges2shoes.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/
--rw-r--r--   0 runner    (1001) docker     (123)    12150 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2727 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-c_c2_8xb3-1100kiters_ffhq-256-512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2713 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-d_c2_8xb3-1100kiters_ffhq-256-512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2867 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-e_c2_8xb3-1100kiters_ffhq-256-512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2829 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c1_8xb2-1600kiters_ffhq-256-1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     2811 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c2_8xb3-1100kiters_ffhq-256-512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2800 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c2_8xb3-1100kiters_ffhq-256-896.py
--rw-r--r--   0 runner    (1001) docker     (123)     2887 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-g_c1_8xb3-1100kiters_ffhq-256-512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2771 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-h_c2_8xb3-1100kiters_ffhq-256-512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2757 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-i_c2_8xb3-1100kiters_ffhq-256-512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2911 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-j_c2_8xb3-1100kiters_ffhq-256-512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2885 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-k_c2_8xb3-1100kiters_ffhq-256-512.py
--rw-r--r--   0 runner    (1001) docker     (123)      594 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan-csg_bohemian.py
--rw-r--r--   0 runner    (1001) docker     (123)      585 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan-csg_fish.py
--rw-r--r--   0 runner    (1001) docker     (123)      419 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan_interp-pad_balloons.py
--rw-r--r--   0 runner    (1001) docker     (123)      435 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan_interp-pad_disc-nobn_balloons.py
--rw-r--r--   0 runner    (1001) docker     (123)      432 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan_interp-pad_disc-nobn_fish.py
--rw-r--r--   0 runner    (1001) docker     (123)      819 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim4_bohemian.py
--rw-r--r--   0 runner    (1001) docker     (123)      793 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim4_fish.py
--rw-r--r--   0 runner    (1001) docker     (123)      819 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim8_bohemian.py
--rw-r--r--   0 runner    (1001) docker     (123)     1889 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/stylegan2_c2_8xb3-1100kiters_ffhq-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     1889 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/stylegan2_c2_8xb3-1100kiters_ffhq-512x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/rdn/
--rw-r--r--   0 runner    (1001) docker     (123)     1884 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/rdn/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     3839 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/rdn/rdn_x2c64b16_1xb16-1000k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     3839 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/rdn/rdn_x3c64b16_1xb16-1000k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     3892 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/rdn/rdn_x4c64b16_1xb16-1000k_div2k.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/real_basicvsr/
--rw-r--r--   0 runner    (1001) docker     (123)     1160 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/real_basicvsr/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2298 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/real_basicvsr/realbasicvsr_c64b20-1x30x8_8xb1-lr5e-5-150k_reds.py
--rw-r--r--   0 runner    (1001) docker     (123)     9787 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/real_basicvsr/realbasicvsr_wogan-c64b20-2x30x8_8xb2-lr1e-4-300k_reds.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/real_esrgan/
--rw-r--r--   0 runner    (1001) docker     (123)     1137 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/real_esrgan/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2030 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/real_esrgan/realesrgan_c64b23g32_4xb12-lr1e-4-400k_df2k-ost.py
--rw-r--r--   0 runner    (1001) docker     (123)     7875 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/real_esrgan/realesrnet_c64b23g32_4xb12-lr2e-4-1000k_df2k-ost.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/
--rw-r--r--   0 runner    (1001) docker     (123)    11152 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma15.py
--rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma25.py
--rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma50.py
--rw-r--r--   0 runner    (1001) docker     (123)     1057 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma15.py
--rw-r--r--   0 runner    (1001) docker     (123)     1057 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma25.py
--rw-r--r--   0 runner    (1001) docker     (123)     1057 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma50.py
--rw-r--r--   0 runner    (1001) docker     (123)      550 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dpdd-dual.py
--rw-r--r--   0 runner    (1001) docker     (123)      816 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dpdd-single.py
--rw-r--r--   0 runner    (1001) docker     (123)      809 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_gopro.py
--rw-r--r--   0 runner    (1001) docker     (123)      803 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_rain13k.py
--rw-r--r--   0 runner    (1001) docker     (123)      805 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_sidd.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/
--rw-r--r--   0 runner    (1001) docker     (123)     3992 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)      956 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_128_cvt_studioGAN.py
--rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_cvt-studioGAN_cifar10-32x32.py
--rw-r--r--   0 runner    (1001) docker     (123)     1624 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_wReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py
--rw-r--r--   0 runner    (1001) docker     (123)     2471 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_woReLUinplace-Glr1e-4_Dlr4e-4_noaug-ndisc1-8xb32-bigGAN-sch_imagenet1k-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1604 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_woReLUinplace_Glr1e-4_Dlr4e-4_ndisc1-4xb64_imagenet1k-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1533 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_woReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/singan/
--rw-r--r--   0 runner    (1001) docker     (123)     1449 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/singan/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1209 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/singan/singan_balloons.py
--rw-r--r--   0 runner    (1001) docker     (123)      779 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/singan/singan_bohemian.py
--rw-r--r--   0 runner    (1001) docker     (123)     2494 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/singan/singan_fish.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/
--rw-r--r--   0 runner    (1001) docker     (123)     4133 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1081 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj-cvt-studioGAN_cifar10-32x32.py
--rw-r--r--   0 runner    (1001) docker     (123)      938 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj-cvt-studioGAN_imagenet1k-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1902 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj_wReLUinplace_Glr2e-4_Dlr5e-5_ndisc5-2xb128_imagenet1k-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1990 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj_wReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py
--rw-r--r--   0 runner    (1001) docker     (123)     1771 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj_woReLUinplace_Glr2e-4_Dlr5e-5_ndisc5-2xb128_imagenet1k-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     1857 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj_woReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/srcnn/
--rw-r--r--   0 runner    (1001) docker     (123)      797 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/srcnn/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     3850 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/srcnn/srcnn_x4k915_1xb16-1000k_div2k.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/srgan_resnet/
--rw-r--r--   0 runner    (1001) docker     (123)     1456 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/srgan_resnet/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     3728 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/srgan_resnet/msrresnet_x4c64b16_1xb16-1000k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1895 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/srgan_resnet/srgan_x4c64b16_1xb16-1000k_div2k.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/stable_diffusion/
--rw-r--r--   0 runner    (1001) docker     (123)      499 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/stable_diffusion/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1462 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/stable_diffusion/stable-diffusion_ddim_denoisingunet.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv1/
--rw-r--r--   0 runner    (1001) docker     (123)     1214 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv1/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1956 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv1/styleganv1_ffhq-1024x1024_8xb4-25Mimgs.py
--rw-r--r--   0 runner    (1001) docker     (123)     2143 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv1/styleganv1_ffhq-256x256_8xb4-25Mimgs.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/
--rw-r--r--   0 runner    (1001) docker     (123)     4439 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)      351 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2-PL-R1_8xb4-apex-fp16-no-scaler-800kiters_ffhq-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)      441 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2-PL-R1_8xb4-fp16-globalG-partialD-no-scaler-800kiters_ffhq-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)      427 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2-PL_8xb4-fp16-partial-GD-no-scaler-800kiters_ffhq-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     2471 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_ffhq-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     2440 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-cat-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     2443 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-church-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     2442 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-horse-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     2446 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4_ffhq-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     3279 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4_lsun-car-384x512.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/
--rw-r--r--   0 runner    (1001) docker     (123)     4485 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     3079 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-r_ada-gamma3.3_8xb4-fp16_metfaces-1024x1024.py
--rw-r--r--   0 runner    (1001) docker     (123)     1449 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4_ffhq-1024x1024.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1437 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4_ffhqu-256x256.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1508 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4x8_afhqv2-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     2954 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_ada-gamma6.6_8xb4-fp16_metfaces-1024x1024.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1334 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_afhqv2-512x512.py
--rw-r--r--   0 runner    (1001) docker     (123)     1326 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_ffhq-1024x1024.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     1383 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_ffhqu-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     2533 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_gamma2.0_8xb4-fp16-noaug_ffhq-256x256.py
--rw-r--r--   0 runner    (1001) docker     (123)     2329 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_gamma32.8_8xb4-fp16-noaug_ffhq-1024x1024.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/
--rw-r--r--   0 runner    (1001) docker     (123)    19414 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)      213 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_gan-x2s64w8d6e180_8xb4-lr1e-4-600k_df2k-ost.py
--rw-r--r--   0 runner    (1001) docker     (123)      210 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_gan-x4s64w8d6e180_8xb4-lr1e-4-600k_df2k-ost.py
--rw-r--r--   0 runner    (1001) docker     (123)      210 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_gan-x4s64w8d9e240_8xb4-lr1e-4-600k_df2k-ost.py
--rw-r--r--   0 runner    (1001) docker     (123)     1711 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_psnr-x2s64w8d6e180_8xb4-lr1e-4-600k_df2k-ost.py
--rw-r--r--   0 runner    (1001) docker     (123)      284 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_psnr-x4s64w8d6e180_8xb4-lr1e-4-600k_df2k-ost.py
--rw-r--r--   0 runner    (1001) docker     (123)      411 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_psnr-x4s64w8d9e240_8xb4-lr1e-4-600k_df2k-ost.py
--rw-r--r--   0 runner    (1001) docker     (123)     3744 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR10.py
--rw-r--r--   0 runner    (1001) docker     (123)      789 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR20.py
--rw-r--r--   0 runner    (1001) docker     (123)      789 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR30.py
--rw-r--r--   0 runner    (1001) docker     (123)      789 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR40.py
--rw-r--r--   0 runner    (1001) docker     (123)     3996 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR10.py
--rw-r--r--   0 runner    (1001) docker     (123)      787 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR20.py
--rw-r--r--   0 runner    (1001) docker     (123)      787 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR30.py
--rw-r--r--   0 runner    (1001) docker     (123)      787 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR40.py
--rw-r--r--   0 runner    (1001) docker     (123)     4206 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN15.py
--rw-r--r--   0 runner    (1001) docker     (123)      770 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN25.py
--rw-r--r--   0 runner    (1001) docker     (123)      770 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN50.py
--rw-r--r--   0 runner    (1001) docker     (123)     3978 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN15.py
--rw-r--r--   0 runner    (1001) docker     (123)      768 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN25.py
--rw-r--r--   0 runner    (1001) docker     (123)      768 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN50.py
--rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x2s48w8d6e180_8xb4-lr2e-4-500k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)      617 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x2s64w8d4e60_8xb4-lr2e-4-500k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1036 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x2s64w8d6e180_8xb4-lr2e-4-500k_df2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x3s48w8d6e180_8xb4-lr2e-4-500k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)      617 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x3s64w8d4e60_8xb4-lr2e-4-500k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1036 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x3s64w8d6e180_8xb4-lr2e-4-500k_df2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x4s48w8d6e180_8xb4-lr2e-4-500k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)      617 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x4s64w8d4e60_8xb4-lr2e-4-500k_div2k.py
--rw-r--r--   0 runner    (1001) docker     (123)     1036 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x4s64w8d6e180_8xb4-lr2e-4-500k_df2k.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tdan/
--rw-r--r--   0 runner    (1001) docker     (123)     2107 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tdan/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     3604 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tdan/tdan_x4_8xb16-lr1e-4-400k_vimeo90k-bd.py
--rw-r--r--   0 runner    (1001) docker     (123)      483 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tdan/tdan_x4_8xb16-lr1e-4-400k_vimeo90k-bi.py
--rw-r--r--   0 runner    (1001) docker     (123)      425 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tdan/tdan_x4ft_8xb16-lr5e-5-400k_vimeo90k-bi.py
--rw-r--r--   0 runner    (1001) docker     (123)      514 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tdan/tdan_x4ft_8xb16-lr5e-5-800k_vimeo90k-bd.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tof/
--rw-r--r--   0 runner    (1001) docker     (123)     3310 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tof/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)      951 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_spynet-chair-wobn_1xb1_vimeo90k-triplet.py
--rw-r--r--   0 runner    (1001) docker     (123)      951 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_spynet-kitti-wobn_1xb1_vimeo90k-triplet.py
--rw-r--r--   0 runner    (1001) docker     (123)      957 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_spynet-pytoflow-wobn_1xb1_vimeo90k-triplet.py
--rw-r--r--   0 runner    (1001) docker     (123)      965 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_spynet-sintel-wobn-clean_1xb1_vimeo90k-triplet.py
--rw-r--r--   0 runner    (1001) docker     (123)      965 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_spynet-sintel-wobn-final_1xb1_vimeo90k-triplet.py
--rw-r--r--   0 runner    (1001) docker     (123)     2036 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_x4_official_vimeo90k.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/ttsr/
--rw-r--r--   0 runner    (1001) docker     (123)      963 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/ttsr/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/ttsr/ttsr-gan_x4c64b16_1xb9-500k_CUFED.py
--rw-r--r--   0 runner    (1001) docker     (123)     6406 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/ttsr/ttsr-rec_x4c64b16_1xb9-200k_CUFED.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/wgan-gp/
--rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/wgan-gp/metafile.yml
--rw-r--r--   0 runner    (1001) docker     (123)      483 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/wgan-gp/wgangp_GN-GP-50_1xb64-160kiters_lsun-bedroom-128x128.py
--rw-r--r--   0 runner    (1001) docker     (123)     2030 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/configs/wgan-gp/wgangp_GN_1xb64-160kiters_celeba-cropped-128x128.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/
--rw-r--r--   0 runner    (1001) docker     (123)     1331 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/colorization_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     4489 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/conditional_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     4025 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/download_inference_resources.py
--rw-r--r--   0 runner    (1001) docker     (123)    13401 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/gradio-demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1398 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/inpainting_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1309 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/matting_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     4030 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/mmediting_inference_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     2196 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/restoration_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1996 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/restoration_face_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     3034 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/restoration_video_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     3477 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/singan_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1800 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/translation_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     2414 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/unconditional_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     2836 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/demo/video_interpolation_demo.py
--rw-r--r--   0 runner    (1001) docker     (123)     1603 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/model-index.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/analysis_tools/
--rw-r--r--   0 runner    (1001) docker     (123)     2247 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/analysis_tools/get_flops.py
--rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/analysis_tools/print_config.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      265 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/cpu_train.sh
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/bgm/
--rw-r--r--   0 runner    (1001) docker     (123)     4147 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/bgm/preprocess_bgm_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/comp1k/
--rwxr-xr-x   0 runner    (1001) docker     (123)      939 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/comp1k/check_extended_fg.py
--rw-r--r--   0 runner    (1001) docker     (123)    10643 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/comp1k/evaluate_comp1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     4265 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/comp1k/extend_fg.py
--rw-r--r--   0 runner    (1001) docker     (123)     1462 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/comp1k/filter_comp1k_anno.py
--rw-r--r--   0 runner    (1001) docker     (123)    10486 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/comp1k/preprocess_comp1k_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/df2k_ost/
--rw-r--r--   0 runner    (1001) docker     (123)    11576 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/df2k_ost/preprocess_df2k_ost_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/div2k/
--rw-r--r--   0 runner    (1001) docker     (123)    13724 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/div2k/preprocess_div2k_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/reds/
--rw-r--r--   0 runner    (1001) docker     (123)     6659 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/reds/crop_sub_images.py
--rw-r--r--   0 runner    (1001) docker     (123)    11192 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/reds/preprocess_reds_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/vimeo90k/
--rw-r--r--   0 runner    (1001) docker     (123)     6298 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/vimeo90k/preprocess_vimeo90k_dataset.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      479 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dist_test.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)      442 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/dist_train.sh
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/gui/
--rw-r--r--   0 runner    (1001) docker     (123)    15602 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/gui/component.py
--rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/gui/gui.py
--rw-r--r--   0 runner    (1001) docker     (123)     3876 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/gui/page_general.py
--rw-r--r--   0 runner    (1001) docker     (123)    34328 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/gui/page_sr.py
--rw-r--r--   0 runner    (1001) docker     (123)      530 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/gui/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/model_converters/
--rw-r--r--   0 runner    (1001) docker     (123)     1256 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/model_converters/publish_model.py
--rw-r--r--   0 runner    (1001) docker     (123)    10494 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/model_converters/pytorch2onnx.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      566 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/slurm_test.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)      622 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/slurm_train.sh
--rw-r--r--   0 runner    (1001) docker     (123)     2868 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/test.py
--rw-r--r--   0 runner    (1001) docker     (123)     4176 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/.mim/tools/train.py
--rw-r--r--   0 runner    (1001) docker     (123)     1445 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/apis/
--rw-r--r--   0 runner    (1001) docker     (123)       83 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/
--rw-r--r--   0 runner    (1001) docker     (123)     1181 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8600 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/base_mmedit_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)     2773 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/colorization_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)     2789 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/conditional_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)    13415 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/eg3d_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)    30798 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/inference_functions.py
--rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/inpainting_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)     3988 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/matting_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)     4288 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/mmedit_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)     4155 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/restoration_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)     2324 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/text2image_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)     2768 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/translation_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)     2751 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/unconditional_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)     7644 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/video_interpolation_inferencer.py
--rw-r--r--   0 runner    (1001) docker     (123)     7304 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/apis/inferencers/video_restoration_inferencer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)      838 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11561 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/basic_conditional_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)    12825 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/basic_frames_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     8711 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/basic_image_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)    29271 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/categories.py
--rw-r--r--   0 runner    (1001) docker     (123)     6669 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/cifar10_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     5211 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/comp1k_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)    11864 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/data_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     7942 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/grow_scale_image_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     1579 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/imagenet_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     4171 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/mscoco_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     2765 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/paired_image_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     4773 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/singan_dataset.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/
--rw-r--r--   0 runner    (1001) docker     (123)     2985 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9720 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/alpha.py
--rw-r--r--   0 runner    (1001) docker     (123)     2582 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/aug_frames.py
--rw-r--r--   0 runner    (1001) docker     (123)    21020 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/aug_pixel.py
--rw-r--r--   0 runner    (1001) docker     (123)    15752 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/aug_shape.py
--rw-r--r--   0 runner    (1001) docker     (123)    20398 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/blur_kernels.py
--rw-r--r--   0 runner    (1001) docker     (123)    37685 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/crop.py
--rw-r--r--   0 runner    (1001) docker     (123)    11492 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/fgbg.py
--rw-r--r--   0 runner    (1001) docker     (123)     3906 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/formatting.py
--rw-r--r--   0 runner    (1001) docker     (123)     8534 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/generate_assistant.py
--rw-r--r--   0 runner    (1001) docker     (123)     9612 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/generate_frame_indices.py
--rw-r--r--   0 runner    (1001) docker     (123)     2320 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/get_masked_image.py
--rw-r--r--   0 runner    (1001) docker     (123)    18915 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/loading.py
--rw-r--r--   0 runner    (1001) docker     (123)     9543 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/matlab_like_resize.py
--rw-r--r--   0 runner    (1001) docker     (123)     3595 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/normalization.py
--rw-r--r--   0 runner    (1001) docker     (123)    20688 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/random_degradations.py
--rw-r--r--   0 runner    (1001) docker     (123)     5061 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/random_down_sampling.py
--rw-r--r--   0 runner    (1001) docker     (123)     9795 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/trimap.py
--rw-r--r--   0 runner    (1001) docker     (123)     2755 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/transforms/values.py
--rw-r--r--   0 runner    (1001) docker     (123)     4910 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/datasets/unpaired_image_dataset.py
--rw-r--r--   0 runner    (1001) docker     (123)     8886 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/edit.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/engine/
--rw-r--r--   0 runner    (1001) docker     (123)      223 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/engine/hooks/
--rw-r--r--   0 runner    (1001) docker     (123)      570 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/hooks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7318 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/hooks/ema.py
--rw-r--r--   0 runner    (1001) docker     (123)     3341 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/hooks/iter_time_hook.py
--rw-r--r--   0 runner    (1001) docker     (123)     3705 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/hooks/pggan_fetch_data_hook.py
--rw-r--r--   0 runner    (1001) docker     (123)     4941 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/hooks/pickle_data_hook.py
--rw-r--r--   0 runner    (1001) docker     (123)     5050 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/hooks/reduce_lr_scheduler_hook.py
--rw-r--r--   0 runner    (1001) docker     (123)    18445 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/hooks/visualization_hook.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/engine/optimizers/
--rw-r--r--   0 runner    (1001) docker     (123)      384 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/optimizers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2783 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/optimizers/multi_optimizer_constructor.py
--rw-r--r--   0 runner    (1001) docker     (123)     5209 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/optimizers/pggan_optimizer_constructor.py
--rw-r--r--   0 runner    (1001) docker     (123)     3650 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/optimizers/singan_optimizer_constructor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/engine/runner/
--rw-r--r--   0 runner    (1001) docker     (123)      205 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/runner/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    20291 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/runner/edit_loops.py
--rw-r--r--   0 runner    (1001) docker     (123)     7528 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/runner/log_processor.py
--rw-r--r--   0 runner    (1001) docker     (123)     2612 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/runner/loop_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/engine/schedulers/
--rw-r--r--   0 runner    (1001) docker     (123)      209 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/schedulers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1714 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/schedulers/linear_lr_scheduler_with_interval.py
--rw-r--r--   0 runner    (1001) docker     (123)     6441 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/engine/schedulers/reduce_lr_scheduler.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/evaluation/
--rw-r--r--   0 runner    (1001) docker     (123)     1053 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7628 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/evaluator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/evaluation/functional/
--rw-r--r--   0 runner    (1001) docker     (123)      423 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/functional/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12348 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/functional/fid_inception.py
--rw-r--r--   0 runner    (1001) docker     (123)     2347 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/functional/gaussian_funcs.py
--rw-r--r--   0 runner    (1001) docker     (123)    22211 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/functional/inception_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/
--rw-r--r--   0 runner    (1001) docker     (123)     1117 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14859 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/base_gen_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)     5033 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/base_sample_wise_metric.py
--rw-r--r--   0 runner    (1001) docker     (123)     4476 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/connectivity_error.py
--rw-r--r--   0 runner    (1001) docker     (123)     6819 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/equivariance.py
--rw-r--r--   0 runner    (1001) docker     (123)    11715 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/fid.py
--rw-r--r--   0 runner    (1001) docker     (123)     3403 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/gradient_error.py
--rw-r--r--   0 runner    (1001) docker     (123)    15845 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/inception_score.py
--rw-r--r--   0 runner    (1001) docker     (123)     1857 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/mae.py
--rw-r--r--   0 runner    (1001) docker     (123)     2627 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/matting_mse.py
--rw-r--r--   0 runner    (1001) docker     (123)     5061 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/metrics_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    13575 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/ms_ssim.py
--rw-r--r--   0 runner    (1001) docker     (123)     1712 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/mse.py
--rw-r--r--   0 runner    (1001) docker     (123)    11566 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/niqe.py
--rw-r--r--   0 runner    (1001) docker     (123)    11850 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/niqe_pris_params.npz
--rw-r--r--   0 runner    (1001) docker     (123)    11870 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/ppl.py
--rw-r--r--   0 runner    (1001) docker     (123)    11443 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/precision_and_recall.py
--rw-r--r--   0 runner    (1001) docker     (123)     4411 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/psnr.py
--rw-r--r--   0 runner    (1001) docker     (123)     2616 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/sad.py
--rw-r--r--   0 runner    (1001) docker     (123)     4307 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/snr.py
--rw-r--r--   0 runner    (1001) docker     (123)     5943 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/ssim.py
--rw-r--r--   0 runner    (1001) docker     (123)    14289 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/evaluation/metrics/swd.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/
--rw-r--r--   0 runner    (1001) docker     (123)      637 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/
--rw-r--r--   0 runner    (1001) docker     (123)     1244 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      902 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/all_gather_layer.py
--rw-r--r--   0 runner    (1001) docker     (123)     4856 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/aspp.py
--rw-r--r--   0 runner    (1001) docker     (123)      186 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/conv.py
--rw-r--r--   0 runner    (1001) docker     (123)    10449 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/conv2d_gradfix.py
--rw-r--r--   0 runner    (1001) docker     (123)      663 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/downsample.py
--rw-r--r--   0 runner    (1001) docker     (123)     3726 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/ensemble.py
--rw-r--r--   0 runner    (1001) docker     (123)     2652 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/gated_conv_module.py
--rw-r--r--   0 runner    (1001) docker     (123)     1227 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/img_normalize.py
--rw-r--r--   0 runner    (1001) docker     (123)     3530 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/linear_module.py
--rw-r--r--   0 runner    (1001) docker     (123)     6819 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/multi_layer_disc.py
--rw-r--r--   0 runner    (1001) docker     (123)     4942 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/patch_disc.py
--rw-r--r--   0 runner    (1001) docker     (123)    18813 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/resnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     4241 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/separable_conv_module.py
--rw-r--r--   0 runner    (1001) docker     (123)     1107 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/simple_encoder_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     4357 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/smpatch_disc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2987 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/sr_backbone.py
--rw-r--r--   0 runner    (1001) docker     (123)     1572 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/upsample.py
--rw-r--r--   0 runner    (1001) docker     (123)     3909 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_archs/vgg.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/base_models/
--rw-r--r--   0 runner    (1001) docker     (123)      709 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_models/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15297 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_models/average_model.py
--rw-r--r--   0 runner    (1001) docker     (123)    13583 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_models/base_conditional_gan.py
--rw-r--r--   0 runner    (1001) docker     (123)     8338 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_models/base_edit_model.py
--rw-r--r--   0 runner    (1001) docker     (123)    25575 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_models/base_gan.py
--rw-r--r--   0 runner    (1001) docker     (123)    10217 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_models/base_mattor.py
--rw-r--r--   0 runner    (1001) docker     (123)     7790 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_models/base_translation_model.py
--rw-r--r--   0 runner    (1001) docker     (123)     3807 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_models/basic_interpolator.py
--rw-r--r--   0 runner    (1001) docker     (123)    17990 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_models/one_stage.py
--rw-r--r--   0 runner    (1001) docker     (123)    14493 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/base_models/two_stage.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/data_preprocessors/
--rw-r--r--   0 runner    (1001) docker     (123)      215 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/data_preprocessors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    37243 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/data_preprocessors/edit_data_preprocessor.py
--rw-r--r--   0 runner    (1001) docker     (123)     7245 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/data_preprocessors/mattor_preprocessor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/
--rw-r--r--   0 runner    (1001) docker     (123)     4561 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/aotgan/
--rw-r--r--   0 runner    (1001) docker     (123)      349 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/aotgan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2200 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/aotgan/aot_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1909 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/aotgan/aot_encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1022 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/aotgan/aot_encoder_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     7407 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/aotgan/aot_inpaintor.py
--rw-r--r--   0 runner    (1001) docker     (123)     3808 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/aotgan/aot_neck.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/arcface/
--rw-r--r--   0 runner    (1001) docker     (123)      108 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/arcface/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6054 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/arcface/arcface_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)     2668 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/arcface/id_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     3883 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/arcface/model_irse.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/basicvsr/
--rw-r--r--   0 runner    (1001) docker     (123)      156 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/basicvsr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5354 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/basicvsr/basicvsr.py
--rw-r--r--   0 runner    (1001) docker     (123)    13764 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/basicvsr/basicvsr_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/basicvsr_plusplus_net/
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/basicvsr_plusplus_net/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16096 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/basicvsr_plusplus_net/basicvsr_plusplus_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/biggan/
--rw-r--r--   0 runner    (1001) docker     (123)      942 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/biggan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6665 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan.py
--rw-r--r--   0 runner    (1001) docker     (123)    12960 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_deep_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)    20674 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_deep_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    12216 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)    19952 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    30009 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)     9438 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_snmodule.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/cain/
--rw-r--r--   0 runner    (1001) docker     (123)      143 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/cain/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1870 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/cain/cain.py
--rw-r--r--   0 runner    (1001) docker     (123)    10627 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/cain/cain_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/cyclegan/
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/cyclegan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11333 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/cyclegan/cyclegan.py
--rw-r--r--   0 runner    (1001) docker     (123)     5638 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/cyclegan/cyclegan_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)     4709 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/cyclegan/cyclegan_modules.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/dcgan/
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/dcgan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4344 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/dcgan/dcgan.py
--rw-r--r--   0 runner    (1001) docker     (123)     5001 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/dcgan/dcgan_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)     7623 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/dcgan/dcgan_generator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/ddim/
--rw-r--r--   0 runner    (1001) docker     (123)      119 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ddim/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9668 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ddim/ddim_scheduler.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/ddpm/
--rw-r--r--   0 runner    (1001) docker     (123)      178 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ddpm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    21369 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ddpm/attention.py
--rw-r--r--   0 runner    (1001) docker     (123)     9631 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ddpm/ddpm_scheduler.py
--rw-r--r--   0 runner    (1001) docker     (123)    52869 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ddpm/denoising_unet.py
--rw-r--r--   0 runner    (1001) docker     (123)     2975 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ddpm/embeddings.py
--rw-r--r--   0 runner    (1001) docker     (123)     8588 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ddpm/res_blocks.py
--rw-r--r--   0 runner    (1001) docker     (123)    20328 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ddpm/unet_blocks.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/
--rw-r--r--   0 runner    (1001) docker     (123)      595 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15253 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/contextual_attention.py
--rw-r--r--   0 runner    (1001) docker     (123)     2568 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/contextual_attention_neck.py
--rw-r--r--   0 runner    (1001) docker     (123)     3559 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/deepfill_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1859 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/deepfill_disc.py
--rw-r--r--   0 runner    (1001) docker     (123)     2823 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/deepfill_encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     2781 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/deepfill_refiner.py
--rw-r--r--   0 runner    (1001) docker     (123)    15725 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/deepfillv1.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv2/
--rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3013 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/deepfillv2/two_stage_encoder_decoder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/dic/
--rw-r--r--   0 runner    (1001) docker     (123)      467 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/dic/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5298 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/dic/dic.py
--rw-r--r--   0 runner    (1001) docker     (123)    14735 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/dic/dic_net.py
--rw-r--r--   0 runner    (1001) docker     (123)     7207 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/dic/feedback_hour_glass.py
--rw-r--r--   0 runner    (1001) docker     (123)     4188 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/dic/light_cnn.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/dim/
--rw-r--r--   0 runner    (1001) docker     (123)       88 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/dim/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7522 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/dim/dim.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/disco_diffusion/
--rw-r--r--   0 runner    (1001) docker     (123)      356 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/disco_diffusion/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5226 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/disco_diffusion/clip_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)     9608 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/disco_diffusion/disco.py
--rw-r--r--   0 runner    (1001) docker     (123)    19692 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/disco_diffusion/guider.py
--rw-r--r--   0 runner    (1001) docker     (123)     5328 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/disco_diffusion/secondary_model.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/duf/
--rw-r--r--   0 runner    (1001) docker     (123)      128 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/duf/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2714 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/duf/duf.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/edsr/
--rw-r--r--   0 runner    (1001) docker     (123)      101 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/edsr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3795 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/edsr/edsr_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/edvr/
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/edvr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2640 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/edvr/edvr.py
--rw-r--r--   0 runner    (1001) docker     (123)    18573 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/edvr/edvr_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/eg3d/
--rw-r--r--   0 runner    (1001) docker     (123)      324 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/eg3d/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    20954 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/eg3d/camera.py
--rw-r--r--   0 runner    (1001) docker     (123)     4464 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/eg3d/dual_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)    13867 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/eg3d/eg3d.py
--rw-r--r--   0 runner    (1001) docker     (123)    10550 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/eg3d/eg3d_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    12466 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/eg3d/eg3d_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)     6606 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/eg3d/eg3d_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2674 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/eg3d/ray_sampler.py
--rw-r--r--   0 runner    (1001) docker     (123)    24027 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/eg3d/renderer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/esrgan/
--rw-r--r--   0 runner    (1001) docker     (123)      149 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/esrgan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4262 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/esrgan/esrgan.py
--rw-r--r--   0 runner    (1001) docker     (123)     6570 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/esrgan/rrdb_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/fba/
--rw-r--r--   0 runner    (1001) docker     (123)      183 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/fba/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7069 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/fba/fba_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1233 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/fba/fba_encoder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/flavr/
--rw-r--r--   0 runner    (1001) docker     (123)      149 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/flavr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2383 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/flavr/flavr.py
--rw-r--r--   0 runner    (1001) docker     (123)    18190 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/flavr/flavr_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/gca/
--rw-r--r--   0 runner    (1001) docker     (123)      371 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/gca/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3044 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/gca/gca.py
--rw-r--r--   0 runner    (1001) docker     (123)    15490 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/gca/gca_module.py
--rw-r--r--   0 runner    (1001) docker     (123)    14313 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/gca/resgca_dec.py
--rw-r--r--   0 runner    (1001) docker     (123)    20745 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/gca/resgca_enc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/ggan/
--rw-r--r--   0 runner    (1001) docker     (123)       91 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ggan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4304 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ggan/ggan.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/glean/
--rw-r--r--   0 runner    (1001) docker     (123)      125 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/glean/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12606 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/glean/glean_styleganv2.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/global_local/
--rw-r--r--   0 runner    (1001) docker     (123)      384 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/global_local/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3091 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     2057 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_dilation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1880 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_disc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1581 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1458 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_encoder_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     9915 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_inpaintor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/guided_diffusion/
--rw-r--r--   0 runner    (1001) docker     (123)      185 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/guided_diffusion/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12102 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/guided_diffusion/adm.py
--rw-r--r--   0 runner    (1001) docker     (123)    22206 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/guided_diffusion/classifier.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/iconvsr/
--rw-r--r--   0 runner    (1001) docker     (123)      110 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/iconvsr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14816 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/iconvsr/iconvsr_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/indexnet/
--rw-r--r--   0 runner    (1001) docker     (123)      398 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/indexnet/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3297 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/indexnet/indexnet.py
--rw-r--r--   0 runner    (1001) docker     (123)     5554 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/indexnet/indexnet_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)    19093 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/indexnet/indexnet_encoder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/
--rw-r--r--   0 runner    (1001) docker     (123)      255 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9786 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/color_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     9754 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/colorization_net.py
--rw-r--r--   0 runner    (1001) docker     (123)    11231 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/fusion_net.py
--rw-r--r--   0 runner    (1001) docker     (123)     9600 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/inst_colorization.py
--rw-r--r--   0 runner    (1001) docker     (123)     4859 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/weight_layer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/liif/
--rw-r--r--   0 runner    (1001) docker     (123)      235 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/liif/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2584 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/liif/liif.py
--rw-r--r--   0 runner    (1001) docker     (123)    10133 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/liif/liif_net.py
--rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/liif/mlp_refiner.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/lsgan/
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/lsgan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4392 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/lsgan/lsgan.py
--rw-r--r--   0 runner    (1001) docker     (123)     4402 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/lsgan/lsgan_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)     7364 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/lsgan/lsgan_generator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/mspie/
--rw-r--r--   0 runner    (1001) docker     (123)      566 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/mspie/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8923 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/mspie/mspie_stylegan2.py
--rw-r--r--   0 runner    (1001) docker     (123)     3117 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/mspie/mspie_stylegan2_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)    19309 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/mspie/mspie_stylegan2_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    11250 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/mspie/mspie_stylegan2_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)     2294 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/mspie/pe_singan.py
--rw-r--r--   0 runner    (1001) docker     (123)     9673 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/mspie/pe_singan_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)     8872 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/mspie/positional_encoding.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/nafnet/
--rw-r--r--   0 runner    (1001) docker     (123)      242 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/nafnet/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5062 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/nafnet/naf_avgpool2d.py
--rw-r--r--   0 runner    (1001) docker     (123)     1812 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/nafnet/naf_layerNorm2d.py
--rw-r--r--   0 runner    (1001) docker     (123)     8372 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/nafnet/nafbaseline_net.py
--rw-r--r--   0 runner    (1001) docker     (123)     8539 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/nafnet/nafnet_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/pconv/
--rw-r--r--   0 runner    (1001) docker     (123)      460 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pconv/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3645 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pconv/mask_conv_module.py
--rw-r--r--   0 runner    (1001) docker     (123)     3603 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pconv/partial_conv.py
--rw-r--r--   0 runner    (1001) docker     (123)     3631 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pconv/pconv_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     4325 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pconv/pconv_encoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1024 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pconv/pconv_encoder_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     2823 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pconv/pconv_inpaintor.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/pggan/
--rw-r--r--   0 runner    (1001) docker     (123)      774 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pggan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    20707 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pggan/pggan.py
--rw-r--r--   0 runner    (1001) docker     (123)     9244 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pggan/pggan_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)    10398 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pggan/pggan_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    19722 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pggan/pggan_modules.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/pix2pix/
--rw-r--r--   0 runner    (1001) docker     (123)      162 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pix2pix/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9137 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pix2pix/pix2pix.py
--rw-r--r--   0 runner    (1001) docker     (123)     4785 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pix2pix/pix2pix_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)     4255 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/pix2pix/pix2pix_modules.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/plain/
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/plain/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8757 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/plain/plain_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)     1867 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/plain/plain_refiner.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/rdn/
--rw-r--r--   0 runner    (1001) docker     (123)      110 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/rdn/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5708 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/rdn/rdn_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/real_basicvsr/
--rw-r--r--   0 runner    (1001) docker     (123)      182 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/real_basicvsr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6509 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/real_basicvsr/real_basicvsr.py
--rw-r--r--   0 runner    (1001) docker     (123)     3841 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/real_basicvsr/real_basicvsr_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/real_esrgan/
--rw-r--r--   0 runner    (1001) docker     (123)      215 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/real_esrgan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7314 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/real_esrgan/real_esrgan.py
--rw-r--r--   0 runner    (1001) docker     (123)     3140 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/real_esrgan/unet_disc.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/restormer/
--rw-r--r--   0 runner    (1001) docker     (123)      110 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/restormer/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    17236 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/restormer/restormer_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/sagan/
--rw-r--r--   0 runner    (1001) docker     (123)      420 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/sagan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6964 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/sagan/sagan.py
--rw-r--r--   0 runner    (1001) docker     (123)    17462 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/sagan/sagan_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)    20851 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/sagan/sagan_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    25894 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/sagan/sagan_modules.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/singan/
--rw-r--r--   0 runner    (1001) docker     (123)      285 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/singan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    28167 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/singan/singan.py
--rw-r--r--   0 runner    (1001) docker     (123)     3244 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/singan/singan_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)     7217 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/singan/singan_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)     8103 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/singan/singan_modules.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/srcnn/
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/srcnn/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2462 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/srcnn/srcnn_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/srgan/
--rw-r--r--   0 runner    (1001) docker     (123)      208 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/srgan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3663 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/srgan/modified_vgg.py
--rw-r--r--   0 runner    (1001) docker     (123)     3690 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/srgan/sr_resnet.py
--rw-r--r--   0 runner    (1001) docker     (123)    10754 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/srgan/srgan.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/stable_diffusion/
--rw-r--r--   0 runner    (1001) docker     (123)      125 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stable_diffusion/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7641 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stable_diffusion/clip_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)    20808 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stable_diffusion/stable_diffusion.py
--rw-r--r--   0 runner    (1001) docker     (123)    34271 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stable_diffusion/vae.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/
--rw-r--r--   0 runner    (1001) docker     (123)      591 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6577 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/stylegan1.py
--rw-r--r--   0 runner    (1001) docker     (123)     5267 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/stylegan1_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)    14053 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/stylegan1_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    12342 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/stylegan1_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)     2395 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/stylegan_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/
--rw-r--r--   0 runner    (1001) docker     (123)      584 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/ada/
--rw-r--r--   0 runner    (1001) docker     (123)       48 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/ada/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    32592 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/ada/augment.py
--rw-r--r--   0 runner    (1001) docker     (123)     3439 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/ada/grid_sample_gradfix.py
--rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/ada/misc.py
--rw-r--r--   0 runner    (1001) docker     (123)     7074 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/ada/upfirdn2d.py
--rw-r--r--   0 runner    (1001) docker     (123)    14184 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/stylegan2.py
--rw-r--r--   0 runner    (1001) docker     (123)    13479 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/stylegan2_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)    23415 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/stylegan2_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    25746 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/stylegan2_modules.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/
--rw-r--r--   0 runner    (1001) docker     (123)      339 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10154 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3.py
--rw-r--r--   0 runner    (1001) docker     (123)     8129 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)    28034 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_modules.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_ops/
--rw-r--r--   0 runner    (1001) docker     (123)      514 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_ops/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6725 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_ops/custom_ops.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_ops/ops/
--rw-r--r--   0 runner    (1001) docker     (123)      448 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_ops/ops/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10305 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_ops/ops/bias_act.py
--rw-r--r--   0 runner    (1001) docker     (123)    14178 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_ops/ops/filtered_lrelu.py
--rw-r--r--   0 runner    (1001) docker     (123)    16743 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_ops/ops/upfirdn2d.py
--rw-r--r--   0 runner    (1001) docker     (123)     6022 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/swinir/
--rw-r--r--   0 runner    (1001) docker     (123)      107 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/swinir/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4845 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/swinir/swinir_modules.py
--rw-r--r--   0 runner    (1001) docker     (123)    12021 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/swinir/swinir_net.py
--rw-r--r--   0 runner    (1001) docker     (123)    20750 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/swinir/swinir_rstb.py
--rw-r--r--   0 runner    (1001) docker     (123)     2695 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/swinir/swinir_utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/tdan/
--rw-r--r--   0 runner    (1001) docker     (123)      132 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/tdan/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3256 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/tdan/tdan.py
--rw-r--r--   0 runner    (1001) docker     (123)     6089 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/tdan/tdan_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/tof/
--rw-r--r--   0 runner    (1001) docker     (123)      196 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/tof/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7806 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/tof/tof_vfi_net.py
--rw-r--r--   0 runner    (1001) docker     (123)     6438 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/tof/tof_vsr_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/ttsr/
--rw-r--r--   0 runner    (1001) docker     (123)      316 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ttsr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2731 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ttsr/lte.py
--rw-r--r--   0 runner    (1001) docker     (123)     3871 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ttsr/search_transformer.py
--rw-r--r--   0 runner    (1001) docker     (123)     7615 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ttsr/ttsr.py
--rw-r--r--   0 runner    (1001) docker     (123)     1566 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ttsr/ttsr_disc.py
--rw-r--r--   0 runner    (1001) docker     (123)    13928 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/ttsr/ttsr_net.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/editors/wgan_gp/
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/wgan_gp/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3965 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/wgan_gp/wgan_discriminator.py
--rw-r--r--   0 runner    (1001) docker     (123)     5593 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/wgan_gp/wgan_generator.py
--rw-r--r--   0 runner    (1001) docker     (123)     4761 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/wgan_gp/wgan_gp.py
--rw-r--r--   0 runner    (1001) docker     (123)     6765 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/editors/wgan_gp/wgan_gp_module.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/losses/
--rw-r--r--   0 runner    (1001) docker     (123)     1770 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4390 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/clip_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     7482 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/composition_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     2058 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/face_id_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     3260 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/feature_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)    21058 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/gan_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     2181 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/gradient_loss.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/
--rw-r--r--   0 runner    (1001) docker     (123)      625 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4124 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/clip_loss_comps.py
--rw-r--r--   0 runner    (1001) docker     (123)    16741 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/disc_auxiliary_loss_comps.py
--rw-r--r--   0 runner    (1001) docker     (123)     4192 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/face_id_loss_comps.py
--rw-r--r--   0 runner    (1001) docker     (123)     4173 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/gan_loss_comps.py
--rw-r--r--   0 runner    (1001) docker     (123)     7309 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/gen_auxiliary_loss_comps.py
--rw-r--r--   0 runner    (1001) docker     (123)     4135 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/loss_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (123)    10892 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/perceptual_loss.py
--rw-r--r--   0 runner    (1001) docker     (123)     9690 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/losses/pixelwise_loss.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/models/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      814 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4450 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/utils/bbox_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      803 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/utils/diffusion_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2333 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/utils/flow_warp.py
--rw-r--r--   0 runner    (1001) docker     (123)     8571 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/utils/model_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     6327 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/utils/sampling_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/models/utils/tensor_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     6812 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/registry.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/structures/
--rw-r--r--   0 runner    (1001) docker     (123)      123 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/structures/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12410 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/structures/edit_data_sample.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/utils/
--rw-r--r--   0 runner    (1001) docker     (123)     1208 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      561 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/utils/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     7445 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/utils/img_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3093 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/utils/io_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      644 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/utils/logger.py
--rw-r--r--   0 runner    (1001) docker     (123)     4949 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/utils/sampler.py
--rw-r--r--   0 runner    (1001) docker     (123)     2409 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/utils/setup_env.py
--rw-r--r--   0 runner    (1001) docker     (123)    18301 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/utils/trans_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)      463 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/utils/typing.py
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit/visualization/
--rw-r--r--   0 runner    (1001) docker     (123)      427 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/visualization/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4988 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/visualization/concat_visualizer.py
--rw-r--r--   0 runner    (1001) docker     (123)    12566 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/visualization/gen_visualizer.py
--rw-r--r--   0 runner    (1001) docker     (123)    17165 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/mmedit/visualization/vis_backend.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    22057 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    42233 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      673 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/mmedit.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/requirements/
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/requirements/docs.txt
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/requirements/mminstall.txt
--rw-r--r--   0 runner    (1001) docker     (123)      167 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/requirements/optional.txt
--rw-r--r--   0 runner    (1001) docker     (123)      135 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/requirements/readthedocs.txt
--rw-r--r--   0 runner    (1001) docker     (123)      482 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/requirements/runtime.txt
--rw-r--r--   0 runner    (1001) docker     (123)      262 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/requirements/tests.txt
--rw-r--r--   0 runner    (1001) docker     (123)      657 2023-03-03 07:44:39.000000 mmedit-1.0.0rc6/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     9500 2023-03-03 07:44:16.000000 mmedit-1.0.0rc6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/
+-rw-r--r--   0 runner    (1001) docker     (123)      281 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    22042 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    17763 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)     5631 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/basicvsr_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1080 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/celeba.py
+-rw-r--r--   0 runner    (1001) docker     (123)      696 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/cifar10_noaug.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1025 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/cifar10_nopad.py
+-rw-r--r--   0 runner    (1001) docker     (123)      925 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/comp1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2851 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/deblurring-defocus_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2859 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/deblurring-motion_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1736 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/decompression_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2931 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/denoising-gaussian_color_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2403 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/denoising-gaussian_gray_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1570 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/denoising-real_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3583 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/deraining_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1254 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/ffhq_flip.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1184 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/grow_scale_imgs_ffhq_styleganv1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1390 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/imagenet_128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1395 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/imagenet_256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1392 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/imagenet_512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1386 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/imagenet_64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1329 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/imagenet_noaug_128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2833 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/liif_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1170 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/lsun_stylegan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2938 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/paired_imgs_256x256_crop.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1229 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/places.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2588 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/sisr_x2_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2537 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/sisr_x3_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2537 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/sisr_x4_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3767 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/tdan_test_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1176 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1137 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1216 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_flip_512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1283 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_flip_lanczos_resize_256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3154 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/unpaired_imgs_256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/default_runtime.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2047 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/gen_default_runtime.py
+-rw-r--r--   0 runner    (1001) docker     (123)      964 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/inpaint_default_runtime.py
+-rw-r--r--   0 runner    (1001) docker     (123)      989 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/matting_default_runtime.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/
+-rw-r--r--   0 runner    (1001) docker     (123)      783 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_cyclegan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3210 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_deepfillv1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3261 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_deepfillv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3226 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_edvr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_gl.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1436 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_glean.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3533 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_liif.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_pconv.py
+-rw-r--r--   0 runner    (1001) docker     (123)      817 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_pix2pix.py
+-rw-r--r--   0 runner    (1001) docker     (123)      279 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_styleganv1.py
+-rw-r--r--   0 runner    (1001) docker     (123)      801 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_styleganv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      846 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_styleganv3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2890 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_tof.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/biggan/
+-rw-r--r--   0 runner    (1001) docker     (123)      796 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/biggan/base_biggan_128x128.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/dcgan/
+-rw-r--r--   0 runner    (1001) docker     (123)      353 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/dcgan/base_dcgan_128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      340 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/dcgan/base_dcgan_64x64.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/sagan/
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/sagan/base_sagan_128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      671 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/sagan/base_sagan_32x32.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/sngan_proj/
+-rw-r--r--   0 runner    (1001) docker     (123)      330 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/sngan_proj/base_sngan_proj_128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      328 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/sngan_proj/base_sngan_proj_32x32.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/aot_gan/
+-rw-r--r--   0 runner    (1001) docker     (123)     3876 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/aot_gan/aot-gan_smpgan_4xb4_places-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      655 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/aot_gan/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr/
+-rw-r--r--   0 runner    (1001) docker     (123)     3586 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr/basicvsr_2xb4_reds4.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2564 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr/basicvsr_2xb4_vimeo90k-bd.py
+-rw-r--r--   0 runner    (1001) docker     (123)      425 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr/basicvsr_2xb4_vimeo90k-bi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3143 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/
+-rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-decompress-track1.py
+-rw-r--r--   0 runner    (1001) docker     (123)      384 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-decompress-track2.py
+-rw-r--r--   0 runner    (1001) docker     (123)      384 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-decompress-track3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1788 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-vsr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1278 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_4xb2-300k_vimeo90k-bd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1278 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_4xb2-300k_vimeo90k-bi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1367 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_8xb1-600k_reds4.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5065 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/
+-rw-r--r--   0 runner    (1001) docker     (123)     1561 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face-rgb_imagenet1k-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1780 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face_rgb_imagenet1k-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1780 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face_rgb_imagenet1k-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2312 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan_2xb25-500kiters_cifar10-32x32.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1706 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan_ajbrock-sn_8xb32-1500kiters_imagenet1k-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1550 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan_cvt-BigGAN-PyTorch-rgb_imagenet1k-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2818 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/cain/
+-rw-r--r--   0 runner    (1001) docker     (123)     4202 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/cain/cain_g1b32_1xb5_vimeo90k-triplet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      632 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/cain/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/controlnet/
+-rw-r--r--   0 runner    (1001) docker     (123)     2454 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/controlnet/controlnet-1xb1-fill50k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1117 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/controlnet/controlnet-canny.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/controlnet/controlnet-pose.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1115 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/controlnet/controlnet-seg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1208 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/controlnet/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/
+-rw-r--r--   0 runner    (1001) docker     (123)     3170 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-250kiters_summer2winter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3116 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-270kiters_horse2zebra.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2562 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-80kiters_facades.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3147 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-250kiters_summer2winter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3117 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-270kiters_horse2zebra.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2563 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-80kiters_facades.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3355 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dcgan/
+-rw-r--r--   0 runner    (1001) docker     (123)     1432 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dcgan/dcgan_1xb128-300kiters_celeba-cropped-64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1389 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dcgan/dcgan_1xb128-5epoches_lsun-bedroom-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1894 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dcgan/dcgan_Glr4e-4_Dlr1e-4_1xb128-5kiters_mnist-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1753 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dcgan/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv1/deepfillv1_4xb4_celeba-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1441 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv1/deepfillv1_8xb2_places-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1003 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv1/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv2/
+-rw-r--r--   0 runner    (1001) docker     (123)     1495 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv2/deepfillv2_8xb2_celeba-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1496 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv2/deepfillv2_8xb2_places-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)      998 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv2/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dic/
+-rw-r--r--   0 runner    (1001) docker     (123)     1764 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dic/dic_gan-x8c48b6_4xb2-500k_celeba-hq.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4406 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dic/dic_x8c48b6_4xb2-150k_celeba-hq.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1006 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dic/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dim/
+-rw-r--r--   0 runner    (1001) docker     (123)     2655 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dim/dim_stage1-v16_1xb1-1000k_comp1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      851 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dim/dim_stage1-v16_1xb1-1000k_comp1k_online-merge.py
+-rw-r--r--   0 runner    (1001) docker     (123)      505 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dim/dim_stage2-v16-pln_1xb1-1000k_comp1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      508 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dim/dim_stage3-v16-pln_1xb1-1000k_comp1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1595 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/dim/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/disco_diffusion/
+-rw-r--r--   0 runner    (1001) docker     (123)     1574 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/disco_diffusion/disco-diffusion_adm-u-finetuned_imagenet-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1566 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/disco_diffusion/disco-diffusion_adm-u-finetuned_imagenet-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/disco_diffusion/disco-diffusion_portrait-generator-v001.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1231 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/disco_diffusion/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/edsr/
+-rw-r--r--   0 runner    (1001) docker     (123)     3885 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/edsr/edsr_x2c64b16_1xb16-300k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4044 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/edsr/edsr_x3c64b16_1xb16-300k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3972 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/edsr/edsr_x4c64b16_1xb16-300k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1916 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/edsr/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/edvr/
+-rw-r--r--   0 runner    (1001) docker     (123)     1138 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/edvr/edvrl_c128b40_8xb8-lr2e-4-600k_reds4.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1005 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/edvr/edvrl_wotsa-c128b40_8xb8-lr2e-4-600k_reds4.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1299 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/edvr/edvrm_8xb4-600k_reds.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1108 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/edvr/edvrm_wotsa_8xb4-600k_reds.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1798 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/edvr/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/eg3d/
+-rw-r--r--   0 runner    (1001) docker     (123)     2204 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_afhq-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2346 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_ffhq-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2379 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_shapenet-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1416 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/eg3d/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/esrgan/
+-rw-r--r--   0 runner    (1001) docker     (123)     3759 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/esrgan/esrgan_psnr-x4c64b23g32_1xb16-1000k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2106 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/esrgan/esrgan_x4c64b23g32_1xb16-400k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1424 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/esrgan/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/flavr/
+-rw-r--r--   0 runner    (1001) docker     (123)     4502 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/flavr/flavr_in4out1_8xb4_vimeo90k-septuplet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      643 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/flavr/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/gca/
+-rw-r--r--   0 runner    (1001) docker     (123)     3622 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/gca/baseline_r34_4xb10-200k_comp1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1408 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/gca/baseline_r34_4xb10-dimaug-200k_comp1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3559 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/gca/gca_r34_4xb10-200k_comp1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1398 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/gca/gca_r34_4xb10-dimaug-200k_comp1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1772 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/gca/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/ggan/
+-rw-r--r--   0 runner    (1001) docker     (123)     1616 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/ggan/ggan_dcgan-archi_lr1e-3-1xb128-12Mimgs_celeba-cropped-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1626 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/ggan/ggan_dcgan-archi_lr1e-4-1xb64-10Mimgs_celeba-cropped-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1984 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/ggan/ggan_lsgan-archi_lr1e-4-1xb128-20Mimgs_lsun-bedroom-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1470 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/ggan/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/glean/
+-rw-r--r--   0 runner    (1001) docker     (123)      309 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/glean/glean_in128out1024-fp16_4xb2-300k_ffhq-celeba-hq.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4994 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/glean/glean_in128out1024_4xb2-300k_ffhq-celeba-hq.py
+-rw-r--r--   0 runner    (1001) docker     (123)      261 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/glean/glean_x16-fp16_2xb8_ffhq.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3286 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/glean/glean_x16_2xb8_cat.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3299 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/glean/glean_x16_2xb8_ffhq.py
+-rw-r--r--   0 runner    (1001) docker     (123)      257 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/glean/glean_x8-fp16_2xb8_cat.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3600 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/glean/glean_x8_2xb8_cat.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/glean/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/global_local/
+-rw-r--r--   0 runner    (1001) docker     (123)     1496 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/global_local/gl_8xb12_celeba-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1502 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/global_local/gl_8xb12_places-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1022 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/global_local/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/
+-rw-r--r--   0 runner    (1001) docker     (123)      852 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)      858 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      841 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1485 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1384 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1392 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2542 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/iconvsr/
+-rw-r--r--   0 runner    (1001) docker     (123)      913 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_reds4.py
+-rw-r--r--   0 runner    (1001) docker     (123)      960 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_vimeo90k-bd.py
+-rw-r--r--   0 runner    (1001) docker     (123)      969 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_vimeo90k-bi.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3123 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/iconvsr/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/indexnet/
+-rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/indexnet/indexnet_mobv2-dimaug_1xb16-78k_comp1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3252 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/indexnet/indexnet_mobv2_1xb16-78k_comp1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1056 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/indexnet/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/inst_colorization/
+-rw-r--r--   0 runner    (1001) docker     (123)     1523 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/inst_colorization/inst-colorizatioon_full_official_cocostuff-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)      726 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/inst_colorization/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/liif/
+-rw-r--r--   0 runner    (1001) docker     (123)      994 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/liif/liif-edsr-norm_c64b16_1xb16-1000k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1084 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/liif/liif-rdn-norm_c64b16_1xb16-1000k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4523 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/liif/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/lsgan/
+-rw-r--r--   0 runner    (1001) docker     (123)     1615 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-3-1xb128-12Mimgs_celeba-cropped-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1268 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-4-1xb128-12Mimgs_lsun-bedroom-64x64.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1755 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-4-1xb64-10Mimgs_celeba-cropped-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1485 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/lsgan/lsgan_lsgan-archi_lr1e-4-1xb64-10Mimgs_lsun-bedroom-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2052 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/lsgan/metafile.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/nafnet/
+-rw-r--r--   0 runner    (1001) docker     (123)      957 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/nafnet/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     3364 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/nafnet/nafnet_c64eb11128mb1db1111_8xb8-lr1e-3-400k_gopro.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3346 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/nafnet/nafnet_c64eb2248mb12db2222_8xb8-lr1e-3-400k_sidd.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/partial_conv/
+-rw-r--r--   0 runner    (1001) docker     (123)     1415 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/partial_conv/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1999 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/partial_conv/pconv_stage1_8xb12_places-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1998 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/partial_conv/pconv_stage1_8xb1_celeba-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2065 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/partial_conv/pconv_stage2_4xb2_celeba-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2061 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/partial_conv/pconv_stage2_4xb2_places-256x256.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/pggan/
+-rw-r--r--   0 runner    (1001) docker     (123)     1309 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/pggan/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     3244 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/pggan/pggan_8xb4-12Mimg_celeba-hq-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3043 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/pggan/pggan_8xb4-12Mimgs_celeba-cropped-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)      285 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/pggan/pggan_8xb4-12Mimgs_lsun-bedroom-128x128.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/pix2pix/
+-rw-r--r--   0 runner    (1001) docker     (123)     2040 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/pix2pix/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2743 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-220kiters_aerial2maps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2743 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-220kiters_maps2aerial.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2688 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-80kiters_facades.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3149 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_wo-jitter-flip-1xb4-190kiters_edges2shoes.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/
+-rw-r--r--   0 runner    (1001) docker     (123)    12150 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2727 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-c_c2_8xb3-1100kiters_ffhq-256-512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2713 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-d_c2_8xb3-1100kiters_ffhq-256-512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2867 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-e_c2_8xb3-1100kiters_ffhq-256-512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2829 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c1_8xb2-1600kiters_ffhq-256-1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2811 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c2_8xb3-1100kiters_ffhq-256-512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2800 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c2_8xb3-1100kiters_ffhq-256-896.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2887 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-g_c1_8xb3-1100kiters_ffhq-256-512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2771 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-h_c2_8xb3-1100kiters_ffhq-256-512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2757 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-i_c2_8xb3-1100kiters_ffhq-256-512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2911 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-j_c2_8xb3-1100kiters_ffhq-256-512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2885 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-k_c2_8xb3-1100kiters_ffhq-256-512.py
+-rw-r--r--   0 runner    (1001) docker     (123)      594 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan-csg_bohemian.py
+-rw-r--r--   0 runner    (1001) docker     (123)      585 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan-csg_fish.py
+-rw-r--r--   0 runner    (1001) docker     (123)      419 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan_interp-pad_balloons.py
+-rw-r--r--   0 runner    (1001) docker     (123)      435 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan_interp-pad_disc-nobn_balloons.py
+-rw-r--r--   0 runner    (1001) docker     (123)      432 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan_interp-pad_disc-nobn_fish.py
+-rw-r--r--   0 runner    (1001) docker     (123)      819 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim4_bohemian.py
+-rw-r--r--   0 runner    (1001) docker     (123)      793 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim4_fish.py
+-rw-r--r--   0 runner    (1001) docker     (123)      819 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim8_bohemian.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1889 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/stylegan2_c2_8xb3-1100kiters_ffhq-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1889 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/stylegan2_c2_8xb3-1100kiters_ffhq-512x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/rdn/
+-rw-r--r--   0 runner    (1001) docker     (123)     1884 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/rdn/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     3839 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/rdn/rdn_x2c64b16_1xb16-1000k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3839 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/rdn/rdn_x3c64b16_1xb16-1000k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3892 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/rdn/rdn_x4c64b16_1xb16-1000k_div2k.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/real_basicvsr/
+-rw-r--r--   0 runner    (1001) docker     (123)     1160 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/real_basicvsr/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2298 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/real_basicvsr/realbasicvsr_c64b20-1x30x8_8xb1-lr5e-5-150k_reds.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9968 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/real_basicvsr/realbasicvsr_wogan-c64b20-2x30x8_8xb2-lr1e-4-300k_reds.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/real_esrgan/
+-rw-r--r--   0 runner    (1001) docker     (123)     1137 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/real_esrgan/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2030 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/real_esrgan/realesrgan_c64b23g32_4xb12-lr1e-4-400k_df2k-ost.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7875 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/real_esrgan/realesrnet_c64b23g32_4xb12-lr2e-4-1000k_df2k-ost.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/
+-rw-r--r--   0 runner    (1001) docker     (123)    11152 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma15.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma25.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1079 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma50.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1057 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma15.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1057 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma25.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1057 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma50.py
+-rw-r--r--   0 runner    (1001) docker     (123)      550 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dpdd-dual.py
+-rw-r--r--   0 runner    (1001) docker     (123)      816 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dpdd-single.py
+-rw-r--r--   0 runner    (1001) docker     (123)      809 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_gopro.py
+-rw-r--r--   0 runner    (1001) docker     (123)      803 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_rain13k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      805 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_sidd.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/
+-rw-r--r--   0 runner    (1001) docker     (123)     3992 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      956 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_128_cvt_studioGAN.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_cvt-studioGAN_cifar10-32x32.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1624 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_wReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2471 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_woReLUinplace-Glr1e-4_Dlr4e-4_noaug-ndisc1-8xb32-bigGAN-sch_imagenet1k-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1604 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_woReLUinplace_Glr1e-4_Dlr4e-4_ndisc1-4xb64_imagenet1k-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1533 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_woReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/singan/
+-rw-r--r--   0 runner    (1001) docker     (123)     1449 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/singan/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1209 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/singan/singan_balloons.py
+-rw-r--r--   0 runner    (1001) docker     (123)      779 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/singan/singan_bohemian.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2494 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/singan/singan_fish.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/
+-rw-r--r--   0 runner    (1001) docker     (123)     4133 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1081 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj-cvt-studioGAN_cifar10-32x32.py
+-rw-r--r--   0 runner    (1001) docker     (123)      938 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj-cvt-studioGAN_imagenet1k-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1902 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj_wReLUinplace_Glr2e-4_Dlr5e-5_ndisc5-2xb128_imagenet1k-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1990 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj_wReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1771 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj_woReLUinplace_Glr2e-4_Dlr5e-5_ndisc5-2xb128_imagenet1k-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1857 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj_woReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/srcnn/
+-rw-r--r--   0 runner    (1001) docker     (123)      797 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/srcnn/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     3850 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/srcnn/srcnn_x4k915_1xb16-1000k_div2k.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/srgan_resnet/
+-rw-r--r--   0 runner    (1001) docker     (123)     1456 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/srgan_resnet/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     3728 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/srgan_resnet/msrresnet_x4c64b16_1xb16-1000k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1895 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/srgan_resnet/srgan_x4c64b16_1xb16-1000k_div2k.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/stable_diffusion/
+-rw-r--r--   0 runner    (1001) docker     (123)      499 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/stable_diffusion/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1678 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/stable_diffusion/stable-diffusion_ddim_denoisingunet.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1214 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv1/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1956 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv1/styleganv1_ffhq-1024x1024_8xb4-25Mimgs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2143 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv1/styleganv1_ffhq-256x256_8xb4-25Mimgs.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/
+-rw-r--r--   0 runner    (1001) docker     (123)     4439 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      351 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2-PL-R1_8xb4-apex-fp16-no-scaler-800kiters_ffhq-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)      441 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2-PL-R1_8xb4-fp16-globalG-partialD-no-scaler-800kiters_ffhq-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2-PL_8xb4-fp16-partial-GD-no-scaler-800kiters_ffhq-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2471 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_ffhq-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2440 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-cat-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2443 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-church-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2442 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-horse-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2446 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4_ffhq-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3279 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4_lsun-car-384x512.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/
+-rw-r--r--   0 runner    (1001) docker     (123)     4485 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     3079 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-r_ada-gamma3.3_8xb4-fp16_metfaces-1024x1024.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1449 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4_ffhq-1024x1024.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1437 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4_ffhqu-256x256.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1508 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4x8_afhqv2-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2954 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_ada-gamma6.6_8xb4-fp16_metfaces-1024x1024.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1334 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_afhqv2-512x512.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1326 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_ffhq-1024x1024.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1383 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_ffhqu-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2533 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_gamma2.0_8xb4-fp16-noaug_ffhq-256x256.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2329 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_gamma32.8_8xb4-fp16-noaug_ffhq-1024x1024.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/
+-rw-r--r--   0 runner    (1001) docker     (123)    19414 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      213 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_gan-x2s64w8d6e180_8xb4-lr1e-4-600k_df2k-ost.py
+-rw-r--r--   0 runner    (1001) docker     (123)      210 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_gan-x4s64w8d6e180_8xb4-lr1e-4-600k_df2k-ost.py
+-rw-r--r--   0 runner    (1001) docker     (123)      210 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_gan-x4s64w8d9e240_8xb4-lr1e-4-600k_df2k-ost.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1711 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_psnr-x2s64w8d6e180_8xb4-lr1e-4-600k_df2k-ost.py
+-rw-r--r--   0 runner    (1001) docker     (123)      284 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_psnr-x4s64w8d6e180_8xb4-lr1e-4-600k_df2k-ost.py
+-rw-r--r--   0 runner    (1001) docker     (123)      411 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_psnr-x4s64w8d9e240_8xb4-lr1e-4-600k_df2k-ost.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3744 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR10.py
+-rw-r--r--   0 runner    (1001) docker     (123)      789 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR20.py
+-rw-r--r--   0 runner    (1001) docker     (123)      789 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR30.py
+-rw-r--r--   0 runner    (1001) docker     (123)      789 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR40.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3996 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR10.py
+-rw-r--r--   0 runner    (1001) docker     (123)      787 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR20.py
+-rw-r--r--   0 runner    (1001) docker     (123)      787 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR30.py
+-rw-r--r--   0 runner    (1001) docker     (123)      787 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR40.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4206 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN15.py
+-rw-r--r--   0 runner    (1001) docker     (123)      770 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN25.py
+-rw-r--r--   0 runner    (1001) docker     (123)      770 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN50.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3978 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN15.py
+-rw-r--r--   0 runner    (1001) docker     (123)      768 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN25.py
+-rw-r--r--   0 runner    (1001) docker     (123)      768 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN50.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x2s48w8d6e180_8xb4-lr2e-4-500k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      617 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x2s64w8d4e60_8xb4-lr2e-4-500k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1036 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x2s64w8d6e180_8xb4-lr2e-4-500k_df2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x3s48w8d6e180_8xb4-lr2e-4-500k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      617 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x3s64w8d4e60_8xb4-lr2e-4-500k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1036 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x3s64w8d6e180_8xb4-lr2e-4-500k_df2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3749 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x4s48w8d6e180_8xb4-lr2e-4-500k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)      617 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x4s64w8d4e60_8xb4-lr2e-4-500k_div2k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1036 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x4s64w8d6e180_8xb4-lr2e-4-500k_df2k.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tdan/
+-rw-r--r--   0 runner    (1001) docker     (123)     2107 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tdan/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     3604 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tdan/tdan_x4_8xb16-lr1e-4-400k_vimeo90k-bd.py
+-rw-r--r--   0 runner    (1001) docker     (123)      483 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tdan/tdan_x4_8xb16-lr1e-4-400k_vimeo90k-bi.py
+-rw-r--r--   0 runner    (1001) docker     (123)      425 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tdan/tdan_x4ft_8xb16-lr5e-5-400k_vimeo90k-bi.py
+-rw-r--r--   0 runner    (1001) docker     (123)      514 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tdan/tdan_x4ft_8xb16-lr5e-5-800k_vimeo90k-bd.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tof/
+-rw-r--r--   0 runner    (1001) docker     (123)     3310 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tof/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      951 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_spynet-chair-wobn_1xb1_vimeo90k-triplet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      951 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_spynet-kitti-wobn_1xb1_vimeo90k-triplet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      957 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_spynet-pytoflow-wobn_1xb1_vimeo90k-triplet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      965 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_spynet-sintel-wobn-clean_1xb1_vimeo90k-triplet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      965 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_spynet-sintel-wobn-final_1xb1_vimeo90k-triplet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2036 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_x4_official_vimeo90k.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/ttsr/
+-rw-r--r--   0 runner    (1001) docker     (123)      963 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/ttsr/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     2115 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/ttsr/ttsr-gan_x4c64b16_1xb9-500k_CUFED.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6406 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/ttsr/ttsr-rec_x4c64b16_1xb9-200k_CUFED.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/wgan-gp/
+-rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/wgan-gp/metafile.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      483 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/wgan-gp/wgangp_GN-GP-50_1xb64-160kiters_lsun-bedroom-128x128.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2030 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/configs/wgan-gp/wgangp_GN_1xb64-160kiters_celeba-cropped-128x128.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/
+-rw-r--r--   0 runner    (1001) docker     (123)     1331 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/colorization_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4489 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/conditional_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4025 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/download_inference_resources.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13401 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/gradio-demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1398 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/inpainting_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1309 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/matting_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4030 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/mmediting_inference_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2196 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/restoration_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1996 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/restoration_face_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3034 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/restoration_video_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3477 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/singan_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1800 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/translation_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2431 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/unconditional_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2836 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/demo/video_interpolation_demo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1637 2023-04-07 07:57:25.000000 mmedit-1.0.0rc7/mmedit/.mim/model-index.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/analysis_tools/
+-rw-r--r--   0 runner    (1001) docker     (123)     4460 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/analysis_tools/get_flops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/analysis_tools/print_config.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      265 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/cpu_train.sh
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/bgm/
+-rw-r--r--   0 runner    (1001) docker     (123)     4147 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/bgm/preprocess_bgm_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/comp1k/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      939 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/comp1k/check_extended_fg.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10643 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/comp1k/evaluate_comp1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4265 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/comp1k/extend_fg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1462 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/comp1k/filter_comp1k_anno.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10486 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/comp1k/preprocess_comp1k_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/df2k_ost/
+-rw-r--r--   0 runner    (1001) docker     (123)    12294 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/df2k_ost/preprocess_df2k_ost_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/div2k/
+-rw-r--r--   0 runner    (1001) docker     (123)    14970 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/div2k/preprocess_div2k_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/glean/
+-rw-r--r--   0 runner    (1001) docker     (123)     3706 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/glean/preprocess_cat_test_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5188 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/glean/preprocess_cat_train_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3087 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/glean/preprocess_ffhq_celebahq_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/reds/
+-rw-r--r--   0 runner    (1001) docker     (123)     6687 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/reds/crop_sub_images.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11232 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/reds/preprocess_reds_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/sidd/
+-rw-r--r--   0 runner    (1001) docker     (123)     2639 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/sidd/preprocess_sidd_test_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/vid4/
+-rw-r--r--   0 runner    (1001) docker     (123)     3039 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/vid4/preprocess_vid4_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/vimeo90k/
+-rw-r--r--   0 runner    (1001) docker     (123)    11198 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/vimeo90k/preprocess_vimeo90k_dataset.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      479 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dist_test.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)      442 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/dist_train.sh
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/gui/
+-rw-r--r--   0 runner    (1001) docker     (123)    15602 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/gui/component.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2506 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/gui/gui.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3876 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/gui/page_general.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34328 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/gui/page_sr.py
+-rw-r--r--   0 runner    (1001) docker     (123)      530 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/gui/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/model_converters/
+-rw-r--r--   0 runner    (1001) docker     (123)     1256 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/model_converters/publish_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10494 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/model_converters/pytorch2onnx.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      566 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/slurm_test.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)      622 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/slurm_train.sh
+-rw-r--r--   0 runner    (1001) docker     (123)     2868 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4365 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/.mim/tools/train.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1445 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/apis/
+-rw-r--r--   0 runner    (1001) docker     (123)       83 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/
+-rw-r--r--   0 runner    (1001) docker     (123)     1181 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8600 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/base_mmedit_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2773 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/colorization_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2789 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/conditional_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13415 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/eg3d_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3909 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/image_super_resolution_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30798 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/inference_functions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3284 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/inpainting_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3988 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/matting_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4381 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/mmedit_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2324 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/text2image_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2768 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/translation_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2751 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/unconditional_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7644 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/video_interpolation_inferencer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7304 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/apis/inferencers/video_restoration_inferencer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)      909 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11563 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/basic_conditional_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12825 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/basic_frames_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8711 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/basic_image_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29271 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/categories.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6669 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/cifar10_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5211 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/comp1k_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1974 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/controlnet_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11864 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/data_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7942 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/grow_scale_image_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1579 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/imagenet_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4171 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/mscoco_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2765 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/paired_image_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4773 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/singan_dataset.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/
+-rw-r--r--   0 runner    (1001) docker     (123)     2985 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9720 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/alpha.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2582 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/aug_frames.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21020 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/aug_pixel.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15752 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/aug_shape.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20398 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/blur_kernels.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37682 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/crop.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11492 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/fgbg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3906 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/formatting.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8534 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/generate_assistant.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9612 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/generate_frame_indices.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2320 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/get_masked_image.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18915 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/loading.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9543 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/matlab_like_resize.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3595 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/normalization.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20688 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/random_degradations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5061 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/random_down_sampling.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9795 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/trimap.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2755 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/transforms/values.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4910 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/datasets/unpaired_image_dataset.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9197 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/edit.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/engine/
+-rw-r--r--   0 runner    (1001) docker     (123)      223 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/engine/hooks/
+-rw-r--r--   0 runner    (1001) docker     (123)      570 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/hooks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7318 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/hooks/ema.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3341 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/hooks/iter_time_hook.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3705 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/hooks/pggan_fetch_data_hook.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4941 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/hooks/pickle_data_hook.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5050 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/hooks/reduce_lr_scheduler_hook.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18445 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/hooks/visualization_hook.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/engine/optimizers/
+-rw-r--r--   0 runner    (1001) docker     (123)      384 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/optimizers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2783 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/optimizers/multi_optimizer_constructor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5209 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/optimizers/pggan_optimizer_constructor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3650 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/optimizers/singan_optimizer_constructor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/engine/runner/
+-rw-r--r--   0 runner    (1001) docker     (123)      205 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/runner/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20291 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/runner/edit_loops.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1193 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/runner/log_processor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2612 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/runner/loop_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/engine/schedulers/
+-rw-r--r--   0 runner    (1001) docker     (123)      209 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/schedulers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1714 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/schedulers/linear_lr_scheduler_with_interval.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6441 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/engine/schedulers/reduce_lr_scheduler.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/evaluation/
+-rw-r--r--   0 runner    (1001) docker     (123)     1053 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7628 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/evaluator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/evaluation/functional/
+-rw-r--r--   0 runner    (1001) docker     (123)      423 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/functional/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12348 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/functional/fid_inception.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2347 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/functional/gaussian_funcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22211 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/functional/inception_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/
+-rw-r--r--   0 runner    (1001) docker     (123)     1117 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14859 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/base_gen_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5033 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/base_sample_wise_metric.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4536 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/connectivity_error.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6819 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/equivariance.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11715 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/fid.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3459 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/gradient_error.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15845 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/inception_score.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1857 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/mae.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2679 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/matting_mse.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5053 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/metrics_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13575 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/ms_ssim.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1712 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/mse.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11566 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/niqe.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11850 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/niqe_pris_params.npz
+-rw-r--r--   0 runner    (1001) docker     (123)    11870 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/ppl.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11443 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/precision_and_recall.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4411 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/psnr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2661 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/sad.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4307 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/snr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5943 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/ssim.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14289 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/evaluation/metrics/swd.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/
+-rw-r--r--   0 runner    (1001) docker     (123)      637 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/
+-rw-r--r--   0 runner    (1001) docker     (123)     2714 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      902 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/all_gather_layer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4856 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/aspp.py
+-rw-r--r--   0 runner    (1001) docker     (123)      186 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/conv.py
+-rw-r--r--   0 runner    (1001) docker     (123)      663 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/downsample.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3726 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/ensemble.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2652 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/gated_conv_module.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1227 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/img_normalize.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3530 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/linear_module.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6819 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/multi_layer_disc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4942 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/patch_disc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18813 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/resnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4241 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/separable_conv_module.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1107 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/simple_encoder_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4357 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/smpatch_disc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2987 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/sr_backbone.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1572 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/upsample.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3909 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/vgg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6619 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_archs/wrapper.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/base_models/
+-rw-r--r--   0 runner    (1001) docker     (123)      709 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_models/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15297 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_models/average_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13583 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_models/base_conditional_gan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8338 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_models/base_edit_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25575 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_models/base_gan.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10217 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_models/base_mattor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7790 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_models/base_translation_model.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3807 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_models/basic_interpolator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17990 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_models/one_stage.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14493 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/base_models/two_stage.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/data_preprocessors/
+-rw-r--r--   0 runner    (1001) docker     (123)      215 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/data_preprocessors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    37145 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/data_preprocessors/edit_data_preprocessor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7245 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/data_preprocessors/mattor_preprocessor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/diffusion_schedulers/
+-rw-r--r--   0 runner    (1001) docker     (123)     4836 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/diffusion_schedulers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10327 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/diffusion_schedulers/ddim_scheduler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9639 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/diffusion_schedulers/ddpm_scheduler.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/
+-rw-r--r--   0 runner    (1001) docker     (123)     4553 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/aotgan/
+-rw-r--r--   0 runner    (1001) docker     (123)      349 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/aotgan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2200 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/aotgan/aot_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1909 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/aotgan/aot_encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1022 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/aotgan/aot_encoder_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7407 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/aotgan/aot_inpaintor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3808 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/aotgan/aot_neck.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/arcface/
+-rw-r--r--   0 runner    (1001) docker     (123)      108 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/arcface/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6054 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/arcface/arcface_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2668 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/arcface/id_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3883 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/arcface/model_irse.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/basicvsr/
+-rw-r--r--   0 runner    (1001) docker     (123)      156 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/basicvsr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5354 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/basicvsr/basicvsr.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13764 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/basicvsr/basicvsr_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/basicvsr_plusplus_net/
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/basicvsr_plusplus_net/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16241 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/basicvsr_plusplus_net/basicvsr_plusplus_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/biggan/
+-rw-r--r--   0 runner    (1001) docker     (123)      942 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/biggan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6665 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12960 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_deep_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20674 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_deep_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12216 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19952 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    30009 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9438 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_snmodule.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/cain/
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/cain/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1870 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/cain/cain.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10627 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/cain/cain_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/controlnet/
+-rw-r--r--   0 runner    (1001) docker     (123)      202 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/controlnet/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22242 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/controlnet/controlnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2181 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/controlnet/controlnet_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/cyclegan/
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/cyclegan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11333 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/cyclegan/cyclegan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5638 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/cyclegan/cyclegan_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4709 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/cyclegan/cyclegan_modules.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/dcgan/
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/dcgan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4344 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/dcgan/dcgan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5001 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/dcgan/dcgan_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7623 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/dcgan/dcgan_generator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/ddpm/
+-rw-r--r--   0 runner    (1001) docker     (123)      119 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ddpm/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21369 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ddpm/attention.py
+-rw-r--r--   0 runner    (1001) docker     (123)    52979 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ddpm/denoising_unet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2975 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ddpm/embeddings.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8588 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ddpm/res_blocks.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20328 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ddpm/unet_blocks.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/
+-rw-r--r--   0 runner    (1001) docker     (123)      595 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15253 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/contextual_attention.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2568 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/contextual_attention_neck.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3559 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/deepfill_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1859 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/deepfill_disc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2823 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/deepfill_encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2781 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/deepfill_refiner.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15868 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/deepfillv1.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv2/
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3013 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/deepfillv2/two_stage_encoder_decoder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/dic/
+-rw-r--r--   0 runner    (1001) docker     (123)      467 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/dic/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6570 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/dic/dic.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14735 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/dic/dic_net.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7207 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/dic/feedback_hour_glass.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4188 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/dic/light_cnn.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/dim/
+-rw-r--r--   0 runner    (1001) docker     (123)       88 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/dim/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7522 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/dim/dim.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/disco_diffusion/
+-rw-r--r--   0 runner    (1001) docker     (123)      356 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/disco_diffusion/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6069 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/disco_diffusion/clip_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9607 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/disco_diffusion/disco.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19913 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/disco_diffusion/guider.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5328 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/disco_diffusion/secondary_model.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/duf/
+-rw-r--r--   0 runner    (1001) docker     (123)      128 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/duf/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2714 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/duf/duf.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/edsr/
+-rw-r--r--   0 runner    (1001) docker     (123)      101 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/edsr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3795 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/edsr/edsr_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/edvr/
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/edvr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2640 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/edvr/edvr.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18573 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/edvr/edvr_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/eg3d/
+-rw-r--r--   0 runner    (1001) docker     (123)      324 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/eg3d/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20954 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/eg3d/camera.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4464 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/eg3d/dual_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13867 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/eg3d/eg3d.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10550 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/eg3d/eg3d_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12466 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/eg3d/eg3d_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6606 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/eg3d/eg3d_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2674 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/eg3d/ray_sampler.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24027 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/eg3d/renderer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/esrgan/
+-rw-r--r--   0 runner    (1001) docker     (123)      149 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/esrgan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4262 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/esrgan/esrgan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6570 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/esrgan/rrdb_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/fba/
+-rw-r--r--   0 runner    (1001) docker     (123)      183 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/fba/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7069 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/fba/fba_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1233 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/fba/fba_encoder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/flavr/
+-rw-r--r--   0 runner    (1001) docker     (123)      149 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/flavr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2383 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/flavr/flavr.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18190 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/flavr/flavr_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/gca/
+-rw-r--r--   0 runner    (1001) docker     (123)      371 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/gca/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3044 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/gca/gca.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15490 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/gca/gca_module.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14313 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/gca/resgca_dec.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20745 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/gca/resgca_enc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/ggan/
+-rw-r--r--   0 runner    (1001) docker     (123)       91 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ggan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4304 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ggan/ggan.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/glean/
+-rw-r--r--   0 runner    (1001) docker     (123)      125 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/glean/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12606 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/glean/glean_styleganv2.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/global_local/
+-rw-r--r--   0 runner    (1001) docker     (123)      384 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/global_local/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3091 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2057 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_dilation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1880 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_disc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1581 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1458 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_encoder_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10057 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_inpaintor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/guided_diffusion/
+-rw-r--r--   0 runner    (1001) docker     (123)      185 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/guided_diffusion/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12101 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/guided_diffusion/adm.py
+-rw-r--r--   0 runner    (1001) docker     (123)    22206 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/guided_diffusion/classifier.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/iconvsr/
+-rw-r--r--   0 runner    (1001) docker     (123)      110 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/iconvsr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14816 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/iconvsr/iconvsr_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/indexnet/
+-rw-r--r--   0 runner    (1001) docker     (123)      398 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/indexnet/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3297 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/indexnet/indexnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5554 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/indexnet/indexnet_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19093 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/indexnet/indexnet_encoder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/
+-rw-r--r--   0 runner    (1001) docker     (123)      255 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9786 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/color_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9754 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/colorization_net.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11231 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/fusion_net.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9600 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/inst_colorization.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4859 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/weight_layer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/liif/
+-rw-r--r--   0 runner    (1001) docker     (123)      235 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/liif/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2584 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/liif/liif.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10133 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/liif/liif_net.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1120 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/liif/mlp_refiner.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/lsgan/
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/lsgan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4392 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/lsgan/lsgan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4402 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/lsgan/lsgan_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7364 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/lsgan/lsgan_generator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/mspie/
+-rw-r--r--   0 runner    (1001) docker     (123)      566 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/mspie/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8923 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/mspie/mspie_stylegan2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3117 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/mspie/mspie_stylegan2_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19309 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/mspie/mspie_stylegan2_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11417 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/mspie/mspie_stylegan2_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2294 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/mspie/pe_singan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9673 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/mspie/pe_singan_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8872 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/mspie/positional_encoding.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/nafnet/
+-rw-r--r--   0 runner    (1001) docker     (123)      242 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/nafnet/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5062 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/nafnet/naf_avgpool2d.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1812 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/nafnet/naf_layerNorm2d.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8372 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/nafnet/nafbaseline_net.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8539 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/nafnet/nafnet_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/pconv/
+-rw-r--r--   0 runner    (1001) docker     (123)      460 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pconv/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3645 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pconv/mask_conv_module.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3603 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pconv/partial_conv.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3631 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pconv/pconv_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4325 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pconv/pconv_encoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1024 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pconv/pconv_encoder_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2823 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pconv/pconv_inpaintor.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/pggan/
+-rw-r--r--   0 runner    (1001) docker     (123)      774 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pggan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20707 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pggan/pggan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9244 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pggan/pggan_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10398 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pggan/pggan_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19722 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pggan/pggan_modules.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/pix2pix/
+-rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pix2pix/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9137 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pix2pix/pix2pix.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4785 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pix2pix/pix2pix_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4255 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/pix2pix/pix2pix_modules.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/plain/
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/plain/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8757 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/plain/plain_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1867 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/plain/plain_refiner.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/rdn/
+-rw-r--r--   0 runner    (1001) docker     (123)      110 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/rdn/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5708 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/rdn/rdn_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/real_basicvsr/
+-rw-r--r--   0 runner    (1001) docker     (123)      182 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/real_basicvsr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7651 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/real_basicvsr/real_basicvsr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3841 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/real_basicvsr/real_basicvsr_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/real_esrgan/
+-rw-r--r--   0 runner    (1001) docker     (123)      215 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/real_esrgan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7314 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/real_esrgan/real_esrgan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3140 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/real_esrgan/unet_disc.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/restormer/
+-rw-r--r--   0 runner    (1001) docker     (123)      110 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/restormer/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17236 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/restormer/restormer_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/sagan/
+-rw-r--r--   0 runner    (1001) docker     (123)      420 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/sagan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6964 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/sagan/sagan.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17462 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/sagan/sagan_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20851 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/sagan/sagan_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25894 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/sagan/sagan_modules.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/singan/
+-rw-r--r--   0 runner    (1001) docker     (123)      285 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/singan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28167 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/singan/singan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3244 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/singan/singan_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7217 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/singan/singan_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8103 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/singan/singan_modules.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/srcnn/
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/srcnn/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2462 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/srcnn/srcnn_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/srgan/
+-rw-r--r--   0 runner    (1001) docker     (123)      208 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/srgan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3663 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/srgan/modified_vgg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3690 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/srgan/sr_resnet.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10843 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/srgan/srgan.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/stable_diffusion/
+-rw-r--r--   0 runner    (1001) docker     (123)      173 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stable_diffusion/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7641 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stable_diffusion/clip_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20545 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stable_diffusion/stable_diffusion.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34487 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stable_diffusion/vae.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/
+-rw-r--r--   0 runner    (1001) docker     (123)      591 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6577 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/stylegan1.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5267 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/stylegan1_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14053 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/stylegan1_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12346 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/stylegan1_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2395 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/stylegan_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/
+-rw-r--r--   0 runner    (1001) docker     (123)      584 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/ada/
+-rw-r--r--   0 runner    (1001) docker     (123)       48 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/ada/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32653 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/ada/augment.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3439 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/ada/grid_sample_gradfix.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1058 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/ada/misc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7216 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/ada/upfirdn2d.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14184 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/stylegan2.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13479 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/stylegan2_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    23415 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/stylegan2_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26059 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/stylegan2_modules.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan3/
+-rw-r--r--   0 runner    (1001) docker     (123)      339 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan3/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10154 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan3/stylegan3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8129 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan3/stylegan3_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)    28215 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan3/stylegan3_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6143 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/stylegan3/stylegan3_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/swinir/
+-rw-r--r--   0 runner    (1001) docker     (123)      107 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/swinir/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4845 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/swinir/swinir_modules.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12021 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/swinir/swinir_net.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20750 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/swinir/swinir_rstb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2695 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/swinir/swinir_utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/tdan/
+-rw-r--r--   0 runner    (1001) docker     (123)      132 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/tdan/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3256 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/tdan/tdan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6089 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/tdan/tdan_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/tof/
+-rw-r--r--   0 runner    (1001) docker     (123)      196 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/tof/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7806 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/tof/tof_vfi_net.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6438 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/tof/tof_vsr_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/ttsr/
+-rw-r--r--   0 runner    (1001) docker     (123)      316 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ttsr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2731 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ttsr/lte.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3871 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ttsr/search_transformer.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8782 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ttsr/ttsr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1566 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ttsr/ttsr_disc.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13928 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/ttsr/ttsr_net.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/editors/wgan_gp/
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/wgan_gp/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3965 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/wgan_gp/wgan_discriminator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5593 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/wgan_gp/wgan_generator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4761 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/wgan_gp/wgan_gp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6765 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/editors/wgan_gp/wgan_gp_module.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/losses/
+-rw-r--r--   0 runner    (1001) docker     (123)     1770 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4390 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/clip_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7482 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/composition_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2058 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/face_id_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3260 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/feature_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)    21058 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/gan_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2181 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/gradient_loss.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/
+-rw-r--r--   0 runner    (1001) docker     (123)      625 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4124 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/clip_loss_comps.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16741 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/disc_auxiliary_loss_comps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4192 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/face_id_loss_comps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4173 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/gan_loss_comps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7309 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/gen_auxiliary_loss_comps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4135 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/loss_wrapper.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10892 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/perceptual_loss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9690 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/losses/pixelwise_loss.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/models/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      972 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4450 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/utils/bbox_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      803 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/utils/diffusion_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2333 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/utils/flow_warp.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10755 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/utils/model_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6327 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/utils/sampling_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1946 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/models/utils/tensor_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6833 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/registry.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/structures/
+-rw-r--r--   0 runner    (1001) docker     (123)      123 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/structures/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12588 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/structures/edit_data_sample.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)     1208 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      561 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/utils/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7445 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/utils/img_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3093 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/utils/io_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      644 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/utils/logger.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5276 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/utils/sampler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2409 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/utils/setup_env.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18301 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/utils/trans_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      463 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/utils/typing.py
+-rw-r--r--   0 runner    (1001) docker     (123)      484 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit/visualization/
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/visualization/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4988 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/visualization/concat_visualizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12566 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/visualization/gen_visualizer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17165 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/mmedit/visualization/vis_backend.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    22042 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    42694 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      697 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/mmedit.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/requirements/
+-rw-r--r--   0 runner    (1001) docker     (123)      230 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/requirements/docs.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/requirements/mminstall.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      164 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/requirements/optional.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      134 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/requirements/readthedocs.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      500 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/requirements/runtime.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      259 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/requirements/tests.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      657 2023-04-07 07:57:26.000000 mmedit-1.0.0rc7/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     9500 2023-04-07 07:56:59.000000 mmedit-1.0.0rc7/setup.py
```

### Comparing `mmedit-1.0.0rc6/PKG-INFO` & `mmedit-1.0.0rc7/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mmedit
-Version: 1.0.0rc6
+Version: 1.0.0rc7
 Summary: OpenMMLab Image and Video Editing Toolbox and Benchmark
 Home-page: https://github.com/open-mmlab/mmediting
 Maintainer: MMEditing Contributors
 Maintainer-email: openmmlab@gmail.com
 License: Apache License 2.0
 Description: <div id="top" align="center">
           <img src="docs/en/_static/image/mmediting-logo.png" width="500px"/>
@@ -23,25 +23,25 @@
                 <i><font size="4">TRY IT OUT</font></i>
               </a>
             </sup>
           </div>
           <div>&nbsp;</div>
         
         [![PyPI](https://badge.fury.io/py/mmedit.svg)](https://pypi.org/project/mmedit/)
-        [![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmediting.readthedocs.io/en/1.x/)
+        [![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmediting.readthedocs.io/en/latest/)
         [![badge](https://github.com/open-mmlab/mmediting/workflows/build/badge.svg)](https://github.com/open-mmlab/mmediting/actions)
         [![codecov](https://codecov.io/gh/open-mmlab/mmediting/branch/master/graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmediting)
-        [![license](https://img.shields.io/github/license/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/blob/1.x/LICENSE)
+        [![license](https://img.shields.io/github/license/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/blob/main/LICENSE)
         [![open issues](https://isitmaintained.com/badge/open/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/issues)
         [![issue resolution](https://isitmaintained.com/badge/resolution/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/issues)
         
-        [📘Documentation](https://mmediting.readthedocs.io/en/1.x/) |
-        [🛠️Installation](https://mmediting.readthedocs.io/en/1.x/get_started/install.html) |
-        [📊Model Zoo](https://mmediting.readthedocs.io/en/1.x/model_zoo/overview.html) |
-        [🆕Update News](https://mmediting.readthedocs.io/en/1.x/changelog.html) |
+        [📘Documentation](https://mmediting.readthedocs.io/en/latest/) |
+        [🛠️Installation](https://mmediting.readthedocs.io/en/latest/get_started/install.html) |
+        [📊Model Zoo](https://mmediting.readthedocs.io/en/latest/model_zoo/overview.html) |
+        [🆕Update News](https://mmediting.readthedocs.io/en/latest/changelog.html) |
         [🚀Ongoing Projects](https://github.com/open-mmlab/mmediting/projects) |
         [🤔Reporting Issues](https://github.com/open-mmlab/mmediting/issues)
         
         English | [简体中文](README_zh-CN.md)
         
         </div>
         
@@ -57,18 +57,19 @@
           <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
           <a href="https://www.youtube.com/openmmlab" style="text-decoration:none;">
             <img src="https://user-images.githubusercontent.com/25839884/218346691-ceb2116a-465a-40af-8424-9f30d2348ca9.png" width="3%" alt="" /></a>
         </div>
         
         ## 🚀 What's New <a><img width="35" height="20" src="https://user-images.githubusercontent.com/12782558/212848161-5e783dd6-11e8-4fe0-bbba-39ffb77730be.png"></a>
         
-        ### New release [**MMEditing v1.0.0rc6**](https://github.com/open-mmlab/mmediting/releases/tag/v1.0.0rc6) \[02/03/2023\]:
+        ### New release [**MMEditing v1.0.0rc7**](https://github.com/open-mmlab/mmediting/releases/tag/v1.0.0rc7) \[07/04/2023\]:
         
-        - Support Gradio gui of Inpainting inference.
-        - Support Colorization, Translationin and all GAN models inferencer.
+        - Support DiffuserWrapper
+        - Support ControlNet (training and inference).
+        - Support PyTorch 2.0 (successfully compile 33+ models on 'inductor' backend).
         
         **MMEditing** has supported all the tasks, models, metrics, and losses in [MMGeneration](https://github.com/open-mmlab/mmgeneration) and unifies interfaces of all components based on [MMEngine](https://github.com/open-mmlab/mmengine) 😍.
         
         Please refer to [changelog.md](docs/en/changelog.md) for details and release history.
         
         Please refer to [migration documents](docs/en/migration/overview.md) to migrate from [old version](https://github.com/open-mmlab/mmediting/tree/master) MMEditing 0.x to our brand new 1.x version.
         
@@ -89,29 +90,29 @@
         
         MMEditing is an open-source image and video editing&generating toolbox based on PyTorch. It is a part of the [OpenMMLab](https://openmmlab.com/) project.
         
         Currently, MMEditing support multiple image and video generation/editing tasks.
         
         https://user-images.githubusercontent.com/12782558/217152698-49169038-9872-4200-80f7-1d5f7613afd7.mp4
         
-        The best practice on our main 1.x branch works with **Python 3.8+** and **PyTorch 1.9+**.
+        The best practice on our main branch works with **Python 3.8+** and **PyTorch 1.9+**.
         
         ### ✨ Major features
         
         - **State of the Art**
         
           MMEditing provides state-of-the-art generative models to process, edit and synthesize images and videos.
         
         - **Powerful and Popular Applications**
         
           MMEditing supports popular and contemporary image restoration, text-to-image, 3D-aware generation, inpainting, matting, super-resolution and generation applications. Specifically, MMEditing supports GAN interpolation, GAN projection, GAN manipulations and many other popular GAN’s applications. It’s time to play with your GANs!
         
         - **New Modular Design for Flexible Combination**
         
-          We decompose the editing framework into different modules and one can easily construct a customized editor framework by combining different modules. Specifically, a new design for complex loss modules is proposed for customizing the links between modules, which can achieve flexible combinations among different modules.(Tutorial for [losses](https://mmediting.readthedocs.io/en/dev-1.x/howto/losses.html))
+          We decompose the editing framework into different modules and one can easily construct a customized editor framework by combining different modules. Specifically, a new design for complex loss modules is proposed for customizing the links between modules, which can achieve flexible combinations among different modules.(Tutorial for [losses](https://mmediting.readthedocs.io/en/latest/howto/losses.html))
         
         - **Efficient Distributed Training**
         
           With the support of [MMSeparateDistributedDataParallel](https://github.com/open-mmlab/mmengine/blob/main/mmengine/model/wrappers/seperate_distributed.py), distributed training for dynamic architectures can be easily implemented.
         
         <p align="right"><a href="#top">🔝Back to top</a></p>
         
@@ -139,22 +140,22 @@
         
         **Step 2.**
         Install MMCV with [MIM](https://github.com/open-mmlab/mim).
         
         ```shell
         pip3 install openmim
         # wait for more pre-compiled pkgs to release
-        mim install 'mmcv>=2.0.0rc1'
+        mim install 'mmcv>=2.0.0'
         ```
         
         **Step 3.**
         Install MMEditing from source.
         
         ```shell
-        git clone -b 1.x https://github.com/open-mmlab/mmediting.git
+        git clone https://github.com/open-mmlab/mmediting.git
         cd mmediting
         pip3 install -e .
         ```
         
         Please refer to [installation](docs/en/get_started/install.md) for more detailed instruction.
         
         **Getting Started**
@@ -309,14 +310,15 @@
                   <li><a href="configs/dim/README.md">DIM (CVPR'2017)</a></li>
                   <li><a href="configs/indexnet/README.md">IndexNet (ICCV'2019)</a></li>
                   <li><a href="configs/mask2former">GCA (AAAI'2020)</a></li>
                 </ul>
               </td>
               <td>
                 <ul>
+                  <li><a href="configs/controlnet/README.md">ControlNet (2023)</a></li>
                   <li><a href="projects/glide/configs/README.md">GLIDE (NeurIPS'2021)</a></li>
                   <li><a href="configs/disco_diffusion/README.md">Disco-Diffusion (2022)</a></li>
                   <li><a href="configs/stable_diffusion/README.md">Stable-Diffusion (2022)</a></li>
                 </ul>
               </td>
               <td>
                 <ul>
@@ -325,26 +327,26 @@
               </td>
             </tr>
         </td>
             </tr>
           </tbody>
         </table>
         
-        Please refer to [model_zoo](https://mmediting.readthedocs.io/en/1.x/model_zoo/overview.html) for more details.
+        Please refer to [model_zoo](https://mmediting.readthedocs.io/en/latest/model_zoo/overview.html) for more details.
         
         <p align="right"><a href="#top">🔝Back to top</a></p>
         
         ## 🤝 Acknowledgement
         
         MMEditing is an open source project that is contributed by researchers and engineers from various colleges and companies. We wish that the toolbox and benchmark could serve the growing research community by providing a flexible toolkit to reimplement existing methods and develop their own new methods.
         
         We appreciate all the contributors who implement their methods or add new features, as well as users who give valuable feedbacks. Thank you all!
         
         <a href="https://github.com/open-mmlab/mmediting/graphs/contributors">
-          <img src="https://contrib.rocks/image?repo=liuwenran/mmediting" />
+          <img src="https://contrib.rocks/image?repo=open-mmlab/mmediting" />
         </a>
         
         <p align="right"><a href="#top">🔝Back to top</a></p>
         
         ## 🖊️ Citation
         
         If MMEditing is helpful to your research, please cite it as below.
@@ -366,32 +368,32 @@
         Please refer to [LICENSES](LICENSE) for the careful check, if you are using our code for commercial matters.
         
         <p align="right"><a href="#top">🔝Back to top</a></p>
         
         ## 🏗️ ️OpenMMLab Family
         
         - [MMEngine](https://github.com/open-mmlab/mmengine): OpenMMLab foundational library for training deep learning models.
-        - [MMCV](https://github.com/open-mmlab/mmcv/tree/2.x): OpenMMLab foundational library for computer vision.
+        - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for computer vision.
         - [MIM](https://github.com/open-mmlab/mim): MIM installs OpenMMLab packages.
-        - [MMClassification](https://github.com/open-mmlab/mmclassification/tree/1.x): OpenMMLab image classification toolbox and benchmark.
-        - [MMDetection](https://github.com/open-mmlab/mmdetection/tree/3.x): OpenMMLab detection toolbox and benchmark.
-        - [MMDetection3D](https://github.com/open-mmlab/mmdetection3d/tree/1.x): OpenMMLab's next-generation platform for general 3D object detection.
-        - [MMRotate](https://github.com/open-mmlab/mmrotate/tree/1.x): OpenMMLab rotated object detection toolbox and benchmark.
-        - [MMSegmentation](https://github.com/open-mmlab/mmsegmentation/tree/1.x): OpenMMLab semantic segmentation toolbox and benchmark.
-        - [MMOCR](https://github.com/open-mmlab/mmocr/tree/1.x): OpenMMLab text detection, recognition, and understanding toolbox.
-        - [MMPose](https://github.com/open-mmlab/mmpose/tree/1.x): OpenMMLab pose estimation toolbox and benchmark.
-        - [MMHuman3D](https://github.com/open-mmlab/mmhuman3d/tree/1.x): OpenMMLab 3D human parametric model toolbox and benchmark.
-        - [MMSelfSup](https://github.com/open-mmlab/mmselfsup/tree/1.x): OpenMMLab self-supervised learning toolbox and benchmark.
-        - [MMRazor](https://github.com/open-mmlab/mmrazor/tree/1.x): OpenMMLab model compression toolbox and benchmark.
-        - [MMFewShot](https://github.com/open-mmlab/mmfewshot/tree/1.x): OpenMMLab fewshot learning toolbox and benchmark.
-        - [MMAction2](https://github.com/open-mmlab/mmaction2/tree/1.x): OpenMMLab's next-generation action understanding toolbox and benchmark.
-        - [MMTracking](https://github.com/open-mmlab/mmtracking/tree/1.x): OpenMMLab video perception toolbox and benchmark.
-        - [MMFlow](https://github.com/open-mmlab/mmflow/tree/1.x): OpenMMLab optical flow toolbox and benchmark.
-        - [MMEditing](https://github.com/open-mmlab/mmediting/tree/1.x): OpenMMLab image and video editing toolbox.
-        - [MMGeneration](https://github.com/open-mmlab/mmgeneration/tree/1.x): OpenMMLab image and video generative models toolbox.
+        - [MMClassification](https://github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
+        - [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection toolbox and benchmark.
+        - [MMDetection3D](https://github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for general 3D object detection.
+        - [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab rotated object detection toolbox and benchmark.
+        - [MMSegmentation](https://github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox and benchmark.
+        - [MMOCR](https://github.com/open-mmlab/mmocr): OpenMMLab text detection, recognition, and understanding toolbox.
+        - [MMPose](https://github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
+        - [MMHuman3D](https://github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human parametric model toolbox and benchmark.
+        - [MMSelfSup](https://github.com/open-mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox and benchmark.
+        - [MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab model compression toolbox and benchmark.
+        - [MMFewShot](https://github.com/open-mmlab/mmfewshot): OpenMMLab fewshot learning toolbox and benchmark.
+        - [MMAction2](https://github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action understanding toolbox and benchmark.
+        - [MMTracking](https://github.com/open-mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark.
+        - [MMFlow](https://github.com/open-mmlab/mmflow): OpenMMLab optical flow toolbox and benchmark.
+        - [MMEditing](https://github.com/open-mmlab/mmediting): OpenMMLab image and video editing toolbox.
+        - [MMGeneration](https://github.com/open-mmlab/mmgeneration): OpenMMLab image and video generative models toolbox.
         - [MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab model deployment framework.
         
         <p align="right"><a href="#top">🔝Back to top</a></p>
         
 Keywords: computer vision,super resolution,video interpolation,inpainting,matting,SISR,RefSR,VSR,GAN,VFI
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
```

#### html2text {}

```diff
@@ -1,72 +1,73 @@
-Metadata-Version: 2.1 Name: mmedit Version: 1.0.0rc6 Summary: OpenMMLab Image
+Metadata-Version: 2.1 Name: mmedit Version: 1.0.0rc7 Summary: OpenMMLab Image
 and Video Editing Toolbox and Benchmark Home-page: https://github.com/open-
 mmlab/mmediting Maintainer: MMEditing Contributors Maintainer-email:
 openmmlab@gmail.com License: Apache License 2.0 Description:
                   [docs/en/_static/image/mmediting-logo.png]
                                         
            OpenMMLab website HOT      OpenMMLab platform TRY_IT_OUT
                                         
 [![PyPI](https://badge.fury.io/py/mmedit.svg)](https://pypi.org/project/mmedit/
       ) [![docs](https://img.shields.io/badge/docs-latest-blue)](https://
-  mmediting.readthedocs.io/en/1.x/) [![badge](https://github.com/open-mmlab/
+ mmediting.readthedocs.io/en/latest/) [![badge](https://github.com/open-mmlab/
 mmediting/workflows/build/badge.svg)](https://github.com/open-mmlab/mmediting/
 actions) [![codecov](https://codecov.io/gh/open-mmlab/mmediting/branch/master/
    graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmediting) [![license]
   (https://img.shields.io/github/license/open-mmlab/mmediting.svg)](https://
-  github.com/open-mmlab/mmediting/blob/1.x/LICENSE) [![open issues](https://
+  github.com/open-mmlab/mmediting/blob/main/LICENSE) [![open issues](https://
  isitmaintained.com/badge/open/open-mmlab/mmediting.svg)](https://github.com/
  open-mmlab/mmediting/issues) [![issue resolution](https://isitmaintained.com/
   badge/resolution/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/
-mmediting/issues) [ðDocumentation](https://mmediting.readthedocs.io/en/1.x/
-) | [ð ï¸Installation](https://mmediting.readthedocs.io/en/1.x/get_started/
-   install.html) | [ðModel Zoo](https://mmediting.readthedocs.io/en/1.x/
-model_zoo/overview.html) | [ðUpdate News](https://mmediting.readthedocs.io/
-en/1.x/changelog.html) | [ðOngoing Projects](https://github.com/open-mmlab/
-  mmediting/projects) | [ð¤Reporting Issues](https://github.com/open-mmlab/
-          mmediting/issues) English | [ç®ä½ä¸­æ](README_zh-CN.md)
+  mmediting/issues) [ðDocumentation](https://mmediting.readthedocs.io/en/
+ latest/) | [ð ï¸Installation](https://mmediting.readthedocs.io/en/latest/
+ get_started/install.html) | [ðModel Zoo](https://mmediting.readthedocs.io/
+        en/latest/model_zoo/overview.html) | [ðUpdate News](https://
+  mmediting.readthedocs.io/en/latest/changelog.html) | [ðOngoing Projects]
+  (https://github.com/open-mmlab/mmediting/projects) | [ð¤Reporting Issues]
+   (https://github.com/open-mmlab/mmediting/issues) English | [ç®ä½ä¸­æ]
+                               (README_zh-CN.md)
 
 ## ð What's New [https://user-images.githubusercontent.com/12782558/
 212848161-5e783dd6-11e8-4fe0-bbba-39ffb77730be.png] ### New release
-[**MMEditing v1.0.0rc6**](https://github.com/open-mmlab/mmediting/releases/tag/
-v1.0.0rc6) \[02/03/2023\]: - Support Gradio gui of Inpainting inference. -
-Support Colorization, Translationin and all GAN models inferencer.
-**MMEditing** has supported all the tasks, models, metrics, and losses in
-[MMGeneration](https://github.com/open-mmlab/mmgeneration) and unifies
-interfaces of all components based on [MMEngine](https://github.com/open-mmlab/
-mmengine) ð. Please refer to [changelog.md](docs/en/changelog.md) for
-details and release history. Please refer to [migration documents](docs/en/
-migration/overview.md) to migrate from [old version](https://github.com/open-
-mmlab/mmediting/tree/master) MMEditing 0.x to our brand new 1.x version. ##
-ð Table of Contents - [ð Introduction](#ð-introduction) - [ð
-Contributing](#ð-contributing) - [ð ï¸ Installation](#ð ï¸-
-installation) - [ð Model Zoo](#ð-model-zoo) - [ð¤ Acknowledgement]
-(#ð¤-acknowledgement) - [ðï¸ Citation](#ðï¸-citation) - [ð«
-License](#ð«-license) - [ðï¸ ï¸OpenMMLab Family](#ðï¸-ï¸openmmlab-
-family)
+[**MMEditing v1.0.0rc7**](https://github.com/open-mmlab/mmediting/releases/tag/
+v1.0.0rc7) \[07/04/2023\]: - Support DiffuserWrapper - Support ControlNet
+(training and inference). - Support PyTorch 2.0 (successfully compile 33+
+models on 'inductor' backend). **MMEditing** has supported all the tasks,
+models, metrics, and losses in [MMGeneration](https://github.com/open-mmlab/
+mmgeneration) and unifies interfaces of all components based on [MMEngine]
+(https://github.com/open-mmlab/mmengine) ð. Please refer to [changelog.md]
+(docs/en/changelog.md) for details and release history. Please refer to
+[migration documents](docs/en/migration/overview.md) to migrate from [old
+version](https://github.com/open-mmlab/mmediting/tree/master) MMEditing 0.x to
+our brand new 1.x version. ## ð Table of Contents - [ð Introduction]
+(#ð-introduction) - [ð Contributing](#ð-contributing) - [ð ï¸
+Installation](#ð ï¸-installation) - [ð Model Zoo](#ð-model-zoo) -
+[ð¤ Acknowledgement](#ð¤-acknowledgement) - [ðï¸ Citation](#ðï¸-
+citation) - [ð« License](#ð«-license) - [ðï¸ ï¸OpenMMLab Family]
+(#ðï¸-ï¸openmmlab-family)
                                                                 ðBack_to_top
 ## ð Introduction MMEditing is an open-source image and video
 editing&generating toolbox based on PyTorch. It is a part of the [OpenMMLab]
 (https://openmmlab.com/) project. Currently, MMEditing support multiple image
 and video generation/editing tasks. https://user-images.githubusercontent.com/
 12782558/217152698-49169038-9872-4200-80f7-1d5f7613afd7.mp4 The best practice
-on our main 1.x branch works with **Python 3.8+** and **PyTorch 1.9+**. ### â¨
+on our main branch works with **Python 3.8+** and **PyTorch 1.9+**. ### â¨
 Major features - **State of the Art** MMEditing provides state-of-the-art
 generative models to process, edit and synthesize images and videos. -
 **Powerful and Popular Applications** MMEditing supports popular and
 contemporary image restoration, text-to-image, 3D-aware generation, inpainting,
 matting, super-resolution and generation applications. Specifically, MMEditing
 supports GAN interpolation, GAN projection, GAN manipulations and many other
 popular GANâs applications. Itâs time to play with your GANs! - **New
 Modular Design for Flexible Combination** We decompose the editing framework
 into different modules and one can easily construct a customized editor
 framework by combining different modules. Specifically, a new design for
 complex loss modules is proposed for customizing the links between modules,
 which can achieve flexible combinations among different modules.(Tutorial for
-[losses](https://mmediting.readthedocs.io/en/dev-1.x/howto/losses.html)) -
+[losses](https://mmediting.readthedocs.io/en/latest/howto/losses.html)) -
 **Efficient Distributed Training** With the support of
 [MMSeparateDistributedDataParallel](https://github.com/open-mmlab/mmengine/
 blob/main/mmengine/model/wrappers/seperate_distributed.py), distributed
 training for dynamic architectures can be easily implemented.
                                                                 ðBack_to_top
 ## ð Contributing More and more community contributors are joining us to
 make our repo better. Some recent projects are contributed by the community
@@ -82,17 +83,17 @@
                                                                 ðBack_to_top
 ## ð ï¸ Installation MMEditing depends on [PyTorch](https://pytorch.org/),
 [MMEngine](https://github.com/open-mmlab/mmengine) and [MMCV](https://
 github.com/open-mmlab/mmcv). Below are quick steps for installation. **Step
 1.** Install PyTorch following [official instructions](https://pytorch.org/get-
 started/locally/). **Step 2.** Install MMCV with [MIM](https://github.com/open-
 mmlab/mim). ```shell pip3 install openmim # wait for more pre-compiled pkgs to
-release mim install 'mmcv>=2.0.0rc1' ``` **Step 3.** Install MMEditing from
-source. ```shell git clone -b 1.x https://github.com/open-mmlab/mmediting.git
-cd mmediting pip3 install -e . ``` Please refer to [installation](docs/en/
+release mim install 'mmcv>=2.0.0' ``` **Step 3.** Install MMEditing from
+source. ```shell git clone https://github.com/open-mmlab/mmediting.git cd
+mmediting pip3 install -e . ``` Please refer to [installation](docs/en/
 get_started/install.md) for more detailed instruction. **Getting Started**
 Please see [quick run](docs/en/get_started/quick_run.md) and [inference](docs/
 en/user_guides/inference.md) for the basic usage of MMEditing.
                                                                 ðBack_to_top
 ## ð Model Zoo
                              Supported algorithms
                                                                      Image Super-
@@ -130,74 +131,72 @@
     * IconVSR_
       (CVPR'2021)
     * BasicVSR++_
       (CVPR'2022)
     * RealBasicVSR
       (CVPR'2022)
       Inpainting            Matting           Text-to-Image    3D-aware Generation
-    * Global&Local     * DIM_               * GLIDE_               * EG3D_
-      (ToG'2017)         (CVPR'2017)          (NeurIPS'2021)         (CVPR'2022)
-    * DeepFillv1_      * IndexNet_          * Disco-Diffusion_
-      (CVPR'2018)        (ICCV'2019)          (2022)
-    * PConv_           * GCA_               * Stable-Diffusion
+    * Global&Local     * DIM_               * ControlNet_          * EG3D_
+      (ToG'2017)         (CVPR'2017)          (2023)                 (CVPR'2022)
+    * DeepFillv1_      * IndexNet_          * GLIDE_
+      (CVPR'2018)        (ICCV'2019)          (NeurIPS'2021)
+    * PConv_           * GCA_               * Disco-Diffusion_
       (ECCV'2018)        (AAAI'2020)          (2022)
-    * DeepFillv2_
-      (CVPR'2019)
+    * DeepFillv2_                           * Stable-Diffusion
+      (CVPR'2019)                             (2022)
     * AOT-GAN_
       (TVCG'2019)
-Please refer to [model_zoo](https://mmediting.readthedocs.io/en/1.x/model_zoo/
-overview.html) for more details.
+Please refer to [model_zoo](https://mmediting.readthedocs.io/en/latest/
+model_zoo/overview.html) for more details.
                                                                 ðBack_to_top
 ## ð¤ Acknowledgement MMEditing is an open source project that is contributed
 by researchers and engineers from various colleges and companies. We wish that
 the toolbox and benchmark could serve the growing research community by
 providing a flexible toolkit to reimplement existing methods and develop their
 own new methods. We appreciate all the contributors who implement their methods
 or add new features, as well as users who give valuable feedbacks. Thank you
-all! [https://contrib.rocks/image?repo=liuwenran/mmediting]
+all! [https://contrib.rocks/image?repo=open-mmlab/mmediting]
                                                                 ðBack_to_top
 ## ðï¸ Citation If MMEditing is helpful to your research, please cite it as
 below. ```bibtex @misc{mmediting2022, title = {{MMEditing}: {OpenMMLab} Image
 and Video Editing Toolbox}, author = {{MMEditing Contributors}}, howpublished =
 {\url{https://github.com/open-mmlab/mmediting}}, year = {2022} } ```
                                                                 ðBack_to_top
 ## ð« License This project is released under the [Apache 2.0 license]
 (LICENSE). Please refer to [LICENSES](LICENSE) for the careful check, if you
 are using our code for commercial matters.
                                                                 ðBack_to_top
 ## ðï¸ ï¸OpenMMLab Family - [MMEngine](https://github.com/open-mmlab/
 mmengine): OpenMMLab foundational library for training deep learning models. -
-[MMCV](https://github.com/open-mmlab/mmcv/tree/2.x): OpenMMLab foundational
-library for computer vision. - [MIM](https://github.com/open-mmlab/mim): MIM
-installs OpenMMLab packages. - [MMClassification](https://github.com/open-
-mmlab/mmclassification/tree/1.x): OpenMMLab image classification toolbox and
-benchmark. - [MMDetection](https://github.com/open-mmlab/mmdetection/tree/3.x):
-OpenMMLab detection toolbox and benchmark. - [MMDetection3D](https://
-github.com/open-mmlab/mmdetection3d/tree/1.x): OpenMMLab's next-generation
-platform for general 3D object detection. - [MMRotate](https://github.com/open-
-mmlab/mmrotate/tree/1.x): OpenMMLab rotated object detection toolbox and
-benchmark. - [MMSegmentation](https://github.com/open-mmlab/mmsegmentation/
-tree/1.x): OpenMMLab semantic segmentation toolbox and benchmark. - [MMOCR]
-(https://github.com/open-mmlab/mmocr/tree/1.x): OpenMMLab text detection,
-recognition, and understanding toolbox. - [MMPose](https://github.com/open-
-mmlab/mmpose/tree/1.x): OpenMMLab pose estimation toolbox and benchmark. -
-[MMHuman3D](https://github.com/open-mmlab/mmhuman3d/tree/1.x): OpenMMLab 3D
-human parametric model toolbox and benchmark. - [MMSelfSup](https://github.com/
-open-mmlab/mmselfsup/tree/1.x): OpenMMLab self-supervised learning toolbox and
-benchmark. - [MMRazor](https://github.com/open-mmlab/mmrazor/tree/1.x):
-OpenMMLab model compression toolbox and benchmark. - [MMFewShot](https://
-github.com/open-mmlab/mmfewshot/tree/1.x): OpenMMLab fewshot learning toolbox
-and benchmark. - [MMAction2](https://github.com/open-mmlab/mmaction2/tree/1.x):
-OpenMMLab's next-generation action understanding toolbox and benchmark. -
-[MMTracking](https://github.com/open-mmlab/mmtracking/tree/1.x): OpenMMLab
-video perception toolbox and benchmark. - [MMFlow](https://github.com/open-
-mmlab/mmflow/tree/1.x): OpenMMLab optical flow toolbox and benchmark. -
-[MMEditing](https://github.com/open-mmlab/mmediting/tree/1.x): OpenMMLab image
-and video editing toolbox. - [MMGeneration](https://github.com/open-mmlab/
-mmgeneration/tree/1.x): OpenMMLab image and video generative models toolbox. -
+[MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for
+computer vision. - [MIM](https://github.com/open-mmlab/mim): MIM installs
+OpenMMLab packages. - [MMClassification](https://github.com/open-mmlab/
+mmclassification): OpenMMLab image classification toolbox and benchmark. -
+[MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection
+toolbox and benchmark. - [MMDetection3D](https://github.com/open-mmlab/
+mmdetection3d): OpenMMLab's next-generation platform for general 3D object
+detection. - [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab
+rotated object detection toolbox and benchmark. - [MMSegmentation](https://
+github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox
+and benchmark. - [MMOCR](https://github.com/open-mmlab/mmocr): OpenMMLab text
+detection, recognition, and understanding toolbox. - [MMPose](https://
+github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
+- [MMHuman3D](https://github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human
+parametric model toolbox and benchmark. - [MMSelfSup](https://github.com/open-
+mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox and benchmark. -
+[MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab model compression
+toolbox and benchmark. - [MMFewShot](https://github.com/open-mmlab/mmfewshot):
+OpenMMLab fewshot learning toolbox and benchmark. - [MMAction2](https://
+github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action
+understanding toolbox and benchmark. - [MMTracking](https://github.com/open-
+mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark. - [MMFlow]
+(https://github.com/open-mmlab/mmflow): OpenMMLab optical flow toolbox and
+benchmark. - [MMEditing](https://github.com/open-mmlab/mmediting): OpenMMLab
+image and video editing toolbox. - [MMGeneration](https://github.com/open-
+mmlab/mmgeneration): OpenMMLab image and video generative models toolbox. -
 [MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab model deployment
 framework.
                                                                 ðBack_to_top
 Keywords: computer vision,super resolution,video
 interpolation,inpainting,matting,SISR,RefSR,VSR,GAN,VFI Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta Classifier: Intended Audience ::
 Developers Classifier: Intended Audience :: Education Classifier: Intended
```

### Comparing `mmedit-1.0.0rc6/README.md` & `mmedit-1.0.0rc7/README.md`

 * *Files 11% similar despite different names*

```diff
@@ -15,25 +15,25 @@
         <i><font size="4">TRY IT OUT</font></i>
       </a>
     </sup>
   </div>
   <div>&nbsp;</div>
 
 [![PyPI](https://badge.fury.io/py/mmedit.svg)](https://pypi.org/project/mmedit/)
-[![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmediting.readthedocs.io/en/1.x/)
+[![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmediting.readthedocs.io/en/latest/)
 [![badge](https://github.com/open-mmlab/mmediting/workflows/build/badge.svg)](https://github.com/open-mmlab/mmediting/actions)
 [![codecov](https://codecov.io/gh/open-mmlab/mmediting/branch/master/graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmediting)
-[![license](https://img.shields.io/github/license/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/blob/1.x/LICENSE)
+[![license](https://img.shields.io/github/license/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/blob/main/LICENSE)
 [![open issues](https://isitmaintained.com/badge/open/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/issues)
 [![issue resolution](https://isitmaintained.com/badge/resolution/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/issues)
 
-[📘Documentation](https://mmediting.readthedocs.io/en/1.x/) |
-[🛠️Installation](https://mmediting.readthedocs.io/en/1.x/get_started/install.html) |
-[📊Model Zoo](https://mmediting.readthedocs.io/en/1.x/model_zoo/overview.html) |
-[🆕Update News](https://mmediting.readthedocs.io/en/1.x/changelog.html) |
+[📘Documentation](https://mmediting.readthedocs.io/en/latest/) |
+[🛠️Installation](https://mmediting.readthedocs.io/en/latest/get_started/install.html) |
+[📊Model Zoo](https://mmediting.readthedocs.io/en/latest/model_zoo/overview.html) |
+[🆕Update News](https://mmediting.readthedocs.io/en/latest/changelog.html) |
 [🚀Ongoing Projects](https://github.com/open-mmlab/mmediting/projects) |
 [🤔Reporting Issues](https://github.com/open-mmlab/mmediting/issues)
 
 English | [简体中文](README_zh-CN.md)
 
 </div>
 
@@ -49,18 +49,19 @@
   <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
   <a href="https://www.youtube.com/openmmlab" style="text-decoration:none;">
     <img src="https://user-images.githubusercontent.com/25839884/218346691-ceb2116a-465a-40af-8424-9f30d2348ca9.png" width="3%" alt="" /></a>
 </div>
 
 ## 🚀 What's New <a><img width="35" height="20" src="https://user-images.githubusercontent.com/12782558/212848161-5e783dd6-11e8-4fe0-bbba-39ffb77730be.png"></a>
 
-### New release [**MMEditing v1.0.0rc6**](https://github.com/open-mmlab/mmediting/releases/tag/v1.0.0rc6) \[02/03/2023\]:
+### New release [**MMEditing v1.0.0rc7**](https://github.com/open-mmlab/mmediting/releases/tag/v1.0.0rc7) \[07/04/2023\]:
 
-- Support Gradio gui of Inpainting inference.
-- Support Colorization, Translationin and all GAN models inferencer.
+- Support DiffuserWrapper
+- Support ControlNet (training and inference).
+- Support PyTorch 2.0 (successfully compile 33+ models on 'inductor' backend).
 
 **MMEditing** has supported all the tasks, models, metrics, and losses in [MMGeneration](https://github.com/open-mmlab/mmgeneration) and unifies interfaces of all components based on [MMEngine](https://github.com/open-mmlab/mmengine) 😍.
 
 Please refer to [changelog.md](docs/en/changelog.md) for details and release history.
 
 Please refer to [migration documents](docs/en/migration/overview.md) to migrate from [old version](https://github.com/open-mmlab/mmediting/tree/master) MMEditing 0.x to our brand new 1.x version.
 
@@ -81,29 +82,29 @@
 
 MMEditing is an open-source image and video editing&generating toolbox based on PyTorch. It is a part of the [OpenMMLab](https://openmmlab.com/) project.
 
 Currently, MMEditing support multiple image and video generation/editing tasks.
 
 https://user-images.githubusercontent.com/12782558/217152698-49169038-9872-4200-80f7-1d5f7613afd7.mp4
 
-The best practice on our main 1.x branch works with **Python 3.8+** and **PyTorch 1.9+**.
+The best practice on our main branch works with **Python 3.8+** and **PyTorch 1.9+**.
 
 ### ✨ Major features
 
 - **State of the Art**
 
   MMEditing provides state-of-the-art generative models to process, edit and synthesize images and videos.
 
 - **Powerful and Popular Applications**
 
   MMEditing supports popular and contemporary image restoration, text-to-image, 3D-aware generation, inpainting, matting, super-resolution and generation applications. Specifically, MMEditing supports GAN interpolation, GAN projection, GAN manipulations and many other popular GAN’s applications. It’s time to play with your GANs!
 
 - **New Modular Design for Flexible Combination**
 
-  We decompose the editing framework into different modules and one can easily construct a customized editor framework by combining different modules. Specifically, a new design for complex loss modules is proposed for customizing the links between modules, which can achieve flexible combinations among different modules.(Tutorial for [losses](https://mmediting.readthedocs.io/en/dev-1.x/howto/losses.html))
+  We decompose the editing framework into different modules and one can easily construct a customized editor framework by combining different modules. Specifically, a new design for complex loss modules is proposed for customizing the links between modules, which can achieve flexible combinations among different modules.(Tutorial for [losses](https://mmediting.readthedocs.io/en/latest/howto/losses.html))
 
 - **Efficient Distributed Training**
 
   With the support of [MMSeparateDistributedDataParallel](https://github.com/open-mmlab/mmengine/blob/main/mmengine/model/wrappers/seperate_distributed.py), distributed training for dynamic architectures can be easily implemented.
 
 <p align="right"><a href="#top">🔝Back to top</a></p>
 
@@ -131,22 +132,22 @@
 
 **Step 2.**
 Install MMCV with [MIM](https://github.com/open-mmlab/mim).
 
 ```shell
 pip3 install openmim
 # wait for more pre-compiled pkgs to release
-mim install 'mmcv>=2.0.0rc1'
+mim install 'mmcv>=2.0.0'
 ```
 
 **Step 3.**
 Install MMEditing from source.
 
 ```shell
-git clone -b 1.x https://github.com/open-mmlab/mmediting.git
+git clone https://github.com/open-mmlab/mmediting.git
 cd mmediting
 pip3 install -e .
 ```
 
 Please refer to [installation](docs/en/get_started/install.md) for more detailed instruction.
 
 **Getting Started**
@@ -301,14 +302,15 @@
           <li><a href="configs/dim/README.md">DIM (CVPR'2017)</a></li>
           <li><a href="configs/indexnet/README.md">IndexNet (ICCV'2019)</a></li>
           <li><a href="configs/mask2former">GCA (AAAI'2020)</a></li>
         </ul>
       </td>
       <td>
         <ul>
+          <li><a href="configs/controlnet/README.md">ControlNet (2023)</a></li>
           <li><a href="projects/glide/configs/README.md">GLIDE (NeurIPS'2021)</a></li>
           <li><a href="configs/disco_diffusion/README.md">Disco-Diffusion (2022)</a></li>
           <li><a href="configs/stable_diffusion/README.md">Stable-Diffusion (2022)</a></li>
         </ul>
       </td>
       <td>
         <ul>
@@ -317,26 +319,26 @@
       </td>
     </tr>
 </td>
     </tr>
   </tbody>
 </table>
 
-Please refer to [model_zoo](https://mmediting.readthedocs.io/en/1.x/model_zoo/overview.html) for more details.
+Please refer to [model_zoo](https://mmediting.readthedocs.io/en/latest/model_zoo/overview.html) for more details.
 
 <p align="right"><a href="#top">🔝Back to top</a></p>
 
 ## 🤝 Acknowledgement
 
 MMEditing is an open source project that is contributed by researchers and engineers from various colleges and companies. We wish that the toolbox and benchmark could serve the growing research community by providing a flexible toolkit to reimplement existing methods and develop their own new methods.
 
 We appreciate all the contributors who implement their methods or add new features, as well as users who give valuable feedbacks. Thank you all!
 
 <a href="https://github.com/open-mmlab/mmediting/graphs/contributors">
-  <img src="https://contrib.rocks/image?repo=liuwenran/mmediting" />
+  <img src="https://contrib.rocks/image?repo=open-mmlab/mmediting" />
 </a>
 
 <p align="right"><a href="#top">🔝Back to top</a></p>
 
 ## 🖊️ Citation
 
 If MMEditing is helpful to your research, please cite it as below.
@@ -358,28 +360,28 @@
 Please refer to [LICENSES](LICENSE) for the careful check, if you are using our code for commercial matters.
 
 <p align="right"><a href="#top">🔝Back to top</a></p>
 
 ## 🏗️ ️OpenMMLab Family
 
 - [MMEngine](https://github.com/open-mmlab/mmengine): OpenMMLab foundational library for training deep learning models.
-- [MMCV](https://github.com/open-mmlab/mmcv/tree/2.x): OpenMMLab foundational library for computer vision.
+- [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for computer vision.
 - [MIM](https://github.com/open-mmlab/mim): MIM installs OpenMMLab packages.
-- [MMClassification](https://github.com/open-mmlab/mmclassification/tree/1.x): OpenMMLab image classification toolbox and benchmark.
-- [MMDetection](https://github.com/open-mmlab/mmdetection/tree/3.x): OpenMMLab detection toolbox and benchmark.
-- [MMDetection3D](https://github.com/open-mmlab/mmdetection3d/tree/1.x): OpenMMLab's next-generation platform for general 3D object detection.
-- [MMRotate](https://github.com/open-mmlab/mmrotate/tree/1.x): OpenMMLab rotated object detection toolbox and benchmark.
-- [MMSegmentation](https://github.com/open-mmlab/mmsegmentation/tree/1.x): OpenMMLab semantic segmentation toolbox and benchmark.
-- [MMOCR](https://github.com/open-mmlab/mmocr/tree/1.x): OpenMMLab text detection, recognition, and understanding toolbox.
-- [MMPose](https://github.com/open-mmlab/mmpose/tree/1.x): OpenMMLab pose estimation toolbox and benchmark.
-- [MMHuman3D](https://github.com/open-mmlab/mmhuman3d/tree/1.x): OpenMMLab 3D human parametric model toolbox and benchmark.
-- [MMSelfSup](https://github.com/open-mmlab/mmselfsup/tree/1.x): OpenMMLab self-supervised learning toolbox and benchmark.
-- [MMRazor](https://github.com/open-mmlab/mmrazor/tree/1.x): OpenMMLab model compression toolbox and benchmark.
-- [MMFewShot](https://github.com/open-mmlab/mmfewshot/tree/1.x): OpenMMLab fewshot learning toolbox and benchmark.
-- [MMAction2](https://github.com/open-mmlab/mmaction2/tree/1.x): OpenMMLab's next-generation action understanding toolbox and benchmark.
-- [MMTracking](https://github.com/open-mmlab/mmtracking/tree/1.x): OpenMMLab video perception toolbox and benchmark.
-- [MMFlow](https://github.com/open-mmlab/mmflow/tree/1.x): OpenMMLab optical flow toolbox and benchmark.
-- [MMEditing](https://github.com/open-mmlab/mmediting/tree/1.x): OpenMMLab image and video editing toolbox.
-- [MMGeneration](https://github.com/open-mmlab/mmgeneration/tree/1.x): OpenMMLab image and video generative models toolbox.
+- [MMClassification](https://github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
+- [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection toolbox and benchmark.
+- [MMDetection3D](https://github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for general 3D object detection.
+- [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab rotated object detection toolbox and benchmark.
+- [MMSegmentation](https://github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox and benchmark.
+- [MMOCR](https://github.com/open-mmlab/mmocr): OpenMMLab text detection, recognition, and understanding toolbox.
+- [MMPose](https://github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
+- [MMHuman3D](https://github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human parametric model toolbox and benchmark.
+- [MMSelfSup](https://github.com/open-mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox and benchmark.
+- [MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab model compression toolbox and benchmark.
+- [MMFewShot](https://github.com/open-mmlab/mmfewshot): OpenMMLab fewshot learning toolbox and benchmark.
+- [MMAction2](https://github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action understanding toolbox and benchmark.
+- [MMTracking](https://github.com/open-mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark.
+- [MMFlow](https://github.com/open-mmlab/mmflow): OpenMMLab optical flow toolbox and benchmark.
+- [MMEditing](https://github.com/open-mmlab/mmediting): OpenMMLab image and video editing toolbox.
+- [MMGeneration](https://github.com/open-mmlab/mmgeneration): OpenMMLab image and video generative models toolbox.
 - [MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab model deployment framework.
 
 <p align="right"><a href="#top">🔝Back to top</a></p>
```

#### html2text {}

```diff
@@ -1,68 +1,69 @@
                   [docs/en/_static/image/mmediting-logo.png]
                                         
            OpenMMLab website HOT      OpenMMLab platform TRY_IT_OUT
                                         
 [![PyPI](https://badge.fury.io/py/mmedit.svg)](https://pypi.org/project/mmedit/
       ) [![docs](https://img.shields.io/badge/docs-latest-blue)](https://
-  mmediting.readthedocs.io/en/1.x/) [![badge](https://github.com/open-mmlab/
+ mmediting.readthedocs.io/en/latest/) [![badge](https://github.com/open-mmlab/
 mmediting/workflows/build/badge.svg)](https://github.com/open-mmlab/mmediting/
 actions) [![codecov](https://codecov.io/gh/open-mmlab/mmediting/branch/master/
    graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmediting) [![license]
   (https://img.shields.io/github/license/open-mmlab/mmediting.svg)](https://
-  github.com/open-mmlab/mmediting/blob/1.x/LICENSE) [![open issues](https://
+  github.com/open-mmlab/mmediting/blob/main/LICENSE) [![open issues](https://
  isitmaintained.com/badge/open/open-mmlab/mmediting.svg)](https://github.com/
  open-mmlab/mmediting/issues) [![issue resolution](https://isitmaintained.com/
   badge/resolution/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/
-mmediting/issues) [ðDocumentation](https://mmediting.readthedocs.io/en/1.x/
-) | [ð ï¸Installation](https://mmediting.readthedocs.io/en/1.x/get_started/
-   install.html) | [ðModel Zoo](https://mmediting.readthedocs.io/en/1.x/
-model_zoo/overview.html) | [ðUpdate News](https://mmediting.readthedocs.io/
-en/1.x/changelog.html) | [ðOngoing Projects](https://github.com/open-mmlab/
-  mmediting/projects) | [ð¤Reporting Issues](https://github.com/open-mmlab/
-          mmediting/issues) English | [ç®ä½ä¸­æ](README_zh-CN.md)
+  mmediting/issues) [ðDocumentation](https://mmediting.readthedocs.io/en/
+ latest/) | [ð ï¸Installation](https://mmediting.readthedocs.io/en/latest/
+ get_started/install.html) | [ðModel Zoo](https://mmediting.readthedocs.io/
+        en/latest/model_zoo/overview.html) | [ðUpdate News](https://
+  mmediting.readthedocs.io/en/latest/changelog.html) | [ðOngoing Projects]
+  (https://github.com/open-mmlab/mmediting/projects) | [ð¤Reporting Issues]
+   (https://github.com/open-mmlab/mmediting/issues) English | [ç®ä½ä¸­æ]
+                               (README_zh-CN.md)
 
 ## ð What's New [https://user-images.githubusercontent.com/12782558/
 212848161-5e783dd6-11e8-4fe0-bbba-39ffb77730be.png] ### New release
-[**MMEditing v1.0.0rc6**](https://github.com/open-mmlab/mmediting/releases/tag/
-v1.0.0rc6) \[02/03/2023\]: - Support Gradio gui of Inpainting inference. -
-Support Colorization, Translationin and all GAN models inferencer.
-**MMEditing** has supported all the tasks, models, metrics, and losses in
-[MMGeneration](https://github.com/open-mmlab/mmgeneration) and unifies
-interfaces of all components based on [MMEngine](https://github.com/open-mmlab/
-mmengine) ð. Please refer to [changelog.md](docs/en/changelog.md) for
-details and release history. Please refer to [migration documents](docs/en/
-migration/overview.md) to migrate from [old version](https://github.com/open-
-mmlab/mmediting/tree/master) MMEditing 0.x to our brand new 1.x version. ##
-ð Table of Contents - [ð Introduction](#ð-introduction) - [ð
-Contributing](#ð-contributing) - [ð ï¸ Installation](#ð ï¸-
-installation) - [ð Model Zoo](#ð-model-zoo) - [ð¤ Acknowledgement]
-(#ð¤-acknowledgement) - [ðï¸ Citation](#ðï¸-citation) - [ð«
-License](#ð«-license) - [ðï¸ ï¸OpenMMLab Family](#ðï¸-ï¸openmmlab-
-family)
+[**MMEditing v1.0.0rc7**](https://github.com/open-mmlab/mmediting/releases/tag/
+v1.0.0rc7) \[07/04/2023\]: - Support DiffuserWrapper - Support ControlNet
+(training and inference). - Support PyTorch 2.0 (successfully compile 33+
+models on 'inductor' backend). **MMEditing** has supported all the tasks,
+models, metrics, and losses in [MMGeneration](https://github.com/open-mmlab/
+mmgeneration) and unifies interfaces of all components based on [MMEngine]
+(https://github.com/open-mmlab/mmengine) ð. Please refer to [changelog.md]
+(docs/en/changelog.md) for details and release history. Please refer to
+[migration documents](docs/en/migration/overview.md) to migrate from [old
+version](https://github.com/open-mmlab/mmediting/tree/master) MMEditing 0.x to
+our brand new 1.x version. ## ð Table of Contents - [ð Introduction]
+(#ð-introduction) - [ð Contributing](#ð-contributing) - [ð ï¸
+Installation](#ð ï¸-installation) - [ð Model Zoo](#ð-model-zoo) -
+[ð¤ Acknowledgement](#ð¤-acknowledgement) - [ðï¸ Citation](#ðï¸-
+citation) - [ð« License](#ð«-license) - [ðï¸ ï¸OpenMMLab Family]
+(#ðï¸-ï¸openmmlab-family)
                                                                 ðBack_to_top
 ## ð Introduction MMEditing is an open-source image and video
 editing&generating toolbox based on PyTorch. It is a part of the [OpenMMLab]
 (https://openmmlab.com/) project. Currently, MMEditing support multiple image
 and video generation/editing tasks. https://user-images.githubusercontent.com/
 12782558/217152698-49169038-9872-4200-80f7-1d5f7613afd7.mp4 The best practice
-on our main 1.x branch works with **Python 3.8+** and **PyTorch 1.9+**. ### â¨
+on our main branch works with **Python 3.8+** and **PyTorch 1.9+**. ### â¨
 Major features - **State of the Art** MMEditing provides state-of-the-art
 generative models to process, edit and synthesize images and videos. -
 **Powerful and Popular Applications** MMEditing supports popular and
 contemporary image restoration, text-to-image, 3D-aware generation, inpainting,
 matting, super-resolution and generation applications. Specifically, MMEditing
 supports GAN interpolation, GAN projection, GAN manipulations and many other
 popular GANâs applications. Itâs time to play with your GANs! - **New
 Modular Design for Flexible Combination** We decompose the editing framework
 into different modules and one can easily construct a customized editor
 framework by combining different modules. Specifically, a new design for
 complex loss modules is proposed for customizing the links between modules,
 which can achieve flexible combinations among different modules.(Tutorial for
-[losses](https://mmediting.readthedocs.io/en/dev-1.x/howto/losses.html)) -
+[losses](https://mmediting.readthedocs.io/en/latest/howto/losses.html)) -
 **Efficient Distributed Training** With the support of
 [MMSeparateDistributedDataParallel](https://github.com/open-mmlab/mmengine/
 blob/main/mmengine/model/wrappers/seperate_distributed.py), distributed
 training for dynamic architectures can be easily implemented.
                                                                 ðBack_to_top
 ## ð Contributing More and more community contributors are joining us to
 make our repo better. Some recent projects are contributed by the community
@@ -78,17 +79,17 @@
                                                                 ðBack_to_top
 ## ð ï¸ Installation MMEditing depends on [PyTorch](https://pytorch.org/),
 [MMEngine](https://github.com/open-mmlab/mmengine) and [MMCV](https://
 github.com/open-mmlab/mmcv). Below are quick steps for installation. **Step
 1.** Install PyTorch following [official instructions](https://pytorch.org/get-
 started/locally/). **Step 2.** Install MMCV with [MIM](https://github.com/open-
 mmlab/mim). ```shell pip3 install openmim # wait for more pre-compiled pkgs to
-release mim install 'mmcv>=2.0.0rc1' ``` **Step 3.** Install MMEditing from
-source. ```shell git clone -b 1.x https://github.com/open-mmlab/mmediting.git
-cd mmediting pip3 install -e . ``` Please refer to [installation](docs/en/
+release mim install 'mmcv>=2.0.0' ``` **Step 3.** Install MMEditing from
+source. ```shell git clone https://github.com/open-mmlab/mmediting.git cd
+mmediting pip3 install -e . ``` Please refer to [installation](docs/en/
 get_started/install.md) for more detailed instruction. **Getting Started**
 Please see [quick run](docs/en/get_started/quick_run.md) and [inference](docs/
 en/user_guides/inference.md) for the basic usage of MMEditing.
                                                                 ðBack_to_top
 ## ð Model Zoo
                              Supported algorithms
                                                                      Image Super-
@@ -126,70 +127,68 @@
     * IconVSR_
       (CVPR'2021)
     * BasicVSR++_
       (CVPR'2022)
     * RealBasicVSR
       (CVPR'2022)
       Inpainting            Matting           Text-to-Image    3D-aware Generation
-    * Global&Local     * DIM_               * GLIDE_               * EG3D_
-      (ToG'2017)         (CVPR'2017)          (NeurIPS'2021)         (CVPR'2022)
-    * DeepFillv1_      * IndexNet_          * Disco-Diffusion_
-      (CVPR'2018)        (ICCV'2019)          (2022)
-    * PConv_           * GCA_               * Stable-Diffusion
+    * Global&Local     * DIM_               * ControlNet_          * EG3D_
+      (ToG'2017)         (CVPR'2017)          (2023)                 (CVPR'2022)
+    * DeepFillv1_      * IndexNet_          * GLIDE_
+      (CVPR'2018)        (ICCV'2019)          (NeurIPS'2021)
+    * PConv_           * GCA_               * Disco-Diffusion_
       (ECCV'2018)        (AAAI'2020)          (2022)
-    * DeepFillv2_
-      (CVPR'2019)
+    * DeepFillv2_                           * Stable-Diffusion
+      (CVPR'2019)                             (2022)
     * AOT-GAN_
       (TVCG'2019)
-Please refer to [model_zoo](https://mmediting.readthedocs.io/en/1.x/model_zoo/
-overview.html) for more details.
+Please refer to [model_zoo](https://mmediting.readthedocs.io/en/latest/
+model_zoo/overview.html) for more details.
                                                                 ðBack_to_top
 ## ð¤ Acknowledgement MMEditing is an open source project that is contributed
 by researchers and engineers from various colleges and companies. We wish that
 the toolbox and benchmark could serve the growing research community by
 providing a flexible toolkit to reimplement existing methods and develop their
 own new methods. We appreciate all the contributors who implement their methods
 or add new features, as well as users who give valuable feedbacks. Thank you
-all! [https://contrib.rocks/image?repo=liuwenran/mmediting]
+all! [https://contrib.rocks/image?repo=open-mmlab/mmediting]
                                                                 ðBack_to_top
 ## ðï¸ Citation If MMEditing is helpful to your research, please cite it as
 below. ```bibtex @misc{mmediting2022, title = {{MMEditing}: {OpenMMLab} Image
 and Video Editing Toolbox}, author = {{MMEditing Contributors}}, howpublished =
 {\url{https://github.com/open-mmlab/mmediting}}, year = {2022} } ```
                                                                 ðBack_to_top
 ## ð« License This project is released under the [Apache 2.0 license]
 (LICENSE). Please refer to [LICENSES](LICENSE) for the careful check, if you
 are using our code for commercial matters.
                                                                 ðBack_to_top
 ## ðï¸ ï¸OpenMMLab Family - [MMEngine](https://github.com/open-mmlab/
 mmengine): OpenMMLab foundational library for training deep learning models. -
-[MMCV](https://github.com/open-mmlab/mmcv/tree/2.x): OpenMMLab foundational
-library for computer vision. - [MIM](https://github.com/open-mmlab/mim): MIM
-installs OpenMMLab packages. - [MMClassification](https://github.com/open-
-mmlab/mmclassification/tree/1.x): OpenMMLab image classification toolbox and
-benchmark. - [MMDetection](https://github.com/open-mmlab/mmdetection/tree/3.x):
-OpenMMLab detection toolbox and benchmark. - [MMDetection3D](https://
-github.com/open-mmlab/mmdetection3d/tree/1.x): OpenMMLab's next-generation
-platform for general 3D object detection. - [MMRotate](https://github.com/open-
-mmlab/mmrotate/tree/1.x): OpenMMLab rotated object detection toolbox and
-benchmark. - [MMSegmentation](https://github.com/open-mmlab/mmsegmentation/
-tree/1.x): OpenMMLab semantic segmentation toolbox and benchmark. - [MMOCR]
-(https://github.com/open-mmlab/mmocr/tree/1.x): OpenMMLab text detection,
-recognition, and understanding toolbox. - [MMPose](https://github.com/open-
-mmlab/mmpose/tree/1.x): OpenMMLab pose estimation toolbox and benchmark. -
-[MMHuman3D](https://github.com/open-mmlab/mmhuman3d/tree/1.x): OpenMMLab 3D
-human parametric model toolbox and benchmark. - [MMSelfSup](https://github.com/
-open-mmlab/mmselfsup/tree/1.x): OpenMMLab self-supervised learning toolbox and
-benchmark. - [MMRazor](https://github.com/open-mmlab/mmrazor/tree/1.x):
-OpenMMLab model compression toolbox and benchmark. - [MMFewShot](https://
-github.com/open-mmlab/mmfewshot/tree/1.x): OpenMMLab fewshot learning toolbox
-and benchmark. - [MMAction2](https://github.com/open-mmlab/mmaction2/tree/1.x):
-OpenMMLab's next-generation action understanding toolbox and benchmark. -
-[MMTracking](https://github.com/open-mmlab/mmtracking/tree/1.x): OpenMMLab
-video perception toolbox and benchmark. - [MMFlow](https://github.com/open-
-mmlab/mmflow/tree/1.x): OpenMMLab optical flow toolbox and benchmark. -
-[MMEditing](https://github.com/open-mmlab/mmediting/tree/1.x): OpenMMLab image
-and video editing toolbox. - [MMGeneration](https://github.com/open-mmlab/
-mmgeneration/tree/1.x): OpenMMLab image and video generative models toolbox. -
+[MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for
+computer vision. - [MIM](https://github.com/open-mmlab/mim): MIM installs
+OpenMMLab packages. - [MMClassification](https://github.com/open-mmlab/
+mmclassification): OpenMMLab image classification toolbox and benchmark. -
+[MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection
+toolbox and benchmark. - [MMDetection3D](https://github.com/open-mmlab/
+mmdetection3d): OpenMMLab's next-generation platform for general 3D object
+detection. - [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab
+rotated object detection toolbox and benchmark. - [MMSegmentation](https://
+github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox
+and benchmark. - [MMOCR](https://github.com/open-mmlab/mmocr): OpenMMLab text
+detection, recognition, and understanding toolbox. - [MMPose](https://
+github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
+- [MMHuman3D](https://github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human
+parametric model toolbox and benchmark. - [MMSelfSup](https://github.com/open-
+mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox and benchmark. -
+[MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab model compression
+toolbox and benchmark. - [MMFewShot](https://github.com/open-mmlab/mmfewshot):
+OpenMMLab fewshot learning toolbox and benchmark. - [MMAction2](https://
+github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action
+understanding toolbox and benchmark. - [MMTracking](https://github.com/open-
+mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark. - [MMFlow]
+(https://github.com/open-mmlab/mmflow): OpenMMLab optical flow toolbox and
+benchmark. - [MMEditing](https://github.com/open-mmlab/mmediting): OpenMMLab
+image and video editing toolbox. - [MMGeneration](https://github.com/open-
+mmlab/mmgeneration): OpenMMLab image and video generative models toolbox. -
 [MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab model deployment
 framework.
                                                                 ðBack_to_top
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/basicvsr_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/basicvsr_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/celeba.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/celeba.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/cifar10_noaug.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/cifar10_noaug.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/cifar10_nopad.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/cifar10_nopad.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/comp1k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/comp1k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/deblurring-defocus_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/deblurring-defocus_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/deblurring-motion_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/deblurring-motion_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/decompression_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/decompression_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/denoising-gaussian_color_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/denoising-gaussian_color_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/denoising-gaussian_gray_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/denoising-gaussian_gray_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/denoising-real_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/denoising-real_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/deraining_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/deraining_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/ffhq_flip.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/ffhq_flip.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/grow_scale_imgs_ffhq_styleganv1.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/grow_scale_imgs_ffhq_styleganv1.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/imagenet_128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/imagenet_128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/imagenet_256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/imagenet_256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/imagenet_512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/imagenet_512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/imagenet_64.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/imagenet_64.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/imagenet_noaug_128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/imagenet_noaug_128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/liif_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/liif_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/lsun_stylegan.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/lsun_stylegan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/paired_imgs_256x256_crop.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/paired_imgs_256x256_crop.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/places.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/places.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/sisr_x2_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/sisr_x2_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/sisr_x3_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/sisr_x3_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/sisr_x4_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/sisr_x4_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/tdan_test_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/tdan_test_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_64x64.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_64x64.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_flip_512x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_flip_512x512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_flip_lanczos_resize_256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/unconditional_imgs_flip_lanczos_resize_256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/datasets/unpaired_imgs_256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/datasets/unpaired_imgs_256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/default_runtime.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/default_runtime.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/gen_default_runtime.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/gen_default_runtime.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/inpaint_default_runtime.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/inpaint_default_runtime.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/matting_default_runtime.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/matting_default_runtime.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_cyclegan.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_cyclegan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_deepfillv1.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_deepfillv1.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_deepfillv2.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_deepfillv2.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_edvr.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_edvr.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_gl.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_gl.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_glean.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_glean.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_liif.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_liif.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_pconv.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_pconv.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_pix2pix.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_pix2pix.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_styleganv2.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_styleganv2.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_styleganv3.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_styleganv3.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/base_tof.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/base_tof.py`

 * *Files 4% similar despite different names*

```diff
@@ -31,15 +31,15 @@
 
 train_dataloader = dict(
     num_workers=4,
     persistent_workers=False,
     sampler=dict(type='InfiniteSampler', shuffle=True),
     dataset=dict(
         type=train_dataset_type,
-        ann_file='tri_testlist.txt',
+        ann_file='tri_trainlist.txt',
         metainfo=dict(dataset_type='vimeo90k', task_name='vfi'),
         data_root=data_root,
         data_prefix=dict(img='sequences', gt='sequences'),
         pipeline=train_pipeline,
         depth=2,
         load_frames_list=dict(img=['im1.png', 'im3.png'], gt=['im2.png'])))
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/biggan/base_biggan_128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/biggan/base_biggan_128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/sagan/base_sagan_128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/sagan/base_sagan_128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/_base_/models/sagan/base_sagan_32x32.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/_base_/models/sagan/base_sagan_32x32.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/aot_gan/aot-gan_smpgan_4xb4_places-512x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/aot_gan/aot-gan_smpgan_4xb4_places-512x512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/aot_gan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/aot_gan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr/basicvsr_2xb4_reds4.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr/basicvsr_2xb4_reds4.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr/basicvsr_2xb4_vimeo90k-bd.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr/basicvsr_2xb4_vimeo90k-bd.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-decompress-track1.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-decompress-track1.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-vsr.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c128n25_600k_ntire-vsr.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_4xb2-300k_vimeo90k-bd.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_4xb2-300k_vimeo90k-bd.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_4xb2-300k_vimeo90k-bi.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_4xb2-300k_vimeo90k-bi.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_8xb1-600k_reds4.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/basicvsr-pp_c64n7_8xb1-600k_reds4.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/basicvsr_pp/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/basicvsr_pp/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face-rgb_imagenet1k-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face-rgb_imagenet1k-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face_rgb_imagenet1k-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face_rgb_imagenet1k-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face_rgb_imagenet1k-512x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face_rgb_imagenet1k-512x512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan_2xb25-500kiters_cifar10-32x32.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan_2xb25-500kiters_cifar10-32x32.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan_ajbrock-sn_8xb32-1500kiters_imagenet1k-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan_ajbrock-sn_8xb32-1500kiters_imagenet1k-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/biggan_cvt-BigGAN-PyTorch-rgb_imagenet1k-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/biggan_cvt-BigGAN-PyTorch-rgb_imagenet1k-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/biggan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/biggan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/cain/cain_g1b32_1xb5_vimeo90k-triplet.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/cain/cain_g1b32_1xb5_vimeo90k-triplet.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/cain/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/cain/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-250kiters_summer2winter.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-250kiters_summer2winter.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-270kiters_horse2zebra.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-270kiters_horse2zebra.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-80kiters_facades.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-80kiters_facades.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-250kiters_summer2winter.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-250kiters_summer2winter.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-270kiters_horse2zebra.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-270kiters_horse2zebra.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-80kiters_facades.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-80kiters_facades.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/cyclegan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/cyclegan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/dcgan/dcgan_1xb128-300kiters_celeba-cropped-64.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/dcgan/dcgan_1xb128-300kiters_celeba-cropped-64.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/dcgan/dcgan_1xb128-5epoches_lsun-bedroom-64x64.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/dcgan/dcgan_1xb128-5epoches_lsun-bedroom-64x64.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/dcgan/dcgan_Glr4e-4_Dlr1e-4_1xb128-5kiters_mnist-64x64.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/dcgan/dcgan_Glr4e-4_Dlr1e-4_1xb128-5kiters_mnist-64x64.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/dcgan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/dcgan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv1/deepfillv1_4xb4_celeba-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv1/deepfillv1_4xb4_celeba-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv1/deepfillv1_8xb2_places-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv1/deepfillv1_8xb2_places-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv1/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv1/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv2/deepfillv2_8xb2_celeba-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv2/deepfillv2_8xb2_celeba-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv2/deepfillv2_8xb2_places-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv2/deepfillv2_8xb2_places-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/deepfillv2/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/deepfillv2/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/dic/dic_gan-x8c48b6_4xb2-500k_celeba-hq.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/dic/dic_gan-x8c48b6_4xb2-500k_celeba-hq.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/dic/dic_x8c48b6_4xb2-150k_celeba-hq.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/dic/dic_x8c48b6_4xb2-150k_celeba-hq.py`

 * *Files 3% similar despite different names*

```diff
@@ -74,14 +74,38 @@
         output_keys=['img'],
         interpolation='bicubic',
         backend='pillow'),
     dict(type='PackEditInputs')
 ]
 test_pipeline = valid_pipeline
 
+inference_pipeline = [
+    dict(
+        type='LoadImageFromFile',
+        key='img',
+        color_type='color',
+        channel_order='rgb',
+        imdecode_backend='cv2'),
+    dict(
+        type='Resize',
+        scale=(128, 128),
+        keys=['img'],
+        interpolation='bicubic',
+        backend='pillow'),
+    dict(
+        type='Resize',
+        scale=1 / 8,
+        keep_ratio=True,
+        keys=['img'],
+        output_keys=['img'],
+        interpolation='bicubic',
+        backend='pillow'),
+    dict(type='PackEditInputs')
+]
+
 # dataset settings
 dataset_type = 'BasicImageDataset'
 data_root = 'data'
 
 train_dataloader = dict(
     num_workers=4,
     batch_size=2,  # gpus 4
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/dic/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/dic/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/dim/dim_stage1-v16_1xb1-1000k_comp1k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/dim/dim_stage1-v16_1xb1-1000k_comp1k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/dim/dim_stage1-v16_1xb1-1000k_comp1k_online-merge.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/dim/dim_stage1-v16_1xb1-1000k_comp1k_online-merge.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/dim/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/dim/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/disco_diffusion/disco-diffusion_adm-u-finetuned_imagenet-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/disco_diffusion/disco-diffusion_adm-u-finetuned_imagenet-256x256.py`

 * *Files 4% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 pretrained_cfgs = dict(
     unet=dict(ckpt_path=unet_ckpt_path, prefix='unet'),
     secondary_model=dict(ckpt_path=secondary_model_ckpt_path, prefix=''))
 
 secondary_model = dict(type='SecondaryDiffusionImageNet2')
 
 diffusion_scheduler = dict(
-    type='DDIMScheduler',
+    type='EditDDIMScheduler',
     variance_type='learned_range',
     beta_schedule='linear',
     clip_sample=False)
 
 clip_models = [
     dict(type='ClipWrapper', clip_type='clip', name='ViT-B/32', jit=False),
     dict(type='ClipWrapper', clip_type='clip', name='ViT-B/16', jit=False),
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/disco_diffusion/disco-diffusion_adm-u-finetuned_imagenet-512x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/disco_diffusion/disco-diffusion_adm-u-finetuned_imagenet-512x512.py`

 * *Files 8% similar despite different names*

```diff
@@ -22,15 +22,15 @@
 pretrained_cfgs = dict(
     unet=dict(ckpt_path=unet_ckpt_path, prefix='unet'),
     secondary_model=dict(ckpt_path=secondary_model_ckpt_path, prefix=''))
 
 secondary_model = dict(type='SecondaryDiffusionImageNet2')
 
 diffusion_scheduler = dict(
-    type='DDIMScheduler',
+    type='EditDDIMScheduler',
     variance_type='learned_range',
     beta_schedule='linear',
     clip_sample=False)
 
 clip_models = [
     dict(type='ClipWrapper', clip_type='clip', name='ViT-B/32', jit=False),
     dict(type='ClipWrapper', clip_type='clip', name='ViT-B/16', jit=False),
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/disco_diffusion/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/disco_diffusion/metafile.yml`

 * *Files 23% similar despite different names*

```diff
@@ -3,34 +3,33 @@
   Paper:
     Title: Disco Diffusion
     URL: https://github.com/alembics/disco-diffusion
   README: configs/disco_diffusion/README.md
   Task:
   - text2image
   - image2image
-  - diffusion
   Year: 2022
 Models:
 - Config: configs/disco_diffusion/disco-diffusion_adm-u-finetuned_imagenet-512x512.py
   In Collection: Disco Diffusion
   Name: disco-diffusion_adm-u-finetuned_imagenet-512x512
   Results:
   - Dataset: ImageNet
     Metrics: {}
-    Task: Text2Image, Image2Image, diffusion
+    Task: Text2Image, Image2Image
   Weights: https://download.openmmlab.com/mmediting/synthesizers/disco/adm-u_finetuned_imagenet-512x512-ab471d70.pth
 - Config: configs/disco_diffusion/disco-diffusion_adm-u-finetuned_imagenet-256x256.py
   In Collection: Disco Diffusion
   Name: disco-diffusion_adm-u-finetuned_imagenet-256x256
   Results:
   - Dataset: ImageNet
     Metrics: {}
-    Task: Text2Image, Image2Image, diffusion
+    Task: Text2Image, Image2Image
   Weights: <>
 - Config: configs/disco_diffusion/disco-diffusion_portrait-generator-v001.py
   In Collection: Disco Diffusion
   Name: disco-diffusion_portrait-generator-v001
   Results:
   - Dataset: unknown
     Metrics: {}
-    Task: Text2Image, Image2Image, diffusion
+    Task: Text2Image, Image2Image
   Weights: https://download.openmmlab.com/mmediting/synthesizers/disco/adm-u-cvt-rgb_portrait-v001-f4a3f3bc.pth
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/edsr/edsr_x2c64b16_1xb16-300k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/edsr/edsr_x2c64b16_1xb16-300k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/edsr/edsr_x3c64b16_1xb16-300k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/edsr/edsr_x3c64b16_1xb16-300k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/edsr/edsr_x4c64b16_1xb16-300k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/edsr/edsr_x4c64b16_1xb16-300k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/edsr/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/edsr/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/edvr/edvrl_c128b40_8xb8-lr2e-4-600k_reds4.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/edvr/edvrl_c128b40_8xb8-lr2e-4-600k_reds4.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/edvr/edvrl_wotsa-c128b40_8xb8-lr2e-4-600k_reds4.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/edvr/edvrl_wotsa-c128b40_8xb8-lr2e-4-600k_reds4.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/edvr/edvrm_8xb4-600k_reds.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/edvr/edvrm_8xb4-600k_reds.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/edvr/edvrm_wotsa_8xb4-600k_reds.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/edvr/edvrm_wotsa_8xb4-600k_reds.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/edvr/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/edvr/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_afhq-512x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_afhq-512x512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_ffhq-512x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_ffhq-512x512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_shapenet-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/eg3d/eg3d_cvt-official-rgb_shapenet-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/eg3d/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/eg3d/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/esrgan/esrgan_psnr-x4c64b23g32_1xb16-1000k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/esrgan/esrgan_psnr-x4c64b23g32_1xb16-1000k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/esrgan/esrgan_x4c64b23g32_1xb16-400k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/esrgan/esrgan_x4c64b23g32_1xb16-400k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/esrgan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/esrgan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/flavr/flavr_in4out1_8xb4_vimeo90k-septuplet.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/flavr/flavr_in4out1_8xb4_vimeo90k-septuplet.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/flavr/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/flavr/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/gca/baseline_r34_4xb10-200k_comp1k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/gca/baseline_r34_4xb10-200k_comp1k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/gca/baseline_r34_4xb10-dimaug-200k_comp1k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/gca/baseline_r34_4xb10-dimaug-200k_comp1k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/gca/gca_r34_4xb10-200k_comp1k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/gca/gca_r34_4xb10-200k_comp1k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/gca/gca_r34_4xb10-dimaug-200k_comp1k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/gca/gca_r34_4xb10-dimaug-200k_comp1k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/gca/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/gca/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/ggan/ggan_dcgan-archi_lr1e-3-1xb128-12Mimgs_celeba-cropped-64x64.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/ggan/ggan_dcgan-archi_lr1e-3-1xb128-12Mimgs_celeba-cropped-64x64.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/ggan/ggan_dcgan-archi_lr1e-4-1xb64-10Mimgs_celeba-cropped-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/ggan/ggan_dcgan-archi_lr1e-4-1xb64-10Mimgs_celeba-cropped-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/ggan/ggan_lsgan-archi_lr1e-4-1xb128-20Mimgs_lsun-bedroom-64x64.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/ggan/ggan_lsgan-archi_lr1e-4-1xb128-20Mimgs_lsun-bedroom-64x64.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/ggan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/ggan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/glean/glean_in128out1024_4xb2-300k_ffhq-celeba-hq.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/glean/glean_in128out1024_4xb2-300k_ffhq-celeba-hq.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/glean/glean_x16_2xb8_cat.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/glean/glean_x16_2xb8_cat.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/glean/glean_x16_2xb8_ffhq.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/glean/glean_x16_2xb8_ffhq.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/glean/glean_x8_2xb8_cat.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/glean/glean_x8_2xb8_cat.py`

 * *Files 3% similar despite different names*

```diff
@@ -81,14 +81,29 @@
         type='LoadImageFromFile',
         key='gt',
         color_type='color',
         channel_order='rgb'),
     dict(type='PackEditInputs')
 ]
 
+inference_pipeline = [
+    dict(
+        type='LoadImageFromFile',
+        key='img',
+        color_type='color',
+        channel_order='rgb'),
+    dict(
+        type='Resize',
+        scale=(32, 32),
+        keys=['img'],
+        interpolation='bicubic',
+        backend='pillow'),
+    dict(type='PackEditInputs')
+]
+
 # dataset settings
 dataset_type = 'BasicImageDataset'
 
 train_dataloader = dict(
     num_workers=8,
     batch_size=8,
     persistent_workers=False,
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/glean/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/glean/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/global_local/gl_8xb12_celeba-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/global_local/gl_8xb12_celeba-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/global_local/gl_8xb12_places-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/global_local/gl_8xb12_places-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/global_local/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/global_local/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-512x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-512x512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-64x64.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm-g_ddim25_8xb32_imagenet-64x64.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-512x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-512x512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-64x64.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/adm_ddim250_8xb32_imagenet-64x64.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/guided_diffusion/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/guided_diffusion/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_reds4.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_reds4.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_vimeo90k-bd.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_vimeo90k-bd.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_vimeo90k-bi.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/iconvsr/iconvsr_2xb4_vimeo90k-bi.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/iconvsr/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/iconvsr/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/indexnet/indexnet_mobv2-dimaug_1xb16-78k_comp1k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/indexnet/indexnet_mobv2-dimaug_1xb16-78k_comp1k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/indexnet/indexnet_mobv2_1xb16-78k_comp1k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/indexnet/indexnet_mobv2_1xb16-78k_comp1k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/indexnet/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/indexnet/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/inst_colorization/inst-colorizatioon_full_official_cocostuff-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/inst_colorization/inst-colorizatioon_full_official_cocostuff-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/inst_colorization/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/inst_colorization/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/liif/liif-edsr-norm_c64b16_1xb16-1000k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/liif/liif-edsr-norm_c64b16_1xb16-1000k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/liif/liif-rdn-norm_c64b16_1xb16-1000k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/liif/liif-rdn-norm_c64b16_1xb16-1000k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/liif/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/liif/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-3-1xb128-12Mimgs_celeba-cropped-64x64.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-3-1xb128-12Mimgs_celeba-cropped-64x64.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-4-1xb128-12Mimgs_lsun-bedroom-64x64.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-4-1xb128-12Mimgs_lsun-bedroom-64x64.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-4-1xb64-10Mimgs_celeba-cropped-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/lsgan/lsgan_dcgan-archi_lr1e-4-1xb64-10Mimgs_celeba-cropped-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/lsgan/lsgan_lsgan-archi_lr1e-4-1xb64-10Mimgs_lsun-bedroom-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/lsgan/lsgan_lsgan-archi_lr1e-4-1xb64-10Mimgs_lsun-bedroom-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/lsgan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/lsgan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/nafnet/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/nafnet/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/nafnet/nafnet_c64eb11128mb1db1111_8xb8-lr1e-3-400k_gopro.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/nafnet/nafnet_c64eb11128mb1db1111_8xb8-lr1e-3-400k_gopro.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,13 @@
 _base_ = '../_base_/default_runtime.py'
 
 experiment_name = 'nafnet_c64eb11128mb1db1111_lr1e-3_400k_gopro'
 work_dir = f'./work_dirs/{experiment_name}'
 save_dir = './work_dirs/'
 
-# DistributedDataParallel
-model_wrapper_cfg = dict(type='MMSeparateDistributedDataParallel')
-
 # model settings
 model = dict(
     type='BaseEditModel',
     generator=dict(
         type='NAFNetLocal',
         img_channels=3,
         mid_channels=64,
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/nafnet/nafnet_c64eb2248mb12db2222_8xb8-lr1e-3-400k_sidd.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/nafnet/nafnet_c64eb2248mb12db2222_8xb8-lr1e-3-400k_sidd.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,13 @@
 _base_ = '../_base_/default_runtime.py'
 
 experiment_name = 'nafnet_c64eb2248mb12db2222_lr1e-3_400k_sidd'
 work_dir = f'./work_dirs/{experiment_name}'
 save_dir = './work_dirs/'
 
-# DistributedDataParallel
-model_wrapper_cfg = dict(type='MMSeparateDistributedDataParallel')
-
 # model settings
 model = dict(
     type='BaseEditModel',
     generator=dict(
         type='NAFNet',
         img_channels=3,
         mid_channels=64,
@@ -90,19 +87,17 @@
 train_cfg = dict(
     type='IterBasedTrainLoop', max_iters=400_000, val_interval=20000)
 val_cfg = dict(type='EditValLoop')
 test_cfg = dict(type='EditTestLoop')
 
 # optimizer
 optim_wrapper = dict(
-    constructor='MultiOptimWrapperConstructor',
-    generator=dict(
-        type='OptimWrapper',
-        optimizer=dict(
-            type='AdamW', lr=1e-3, weight_decay=1e-3, betas=(0.9, 0.9))))
+    constructor='DefaultOptimWrapperConstructor',
+    type='OptimWrapper',
+    optimizer=dict(type='AdamW', lr=1e-3, weight_decay=1e-3, betas=(0.9, 0.9)))
 
 # learning policy
 param_scheduler = dict(
     type='CosineAnnealingLR', by_epoch=False, T_max=400_000, eta_min=1e-7)
 
 default_hooks = dict(
     checkpoint=dict(
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/partial_conv/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/partial_conv/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/partial_conv/pconv_stage1_8xb12_places-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/partial_conv/pconv_stage1_8xb12_places-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/partial_conv/pconv_stage1_8xb1_celeba-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/partial_conv/pconv_stage1_8xb1_celeba-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/partial_conv/pconv_stage2_4xb2_celeba-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/partial_conv/pconv_stage2_4xb2_celeba-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/partial_conv/pconv_stage2_4xb2_places-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/partial_conv/pconv_stage2_4xb2_places-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/pggan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/pggan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/pggan/pggan_8xb4-12Mimg_celeba-hq-1024x1024.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/pggan/pggan_8xb4-12Mimg_celeba-hq-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/pggan/pggan_8xb4-12Mimgs_celeba-cropped-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/pggan/pggan_8xb4-12Mimgs_celeba-cropped-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/pix2pix/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/pix2pix/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-220kiters_aerial2maps.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-220kiters_aerial2maps.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-220kiters_maps2aerial.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-220kiters_maps2aerial.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-80kiters_facades.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_1xb1-80kiters_facades.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_wo-jitter-flip-1xb4-190kiters_edges2shoes.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/pix2pix/pix2pix_vanilla-unet-bn_wo-jitter-flip-1xb4-190kiters_edges2shoes.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-c_c2_8xb3-1100kiters_ffhq-256-512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-c_c2_8xb3-1100kiters_ffhq-256-512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-d_c2_8xb3-1100kiters_ffhq-256-512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-d_c2_8xb3-1100kiters_ffhq-256-512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-e_c2_8xb3-1100kiters_ffhq-256-512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-e_c2_8xb3-1100kiters_ffhq-256-512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c1_8xb2-1600kiters_ffhq-256-1024.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c1_8xb2-1600kiters_ffhq-256-1024.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c2_8xb3-1100kiters_ffhq-256-512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c2_8xb3-1100kiters_ffhq-256-512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c2_8xb3-1100kiters_ffhq-256-896.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-f_c2_8xb3-1100kiters_ffhq-256-896.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-g_c1_8xb3-1100kiters_ffhq-256-512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-g_c1_8xb3-1100kiters_ffhq-256-512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-h_c2_8xb3-1100kiters_ffhq-256-512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-h_c2_8xb3-1100kiters_ffhq-256-512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-i_c2_8xb3-1100kiters_ffhq-256-512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-i_c2_8xb3-1100kiters_ffhq-256-512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-j_c2_8xb3-1100kiters_ffhq-256-512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-j_c2_8xb3-1100kiters_ffhq-256-512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-k_c2_8xb3-1100kiters_ffhq-256-512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/mspie-stylegan2-config-k_c2_8xb3-1100kiters_ffhq-256-512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan-csg_bohemian.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan-csg_bohemian.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan-csg_fish.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan-csg_fish.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim4_bohemian.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim4_bohemian.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim4_fish.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim4_fish.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim8_bohemian.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/singan_spe-dim8_bohemian.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/stylegan2_c2_8xb3-1100kiters_ffhq-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/stylegan2_c2_8xb3-1100kiters_ffhq-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/positional_encoding_in_gans/stylegan2_c2_8xb3-1100kiters_ffhq-512x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/positional_encoding_in_gans/stylegan2_c2_8xb3-1100kiters_ffhq-512x512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/rdn/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/rdn/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/rdn/rdn_x2c64b16_1xb16-1000k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/rdn/rdn_x2c64b16_1xb16-1000k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/rdn/rdn_x3c64b16_1xb16-1000k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/rdn/rdn_x3c64b16_1xb16-1000k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/rdn/rdn_x4c64b16_1xb16-1000k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/rdn/rdn_x4c64b16_1xb16-1000k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/real_basicvsr/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/real_basicvsr/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/real_basicvsr/realbasicvsr_c64b20-1x30x8_8xb1-lr5e-5-150k_reds.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/real_basicvsr/realbasicvsr_c64b20-1x30x8_8xb1-lr5e-5-150k_reds.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/real_basicvsr/realbasicvsr_wogan-c64b20-2x30x8_8xb2-lr1e-4-300k_reds.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/real_basicvsr/realbasicvsr_wogan-c64b20-2x30x8_8xb2-lr1e-4-300k_reds.py`

 * *Files 1% similar despite different names*

```diff
@@ -210,14 +210,20 @@
         interval_list=[1],
         filename_tmpl='{:08d}.png'),
     dict(type='LoadImageFromFile', key='gt', channel_order='rgb'),
     dict(type='LoadImageFromFile', key='img', channel_order='rgb'),
     dict(type='PackEditInputs')
 ]
 
+demo_pipeline = [
+    dict(type='GenerateSegmentIndices', interval_list=[1]),
+    dict(type='LoadImageFromFile', key='img', channel_order='rgb'),
+    dict(type='PackEditInputs')
+]
+
 data_root = 'data'
 
 train_dataloader = dict(
     num_workers=10,
     batch_size=2,
     persistent_workers=False,
     sampler=dict(type='InfiniteSampler', shuffle=True),
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/real_esrgan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/real_esrgan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/real_esrgan/realesrgan_c64b23g32_4xb12-lr1e-4-400k_df2k-ost.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/real_esrgan/realesrgan_c64b23g32_4xb12-lr1e-4-400k_df2k-ost.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/real_esrgan/realesrnet_c64b23g32_4xb12-lr2e-4-1000k_df2k-ost.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/real_esrgan/realesrnet_c64b23g32_4xb12-lr2e-4-1000k_df2k-ost.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma15.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma15.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma25.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma25.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma50.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-color-sigma50.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma15.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma15.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma25.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma25.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma50.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dfwb-gray-sigma50.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dpdd-dual.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dpdd-dual.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_dpdd-single.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_dpdd-single.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_gopro.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_gopro.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_rain13k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_rain13k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/restormer/restormer_official_sidd.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/restormer/restormer_official_sidd.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_128_cvt_studioGAN.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_128_cvt_studioGAN.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_cvt-studioGAN_cifar10-32x32.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_cvt-studioGAN_cifar10-32x32.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_wReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_wReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_woReLUinplace-Glr1e-4_Dlr4e-4_noaug-ndisc1-8xb32-bigGAN-sch_imagenet1k-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_woReLUinplace-Glr1e-4_Dlr4e-4_noaug-ndisc1-8xb32-bigGAN-sch_imagenet1k-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_woReLUinplace_Glr1e-4_Dlr4e-4_ndisc1-4xb64_imagenet1k-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_woReLUinplace_Glr1e-4_Dlr4e-4_ndisc1-4xb64_imagenet1k-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sagan/sagan_woReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sagan/sagan_woReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/singan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/singan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/singan/singan_balloons.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/singan/singan_balloons.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/singan/singan_bohemian.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/singan/singan_bohemian.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/singan/singan_fish.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/singan/singan_fish.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj-cvt-studioGAN_cifar10-32x32.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj-cvt-studioGAN_cifar10-32x32.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj-cvt-studioGAN_imagenet1k-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj-cvt-studioGAN_imagenet1k-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj_wReLUinplace_Glr2e-4_Dlr5e-5_ndisc5-2xb128_imagenet1k-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj_wReLUinplace_Glr2e-4_Dlr5e-5_ndisc5-2xb128_imagenet1k-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj_wReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj_wReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj_woReLUinplace_Glr2e-4_Dlr5e-5_ndisc5-2xb128_imagenet1k-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj_woReLUinplace_Glr2e-4_Dlr5e-5_ndisc5-2xb128_imagenet1k-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/sngan_proj/sngan-proj_woReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/sngan_proj/sngan-proj_woReLUinplace_lr2e-4-ndisc5-1xb64_cifar10-32x32.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/srcnn/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/srcnn/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/srcnn/srcnn_x4k915_1xb16-1000k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/srcnn/srcnn_x4k915_1xb16-1000k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/srgan_resnet/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/srgan_resnet/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/srgan_resnet/msrresnet_x4c64b16_1xb16-1000k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/srgan_resnet/msrresnet_x4c64b16_1xb16-1000k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/srgan_resnet/srgan_x4c64b16_1xb16-1000k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/srgan_resnet/srgan_x4c64b16_1xb16-1000k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/stable_diffusion/stable-diffusion_ddim_denoisingunet.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/stable_diffusion/stable-diffusion_ddim_denoisingunet.py`

 * *Files 22% similar despite different names*

```diff
@@ -16,14 +16,15 @@
     up_block_types=[
         'UpBlock2D', 'CrossAttnUpBlock2D', 'CrossAttnUpBlock2D',
         'CrossAttnUpBlock2D'
     ],
     output_cfg=dict(var='fixed'))
 
 vae = dict(
+    type='EditAutoencoderKL',
     act_fn='silu',
     block_out_channels=[128, 256, 512, 512],
     down_block_types=[
         'DownEncoderBlock2D', 'DownEncoderBlock2D', 'DownEncoderBlock2D',
         'DownEncoderBlock2D'
     ],
     in_channels=3,
@@ -34,25 +35,28 @@
     sample_size=512,
     up_block_types=[
         'UpDecoderBlock2D', 'UpDecoderBlock2D', 'UpDecoderBlock2D',
         'UpDecoderBlock2D'
     ])
 
 diffusion_scheduler = dict(
-    type='DDIMScheduler',
+    type='EditDDIMScheduler',
     variance_type='learned_range',
     beta_end=0.012,
     beta_schedule='scaled_linear',
     beta_start=0.00085,
     num_train_timesteps=1000,
     set_alpha_to_one=False,
     clip_sample=False)
 
-init_cfg = dict(type='Pretrained', pretrained_model_path='')
-
 model = dict(
     type='StableDiffusion',
-    diffusion_scheduler=diffusion_scheduler,
     unet=unet,
     vae=vae,
-    init_cfg=init_cfg,
-)
+    text_encoder=dict(
+        type='ClipWrapper',
+        clip_type='huggingface',
+        pretrained_model_name_or_path='runwayml/stable-diffusion-v1-5',
+        subfolder='text_encoder'),
+    tokenizer='runwayml/stable-diffusion-v1-5',
+    scheduler=diffusion_scheduler,
+    test_scheduler=diffusion_scheduler)
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv1/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv1/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv1/styleganv1_ffhq-1024x1024_8xb4-25Mimgs.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv1/styleganv1_ffhq-1024x1024_8xb4-25Mimgs.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv1/styleganv1_ffhq-256x256_8xb4-25Mimgs.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv1/styleganv1_ffhq-256x256_8xb4-25Mimgs.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_ffhq-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_ffhq-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-cat-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-cat-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-church-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-church-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-horse-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4-800kiters_lsun-horse-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4_ffhq-1024x1024.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4_ffhq-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4_lsun-car-384x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv2/stylegan2_c2_8xb4_lsun-car-384x512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-r_ada-gamma3.3_8xb4-fp16_metfaces-1024x1024.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-r_ada-gamma3.3_8xb4-fp16_metfaces-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4_ffhq-1024x1024.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4_ffhq-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4_ffhqu-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4_ffhqu-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4x8_afhqv2-512x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-r_cvt-official-rgb_8xb4x8_afhqv2-512x512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_ada-gamma6.6_8xb4-fp16_metfaces-1024x1024.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_ada-gamma6.6_8xb4-fp16_metfaces-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_afhqv2-512x512.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_afhqv2-512x512.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_ffhq-1024x1024.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_ffhq-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_ffhqu-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_cvt-official-rgb_8xb4_ffhqu-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_gamma2.0_8xb4-fp16-noaug_ffhq-256x256.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_gamma2.0_8xb4-fp16-noaug_ffhq-256x256.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/styleganv3/stylegan3-t_gamma32.8_8xb4-fp16-noaug_ffhq-1024x1024.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/styleganv3/stylegan3-t_gamma32.8_8xb4-fp16-noaug_ffhq-1024x1024.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_psnr-x2s64w8d6e180_8xb4-lr1e-4-600k_df2k-ost.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_psnr-x2s64w8d6e180_8xb4-lr1e-4-600k_df2k-ost.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR10.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR10.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR20.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR20.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR30.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR30.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR40.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-colorCAR40.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR10.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR10.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR20.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR20.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR30.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR30.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR40.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s126w7d6e180_8xb1-lr2e-4-1600k_dfwb-grayCAR40.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN15.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN15.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN25.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN25.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN50.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-colorDN50.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN15.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN15.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN25.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN25.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN50.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_s128w8d6e180_8xb1-lr2e-4-1600k_dfwb-grayDN50.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x2s48w8d6e180_8xb4-lr2e-4-500k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x2s48w8d6e180_8xb4-lr2e-4-500k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x2s64w8d4e60_8xb4-lr2e-4-500k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x2s64w8d4e60_8xb4-lr2e-4-500k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x2s64w8d6e180_8xb4-lr2e-4-500k_df2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x2s64w8d6e180_8xb4-lr2e-4-500k_df2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x3s48w8d6e180_8xb4-lr2e-4-500k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x3s48w8d6e180_8xb4-lr2e-4-500k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x3s64w8d4e60_8xb4-lr2e-4-500k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x3s64w8d4e60_8xb4-lr2e-4-500k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x3s64w8d6e180_8xb4-lr2e-4-500k_df2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x3s64w8d6e180_8xb4-lr2e-4-500k_df2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x4s48w8d6e180_8xb4-lr2e-4-500k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x4s48w8d6e180_8xb4-lr2e-4-500k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x4s64w8d4e60_8xb4-lr2e-4-500k_div2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x4s64w8d4e60_8xb4-lr2e-4-500k_div2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/swinir/swinir_x4s64w8d6e180_8xb4-lr2e-4-500k_df2k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/swinir/swinir_x4s64w8d6e180_8xb4-lr2e-4-500k_df2k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/tdan/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/tdan/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/tdan/tdan_x4_8xb16-lr1e-4-400k_vimeo90k-bd.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/tdan/tdan_x4_8xb16-lr1e-4-400k_vimeo90k-bd.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/tdan/tdan_x4ft_8xb16-lr5e-5-800k_vimeo90k-bd.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/tdan/tdan_x4ft_8xb16-lr5e-5-800k_vimeo90k-bd.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/tof/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/tof/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_spynet-chair-wobn_1xb1_vimeo90k-triplet.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_spynet-chair-wobn_1xb1_vimeo90k-triplet.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_spynet-kitti-wobn_1xb1_vimeo90k-triplet.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_spynet-kitti-wobn_1xb1_vimeo90k-triplet.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_spynet-pytoflow-wobn_1xb1_vimeo90k-triplet.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_spynet-pytoflow-wobn_1xb1_vimeo90k-triplet.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_spynet-sintel-wobn-clean_1xb1_vimeo90k-triplet.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_spynet-sintel-wobn-clean_1xb1_vimeo90k-triplet.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_spynet-sintel-wobn-final_1xb1_vimeo90k-triplet.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_spynet-sintel-wobn-final_1xb1_vimeo90k-triplet.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/tof/tof_x4_official_vimeo90k.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/tof/tof_x4_official_vimeo90k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/ttsr/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/ttsr/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/ttsr/ttsr-gan_x4c64b16_1xb9-500k_CUFED.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/ttsr/ttsr-gan_x4c64b16_1xb9-500k_CUFED.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/ttsr/ttsr-rec_x4c64b16_1xb9-200k_CUFED.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/ttsr/ttsr-rec_x4c64b16_1xb9-200k_CUFED.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/wgan-gp/metafile.yml` & `mmedit-1.0.0rc7/mmedit/.mim/configs/wgan-gp/metafile.yml`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/configs/wgan-gp/wgangp_GN_1xb64-160kiters_celeba-cropped-128x128.py` & `mmedit-1.0.0rc7/mmedit/.mim/configs/wgan-gp/wgangp_GN_1xb64-160kiters_celeba-cropped-128x128.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/colorization_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/colorization_demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/conditional_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/conditional_demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/download_inference_resources.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/download_inference_resources.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/gradio-demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/gradio-demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/inpainting_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/inpainting_demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/matting_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/matting_demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/mmediting_inference_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/mmediting_inference_demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/restoration_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/restoration_demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/restoration_face_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/restoration_face_demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/restoration_video_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/restoration_video_demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/singan_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/singan_demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/translation_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/translation_demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/unconditional_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/unconditional_demo.py`

 * *Files 3% similar despite different names*

```diff
@@ -65,15 +65,17 @@
 
     if args.sample_cfg is None:
         args.sample_cfg = dict()
 
     results = sample_unconditional_model(model, args.num_samples,
                                          args.num_batches, args.sample_model,
                                          **args.sample_cfg)
-    results = (results[:, [2, 1, 0]] + 1.) / 2.
+
+    results = results / 255
+    results = results[:, [2, 1, 0]]
 
     # save images
     mmengine.mkdir_or_exist(os.path.dirname(args.save_path))
     utils.save_image(
         results, args.save_path, nrow=args.nrow, padding=args.padding)
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/demo/video_interpolation_demo.py` & `mmedit-1.0.0rc7/mmedit/.mim/demo/video_interpolation_demo.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/model-index.yml` & `mmedit-1.0.0rc7/mmedit/.mim/model-index.yml`

 * *Files 5% similar despite different names*

```diff
@@ -1,13 +1,14 @@
 Import:
 - configs/aot_gan/metafile.yml
 - configs/basicvsr/metafile.yml
 - configs/basicvsr_pp/metafile.yml
 - configs/biggan/metafile.yml
 - configs/cain/metafile.yml
+- configs/controlnet/metafile.yml
 - configs/cyclegan/metafile.yml
 - configs/dcgan/metafile.yml
 - configs/deepfillv1/metafile.yml
 - configs/deepfillv2/metafile.yml
 - configs/dic/metafile.yml
 - configs/dim/metafile.yml
 - configs/disco_diffusion/metafile.yml
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/analysis_tools/print_config.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/analysis_tools/print_config.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/bgm/preprocess_bgm_dataset.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/bgm/preprocess_bgm_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/comp1k/check_extended_fg.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/comp1k/check_extended_fg.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/comp1k/evaluate_comp1k.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/comp1k/evaluate_comp1k.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/comp1k/extend_fg.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/comp1k/extend_fg.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/comp1k/filter_comp1k_anno.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/comp1k/filter_comp1k_anno.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/comp1k/preprocess_comp1k_dataset.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/comp1k/preprocess_comp1k_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/df2k_ost/preprocess_df2k_ost_dataset.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/df2k_ost/preprocess_df2k_ost_dataset.py`

 * *Files 5% similar despite different names*

```diff
@@ -4,17 +4,31 @@
 import os.path as osp
 import sys
 from multiprocessing import Pool
 
 import cv2
 import lmdb
 import mmcv
+import mmengine
 import numpy as np
 
 
+def generate_anno_file(args):
+    """Generate annotation file for DF2K_OST datasets from the ground-truth
+    folder."""
+
+    print('Generate annotation files ...')
+    txt_file = osp.join(args.data_root, args.anno_path)
+    mmengine.utils.mkdir_or_exist(osp.dirname(txt_file))
+    img_list = sorted(os.listdir(osp.join(args.data_root, 'GT_sub')))
+    with open(txt_file, 'w') as f:
+        for img in img_list:
+            f.write(f'{img} ({args.crop_size}, {args.crop_size}, 3)\n')
+
+
 def main_extract_subimages(args):
     """A multi-thread tool to crop large images to sub-images for faster IO.
 
     It is used for DF2K_OST dataset.
 
     opt (dict): Configuration dict. It contains:
         n_thread (int): Thread number.
@@ -30,16 +44,16 @@
     """
 
     opt = {}
     opt['n_thread'] = args.n_thread
     opt['compression_level'] = args.compression_level
 
     # HR images
-    opt['input_folder'] = osp.join(args.data_root, 'df2k_ost/GT')
-    opt['save_folder'] = osp.join(args.data_root, 'df2k_ost/GT_sub')
+    opt['input_folder'] = osp.join(args.data_root, 'GT')
+    opt['save_folder'] = osp.join(args.data_root, 'GT_sub')
     opt['crop_size'] = args.crop_size
     opt['step'] = args.step
     opt['thresh_size'] = args.thresh_size
     extract_subimages(opt)
 
 
 def extract_subimages(opt):
@@ -56,18 +70,18 @@
     if not osp.exists(save_folder):
         os.makedirs(save_folder)
         print(f'mkdir {save_folder} ...')
     else:
         print(f'Folder {save_folder} already exists. Exit.')
         sys.exit(1)
 
-    img_list = list(mmcv.scandir(input_folder, suffix='png'))
+    img_list = list(mmengine.scandir(input_folder, suffix='png'))
     img_list = [osp.join(input_folder, v) for v in img_list]
 
-    prog_bar = mmcv.ProgressBar(len(img_list))
+    prog_bar = mmengine.ProgressBar(len(img_list))
     pool = Pool(opt['n_thread'])
     for path in img_list:
         pool.apply_async(
             worker, args=(path, opt), callback=lambda arg: prog_bar.update())
     pool.close()
     pool.join()
     print('All processes done.')
@@ -302,14 +316,20 @@
 
 def parse_args():
     parser = argparse.ArgumentParser(
         description='Prepare DF2K_OST dataset',
         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
     parser.add_argument('--data-root', help='dataset root')
     parser.add_argument(
+        '--anno-path',
+        nargs='?',
+        default='meta_info_df2k_ost.txt',
+        type=str,
+        help='annotation file path')
+    parser.add_argument(
         '--crop-size',
         type=int,
         nargs='?',
         default=480,
         help='cropped size for HR images')
     parser.add_argument(
         '--step',
@@ -345,10 +365,13 @@
 
 if __name__ == '__main__':
     args = parse_args()
 
     # extract subimages
     main_extract_subimages(args)
 
+    # generate annotation files
+    generate_anno_file(args)
+
     # prepare lmdb files if necessary
     if args.make_lmdb:
         make_lmdb_for_df2k_ost(args.data_root)
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/div2k/preprocess_div2k_dataset.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/div2k/preprocess_div2k_dataset.py`

 * *Files 12% similar despite different names*

```diff
@@ -9,14 +9,33 @@
 import cv2
 import lmdb
 import mmcv
 import mmengine
 import numpy as np
 
 
+def generate_anno_file(args):
+    """Generate annotation file for DIV2K datasets from the ground-truth
+    folder."""
+
+    print('Generate annotation files ...')
+    train_file = osp.join(args.data_root, args.anno_train_path)
+    test_file = osp.join(args.data_root, args.anno_test_path)
+    mmengine.utils.mkdir_or_exist(osp.dirname(train_file))
+    mmengine.utils.mkdir_or_exist(osp.dirname(test_file))
+    img_list = sorted(
+        os.listdir(osp.join(args.data_root, 'DIV2K_train_HR_sub')))
+    with open(train_file, 'w') as f1, open(test_file, 'w') as f2:
+        for img in img_list:
+            if img[:4] < '0801':
+                f1.write(f'{img} ({args.crop_size}, {args.crop_size}, 3)\n')
+            else:
+                f2.write(f'{img} ({args.crop_size}, {args.crop_size}, 3)\n')
+
+
 def main_extract_subimages(args):
     """A multi-thread tool to crop large images to sub-images for faster IO.
 
     It is used for DIV2K dataset.
 
     opt (dict): Configuration dict. It contains:
         n_thread (int): Thread number.
@@ -348,14 +367,26 @@
 
 def parse_args():
     parser = argparse.ArgumentParser(
         description='Prepare DIV2K dataset',
         formatter_class=argparse.ArgumentDefaultsHelpFormatter)
     parser.add_argument('--data-root', help='dataset root')
     parser.add_argument(
+        '--anno-train-path',
+        nargs='?',
+        default='meta_info_DIV2K800sub_GT.txt',
+        type=str,
+        help='annotation file path of train dataset')
+    parser.add_argument(
+        '--anno-test-path',
+        nargs='?',
+        default='meta_info_DIV2K100sub_GT.txt',
+        type=str,
+        help='annotation file path of test dataset')
+    parser.add_argument(
         '--scales',
         nargs='*',
         default=[2, 3, 4],
         type=int,
         help='scale factor list')
     parser.add_argument(
         '--crop-size',
@@ -393,12 +424,17 @@
         help='whether to prepare lmdb files')
     args = parser.parse_args()
     return args
 
 
 if __name__ == '__main__':
     args = parse_args()
+
     # extract subimages
     main_extract_subimages(args)
+
+    # generate annotation files
+    generate_anno_file(args)
+
     # prepare lmdb files if necessary
     if args.make_lmdb:
         make_lmdb_for_div2k(args.data_root)
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/reds/crop_sub_images.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/reds/crop_sub_images.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,14 +4,15 @@
 import os.path as osp
 import re
 import sys
 from multiprocessing import Pool
 
 import cv2
 import mmcv
+import mmengine
 import numpy as np
 
 
 def worker(path, opt):
     """Worker for each process.
 
     Args:
@@ -50,15 +51,15 @@
     index = 0
     for x in h_space:
         for y in w_space:
             index += 1
             cropped_img = img[x:x + crop_size, y:y + crop_size, ...]
             sub_folder = osp.join(opt['save_folder'],
                                   f'{sequence}_s{index:03d}')
-            mmcv.mkdir_or_exist(sub_folder)
+            mmengine.mkdir_or_exist(sub_folder)
             cv2.imwrite(
                 osp.join(sub_folder, f'{img_name}{extension}'), cropped_img,
                 [cv2.IMWRITE_PNG_COMPRESSION, opt['compression_level']])
     process_info = f'Processing {img_name} ...'
     return process_info
 
 
@@ -76,18 +77,18 @@
     if not osp.exists(save_folder):
         os.makedirs(save_folder)
         print(f'mkdir {save_folder} ...')
     else:
         print(f'Folder {save_folder} already exists. Exit.')
         sys.exit(1)
 
-    img_list = list(mmcv.scandir(input_folder, recursive=True))
+    img_list = list(mmengine.scandir(input_folder, recursive=True))
 
     img_list = [osp.join(input_folder, v) for v in img_list]
-    prog_bar = mmcv.ProgressBar(len(img_list))
+    prog_bar = mmengine.ProgressBar(len(img_list))
     pool = Pool(opt['n_thread'])
     for path in img_list:
         pool.apply_async(
             worker, args=(path, opt), callback=lambda arg: prog_bar.update())
     pool.close()
     pool.join()
     print('All processes done.')
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/dataset_converters/reds/preprocess_reds_dataset.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/dataset_converters/reds/preprocess_reds_dataset.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 import re
 import shutil
 import sys
 
 import cv2
 import lmdb
 import mmcv
+import mmengine
 
 
 def make_lmdb(mode, data_path, lmdb_path, batch=5000, compress_level=1):
     """Create lmdb for the REDS dataset.
 
     Contents of lmdb. The file structure is:
     example.lmdb
@@ -65,15 +66,15 @@
 
     if osp.exists(lmdb_path):
         print(f'Folder {lmdb_path} already exists. Exit.')
         sys.exit(1)
 
     print('Reading image path list ...')
     img_path_list = sorted(
-        list(mmcv.scandir(data_path, suffix='png', recursive=True)))
+        list(mmengine.scandir(data_path, suffix='png', recursive=True)))
     keys = []
     for img_path in img_path_list:
         parts = re.split(r'[\\/]', img_path)
         folder = parts[-2]
         img_name = parts[-1].split('.png')[0]
         keys.append(folder + '_' + img_name)  # example: 000_00000000
 
@@ -84,15 +85,15 @@
                                [cv2.IMWRITE_PNG_COMPRESSION, compress_level])
     data_size_per_img = img_byte.nbytes
     print('Data size per image is: ', data_size_per_img)
     data_size = data_size_per_img * len(img_path_list)
     env = lmdb.open(lmdb_path, map_size=data_size * 10)
 
     # write data to lmdb
-    pbar = mmcv.ProgressBar(len(img_path_list))
+    pbar = mmengine.ProgressBar(len(img_path_list))
     txn = env.begin(write=True)
     txt_file = open(osp.join(lmdb_path, 'meta_info.txt'), 'w')
     for idx, (path, key) in enumerate(zip(img_path_list, keys)):
         pbar.update()
         key_byte = key.encode('ascii')
         img = mmcv.imread(osp.join(data_path, path), flag='unchanged')
         h, w, c = img.shape
@@ -141,15 +142,15 @@
 
     Args:
         root_path (str): Root path for REDS datasets.
     """
 
     print(f'Generate annotation files {file_name}...')
     txt_file = osp.join(root_path, file_name)
-    mmcv.utils.mkdir_or_exist(osp.dirname(txt_file))
+    mmengine.utils.mkdir_or_exist(osp.dirname(txt_file))
     with open(txt_file, 'w') as f:
         for i in range(270):
             for j in range(100):
                 f.write(f'{i:03d}/{j:08d}.png (720, 1280, 3)\n')
 
 
 def split_anno_file(root_path, val_partition='REDS4'):
@@ -176,34 +177,34 @@
     for i in range(270):
         for j in range(100):
             if f'{i:03d}' in val_partition:
                 val_list.append(f'{i:03d}/{j:08d}.png (720, 1280, 3)')
             else:
                 train_list.append(f'{i:03d}/{j:08d}.png (720, 1280, 3)')
 
-    mmcv.utils.mkdir_or_exist(osp.dirname(train_txt_file))
+    mmengine.utils.mkdir_or_exist(osp.dirname(train_txt_file))
     with open(train_txt_file, 'w') as f:
         f.write('\n'.join(train_list))
 
-    mmcv.utils.mkdir_or_exist(osp.dirname(val_txt_file))
+    mmengine.utils.mkdir_or_exist(osp.dirname(val_txt_file))
     with open(val_txt_file, 'w') as f:
         f.write('\n'.join(val_list))
 
 
 def unzip(zip_path):
     """Unzip zip files. It will scan all zip files in zip_path and return unzip
     folder names.
 
     Args:
         zip_path (str): Path for zip files.
 
     Returns:
         list: unzip folder names.
     """
-    zip_files = mmcv.scandir(zip_path, suffix='zip', recursive=False)
+    zip_files = mmengine.scandir(zip_path, suffix='zip', recursive=False)
     import shutil
     import zipfile
     unzip_folders = []
     for zip_file in zip_files:
         zip_file = osp.join(zip_path, zip_file)
         unzip_folder = zip_file.replace('.zip', '').split('_part')[0]
         print(f'Unzip {zip_file} to {unzip_folder}')
```

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/gui/component.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/gui/component.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/gui/gui.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/gui/gui.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/gui/page_general.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/gui/page_general.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/gui/page_sr.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/gui/page_sr.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/gui/utils.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/gui/utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/model_converters/publish_model.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/model_converters/publish_model.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/model_converters/pytorch2onnx.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/model_converters/pytorch2onnx.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/slurm_test.sh` & `mmedit-1.0.0rc7/mmedit/.mim/tools/slurm_test.sh`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/slurm_train.sh` & `mmedit-1.0.0rc7/mmedit/.mim/tools/slurm_train.sh`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/test.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/test.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/.mim/tools/train.py` & `mmedit-1.0.0rc7/mmedit/.mim/tools/train.py`

 * *Files 4% similar despite different names*

```diff
@@ -36,15 +36,18 @@
         'Note that the quotation marks are necessary and that no white space '
         'is allowed.')
     parser.add_argument(
         '--launcher',
         choices=['none', 'pytorch', 'slurm', 'mpi'],
         default='none',
         help='job launcher')
-    parser.add_argument('--local_rank', type=int, default=0)
+    # When using PyTorch version >= 2.0.0, the `torch.distributed.launch`
+    # will pass the `--local-rank` parameter to `tools/train.py` instead
+    # of `--local_rank`.
+    parser.add_argument('--local_rank', '--local-rank', type=int, default=0)
     args = parser.parse_args()
     if 'LOCAL_RANK' not in os.environ:
         os.environ['LOCAL_RANK'] = str(args.local_rank)
 
     return args
 
 
@@ -65,15 +68,15 @@
         # use config filename as default work_dir if cfg.work_dir is None
         cfg.work_dir = osp.join('./work_dirs',
                                 osp.splitext(osp.basename(args.config))[0])
 
     # enable automatic-mixed-precision training
     if args.amp is True:
         if ('constructor' not in cfg.optim_wrapper) or \
-                cfg.optim_wrapper['constructor'] == 'DefaultOptimWrapperConstructor': # noqa
+                cfg.optim_wrapper['constructor'] == 'DefaultOptimWrapperConstructor':  # noqa
             optim_wrapper = cfg.optim_wrapper.type
             if optim_wrapper == 'AmpOptimWrapper':
                 print_colored_log(
                     'AMP training is already enabled in your config.',
                     logger='current',
                     level=logging.WARNING)
             else:
```

### Comparing `mmedit-1.0.0rc6/mmedit/__init__.py` & `mmedit-1.0.0rc7/mmedit/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/__init__.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/base_mmedit_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/base_mmedit_inferencer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/colorization_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/colorization_inferencer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/conditional_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/conditional_inferencer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/eg3d_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/eg3d_inferencer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/inference_functions.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/inference_functions.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/inpainting_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/inpainting_inferencer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/matting_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/matting_inferencer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/mmedit_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/mmedit_inferencer.py`

 * *Files 17% similar despite different names*

```diff
@@ -3,17 +3,17 @@
 
 import torch
 
 from mmedit.utils import ConfigType
 from .colorization_inferencer import ColorizationInferencer
 from .conditional_inferencer import ConditionalInferencer
 from .eg3d_inferencer import EG3DInferencer
+from .image_super_resolution_inferencer import ImageSuperResolutionInferencer
 from .inpainting_inferencer import InpaintingInferencer
 from .matting_inferencer import MattingInferencer
-from .restoration_inferencer import RestorationInferencer
 from .text2image_inferencer import Text2ImageInferencer
 from .translation_inferencer import TranslationInferencer
 from .unconditional_inferencer import UnconditionalInferencer
 from .video_interpolation_inferencer import VideoInterpolationInferencer
 from .video_restoration_inferencer import VideoRestorationInferencer
 
 
@@ -51,24 +51,26 @@
                 config, ckpt, device, extra_parameters, seed=seed)
         elif self.task in ['inpainting', 'Inpainting']:
             self.inferencer = InpaintingInferencer(
                 config, ckpt, device, extra_parameters, seed=seed)
         elif self.task in ['translation', 'Image2Image']:
             self.inferencer = TranslationInferencer(
                 config, ckpt, device, extra_parameters, seed=seed)
-        elif self.task in ['restoration', 'Image Super-Resolution']:
-            self.inferencer = RestorationInferencer(
+        elif self.task in ['Image super-resolution', 'Image Super-Resolution']:
+            self.inferencer = ImageSuperResolutionInferencer(
                 config, ckpt, device, extra_parameters, seed=seed)
         elif self.task in ['video_restoration', 'Video Super-Resolution']:
             self.inferencer = VideoRestorationInferencer(
                 config, ckpt, device, extra_parameters, seed=seed)
         elif self.task in ['video_interpolation', 'Video Interpolation']:
             self.inferencer = VideoInterpolationInferencer(
                 config, ckpt, device, extra_parameters)
-        elif self.task in ['text2image', 'Text2Image']:
+        elif self.task in [
+                'text2image', 'Text2Image', 'Text2Image, Image2Image'
+        ]:
             self.inferencer = Text2ImageInferencer(
                 config, ckpt, device, extra_parameters, seed=seed)
         elif self.task in ['3D_aware_generation', '3D-aware Generation']:
             self.inferencer = EG3DInferencer(
                 config, ckpt, device, extra_parameters, seed=seed)
         else:
             raise ValueError(f'Unknown inferencer task: {self.task}')
```

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/restoration_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/image_super_resolution_inferencer.py`

 * *Files 18% similar despite different names*

```diff
@@ -4,25 +4,24 @@
 
 import mmcv
 import numpy as np
 import torch
 from mmengine import mkdir_or_exist
 from mmengine.dataset import Compose
 from mmengine.dataset.utils import default_collate as collate
-from torch.nn.parallel import scatter
 
 from mmedit.utils import tensor2img
 from .base_mmedit_inferencer import BaseMMEditInferencer, InputsType, PredType
 
 
-class RestorationInferencer(BaseMMEditInferencer):
+class ImageSuperResolutionInferencer(BaseMMEditInferencer):
     """inferencer that predicts with restoration models."""
 
     func_kwargs = dict(
-        preprocess=['img'],
+        preprocess=['img', 'ref'],
         forward=[],
         visualize=['result_out_dir'],
         postprocess=[])
 
     def preprocess(self, img: InputsType, ref: InputsType = None) -> Dict:
         """Process the inputs into a model-feedable format.
 
@@ -34,58 +33,59 @@
         Returns:
             data(Dict): Results of preprocess.
         """
         cfg = self.model.cfg
         device = next(self.model.parameters()).device  # model device
 
         # select the data pipeline
-        if cfg.get('demo_pipeline', None):
+        if cfg.get('inference_pipeline', None):
+            test_pipeline = cfg.inference_pipeline
+        elif cfg.get('demo_pipeline', None):
             test_pipeline = cfg.demo_pipeline
         elif cfg.get('test_pipeline', None):
             test_pipeline = cfg.test_pipeline
         else:
             test_pipeline = cfg.val_pipeline
 
-        # remove gt from test_pipeline
         keys_to_remove = ['gt', 'gt_path']
         for key in keys_to_remove:
             for pipeline in list(test_pipeline):
                 if 'key' in pipeline and key == pipeline['key']:
                     test_pipeline.remove(pipeline)
                 if 'keys' in pipeline and key in pipeline['keys']:
                     pipeline['keys'].remove(key)
                     if len(pipeline['keys']) == 0:
                         test_pipeline.remove(pipeline)
                 if 'meta_keys' in pipeline and key in pipeline['meta_keys']:
                     pipeline['meta_keys'].remove(key)
+
         # build the data pipeline
         test_pipeline = Compose(test_pipeline)
+
         # prepare data
         if ref:  # Ref-SR
-            data = dict(img_path=img, ref_path=ref)
+            data = dict(img_path=img, gt_path=ref)
         else:  # SISR
             data = dict(img_path=img)
         _data = test_pipeline(data)
+
         data = dict()
         data_preprocessor = cfg['model']['data_preprocessor']
         mean = torch.Tensor(data_preprocessor['mean']).view([3, 1, 1])
         std = torch.Tensor(data_preprocessor['std']).view([3, 1, 1])
         data['inputs'] = (_data['inputs'] - mean) / std
         data = collate([data])
+
         if ref:
             data['data_samples'] = [_data['data_samples']]
         if 'cuda' in str(device):
-            data = scatter(data, [device])[0]
+            data['inputs'] = data['inputs'].cuda()
             if ref:
-                data['data_samples'][0].img_lq.data = data['data_samples'][
-                    0].img_lq.data.to(device)
-                data['data_samples'][0].ref_lq.data = data['data_samples'][
-                    0].ref_lq.data.to(device)
-                data['data_samples'][0].ref_img.data = data['data_samples'][
-                    0].ref_img.data.to(device)
+                data['data_samples'][0] = data['data_samples'][0].cuda()
+
         return data
 
     def forward(self, inputs: InputsType) -> PredType:
         """Forward the inputs to the model."""
         with torch.no_grad():
             result = self.model(mode='tensor', **inputs)
         return result
```

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/text2image_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/text2image_inferencer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/translation_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/translation_inferencer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/unconditional_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/unconditional_inferencer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/video_interpolation_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/video_interpolation_inferencer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/apis/inferencers/video_restoration_inferencer.py` & `mmedit-1.0.0rc7/mmedit/apis/inferencers/video_restoration_inferencer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/__init__.py` & `mmedit-1.0.0rc7/mmedit/datasets/__init__.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,19 +1,20 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from .basic_conditional_dataset import BasicConditionalDataset
 from .basic_frames_dataset import BasicFramesDataset
 from .basic_image_dataset import BasicImageDataset
 from .cifar10_dataset import CIFAR10
 from .comp1k_dataset import AdobeComp1kDataset
+from .controlnet_dataset import ControlNetDataset
 from .grow_scale_image_dataset import GrowScaleImgDataset
 from .imagenet_dataset import ImageNet
 from .mscoco_dataset import MSCoCoDataset
 from .paired_image_dataset import PairedImageDataset
 from .singan_dataset import SinGANDataset
 from .unpaired_image_dataset import UnpairedImageDataset
 
 __all__ = [
     'AdobeComp1kDataset', 'BasicImageDataset', 'BasicFramesDataset',
     'BasicConditionalDataset', 'UnpairedImageDataset', 'PairedImageDataset',
     'ImageNet', 'CIFAR10', 'GrowScaleImgDataset', 'SinGANDataset',
-    'MSCoCoDataset'
+    'MSCoCoDataset', 'ControlNetDataset'
 ]
```

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/basic_conditional_dataset.py` & `mmedit-1.0.0rc7/mmedit/datasets/basic_conditional_dataset.py`

 * *Files 1% similar despite different names*

```diff
@@ -11,17 +11,17 @@
 from .data_utils import expanduser, find_folders, get_samples
 
 
 @DATASETS.register_module()
 class BasicConditionalDataset(BaseDataset):
     """Custom dataset for conditional GAN. This class is based on the
     combination of `BaseDataset` (https://github.com/open-
-    mmlab/mmclassification/blob/1.x/mmcls/datasets/base_dataset.py)  # noqa and
-    `CustomDataset` (https://github.com/open-
-    mmlab/mmclassification/blob/1.x/mmcls/datasets/custom.py).  # noqa.
+    mmlab/mmclassification/blob/main/mmcls/datasets/base_dataset.py)  # noqa
+    and `CustomDataset` (https://github.com/open-
+    mmlab/mmclassification/blob/main/mmcls/datasets/custom.py).  # noqa.
 
     The dataset supports two kinds of annotation format.
 
     1. A annotation file read by line (e.g., txt) is provided, and each line indicates a sample:
 
        The sample files: ::
```

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/basic_frames_dataset.py` & `mmedit-1.0.0rc7/mmedit/datasets/basic_frames_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/basic_image_dataset.py` & `mmedit-1.0.0rc7/mmedit/datasets/basic_image_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/categories.py` & `mmedit-1.0.0rc7/mmedit/datasets/categories.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/cifar10_dataset.py` & `mmedit-1.0.0rc7/mmedit/datasets/cifar10_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/comp1k_dataset.py` & `mmedit-1.0.0rc7/mmedit/datasets/comp1k_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/data_utils.py` & `mmedit-1.0.0rc7/mmedit/datasets/data_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/grow_scale_image_dataset.py` & `mmedit-1.0.0rc7/mmedit/datasets/grow_scale_image_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/imagenet_dataset.py` & `mmedit-1.0.0rc7/mmedit/datasets/imagenet_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/mscoco_dataset.py` & `mmedit-1.0.0rc7/mmedit/datasets/mscoco_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/paired_image_dataset.py` & `mmedit-1.0.0rc7/mmedit/datasets/paired_image_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/singan_dataset.py` & `mmedit-1.0.0rc7/mmedit/datasets/singan_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/__init__.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/alpha.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/alpha.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/aug_frames.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/aug_frames.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/aug_pixel.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/aug_pixel.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/aug_shape.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/aug_shape.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/blur_kernels.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/blur_kernels.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/crop.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/crop.py`

 * *Files 0% similar despite different names*

```diff
@@ -960,15 +960,15 @@
                  config_file,
                  key='img',
                  box_num_upbound=-1,
                  finesize=256):
 
         assert mmdet_apis is not None, (
             "Cannot import 'mmdet'. Please install 'mmdet' via "
-            "\"mim install 'mmdet >= 3.0.0rc2'\".")
+            "\"mim install 'mmdet >= 3.0.0'\".")
 
         cfg = get_config(config_file, pretrained=True)
         with DefaultScope.overwrite_default_scope('mmdet'):
             self.predictor = mmdet_apis.init_detector(cfg, cfg.model_path)
 
         self.key = key
         self.box_num_upbound = box_num_upbound
```

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/fgbg.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/fgbg.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/formatting.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/formatting.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/generate_assistant.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/generate_assistant.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/generate_frame_indices.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/generate_frame_indices.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/get_masked_image.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/get_masked_image.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/loading.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/loading.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/matlab_like_resize.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/matlab_like_resize.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/normalization.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/normalization.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/random_degradations.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/random_degradations.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/random_down_sampling.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/random_down_sampling.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/trimap.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/trimap.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/transforms/values.py` & `mmedit-1.0.0rc7/mmedit/datasets/transforms/values.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/datasets/unpaired_image_dataset.py` & `mmedit-1.0.0rc7/mmedit/datasets/unpaired_image_dataset.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/edit.py` & `mmedit-1.0.0rc7/mmedit/edit.py`

 * *Files 3% similar despite different names*

```diff
@@ -35,15 +35,17 @@
         >>> # inference of a translation model, pix2pix for example
         >>> editor = MMEdit(model_name='pix2pix')
         >>> editor.infer(img='./test.jpg', result_out_dir='./pix2pix_res.jpg')
 
         >>> # see demo/mmediting_inference_tutorial.ipynb for more examples
     """
     # unsupported now
-    # singan
+    # singan, liif
+    # output should be checked
+    # dic, glean
 
     inference_supported_models = [
         # colorization models
         'inst_colorization',
 
         # conditional models
         'biggan',
@@ -67,23 +69,36 @@
         'global_local',
         'aot_gan',
 
         # translation models
         'pix2pix',
         'cyclegan',
 
-        # restoration models
+        # image super-resolution models
+        'srcnn',
+        'srgan_resnet',
+        'edsr',
         'esrgan',
+        'rdn',
+        'dic',
+        'ttsr',
+        'glean',
+        'real_esrgan',
 
         # video_interpolation models
         'flavr',
         'cain',
 
         # video_restoration models
         'edvr',
+        'tdan',
+        'basicvsr',
+        'iconvsr',
+        'basicvsr_pp',
+        'real_basicvsr',
 
         # text2image models
         'disco_diffusion',
 
         # 3D-aware generation
         'eg3d',
     ]
```

### Comparing `mmedit-1.0.0rc6/mmedit/engine/hooks/__init__.py` & `mmedit-1.0.0rc7/mmedit/engine/hooks/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/hooks/ema.py` & `mmedit-1.0.0rc7/mmedit/engine/hooks/ema.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/hooks/iter_time_hook.py` & `mmedit-1.0.0rc7/mmedit/engine/hooks/iter_time_hook.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/hooks/pggan_fetch_data_hook.py` & `mmedit-1.0.0rc7/mmedit/engine/hooks/pggan_fetch_data_hook.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/hooks/pickle_data_hook.py` & `mmedit-1.0.0rc7/mmedit/engine/hooks/pickle_data_hook.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/hooks/reduce_lr_scheduler_hook.py` & `mmedit-1.0.0rc7/mmedit/engine/hooks/reduce_lr_scheduler_hook.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/hooks/visualization_hook.py` & `mmedit-1.0.0rc7/mmedit/engine/hooks/visualization_hook.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/optimizers/multi_optimizer_constructor.py` & `mmedit-1.0.0rc7/mmedit/engine/optimizers/multi_optimizer_constructor.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/optimizers/pggan_optimizer_constructor.py` & `mmedit-1.0.0rc7/mmedit/engine/optimizers/pggan_optimizer_constructor.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/optimizers/singan_optimizer_constructor.py` & `mmedit-1.0.0rc7/mmedit/engine/optimizers/singan_optimizer_constructor.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/runner/edit_loops.py` & `mmedit-1.0.0rc7/mmedit/engine/runner/edit_loops.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/runner/loop_utils.py` & `mmedit-1.0.0rc7/mmedit/engine/runner/loop_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/schedulers/linear_lr_scheduler_with_interval.py` & `mmedit-1.0.0rc7/mmedit/engine/schedulers/linear_lr_scheduler_with_interval.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/engine/schedulers/reduce_lr_scheduler.py` & `mmedit-1.0.0rc7/mmedit/engine/schedulers/reduce_lr_scheduler.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/__init__.py` & `mmedit-1.0.0rc7/mmedit/evaluation/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/evaluator.py` & `mmedit-1.0.0rc7/mmedit/evaluation/evaluator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/functional/fid_inception.py` & `mmedit-1.0.0rc7/mmedit/evaluation/functional/fid_inception.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/functional/gaussian_funcs.py` & `mmedit-1.0.0rc7/mmedit/evaluation/functional/gaussian_funcs.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/functional/inception_utils.py` & `mmedit-1.0.0rc7/mmedit/evaluation/functional/inception_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/__init__.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/base_gen_metric.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/base_gen_metric.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/base_sample_wise_metric.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/base_sample_wise_metric.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/connectivity_error.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/connectivity_error.py`

 * *Files 7% similar despite different names*

```diff
@@ -2,24 +2,24 @@
 """Evaluation metrics used in Image Matting."""
 
 from typing import List, Sequence
 
 import cv2
 import numpy as np
 import torch.nn as nn
-from mmengine.evaluator import BaseMetric
 from mmengine.model import is_model_wrapper
 from torch.utils.data.dataloader import DataLoader
 
 from mmedit.registry import METRICS
+from .base_sample_wise_metric import BaseSampleWiseMetric
 from .metrics_utils import _fetch_data_and_check, average
 
 
 @METRICS.register_module()
-class ConnectivityError(BaseMetric):
+class ConnectivityError(BaseSampleWiseMetric):
     """Connectivity error for evaluating alpha matte prediction.
 
     .. note::
 
         Current implementation assume image / alpha / trimap array in numpy
         format and with pixel value ranging from 0 to 255.
 
@@ -36,14 +36,16 @@
 
     Default prefix: ''
 
     Metrics:
         - ConnectivityError (float): Connectivity Error
     """
 
+    metric = 'ConnectivityError'
+
     def __init__(
         self,
         step=0.1,
         norm_constant=1000,
         **kwargs,
     ) -> None:
         self.step = step
```

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/equivariance.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/equivariance.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/fid.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/fid.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/gradient_error.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/gradient_error.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,24 +1,24 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from typing import List, Sequence
 
 import cv2
 import numpy as np
 import torch.nn as nn
-from mmengine.evaluator import BaseMetric
 from mmengine.model import is_model_wrapper
 from torch.utils.data.dataloader import DataLoader
 
 from mmedit.registry import METRICS
 from ..functional import gauss_gradient
+from .base_sample_wise_metric import BaseSampleWiseMetric
 from .metrics_utils import _fetch_data_and_check, average
 
 
 @METRICS.register_module()
-class GradientError(BaseMetric):
+class GradientError(BaseSampleWiseMetric):
     """Gradient error for evaluating alpha matte prediction.
 
     .. note::
 
         Current implementation assume image / alpha / trimap array in numpy
         format and with pixel value ranging from 0 to 255.
 
@@ -35,14 +35,16 @@
 
     Default prefix: ''
 
     Metrics:
         - GradientError (float): Gradient Error
     """
 
+    metric = 'GradientError'
+
     def __init__(
         self,
         sigma=1.4,
         norm_constant=1000,
         **kwargs,
     ) -> None:
         self.sigma = sigma
```

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/inception_score.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/inception_score.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/mae.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/mae.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/matting_mse.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/matting_mse.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from typing import List, Sequence
 
 import torch.nn as nn
-from mmengine.evaluator import BaseMetric
 from mmengine.model import is_model_wrapper
 from torch.utils.data.dataloader import DataLoader
 
 from mmedit.registry import METRICS
+from .base_sample_wise_metric import BaseSampleWiseMetric
 from .metrics_utils import _fetch_data_and_check, average
 
 
 @METRICS.register_module()
-class MattingMSE(BaseMetric):
+class MattingMSE(BaseSampleWiseMetric):
     """Mean Squared Error metric for image matting.
 
     This metric compute per-pixel squared error average across all
     pixels.
     i.e. mean((a-b)^2) / norm_const
 
     .. note::
@@ -35,14 +35,15 @@
             Default to 1000.
 
     Metrics:
         - MattingMSE (float): Mean of Squared Error
     """
 
     default_prefix = ''
+    metric = 'MattingMSE'
 
     def __init__(
         self,
         norm_const=1000,
         **kwargs,
     ) -> None:
         self.norm_const = norm_const
```

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/metrics_utils.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/metrics_utils.py`

 * *Files 0% similar despite different names*

```diff
@@ -29,15 +29,15 @@
     Returns:
         pred_alpha (Tensor): Pred_alpha data of predictions.
         ori_alpha (Tensor): Ori_alpha data of data_batch.
         ori_trimap (Tensor): Ori_trimap data of data_batch.
     """
     ori_trimap = data_samples['ori_trimap'][0, :, :].cpu().numpy()
     ori_alpha = data_samples['ori_alpha'][0, :, :].cpu().numpy()
-    pred_alpha = data_samples['output']['pred_alpha']['data']  # 2D tensor
+    pred_alpha = data_samples['output']['pred_alpha']  # 2D tensor
     pred_alpha = pred_alpha.cpu().numpy()
 
     _assert_ndim(ori_trimap, 'trimap', 2, 'HxW')
     _assert_ndim(ori_alpha, 'gt_alpha', 2, 'HxW')
     _assert_ndim(pred_alpha, 'pred_alpha', 2, 'HxW')
     _assert_masked(pred_alpha, ori_trimap)
```

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/ms_ssim.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/ms_ssim.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/mse.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/mse.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/niqe.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/niqe.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/niqe_pris_params.npz` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/niqe_pris_params.npz`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/ppl.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/ppl.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/precision_and_recall.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/precision_and_recall.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/psnr.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/psnr.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/sad.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/sad.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from typing import List, Sequence
 
 import numpy as np
 import torch.nn as nn
-from mmengine.evaluator import BaseMetric
 from mmengine.model import is_model_wrapper
 from torch.utils.data.dataloader import DataLoader
 
 from mmedit.registry import METRICS
+from .base_sample_wise_metric import BaseSampleWiseMetric
 from .metrics_utils import _fetch_data_and_check, average
 
 
 @METRICS.register_module()
-class SAD(BaseMetric):
+class SAD(BaseSampleWiseMetric):
     """Sum of Absolute Differences metric for image matting.
 
     This metric compute per-pixel absolute difference and sum across all
     pixels.
     i.e. sum(abs(a-b)) / norm_const
 
     .. note::
@@ -36,14 +36,15 @@
             Default to 1000.
 
     Metrics:
         - SAD (float): Sum of Absolute Differences
     """
 
     default_prefix = ''
+    metric = 'SAD'
 
     def __init__(
         self,
         norm_const=1000,
         **kwargs,
     ) -> None:
         self.norm_const = norm_const
```

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/snr.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/snr.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/ssim.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/ssim.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/evaluation/metrics/swd.py` & `mmedit-1.0.0rc7/mmedit/evaluation/metrics/swd.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/all_gather_layer.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/all_gather_layer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/aspp.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/aspp.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/downsample.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/downsample.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/ensemble.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/ensemble.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/gated_conv_module.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/gated_conv_module.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/img_normalize.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/img_normalize.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/linear_module.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/linear_module.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/multi_layer_disc.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/multi_layer_disc.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/patch_disc.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/patch_disc.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/resnet.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/resnet.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/separable_conv_module.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/separable_conv_module.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/simple_encoder_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/simple_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/smpatch_disc.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/smpatch_disc.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/sr_backbone.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/sr_backbone.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/upsample.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/upsample.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_archs/vgg.py` & `mmedit-1.0.0rc7/mmedit/models/base_archs/vgg.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_models/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/base_models/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_models/average_model.py` & `mmedit-1.0.0rc7/mmedit/models/base_models/average_model.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_models/base_conditional_gan.py` & `mmedit-1.0.0rc7/mmedit/models/base_models/base_conditional_gan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_models/base_edit_model.py` & `mmedit-1.0.0rc7/mmedit/models/base_models/base_edit_model.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_models/base_gan.py` & `mmedit-1.0.0rc7/mmedit/models/base_models/base_gan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_models/base_mattor.py` & `mmedit-1.0.0rc7/mmedit/models/base_models/base_mattor.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_models/base_translation_model.py` & `mmedit-1.0.0rc7/mmedit/models/base_models/base_translation_model.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_models/basic_interpolator.py` & `mmedit-1.0.0rc7/mmedit/models/base_models/basic_interpolator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_models/one_stage.py` & `mmedit-1.0.0rc7/mmedit/models/base_models/one_stage.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/base_models/two_stage.py` & `mmedit-1.0.0rc7/mmedit/models/base_models/two_stage.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/data_preprocessors/edit_data_preprocessor.py` & `mmedit-1.0.0rc7/mmedit/models/data_preprocessors/edit_data_preprocessor.py`

 * *Files 1% similar despite different names*

```diff
@@ -754,16 +754,14 @@
         # NOTE: If same padding, batch_tensor will un-padded with the padding
         # info # of the first sample and return a Unpadded tensor. Otherwise,
         # input tensor # will un-padded with the corresponding padding info
         # saved in data samples and return a list of tensor.
         if data_samples is None:
             return batch_tensor
 
-        # import ipdb
-        # ipdb.set_trace()
         if isinstance(data_samples, list):
             is_batch_data = True
             if 'padding_size' in data_samples[0].metainfo_keys():
                 pad_infos = [
                     sample.metainfo['padding_size'] for sample in data_samples
                 ]
             else:
@@ -790,16 +788,14 @@
                 print_log(
                     'Cannot find padding information (\'padding_size\') in '
                     'meta info of \'data_samples\'. Please check whether '
                     'you have called \'self.forward\' properly.', 'current',
                     WARNING)
             return batch_tensor if is_batch_data else batch_tensor[0]
 
-        # import ipdb
-        # ipdb.set_trace()
         if same_padding:
             # un-pad with the padding info of the first sample
             padded_h, padded_w = pad_infos[0][-2:]
             padded_h, padded_w = int(padded_h), int(padded_w)
             h, w = batch_tensor.shape[-2:]
             batch_tensor = batch_tensor[..., :h - padded_h, :w - padded_w]
             return batch_tensor if is_batch_data else batch_tensor[0]
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/data_preprocessors/mattor_preprocessor.py` & `mmedit-1.0.0rc7/mmedit/models/data_preprocessors/mattor_preprocessor.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/editors/__init__.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from .aotgan import AOTBlockNeck, AOTEncoderDecoder, AOTInpaintor
 from .arcface import IDLossModel
 from .basicvsr import BasicVSR, BasicVSRNet
 from .basicvsr_plusplus_net import BasicVSRPlusPlusNet
 from .biggan import BigGAN
 from .cain import CAIN, CAINNet
+from .controlnet import ControlStableDiffusion
 from .cyclegan import CycleGAN
 from .dcgan import DCGAN
-from .ddim import DDIMScheduler
-from .ddpm import DDPMScheduler, DenoisingUnet
+from .ddpm import DenoisingUnet
 from .deepfillv1 import (ContextualAttentionModule, ContextualAttentionNeck,
                          DeepFillDecoder, DeepFillEncoder, DeepFillRefiner,
                          DeepFillv1Discriminators, DeepFillv1Inpaintor)
 from .deepfillv2 import DeepFillEncoderDecoder
 from .dic import (DIC, DICNet, FeedbackBlock, FeedbackBlockCustom,
                   FeedbackBlockHeatmapAttention, LightCNN, MaxFeature)
 from .dim import DIM
@@ -81,11 +81,11 @@
     'TTSRDiscriminator', 'TTSRNet', 'SearchTransformer', 'GLEANStyleGANv2',
     'LIIF', 'MLPRefiner', 'PlainRefiner', 'PlainDecoder', 'FBAResnetDilated',
     'FBADecoder', 'WGANGP', 'CycleGAN', 'SAGAN', 'LSGAN', 'GGAN', 'Pix2Pix',
     'StyleGAN1', 'StyleGAN2', 'StyleGAN3', 'BigGAN', 'DCGAN',
     'ProgressiveGrowingGAN', 'SinGAN', 'AblatedDiffusionModel',
     'DiscoDiffusion', 'IDLossModel', 'PESinGAN', 'MSPIEStyleGAN2',
     'StyleGAN3Generator', 'InstColorization', 'NAFBaseline',
-    'NAFBaselineLocal', 'NAFNet', 'NAFNetLocal', 'DDIMScheduler',
-    'DDPMScheduler', 'DenoisingUnet', 'ClipWrapper', 'EG3D', 'Restormer',
-    'SwinIRNet', 'StableDiffusion'
+    'NAFBaselineLocal', 'NAFNet', 'NAFNetLocal', 'DenoisingUnet',
+    'ClipWrapper', 'EG3D', 'Restormer', 'SwinIRNet', 'StableDiffusion',
+    'ControlStableDiffusion'
 ]
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/aotgan/aot_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/aotgan/aot_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/aotgan/aot_encoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/aotgan/aot_encoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/aotgan/aot_encoder_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/aotgan/aot_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/aotgan/aot_inpaintor.py` & `mmedit-1.0.0rc7/mmedit/models/editors/aotgan/aot_inpaintor.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/aotgan/aot_neck.py` & `mmedit-1.0.0rc7/mmedit/models/editors/aotgan/aot_neck.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/arcface/arcface_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/arcface/arcface_modules.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/arcface/id_loss.py` & `mmedit-1.0.0rc7/mmedit/models/editors/arcface/id_loss.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/arcface/model_irse.py` & `mmedit-1.0.0rc7/mmedit/models/editors/arcface/model_irse.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/basicvsr/basicvsr.py` & `mmedit-1.0.0rc7/mmedit/models/editors/basicvsr/basicvsr.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/basicvsr/basicvsr_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/basicvsr/basicvsr_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/basicvsr_plusplus_net/basicvsr_plusplus_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/basicvsr_plusplus_net/basicvsr_plusplus_net.py`

 * *Files 2% similar despite different names*

```diff
@@ -164,16 +164,19 @@
             dict(list[tensor]): A dictionary containing all the propagated
                 features. Each key in the dictionary corresponds to a
                 propagation branch, which is represented by a list of tensors.
         """
 
         n, t, _, h, w = flows.size()
 
-        frame_idx = range(0, t + 1)
-        flow_idx = range(-1, t)
+        # PyTorch 2.0 could not compile data type of 'range'
+        # frame_idx = range(0, t + 1)
+        # flow_idx = range(-1, t)
+        frame_idx = list(range(0, t + 1))
+        flow_idx = list(range(-1, t))
         mapping_idx = list(range(0, len(feats['spatial'])))
         mapping_idx += mapping_idx[::-1]
 
         if 'backward' in module_name:
             frame_idx = frame_idx[::-1]
             flow_idx = frame_idx
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/biggan/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/editors/biggan/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_deep_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_deep_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_deep_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_deep_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_modules.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/biggan/biggan_snmodule.py` & `mmedit-1.0.0rc7/mmedit/models/editors/biggan/biggan_snmodule.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/cain/cain.py` & `mmedit-1.0.0rc7/mmedit/models/editors/cain/cain.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/cain/cain_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/cain/cain_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/cyclegan/cyclegan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/cyclegan/cyclegan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/cyclegan/cyclegan_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/cyclegan/cyclegan_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/cyclegan/cyclegan_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/cyclegan/cyclegan_modules.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/dcgan/dcgan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/dcgan/dcgan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/dcgan/dcgan_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/dcgan/dcgan_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/dcgan/dcgan_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/dcgan/dcgan_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ddim/ddim_scheduler.py` & `mmedit-1.0.0rc7/mmedit/models/diffusion_schedulers/ddim_scheduler.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 # Copyright (c) OpenMMLab. All rights reserved.
-from typing import Union
+from typing import Optional, Union
 
 import numpy as np
 import torch
 
 from mmedit.models.utils.diffusion_utils import betas_for_alpha_bar
 from mmedit.registry import DIFFUSION_SCHEDULERS
 
 
 @DIFFUSION_SCHEDULERS.register_module()
-class DDIMScheduler:
-    """```DDIMScheduler``` support the diffusion and reverse process formulated
-    in https://arxiv.org/abs/2010.02502.
+class EditDDIMScheduler:
+    """```EditDDIMScheduler``` support the diffusion and reverse process
+    formulated in https://arxiv.org/abs/2010.02502.
 
     The code is heavily influenced by https://github.com/huggingface/diffusers/blob/main/src/diffusers/schedulers/scheduling_ddim.py. # noqa
     The difference is that we ensemble gradient-guided sampling in step function.
 
     Args:
         num_train_timesteps (int, optional): _description_. Defaults to 1000.
         beta_start (float, optional): _description_. Defaults to 0.0001.
@@ -73,27 +73,46 @@
         # there is no previous alphas_cumprod because we are already
         # at 0 `set_alpha_to_one` decides whether we set this paratemer
         # simply to one or whether we use the final alpha of the
         # "non-previous" one.
         self.final_alpha_cumprod = np.array(
             1.0) if set_alpha_to_one else self.alphas_cumprod[0]
 
+        # standard deviation of the initial noise distribution
+        self.init_noise_sigma = 1.0
+
         # setable values
         self.num_inference_steps = None
         self.timesteps = np.arange(0, num_train_timesteps)[::-1].copy()
 
     def set_timesteps(self, num_inference_steps, offset=0):
         """set time steps."""
 
         self.num_inference_steps = num_inference_steps
         self.timesteps = np.arange(
             0, self.num_train_timesteps,
             self.num_train_timesteps // self.num_inference_steps)[::-1].copy()
         self.timesteps += offset
 
+    def scale_model_input(self,
+                          sample: torch.FloatTensor,
+                          timestep: Optional[int] = None) -> torch.FloatTensor:
+        """Ensures interchangeability with schedulers that need to scale the
+        denoising model input depending on the current timestep.
+
+        Args:
+            sample (`torch.FloatTensor`): input sample
+            timestep (`int`, optional): current timestep
+
+        Returns:
+            `torch.FloatTensor`: scaled input sample
+        """
+
+        return sample
+
     def _get_variance(self, timestep, prev_timestep):
         """get variance."""
 
         alpha_prod_t = self.alphas_cumprod[timestep]
         alpha_prod_t_prev = self.alphas_cumprod[
             prev_timestep] if prev_timestep >= 0 else self.final_alpha_cumprod
         beta_prod_t = 1 - alpha_prod_t
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ddpm/attention.py` & `mmedit-1.0.0rc7/mmedit/models/editors/ddpm/attention.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ddpm/ddpm_scheduler.py` & `mmedit-1.0.0rc7/mmedit/models/diffusion_schedulers/ddpm_scheduler.py`

 * *Files 1% similar despite different names*

```diff
@@ -5,25 +5,25 @@
 import torch
 
 from mmedit.models.utils.diffusion_utils import betas_for_alpha_bar
 from mmedit.registry import DIFFUSION_SCHEDULERS
 
 
 @DIFFUSION_SCHEDULERS.register_module()
-class DDPMScheduler:
+class EditDDPMScheduler:
 
     def __init__(self,
                  num_train_timesteps: int = 1000,
                  beta_start: float = 0.0001,
                  beta_end: float = 0.02,
                  beta_schedule: str = 'linear',
                  trained_betas: Optional[Union[np.array, list]] = None,
                  variance_type='fixed_small',
                  clip_sample=True):
-        """```DDPMScheduler``` support the diffusion and reverse process
+        """```EditDDPMScheduler``` support the diffusion and reverse process
         formulated in https://arxiv.org/abs/2006.11239.
 
         The code is heavily influenced by https://github.com/huggingface/diffusers/blob/main/src/diffusers/schedulers/scheduling_ddpm.py. # noqa
 
         Args:
             num_train_timesteps (int, optional): The timesteps for training
                 process. Defaults to 1000.
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ddpm/denoising_unet.py` & `mmedit-1.0.0rc7/mmedit/models/editors/ddpm/denoising_unet.py`

 * *Files 0% similar despite different names*

```diff
@@ -1128,14 +1128,17 @@
                 kernel_size=3,
                 padding=1,
                 act_cfg=act_cfg,
                 norm_cfg=norm_cfg,
                 bias=True,
                 order=('norm', 'act', 'conv'))
 
+        if self.unet_type == 'stable':
+            self.sample_size = image_size // 8  # NOTE: hard code here
+
         self.init_weights(pretrained)
 
     def forward(self,
                 x_t,
                 t,
                 encoder_hidden_states=None,
                 label=None,
@@ -1271,15 +1274,15 @@
 
             # forward upsample blocks
             for block in self.out_blocks:
                 h = block(torch.cat([h, hs.pop()], dim=1), embedding)
             h = h.type(x_t.dtype)
             outputs = self.out(h)
 
-        return {'outputs': outputs}
+        return {'sample': outputs}
 
     def init_weights(self, pretrained=None):
         """Init weights for models.
 
         We just use the initialization method proposed in the original paper.
 
         Args:
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ddpm/embeddings.py` & `mmedit-1.0.0rc7/mmedit/models/editors/ddpm/embeddings.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ddpm/res_blocks.py` & `mmedit-1.0.0rc7/mmedit/models/editors/ddpm/res_blocks.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ddpm/unet_blocks.py` & `mmedit-1.0.0rc7/mmedit/models/editors/ddpm/unet_blocks.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/contextual_attention.py` & `mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/contextual_attention.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/contextual_attention_neck.py` & `mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/contextual_attention_neck.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/deepfill_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/deepfill_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/deepfill_disc.py` & `mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/deepfill_disc.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/deepfill_encoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/deepfill_encoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/deepfill_refiner.py` & `mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/deepfill_refiner.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/deepfillv1/deepfillv1.py` & `mmedit-1.0.0rc7/mmedit/models/editors/deepfillv1/deepfillv1.py`

 * *Files 2% similar despite different names*

```diff
@@ -279,15 +279,18 @@
         batch_inputs, data_samples = data['inputs'], data['data_samples']
         log_vars = {}
 
         masked_img = batch_inputs  # float
         gt_img = data_samples.gt_img
         mask = data_samples.mask
         mask = mask.float()
-        bbox_tensor = torch.LongTensor(data_samples.mask_bbox)
+
+        # PyTorch 2.0 could not compile 'data_samples.mask_bbox'
+        # bbox_tensor = torch.LongTensor(data_samples.mask_bbox)
+        bbox_tensor = torch.LongTensor(data_samples.metainfo['mask_bbox'])
 
         # get common output from encdec
         # input with ones
         tmp_ones = torch.ones_like(mask)
         input_x = torch.cat([masked_img, tmp_ones, mask], dim=1)
         stage1_fake_res, stage2_fake_res = self.generator(input_x)
         stage1_fake_img = masked_img * (1. - mask) + stage1_fake_res * mask
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/deepfillv2/two_stage_encoder_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/deepfillv2/two_stage_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/dic/dic.py` & `mmedit-1.0.0rc7/mmedit/models/editors/dic/dic.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,8 +1,14 @@
 # Copyright (c) OpenMMLab. All rights reserved.
+from typing import Dict, List
+
+import torch
+from mmengine.optim import OptimWrapperDict
+
+from mmedit.models.utils import set_requires_grad
 from mmedit.registry import MODELS
 from ..srgan import SRGAN
 
 
 @MODELS.register_module()
 class DIC(SRGAN):
     """DIC model for Face Super-Resolution.
@@ -119,34 +125,70 @@
             if self.gan_loss and self.discriminator:
                 fake_g_pred = self.discriminator(pred)
                 losses['loss_gan'] = self.gan_loss(
                     fake_g_pred, target_is_real=True, is_disc=False)
 
         return losses
 
-    def d_step_with_optim(self, batch_outputs, batch_gt_data, optim_wrapper):
-        """D step with optim of GAN: Calculate losses of discriminator and run
-        optim.
+    def train_step(self, data: List[dict],
+                   optim_wrapper: OptimWrapperDict) -> Dict[str, torch.Tensor]:
+        """Train step of GAN-based method.
 
         Args:
-            batch_outputs (Tuple[Tensor]): Batch output of generator.
-            batch_gt_data (Tuple[Tensor]): Batch GT data.
-            optim_wrapper (OptimWrapper): Optim wrapper of discriminator.
+            data (List[dict]): Data sampled from dataloader.
+            optim_wrapper (OptimWrapper): OptimWrapper instance
+                used to update model parameters.
 
         Returns:
-            dict: Dict of parsed losses.
+            Dict[str, torch.Tensor]: A ``dict`` of tensor for logging.
         """
 
-        sr_list, _ = batch_outputs
-        gt, _ = batch_gt_data
+        g_optim_wrapper = optim_wrapper['generator']
+
+        data = self.data_preprocessor(data, True)
+        batch_inputs = data['inputs']
+        data_samples = data['data_samples']
+        batch_gt_data = self.extract_gt_data(data_samples)
+
+        log_vars = dict()
+
+        with g_optim_wrapper.optim_context(self):
+            batch_outputs = self.forward_train(batch_inputs, data_samples)
+
+        if self.if_run_g():
+            set_requires_grad(self.discriminator, False)
+
+            log_vars_d = self.g_step_with_optim(
+                batch_outputs=batch_outputs,
+                batch_gt_data=batch_gt_data,
+                optim_wrapper=optim_wrapper)
+
+            log_vars.update(log_vars_d)
+
+        if self.if_run_d():
+            set_requires_grad(self.discriminator, True)
+
+            sr_list, _ = batch_outputs
+            gt, _ = batch_gt_data
+
+            for _ in range(self.disc_repeat):
+                # detach before function call to resolve PyTorch2.0 compile bug
+                log_vars_d = self.d_step_with_optim(
+                    batch_outputs=sr_list[-1].detach(),
+                    batch_gt_data=gt,
+                    optim_wrapper=optim_wrapper)
+
+            log_vars.update(log_vars_d)
+
+        if 'loss' in log_vars:
+            log_vars.pop('loss')
+
+        self.step_counter += 1
 
-        return super().d_step_with_optim(
-            batch_outputs=sr_list[-1],
-            batch_gt_data=gt,
-            optim_wrapper=optim_wrapper)
+        return log_vars
 
     @staticmethod
     def extract_gt_data(data_samples):
         """extract gt data from data samples.
 
         Args:
             data_samples (list): List of EditDataSample.
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/dic/dic_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/dic/dic_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/dic/feedback_hour_glass.py` & `mmedit-1.0.0rc7/mmedit/models/editors/dic/feedback_hour_glass.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/dic/light_cnn.py` & `mmedit-1.0.0rc7/mmedit/models/editors/dic/light_cnn.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/dim/dim.py` & `mmedit-1.0.0rc7/mmedit/models/editors/dim/dim.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/disco_diffusion/clip_wrapper.py` & `mmedit-1.0.0rc7/mmedit/models/editors/disco_diffusion/clip_wrapper.py`

 * *Files 21% similar despite different names*

```diff
@@ -3,24 +3,23 @@
 from mmengine import print_log
 
 from mmedit.registry import MODELS
 
 
 @MODELS.register_module()
 class ClipWrapper(nn.Module):
-    """Clip Models wrapper for disco-diffusion.
+    r"""Clip Models wrapper.
 
     We provide wrappers for the clip models of ``openai`` and
     ``mlfoundations``, where the user can specify ``clip_type``
     as ``clip`` or ``open_clip``, and then initialize a clip model
     using the same arguments as in the original codebase. The
     following clip models settings are provided in the official
     repo of disco diffusion:
-
-    |            Setting            | Source    | Arguments                                                    | # noqa
+|            Setting            | Source    | Arguments                                                    | # noqa
     |:-----------------------------:|-----------|--------------------------------------------------------------| # noqa
     | ViTB32                        | clip      | name='ViT-B/32',                  jit=False                  | # noqa
     | ViTB16                        | clip      | name='ViT-B/16',                  jit=False                  | # noqa
     | ViTL14                        | clip      | name='ViT-L/14',                  jit=False                  | # noqa
     | ViTL14_336px                  | clip      | name='ViT-L/14@336px',            jit=False                  | # noqa
     | RN50                          | clip      | name='RN50',                      jit=False                  | # noqa
     | RN50x4                        | clip      | name='RN50x4',                    jit=False                  | # noqa
@@ -38,50 +37,80 @@
     | RN50_cc12m                    | open_clip | model_name='RN50',                pretrained='cc12m'         | # noqa
     | RN50_quickgelu_yfcc15m        | open_clip | model_name='RN50-quickgelu',      pretrained='yfcc15m'       | # noqa
     | RN50_quickgelu_cc12m          | open_clip | model_name='RN50-quickgelu',      pretrained='cc12m'         | # noqa
     | RN101_yfcc15m                 | open_clip | model_name='RN101',               pretrained='yfcc15m'       | # noqa
     | RN101_quickgelu_yfcc15m       | open_clip | model_name='RN101-quickgelu',     pretrained='yfcc15m'       | # noqa
 
     An example of a ``clip_modes_cfg`` is as follows:
-    .. code-block:: python
 
-        clip_models = [
-            dict(type='ClipWrapper', clip_type='clip', name='ViT-B/32', jit=False),
-            dict(type='ClipWrapper', clip_type='clip', name='ViT-B/16', jit=False),
-            dict(type='ClipWrapper', clip_type='clip', name='RN50', jit=False)
-        ]
+    Examples:
+
+    >>> # Use OpenAI's CLIP
+    >>> config = dict(
+    >>>     type='ClipWrapper',
+    >>>     clip_type='clip',
+    >>>     name='ViT-B/32',
+    >>>     jit=False)
+
+    >>> # Use OpenCLIP
+    >>> config = dict(
+    >>>     type='ClipWrapper',
+    >>>     clip_type='open_clip',
+    >>>     model_name='RN50',
+    >>>     pretrained='yfcc15m')
+
+    >>> # Use CLIP from Hugging Face Transformers
+    >>> config = dict(
+    >>>     type='ClipWrapper',
+    >>>     clip_type='huggingface',
+    >>>     pretrained_model_name_or_path='runwayml/stable-diffusion-v1-5',
+    >>>     subfolder='text_encoder')
 
     Args:
         clip_type (List[Dict]): The original source of the clip model. Whether be
-            ``clip`` or ``open_clip``.
+            ``clip``, ``open_clip`` or ``hugging_face``.
+
+        *args, **kwargs: Arguments to initialize corresponding clip model.
     """
 
     def __init__(self, clip_type, *args, **kwargs):
 
         super().__init__()
         self.clip_type = clip_type
-        assert clip_type in ['clip', 'open_clip']
+        assert clip_type in ['clip', 'open_clip', 'huggingface']
+
+        error_msg = ('{} need to be installed! Run `pip install -r '
+                     'requirements/optional.txt` and try again')
         if clip_type == 'clip':
             try:
                 import clip
             except ImportError:
-                raise ImportError(
-                    'clip need to be installed! Run `pip install -r requirements/optional.txt` and try again'  # noqa
-                )  # noqa
+                raise ImportError(error_msg.format('\'clip\''))
             print_log(f'Creating {kwargs["name"]} by OpenAI', 'current')
             self.model, _ = clip.load(*args, **kwargs)
         elif clip_type == 'open_clip':
             try:
                 import open_clip
             except ImportError:
-                raise ImportError(
-                    'open_clip_torch need to be installed! Run `pip install -r requirements/optional.txt` and try again'  # noqa
-                )  # noqa
-            print_log(
-                f'Creating {kwargs["model_name"]} by mlfoundations',  # noqa
-                'current')
+                raise ImportError(error_msg.format('\'open_clip_torch\''))
+            print_log(f'Creating {kwargs["model_name"]} by '
+                      'mlfoundations', 'current')
             self.model = open_clip.create_model(*args, **kwargs)
+
+        elif clip_type == 'huggingface':
+            try:
+                import transformers
+            except ImportError:
+                raise ImportError(error_msg.format('\'transforms\''))
+            # NOTE: use CLIPTextModel to adopt stable diffusion pipeline
+            model_cls = transformers.CLIPTextModel
+            self.model = model_cls.from_pretrained(*args, **kwargs)
+            self.config = self.model.config
+            print_log(
+                f'Creating {self.model.name_or_path} '
+                'by \'HuggingFace\'', 'current')
+
         self.model.eval().requires_grad_(False)
 
     def forward(self, *args, **kwargs):
         """Forward function."""
         return self.model(*args, **kwargs)
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/disco_diffusion/disco.py` & `mmedit-1.0.0rc7/mmedit/models/editors/disco_diffusion/disco.py`

 * *Files 0% similar despite different names*

```diff
@@ -199,15 +199,15 @@
         model_stats = self.guider.compute_prompt_stats(
             text_prompts=text_prompts)
         timesteps = infer_scheduler.timesteps[skip_steps:]
         if show_progress:
             timesteps = tqdm(timesteps)
         for t in timesteps:
             # 1. predicted model_output
-            model_output = self.unet(image, t)['outputs']
+            model_output = self.unet(image, t)['sample']
 
             # 2. compute previous image: x_t -> x_t-1
             cond_kwargs = dict(
                 model_stats=model_stats,
                 init_image=init_image,
                 unet=self.unet,
                 clip_guidance_scale=clip_guidance_scale,
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/disco_diffusion/guider.py` & `mmedit-1.0.0rc7/mmedit/models/editors/disco_diffusion/guider.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,26 +1,28 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import math
 
-import clip
 import lpips
 import numpy as np
 import pandas as pd
 import torch
 import torch.nn as nn
 import torch.nn.functional as F
 import torchvision.transforms as T
 import torchvision.transforms.functional as TF
 from mmengine.utils import digit_version
 from resize_right import resize
 from torchvision import __version__ as TORCHVISION_VERSION
 
 from mmedit.models.losses import tv_loss
+from mmedit.utils import try_import
 from .secondary_model import alpha_sigma_to_t
 
+clip = try_import('clip')
+
 normalize = T.Normalize(
     mean=[0.48145466, 0.4578275, 0.40821073],
     std=[0.26862954, 0.26130258, 0.27577711])
 
 
 def sinc(x):
     """
@@ -305,14 +307,19 @@
 
     Args:
         clip_models (List[Dict]): List of clip model settings.
     """
 
     def __init__(self, clip_models):
         super().__init__()
+
+        assert clip is not None, (
+            "Cannot import 'clip'. Please install 'clip' via "
+            "\"pip install git+https://github.com/openai/CLIP.git\".")
+
         self.clip_models = clip_models
         self.lpips_model = lpips.LPIPS(net='vgg')
 
     def frame_prompt_from_text(self, text_prompts, frame_num=0):
         """Get current frame prompt."""
         prompts_series = split_prompts(text_prompts)
         if prompts_series is not None and frame_num >= len(prompts_series):
@@ -429,15 +436,15 @@
                     (1 - diffusion_scheduler.alphas_cumprod[t])**0.5,
                     dtype=torch.float32)
                 cosine_t = alpha_sigma_to_t(alpha, sigma).to(x.device)
                 model_output = secondary_model(
                     x, cosine_t[None].repeat([x.shape[0]]))
                 pred_original_sample = model_output['pred']
             else:
-                model_output = model(x, t)['outputs']
+                model_output = model(x, t)['sample']
                 model_output, predicted_variance = torch.split(
                     model_output, x.shape[1], dim=1)
                 alpha_prod_t = 1 - beta_prod_t
                 pred_original_sample = (x - beta_prod_t**(0.5) *
                                         model_output) / alpha_prod_t**(0.5)
             # fac = diffusion_scheduler_output['beta_prod_t']** (0.5)
             # x_in = diffusion_scheduler_output['original_sample'] * fac + x * (1 - fac) # noqa
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/disco_diffusion/secondary_model.py` & `mmedit-1.0.0rc7/mmedit/models/editors/disco_diffusion/secondary_model.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/duf/duf.py` & `mmedit-1.0.0rc7/mmedit/models/editors/duf/duf.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/edsr/edsr_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/edsr/edsr_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/edvr/edvr.py` & `mmedit-1.0.0rc7/mmedit/models/editors/edvr/edvr.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/edvr/edvr_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/edvr/edvr_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/eg3d/camera.py` & `mmedit-1.0.0rc7/mmedit/models/editors/eg3d/camera.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/eg3d/dual_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/eg3d/dual_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/eg3d/eg3d.py` & `mmedit-1.0.0rc7/mmedit/models/editors/eg3d/eg3d.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/eg3d/eg3d_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/eg3d/eg3d_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/eg3d/eg3d_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/eg3d/eg3d_modules.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/eg3d/eg3d_utils.py` & `mmedit-1.0.0rc7/mmedit/models/editors/eg3d/eg3d_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/eg3d/ray_sampler.py` & `mmedit-1.0.0rc7/mmedit/models/editors/eg3d/ray_sampler.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/eg3d/renderer.py` & `mmedit-1.0.0rc7/mmedit/models/editors/eg3d/renderer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/esrgan/esrgan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/esrgan/esrgan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/esrgan/rrdb_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/esrgan/rrdb_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/fba/fba_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/fba/fba_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/fba/fba_encoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/fba/fba_encoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/flavr/flavr.py` & `mmedit-1.0.0rc7/mmedit/models/editors/flavr/flavr.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/flavr/flavr_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/flavr/flavr_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/gca/gca.py` & `mmedit-1.0.0rc7/mmedit/models/editors/gca/gca.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/gca/gca_module.py` & `mmedit-1.0.0rc7/mmedit/models/editors/gca/gca_module.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/gca/resgca_dec.py` & `mmedit-1.0.0rc7/mmedit/models/editors/gca/resgca_dec.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/gca/resgca_enc.py` & `mmedit-1.0.0rc7/mmedit/models/editors/gca/resgca_enc.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ggan/ggan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/ggan/ggan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/glean/glean_styleganv2.py` & `mmedit-1.0.0rc7/mmedit/models/editors/glean/glean_styleganv2.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_dilation.py` & `mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_dilation.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_disc.py` & `mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_disc.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_encoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_encoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_encoder_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/global_local/gl_inpaintor.py` & `mmedit-1.0.0rc7/mmedit/models/editors/global_local/gl_inpaintor.py`

 * *Files 2% similar despite different names*

```diff
@@ -176,15 +176,17 @@
         log_vars = {}
 
         masked_img = batch_inputs  # float
         gt_img = data_samples.gt_img
         mask = data_samples.mask
         mask = mask.float()
 
-        bbox_tensor = torch.LongTensor(data_samples.mask_bbox)
+        # PyTorch 2.0 could not compile 'data_samples.mask_bbox'
+        # bbox_tensor = torch.LongTensor(data_samples.mask_bbox)
+        bbox_tensor = torch.LongTensor(data_samples.metainfo['mask_bbox'])
 
         input_x = torch.cat([masked_img, mask], dim=1)
         fake_res = self.generator(input_x)
         fake_img = gt_img * (1. - mask) + fake_res * mask
 
         fake_local, bbox_new = extract_around_bbox(fake_img, bbox_tensor,
                                                    self.train_cfg.local_size)
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/guided_diffusion/adm.py` & `mmedit-1.0.0rc7/mmedit/models/editors/guided_diffusion/adm.py`

 * *Files 1% similar despite different names*

```diff
@@ -158,15 +158,15 @@
 
         timesteps = infer_scheduler.timesteps
 
         if show_progress and mmengine.dist.is_main_process():
             timesteps = tqdm(timesteps)
         for t in timesteps:
             # 1. predicted model_output
-            model_output = self.unet(image, t, label=labels)['outputs']
+            model_output = self.unet(image, t, label=labels)['sample']
 
             # 2. compute previous image: x_t -> x_t-1
             if classifier_scale > 0 and self.classifier is not None:
                 cond_fn = classifier_grad
                 cond_kwargs = dict(
                     y=labels,
                     classifier=self.classifier,
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/guided_diffusion/classifier.py` & `mmedit-1.0.0rc7/mmedit/models/editors/guided_diffusion/classifier.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/iconvsr/iconvsr_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/iconvsr/iconvsr_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/indexnet/indexnet.py` & `mmedit-1.0.0rc7/mmedit/models/editors/indexnet/indexnet.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/indexnet/indexnet_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/indexnet/indexnet_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/indexnet/indexnet_encoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/indexnet/indexnet_encoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/color_utils.py` & `mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/color_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/colorization_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/colorization_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/fusion_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/fusion_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/inst_colorization.py` & `mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/inst_colorization.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/inst_colorization/weight_layer.py` & `mmedit-1.0.0rc7/mmedit/models/editors/inst_colorization/weight_layer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/liif/liif.py` & `mmedit-1.0.0rc7/mmedit/models/editors/liif/liif.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/liif/liif_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/liif/liif_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/liif/mlp_refiner.py` & `mmedit-1.0.0rc7/mmedit/models/editors/liif/mlp_refiner.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/lsgan/lsgan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/lsgan/lsgan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/lsgan/lsgan_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/lsgan/lsgan_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/lsgan/lsgan_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/lsgan/lsgan_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/mspie/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/editors/mspie/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/mspie/mspie_stylegan2.py` & `mmedit-1.0.0rc7/mmedit/models/editors/mspie/mspie_stylegan2.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/mspie/mspie_stylegan2_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/mspie/mspie_stylegan2_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/mspie/mspie_stylegan2_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/mspie/mspie_stylegan2_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/mspie/mspie_stylegan2_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/mspie/mspie_stylegan2_modules.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,22 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from copy import deepcopy
 
 import torch
 import torch.nn as nn
 import torch.nn.functional as F
 
-from ...base_archs import conv2d, conv_transpose2d
+try:
+    from mmcv.ops import conv2d, conv_transpose2d
+except ImportError:
+    conv2d = None
+    conv_transpose2d = None
+    print('Warning: mmcv.ops.conv2d, mmcv.ops.conv_transpose2d'
+          'are not available.')
+
 from ..pggan import equalized_lr
 from ..stylegan1 import Blur, EqualLinearActModule, NoiseInjection
 from ..stylegan2.stylegan2_modules import _FusedBiasLeakyReLU
 
 
 class ModulatedPEConv2d(nn.Module):
     r"""Modulated Conv2d in StyleGANv2 with Positional Encoding (PE).
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/mspie/pe_singan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/mspie/pe_singan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/mspie/pe_singan_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/mspie/pe_singan_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/mspie/positional_encoding.py` & `mmedit-1.0.0rc7/mmedit/models/editors/mspie/positional_encoding.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/nafnet/naf_avgpool2d.py` & `mmedit-1.0.0rc7/mmedit/models/editors/nafnet/naf_avgpool2d.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/nafnet/naf_layerNorm2d.py` & `mmedit-1.0.0rc7/mmedit/models/editors/nafnet/naf_layerNorm2d.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/nafnet/nafbaseline_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/nafnet/nafbaseline_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/nafnet/nafnet_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/nafnet/nafnet_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pconv/mask_conv_module.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pconv/mask_conv_module.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pconv/partial_conv.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pconv/partial_conv.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pconv/pconv_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pconv/pconv_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pconv/pconv_encoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pconv/pconv_encoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pconv/pconv_encoder_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pconv/pconv_encoder_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pconv/pconv_inpaintor.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pconv/pconv_inpaintor.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pggan/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pggan/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pggan/pggan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pggan/pggan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pggan/pggan_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pggan/pggan_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pggan/pggan_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pggan/pggan_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pggan/pggan_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pggan/pggan_modules.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pix2pix/pix2pix.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pix2pix/pix2pix.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pix2pix/pix2pix_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pix2pix/pix2pix_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/pix2pix/pix2pix_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/pix2pix/pix2pix_modules.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/plain/plain_decoder.py` & `mmedit-1.0.0rc7/mmedit/models/editors/plain/plain_decoder.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/plain/plain_refiner.py` & `mmedit-1.0.0rc7/mmedit/models/editors/plain/plain_refiner.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/rdn/rdn_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/rdn/rdn_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/real_basicvsr/real_basicvsr.py` & `mmedit-1.0.0rc7/mmedit/models/editors/real_basicvsr/real_basicvsr.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,12 +1,15 @@
 # Copyright (c) OpenMMLab. All rights reserved.
+from typing import Dict, List
+
 import torch
 import torch.nn.functional as F
 from mmengine.optim import OptimWrapperDict
 
+from mmedit.models.utils import set_requires_grad
 from mmedit.registry import MODELS
 from ..real_esrgan import RealESRGAN
 
 
 @MODELS.register_module()
 class RealBasicVSR(RealESRGAN):
     """RealBasicVSR model for real-world video super-resolution.
@@ -131,37 +134,71 @@
             batch_gt_data=(gt_pixel, gt_percep, gt_gan))
 
         if self.cleaning_loss:
             losses['loss_clean'] = self.cleaning_loss(fake_g_lq, gt_clean)
 
         return losses
 
-    def d_step_with_optim(self, batch_outputs: torch.Tensor,
-                          batch_gt_data: torch.Tensor,
-                          optim_wrapper: OptimWrapperDict):
-        """D step with optim of GAN: Calculate losses of discriminator and run
-        optim.
+    def train_step(self, data: List[dict],
+                   optim_wrapper: OptimWrapperDict) -> Dict[str, torch.Tensor]:
+        """Train step of GAN-based method.
 
         Args:
-            batch_outputs (Tensor): Batch output of generator.
-            batch_gt_data (Tensor): Batch GT data.
-            optim_wrapper (OptimWrapperDict): Optim wrapper dict.
+            data (List[dict]): Data sampled from dataloader.
+            optim_wrapper (OptimWrapper): OptimWrapper instance
+                used to update model parameters.
 
         Returns:
-            dict: Dict of parsed losses.
+            Dict[str, torch.Tensor]: A ``dict`` of tensor for logging.
         """
 
-        gt_pixel, gt_percep, gt_gan, gt_clean = batch_gt_data
-        fake_g_output, fake_g_lq = batch_outputs
-        fake_g_output = fake_g_output.view(gt_pixel.shape)
+        g_optim_wrapper = optim_wrapper['generator']
 
-        return super().d_step_with_optim(
-            batch_outputs=fake_g_output,
-            batch_gt_data=(gt_pixel, gt_percep, gt_gan),
-            optim_wrapper=optim_wrapper)
+        data = self.data_preprocessor(data, True)
+        batch_inputs = data['inputs']
+        data_samples = data['data_samples']
+        batch_gt_data = self.extract_gt_data(data_samples)
+
+        log_vars = dict()
+
+        with g_optim_wrapper.optim_context(self):
+            batch_outputs = self.forward_train(batch_inputs, data_samples)
+
+        if self.if_run_g():
+            set_requires_grad(self.discriminator, False)
+
+            log_vars_d = self.g_step_with_optim(
+                batch_outputs=batch_outputs,
+                batch_gt_data=batch_gt_data,
+                optim_wrapper=optim_wrapper)
+
+            log_vars.update(log_vars_d)
+
+        if self.if_run_d():
+            set_requires_grad(self.discriminator, True)
+
+            gt_pixel, gt_percep, gt_gan, gt_clean = batch_gt_data
+            fake_g_output, fake_g_lq = batch_outputs
+            fake_g_output = fake_g_output.view(gt_pixel.shape)
+
+            for _ in range(self.disc_repeat):
+                # detach before function call to resolve PyTorch2.0 compile bug
+                log_vars_d = self.d_step_with_optim(
+                    batch_outputs=fake_g_output.detach(),
+                    batch_gt_data=(gt_pixel, gt_percep, gt_gan),
+                    optim_wrapper=optim_wrapper)
+
+            log_vars.update(log_vars_d)
+
+        if 'loss' in log_vars:
+            log_vars.pop('loss')
+
+        self.step_counter += 1
+
+        return log_vars
 
     def forward_train(self, batch_inputs, data_samples=None):
         """Forward Train.
 
         Run forward of generator with ``return_lqs=True``
 
         Args:
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/real_basicvsr/real_basicvsr_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/real_basicvsr/real_basicvsr_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/real_esrgan/real_esrgan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/real_esrgan/real_esrgan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/real_esrgan/unet_disc.py` & `mmedit-1.0.0rc7/mmedit/models/editors/real_esrgan/unet_disc.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/restormer/restormer_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/restormer/restormer_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/sagan/sagan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/sagan/sagan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/sagan/sagan_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/sagan/sagan_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/sagan/sagan_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/sagan/sagan_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/sagan/sagan_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/sagan/sagan_modules.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/singan/singan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/singan/singan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/singan/singan_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/singan/singan_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/singan/singan_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/singan/singan_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/singan/singan_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/singan/singan_modules.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/srcnn/srcnn_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/srcnn/srcnn_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/srgan/modified_vgg.py` & `mmedit-1.0.0rc7/mmedit/models/editors/srgan/modified_vgg.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/srgan/sr_resnet.py` & `mmedit-1.0.0rc7/mmedit/models/editors/srgan/sr_resnet.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/srgan/srgan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/srgan/srgan.py`

 * *Files 1% similar despite different names*

```diff
@@ -304,16 +304,17 @@
 
             log_vars.update(log_vars_d)
 
         if self.if_run_d():
             set_requires_grad(self.discriminator, True)
 
             for _ in range(self.disc_repeat):
+                # detach before function call to resolve PyTorch2.0 compile bug
                 log_vars_d = self.d_step_with_optim(
-                    batch_outputs=batch_outputs,
+                    batch_outputs=batch_outputs.detach(),
                     batch_gt_data=batch_gt_data,
                     optim_wrapper=optim_wrapper)
 
             log_vars.update(log_vars_d)
 
         if 'loss' in log_vars:
             log_vars.pop('loss')
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stable_diffusion/clip_wrapper.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stable_diffusion/clip_wrapper.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stable_diffusion/stable_diffusion.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stable_diffusion/stable_diffusion.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,130 +1,123 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import inspect
-import os.path as osp
+from copy import deepcopy
 from typing import Dict, List, Optional, Union
 
 import torch
+import torch.nn as nn
 from mmengine.logging import MMLogger
 from mmengine.model import BaseModel
 from mmengine.runner import set_random_seed
-from mmengine.runner.checkpoint import _load_checkpoint
+from PIL import Image
 from tqdm.auto import tqdm
+from transformers import CLIPTokenizer
 
+from mmedit.models.utils import build_module, set_xformers
 from mmedit.registry import DIFFUSION_SCHEDULERS, MODELS
-from .clip_wrapper import load_clip_submodels
-from .vae import AutoencoderKL
 
 logger = MMLogger.get_current_instance()
 
+ModelType = Union[Dict, nn.Module]
+
 
 @MODELS.register_module('sd')
 @MODELS.register_module()
 class StableDiffusion(BaseModel):
-    """class to run stable diffsuion pipeline.
+    """Class for Stable Diffusion. Refers to https://github.com/Stability-
+    AI/stablediffusion and https://github.com/huggingface/diffusers/blob/main/s
+    rc/diffusers/pipelines/stable_diffusion/pipeline_stable_diffusion_attend_an
+    d_excite.py  # noqa.
 
     Args:
-        diffusion_scheduler(dict): Diffusion scheduler config.
-        unet_cfg(dict): Unet config.
-        vae_cfg(dict): Vae config.
-        pretrained_ckpt_path(dict):
-            Pretrained ckpt path for submodels in stable diffusion.
-        requires_safety_checker(bool):
-            whether to run safety checker after image generated.
-        unet_sample_size(int): sampel size for unet.
+        unet (Union[dict, nn.Module]): The config or module for Unet model.
+        text_encoder (Union[dict, nn.Module]): The config or module for text
+            encoder.
+        vae (Union[dict, nn.Module]): The config or module for VAE model.
+        tokenizer (str): The **name** for CLIP tokenizer.
+        schedule (Union[dict, nn.Module]): The config or module for diffusion
+            scheduler.
+        test_scheduler (Union[dict, nn.Module], optional): The config or
+            module for diffusion scheduler in test stage (`self.infer`). If not
+            passed, will use the same scheduler as `schedule`. Defaults to
+            None.
+        enable_xformers (bool, optional): Whether to use xformers.
+            Defaults to True.
+        data_preprocessor (dict, optional): The pre-process config of
+            :class:`BaseDataPreprocessor`.
+        init_cfg (dict, optional): The weight initialized config for
+            :class:`BaseModule`.
     """
 
     def __init__(self,
-                 diffusion_scheduler,
-                 unet,
-                 vae,
-                 requires_safety_checker=True,
-                 unet_sample_size=64,
-                 init_cfg=None):
-        super().__init__()
-
-        self.device = torch.device('cpu')
-        self.submodels = [
-            'tokenizer', 'vae', 'scheduler', 'unet', 'feature_extractor',
-            'text_encoder'
-        ]
-        self.requires_safety_checker = requires_safety_checker
-
-        self.scheduler = DIFFUSION_SCHEDULERS.build(
-            diffusion_scheduler) if isinstance(diffusion_scheduler,
-                                               dict) else diffusion_scheduler
-        self.scheduler.order = 1
-        self.scheduler.init_noise_sigma = 1.0
-
-        self.unet_sample_size = unet_sample_size
-        self.unet = MODELS.build(unet) if isinstance(unet, dict) else unet
+                 vae: ModelType,
+                 text_encoder: ModelType,
+                 tokenizer: str,
+                 unet: ModelType,
+                 scheduler: ModelType,
+                 test_scheduler: Optional[ModelType] = None,
+                 enable_xformers: bool = True,
+                 data_preprocessor: Optional[ModelType] = dict(
+                     type='EditDataPreprocessor'),
+                 init_cfg: Optional[dict] = None):
+
+        # TODO: support `from_pretrained` for this class
+        super().__init__(data_preprocessor, init_cfg)
+
+        self.vae = build_module(vae, MODELS)
+        self.unet = build_module(unet, MODELS)
+        self.scheduler = build_module(scheduler, DIFFUSION_SCHEDULERS)
+        if test_scheduler is None:
+            self.test_scheduler = deepcopy(self.scheduler)
+        else:
+            self.test_scheduler = build_module(test_scheduler,
+                                               DIFFUSION_SCHEDULERS)
+        self.text_encoder = build_module(text_encoder, MODELS)
+        if isinstance(tokenizer, nn.Module):
+            self.tokenizer = tokenizer
+        else:
+            # NOTE: here we assume tokenizer is an string
+            # TODO: maybe support a tokenizer wrapper later
+            self.tokenizer = CLIPTokenizer.from_pretrained(
+                tokenizer, subfolder='tokenizer')
 
-        self.vae = AutoencoderKL(**vae) if isinstance(vae, dict) else vae
+        self.unet_sample_size = self.unet.sample_size
         self.vae_scale_factor = 2**(len(self.vae.block_out_channels) - 1)
 
-        self.init_cfg = init_cfg
-        self.init_weights()
-
-    def init_weights(self):
-        """load pretrained ckpt for each submodel."""
-        if self.init_cfg is not None and self.init_cfg['type'] == 'Pretrained':
-            map_location = self.init_cfg.get('map_location', 'cpu')
-            pretrained_model_path = self.init_cfg.get('pretrained_model_path',
-                                                      None)
-            if pretrained_model_path:
-                unet_ckpt_path = osp.join(pretrained_model_path, 'unet',
-                                          'diffusion_pytorch_model.bin')
-                if unet_ckpt_path:
-                    state_dict = _load_checkpoint(unet_ckpt_path, map_location)
-                    self.unet.load_state_dict(state_dict, strict=True)
-
-                vae_ckpt_path = osp.join(pretrained_model_path, 'vae',
-                                         'diffusion_pytorch_model.bin')
-                if vae_ckpt_path:
-                    state_dict = _load_checkpoint(vae_ckpt_path, map_location)
-                    self.vae.load_state_dict(state_dict, strict=True)
-
-        self.tokenizer, self.feature_extractor, self.text_encoder, self.safety_checker = load_clip_submodels(  # noqa
-            self.init_cfg, self.submodels, self.requires_safety_checker)
+        self.enable_xformers = enable_xformers
+        self.set_xformers()
 
-    def to(self, torch_device: Optional[Union[str, torch.device]] = None):
-        """put submodels to torch device.
-
-        Args:
-            torch_device(Optional[Union[str, torch.device]]):
-                device to put, default to None.
+    def set_xformers(self) -> nn.Module:
+        """Set xformers for the model.
 
         Returns:
-            self(StableDiffusion):
-                class instance itsself.
+            nn.Module: The model with xformers.
         """
-        if torch_device is None:
-            return self
+        if self.enable_xformers:
+            set_xformers(self)
 
-        for name in self.submodels:
-            module = getattr(self, name)
-            if isinstance(module, torch.nn.Module):
-                module.to(torch_device)
-        self.device = torch.device(torch_device)
-        return self
+    @property
+    def device(self):
+        return next(self.parameters()).device
 
     @torch.no_grad()
     def infer(self,
               prompt: Union[str, List[str]],
               height: Optional[int] = None,
               width: Optional[int] = None,
               num_inference_steps: int = 50,
               guidance_scale: float = 7.5,
               negative_prompt: Optional[Union[str, List[str]]] = None,
               num_images_per_prompt: Optional[int] = 1,
               eta: float = 0.0,
               generator: Optional[torch.Generator] = None,
               latents: Optional[torch.FloatTensor] = None,
               show_progress=True,
-              seed=1):
+              seed=1,
+              return_type='image'):
         """Function invoked when calling the pipeline for generation.
 
         Args:
             prompt (`str` or `List[str]`):
                 The prompt or prompts to guide the image generation.
             height (`int`, *optional*,
                 defaults to self.unet_sample_size * self.vae_scale_factor):
@@ -156,20 +149,26 @@
                 Pre-generated noisy latents,
                 sampled from a Gaussian distribution,
                 to be used as inputs for image generation.
                 Can be used to tweak the same generation
                 with different prompts.
                 If not provided, a latents tensor will be
                 generated by sampling using the supplied random `generator`.
+            return_type (str): The return type of the inference results.
+                Supported types are 'image', 'numpy', 'tensor'. If 'image'
+                is passed, a list of PIL images will be returned. If 'numpy'
+                is passed, a numpy array with shape [N, C, H, W] will be
+                returned, and the value range will be same as decoder's
+                output range. If 'tensor' is passed, the decoder's output
+                will be returned. Defaults to 'image'.
 
         Returns:
-            dict:['samples', 'nsfw_content_detected']:
-                'samples': image result samples
-                'nsfw_content_detected': nsfw content flags for image samples.
+            dict: A dict containing the generated images.
         """
+        assert return_type in ['image', 'tensor', 'numpy']
         set_random_seed(seed=seed)
 
         # 0. Default height and width to unet
         height = height or self.unet_sample_size * self.vae_scale_factor
         width = width or self.unet_sample_size * self.vae_scale_factor
 
         # 1. Check inputs. Raise error if not correct
@@ -188,15 +187,14 @@
         # 3. Encode input prompt
         text_embeddings = self._encode_prompt(prompt, device,
                                               num_images_per_prompt,
                                               do_classifier_free_guidance,
                                               negative_prompt)
 
         # 4. Prepare timesteps
-        # self.scheduler.set_timesteps(num_inference_steps, device=device)
         self.scheduler.set_timesteps(num_inference_steps)
         timesteps = self.scheduler.timesteps
 
         # 5. Prepare latent variables
         num_channels_latents = self.unet.in_channels
         latents = self.prepare_latents(
             batch_size * num_images_per_prompt,
@@ -216,63 +214,79 @@
         # 7. Denoising loop
         if show_progress:
             timesteps = tqdm(timesteps)
         for i, t in enumerate(timesteps):
             # expand the latents if we are doing classifier free guidance
             latent_model_input = torch.cat(
                 [latents] * 2) if do_classifier_free_guidance else latents
-            # latent_model_input = \
-            # self.scheduler.scale_model_input(latent_model_input, t)
+            latent_model_input = self.scheduler.scale_model_input(
+                latent_model_input, t)
 
             # predict the noise residual
             noise_pred = self.unet(
                 latent_model_input, t,
-                encoder_hidden_states=text_embeddings)['outputs']
+                encoder_hidden_states=text_embeddings)['sample']
 
             # perform guidance
             if do_classifier_free_guidance:
                 noise_pred_uncond, noise_pred_text = noise_pred.chunk(2)
                 noise_pred = noise_pred_uncond + guidance_scale * (
                     noise_pred_text - noise_pred_uncond)
 
                 # compute the previous noisy sample x_t -> x_t-1
                 latents = self.scheduler.step(
                     noise_pred, t, latents, **extra_step_kwargs)['prev_sample']
 
         # 8. Post-processing
-        image = self.decode_latents(latents)
+        image = self.decode_latents(latents.to(self.vae.dtype))
+        if return_type == 'image':
+            image = self.output_to_pil(image)
+        elif return_type == 'numpy':
+            image = image.cpu().numpy()
+        else:
+            assert return_type == 'tensor', (
+                'Only support \'image\', \'numpy\' and \'tensor\' for '
+                f'return_type, but receive {return_type}')
+
+        return {'samples': image}
+
+    def output_to_pil(self, image) -> List[Image.Image]:
+        """Convert output tensor to PIL image. Output tensor will be de-normed
+        to [0, 255] by `EditDataPreprocessor.destruct`. Due to no
+        `data_samples` is passed, color order conversion will not be performed.
 
-        # 9. Run safety checker
-        image, has_nsfw_concept = self.run_safety_checker(
-            image, device, text_embeddings.dtype)
-        image = image[0].permute([2, 0, 1])
+        Args:
+            image (torch.Tensor): The output tensor of the decoder.
 
-        return {'samples': image, 'nsfw_content_detected': has_nsfw_concept}
+        Returns:
+            List[Image.Image]: The list of processed PIL images.
+        """
+        image = self.data_preprocessor.destruct(image)
+        image = image.permute(0, 2, 3, 1).to(torch.uint8).cpu().numpy()
+        image = [Image.fromarray(img) for img in image]
+        return image
 
     def _encode_prompt(self, prompt, device, num_images_per_prompt,
                        do_classifier_free_guidance, negative_prompt):
         """Encodes the prompt into text encoder hidden states.
 
         Args:
-            prompt (str or list(int)):
-                prompt to be encoded.
-            device: (torch.device):
-                torch device.
-            num_images_per_prompt (int):
-                number of images that should be generated per prompt.
-            do_classifier_free_guidance (`bool`):
-                whether to use classifier free guidance or not.
-            negative_prompt (str or List[str]):
-                The prompt or prompts not to guide the image generation.
-                Ignored when not using guidance (i.e., ignored
-                if `guidance_scale` is less than `1`).
+            prompt (str or list(int)): prompt to be encoded.
+            device: (torch.device): torch device.
+            num_images_per_prompt (int): number of images that should be
+                generated per prompt.
+            do_classifier_free_guidance (`bool`): whether to use classifier
+                free guidance or not.
+            negative_prompt (str or List[str]): The prompt or prompts not
+                to guide the image generation. Ignored when not using
+                guidance (i.e., ignored if `guidance_scale` is less than `1`).
 
         Returns:
-            text_embeddings (torch.Tensor):
-                text embeddings generated by clip text encoder.
+            text_embeddings (torch.Tensor): text embeddings generated by
+                clip text encoder.
         """
         batch_size = len(prompt) if isinstance(prompt, list) else 1
 
         text_inputs = self.tokenizer(
             prompt,
             padding='max_length',
             max_length=self.tokenizer.model_max_length,
@@ -364,57 +378,28 @@
             # Here we concatenate the unconditional
             # and text embeddings into a single batch
             # to avoid doing two forward passes
             text_embeddings = torch.cat([uncond_embeddings, text_embeddings])
 
         return text_embeddings
 
-    def run_safety_checker(self, image, device, dtype):
-        """run safety checker to check whether image has nsfw content.
-
-        Args:
-            image (numpy.ndarray):
-                image generated by stable diffusion.
-            device (torch.device):
-                device to run safety checker.
-            dtype (torch.dtype):
-                float type to run.
-
-        Returns:
-            image (numpy.ndarray):
-                black image if nsfw content detected else input image.
-            has_nsfw_concept (list[bool]):
-                flag list to indicate nsfw content detected.
-        """
-        if self.safety_checker is not None:
-            safety_checker_input = self.feature_extractor(
-                image[0], return_tensors='pt').to(device)
-            image, has_nsfw_concept = self.safety_checker(
-                images=image,
-                clip_input=safety_checker_input.pixel_values.to(dtype))
-        else:
-            has_nsfw_concept = None
-        return image, has_nsfw_concept
-
     def decode_latents(self, latents):
         """use vae to decode latents.
 
         Args:
             latents (torch.Tensor): latents to decode.
 
         Returns:
-            image (numpy.ndarray): image result.
+            image (torch.Tensor): image result.
         """
         latents = 1 / 0.18215 * latents
-        image = self.vae.decode(latents).sample
-        image = (image / 2 + 0.5).clamp(0, 1)
+        image = self.vae.decode(latents)['sample']
         # we always cast to float32 as this does not cause
         # significant overhead and is compatible with bfloa16
-        image = image.cpu().permute(0, 2, 3, 1).float()
-        return image
+        return image.float()
 
     def prepare_extra_step_kwargs(self, generator, eta):
         """prepare extra kwargs for the scheduler step.
 
         Args:
             generator (torch.Generator):
                 generator for random functions.
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stable_diffusion/vae.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stable_diffusion/vae.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,14 +7,16 @@
 import torch
 import torch.nn as nn
 import torch.nn.functional as F
 from addict import Dict
 from mmengine.utils.dl_utils import TORCH_VERSION
 from mmengine.utils.version_utils import digit_version
 
+from mmedit.registry import MODELS
+
 
 class Downsample2D(nn.Module):
     """A downsampling layer with an optional convolution.
 
     Args:
         channels (int): channels in the inputs and outputs.
         use_conv (bool): a bool determining if a convolution is applied.
@@ -870,14 +872,15 @@
             dim=dims)  # noqa
 
     def mode(self):
         """return self.mean."""
         return self.mean
 
 
+@MODELS.register_module('EditAutoencoderKL')
 class AutoencoderKL(nn.Module):
     r"""Variational Autoencoder (VAE) model with KL loss
     from the paper Auto-Encoding Variational Bayes by Diederik P. Kingma
     and Max Welling.
 
     Args:
         in_channels (int, *optional*, defaults to 3):
@@ -940,14 +943,19 @@
         )
 
         self.quant_conv = torch.nn.Conv2d(2 * latent_channels,
                                           2 * latent_channels, 1)
         self.post_quant_conv = torch.nn.Conv2d(latent_channels,
                                                latent_channels, 1)
 
+    @property
+    def dtype(self):
+        """The data type of the parameters of VAE."""
+        return next(self.parameters()).dtype
+
     def encode(self, x: torch.FloatTensor, return_dict: bool = True) -> Dict:
         """encode input."""
         h = self.encoder(x)
         moments = self.quant_conv(h)
         posterior = DiagonalGaussianDistribution(moments)
 
         if not return_dict:
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/stylegan1.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/stylegan1.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/stylegan1_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/stylegan1_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/stylegan1_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/stylegan1_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/stylegan1_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/stylegan1_modules.py`

 * *Files 0% similar despite different names*

```diff
@@ -208,15 +208,15 @@
             x (Tensor): Input feature map with shape of (N, C, H, W).
 
         Returns:
             Tensor: Output feature map.
         """
 
         # In Tero's implementation, he uses fp32
-        return upfirdn2d(x, self.kernel.to(x.dtype), pad=self.pad)
+        return upfirdn2d(x, self.kernel.to(x.dtype), padding=self.pad)
 
 
 class AdaptiveInstanceNorm(nn.Module):
     r"""Adaptive Instance Normalization Module.
 
     Ref: https://github.com/rosinality/style-based-gan-pytorch/blob/master/model.py  # noqa
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan1/stylegan_utils.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan1/stylegan_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/ada/augment.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/ada/augment.py`

 * *Files 1% similar despite different names*

```diff
@@ -6,15 +6,20 @@
 # distribution of this software and related documentation without an express
 # license agreement from NVIDIA CORPORATION is strictly prohibited.
 
 import numpy as np
 import scipy.signal
 import torch
 
-from ....base_archs import conv2d_gradfix
+try:
+    from mmcv.ops import conv2d
+except ImportError:
+    conv2d = None
+    print('Warning: mmcv.ops.conv2d are not available.')
+
 from . import grid_sample_gradfix, misc, upfirdn2d
 
 # ----------------------------------------------------------------------------
 # Coefficients of various wavelet decomposition low-pass filters.
 
 wavelets = {
     'haar': [0.7071067811865476, 0.7071067811865476],
@@ -726,19 +731,19 @@
 
             # Apply filter.
             p = self.Hz_fbank.shape[1] // 2
             images = images.reshape(
                 [1, batch_size * num_channels, height, width])
             images = torch.nn.functional.pad(
                 input=images, pad=[p, p, p, p], mode='reflect')
-            images = conv2d_gradfix.conv2d(
+            images = conv2d(
                 input=images,
                 weight=Hz_prime.unsqueeze(2),
                 groups=batch_size * num_channels)
-            images = conv2d_gradfix.conv2d(
+            images = conv2d(
                 input=images,
                 weight=Hz_prime.unsqueeze(3),
                 groups=batch_size * num_channels)
             images = images.reshape([batch_size, num_channels, height, width])
 
         # ------------------------
         # Image-space corruptions.
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/ada/grid_sample_gradfix.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/ada/grid_sample_gradfix.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/ada/misc.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/ada/misc.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/ada/upfirdn2d.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/ada/upfirdn2d.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,11 +1,16 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import numpy as np
 import torch
-from mmcv.ops.upfirdn2d import upfirdn2d
+
+try:
+    from mmcv.ops import upfirdn2d
+except ImportError:
+    upfirdn2d = None
+    print('Warning: mmcv.ops.upfirdn2d is not available.')
 
 
 def _parse_scaling(scaling):
     if isinstance(scaling, int):
         scaling = [scaling, scaling]
     assert isinstance(scaling, (list, tuple))
     assert all(isinstance(x, int) for x in scaling)
@@ -77,16 +82,18 @@
     ]
 
     gain = gain * upx * upy
     f = f * (gain**(f.ndim / 2))
     if flip_filter:
         f = f.flip(list(range(f.ndim)))
     if f.ndim == 1:
-        x = upfirdn2d(x, f.unsqueeze(0), up=(upx, 1), pad=(p[0], p[1], 0, 0))
-        x = upfirdn2d(x, f.unsqueeze(1), up=(1, upy), pad=(0, 0, p[2], p[3]))
+        x = upfirdn2d(
+            x, f.unsqueeze(0), up=(upx, 1), padding=(p[0], p[1], 0, 0))
+        x = upfirdn2d(
+            x, f.unsqueeze(1), up=(1, upy), padding=(0, 0, p[2], p[3]))
     return x
 
 
 def setup_filter(f,
                  device=torch.device('cpu'),
                  normalize=True,
                  flip_filter=False,
@@ -179,11 +186,11 @@
         pady0 + (fh - downy + 1) // 2,
         pady1 + (fh - downy) // 2,
     ]
     if flip_filter:
         f = f.flip(list(range(f.ndim)))
     if f.ndim == 1:
         x = upfirdn2d(
-            x, f.unsqueeze(0), down=(downx, 1), pad=(p[0], p[1], 0, 0))
+            x, f.unsqueeze(0), down=(downx, 1), padding=(p[0], p[1], 0, 0))
         x = upfirdn2d(
-            x, f.unsqueeze(1), down=(1, downy), pad=(0, 0, p[2], p[3]))
+            x, f.unsqueeze(1), down=(1, downy), padding=(0, 0, p[2], p[3]))
     return x
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/stylegan2.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/stylegan2.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/stylegan2_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/stylegan2_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/stylegan2_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/stylegan2_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan2/stylegan2_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan2/stylegan2_modules.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,18 +6,26 @@
 from mmcv.ops.fused_bias_leakyrelu import (FusedBiasLeakyReLU,
                                            fused_bias_leakyrelu)
 from mmcv.ops.upfirdn2d import upfirdn2d
 from mmengine.dist import get_dist_info
 from mmengine.runner.amp import autocast
 
 from mmedit.models.base_archs import AllGatherLayer
-from ...base_archs import conv2d, conv_transpose2d
 from ..pggan import EqualizedLRConvModule, equalized_lr
 from ..stylegan1 import Blur, EqualLinearActModule, NoiseInjection, make_kernel
 
+try:
+    from mmcv.ops import conv2d, conv_transpose2d
+except ImportError:
+    import torch.nn.functional as F
+    conv2d = F.conv2d
+    conv_transpose2d = F.conv_transpose2d
+    print('Warning: mmcv.ops.conv2d, mmcv.ops.conv_transpose2d'
+          ' and mmcv.ops.upfirdn2d are not available.')
+
 
 class _FusedBiasLeakyReLU(FusedBiasLeakyReLU):
     """Wrap FusedBiasLeakyReLU to support FP16 training."""
 
     def forward(self, x):
         """Forward function.
 
@@ -50,27 +58,31 @@
         self.register_buffer('kernel', kernel)
 
         p = kernel.shape[0] - factor
 
         pad0 = (p + 1) // 2 + factor - 1
         pad1 = p // 2
 
-        self.pad = (pad0, pad1)
+        self.pad = (pad0, pad1, pad0, pad1)
 
     def forward(self, x):
         """Forward function.
 
         Args:
             x (Tensor): Input feature map with shape of (N, C, H, W).
 
         Returns:
             Tensor: Output feature map.
         """
         out = upfirdn2d(
-            x, self.kernel.to(x.dtype), up=self.factor, down=1, pad=self.pad)
+            x,
+            self.kernel.to(x.dtype),
+            up=self.factor,
+            down=1,
+            padding=self.pad)
 
         return out
 
 
 class DownsampleUpFIRDn(nn.Module):
     """UpFIRDn for Downsampling.
 
@@ -105,15 +117,15 @@
             Tensor: Output feature map.
         """
         out = upfirdn2d(
             input,
             self.kernel.to(input.dtype),
             up=1,
             down=self.factor,
-            pad=self.pad)
+            padding=self.pad)
 
         return out
 
 
 class ModulatedConv2d(nn.Module):
     r"""Modulated Conv2d in StyleGANv2.
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan3/stylegan3.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan3/stylegan3_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan3/stylegan3_modules.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,17 +1,25 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import numpy as np
 import scipy
 import torch
 import torch.nn as nn
+
+try:
+    from mmcv.ops import bias_act, conv2d_gradfix, filtered_lrelu
+except ImportError:
+    bias_act = None
+    conv2d_gradfix = None
+    filtered_lrelu = None
+    print('Warning: mmcv.ops.bias_act, mmcv.ops.conv2d_gradfix'
+          ' and mmcv.ops.filtered_lrelu are not available.')
+
 from mmengine.runner.amp import autocast
 
-from mmedit.models.base_archs import conv2d_gradfix
 from mmedit.registry import MODELS
-from .stylegan3_ops.ops import bias_act, filtered_lrelu
 
 
 def modulated_conv2d(
     x,
     w,
     s,
     demodulate=True,
@@ -112,15 +120,15 @@
             b = b.to(x.dtype)
             if self.bias_gain != 1:
                 b = b * self.bias_gain
         if self.activation == 'linear' and b is not None:
             x = torch.addmm(b.unsqueeze(0), x, w.t())
         else:
             x = x.matmul(w.t())
-            x = bias_act.bias_act(x, b, act=self.activation)
+            x = bias_act(x, b, act=self.activation)
         return x
 
 
 @MODELS.register_module()
 class MappingNetwork(nn.Module):
     """Style mapping network used in StyleGAN3. The main difference between it
     and styleganv1,v2 is that mean latent is registered as a buffer and dynamic
@@ -524,19 +532,19 @@
                 padding=self.conv_kernel - 1,
                 demodulate=(not self.is_torgb),
                 input_gain=input_gain)
 
             # Execute bias, filtered leaky ReLU, and clamping.
             gain = 1 if self.is_torgb else np.sqrt(2)
             slope = 1 if self.is_torgb else 0.2
-            x = filtered_lrelu.filtered_lrelu(
-                x=x,
-                fu=self.up_filter,
-                fd=self.down_filter,
-                b=self.bias.to(x.dtype),
+            x = filtered_lrelu(
+                input=x,
+                filter_up=self.up_filter,
+                filter_down=self.down_filter,
+                bias=self.bias.to(x.dtype),
                 up=self.up_factor,
                 down=self.down_factor,
                 padding=self.padding,
                 gain=gain,
                 slope=slope,
                 clamp=self.conv_clamp)
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/stylegan3/stylegan3_utils.py` & `mmedit-1.0.0rc7/mmedit/models/editors/stylegan3/stylegan3_utils.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,12 +1,19 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import numpy as np
 import torch
 
-from .stylegan3_ops.ops import upfirdn2d
+try:
+    from mmcv.ops import filter2d, upsample2d
+except ImportError:
+    filter2d = None
+    upsample2d = None
+    print(
+        'Warning: mmcv.ops.filter2d and mmcv.ops.upsample2d are not available.'
+    )
 
 
 def apply_integer_translation(x, tx, ty):
     _N, _C, H, W = x.shape
     tx = torch.as_tensor(tx * W).to(dtype=torch.float32, device=x.device)
     ty = torch.as_tensor(ty * H).to(dtype=torch.float32, device=x.device)
     ix = tx.round().to(torch.int64)
@@ -43,18 +50,16 @@
     zx1 = min(ix + a, 0) + W
     zy1 = min(iy + a, 0) + H
     if zx0 < zx1 and zy0 < zy1:
         taps = torch.arange(a * 2, device=x.device) - b
         filter_x = (sinc(taps - fx) * sinc((taps - fx) / a)).unsqueeze(0)
         filter_y = (sinc(taps - fy) * sinc((taps - fy) / a)).unsqueeze(1)
         y = x
-        y = upfirdn2d.filter2d(
-            y, filter_x / filter_x.sum(), padding=[b, a, 0, 0])
-        y = upfirdn2d.filter2d(
-            y, filter_y / filter_y.sum(), padding=[0, 0, b, a])
+        y = filter2d(y, filter_x / filter_x.sum(), padding=[b, a, 0, 0])
+        y = filter2d(y, filter_y / filter_y.sum(), padding=[0, 0, b, a])
         y = y[:, :,
               max(b - iy, 0):H + b + a + min(-iy - a, 0),
               max(b - ix, 0):W + b + a + min(-ix - a, 0)]
         z[:, :, zy0:zy1, zx0:zx1] = y
 
     m = torch.zeros_like(x)
     mx0 = max(ix + a, 0)
@@ -137,15 +142,15 @@
     theta[1, 2] += 1 / up / H
     theta[0, :] *= W / (W + p / up * 2)
     theta[1, :] *= H / (H + p / up * 2)
     theta = theta[:2, :3].unsqueeze(0).repeat([x.shape[0], 1, 1])
     g = torch.nn.functional.affine_grid(theta, x.shape, align_corners=False)
 
     # Resample image.
-    y = upfirdn2d.upsample2d(x=x, f=f, up=up, padding=p)
+    y = upsample2d(input=x, filter=f, up=up, padding=p)
     z = torch.nn.functional.grid_sample(
         y, g, mode='bilinear', padding_mode='zeros', align_corners=False)
 
     # Form mask.
     m = torch.zeros_like(y)
     c = p * 2 + 1
     m[:, :, c:-c, c:-c] = 1
@@ -162,12 +167,12 @@
 
 
 def apply_fractional_pseudo_rotation(x, angle, a=3, **filter_kwargs):
     angle = torch.as_tensor(angle).to(dtype=torch.float32, device=x.device)
     mat = rotation_matrix(-angle)
     f = construct_affine_bandlimit_filter(
         mat, a=a, amax=a * 2, up=1, **filter_kwargs)
-    y = upfirdn2d.filter2d(x=x, f=f)
+    y = filter2d(input=x, filter=f)
     m = torch.zeros_like(y)
     c = f.shape[0] // 2
     m[:, :, c:-c, c:-c] = 1
     return y, m
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/swinir/swinir_modules.py` & `mmedit-1.0.0rc7/mmedit/models/editors/swinir/swinir_modules.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/swinir/swinir_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/swinir/swinir_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/swinir/swinir_rstb.py` & `mmedit-1.0.0rc7/mmedit/models/editors/swinir/swinir_rstb.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/swinir/swinir_utils.py` & `mmedit-1.0.0rc7/mmedit/models/editors/swinir/swinir_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/tdan/tdan.py` & `mmedit-1.0.0rc7/mmedit/models/editors/tdan/tdan.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/tdan/tdan_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/tdan/tdan_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/tof/tof_vfi_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/tof/tof_vfi_net.py`

 * *Files 2% similar despite different names*

```diff
@@ -56,19 +56,19 @@
         Returns:
             Tensor: Interpolated frame with shape of (b, 3, h, w).
         """
 
         flow_10 = self.spynet(imgs[:, 0], imgs[:, 1]).permute(0, 2, 3, 1)
         flow_01 = self.spynet(imgs[:, 1], imgs[:, 0]).permute(0, 2, 3, 1)
 
-        wrap_frame0 = flow_warp(imgs[:, 0], flow_01 / 2)
-        wrap_frame1 = flow_warp(imgs[:, 1], flow_10 / 2)
+        warp_frame0 = flow_warp(imgs[:, 0], flow_01 / 2)
+        warp_frame1 = flow_warp(imgs[:, 1], flow_10 / 2)
 
-        wrap_frames = torch.stack([wrap_frame0, wrap_frame1], dim=1)
-        output = self.resnet(wrap_frames)
+        warp_frames = torch.stack([warp_frame0, warp_frame1], dim=1)
+        output = self.resnet(warp_frames)
 
         return output
 
 
 class BasicModule(nn.Module):
     """Basic module of SPyNet.
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/tof/tof_vsr_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/tof/tof_vsr_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ttsr/lte.py` & `mmedit-1.0.0rc7/mmedit/models/editors/ttsr/lte.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ttsr/search_transformer.py` & `mmedit-1.0.0rc7/mmedit/models/editors/ttsr/search_transformer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ttsr/ttsr.py` & `mmedit-1.0.0rc7/mmedit/models/editors/ttsr/ttsr.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,8 +1,10 @@
 # Copyright (c) OpenMMLab. All rights reserved.
+from typing import Dict, List
+
 import torch
 from mmengine.optim import OptimWrapperDict
 
 from mmedit.models.utils import set_requires_grad
 from mmedit.registry import MODELS
 from mmedit.structures import EditDataSample
 from ..srgan import SRGAN
@@ -190,26 +192,62 @@
 
         if e_optim_wrapper.should_update():
             e_optim_wrapper.step()
             e_optim_wrapper.zero_grad()
 
         return log_vars_g
 
-    def d_step_with_optim(self, batch_outputs, batch_gt_data, optim_wrapper):
-        """D step with optim of GAN: Calculate losses of discriminator and run
-        optim.
+    def train_step(self, data: List[dict],
+                   optim_wrapper: OptimWrapperDict) -> Dict[str, torch.Tensor]:
+        """Train step of GAN-based method.
 
         Args:
-            batch_outputs (Tuple[Tensor]): Batch output of generator.
-            batch_gt_data (Tensor): Batch GT data.
-            optim_wrapper (OptimWrapper): Optim wrapper of discriminator.
+            data (List[dict]): Data sampled from dataloader.
+            optim_wrapper (OptimWrapper): OptimWrapper instance
+                used to update model parameters.
 
         Returns:
-            dict: Dict of parsed losses.
+            Dict[str, torch.Tensor]: A ``dict`` of tensor for logging.
         """
 
-        pred, _, _ = batch_outputs
+        g_optim_wrapper = optim_wrapper['generator']
+
+        data = self.data_preprocessor(data, True)
+        batch_inputs = data['inputs']
+        data_samples = data['data_samples']
+        batch_gt_data = self.extract_gt_data(data_samples)
+
+        log_vars = dict()
+
+        with g_optim_wrapper.optim_context(self):
+            batch_outputs = self.forward_train(batch_inputs, data_samples)
+
+        if self.if_run_g():
+            set_requires_grad(self.discriminator, False)
+
+            log_vars_d = self.g_step_with_optim(
+                batch_outputs=batch_outputs,
+                batch_gt_data=batch_gt_data,
+                optim_wrapper=optim_wrapper)
+
+            log_vars.update(log_vars_d)
+
+        if self.if_run_d():
+            set_requires_grad(self.discriminator, True)
+
+            pred, _, _ = batch_outputs
+
+            for _ in range(self.disc_repeat):
+                # detach before function call to resolve PyTorch2.0 compile bug
+                log_vars_d = self.d_step_with_optim(
+                    batch_outputs=pred.detach(),
+                    batch_gt_data=batch_gt_data,
+                    optim_wrapper=optim_wrapper)
+
+            log_vars.update(log_vars_d)
+
+        if 'loss' in log_vars:
+            log_vars.pop('loss')
+
+        self.step_counter += 1
 
-        return super().d_step_with_optim(
-            batch_outputs=pred,
-            batch_gt_data=batch_gt_data,
-            optim_wrapper=optim_wrapper)
+        return log_vars
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ttsr/ttsr_disc.py` & `mmedit-1.0.0rc7/mmedit/models/editors/ttsr/ttsr_disc.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/ttsr/ttsr_net.py` & `mmedit-1.0.0rc7/mmedit/models/editors/ttsr/ttsr_net.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/wgan_gp/wgan_discriminator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/wgan_gp/wgan_discriminator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/wgan_gp/wgan_generator.py` & `mmedit-1.0.0rc7/mmedit/models/editors/wgan_gp/wgan_generator.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/wgan_gp/wgan_gp.py` & `mmedit-1.0.0rc7/mmedit/models/editors/wgan_gp/wgan_gp.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/editors/wgan_gp/wgan_gp_module.py` & `mmedit-1.0.0rc7/mmedit/models/editors/wgan_gp/wgan_gp_module.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/losses/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/clip_loss.py` & `mmedit-1.0.0rc7/mmedit/models/losses/clip_loss.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/composition_loss.py` & `mmedit-1.0.0rc7/mmedit/models/losses/composition_loss.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/face_id_loss.py` & `mmedit-1.0.0rc7/mmedit/models/losses/face_id_loss.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/feature_loss.py` & `mmedit-1.0.0rc7/mmedit/models/losses/feature_loss.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/gan_loss.py` & `mmedit-1.0.0rc7/mmedit/models/losses/gan_loss.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/gradient_loss.py` & `mmedit-1.0.0rc7/mmedit/models/losses/gradient_loss.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/clip_loss_comps.py` & `mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/clip_loss_comps.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/disc_auxiliary_loss_comps.py` & `mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/disc_auxiliary_loss_comps.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/face_id_loss_comps.py` & `mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/face_id_loss_comps.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/gan_loss_comps.py` & `mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/gan_loss_comps.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/loss_comps/gen_auxiliary_loss_comps.py` & `mmedit-1.0.0rc7/mmedit/models/losses/loss_comps/gen_auxiliary_loss_comps.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/loss_wrapper.py` & `mmedit-1.0.0rc7/mmedit/models/losses/loss_wrapper.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/perceptual_loss.py` & `mmedit-1.0.0rc7/mmedit/models/losses/perceptual_loss.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/losses/pixelwise_loss.py` & `mmedit-1.0.0rc7/mmedit/models/losses/pixelwise_loss.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/utils/__init__.py` & `mmedit-1.0.0rc7/mmedit/models/utils/__init__.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,17 +1,20 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 
 from .bbox_utils import extract_around_bbox, extract_bbox_patch
 from .flow_warp import flow_warp
-from .model_utils import (default_init_weights, generation_init_weights,
-                          get_module_device, get_valid_noise_size,
-                          get_valid_num_batches, make_layer, set_requires_grad)
+from .model_utils import (build_module, default_init_weights,
+                          generation_init_weights, get_module_device,
+                          get_valid_noise_size, get_valid_num_batches,
+                          make_layer, set_requires_grad, set_xformers,
+                          xformers_is_enable)
 from .sampling_utils import label_sample_fn, noise_sample_fn
 from .tensor_utils import get_unknown_tensor, normalize_vecs
 
 __all__ = [
     'default_init_weights', 'make_layer', 'flow_warp',
     'generation_init_weights', 'set_requires_grad', 'extract_bbox_patch',
     'extract_around_bbox', 'get_unknown_tensor', 'noise_sample_fn',
     'label_sample_fn', 'get_valid_num_batches', 'get_valid_noise_size',
-    'get_module_device', 'normalize_vecs'
+    'get_module_device', 'normalize_vecs', 'build_module', 'set_xformers',
+    'xformers_is_enable'
 ]
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/utils/bbox_utils.py` & `mmedit-1.0.0rc7/mmedit/models/utils/bbox_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/utils/diffusion_utils.py` & `mmedit-1.0.0rc7/mmedit/models/utils/diffusion_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/utils/flow_warp.py` & `mmedit-1.0.0rc7/mmedit/models/utils/flow_warp.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/utils/model_utils.py` & `mmedit-1.0.0rc7/mmedit/models/utils/model_utils.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,16 +1,17 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 import logging
-from typing import Dict, List, Optional, Union
+from typing import Any, Dict, List, Optional, Union
 
 import torch
 import torch.nn as nn
 from mmengine import print_log
 from mmengine.model.weight_init import (constant_init, kaiming_init,
                                         normal_init, xavier_init)
+from mmengine.registry import Registry
 from mmengine.utils.dl_utils.parrots_wrapper import _BatchNorm
 from torch import Tensor
 from torch.nn import init
 
 from mmedit.structures import EditDataSample
 from mmedit.utils.typing import ForwardInputs
 
@@ -228,7 +229,73 @@
     elif num_batches_inputs and num_batches_samples:
         assert num_batches_inputs == num_batches_samples, (
             '\'num_batches\' inferred from \'inputs\' and \'data_samples\' '
             f'are different, ({num_batches_inputs} vs. {num_batches_samples}).'
             ' Please check your input carefully.')
 
     return num_batches_inputs or num_batches_samples
+
+
+def build_module(module: Union[dict, nn.Module], builder: Registry, *args,
+                 **kwargs) -> Any:
+    """Build module from config or return the module itself.
+
+    Args:
+        module (Union[dict, nn.Module]): The module to build.
+        builder (Registry): The registry to build module.
+        *args, **kwargs: Arguments passed to build function.
+
+    Returns:
+        Any: The built module.
+    """
+    if isinstance(module, dict):
+        return builder.build(module, *args, **kwargs)
+    elif isinstance(module, nn.Module):
+        return module
+    else:
+        raise TypeError(
+            f'Only support dict and nn.Module, but got {type(module)}.')
+
+
+def xformers_is_enable(verbose: bool = False) -> bool:
+    """Check whether xformers is installed.
+    Args:
+        verbose (bool): Whether to print the log.
+
+    Returns:
+        bool: Whether xformers is installed.
+    """
+    from mmedit.utils import try_import
+    xformers = try_import('xformers')
+    if xformers is None and verbose:
+        print_log('Do not support Xformers.', 'current')
+    return xformers is not None
+
+
+def set_xformers(module: nn.Module, prefix: str = '') -> nn.Module:
+    """Set xformers' efficient Attention for attention modules.
+
+    Args:
+        module (nn.Module): The module to set xformers.
+        prefix (str): The prefix of the module name.
+
+    Returns:
+        nn.Module: The module with xformers' efficient Attention.
+    """
+
+    if not xformers_is_enable:
+        print_log('Do not support Xformers. Please install Xformers first. '
+                  'The program will run without Xformers.')
+        return
+
+    for n, m in module.named_children():
+        if hasattr(m, 'set_use_memory_efficient_attention_xformers'):
+            # set xformers for Diffusers' Cross Attention
+            m.set_use_memory_efficient_attention_xformers(True)
+            module_name = f'{prefix}.{n}' if prefix else n
+            print_log(
+                'Enable Xformers for HuggingFace Diffusers\' '
+                f'module \'{module_name}\'.', 'current')
+        else:
+            set_xformers(m, prefix=n)
+
+    return module
```

### Comparing `mmedit-1.0.0rc6/mmedit/models/utils/sampling_utils.py` & `mmedit-1.0.0rc7/mmedit/models/utils/sampling_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/models/utils/tensor_utils.py` & `mmedit-1.0.0rc7/mmedit/models/utils/tensor_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/registry.py` & `mmedit-1.0.0rc7/mmedit/registry.py`

 * *Files 1% similar despite different names*

```diff
@@ -151,15 +151,15 @@
     'task util',
     parent=MMENGINE_TASK_UTILS,
     locations=['mmedit.models'],
 )
 # modules for diffusion models that support adding noise and denoising
 DIFFUSION_SCHEDULERS = Registry(
     'diffusion scheduler',
-    locations=['mmedit.models'],
+    locations=['mmedit.models.diffusion_schedulers'],
 )
 
 #######################################################################
 #                          mmedit.evaluation                           #
 #######################################################################
 
 # Metrics to evaluate the model prediction results.
```

### Comparing `mmedit-1.0.0rc6/mmedit/structures/edit_data_sample.py` & `mmedit-1.0.0rc7/mmedit/structures/edit_data_sample.py`

 * *Files 2% similar despite different names*

```diff
@@ -24,15 +24,14 @@
         value (torch.Tensor | numpy.ndarray | Sequence | int): Label value.
         num_classes (int, optional): The number of classes. If not None, set
             it to the metainfo. Defaults to None.
 
     Returns:
         :obj:`mmengine.LabelData`: The foramtted label data.
     """
-
     # Handle single number
     if isinstance(value, (torch.Tensor, np.ndarray)) and value.ndim == 0:
         value = int(value.item())
 
     if isinstance(value, np.ndarray):
         value = torch.from_numpy(value)
     elif isinstance(value, Sequence) and not mmengine.is_str(value):
@@ -136,14 +135,15 @@
         'img_channel_order': 'img_channel_order',
         'gt_channel_order': 'gt_channel_order',
         'gt_color_type': 'gt_color_type',
         'img_color_type': 'img_color_type',
         'sample_idx': 'sample_idx',
         'num_input_frames': 'num_input_frames',
         'num_output_frames': 'num_output_frames',
+        'mask_bbox': 'mask_bbox',
         # for LIIF
         'coord': 'coord',
         'cell': 'cell',
     }
 
     # source_key_in_results: target_key_in_datafield
     DATA_KEYS = {
@@ -161,15 +161,17 @@
         'ref': 'ref_img',
         'ref_lq': 'ref_lq',
         'mask': 'mask',
         'trimap': 'trimap',
         'gray': 'gray',
         'cropped_img': 'cropped_img',
         'pred_img': 'pred_img',
-        'ori_trimap': 'ori_trimap'
+        'ori_trimap': 'ori_trimap',
+        # For text to images
+        'prompt': 'prompt'
     }
 
     def set_predefined_data(self, data: dict) -> None:
         """set or change pre-defined key-value pairs in ``data_field`` by
         parameter ``data``.
 
         Args:
@@ -198,14 +200,16 @@
                 model predictions.
         """
         assert isinstance(data,
                           dict), f'data should be a `dict` but got {data}'
         for k, v in data.items():
             if k == 'gt_label':
                 self.set_gt_label(v)
+            elif k == 'prompt':
+                self.set_field(v, k, dtype=(str, list))
             else:
                 self.set_field(all_to_tensor(v), k, dtype=torch.Tensor)
 
     def set_gt_label(
         self, value: Union[np.ndarray, torch.Tensor, Sequence[Number], Number]
     ) -> 'EditDataSample':
         """Set label of ``gt_label``."""
```

### Comparing `mmedit-1.0.0rc6/mmedit/utils/__init__.py` & `mmedit-1.0.0rc7/mmedit/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/utils/cli.py` & `mmedit-1.0.0rc7/mmedit/utils/cli.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/utils/img_utils.py` & `mmedit-1.0.0rc7/mmedit/utils/img_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/utils/io_utils.py` & `mmedit-1.0.0rc7/mmedit/utils/io_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/utils/logger.py` & `mmedit-1.0.0rc7/mmedit/utils/logger.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/utils/sampler.py` & `mmedit-1.0.0rc7/mmedit/utils/sampler.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # Copyright (c) OpenMMLab. All rights reserved.
 from copy import deepcopy
 from typing import Optional
 
 from mmengine.dataset import pseudo_collate
 from mmengine.runner import Runner
-from torch.utils.data.dataloader import DataLoader
+from torch.utils.data import ConcatDataset, DataLoader
 
 
 def _check_keys(sample_kwargs: dict, key: str) -> None:
     """Check whether target `key` is in the `sample_kwargs`."""
     assert key in sample_kwargs, (
         f'\'{key}\' must be set in \'sample_kwargs\'. But only find '
         f'following keys: \'{list(sample_kwargs.keys())}\'.')
@@ -79,15 +79,15 @@
         self.idx = 0
 
     def __iter__(self):
         self.idx = 0
         return self
 
     def __next__(self):
-        if self.idx > self.max_times:
+        if self.idx >= self.max_times:
             raise StopIteration
         self.idx += 1
 
         noise = self.module.noise_fn(num_batches=self.num_batches)
         sample_kwargs = deepcopy(self.sample_kwargs)
         sample_kwargs['noise'] = noise
         # return sample_kwargs
@@ -112,41 +112,48 @@
         self._iterator = iter(self._dataloader)
 
     def __iter__(self):
         self.idx = 0
         return self
 
     def __next__(self):
-        if self.idx > self.max_times:
+        if self.idx >= self.max_times:
             self._iterator = iter(self._dataloader)
             raise StopIteration
         self.idx += 1
         return next(self._iterator)
 
 
 class ValDataSampler:
-    """Sampler loop the train_dataloader."""
+    """Sampler loop the val_dataloader."""
 
     def __init__(self, sample_kwargs: dict, runner: Runner) -> None:
         _check_keys(sample_kwargs, 'max_times')
 
         self.sample_kwargs = deepcopy(sample_kwargs)
         self.max_times = self.sample_kwargs.pop('max_times')
 
         # build a new vanilla dataloader, because we should not reset the one
         # used in the training process.
-        dataset = runner.val_dataloader.dataset
-        batch_size = runner.val_dataloader.batch_size
+        if hasattr(runner.val_loop, 'dataloader'):
+            dataset = runner.val_loop.dataloader.dataset
+            batch_size = runner.val_loop.dataloader.batch_size
+        else:
+            # EditValLoop use `dataloaders` instead `dataloader`
+            loaders = runner.val_loop.dataloaders
+            dataset = ConcatDataset([loader.dataset for loader in loaders])
+            batch_size = loaders[0].batch_size
+
         self._dataloader = DataLoader(
             dataset, batch_size=batch_size, collate_fn=pseudo_collate)
         self._iterator = iter(self._dataloader)
 
     def __iter__(self):
         self.idx = 0
         return self
 
     def __next__(self):
-        if self.idx > self.max_times:
+        if self.idx >= self.max_times:
             self._iterator = iter(self._dataloader)
             raise StopIteration
         self.idx += 1
         return next(self._iterator)
```

### Comparing `mmedit-1.0.0rc6/mmedit/utils/setup_env.py` & `mmedit-1.0.0rc7/mmedit/utils/setup_env.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/utils/trans_utils.py` & `mmedit-1.0.0rc7/mmedit/utils/trans_utils.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/visualization/concat_visualizer.py` & `mmedit-1.0.0rc7/mmedit/visualization/concat_visualizer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/visualization/gen_visualizer.py` & `mmedit-1.0.0rc7/mmedit/visualization/gen_visualizer.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit/visualization/vis_backend.py` & `mmedit-1.0.0rc7/mmedit/visualization/vis_backend.py`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/mmedit.egg-info/PKG-INFO` & `mmedit-1.0.0rc7/mmedit.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mmedit
-Version: 1.0.0rc6
+Version: 1.0.0rc7
 Summary: OpenMMLab Image and Video Editing Toolbox and Benchmark
 Home-page: https://github.com/open-mmlab/mmediting
 Maintainer: MMEditing Contributors
 Maintainer-email: openmmlab@gmail.com
 License: Apache License 2.0
 Description: <div id="top" align="center">
           <img src="docs/en/_static/image/mmediting-logo.png" width="500px"/>
@@ -23,25 +23,25 @@
                 <i><font size="4">TRY IT OUT</font></i>
               </a>
             </sup>
           </div>
           <div>&nbsp;</div>
         
         [![PyPI](https://badge.fury.io/py/mmedit.svg)](https://pypi.org/project/mmedit/)
-        [![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmediting.readthedocs.io/en/1.x/)
+        [![docs](https://img.shields.io/badge/docs-latest-blue)](https://mmediting.readthedocs.io/en/latest/)
         [![badge](https://github.com/open-mmlab/mmediting/workflows/build/badge.svg)](https://github.com/open-mmlab/mmediting/actions)
         [![codecov](https://codecov.io/gh/open-mmlab/mmediting/branch/master/graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmediting)
-        [![license](https://img.shields.io/github/license/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/blob/1.x/LICENSE)
+        [![license](https://img.shields.io/github/license/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/blob/main/LICENSE)
         [![open issues](https://isitmaintained.com/badge/open/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/issues)
         [![issue resolution](https://isitmaintained.com/badge/resolution/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/mmediting/issues)
         
-        [📘Documentation](https://mmediting.readthedocs.io/en/1.x/) |
-        [🛠️Installation](https://mmediting.readthedocs.io/en/1.x/get_started/install.html) |
-        [📊Model Zoo](https://mmediting.readthedocs.io/en/1.x/model_zoo/overview.html) |
-        [🆕Update News](https://mmediting.readthedocs.io/en/1.x/changelog.html) |
+        [📘Documentation](https://mmediting.readthedocs.io/en/latest/) |
+        [🛠️Installation](https://mmediting.readthedocs.io/en/latest/get_started/install.html) |
+        [📊Model Zoo](https://mmediting.readthedocs.io/en/latest/model_zoo/overview.html) |
+        [🆕Update News](https://mmediting.readthedocs.io/en/latest/changelog.html) |
         [🚀Ongoing Projects](https://github.com/open-mmlab/mmediting/projects) |
         [🤔Reporting Issues](https://github.com/open-mmlab/mmediting/issues)
         
         English | [简体中文](README_zh-CN.md)
         
         </div>
         
@@ -57,18 +57,19 @@
           <img src="https://user-images.githubusercontent.com/25839884/218346358-56cc8e2f-a2b8-487f-9088-32480cceabcf.png" width="3%" alt="" />
           <a href="https://www.youtube.com/openmmlab" style="text-decoration:none;">
             <img src="https://user-images.githubusercontent.com/25839884/218346691-ceb2116a-465a-40af-8424-9f30d2348ca9.png" width="3%" alt="" /></a>
         </div>
         
         ## 🚀 What's New <a><img width="35" height="20" src="https://user-images.githubusercontent.com/12782558/212848161-5e783dd6-11e8-4fe0-bbba-39ffb77730be.png"></a>
         
-        ### New release [**MMEditing v1.0.0rc6**](https://github.com/open-mmlab/mmediting/releases/tag/v1.0.0rc6) \[02/03/2023\]:
+        ### New release [**MMEditing v1.0.0rc7**](https://github.com/open-mmlab/mmediting/releases/tag/v1.0.0rc7) \[07/04/2023\]:
         
-        - Support Gradio gui of Inpainting inference.
-        - Support Colorization, Translationin and all GAN models inferencer.
+        - Support DiffuserWrapper
+        - Support ControlNet (training and inference).
+        - Support PyTorch 2.0 (successfully compile 33+ models on 'inductor' backend).
         
         **MMEditing** has supported all the tasks, models, metrics, and losses in [MMGeneration](https://github.com/open-mmlab/mmgeneration) and unifies interfaces of all components based on [MMEngine](https://github.com/open-mmlab/mmengine) 😍.
         
         Please refer to [changelog.md](docs/en/changelog.md) for details and release history.
         
         Please refer to [migration documents](docs/en/migration/overview.md) to migrate from [old version](https://github.com/open-mmlab/mmediting/tree/master) MMEditing 0.x to our brand new 1.x version.
         
@@ -89,29 +90,29 @@
         
         MMEditing is an open-source image and video editing&generating toolbox based on PyTorch. It is a part of the [OpenMMLab](https://openmmlab.com/) project.
         
         Currently, MMEditing support multiple image and video generation/editing tasks.
         
         https://user-images.githubusercontent.com/12782558/217152698-49169038-9872-4200-80f7-1d5f7613afd7.mp4
         
-        The best practice on our main 1.x branch works with **Python 3.8+** and **PyTorch 1.9+**.
+        The best practice on our main branch works with **Python 3.8+** and **PyTorch 1.9+**.
         
         ### ✨ Major features
         
         - **State of the Art**
         
           MMEditing provides state-of-the-art generative models to process, edit and synthesize images and videos.
         
         - **Powerful and Popular Applications**
         
           MMEditing supports popular and contemporary image restoration, text-to-image, 3D-aware generation, inpainting, matting, super-resolution and generation applications. Specifically, MMEditing supports GAN interpolation, GAN projection, GAN manipulations and many other popular GAN’s applications. It’s time to play with your GANs!
         
         - **New Modular Design for Flexible Combination**
         
-          We decompose the editing framework into different modules and one can easily construct a customized editor framework by combining different modules. Specifically, a new design for complex loss modules is proposed for customizing the links between modules, which can achieve flexible combinations among different modules.(Tutorial for [losses](https://mmediting.readthedocs.io/en/dev-1.x/howto/losses.html))
+          We decompose the editing framework into different modules and one can easily construct a customized editor framework by combining different modules. Specifically, a new design for complex loss modules is proposed for customizing the links between modules, which can achieve flexible combinations among different modules.(Tutorial for [losses](https://mmediting.readthedocs.io/en/latest/howto/losses.html))
         
         - **Efficient Distributed Training**
         
           With the support of [MMSeparateDistributedDataParallel](https://github.com/open-mmlab/mmengine/blob/main/mmengine/model/wrappers/seperate_distributed.py), distributed training for dynamic architectures can be easily implemented.
         
         <p align="right"><a href="#top">🔝Back to top</a></p>
         
@@ -139,22 +140,22 @@
         
         **Step 2.**
         Install MMCV with [MIM](https://github.com/open-mmlab/mim).
         
         ```shell
         pip3 install openmim
         # wait for more pre-compiled pkgs to release
-        mim install 'mmcv>=2.0.0rc1'
+        mim install 'mmcv>=2.0.0'
         ```
         
         **Step 3.**
         Install MMEditing from source.
         
         ```shell
-        git clone -b 1.x https://github.com/open-mmlab/mmediting.git
+        git clone https://github.com/open-mmlab/mmediting.git
         cd mmediting
         pip3 install -e .
         ```
         
         Please refer to [installation](docs/en/get_started/install.md) for more detailed instruction.
         
         **Getting Started**
@@ -309,14 +310,15 @@
                   <li><a href="configs/dim/README.md">DIM (CVPR'2017)</a></li>
                   <li><a href="configs/indexnet/README.md">IndexNet (ICCV'2019)</a></li>
                   <li><a href="configs/mask2former">GCA (AAAI'2020)</a></li>
                 </ul>
               </td>
               <td>
                 <ul>
+                  <li><a href="configs/controlnet/README.md">ControlNet (2023)</a></li>
                   <li><a href="projects/glide/configs/README.md">GLIDE (NeurIPS'2021)</a></li>
                   <li><a href="configs/disco_diffusion/README.md">Disco-Diffusion (2022)</a></li>
                   <li><a href="configs/stable_diffusion/README.md">Stable-Diffusion (2022)</a></li>
                 </ul>
               </td>
               <td>
                 <ul>
@@ -325,26 +327,26 @@
               </td>
             </tr>
         </td>
             </tr>
           </tbody>
         </table>
         
-        Please refer to [model_zoo](https://mmediting.readthedocs.io/en/1.x/model_zoo/overview.html) for more details.
+        Please refer to [model_zoo](https://mmediting.readthedocs.io/en/latest/model_zoo/overview.html) for more details.
         
         <p align="right"><a href="#top">🔝Back to top</a></p>
         
         ## 🤝 Acknowledgement
         
         MMEditing is an open source project that is contributed by researchers and engineers from various colleges and companies. We wish that the toolbox and benchmark could serve the growing research community by providing a flexible toolkit to reimplement existing methods and develop their own new methods.
         
         We appreciate all the contributors who implement their methods or add new features, as well as users who give valuable feedbacks. Thank you all!
         
         <a href="https://github.com/open-mmlab/mmediting/graphs/contributors">
-          <img src="https://contrib.rocks/image?repo=liuwenran/mmediting" />
+          <img src="https://contrib.rocks/image?repo=open-mmlab/mmediting" />
         </a>
         
         <p align="right"><a href="#top">🔝Back to top</a></p>
         
         ## 🖊️ Citation
         
         If MMEditing is helpful to your research, please cite it as below.
@@ -366,32 +368,32 @@
         Please refer to [LICENSES](LICENSE) for the careful check, if you are using our code for commercial matters.
         
         <p align="right"><a href="#top">🔝Back to top</a></p>
         
         ## 🏗️ ️OpenMMLab Family
         
         - [MMEngine](https://github.com/open-mmlab/mmengine): OpenMMLab foundational library for training deep learning models.
-        - [MMCV](https://github.com/open-mmlab/mmcv/tree/2.x): OpenMMLab foundational library for computer vision.
+        - [MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for computer vision.
         - [MIM](https://github.com/open-mmlab/mim): MIM installs OpenMMLab packages.
-        - [MMClassification](https://github.com/open-mmlab/mmclassification/tree/1.x): OpenMMLab image classification toolbox and benchmark.
-        - [MMDetection](https://github.com/open-mmlab/mmdetection/tree/3.x): OpenMMLab detection toolbox and benchmark.
-        - [MMDetection3D](https://github.com/open-mmlab/mmdetection3d/tree/1.x): OpenMMLab's next-generation platform for general 3D object detection.
-        - [MMRotate](https://github.com/open-mmlab/mmrotate/tree/1.x): OpenMMLab rotated object detection toolbox and benchmark.
-        - [MMSegmentation](https://github.com/open-mmlab/mmsegmentation/tree/1.x): OpenMMLab semantic segmentation toolbox and benchmark.
-        - [MMOCR](https://github.com/open-mmlab/mmocr/tree/1.x): OpenMMLab text detection, recognition, and understanding toolbox.
-        - [MMPose](https://github.com/open-mmlab/mmpose/tree/1.x): OpenMMLab pose estimation toolbox and benchmark.
-        - [MMHuman3D](https://github.com/open-mmlab/mmhuman3d/tree/1.x): OpenMMLab 3D human parametric model toolbox and benchmark.
-        - [MMSelfSup](https://github.com/open-mmlab/mmselfsup/tree/1.x): OpenMMLab self-supervised learning toolbox and benchmark.
-        - [MMRazor](https://github.com/open-mmlab/mmrazor/tree/1.x): OpenMMLab model compression toolbox and benchmark.
-        - [MMFewShot](https://github.com/open-mmlab/mmfewshot/tree/1.x): OpenMMLab fewshot learning toolbox and benchmark.
-        - [MMAction2](https://github.com/open-mmlab/mmaction2/tree/1.x): OpenMMLab's next-generation action understanding toolbox and benchmark.
-        - [MMTracking](https://github.com/open-mmlab/mmtracking/tree/1.x): OpenMMLab video perception toolbox and benchmark.
-        - [MMFlow](https://github.com/open-mmlab/mmflow/tree/1.x): OpenMMLab optical flow toolbox and benchmark.
-        - [MMEditing](https://github.com/open-mmlab/mmediting/tree/1.x): OpenMMLab image and video editing toolbox.
-        - [MMGeneration](https://github.com/open-mmlab/mmgeneration/tree/1.x): OpenMMLab image and video generative models toolbox.
+        - [MMClassification](https://github.com/open-mmlab/mmclassification): OpenMMLab image classification toolbox and benchmark.
+        - [MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection toolbox and benchmark.
+        - [MMDetection3D](https://github.com/open-mmlab/mmdetection3d): OpenMMLab's next-generation platform for general 3D object detection.
+        - [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab rotated object detection toolbox and benchmark.
+        - [MMSegmentation](https://github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox and benchmark.
+        - [MMOCR](https://github.com/open-mmlab/mmocr): OpenMMLab text detection, recognition, and understanding toolbox.
+        - [MMPose](https://github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
+        - [MMHuman3D](https://github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human parametric model toolbox and benchmark.
+        - [MMSelfSup](https://github.com/open-mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox and benchmark.
+        - [MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab model compression toolbox and benchmark.
+        - [MMFewShot](https://github.com/open-mmlab/mmfewshot): OpenMMLab fewshot learning toolbox and benchmark.
+        - [MMAction2](https://github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action understanding toolbox and benchmark.
+        - [MMTracking](https://github.com/open-mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark.
+        - [MMFlow](https://github.com/open-mmlab/mmflow): OpenMMLab optical flow toolbox and benchmark.
+        - [MMEditing](https://github.com/open-mmlab/mmediting): OpenMMLab image and video editing toolbox.
+        - [MMGeneration](https://github.com/open-mmlab/mmgeneration): OpenMMLab image and video generative models toolbox.
         - [MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab model deployment framework.
         
         <p align="right"><a href="#top">🔝Back to top</a></p>
         
 Keywords: computer vision,super resolution,video interpolation,inpainting,matting,SISR,RefSR,VSR,GAN,VFI
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
```

#### html2text {}

```diff
@@ -1,72 +1,73 @@
-Metadata-Version: 2.1 Name: mmedit Version: 1.0.0rc6 Summary: OpenMMLab Image
+Metadata-Version: 2.1 Name: mmedit Version: 1.0.0rc7 Summary: OpenMMLab Image
 and Video Editing Toolbox and Benchmark Home-page: https://github.com/open-
 mmlab/mmediting Maintainer: MMEditing Contributors Maintainer-email:
 openmmlab@gmail.com License: Apache License 2.0 Description:
                   [docs/en/_static/image/mmediting-logo.png]
                                         
            OpenMMLab website HOT      OpenMMLab platform TRY_IT_OUT
                                         
 [![PyPI](https://badge.fury.io/py/mmedit.svg)](https://pypi.org/project/mmedit/
       ) [![docs](https://img.shields.io/badge/docs-latest-blue)](https://
-  mmediting.readthedocs.io/en/1.x/) [![badge](https://github.com/open-mmlab/
+ mmediting.readthedocs.io/en/latest/) [![badge](https://github.com/open-mmlab/
 mmediting/workflows/build/badge.svg)](https://github.com/open-mmlab/mmediting/
 actions) [![codecov](https://codecov.io/gh/open-mmlab/mmediting/branch/master/
    graph/badge.svg)](https://codecov.io/gh/open-mmlab/mmediting) [![license]
   (https://img.shields.io/github/license/open-mmlab/mmediting.svg)](https://
-  github.com/open-mmlab/mmediting/blob/1.x/LICENSE) [![open issues](https://
+  github.com/open-mmlab/mmediting/blob/main/LICENSE) [![open issues](https://
  isitmaintained.com/badge/open/open-mmlab/mmediting.svg)](https://github.com/
  open-mmlab/mmediting/issues) [![issue resolution](https://isitmaintained.com/
   badge/resolution/open-mmlab/mmediting.svg)](https://github.com/open-mmlab/
-mmediting/issues) [ðDocumentation](https://mmediting.readthedocs.io/en/1.x/
-) | [ð ï¸Installation](https://mmediting.readthedocs.io/en/1.x/get_started/
-   install.html) | [ðModel Zoo](https://mmediting.readthedocs.io/en/1.x/
-model_zoo/overview.html) | [ðUpdate News](https://mmediting.readthedocs.io/
-en/1.x/changelog.html) | [ðOngoing Projects](https://github.com/open-mmlab/
-  mmediting/projects) | [ð¤Reporting Issues](https://github.com/open-mmlab/
-          mmediting/issues) English | [ç®ä½ä¸­æ](README_zh-CN.md)
+  mmediting/issues) [ðDocumentation](https://mmediting.readthedocs.io/en/
+ latest/) | [ð ï¸Installation](https://mmediting.readthedocs.io/en/latest/
+ get_started/install.html) | [ðModel Zoo](https://mmediting.readthedocs.io/
+        en/latest/model_zoo/overview.html) | [ðUpdate News](https://
+  mmediting.readthedocs.io/en/latest/changelog.html) | [ðOngoing Projects]
+  (https://github.com/open-mmlab/mmediting/projects) | [ð¤Reporting Issues]
+   (https://github.com/open-mmlab/mmediting/issues) English | [ç®ä½ä¸­æ]
+                               (README_zh-CN.md)
 
 ## ð What's New [https://user-images.githubusercontent.com/12782558/
 212848161-5e783dd6-11e8-4fe0-bbba-39ffb77730be.png] ### New release
-[**MMEditing v1.0.0rc6**](https://github.com/open-mmlab/mmediting/releases/tag/
-v1.0.0rc6) \[02/03/2023\]: - Support Gradio gui of Inpainting inference. -
-Support Colorization, Translationin and all GAN models inferencer.
-**MMEditing** has supported all the tasks, models, metrics, and losses in
-[MMGeneration](https://github.com/open-mmlab/mmgeneration) and unifies
-interfaces of all components based on [MMEngine](https://github.com/open-mmlab/
-mmengine) ð. Please refer to [changelog.md](docs/en/changelog.md) for
-details and release history. Please refer to [migration documents](docs/en/
-migration/overview.md) to migrate from [old version](https://github.com/open-
-mmlab/mmediting/tree/master) MMEditing 0.x to our brand new 1.x version. ##
-ð Table of Contents - [ð Introduction](#ð-introduction) - [ð
-Contributing](#ð-contributing) - [ð ï¸ Installation](#ð ï¸-
-installation) - [ð Model Zoo](#ð-model-zoo) - [ð¤ Acknowledgement]
-(#ð¤-acknowledgement) - [ðï¸ Citation](#ðï¸-citation) - [ð«
-License](#ð«-license) - [ðï¸ ï¸OpenMMLab Family](#ðï¸-ï¸openmmlab-
-family)
+[**MMEditing v1.0.0rc7**](https://github.com/open-mmlab/mmediting/releases/tag/
+v1.0.0rc7) \[07/04/2023\]: - Support DiffuserWrapper - Support ControlNet
+(training and inference). - Support PyTorch 2.0 (successfully compile 33+
+models on 'inductor' backend). **MMEditing** has supported all the tasks,
+models, metrics, and losses in [MMGeneration](https://github.com/open-mmlab/
+mmgeneration) and unifies interfaces of all components based on [MMEngine]
+(https://github.com/open-mmlab/mmengine) ð. Please refer to [changelog.md]
+(docs/en/changelog.md) for details and release history. Please refer to
+[migration documents](docs/en/migration/overview.md) to migrate from [old
+version](https://github.com/open-mmlab/mmediting/tree/master) MMEditing 0.x to
+our brand new 1.x version. ## ð Table of Contents - [ð Introduction]
+(#ð-introduction) - [ð Contributing](#ð-contributing) - [ð ï¸
+Installation](#ð ï¸-installation) - [ð Model Zoo](#ð-model-zoo) -
+[ð¤ Acknowledgement](#ð¤-acknowledgement) - [ðï¸ Citation](#ðï¸-
+citation) - [ð« License](#ð«-license) - [ðï¸ ï¸OpenMMLab Family]
+(#ðï¸-ï¸openmmlab-family)
                                                                 ðBack_to_top
 ## ð Introduction MMEditing is an open-source image and video
 editing&generating toolbox based on PyTorch. It is a part of the [OpenMMLab]
 (https://openmmlab.com/) project. Currently, MMEditing support multiple image
 and video generation/editing tasks. https://user-images.githubusercontent.com/
 12782558/217152698-49169038-9872-4200-80f7-1d5f7613afd7.mp4 The best practice
-on our main 1.x branch works with **Python 3.8+** and **PyTorch 1.9+**. ### â¨
+on our main branch works with **Python 3.8+** and **PyTorch 1.9+**. ### â¨
 Major features - **State of the Art** MMEditing provides state-of-the-art
 generative models to process, edit and synthesize images and videos. -
 **Powerful and Popular Applications** MMEditing supports popular and
 contemporary image restoration, text-to-image, 3D-aware generation, inpainting,
 matting, super-resolution and generation applications. Specifically, MMEditing
 supports GAN interpolation, GAN projection, GAN manipulations and many other
 popular GANâs applications. Itâs time to play with your GANs! - **New
 Modular Design for Flexible Combination** We decompose the editing framework
 into different modules and one can easily construct a customized editor
 framework by combining different modules. Specifically, a new design for
 complex loss modules is proposed for customizing the links between modules,
 which can achieve flexible combinations among different modules.(Tutorial for
-[losses](https://mmediting.readthedocs.io/en/dev-1.x/howto/losses.html)) -
+[losses](https://mmediting.readthedocs.io/en/latest/howto/losses.html)) -
 **Efficient Distributed Training** With the support of
 [MMSeparateDistributedDataParallel](https://github.com/open-mmlab/mmengine/
 blob/main/mmengine/model/wrappers/seperate_distributed.py), distributed
 training for dynamic architectures can be easily implemented.
                                                                 ðBack_to_top
 ## ð Contributing More and more community contributors are joining us to
 make our repo better. Some recent projects are contributed by the community
@@ -82,17 +83,17 @@
                                                                 ðBack_to_top
 ## ð ï¸ Installation MMEditing depends on [PyTorch](https://pytorch.org/),
 [MMEngine](https://github.com/open-mmlab/mmengine) and [MMCV](https://
 github.com/open-mmlab/mmcv). Below are quick steps for installation. **Step
 1.** Install PyTorch following [official instructions](https://pytorch.org/get-
 started/locally/). **Step 2.** Install MMCV with [MIM](https://github.com/open-
 mmlab/mim). ```shell pip3 install openmim # wait for more pre-compiled pkgs to
-release mim install 'mmcv>=2.0.0rc1' ``` **Step 3.** Install MMEditing from
-source. ```shell git clone -b 1.x https://github.com/open-mmlab/mmediting.git
-cd mmediting pip3 install -e . ``` Please refer to [installation](docs/en/
+release mim install 'mmcv>=2.0.0' ``` **Step 3.** Install MMEditing from
+source. ```shell git clone https://github.com/open-mmlab/mmediting.git cd
+mmediting pip3 install -e . ``` Please refer to [installation](docs/en/
 get_started/install.md) for more detailed instruction. **Getting Started**
 Please see [quick run](docs/en/get_started/quick_run.md) and [inference](docs/
 en/user_guides/inference.md) for the basic usage of MMEditing.
                                                                 ðBack_to_top
 ## ð Model Zoo
                              Supported algorithms
                                                                      Image Super-
@@ -130,74 +131,72 @@
     * IconVSR_
       (CVPR'2021)
     * BasicVSR++_
       (CVPR'2022)
     * RealBasicVSR
       (CVPR'2022)
       Inpainting            Matting           Text-to-Image    3D-aware Generation
-    * Global&Local     * DIM_               * GLIDE_               * EG3D_
-      (ToG'2017)         (CVPR'2017)          (NeurIPS'2021)         (CVPR'2022)
-    * DeepFillv1_      * IndexNet_          * Disco-Diffusion_
-      (CVPR'2018)        (ICCV'2019)          (2022)
-    * PConv_           * GCA_               * Stable-Diffusion
+    * Global&Local     * DIM_               * ControlNet_          * EG3D_
+      (ToG'2017)         (CVPR'2017)          (2023)                 (CVPR'2022)
+    * DeepFillv1_      * IndexNet_          * GLIDE_
+      (CVPR'2018)        (ICCV'2019)          (NeurIPS'2021)
+    * PConv_           * GCA_               * Disco-Diffusion_
       (ECCV'2018)        (AAAI'2020)          (2022)
-    * DeepFillv2_
-      (CVPR'2019)
+    * DeepFillv2_                           * Stable-Diffusion
+      (CVPR'2019)                             (2022)
     * AOT-GAN_
       (TVCG'2019)
-Please refer to [model_zoo](https://mmediting.readthedocs.io/en/1.x/model_zoo/
-overview.html) for more details.
+Please refer to [model_zoo](https://mmediting.readthedocs.io/en/latest/
+model_zoo/overview.html) for more details.
                                                                 ðBack_to_top
 ## ð¤ Acknowledgement MMEditing is an open source project that is contributed
 by researchers and engineers from various colleges and companies. We wish that
 the toolbox and benchmark could serve the growing research community by
 providing a flexible toolkit to reimplement existing methods and develop their
 own new methods. We appreciate all the contributors who implement their methods
 or add new features, as well as users who give valuable feedbacks. Thank you
-all! [https://contrib.rocks/image?repo=liuwenran/mmediting]
+all! [https://contrib.rocks/image?repo=open-mmlab/mmediting]
                                                                 ðBack_to_top
 ## ðï¸ Citation If MMEditing is helpful to your research, please cite it as
 below. ```bibtex @misc{mmediting2022, title = {{MMEditing}: {OpenMMLab} Image
 and Video Editing Toolbox}, author = {{MMEditing Contributors}}, howpublished =
 {\url{https://github.com/open-mmlab/mmediting}}, year = {2022} } ```
                                                                 ðBack_to_top
 ## ð« License This project is released under the [Apache 2.0 license]
 (LICENSE). Please refer to [LICENSES](LICENSE) for the careful check, if you
 are using our code for commercial matters.
                                                                 ðBack_to_top
 ## ðï¸ ï¸OpenMMLab Family - [MMEngine](https://github.com/open-mmlab/
 mmengine): OpenMMLab foundational library for training deep learning models. -
-[MMCV](https://github.com/open-mmlab/mmcv/tree/2.x): OpenMMLab foundational
-library for computer vision. - [MIM](https://github.com/open-mmlab/mim): MIM
-installs OpenMMLab packages. - [MMClassification](https://github.com/open-
-mmlab/mmclassification/tree/1.x): OpenMMLab image classification toolbox and
-benchmark. - [MMDetection](https://github.com/open-mmlab/mmdetection/tree/3.x):
-OpenMMLab detection toolbox and benchmark. - [MMDetection3D](https://
-github.com/open-mmlab/mmdetection3d/tree/1.x): OpenMMLab's next-generation
-platform for general 3D object detection. - [MMRotate](https://github.com/open-
-mmlab/mmrotate/tree/1.x): OpenMMLab rotated object detection toolbox and
-benchmark. - [MMSegmentation](https://github.com/open-mmlab/mmsegmentation/
-tree/1.x): OpenMMLab semantic segmentation toolbox and benchmark. - [MMOCR]
-(https://github.com/open-mmlab/mmocr/tree/1.x): OpenMMLab text detection,
-recognition, and understanding toolbox. - [MMPose](https://github.com/open-
-mmlab/mmpose/tree/1.x): OpenMMLab pose estimation toolbox and benchmark. -
-[MMHuman3D](https://github.com/open-mmlab/mmhuman3d/tree/1.x): OpenMMLab 3D
-human parametric model toolbox and benchmark. - [MMSelfSup](https://github.com/
-open-mmlab/mmselfsup/tree/1.x): OpenMMLab self-supervised learning toolbox and
-benchmark. - [MMRazor](https://github.com/open-mmlab/mmrazor/tree/1.x):
-OpenMMLab model compression toolbox and benchmark. - [MMFewShot](https://
-github.com/open-mmlab/mmfewshot/tree/1.x): OpenMMLab fewshot learning toolbox
-and benchmark. - [MMAction2](https://github.com/open-mmlab/mmaction2/tree/1.x):
-OpenMMLab's next-generation action understanding toolbox and benchmark. -
-[MMTracking](https://github.com/open-mmlab/mmtracking/tree/1.x): OpenMMLab
-video perception toolbox and benchmark. - [MMFlow](https://github.com/open-
-mmlab/mmflow/tree/1.x): OpenMMLab optical flow toolbox and benchmark. -
-[MMEditing](https://github.com/open-mmlab/mmediting/tree/1.x): OpenMMLab image
-and video editing toolbox. - [MMGeneration](https://github.com/open-mmlab/
-mmgeneration/tree/1.x): OpenMMLab image and video generative models toolbox. -
+[MMCV](https://github.com/open-mmlab/mmcv): OpenMMLab foundational library for
+computer vision. - [MIM](https://github.com/open-mmlab/mim): MIM installs
+OpenMMLab packages. - [MMClassification](https://github.com/open-mmlab/
+mmclassification): OpenMMLab image classification toolbox and benchmark. -
+[MMDetection](https://github.com/open-mmlab/mmdetection): OpenMMLab detection
+toolbox and benchmark. - [MMDetection3D](https://github.com/open-mmlab/
+mmdetection3d): OpenMMLab's next-generation platform for general 3D object
+detection. - [MMRotate](https://github.com/open-mmlab/mmrotate): OpenMMLab
+rotated object detection toolbox and benchmark. - [MMSegmentation](https://
+github.com/open-mmlab/mmsegmentation): OpenMMLab semantic segmentation toolbox
+and benchmark. - [MMOCR](https://github.com/open-mmlab/mmocr): OpenMMLab text
+detection, recognition, and understanding toolbox. - [MMPose](https://
+github.com/open-mmlab/mmpose): OpenMMLab pose estimation toolbox and benchmark.
+- [MMHuman3D](https://github.com/open-mmlab/mmhuman3d): OpenMMLab 3D human
+parametric model toolbox and benchmark. - [MMSelfSup](https://github.com/open-
+mmlab/mmselfsup): OpenMMLab self-supervised learning toolbox and benchmark. -
+[MMRazor](https://github.com/open-mmlab/mmrazor): OpenMMLab model compression
+toolbox and benchmark. - [MMFewShot](https://github.com/open-mmlab/mmfewshot):
+OpenMMLab fewshot learning toolbox and benchmark. - [MMAction2](https://
+github.com/open-mmlab/mmaction2): OpenMMLab's next-generation action
+understanding toolbox and benchmark. - [MMTracking](https://github.com/open-
+mmlab/mmtracking): OpenMMLab video perception toolbox and benchmark. - [MMFlow]
+(https://github.com/open-mmlab/mmflow): OpenMMLab optical flow toolbox and
+benchmark. - [MMEditing](https://github.com/open-mmlab/mmediting): OpenMMLab
+image and video editing toolbox. - [MMGeneration](https://github.com/open-
+mmlab/mmgeneration): OpenMMLab image and video generative models toolbox. -
 [MMDeploy](https://github.com/open-mmlab/mmdeploy): OpenMMLab model deployment
 framework.
                                                                 ðBack_to_top
 Keywords: computer vision,super resolution,video
 interpolation,inpainting,matting,SISR,RefSR,VSR,GAN,VFI Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta Classifier: Intended Audience ::
 Developers Classifier: Intended Audience :: Education Classifier: Intended
```

### Comparing `mmedit-1.0.0rc6/mmedit.egg-info/SOURCES.txt` & `mmedit-1.0.0rc7/mmedit.egg-info/SOURCES.txt`

 * *Files 3% similar despite different names*

```diff
@@ -88,14 +88,19 @@
 mmedit/.mim/configs/biggan/biggan-deep_cvt-hugging-face_rgb_imagenet1k-512x512.py
 mmedit/.mim/configs/biggan/biggan_2xb25-500kiters_cifar10-32x32.py
 mmedit/.mim/configs/biggan/biggan_ajbrock-sn_8xb32-1500kiters_imagenet1k-128x128.py
 mmedit/.mim/configs/biggan/biggan_cvt-BigGAN-PyTorch-rgb_imagenet1k-128x128.py
 mmedit/.mim/configs/biggan/metafile.yml
 mmedit/.mim/configs/cain/cain_g1b32_1xb5_vimeo90k-triplet.py
 mmedit/.mim/configs/cain/metafile.yml
+mmedit/.mim/configs/controlnet/controlnet-1xb1-fill50k.py
+mmedit/.mim/configs/controlnet/controlnet-canny.py
+mmedit/.mim/configs/controlnet/controlnet-pose.py
+mmedit/.mim/configs/controlnet/controlnet-seg.py
+mmedit/.mim/configs/controlnet/metafile.yml
 mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-250kiters_summer2winter.py
 mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-270kiters_horse2zebra.py
 mmedit/.mim/configs/cyclegan/cyclegan_lsgan-id0-resnet-in_1xb1-80kiters_facades.py
 mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-250kiters_summer2winter.py
 mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-270kiters_horse2zebra.py
 mmedit/.mim/configs/cyclegan/cyclegan_lsgan-resnet-in_1xb1-80kiters_facades.py
 mmedit/.mim/configs/cyclegan/metafile.yml
@@ -368,47 +373,53 @@
 mmedit/.mim/tools/dataset_converters/comp1k/check_extended_fg.py
 mmedit/.mim/tools/dataset_converters/comp1k/evaluate_comp1k.py
 mmedit/.mim/tools/dataset_converters/comp1k/extend_fg.py
 mmedit/.mim/tools/dataset_converters/comp1k/filter_comp1k_anno.py
 mmedit/.mim/tools/dataset_converters/comp1k/preprocess_comp1k_dataset.py
 mmedit/.mim/tools/dataset_converters/df2k_ost/preprocess_df2k_ost_dataset.py
 mmedit/.mim/tools/dataset_converters/div2k/preprocess_div2k_dataset.py
+mmedit/.mim/tools/dataset_converters/glean/preprocess_cat_test_dataset.py
+mmedit/.mim/tools/dataset_converters/glean/preprocess_cat_train_dataset.py
+mmedit/.mim/tools/dataset_converters/glean/preprocess_ffhq_celebahq_dataset.py
 mmedit/.mim/tools/dataset_converters/reds/crop_sub_images.py
 mmedit/.mim/tools/dataset_converters/reds/preprocess_reds_dataset.py
+mmedit/.mim/tools/dataset_converters/sidd/preprocess_sidd_test_dataset.py
+mmedit/.mim/tools/dataset_converters/vid4/preprocess_vid4_dataset.py
 mmedit/.mim/tools/dataset_converters/vimeo90k/preprocess_vimeo90k_dataset.py
 mmedit/.mim/tools/gui/component.py
 mmedit/.mim/tools/gui/gui.py
 mmedit/.mim/tools/gui/page_general.py
 mmedit/.mim/tools/gui/page_sr.py
 mmedit/.mim/tools/gui/utils.py
 mmedit/.mim/tools/model_converters/publish_model.py
 mmedit/.mim/tools/model_converters/pytorch2onnx.py
 mmedit/apis/__init__.py
 mmedit/apis/inferencers/__init__.py
 mmedit/apis/inferencers/base_mmedit_inferencer.py
 mmedit/apis/inferencers/colorization_inferencer.py
 mmedit/apis/inferencers/conditional_inferencer.py
 mmedit/apis/inferencers/eg3d_inferencer.py
+mmedit/apis/inferencers/image_super_resolution_inferencer.py
 mmedit/apis/inferencers/inference_functions.py
 mmedit/apis/inferencers/inpainting_inferencer.py
 mmedit/apis/inferencers/matting_inferencer.py
 mmedit/apis/inferencers/mmedit_inferencer.py
-mmedit/apis/inferencers/restoration_inferencer.py
 mmedit/apis/inferencers/text2image_inferencer.py
 mmedit/apis/inferencers/translation_inferencer.py
 mmedit/apis/inferencers/unconditional_inferencer.py
 mmedit/apis/inferencers/video_interpolation_inferencer.py
 mmedit/apis/inferencers/video_restoration_inferencer.py
 mmedit/datasets/__init__.py
 mmedit/datasets/basic_conditional_dataset.py
 mmedit/datasets/basic_frames_dataset.py
 mmedit/datasets/basic_image_dataset.py
 mmedit/datasets/categories.py
 mmedit/datasets/cifar10_dataset.py
 mmedit/datasets/comp1k_dataset.py
+mmedit/datasets/controlnet_dataset.py
 mmedit/datasets/data_utils.py
 mmedit/datasets/grow_scale_image_dataset.py
 mmedit/datasets/imagenet_dataset.py
 mmedit/datasets/mscoco_dataset.py
 mmedit/datasets/paired_image_dataset.py
 mmedit/datasets/singan_dataset.py
 mmedit/datasets/unpaired_image_dataset.py
@@ -479,42 +490,45 @@
 mmedit/evaluation/metrics/ssim.py
 mmedit/evaluation/metrics/swd.py
 mmedit/models/__init__.py
 mmedit/models/base_archs/__init__.py
 mmedit/models/base_archs/all_gather_layer.py
 mmedit/models/base_archs/aspp.py
 mmedit/models/base_archs/conv.py
-mmedit/models/base_archs/conv2d_gradfix.py
 mmedit/models/base_archs/downsample.py
 mmedit/models/base_archs/ensemble.py
 mmedit/models/base_archs/gated_conv_module.py
 mmedit/models/base_archs/img_normalize.py
 mmedit/models/base_archs/linear_module.py
 mmedit/models/base_archs/multi_layer_disc.py
 mmedit/models/base_archs/patch_disc.py
 mmedit/models/base_archs/resnet.py
 mmedit/models/base_archs/separable_conv_module.py
 mmedit/models/base_archs/simple_encoder_decoder.py
 mmedit/models/base_archs/smpatch_disc.py
 mmedit/models/base_archs/sr_backbone.py
 mmedit/models/base_archs/upsample.py
 mmedit/models/base_archs/vgg.py
+mmedit/models/base_archs/wrapper.py
 mmedit/models/base_models/__init__.py
 mmedit/models/base_models/average_model.py
 mmedit/models/base_models/base_conditional_gan.py
 mmedit/models/base_models/base_edit_model.py
 mmedit/models/base_models/base_gan.py
 mmedit/models/base_models/base_mattor.py
 mmedit/models/base_models/base_translation_model.py
 mmedit/models/base_models/basic_interpolator.py
 mmedit/models/base_models/one_stage.py
 mmedit/models/base_models/two_stage.py
 mmedit/models/data_preprocessors/__init__.py
 mmedit/models/data_preprocessors/edit_data_preprocessor.py
 mmedit/models/data_preprocessors/mattor_preprocessor.py
+mmedit/models/diffusion_schedulers/__init__.py
+mmedit/models/diffusion_schedulers/ddim_scheduler.py
+mmedit/models/diffusion_schedulers/ddpm_scheduler.py
 mmedit/models/editors/__init__.py
 mmedit/models/editors/aotgan/__init__.py
 mmedit/models/editors/aotgan/aot_decoder.py
 mmedit/models/editors/aotgan/aot_encoder.py
 mmedit/models/editors/aotgan/aot_encoder_decoder.py
 mmedit/models/editors/aotgan/aot_inpaintor.py
 mmedit/models/editors/aotgan/aot_neck.py
@@ -534,27 +548,27 @@
 mmedit/models/editors/biggan/biggan_discriminator.py
 mmedit/models/editors/biggan/biggan_generator.py
 mmedit/models/editors/biggan/biggan_modules.py
 mmedit/models/editors/biggan/biggan_snmodule.py
 mmedit/models/editors/cain/__init__.py
 mmedit/models/editors/cain/cain.py
 mmedit/models/editors/cain/cain_net.py
+mmedit/models/editors/controlnet/__init__.py
+mmedit/models/editors/controlnet/controlnet.py
+mmedit/models/editors/controlnet/controlnet_utils.py
 mmedit/models/editors/cyclegan/__init__.py
 mmedit/models/editors/cyclegan/cyclegan.py
 mmedit/models/editors/cyclegan/cyclegan_generator.py
 mmedit/models/editors/cyclegan/cyclegan_modules.py
 mmedit/models/editors/dcgan/__init__.py
 mmedit/models/editors/dcgan/dcgan.py
 mmedit/models/editors/dcgan/dcgan_discriminator.py
 mmedit/models/editors/dcgan/dcgan_generator.py
-mmedit/models/editors/ddim/__init__.py
-mmedit/models/editors/ddim/ddim_scheduler.py
 mmedit/models/editors/ddpm/__init__.py
 mmedit/models/editors/ddpm/attention.py
-mmedit/models/editors/ddpm/ddpm_scheduler.py
 mmedit/models/editors/ddpm/denoising_unet.py
 mmedit/models/editors/ddpm/embeddings.py
 mmedit/models/editors/ddpm/res_blocks.py
 mmedit/models/editors/ddpm/unet_blocks.py
 mmedit/models/editors/deepfillv1/__init__.py
 mmedit/models/editors/deepfillv1/contextual_attention.py
 mmedit/models/editors/deepfillv1/contextual_attention_neck.py
@@ -720,20 +734,14 @@
 mmedit/models/editors/stylegan2/ada/misc.py
 mmedit/models/editors/stylegan2/ada/upfirdn2d.py
 mmedit/models/editors/stylegan3/__init__.py
 mmedit/models/editors/stylegan3/stylegan3.py
 mmedit/models/editors/stylegan3/stylegan3_generator.py
 mmedit/models/editors/stylegan3/stylegan3_modules.py
 mmedit/models/editors/stylegan3/stylegan3_utils.py
-mmedit/models/editors/stylegan3/stylegan3_ops/__init__.py
-mmedit/models/editors/stylegan3/stylegan3_ops/custom_ops.py
-mmedit/models/editors/stylegan3/stylegan3_ops/ops/__init__.py
-mmedit/models/editors/stylegan3/stylegan3_ops/ops/bias_act.py
-mmedit/models/editors/stylegan3/stylegan3_ops/ops/filtered_lrelu.py
-mmedit/models/editors/stylegan3/stylegan3_ops/ops/upfirdn2d.py
 mmedit/models/editors/swinir/__init__.py
 mmedit/models/editors/swinir/swinir_modules.py
 mmedit/models/editors/swinir/swinir_net.py
 mmedit/models/editors/swinir/swinir_rstb.py
 mmedit/models/editors/swinir/swinir_utils.py
 mmedit/models/editors/tdan/__init__.py
 mmedit/models/editors/tdan/tdan.py
```

### Comparing `mmedit-1.0.0rc6/mmedit.egg-info/requires.txt` & `mmedit-1.0.0rc7/mmedit.egg-info/requires.txt`

 * *Files 19% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 av
+diffusers>=0.12.0
 einops
 face-alignment
 facexlib
 lmdb
 lpips
 mmcv>=2.0.0rc1
 mmengine
@@ -13,14 +14,15 @@
 tensorboard
 
 [:python_version < "3.7"]
 av==8.0.3
 
 [all]
 av
+diffusers>=0.12.0
 einops
 face-alignment
 facexlib
 lmdb
 lpips
 mmcv>=2.0.0rc1
 mmengine
@@ -29,32 +31,32 @@
 Pillow
 resize_right
 tensorboard
 clip
 coverage<7.0.0
 imageio-ffmpeg==0.4.4
 interrogate
-mmdet>=3.0.0rc2
+mmdet>=3.0.0
 pytest
 transformers
 clip
 imageio-ffmpeg==0.4.4
-mmdet>=3.0.0rc2
+mmdet>=3.0.0
 open_clip_torch
 PyQt5
 transformers
 
 [all:python_version < "3.7"]
 av==8.0.3
 
 [mim]
-mmcv>=2.0.0rc1
+mmcv>=2.0.0
 mmengine>=0.4.0
 
 [tests]
 clip
 coverage<7.0.0
 imageio-ffmpeg==0.4.4
 interrogate
-mmdet>=3.0.0rc2
+mmdet>=3.0.0
 pytest
 transformers
```

### Comparing `mmedit-1.0.0rc6/setup.cfg` & `mmedit-1.0.0rc7/setup.cfg`

 * *Files identical despite different names*

### Comparing `mmedit-1.0.0rc6/setup.py` & `mmedit-1.0.0rc7/setup.py`

 * *Files identical despite different names*

