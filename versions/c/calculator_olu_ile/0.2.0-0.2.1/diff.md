# Comparing `tmp/calculator_olu_ile-0.2.0.tar.gz` & `tmp/calculator_olu_ile-0.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "calculator_olu_ile-0.2.0.tar", last modified: Sun Apr  2 06:13:15 2023, max compression
+gzip compressed data, was "calculator_olu_ile-0.2.1.tar", last modified: Fri Apr  7 03:26:38 2023, max compression
```

## Comparing `calculator_olu_ile-0.2.0.tar` & `calculator_olu_ile-0.2.1.tar`

### file list

```diff
@@ -1,13 +1,13 @@
--rw-r--r--   0        0        0       56 2023-03-30 16:24:42.225212 calculator_olu_ile-0.2.0/.gitignore
--rw-r--r--   0        0        0    15659 2023-04-02 05:30:35.094469 calculator_olu_ile-0.2.0/115.ipynb
--rw-r--r--   0        0        0      433 2023-04-02 05:51:44.860641 calculator_olu_ile-0.2.0/CHANGELOG.md
--rw-r--r--   0        0        0     1104 2023-03-30 08:54:56.319072 calculator_olu_ile-0.2.0/LICENSE
--rw-r--r--   0        0        0     1698 2023-04-02 05:51:44.870650 calculator_olu_ile-0.2.0/README.md
--rw-r--r--   0        0        0      102 2023-04-02 06:00:16.387869 calculator_olu_ile-0.2.0/calculator_olu_ile/__init__.py
--rw-r--r--   0        0        0     4148 2023-04-01 14:32:14.268401 calculator_olu_ile-0.2.0/calculator_olu_ile/calculator.py
--rw-r--r--   0        0        0      191 2023-04-01 14:29:44.922618 calculator_olu_ile-0.2.0/calculator_olu_ile/customerror.py
--rw-r--r--   0        0        0      384 2023-03-30 08:59:44.431465 calculator_olu_ile-0.2.0/pyproject.toml
--rw-r--r--   0        0        0        0 2023-03-30 09:37:00.176510 calculator_olu_ile-0.2.0/tests/__init__.py
--rw-r--r--   0        0        0     2613 2023-04-02 05:30:35.107478 calculator_olu_ile-0.2.0/tests/calculator_test.py
--rw-r--r--   0        0        0      407 2023-03-30 15:19:38.652618 calculator_olu_ile-0.2.0/tox.ini
--rw-r--r--   0        0        0     1942 1970-01-01 00:00:00.000000 calculator_olu_ile-0.2.0/PKG-INFO
+-rw-r--r--   0        0        0       56 2023-03-30 16:24:42.225212 calculator_olu_ile-0.2.1/.gitignore
+-rw-r--r--   0        0        0    19196 2023-04-06 18:51:29.939588 calculator_olu_ile-0.2.1/115.ipynb
+-rw-r--r--   0        0        0      520 2023-04-07 03:06:28.224372 calculator_olu_ile-0.2.1/CHANGELOG.md
+-rw-r--r--   0        0        0     1104 2023-03-30 08:54:56.319072 calculator_olu_ile-0.2.1/LICENSE
+-rw-r--r--   0        0        0     1698 2023-04-02 05:51:44.870650 calculator_olu_ile-0.2.1/README.md
+-rw-r--r--   0        0        0      102 2023-04-07 03:21:12.048055 calculator_olu_ile-0.2.1/calculator_olu_ile/__init__.py
+-rw-r--r--   0        0        0     4122 2023-04-06 18:48:22.594799 calculator_olu_ile-0.2.1/calculator_olu_ile/calculator.py
+-rw-r--r--   0        0        0      335 2023-04-06 08:27:42.420584 calculator_olu_ile-0.2.1/calculator_olu_ile/customerror.py
+-rw-r--r--   0        0        0      384 2023-03-30 08:59:44.431465 calculator_olu_ile-0.2.1/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-03-30 09:37:00.176510 calculator_olu_ile-0.2.1/tests/__init__.py
+-rw-r--r--   0        0        0     2613 2023-04-02 05:30:35.107478 calculator_olu_ile-0.2.1/tests/calculator_test.py
+-rw-r--r--   0        0        0      414 2023-04-06 18:47:17.483218 calculator_olu_ile-0.2.1/tox.ini
+-rw-r--r--   0        0        0     1942 1970-01-01 00:00:00.000000 calculator_olu_ile-0.2.1/PKG-INFO
```

### Comparing `calculator_olu_ile-0.2.0/115.ipynb` & `calculator_olu_ile-0.2.1/115.ipynb`

 * *Files 24% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.9662229938271605%*

 * *Differences: {"'cells'": "{1: {'execution_count': 36}, 3: {'execution_count': 37}, 5: {'execution_count': 38, "*

 * *            "'metadata': {delete: ['pycharm']}, 'outputs': [OrderedDict([('name', 'stdout'), "*

 * *            "('output_type', 'stream'), ('text', ['Trying:\\n', '    cal = Calculator()\\n', "*

 * *            "'Expecting nothing\\n', 'ok\\n', 'Trying:\\n', '    print(cal.accum)\\n', "*

 * *            "'Expecting:\\n', '    0\\n', 'ok\\n', 'Trying:\\n', '    cal = Calculator()\\n', "*

 * *            "'Expecting nothing\\n', ' […]*

```diff
@@ -6,15 +6,15 @@
             "metadata": {},
             "source": [
                 "## Calculator class"
             ]
         },
         {
             "cell_type": "code",
-            "execution_count": 1,
+            "execution_count": 36,
             "id": "vbgEGbvVgtQY",
             "metadata": {
                 "colab": {
                     "base_uri": "https://localhost:8080/"
                 },
                 "id": "vbgEGbvVgtQY",
                 "outputId": "e70c65dd-e61a-4059-ce6d-e537137aad59"
@@ -162,40 +162,26 @@
                 "            >>> print(cal.is_input_valid(6))\n",
                 "            True\n",
                 "        \"\"\"\n",
                 "        return True if type(num) == int or type(num) == float else False"
             ]
         },
         {
-            "cell_type": "code",
-            "execution_count": null,
-            "id": "45f7b523",
-            "metadata": {
-                "pycharm": {
-                    "is_executing": true
-                }
-            },
-            "outputs": [],
-            "source": [
-                "!pip install -U pytest"
-            ]
-        },
-        {
             "cell_type": "markdown",
             "id": "abEmFjpbVmLe",
             "metadata": {
                 "id": "abEmFjpbVmLe"
             },
             "source": [
                 "## Calculator Test class"
             ]
         },
         {
             "cell_type": "code",
-            "execution_count": 15,
+            "execution_count": 37,
             "id": "UxY_fEH_g7q8",
             "metadata": {
                 "colab": {
                     "base_uri": "https://localhost:8080/"
                 },
                 "id": "UxY_fEH_g7q8",
                 "outputId": "15199045-d241-4b25-9863-04512339b5de"
@@ -286,71 +272,205 @@
                 "    with raises(Exception) as e:\n",
                 "        cal.root('wrong message')\n",
                 "    assert e.type == NoneNumericValueError, \"Should be NoneNumericValueError\"\n"
             ]
         },
         {
             "cell_type": "markdown",
-            "id": "oNWgGKdmV8Nx",
-            "metadata": {
-                "id": "oNWgGKdmV8Nx"
-            },
-            "source": [
-                "## Execute Calculator class"
-            ]
-        },
-        {
-            "cell_type": "code",
-            "execution_count": null,
-            "id": "IS5-62b_1OZ7",
-            "metadata": {
-                "colab": {
-                    "base_uri": "https://localhost:8080/"
-                },
-                "id": "IS5-62b_1OZ7",
-                "outputId": "1f47edea-8d30-4a94-9e2d-8f67664590d9",
-                "pycharm": {
-                    "is_executing": true
-                }
-            },
-            "outputs": [],
-            "source": [
-                "from calculator_olu_ile.calculator import Calculator\n",
-                "cal = Calculator()\n",
-                "cal.add(2)\n",
-                "cal.add(2)\n",
-                "print('='*15, 'Calculator', '='*18, end='\\n\\n')\n",
-                "print('Calculators current result: ', cal.accum, end='\\n\\n')"
-            ]
-        },
-        {
-            "cell_type": "markdown",
             "id": "tt3FwSlvU4ya",
             "metadata": {
                 "id": "tt3FwSlvU4ya"
             },
             "source": [
                 "## Execute doctest"
             ]
         },
         {
             "cell_type": "code",
-            "execution_count": null,
+            "execution_count": 38,
             "id": "V5VwRq0O_oOq",
             "metadata": {
                 "colab": {
                     "base_uri": "https://localhost:8080/"
                 },
                 "id": "V5VwRq0O_oOq",
-                "outputId": "794ef74e-6deb-486e-9d9a-2d69e2fd48a4",
-                "pycharm": {
-                    "is_executing": true
-                }
+                "outputId": "794ef74e-6deb-486e-9d9a-2d69e2fd48a4"
             },
-            "outputs": [],
+            "outputs": [
+                {
+                    "name": "stdout",
+                    "output_type": "stream",
+                    "text": [
+                        "Trying:\n",
+                        "    cal = Calculator()\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.accum)\n",
+                        "Expecting:\n",
+                        "    0\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal = Calculator()\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.accum = 5\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.accum)\n",
+                        "Expecting:\n",
+                        "    5\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal = Calculator()\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.add(2)\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.accum)\n",
+                        "Expecting:\n",
+                        "    2\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.add(2)\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.accum)\n",
+                        "Expecting:\n",
+                        "    4\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal = Calculator()\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.divide(2)\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.accum)\n",
+                        "Expecting:\n",
+                        "    0.0\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.accum = 2\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.divide(2)\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.accum)\n",
+                        "Expecting:\n",
+                        "    1.0\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal = Calculator()\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.is_input_valid(\"text\"))\n",
+                        "Expecting:\n",
+                        "    False\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.is_input_valid(6))\n",
+                        "Expecting:\n",
+                        "    True\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal = Calculator()\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.multiply(2)\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.accum)\n",
+                        "Expecting:\n",
+                        "    0\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.accum = 2\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.multiply(2)\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.accum)\n",
+                        "Expecting:\n",
+                        "    4\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal = Calculator()\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.accum = 9\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.root(2)\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.accum)\n",
+                        "Expecting:\n",
+                        "    3.0\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal = Calculator()\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.subtract(2)\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.accum)\n",
+                        "Expecting:\n",
+                        "    -2\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    cal.subtract(2)\n",
+                        "Expecting nothing\n",
+                        "ok\n",
+                        "Trying:\n",
+                        "    print(cal.accum)\n",
+                        "Expecting:\n",
+                        "    -4\n",
+                        "ok\n",
+                        "3 items had no tests:\n",
+                        "    calculator\n",
+                        "    calculator.Calculator\n",
+                        "    calculator.Calculator.__init__\n",
+                        "7 items passed all tests:\n",
+                        "   5 tests in calculator.Calculator.accum\n",
+                        "   5 tests in calculator.Calculator.add\n",
+                        "   6 tests in calculator.Calculator.divide\n",
+                        "   3 tests in calculator.Calculator.is_input_valid\n",
+                        "   6 tests in calculator.Calculator.multiply\n",
+                        "   4 tests in calculator.Calculator.root\n",
+                        "   5 tests in calculator.Calculator.subtract\n",
+                        "34 tests in 10 items.\n",
+                        "34 passed and 0 failed.\n",
+                        "Test passed.\n"
+                    ]
+                }
+            ],
             "source": [
                 "# run doctest on calculator.py\n",
                 "!python -m doctest -v C:\\Users\\abayomi\\Desktop\\olilesa-DWWP.1\\calculator_olu_ile\\calculator.py"
             ]
         },
         {
             "cell_type": "markdown",
@@ -360,15 +480,15 @@
             },
             "source": [
                 "## Execute pytest"
             ]
         },
         {
             "cell_type": "code",
-            "execution_count": 18,
+            "execution_count": 39,
             "id": "38rtKR0SkcyA",
             "metadata": {
                 "colab": {
                     "base_uri": "https://localhost:8080/"
                 },
                 "id": "38rtKR0SkcyA",
                 "outputId": "b7ea8200-fa58-4eac-812e-3853e16dfdac"
@@ -416,52 +536,66 @@
             "metadata": {},
             "source": [
                 "## Calculator package installation"
             ]
         },
         {
             "cell_type": "code",
-            "execution_count": null,
+            "execution_count": 40,
             "id": "9c413373",
-            "metadata": {
-                "pycharm": {
-                    "is_executing": true
+            "metadata": {},
+            "outputs": [
+                {
+                    "name": "stdout",
+                    "output_type": "stream",
+                    "text": [
+                        "Requirement already satisfied: calculator_olu_ile in c:\\users\\abayomi\\appdata\\local\\programs\\python\\python38\\lib\\site-packages (0.2.0)\n"
+                    ]
                 }
-            },
-            "outputs": [],
+            ],
             "source": [
-                "!pip install calculator_olu_ile"
+                "!pip install --upgrade calculator_olu_ile"
             ]
         },
         {
             "cell_type": "markdown",
             "id": "dyL5vICrWKY5",
             "metadata": {
                 "id": "dyL5vICrWKY5"
             },
             "source": [
                 "## Calculator package import/use"
             ]
         },
         {
             "cell_type": "code",
-            "execution_count": null,
+            "execution_count": 41,
             "id": "pt1UGk57tueJ",
             "metadata": {
-                "id": "pt1UGk57tueJ",
-                "pycharm": {
-                    "is_executing": true
-                }
+                "id": "pt1UGk57tueJ"
             },
-            "outputs": [],
+            "outputs": [
+                {
+                    "name": "stdout",
+                    "output_type": "stream",
+                    "text": [
+                        "=============== Calculator ==================\n",
+                        "\n",
+                        "Calculators current result:  4\n",
+                        "\n"
+                    ]
+                }
+            ],
             "source": [
                 "from calculator_olu_ile.calculator import Calculator\n",
-                "cap = Calculator()\n",
-                "cap.add(2)\n",
-                "print(cap.accum_state)"
+                "cal = Calculator()\n",
+                "cal.add(2)\n",
+                "cal.add(2)\n",
+                "print('='*15, 'Calculator', '='*18, end='\\n\\n')\n",
+                "print('Calculators current result: ', cal.accum, end='\\n\\n')"
             ]
         }
     ],
     "metadata": {
         "colab": {
             "provenance": []
         },
```

### Comparing `calculator_olu_ile-0.2.0/LICENSE` & `calculator_olu_ile-0.2.1/LICENSE`

 * *Files identical despite different names*

### Comparing `calculator_olu_ile-0.2.0/README.md` & `calculator_olu_ile-0.2.1/README.md`

 * *Files identical despite different names*

### Comparing `calculator_olu_ile-0.2.0/calculator_olu_ile/calculator.py` & `calculator_olu_ile-0.2.1/calculator_olu_ile/calculator.py`

 * *Files 2% similar despite different names*

```diff
@@ -80,42 +80,42 @@
             1.0
         """
         if self.is_input_valid(num):
             self.__accum /= num
         else:
             raise NoneNumericValueError(num)
 
-    def root(self, pow: Union[int]) -> None:
+    def root(self, pwr: Union[int]) -> None:
         """find root of number.
-           if num has an invalid value eg string then raise an exception.
+           if num has an invalid value .eg string then raise an exception.
 
         For example:
             >>> cal = Calculator()
             >>> cal.accum = 9
             >>> cal.root(2)
             >>> print(cal.accum)
             3.0
         """
-        if self.is_input_valid(pow):
-            self.__accum = self.__accum ** (1 / pow)
+        if self.is_input_valid(pwr):
+            self.__accum = self.__accum ** (1 / pwr)
         else:
-            raise NoneNumericValueError(pow)
+            raise NoneNumericValueError(pwr)
 
     @property
     def accum(self) -> Union[int, float]:
         """
         getter: gets current state/value of accumulator
 
         For example:
             >>> cal = Calculator()
             >>> print(cal.accum)
             0
 
         setter: sets the state of the accumulator
-                if num has an invalid value eg string then raise an exception
+                if num has an invalid value .eg string then raise an exception
 
         For example:
             >>> cal = Calculator()
             >>> cal.accum = 5
             >>> print(cal.accum)
             5
         """
@@ -135,8 +135,8 @@
         For example:
             >>> cal = Calculator()
             >>> print(cal.is_input_valid("text"))
             False
             >>> print(cal.is_input_valid(6))
             True
         """
-        return True if type(num) == int or type(num) == float else False
+        return isinstance(num, (int, float))
```

### Comparing `calculator_olu_ile-0.2.0/tests/calculator_test.py` & `calculator_olu_ile-0.2.1/tests/calculator_test.py`

 * *Files identical despite different names*

### Comparing `calculator_olu_ile-0.2.0/PKG-INFO` & `calculator_olu_ile-0.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: calculator_olu_ile
-Version: 0.2.0
+Version: 0.2.1
 Summary: Calculator with operations add, subtract, divide, multipy and root.
 Author-email: Oluwole Ilesanmi <oluwoleilesanmi@gmail.com>
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
 Classifier: License :: OSI Approved :: MIT License
 
 # Calculator
```

