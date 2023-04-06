# Comparing `tmp/bago-0.0.8.tar.gz` & `tmp/bago-0.0.9.tar.gz`

## Comparing `bago-0.0.8.tar` & `bago-0.0.9.tar`

### file list

```diff
@@ -1,146 +1,146 @@
--rw-r--r--   0        0        0     5456 2020-02-02 00:00:00.000000 bago-0.0.8/Start_Jupyter.ipynb
--rwxr-xr-x   0        0        0      804 2020-02-02 00:00:00.000000 bago-0.0.8/docs/make.bat
--rw-r--r--   0        0        0    10648 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/MSdata-obj.doctree
--rw-r--r--   0        0        0     8464 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/acq-func.doctree
--rw-r--r--   0        0        0     8437 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/applications.doctree
--rw-r--r--   0        0        0     6916 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/backgrounds.doctree
--rw-r--r--   0        0        0     6061 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/computeNextGradient.doctree
--rw-r--r--   0        0        0     6669 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/computeSecondGradient.doctree
--rw-r--r--   0        0        0     6042 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/computeSepEff.doctree
--rw-r--r--   0        0        0     7577 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/dotProd.doctree
--rw-r--r--   0        0        0     3710 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/encodings.doctree
--rw-r--r--   0        0        0   259827 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/environment.pickle
--rw-r--r--   0        0        0     5715 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/findTopSignals.doctree
--rw-r--r--   0        0        0     6416 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/fit.doctree
--rw-r--r--   0        0        0    10142 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/genSearchSpace.doctree
--rw-r--r--   0        0        0     6584 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/getBPCData.doctree
--rw-r--r--   0        0        0     6240 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/getMobilePhasePct.doctree
--rw-r--r--   0        0        0     6549 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/getUniqueMz.doctree
--rw-r--r--   0        0        0    11681 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/getting-started-with-ipynb.doctree
--rw-r--r--   0        0        0     2600 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/getting-started-with-software.doctree
--rw-r--r--   0        0        0    10049 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/gpModel-obj.doctree
--rw-r--r--   0        0        0    29969 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/index.doctree
--rw-r--r--   0        0        0     8552 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/numberUniqueMS2.doctree
--rw-r--r--   0        0        0     6115 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/outputConfig.doctree
--rw-r--r--   0        0        0     5463 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/plotBPC.doctree
--rw-r--r--   0        0        0    16020 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/readMSdata.doctree
--rw-r--r--   0        0        0     6778 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/doctrees/updateModel.doctree
--rw-r--r--   0        0        0      234 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/.buildinfo
--rw-r--r--   0        0        0     9245 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/MSdata-obj.html
--rw-r--r--   0        0        0     8515 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/acq-func.html
--rw-r--r--   0        0        0     8199 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/applications.html
--rw-r--r--   0        0        0     8581 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/backgrounds.html
--rw-r--r--   0        0        0     8570 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/computeNextGradient.html
--rw-r--r--   0        0        0     8685 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/computeSecondGradient.html
--rw-r--r--   0        0        0     8708 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/computeSepEff.html
--rw-r--r--   0        0        0     8989 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/dotProd.html
--rw-r--r--   0        0        0     7326 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/encodings.html
--rw-r--r--   0        0        0     8391 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/findTopSignals.html
--rw-r--r--   0        0        0     8695 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/fit.html
--rw-r--r--   0        0        0     9516 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/genSearchSpace.html
--rw-r--r--   0        0        0    12336 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/genindex.html
--rw-r--r--   0        0        0     8400 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/getBPCData.html
--rw-r--r--   0        0        0     8703 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/getMobilePhasePct.html
--rw-r--r--   0        0        0     8616 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/getUniqueMz.html
--rw-r--r--   0        0        0    10591 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/getting-started-with-ipynb.html
--rw-r--r--   0        0        0     6896 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/getting-started-with-software.html
--rw-r--r--   0        0        0     8820 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/gpModel-obj.html
--rw-r--r--   0        0        0    12985 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/index.html
--rw-r--r--   0        0        0     9239 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/numberUniqueMS2.html
--rw-r--r--   0        0        0      879 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/objects.inv
--rw-r--r--   0        0        0     8667 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/outputConfig.html
--rw-r--r--   0        0        0     8161 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/plotBPC.html
--rw-r--r--   0        0        0    12881 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/readMSdata.html
--rw-r--r--   0        0        0     6267 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/search.html
--rw-r--r--   0        0        0    14445 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/searchindex.js
--rw-r--r--   0        0        0     8700 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/updateModel.html
--rw-r--r--   0        0        0      894 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/MSdata-obj.rst.txt
--rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/acq-func.rst.txt
--rw-r--r--   0        0        0      856 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/applications.rst.txt
--rw-r--r--   0        0        0     1686 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/backgrounds.rst.txt
--rw-r--r--   0        0        0      674 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/computeNextGradient.rst.txt
--rw-r--r--   0        0        0      549 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/computeSecondGradient.rst.txt
--rw-r--r--   0        0        0      533 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/computeSepEff.rst.txt
--rw-r--r--   0        0        0      599 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/dotProd.rst.txt
--rw-r--r--   0        0        0      533 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/encodings.rst.txt
--rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/findTopSignals.rst.txt
--rw-r--r--   0        0        0      568 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/fit.rst.txt
--rw-r--r--   0        0        0      973 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/genSearchSpace.rst.txt
--rw-r--r--   0        0        0      488 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/getBPCData.rst.txt
--rw-r--r--   0        0        0      613 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/getMobilePhasePct.rst.txt
--rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/getUniqueMz.rst.txt
--rw-r--r--   0        0        0     2066 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/getting-started-with-ipynb.rst.txt
--rw-r--r--   0        0        0       85 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/getting-started-with-software.rst.txt
--rw-r--r--   0        0        0      928 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/gpModel-obj.rst.txt
--rw-r--r--   0        0        0     3651 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/index.rst.txt
--rw-r--r--   0        0        0      611 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/numberUniqueMS2.rst.txt
--rw-r--r--   0        0        0      481 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/outputConfig.rst.txt
--rw-r--r--   0        0        0      351 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/plotBPC.rst.txt
--rw-r--r--   0        0        0     1781 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/readMSdata.rst.txt
--rw-r--r--   0        0        0      549 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_sources/updateModel.rst.txt
--rw-r--r--   0        0        0    15715 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/basic.css
--rw-r--r--   0        0        0     4472 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/doctools.js
--rw-r--r--   0        0        0      433 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/documentation_options.js
--rw-r--r--   0        0        0      286 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/file.png
--rw-r--r--   0        0        0     4957 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/language_data.js
--rw-r--r--   0        0        0       90 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/minus.png
--rw-r--r--   0        0        0       90 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/plus.png
--rw-r--r--   0        0        0     4892 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/pygments.css
--rw-r--r--   0        0        0    18215 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/searchtools.js
--rw-r--r--   0        0        0     4712 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/sphinx_highlight.js
--rw-r--r--   0        0        0     3229 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/badge_only.css
--rw-r--r--   0        0        0   135235 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/theme.css
--rw-r--r--   0        0        0    87624 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff
--rw-r--r--   0        0        0    67312 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff2
--rw-r--r--   0        0        0    86288 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff
--rw-r--r--   0        0        0    66444 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff2
--rw-r--r--   0        0        0   165742 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.eot
--rw-r--r--   0        0        0   444379 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.svg
--rw-r--r--   0        0        0   165548 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.ttf
--rw-r--r--   0        0        0    98024 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.woff
--rw-r--r--   0        0        0    77160 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.woff2
--rw-r--r--   0        0        0   323344 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/lato-bold-italic.woff
--rw-r--r--   0        0        0   193308 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/lato-bold-italic.woff2
--rw-r--r--   0        0        0   309728 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/lato-bold.woff
--rw-r--r--   0        0        0   184912 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/lato-bold.woff2
--rw-r--r--   0        0        0   328412 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/lato-normal-italic.woff
--rw-r--r--   0        0        0   195704 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/lato-normal-italic.woff2
--rw-r--r--   0        0        0   309192 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/lato-normal.woff
--rw-r--r--   0        0        0   182708 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/css/fonts/lato-normal.woff2
--rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/js/badge_only.js
--rw-r--r--   0        0        0     4370 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/js/html5shiv-printshiv.min.js
--rw-r--r--   0        0        0     2734 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/js/html5shiv.min.js
--rw-r--r--   0        0        0     5023 2020-02-02 00:00:00.000000 bago-0.0.8/docs/build/html/_static/js/theme.js
--rw-r--r--   0        0        0      894 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/MSdata-obj.rst
--rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/acq-func.rst
--rw-r--r--   0        0        0      856 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/applications.rst
--rw-r--r--   0        0        0     1686 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/backgrounds.rst
--rw-r--r--   0        0        0      674 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/computeNextGradient.rst
--rw-r--r--   0        0        0      549 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/computeSecondGradient.rst
--rw-r--r--   0        0        0      533 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/computeSepEff.rst
--rw-r--r--   0        0        0     1006 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/conf.py
--rw-r--r--   0        0        0      599 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/dotProd.rst
--rw-r--r--   0        0        0      533 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/encodings.rst
--rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/findTopSignals.rst
--rw-r--r--   0        0        0      568 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/fit.rst
--rw-r--r--   0        0        0      973 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/genSearchSpace.rst
--rw-r--r--   0        0        0      488 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/getBPCData.rst
--rw-r--r--   0        0        0      613 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/getMobilePhasePct.rst
--rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/getUniqueMz.rst
--rw-r--r--   0        0        0     2066 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/getting-started-with-ipynb.rst
--rw-r--r--   0        0        0       85 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/getting-started-with-software.rst
--rw-r--r--   0        0        0      928 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/gpModel-obj.rst
--rw-r--r--   0        0        0     3651 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/index.rst
--rw-r--r--   0        0        0      611 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/numberUniqueMS2.rst
--rw-r--r--   0        0        0      481 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/outputConfig.rst
--rw-r--r--   0        0        0      351 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/plotBPC.rst
--rw-r--r--   0        0        0     1781 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/readMSdata.rst
--rw-r--r--   0        0        0      549 2020-02-02 00:00:00.000000 bago-0.0.8/docs/source/updateModel.rst
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 bago-0.0.8/src/bago/__init__.py
--rw-r--r--   0        0        0     7259 2020-02-02 00:00:00.000000 bago-0.0.8/src/bago/bagoMain.py
--rw-r--r--   0        0        0    11150 2020-02-02 00:00:00.000000 bago-0.0.8/src/bago/models.py
--rw-r--r--   0        0        0    31167 2020-02-02 00:00:00.000000 bago-0.0.8/src/bago/rawDataHelper.py
--rw-r--r--   0        0        0     1084 2020-02-02 00:00:00.000000 bago-0.0.8/LICENSE
--rw-r--r--   0        0        0     1215 2020-02-02 00:00:00.000000 bago-0.0.8/README.md
--rw-r--r--   0        0        0      587 2020-02-02 00:00:00.000000 bago-0.0.8/pyproject.toml
--rw-r--r--   0        0        0     1663 2020-02-02 00:00:00.000000 bago-0.0.8/PKG-INFO
+-rw-r--r--   0        0        0     5456 2020-02-02 00:00:00.000000 bago-0.0.9/Start_Jupyter.ipynb
+-rwxr-xr-x   0        0        0      804 2020-02-02 00:00:00.000000 bago-0.0.9/docs/make.bat
+-rw-r--r--   0        0        0    10648 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/MSdata-obj.doctree
+-rw-r--r--   0        0        0     8464 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/acq-func.doctree
+-rw-r--r--   0        0        0     8437 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/applications.doctree
+-rw-r--r--   0        0        0     6916 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/backgrounds.doctree
+-rw-r--r--   0        0        0     6061 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/computeNextGradient.doctree
+-rw-r--r--   0        0        0     6669 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/computeSecondGradient.doctree
+-rw-r--r--   0        0        0     6042 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/computeSepEff.doctree
+-rw-r--r--   0        0        0     7577 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/dotProd.doctree
+-rw-r--r--   0        0        0     3710 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/encodings.doctree
+-rw-r--r--   0        0        0   259827 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/environment.pickle
+-rw-r--r--   0        0        0     5715 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/findTopSignals.doctree
+-rw-r--r--   0        0        0     6416 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/fit.doctree
+-rw-r--r--   0        0        0    10142 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/genSearchSpace.doctree
+-rw-r--r--   0        0        0     6584 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/getBPCData.doctree
+-rw-r--r--   0        0        0     6240 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/getMobilePhasePct.doctree
+-rw-r--r--   0        0        0     6549 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/getUniqueMz.doctree
+-rw-r--r--   0        0        0    11681 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/getting-started-with-ipynb.doctree
+-rw-r--r--   0        0        0     2600 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/getting-started-with-software.doctree
+-rw-r--r--   0        0        0    10049 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/gpModel-obj.doctree
+-rw-r--r--   0        0        0    29969 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/index.doctree
+-rw-r--r--   0        0        0     8552 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/numberUniqueMS2.doctree
+-rw-r--r--   0        0        0     6115 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/outputConfig.doctree
+-rw-r--r--   0        0        0     5463 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/plotBPC.doctree
+-rw-r--r--   0        0        0    16020 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/readMSdata.doctree
+-rw-r--r--   0        0        0     6778 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/doctrees/updateModel.doctree
+-rw-r--r--   0        0        0      234 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/.buildinfo
+-rw-r--r--   0        0        0     9245 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/MSdata-obj.html
+-rw-r--r--   0        0        0     8515 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/acq-func.html
+-rw-r--r--   0        0        0     8199 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/applications.html
+-rw-r--r--   0        0        0     8581 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/backgrounds.html
+-rw-r--r--   0        0        0     8570 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/computeNextGradient.html
+-rw-r--r--   0        0        0     8685 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/computeSecondGradient.html
+-rw-r--r--   0        0        0     8708 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/computeSepEff.html
+-rw-r--r--   0        0        0     8989 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/dotProd.html
+-rw-r--r--   0        0        0     7326 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/encodings.html
+-rw-r--r--   0        0        0     8391 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/findTopSignals.html
+-rw-r--r--   0        0        0     8695 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/fit.html
+-rw-r--r--   0        0        0     9516 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/genSearchSpace.html
+-rw-r--r--   0        0        0    12336 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/genindex.html
+-rw-r--r--   0        0        0     8400 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/getBPCData.html
+-rw-r--r--   0        0        0     8703 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/getMobilePhasePct.html
+-rw-r--r--   0        0        0     8616 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/getUniqueMz.html
+-rw-r--r--   0        0        0    10591 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/getting-started-with-ipynb.html
+-rw-r--r--   0        0        0     6896 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/getting-started-with-software.html
+-rw-r--r--   0        0        0     8820 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/gpModel-obj.html
+-rw-r--r--   0        0        0    12985 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/index.html
+-rw-r--r--   0        0        0     9239 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/numberUniqueMS2.html
+-rw-r--r--   0        0        0      879 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/objects.inv
+-rw-r--r--   0        0        0     8667 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/outputConfig.html
+-rw-r--r--   0        0        0     8161 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/plotBPC.html
+-rw-r--r--   0        0        0    12881 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/readMSdata.html
+-rw-r--r--   0        0        0     6267 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/search.html
+-rw-r--r--   0        0        0    14445 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/searchindex.js
+-rw-r--r--   0        0        0     8700 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/updateModel.html
+-rw-r--r--   0        0        0      894 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/MSdata-obj.rst.txt
+-rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/acq-func.rst.txt
+-rw-r--r--   0        0        0      856 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/applications.rst.txt
+-rw-r--r--   0        0        0     1686 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/backgrounds.rst.txt
+-rw-r--r--   0        0        0      674 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/computeNextGradient.rst.txt
+-rw-r--r--   0        0        0      549 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/computeSecondGradient.rst.txt
+-rw-r--r--   0        0        0      533 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/computeSepEff.rst.txt
+-rw-r--r--   0        0        0      599 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/dotProd.rst.txt
+-rw-r--r--   0        0        0      533 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/encodings.rst.txt
+-rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/findTopSignals.rst.txt
+-rw-r--r--   0        0        0      568 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/fit.rst.txt
+-rw-r--r--   0        0        0      973 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/genSearchSpace.rst.txt
+-rw-r--r--   0        0        0      488 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/getBPCData.rst.txt
+-rw-r--r--   0        0        0      613 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/getMobilePhasePct.rst.txt
+-rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/getUniqueMz.rst.txt
+-rw-r--r--   0        0        0     2066 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/getting-started-with-ipynb.rst.txt
+-rw-r--r--   0        0        0       85 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/getting-started-with-software.rst.txt
+-rw-r--r--   0        0        0      928 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/gpModel-obj.rst.txt
+-rw-r--r--   0        0        0     3651 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/index.rst.txt
+-rw-r--r--   0        0        0      611 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/numberUniqueMS2.rst.txt
+-rw-r--r--   0        0        0      481 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/outputConfig.rst.txt
+-rw-r--r--   0        0        0      351 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/plotBPC.rst.txt
+-rw-r--r--   0        0        0     1781 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/readMSdata.rst.txt
+-rw-r--r--   0        0        0      549 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_sources/updateModel.rst.txt
+-rw-r--r--   0        0        0    15715 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/basic.css
+-rw-r--r--   0        0        0     4472 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/doctools.js
+-rw-r--r--   0        0        0      433 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/documentation_options.js
+-rw-r--r--   0        0        0      286 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/file.png
+-rw-r--r--   0        0        0     4957 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/language_data.js
+-rw-r--r--   0        0        0       90 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/minus.png
+-rw-r--r--   0        0        0       90 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/plus.png
+-rw-r--r--   0        0        0     4892 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/pygments.css
+-rw-r--r--   0        0        0    18215 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/searchtools.js
+-rw-r--r--   0        0        0     4712 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/sphinx_highlight.js
+-rw-r--r--   0        0        0     3229 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/badge_only.css
+-rw-r--r--   0        0        0   135235 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/theme.css
+-rw-r--r--   0        0        0    87624 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff
+-rw-r--r--   0        0        0    67312 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff2
+-rw-r--r--   0        0        0    86288 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff
+-rw-r--r--   0        0        0    66444 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff2
+-rw-r--r--   0        0        0   165742 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.eot
+-rw-r--r--   0        0        0   444379 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.svg
+-rw-r--r--   0        0        0   165548 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.ttf
+-rw-r--r--   0        0        0    98024 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.woff
+-rw-r--r--   0        0        0    77160 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.woff2
+-rw-r--r--   0        0        0   323344 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/lato-bold-italic.woff
+-rw-r--r--   0        0        0   193308 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/lato-bold-italic.woff2
+-rw-r--r--   0        0        0   309728 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/lato-bold.woff
+-rw-r--r--   0        0        0   184912 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/lato-bold.woff2
+-rw-r--r--   0        0        0   328412 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/lato-normal-italic.woff
+-rw-r--r--   0        0        0   195704 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/lato-normal-italic.woff2
+-rw-r--r--   0        0        0   309192 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/lato-normal.woff
+-rw-r--r--   0        0        0   182708 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/css/fonts/lato-normal.woff2
+-rw-r--r--   0        0        0      934 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/js/badge_only.js
+-rw-r--r--   0        0        0     4370 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/js/html5shiv-printshiv.min.js
+-rw-r--r--   0        0        0     2734 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/js/html5shiv.min.js
+-rw-r--r--   0        0        0     5023 2020-02-02 00:00:00.000000 bago-0.0.9/docs/build/html/_static/js/theme.js
+-rw-r--r--   0        0        0      894 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/MSdata-obj.rst
+-rw-r--r--   0        0        0     1754 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/acq-func.rst
+-rw-r--r--   0        0        0      856 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/applications.rst
+-rw-r--r--   0        0        0     1686 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/backgrounds.rst
+-rw-r--r--   0        0        0      674 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/computeNextGradient.rst
+-rw-r--r--   0        0        0      549 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/computeSecondGradient.rst
+-rw-r--r--   0        0        0      533 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/computeSepEff.rst
+-rw-r--r--   0        0        0     1006 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/conf.py
+-rw-r--r--   0        0        0      599 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/dotProd.rst
+-rw-r--r--   0        0        0      533 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/encodings.rst
+-rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/findTopSignals.rst
+-rw-r--r--   0        0        0      568 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/fit.rst
+-rw-r--r--   0        0        0      973 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/genSearchSpace.rst
+-rw-r--r--   0        0        0      488 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/getBPCData.rst
+-rw-r--r--   0        0        0      613 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/getMobilePhasePct.rst
+-rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/getUniqueMz.rst
+-rw-r--r--   0        0        0     2066 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/getting-started-with-ipynb.rst
+-rw-r--r--   0        0        0       85 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/getting-started-with-software.rst
+-rw-r--r--   0        0        0      928 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/gpModel-obj.rst
+-rw-r--r--   0        0        0     3651 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/index.rst
+-rw-r--r--   0        0        0      611 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/numberUniqueMS2.rst
+-rw-r--r--   0        0        0      481 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/outputConfig.rst
+-rw-r--r--   0        0        0      351 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/plotBPC.rst
+-rw-r--r--   0        0        0     1781 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/readMSdata.rst
+-rw-r--r--   0        0        0      549 2020-02-02 00:00:00.000000 bago-0.0.9/docs/source/updateModel.rst
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 bago-0.0.9/src/bago/__init__.py
+-rw-r--r--   0        0        0     7471 2020-02-02 00:00:00.000000 bago-0.0.9/src/bago/bagoMain.py
+-rw-r--r--   0        0        0    11150 2020-02-02 00:00:00.000000 bago-0.0.9/src/bago/models.py
+-rw-r--r--   0        0        0    31395 2020-02-02 00:00:00.000000 bago-0.0.9/src/bago/rawDataHelper.py
+-rw-r--r--   0        0        0     1084 2020-02-02 00:00:00.000000 bago-0.0.9/LICENSE
+-rw-r--r--   0        0        0     1215 2020-02-02 00:00:00.000000 bago-0.0.9/README.md
+-rw-r--r--   0        0        0      587 2020-02-02 00:00:00.000000 bago-0.0.9/pyproject.toml
+-rw-r--r--   0        0        0     1663 2020-02-02 00:00:00.000000 bago-0.0.9/PKG-INFO
```

### Comparing `bago-0.0.8/Start_Jupyter.ipynb` & `bago-0.0.9/Start_Jupyter.ipynb`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/make.bat` & `bago-0.0.9/docs/make.bat`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/MSdata-obj.doctree` & `bago-0.0.9/docs/build/doctrees/MSdata-obj.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/acq-func.doctree` & `bago-0.0.9/docs/build/doctrees/acq-func.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/applications.doctree` & `bago-0.0.9/docs/build/doctrees/applications.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/backgrounds.doctree` & `bago-0.0.9/docs/build/doctrees/backgrounds.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/computeNextGradient.doctree` & `bago-0.0.9/docs/build/doctrees/computeNextGradient.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/computeSecondGradient.doctree` & `bago-0.0.9/docs/build/doctrees/computeSecondGradient.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/computeSepEff.doctree` & `bago-0.0.9/docs/build/doctrees/computeSepEff.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/dotProd.doctree` & `bago-0.0.9/docs/build/doctrees/dotProd.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/encodings.doctree` & `bago-0.0.9/docs/build/doctrees/encodings.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/environment.pickle` & `bago-0.0.9/docs/build/doctrees/environment.pickle`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/findTopSignals.doctree` & `bago-0.0.9/docs/build/doctrees/findTopSignals.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/fit.doctree` & `bago-0.0.9/docs/build/doctrees/fit.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/genSearchSpace.doctree` & `bago-0.0.9/docs/build/doctrees/genSearchSpace.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/getBPCData.doctree` & `bago-0.0.9/docs/build/doctrees/getBPCData.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/getMobilePhasePct.doctree` & `bago-0.0.9/docs/build/doctrees/getMobilePhasePct.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/getUniqueMz.doctree` & `bago-0.0.9/docs/build/doctrees/getUniqueMz.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/getting-started-with-ipynb.doctree` & `bago-0.0.9/docs/build/doctrees/getting-started-with-ipynb.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/getting-started-with-software.doctree` & `bago-0.0.9/docs/build/doctrees/getting-started-with-software.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/gpModel-obj.doctree` & `bago-0.0.9/docs/build/doctrees/gpModel-obj.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/index.doctree` & `bago-0.0.9/docs/build/doctrees/index.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/numberUniqueMS2.doctree` & `bago-0.0.9/docs/build/doctrees/numberUniqueMS2.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/outputConfig.doctree` & `bago-0.0.9/docs/build/doctrees/outputConfig.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/plotBPC.doctree` & `bago-0.0.9/docs/build/doctrees/plotBPC.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/readMSdata.doctree` & `bago-0.0.9/docs/build/doctrees/readMSdata.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/doctrees/updateModel.doctree` & `bago-0.0.9/docs/build/doctrees/updateModel.doctree`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/MSdata-obj.html` & `bago-0.0.9/docs/build/html/MSdata-obj.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/acq-func.html` & `bago-0.0.9/docs/build/html/acq-func.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/applications.html` & `bago-0.0.9/docs/build/html/applications.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/backgrounds.html` & `bago-0.0.9/docs/build/html/backgrounds.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/computeNextGradient.html` & `bago-0.0.9/docs/build/html/computeNextGradient.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/computeSecondGradient.html` & `bago-0.0.9/docs/build/html/computeSecondGradient.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/computeSepEff.html` & `bago-0.0.9/docs/build/html/computeSepEff.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/dotProd.html` & `bago-0.0.9/docs/build/html/dotProd.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/encodings.html` & `bago-0.0.9/docs/build/html/encodings.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/findTopSignals.html` & `bago-0.0.9/docs/build/html/findTopSignals.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/fit.html` & `bago-0.0.9/docs/build/html/fit.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/genSearchSpace.html` & `bago-0.0.9/docs/build/html/genSearchSpace.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/genindex.html` & `bago-0.0.9/docs/build/html/genindex.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/getBPCData.html` & `bago-0.0.9/docs/build/html/getBPCData.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/getMobilePhasePct.html` & `bago-0.0.9/docs/build/html/getMobilePhasePct.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/getUniqueMz.html` & `bago-0.0.9/docs/build/html/getUniqueMz.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/getting-started-with-ipynb.html` & `bago-0.0.9/docs/build/html/getting-started-with-ipynb.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/getting-started-with-software.html` & `bago-0.0.9/docs/build/html/getting-started-with-software.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/gpModel-obj.html` & `bago-0.0.9/docs/build/html/gpModel-obj.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/index.html` & `bago-0.0.9/docs/build/html/index.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/numberUniqueMS2.html` & `bago-0.0.9/docs/build/html/numberUniqueMS2.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/objects.inv` & `bago-0.0.9/docs/build/html/objects.inv`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/outputConfig.html` & `bago-0.0.9/docs/build/html/outputConfig.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/plotBPC.html` & `bago-0.0.9/docs/build/html/plotBPC.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/readMSdata.html` & `bago-0.0.9/docs/build/html/readMSdata.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/search.html` & `bago-0.0.9/docs/build/html/search.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/searchindex.js` & `bago-0.0.9/docs/build/html/searchindex.js`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/updateModel.html` & `bago-0.0.9/docs/build/html/updateModel.html`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/MSdata-obj.rst.txt` & `bago-0.0.9/docs/build/html/_sources/MSdata-obj.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/acq-func.rst.txt` & `bago-0.0.9/docs/build/html/_sources/acq-func.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/applications.rst.txt` & `bago-0.0.9/docs/build/html/_sources/applications.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/backgrounds.rst.txt` & `bago-0.0.9/docs/build/html/_sources/backgrounds.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/computeNextGradient.rst.txt` & `bago-0.0.9/docs/build/html/_sources/computeNextGradient.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/computeSecondGradient.rst.txt` & `bago-0.0.9/docs/build/html/_sources/computeSecondGradient.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/computeSepEff.rst.txt` & `bago-0.0.9/docs/build/html/_sources/computeSepEff.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/dotProd.rst.txt` & `bago-0.0.9/docs/build/html/_sources/dotProd.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/encodings.rst.txt` & `bago-0.0.9/docs/build/html/_sources/encodings.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/fit.rst.txt` & `bago-0.0.9/docs/build/html/_sources/fit.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/genSearchSpace.rst.txt` & `bago-0.0.9/docs/build/html/_sources/genSearchSpace.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/getMobilePhasePct.rst.txt` & `bago-0.0.9/docs/build/html/_sources/getMobilePhasePct.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/getting-started-with-ipynb.rst.txt` & `bago-0.0.9/docs/build/html/_sources/getting-started-with-ipynb.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/gpModel-obj.rst.txt` & `bago-0.0.9/docs/build/html/_sources/gpModel-obj.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/index.rst.txt` & `bago-0.0.9/docs/build/html/_sources/index.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/numberUniqueMS2.rst.txt` & `bago-0.0.9/docs/build/html/_sources/numberUniqueMS2.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/readMSdata.rst.txt` & `bago-0.0.9/docs/build/html/_sources/readMSdata.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_sources/updateModel.rst.txt` & `bago-0.0.9/docs/build/html/_sources/updateModel.rst.txt`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/basic.css` & `bago-0.0.9/docs/build/html/_static/basic.css`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/doctools.js` & `bago-0.0.9/docs/build/html/_static/doctools.js`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/language_data.js` & `bago-0.0.9/docs/build/html/_static/language_data.js`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/pygments.css` & `bago-0.0.9/docs/build/html/_static/pygments.css`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/searchtools.js` & `bago-0.0.9/docs/build/html/_static/searchtools.js`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/sphinx_highlight.js` & `bago-0.0.9/docs/build/html/_static/sphinx_highlight.js`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/badge_only.css` & `bago-0.0.9/docs/build/html/_static/css/badge_only.css`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/theme.css` & `bago-0.0.9/docs/build/html/_static/css/theme.css`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff` & `bago-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff2` & `bago-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Bold.woff2`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff` & `bago-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff2` & `bago-0.0.9/docs/build/html/_static/css/fonts/Roboto-Slab-Regular.woff2`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.eot` & `bago-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.eot`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.svg` & `bago-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.svg`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.ttf` & `bago-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.ttf`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.woff` & `bago-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.woff`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/fontawesome-webfont.woff2` & `bago-0.0.9/docs/build/html/_static/css/fonts/fontawesome-webfont.woff2`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/lato-bold-italic.woff` & `bago-0.0.9/docs/build/html/_static/css/fonts/lato-bold-italic.woff`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/lato-bold-italic.woff2` & `bago-0.0.9/docs/build/html/_static/css/fonts/lato-bold-italic.woff2`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/lato-bold.woff` & `bago-0.0.9/docs/build/html/_static/css/fonts/lato-bold.woff`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/lato-bold.woff2` & `bago-0.0.9/docs/build/html/_static/css/fonts/lato-bold.woff2`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/lato-normal-italic.woff` & `bago-0.0.9/docs/build/html/_static/css/fonts/lato-normal-italic.woff`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/lato-normal-italic.woff2` & `bago-0.0.9/docs/build/html/_static/css/fonts/lato-normal-italic.woff2`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/lato-normal.woff` & `bago-0.0.9/docs/build/html/_static/css/fonts/lato-normal.woff`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/css/fonts/lato-normal.woff2` & `bago-0.0.9/docs/build/html/_static/css/fonts/lato-normal.woff2`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/js/badge_only.js` & `bago-0.0.9/docs/build/html/_static/js/badge_only.js`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/js/html5shiv-printshiv.min.js` & `bago-0.0.9/docs/build/html/_static/js/html5shiv-printshiv.min.js`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/js/html5shiv.min.js` & `bago-0.0.9/docs/build/html/_static/js/html5shiv.min.js`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/build/html/_static/js/theme.js` & `bago-0.0.9/docs/build/html/_static/js/theme.js`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/MSdata-obj.rst` & `bago-0.0.9/docs/source/MSdata-obj.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/acq-func.rst` & `bago-0.0.9/docs/source/acq-func.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/applications.rst` & `bago-0.0.9/docs/source/applications.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/backgrounds.rst` & `bago-0.0.9/docs/source/backgrounds.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/computeNextGradient.rst` & `bago-0.0.9/docs/source/computeNextGradient.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/computeSecondGradient.rst` & `bago-0.0.9/docs/source/computeSecondGradient.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/computeSepEff.rst` & `bago-0.0.9/docs/source/computeSepEff.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/conf.py` & `bago-0.0.9/docs/source/conf.py`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/dotProd.rst` & `bago-0.0.9/docs/source/dotProd.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/encodings.rst` & `bago-0.0.9/docs/source/encodings.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/fit.rst` & `bago-0.0.9/docs/source/fit.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/genSearchSpace.rst` & `bago-0.0.9/docs/source/genSearchSpace.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/getMobilePhasePct.rst` & `bago-0.0.9/docs/source/getMobilePhasePct.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/getting-started-with-ipynb.rst` & `bago-0.0.9/docs/source/getting-started-with-ipynb.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/gpModel-obj.rst` & `bago-0.0.9/docs/source/gpModel-obj.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/index.rst` & `bago-0.0.9/docs/source/index.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/numberUniqueMS2.rst` & `bago-0.0.9/docs/source/numberUniqueMS2.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/readMSdata.rst` & `bago-0.0.9/docs/source/readMSdata.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/docs/source/updateModel.rst` & `bago-0.0.9/docs/source/updateModel.rst`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/src/bago/bagoMain.py` & `bago-0.0.9/src/bago/bagoMain.py`

 * *Files 10% similar despite different names*

```diff
@@ -133,23 +133,26 @@
     # Obtain the separation efficiency of each data
     sepEffs = [exp[k].sepEff for k in exp.keys()]
     parameters["sepEffs"] = {k: v for k, v in zip(exp.keys(), sepEffs)}
 
     # Find the key of the data with the highest separation efficiency
     maxSepEffKey = list(exp.keys())[np.argmax(sepEffs)]
 
+    # Find the number of unique MS/MS spectra
+    parameters['uniqueMS2'] = [exp[k].getUniqueMS2(returnNum=True) for k in exp.keys()]
+
     if maxSepEffKey in parameters["grads"].keys():
         # Find the gradient setting that gives the highest separation efficiency
         maxSepEffGrad = parameters["grads"][maxSepEffKey]
 
         # Print the gradient setting that gives the highest separation efficiency
         print("The gradient setting that gives the highest separation efficiency is: {}.".format(maxSepEffGrad))
 
-        # Create a data frame of two columns: gradient name and separation efficiency
-        df = pd.DataFrame({"Gradient": exp.keys(), "Separation efficiency": sepEffs})
+        # Create a data frame of two columns: gradient name, separation efficiency, and number of unique MS/MS spectra
+        df = pd.DataFrame({"Gradient": exp.keys(), "Separation efficiency": sepEffs, "Unique MS/MS": parameters['uniqueMS2']})
 
         # Save the data frame to a csv file
         df.to_csv("Evaluation.csv", index=False)
     else:
         print("The gradient setting that gives the highest separation efficiency is: {}.".format(maxSepEffKey))
```

### Comparing `bago-0.0.8/src/bago/models.py` & `bago-0.0.9/src/bago/models.py`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/src/bago/rawDataHelper.py` & `bago-0.0.9/src/bago/rawDataHelper.py`

 * *Files 1% similar despite different names*

```diff
@@ -653,33 +653,36 @@
 
     if rep == 'simple':
         return dp
     elif rep == 'full':
         return {'dotprod': dp, 'matchNumber': matchNum}
 
 
-def numberUniqueMS2(d, rtTol=1.0, precsMzTol=0.01, dpTol=0.95):
+def getUniqueMS2(d, rtTol=1.0, precsMzTol=0.01, dpTol=0.95, returnNum=False):
     """
     Function to calculate the number of unique MS2.
 
     Parameters
     ----------------------------------------------------------
     d: MSData object
         MS data
     rtTol: float
         Tolerance of retention time, in min.
     precsMzTol: float
         Tolerance of precursor m/z, in Da.
     dpTol: float
         Tolerance of dot product.
+    returnNum: boolean
+        True to return the number of unique MS2;
+        False to return the list of unique MS2.
 
     Returns
     ----------------------------------------------------------
     List:
-        Unique MS2 spectra.
+        Unique MS2 spectra (when returnNum is False).
     """
 
     uniqueMS2 = []
     temp = [{
         "ms2": [d.ms2Data[0]],
         "precsMz": d.ms2Data[0].precsMz,
         "bestms2": d.ms2Data[0]
@@ -716,15 +719,18 @@
             if ms2.rt - m["ms2"][-1].rt > rtTol:
                 trans.append(i)
         for i in list(reversed(trans)):
             uniqueMS2.append(temp.pop(i))
 
     uniqueMS2 += temp
 
-    return uniqueMS2
+    if returnNum:
+        return len(uniqueMS2)
+    else:
+        return uniqueMS2
 
 
 def getUniqueMz(d, precsMzTol=0.01):
     """
     Function to calculate the number of unique m/z
     ----------------------------------------------------------
     d: MSData object
```

### Comparing `bago-0.0.8/LICENSE` & `bago-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/README.md` & `bago-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `bago-0.0.8/pyproject.toml` & `bago-0.0.9/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "bago"
-version = "0.0.8"
+version = "0.0.9"
 authors = [
   { name="Huaxu", email="yhxchem@outlook.com" },
 ]
 maintainers = [
   { name="Huaxu", email="yhxchem@outlook.com" },
 ]
 description = "LC gradient optimization and evaluation"
```

### Comparing `bago-0.0.8/PKG-INFO` & `bago-0.0.9/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: bago
-Version: 0.0.8
+Version: 0.0.9
 Summary: LC gradient optimization and evaluation
 Project-URL: Homepage, https://github.com/Waddlessss/BAGO
 Author-email: Huaxu <yhxchem@outlook.com>
 Maintainer-email: Huaxu <yhxchem@outlook.com>
 License-File: LICENSE
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

