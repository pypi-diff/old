# Comparing `tmp/robotframework_doctestlibrary-0.9.0.tar.gz` & `tmp/robotframework_doctestlibrary-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "robotframework_doctestlibrary-0.9.0.tar", max compression
+gzip compressed data, was "robotframework_doctestlibrary-0.9.1.tar", max compression
```

## Comparing `robotframework_doctestlibrary-0.9.0.tar` & `robotframework_doctestlibrary-0.9.1.tar`

### file list

```diff
@@ -1,13 +1,13 @@
--rw-r--r--   0        0        0    13079 2023-02-09 09:30:54.797620 robotframework_doctestlibrary-0.9.0/DocTest/__init__.py
--rw-r--r--   0        0        0    22957 2023-01-26 17:07:51.051785 robotframework_doctestlibrary-0.9.0/DocTest/CompareImage.py
--rw-r--r--   0        0        0     1462 2023-01-26 17:11:11.928605 robotframework_doctestlibrary-0.9.0/DocTest/Downloader.py
--rw-r--r--   0        0        0     8237 2023-01-26 17:07:51.055086 robotframework_doctestlibrary-0.9.0/DocTest/Ocr.py
--rw-r--r--   0        0        0     9620 2022-07-26 21:25:10.725828 robotframework_doctestlibrary-0.9.0/DocTest/PdfTest.py
--rw-r--r--   0        0        0      147 2021-10-29 12:15:14.814947 robotframework_doctestlibrary-0.9.0/DocTest/PrintJob.py
--rw-r--r--   0        0        0    18725 2021-10-29 12:15:14.814947 robotframework_doctestlibrary-0.9.0/DocTest/PrintJobTests.py
--rw-r--r--   0        0        0    54383 2023-02-09 09:28:54.200237 robotframework_doctestlibrary-0.9.0/DocTest/VisualTest.py
--rw-r--r--   0        0        0    10443 2022-10-04 15:57:02.179122 robotframework_doctestlibrary-0.9.0/LICENSE
--rw-r--r--   0        0        0      954 2023-01-28 11:41:30.992777 robotframework_doctestlibrary-0.9.0/pyproject.toml
--rw-r--r--   0        0        0    12904 2023-02-09 09:31:15.138949 robotframework_doctestlibrary-0.9.0/README.md
--rw-r--r--   0        0        0    13817 1970-01-01 00:00:00.000000 robotframework_doctestlibrary-0.9.0/setup.py
--rw-r--r--   0        0        0    13571 1970-01-01 00:00:00.000000 robotframework_doctestlibrary-0.9.0/PKG-INFO
+-rw-r--r--   0        0        0    13079 2023-02-09 09:30:54.797620 robotframework_doctestlibrary-0.9.1/DocTest/__init__.py
+-rw-r--r--   0        0        0    22964 2023-03-09 09:10:40.959705 robotframework_doctestlibrary-0.9.1/DocTest/CompareImage.py
+-rw-r--r--   0        0        0     1462 2023-01-26 17:11:11.928605 robotframework_doctestlibrary-0.9.1/DocTest/Downloader.py
+-rw-r--r--   0        0        0     8237 2023-01-26 17:07:51.055086 robotframework_doctestlibrary-0.9.1/DocTest/Ocr.py
+-rw-r--r--   0        0        0     9620 2022-07-26 21:25:10.725828 robotframework_doctestlibrary-0.9.1/DocTest/PdfTest.py
+-rw-r--r--   0        0        0      147 2021-10-29 12:15:14.814947 robotframework_doctestlibrary-0.9.1/DocTest/PrintJob.py
+-rw-r--r--   0        0        0    18725 2021-10-29 12:15:14.814947 robotframework_doctestlibrary-0.9.1/DocTest/PrintJobTests.py
+-rw-r--r--   0        0        0    54383 2023-02-09 09:28:54.200237 robotframework_doctestlibrary-0.9.1/DocTest/VisualTest.py
+-rw-r--r--   0        0        0    10443 2022-10-04 15:57:02.179122 robotframework_doctestlibrary-0.9.1/LICENSE
+-rw-r--r--   0        0        0      954 2023-03-09 09:17:18.499089 robotframework_doctestlibrary-0.9.1/pyproject.toml
+-rw-r--r--   0        0        0    12904 2023-02-09 09:31:15.138949 robotframework_doctestlibrary-0.9.1/README.md
+-rw-r--r--   0        0        0    13817 1970-01-01 00:00:00.000000 robotframework_doctestlibrary-0.9.1/setup.py
+-rw-r--r--   0        0        0    13571 1970-01-01 00:00:00.000000 robotframework_doctestlibrary-0.9.1/PKG-INFO
```

### Comparing `robotframework_doctestlibrary-0.9.0/DocTest/__init__.py` & `robotframework_doctestlibrary-0.9.1/DocTest/__init__.py`

 * *Files identical despite different names*

### Comparing `robotframework_doctestlibrary-0.9.0/DocTest/CompareImage.py` & `robotframework_doctestlibrary-0.9.1/DocTest/CompareImage.py`

 * *Files 0% similar despite different names*

```diff
@@ -210,15 +210,15 @@
                         else:
                             self.get_ocr_text_data()
                         for i in range(len(self.opencv_images)):
                             d = self.text_content[i]
                             keys = list(d.keys())
                             n_boxes = len(d['text'])
                             for j in range(n_boxes):
-                                if 'conf' not in keys or int(d['conf'][j]) > self.PYTESSERACT_CONFIDENCE:
+                                if 'conf' not in keys or int(float(d['conf'][j])) > self.PYTESSERACT_CONFIDENCE:
                                     if re.match(pattern, d['text'][j]):
                                         (x, y, w, h) = (d['left'][j], d['top'][j], d['width'][j], d['height'][j])
                                         if self.rerendered_for_ocr:
                                             pixel_recalculation_factor = self.DPI / self.MINIMUM_OCR_RESOLUTION
                                             (x, y, w, h) = (int(pixel_recalculation_factor * x), int(pixel_recalculation_factor * y), int(pixel_recalculation_factor * w), int(pixel_recalculation_factor * h))
                                         text_pattern_mask = {"page":i+1, "x":x-xoffset, "y":y-yoffset, "height":h+2*yoffset, "width":w+2*xoffset}
                                         self.placeholders.append(text_pattern_mask)
```

### Comparing `robotframework_doctestlibrary-0.9.0/DocTest/Downloader.py` & `robotframework_doctestlibrary-0.9.1/DocTest/Downloader.py`

 * *Files identical despite different names*

### Comparing `robotframework_doctestlibrary-0.9.0/DocTest/Ocr.py` & `robotframework_doctestlibrary-0.9.1/DocTest/Ocr.py`

 * *Files identical despite different names*

### Comparing `robotframework_doctestlibrary-0.9.0/DocTest/PdfTest.py` & `robotframework_doctestlibrary-0.9.1/DocTest/PdfTest.py`

 * *Files identical despite different names*

### Comparing `robotframework_doctestlibrary-0.9.0/DocTest/PrintJobTests.py` & `robotframework_doctestlibrary-0.9.1/DocTest/PrintJobTests.py`

 * *Files identical despite different names*

### Comparing `robotframework_doctestlibrary-0.9.0/DocTest/VisualTest.py` & `robotframework_doctestlibrary-0.9.1/DocTest/VisualTest.py`

 * *Files identical despite different names*

### Comparing `robotframework_doctestlibrary-0.9.0/LICENSE` & `robotframework_doctestlibrary-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `robotframework_doctestlibrary-0.9.0/pyproject.toml` & `robotframework_doctestlibrary-0.9.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "robotframework-doctestlibrary"
-version = "0.9.0"
+version = "0.9.1"
 description = "A library for Visual Document Testing"
 authors = ["Many Kasiriha <many.kasiriha@dbschenker.com>"]
 maintainers = ["Many Kasiriha <many.kasiriha@dbschenker.com>"]
 license = "Apache-2.0"
 packages = [
     { include = "DocTest" },
 ]
```

### Comparing `robotframework_doctestlibrary-0.9.0/README.md` & `robotframework_doctestlibrary-0.9.1/README.md`

 * *Files identical despite different names*

### Comparing `robotframework_doctestlibrary-0.9.0/setup.py` & `robotframework_doctestlibrary-0.9.1/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -19,15 +19,15 @@
  'pytesseract',
  'robotframework>=4',
  'scikit-image',
  'scipy']
 
 setup_kwargs = {
     'name': 'robotframework-doctestlibrary',
-    'version': '0.9.0',
+    'version': '0.9.1',
     'description': 'A library for Visual Document Testing',
     'long_description': '\n# robotframework-doctestlibrary\n----\n[Robot Framework](https://robotframework.org) DocTest library.\nSimple Automated Visual Document Testing.\n\nSee keyword documentation for\n\n- [Visual Document Tests](https://manykarim.github.io/robotframework-doctestlibrary/VisualTest.html)\n- [Print Job Tests](https://manykarim.github.io/robotframework-doctestlibrary/PrintJobTest.html)\n- [Pdf Tests (very basic)](https://manykarim.github.io/robotframework-doctestlibrary/PdfTest.html)\n\n\nSee [Talk from RoboCon2021](https://www.youtube.com/watch?v=qmpwlQoJ-nE) for a short demo and some background.\n\nPowered by\n- Open CV\n- scikit-image\n- ImageMagick (only needed for rendering .ps and .pcl files)\n- Ghostscript (only needed for rendering .ps and .pcl files)\n- PyWand (only needed for rendering .ps and .pcl files)\n- Tesseract OCR\n- parsimonious (only needed for parsing .pcl and .ps files for)\n- pymupdf\n- The knowledge of stackoverflow.com\n\n# Installation instructions\n\n`pip install --upgrade robotframework-doctestlibrary`\n\nOnly Python 3.X or newer is supported. Tested with Python 3.8/3.9/3.10\n\nIn general, an installation via `pip` or `poetry` is possible.\n\n## Install robotframework-doctestlibrary\n\n### Installation via `pip` from PyPI (recommended)\n\n* `pip install --upgrade robotframework-doctestlibrary`\n\n\n### Installation via `pip` from GitHub\n\n* `pip install git+https://github.com/manykarim/robotframework-doctestlibrary.git`  \n\nor\n\n* `git clone https://github.com/manykarim/robotframework-doctestlibrary.git`\n* `cd robotframework-doctestlibrary`\n* `pip install -e .`\n\n### Installation via `poetry`\n\n* `git clone https://github.com/manykarim/robotframework-doctestlibrary.git`\n* `cd robotframework-doctestlibrary`\n* `poetry install`\n\n## Install dependencies\n\nInstall Tesseract, Ghostscript, GhostPCL, ImageMagick binaries\n<br>Hint: Since `0.2.0` Ghostscript, GhostPCL and ImageMagick are only needed for rendering `.ps` and `.pcl`files.\n<br> Rendering and content parsing of `.pdf` is done via `MuPDF`\n<br>In the future there might be a separate pypi package for `.pcl` and `.ps` files to get rid of those dependencies.\n\nLinux\n```bash\napt-get install imagemagick tesseract-ocr ghostscript libdmtx0b\n```\n\n\nWindows\n * https://github.com/UB-Mannheim/tesseract/wiki\n * https://ghostscript.com/releases/gsdnld.html\n * https://ghostscript.com/releases/gpcldnld.html\n * https://imagemagick.org/script/download.php\n\n\n## Some special instructions for Windows \n\n### Rename executable for GhostPCL to pcl6.exe (only needed for `.pcl` support)\nThe executable for GhostPCL `gpcl6win64.exe` needs to be renamed to `pcl6.exe`\n\nOtherwise it will not be possible to render .pcl files successfully for visual comparison.\n\n### Add tesseract, ghostscript and imagemagick to system path in windows (only needed for OCR, `.pcl` and `.ps` support)\n* C:\\Program Files\\ImageMagick-7.0.10-Q16-HDRI\n* C:\\Program Files\\Tesseract-OCR\n* C:\\Program Files\\gs\\gs9.53.1\\bin\n* C:\\Program Files\\gs\\ghostpcl-9.53.1-win64\n\n(The folder names and versions on your system might be different)\n\nThat means: When you open the CMD shell you can run the commands\n* `magick.exe`\n* `tesseract.exe`\n* `gswin64.exe`\n* `pcl6.exe`\n\nsuccessfully from any folder/location\n\n### Windows error message regarding pylibdmtx\n\n[How to solve ImportError for pylibdmtx](https://github.com/NaturalHistoryMuseum/pylibdmtx/#windows-error-message)\n\nIf you see an ugly `ImportError` when importing `pylibdmtx` on\nWindows you will most likely need the [Visual C++ Redistributable Packages for\nVisual Studio 2013](https://www.microsoft.com/en-US/download/details.aspx?id=40784). Install `vcredist_x64.exe` if using 64-bit Python, `vcredist_x86.exe` if using 32-bit Python.\n\n## ImageMagick\n\nThe library might return the error `File could not be converted by ImageMagick to OpenCV Image: <path to the file>` when comparing PDF files.\nThis is due to ImageMagick permissions. Verify this as follows with the `sample.pdf` in the `testdata` directory:\n```bash\nconvert sample.pdf sample.jpg \nconvert-im6.q16: attempt to perform an operation not allowed by the security policy\n```\n\nSolution is to copy the `policy.xml` from the repository to the ImageMagick installation directory.\n\n## Docker\n\nYou can also use the [docker images](https://github.com/manykarim/robotframework-doctestlibrary/packages) or create your own Docker Image\n`docker build -t robotframework-doctest .`\nAfterwards you can, e.g., start the container and run the povided examples like this:\n* Windows\n  * `docker run -t -v "%cd%":/opt/test -w /opt/test robotframework-doctest robot atest/Compare.robot`\n* Linux\n  * `docker run -t -v $PWD:/opt/test -w /opt/test robotframework-doctest robot atest/Compare.robot`\n\n## Gitpod.io\n[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/manykarim/robotframework-doctestlibrary)  \nTry out the library using [Gitpod](https://gitpod.io/#https://github.com/manykarim/robotframework-doctestlibrary)\n\n# Examples\n\nHave a look at  \n* [Visual Comparison Tests](./atest/Compare.robot)\n* [PDF Content Tests](./atest/PdfContent.robot)\n* [Print Job Tests](./atest/PrintJobs.robot)\n\nfor more examples.\n\n### Testing with [Robot Framework](https://robotframework.org)\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest\n\n*** Test Cases ***\nCompare two Images and highlight differences\n    Compare Images    Reference.jpg    Candidate.jpg\n```\n\n### Use masks/placeholders to exclude parts from visual comparison\n\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest\n\n*** Test Cases ***\nCompare two Images and ignore parts by using masks\n    Compare Images    Reference.jpg    Candidate.jpg    placeholder_file=masks.json\n\nCompare two PDF Docments and ignore parts by using masks\n    Compare Images    Reference.jpg    Candidate.jpg    placeholder_file=masks.json\n\nCompare two Farm images with date pattern\n    Compare Images    Reference.jpg    Candidate.jpg    placeholder_file=testdata/pattern_mask.json\n\nCompare two Farm images with area mask as list\n    ${top_mask}    Create Dictionary    page=1    type=area    location=top    percent=10\n    ${bottom_mask}    Create Dictionary    page=all    type=area    location=bottom    percent=10\n    ${masks}    Create List    ${top_mask}    ${bottom_mask}\n    Compare Images    Reference.jpg    Candidate.jpg    mask=${masks}\n\nCompare two Farm images with area mask as string\n    Compare Images    Reference.jpg    Candidate.jpg    mask=top:10;bottom:10\n\n```\n#### Different Mask Types to Ignore Parts When Comparing\n##### Areas, Coordinates, Text Patterns\n```python\n[\n    {\n    "page": "all",\n    "name": "Date Pattern",\n    "type": "pattern",\n    "pattern": ".*[0-9]{2}-[a-zA-Z]{3}-[0-9]{4}.*"\n    },\n    {\n    "page": "1",\n    "name": "Top Border",\n    "type": "area",\n    "location": "top",\n    "percent":  5\n    },\n    {\n    "page": "1",\n    "name": "Left Border",\n    "type": "area",\n    "location": "left",\n    "percent":  5\n    },\n    {\n    "page": 1,\n    "name": "Top Rectangle",\n    "type": "coordinates",\n    "x": 0,\n    "y": 0,\n    "height": 10,\n    "width": 210,\n    "unit": "mm"\n    }\n]\n```\n### Accept visual different by checking move distance or text content\n\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest\n\n*** Test Cases ***\nAccept if parts are moved up to 20 pixels by pure visual check\n    Compare Images    Reference.jpg    Candidate.jpg    move_tolerance=20\n\nAccept if parts are moved up to 20 pixels by reading PDF Data\n    Compare Images    Reference.pdf    Candidate.pdf    move_tolerance=20    get_pdf_content=${true}\n\nAccept differences if text content is the same via OCR\n    Compare Images    Reference.jpg    Candidate.jpg    check_text_content=${true}\n\nAccept differences if text content is the same from PDF Data\n    Compare Images    Reference.pdf    Candidate.pdf    check_text_content=${true}    get_pdf_content=${true}\n```\n\n#### Different options to detect moved parts/objects\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest   movement_detection=orb\n\n*** Test Cases ***\nAccept if parts are moved up to 20 pixels by pure visual check\n    Compare Images    Reference.jpg    Candidate.jpg    move_tolerance=20\n```\t\n\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest   movement_detection=template\n\n*** Test Cases ***\nAccept if parts are moved up to 20 pixels by pure visual check\n    Compare Images    Reference.jpg    Candidate.jpg    move_tolerance=20\n```\t\n\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest   movement_detection=classic\n\n*** Test Cases ***\nAccept if parts are moved up to 20 pixels by pure visual check\n    Compare Images    Reference.jpg    Candidate.jpg    move_tolerance=20\n```\t\n\n### Options for taking additional screenshots, screenshot format and render resolution\nTake additional screenshots or reference and candidate file.\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest   take_screenshots=${true}    screenshot_format=png\n```\nTake diff screenshots to highlight differences\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest   show_diff=${true}    DPI=300\n```\n\n### Experimental usage of Open CV East Text Detection to improve OCR\n\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest\n\n*** Test Cases ***\nCompare two Farm images with date pattern and east detection\n    Compare Images    Reference.jpg    Candidate.jpg    placeholder_file=masks.json    ocr_engine=east\n```\n\n### Check content of PDF files\n\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.PdfTest\n\n*** Test Cases ***\nCheck if list of strings exists in PDF File\n    @{strings}=    Create List    First String    Second String\n    PDF Should Contain Strings    ${strings}    Candidate.pdf\n    \nCompare two PDF Files and only check text content\n    Compare Pdf Documents    Reference.pdf    Candidate.pdf    compare=text\n\nCompare two  PDF Files and only check text content and metadata\n    Compare Pdf Documents    Reference.pdf    Candidate.pdf    compare=text,metadata\n    \nCompare two  PDF Files and check all possible content\n    Compare Pdf Documents    Reference.pdf    Candidate.pdf\n```\n\n### Ignore Watermarks for Visual Comparisons\nStore the watermark in a separate B/W image or PDF.\n<br>\nWatermark area needs to be filled with black color.\n<br>\nWatermark content will be subtracted from Visual Comparison result.\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest\n\n*** Test Cases ***\nCompare two Images and ignore jpg watermark\n    Compare Images    Reference.jpg    Candidate.jpg    watermark_file=Watermark.jpg\n\nCompare two Images and ignore pdf watermark\n    Compare Images    Reference.pdf    Candidate.pdf    watermark_file=Watermark.pdf\n\nCompare two Images and ignore watermark folder\n    Compare Images    Reference.pdf    Candidate.pdf    watermark_file=${CURDIR}${/}watermarks\n```\n\nWatermarks can also be passed on Library import. This setting will apply to all Test Cases in Test Suite\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest   watermark_file=${CURDIR}${/}watermarks\n\n*** Test Cases ***\nCompare two Images and ignore watermarks\n    Compare Images    Reference.jpg    Candidate.jpg\n```\n\n### Get Text From Documents or Images\n\n```RobotFramework\n*** Settings ***\nLibrary    DocTest.VisualTest\n\n*** Test Cases ***\nGet Text Content And Compare\n    ${text}    Get Text From Document    Reference.pdf\n    List Should Contain Value    ${text}    Test String\n```\n\n### Using pabot to run tests in parallel\n\nDocument Testing can be run in parallel using [pabot](https://pabot.org/).  \nHowever, you need to pass the additional arguments `--artifacts` and `--artifactsinsubfolders` to the `pabot` command, to move the screenshots to the correct subfolder.  \nOtherwise the screenshots will not be visible in the `log.html`\n\n```\npabot --testlevelsplit --processes 8 --artifacts png,jpg,pdf,xml --artifactsinsubfolders /path/to/your/tests/\n```\n\n### Visual Testing of Web Applications\n\nI experimented a bit and tried to use this library for Visual Testing of Web Applications.  \nPlease have a look at this pilot example [here](https://github.com/manykarim/robotframework-doctestlibrary/blob/main/atest/Browser.robot)\n\n# Development\n\nFeel free to create issues or pull requests.  \nI\'m always happy for any feedback.\n\n## Core team\n\nIn order of appearance.\n\n  * Many Kasiriha\n  * April Wang\n\n## Contributors\n\nThis project is community driven and becomes a reality only through the work of all the people who contribute.\n',
     'author': 'Many Kasiriha',
     'author_email': 'many.kasiriha@dbschenker.com',
     'maintainer': 'Many Kasiriha',
     'maintainer_email': 'many.kasiriha@dbschenker.com',
     'url': 'https://github.com/manykarim/robotframework-doctestlibrary',
```

### Comparing `robotframework_doctestlibrary-0.9.0/PKG-INFO` & `robotframework_doctestlibrary-0.9.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: robotframework-doctestlibrary
-Version: 0.9.0
+Version: 0.9.1
 Summary: A library for Visual Document Testing
 Home-page: https://github.com/manykarim/robotframework-doctestlibrary
 License: Apache-2.0
 Author: Many Kasiriha
 Author-email: many.kasiriha@dbschenker.com
 Maintainer: Many Kasiriha
 Maintainer-email: many.kasiriha@dbschenker.com
```

