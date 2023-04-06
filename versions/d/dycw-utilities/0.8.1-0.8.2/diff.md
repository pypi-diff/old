# Comparing `tmp/dycw_utilities-0.8.1.tar.gz` & `tmp/dycw_utilities-0.8.2.tar.gz`

## Comparing `dycw_utilities-0.8.1.tar` & `dycw_utilities-0.8.2.tar`

### file list

```diff
@@ -1,222 +1,222 @@
--rw-r--r--   0        0        0       20 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/.envrc
--rw-r--r--   0        0        0     1780 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/.pre-commit-config.yaml
--rw-r--r--   0        0        0       17 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/.rgiginore
--rw-r--r--   0        0        0      101 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/Makefile
--rw-r--r--   0        0        0       28 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/conftest.py
--rw-r--r--   0        0        0      631 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/noxfile.py
--rw-r--r--   0        0        0     8808 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/requirements-dev.txt
--rw-r--r--   0        0        0      268 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/requirements.txt
--rw-r--r--   0        0        0      599 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/.github/workflows/pull-request.yml
--rw-r--r--   0        0        0     1061 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/.github/workflows/push.yml
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/__init__.py
--rw-r--r--   0        0        0      492 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/conftest.py
--rw-r--r--   0        0        0      561 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_airium.py
--rw-r--r--   0        0        0     3129 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_atomicwrites.py
--rw-r--r--   0        0        0      933 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_beartype.py
--rw-r--r--   0        0        0      659 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_bidict.py
--rw-r--r--   0        0        0      712 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_class_name.py
--rw-r--r--   0        0        0     2423 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_clean_dir.py
--rw-r--r--   0        0        0      685 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_cryptography.py
--rw-r--r--   0        0        0    12950 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_cvxpy.py
--rw-r--r--   0        0        0    11722 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_datetime.py
--rw-r--r--   0        0        0     2071 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_email.py
--rw-r--r--   0        0        0     2298 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_enum.py
--rw-r--r--   0        0        0      999 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_errors.py
--rw-r--r--   0        0        0      528 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_fastapi.py
--rw-r--r--   0        0        0     9283 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_fastparquet.py
--rw-r--r--   0        0        0      723 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_fpdf2.py
--rw-r--r--   0        0        0      123 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_getpass.py
--rw-r--r--   0        0        0      792 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_git.py
--rw-r--r--   0        0        0      602 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_hashlib.py
--rw-r--r--   0        0        0      236 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_hatch.py
--rw-r--r--   0        0        0     1017 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_iterables.py
--rw-r--r--   0        0        0     1080 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_json.py
--rw-r--r--   0        0        0      402 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_logging.py
--rw-r--r--   0        0        0      493 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_memory_profiler.py
--rw-r--r--   0        0        0     3353 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_modules.py
--rw-r--r--   0        0        0      855 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_monitor_memory.py
--rw-r--r--   0        0        0      638 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_more_itertools.py
--rw-r--r--   0        0        0     1370 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_os.py
--rw-r--r--   0        0        0     1263 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_pathlib.py
--rw-r--r--   0        0        0      821 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_pickle.py
--rw-r--r--   0        0        0     2712 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_pqdm.py
--rw-r--r--   0        0        0      349 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_pyinstrument.py
--rw-r--r--   0        0        0     1413 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_pypi_server.py
--rw-r--r--   0        0        0     5473 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_pytest.py
--rw-r--r--   0        0        0     1208 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_pytest_check.py
--rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_random.py
--rw-r--r--   0        0        0     1946 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_re.py
--rw-r--r--   0        0        0     1512 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_scipy.py
--rw-r--r--   0        0        0      483 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_semver.py
--rw-r--r--   0        0        0      482 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_sentinel.py
--rw-r--r--   0        0        0      134 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_socket.py
--rw-r--r--   0        0        0     2212 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_subprocess.py
--rw-r--r--   0        0        0      348 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_sys.py
--rw-r--r--   0        0        0      789 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_tempfile.py
--rw-r--r--   0        0        0     1834 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_text.py
--rw-r--r--   0        0        0     1885 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_timer.py
--rw-r--r--   0        0        0     1194 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_tqdm.py
--rw-r--r--   0        0        0     6372 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_typed_settings.py
--rw-r--r--   0        0        0     1327 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_types.py
--rw-r--r--   0        0        0      445 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_typing.py
--rw-r--r--   0        0        0     2463 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_warnings.py
--rw-r--r--   0        0        0     1003 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_zipfile.py
--rw-r--r--   0        0        0      171 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/test_zoneinfo.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/attrs/__init__.py
--rw-r--r--   0        0        0     2383 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/attrs/test_attrs.py
--rw-r--r--   0        0        0      938 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/attrs/test_xarray.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/click/__init__.py
--rw-r--r--   0        0        0     4523 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/click/test_click.py
--rw-r--r--   0        0        0     1925 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/click/test_luigi.py
--rw-r--r--   0        0        0     1437 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/click/test_sqlalchemy.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/holoviews/__init__.py
--rw-r--r--   0        0        0      586 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/holoviews/test_holoviews.py
--rw-r--r--   0        0        0     1927 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/holoviews/test_xarray.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/hypothesis/__init__.py
--rw-r--r--   0        0        0    10520 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/hypothesis/test_hypothesis.py
--rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/hypothesis/test_luigi.py
--rw-r--r--   0        0        0     6826 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/hypothesis/test_numpy.py
--rw-r--r--   0        0        0     4351 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/hypothesis/test_pandas.py
--rw-r--r--   0        0        0     1753 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/hypothesis/test_semver.py
--rw-r--r--   0        0        0     1691 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/hypothesis/test_sqlalchemy.py
--rw-r--r--   0        0        0     6672 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/hypothesis/test_xarray.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/loguru/__init__.py
--rw-r--r--   0        0        0     1697 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/loguru/script_to_test_luigi.py
--rw-r--r--   0        0        0     5014 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/loguru/test_loguru.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/luigi/__init__.py
--rw-r--r--   0        0        0     8140 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/luigi/test_attrs.py
--rw-r--r--   0        0        0     8449 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/luigi/test_luigi.py
--rw-r--r--   0        0        0      411 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/luigi/test_semver.py
--rw-r--r--   0        0        0      820 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/luigi/test_server.py
--rw-r--r--   0        0        0     2028 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/luigi/test_sqlalchemy.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/math/__init__.py
--rw-r--r--   0        0        0    16876 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/math/test_math.py
--rw-r--r--   0        0        0     2598 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/math/test_typing.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/__init__.py
--rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/standalone.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/package_with/__init__.py
--rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/package_with/outer_1.py
--rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/package_with/outer_2.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/package_with/subpackage/__init__.py
--rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/package_with/subpackage/inner_1.py
--rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/package_with/subpackage/inner_2.py
--rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/package_with/subpackage/inner_3.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/package_without/__init__.py
--rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/package_without/module_1.py
--rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/modules/package_without/module_2.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/numpy/__init__.py
--rw-r--r--   0        0        0    43715 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/numpy/test_numpy.py
--rw-r--r--   0        0        0    16201 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/numpy/test_typing.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/pandas/__init__.py
--rw-r--r--   0        0        0    10922 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/pandas/test_pandas.py
--rw-r--r--   0        0        0     1912 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/pandas/test_typing.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/sqlalchemy/__init__.py
--rw-r--r--   0        0        0     1508 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/sqlalchemy/test_fastparquet.py
--rw-r--r--   0        0        0    14095 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/sqlalchemy/test_pandas.py
--rw-r--r--   0        0        0    38826 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/sqlalchemy/test_sqlalchemy.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/xarray/__init__.py
--rw-r--r--   0        0        0     2756 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/xarray/test_typing.py
--rw-r--r--   0        0        0      182 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/xarray/test_xarray.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/zarr/__init__.py
--rw-r--r--   0        0        0     7324 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/zarr/test_xarray.py
--rw-r--r--   0        0        0    10301 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/tests/zarr/test_zarr.py
--rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/__init__.py
--rw-r--r--   0        0        0      410 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/airium.py
--rw-r--r--   0        0        0     1223 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/atomicwrites.py
--rw-r--r--   0        0        0      338 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/beartype.py
--rw-r--r--   0        0        0      696 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/bidict.py
--rw-r--r--   0        0        0      321 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/class_name.py
--rw-r--r--   0        0        0      793 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/cryptography.py
--rw-r--r--   0        0        0     9151 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/cvxpy.py
--rw-r--r--   0        0        0     7475 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/datetime.py
--rw-r--r--   0        0        0     2166 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/email.py
--rw-r--r--   0        0        0     1767 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/enum.py
--rw-r--r--   0        0        0      719 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/errors.py
--rw-r--r--   0        0        0      746 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/fastapi.py
--rw-r--r--   0        0        0     6479 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/fastparquet.py
--rw-r--r--   0        0        0     2190 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/fpdf2.py
--rw-r--r--   0        0        0       46 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/getpass.py
--rw-r--r--   0        0        0     1479 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/git.py
--rw-r--r--   0        0        0      393 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/hashlib.py
--rw-r--r--   0        0        0      592 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/hatch.py
--rw-r--r--   0        0        0      737 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/iterables.py
--rw-r--r--   0        0        0     1254 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/json.py
--rw-r--r--   0        0        0      566 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/logging.py
--rw-r--r--   0        0        0     6924 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/loguru.py
--rw-r--r--   0        0        0      881 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/memory_profiler.py
--rw-r--r--   0        0        0     2279 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/modules.py
--rw-r--r--   0        0        0      920 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/more_itertools.py
--rw-r--r--   0        0        0     1278 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/os.py
--rw-r--r--   0        0        0      501 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/pathlib.py
--rw-r--r--   0        0        0      588 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/pickle.py
--rw-r--r--   0        0        0     8490 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/pqdm.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/py.typed
--rw-r--r--   0        0        0      706 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/pyinstrument.py
--rw-r--r--   0        0        0     3526 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/pytest.py
--rw-r--r--   0        0        0      402 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/pytest_check.py
--rw-r--r--   0        0        0       64 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/random.py
--rw-r--r--   0        0        0     1403 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/re.py
--rw-r--r--   0        0        0     1053 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/scipy.py
--rw-r--r--   0        0        0      282 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/semver.py
--rw-r--r--   0        0        0      599 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/sentinel.py
--rw-r--r--   0        0        0       57 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/socket.py
--rw-r--r--   0        0        0     2961 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/subprocess.py
--rw-r--r--   0        0        0      147 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/sys.py
--rw-r--r--   0        0        0      920 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/tempfile.py
--rw-r--r--   0        0        0      947 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/text.py
--rw-r--r--   0        0        0     2150 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/timer.py
--rw-r--r--   0        0        0     4292 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/tqdm.py
--rw-r--r--   0        0        0     5853 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/typed_settings.py
--rw-r--r--   0        0        0      516 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/types.py
--rw-r--r--   0        0        0      299 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/typing.py
--rw-r--r--   0        0        0     1678 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/warnings.py
--rw-r--r--   0        0        0      601 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/zipfile.py
--rw-r--r--   0        0        0       70 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/zoneinfo.py
--rw-r--r--   0        0        0     1384 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/attrs/__init__.py
--rw-r--r--   0        0        0      362 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/attrs/xarray.py
--rw-r--r--   0        0        0     3616 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/clean_dir/__init__.py
--rw-r--r--   0        0        0      116 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/clean_dir/__main__.py
--rw-r--r--   0        0        0      845 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/clean_dir/classes.py
--rw-r--r--   0        0        0     3123 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/click/__init__.py
--rw-r--r--   0        0        0      566 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/click/luigi.py
--rw-r--r--   0        0        0      621 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/click/sqlalchemy.py
--rw-r--r--   0        0        0      701 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/holoviews/__init__.py
--rw-r--r--   0        0        0     1510 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/holoviews/xarray.py
--rw-r--r--   0        0        0     9369 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/hypothesis/__init__.py
--rw-r--r--   0        0        0      426 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/hypothesis/luigi.py
--rw-r--r--   0        0        0     5186 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/hypothesis/numpy.py
--rw-r--r--   0        0        0     4448 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/hypothesis/pandas.py
--rw-r--r--   0        0        0     2533 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/hypothesis/semver.py
--rw-r--r--   0        0        0      797 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/hypothesis/sqlalchemy.py
--rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/hypothesis/typing.py
--rw-r--r--   0        0        0     6071 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/hypothesis/xarray.py
--rw-r--r--   0        0        0    11310 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/luigi/__init__.py
--rw-r--r--   0        0        0     6928 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/luigi/attrs.py
--rw-r--r--   0        0        0      701 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/luigi/semver.py
--rw-r--r--   0        0        0     1898 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/luigi/sqlalchemy.py
--rw-r--r--   0        0        0     1636 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/luigi/server/__init__.py
--rw-r--r--   0        0        0      119 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/luigi/server/__main__.py
--rw-r--r--   0        0        0      810 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/luigi/server/classes.py
--rw-r--r--   0        0        0     2171 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/math/__init__.py
--rw-r--r--   0        0        0    14378 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/math/typing.py
--rw-r--r--   0        0        0     2853 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/monitor_memory/__init__.py
--rw-r--r--   0        0        0      121 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/monitor_memory/__main__.py
--rw-r--r--   0        0        0     1116 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/monitor_memory/classes.py
--rw-r--r--   0        0        0    16442 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/numpy/__init__.py
--rw-r--r--   0        0        0    29381 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/numpy/typing.py
--rw-r--r--   0        0        0     6650 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/pandas/__init__.py
--rw-r--r--   0        0        0     1876 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/pandas/typing.py
--rw-r--r--   0        0        0     1887 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/pypi_server/__init__.py
--rw-r--r--   0        0        0      118 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/pypi_server/__main__.py
--rw-r--r--   0        0        0      753 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/pypi_server/classes.py
--rw-r--r--   0        0        0    25497 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/sqlalchemy/__init__.py
--rw-r--r--   0        0        0     1331 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/sqlalchemy/fastparquet.py
--rw-r--r--   0        0        0    10357 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/sqlalchemy/pandas.py
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/xarray/__init__.py
--rw-r--r--   0        0        0     2036 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/xarray/typing.py
--rw-r--r--   0        0        0    10192 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/zarr/__init__.py
--rw-r--r--   0        0        0     5074 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/utilities/zarr/xarray.py
--rw-r--r--   0        0        0     3127 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/.gitignore
--rw-r--r--   0        0        0     1628 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/README.md
--rw-r--r--   0        0        0     7921 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/pyproject.toml
--rw-r--r--   0        0        0     9135 2020-02-02 00:00:00.000000 dycw_utilities-0.8.1/PKG-INFO
+-rw-r--r--   0        0        0       20 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/.envrc
+-rw-r--r--   0        0        0     1780 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/.pre-commit-config.yaml
+-rw-r--r--   0        0        0       17 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/.rgiginore
+-rw-r--r--   0        0        0      101 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/Makefile
+-rw-r--r--   0        0        0       28 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/conftest.py
+-rw-r--r--   0        0        0      631 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/noxfile.py
+-rw-r--r--   0        0        0     8808 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/requirements-dev.txt
+-rw-r--r--   0        0        0      268 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/requirements.txt
+-rw-r--r--   0        0        0      599 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/.github/workflows/pull-request.yml
+-rw-r--r--   0        0        0     1061 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/.github/workflows/push.yml
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/__init__.py
+-rw-r--r--   0        0        0      492 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/conftest.py
+-rw-r--r--   0        0        0      561 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_airium.py
+-rw-r--r--   0        0        0     3129 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_atomicwrites.py
+-rw-r--r--   0        0        0      933 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_beartype.py
+-rw-r--r--   0        0        0      659 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_bidict.py
+-rw-r--r--   0        0        0      712 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_class_name.py
+-rw-r--r--   0        0        0     2423 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_clean_dir.py
+-rw-r--r--   0        0        0      685 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_cryptography.py
+-rw-r--r--   0        0        0    12950 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_cvxpy.py
+-rw-r--r--   0        0        0    11722 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_datetime.py
+-rw-r--r--   0        0        0     2071 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_email.py
+-rw-r--r--   0        0        0     2298 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_enum.py
+-rw-r--r--   0        0        0      999 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_errors.py
+-rw-r--r--   0        0        0      528 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_fastapi.py
+-rw-r--r--   0        0        0     9283 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_fastparquet.py
+-rw-r--r--   0        0        0      723 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_fpdf2.py
+-rw-r--r--   0        0        0      123 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_getpass.py
+-rw-r--r--   0        0        0      792 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_git.py
+-rw-r--r--   0        0        0      602 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_hashlib.py
+-rw-r--r--   0        0        0      236 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_hatch.py
+-rw-r--r--   0        0        0     1017 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_iterables.py
+-rw-r--r--   0        0        0     1080 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_json.py
+-rw-r--r--   0        0        0      402 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_logging.py
+-rw-r--r--   0        0        0      493 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_memory_profiler.py
+-rw-r--r--   0        0        0     3353 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_modules.py
+-rw-r--r--   0        0        0      855 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_monitor_memory.py
+-rw-r--r--   0        0        0      638 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_more_itertools.py
+-rw-r--r--   0        0        0     1370 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_os.py
+-rw-r--r--   0        0        0     1263 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_pathlib.py
+-rw-r--r--   0        0        0      821 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_pickle.py
+-rw-r--r--   0        0        0     2712 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_pqdm.py
+-rw-r--r--   0        0        0      349 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_pyinstrument.py
+-rw-r--r--   0        0        0     1413 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_pypi_server.py
+-rw-r--r--   0        0        0     5473 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_pytest.py
+-rw-r--r--   0        0        0     1208 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_pytest_check.py
+-rw-r--r--   0        0        0      190 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_random.py
+-rw-r--r--   0        0        0     1946 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_re.py
+-rw-r--r--   0        0        0     1512 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_scipy.py
+-rw-r--r--   0        0        0      483 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_semver.py
+-rw-r--r--   0        0        0      482 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_sentinel.py
+-rw-r--r--   0        0        0      134 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_socket.py
+-rw-r--r--   0        0        0     2212 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_subprocess.py
+-rw-r--r--   0        0        0      348 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_sys.py
+-rw-r--r--   0        0        0      789 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_tempfile.py
+-rw-r--r--   0        0        0     1834 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_text.py
+-rw-r--r--   0        0        0     1885 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_timer.py
+-rw-r--r--   0        0        0     1194 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_tqdm.py
+-rw-r--r--   0        0        0     6372 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_typed_settings.py
+-rw-r--r--   0        0        0     1327 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_types.py
+-rw-r--r--   0        0        0      445 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_typing.py
+-rw-r--r--   0        0        0     2463 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_warnings.py
+-rw-r--r--   0        0        0     1003 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_zipfile.py
+-rw-r--r--   0        0        0      171 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/test_zoneinfo.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/attrs/__init__.py
+-rw-r--r--   0        0        0     2383 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/attrs/test_attrs.py
+-rw-r--r--   0        0        0      938 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/attrs/test_xarray.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/click/__init__.py
+-rw-r--r--   0        0        0     4523 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/click/test_click.py
+-rw-r--r--   0        0        0     1925 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/click/test_luigi.py
+-rw-r--r--   0        0        0     1437 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/click/test_sqlalchemy.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/holoviews/__init__.py
+-rw-r--r--   0        0        0      586 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/holoviews/test_holoviews.py
+-rw-r--r--   0        0        0     1927 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/holoviews/test_xarray.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/hypothesis/__init__.py
+-rw-r--r--   0        0        0    10520 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/hypothesis/test_hypothesis.py
+-rw-r--r--   0        0        0      709 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/hypothesis/test_luigi.py
+-rw-r--r--   0        0        0     9985 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/hypothesis/test_numpy.py
+-rw-r--r--   0        0        0     4351 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/hypothesis/test_pandas.py
+-rw-r--r--   0        0        0     1753 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/hypothesis/test_semver.py
+-rw-r--r--   0        0        0     1691 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/hypothesis/test_sqlalchemy.py
+-rw-r--r--   0        0        0     6672 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/hypothesis/test_xarray.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/loguru/__init__.py
+-rw-r--r--   0        0        0     1697 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/loguru/script_to_test_luigi.py
+-rw-r--r--   0        0        0     5014 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/loguru/test_loguru.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/luigi/__init__.py
+-rw-r--r--   0        0        0     8140 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/luigi/test_attrs.py
+-rw-r--r--   0        0        0     8449 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/luigi/test_luigi.py
+-rw-r--r--   0        0        0      411 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/luigi/test_semver.py
+-rw-r--r--   0        0        0      820 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/luigi/test_server.py
+-rw-r--r--   0        0        0     2028 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/luigi/test_sqlalchemy.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/math/__init__.py
+-rw-r--r--   0        0        0    16876 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/math/test_math.py
+-rw-r--r--   0        0        0     2598 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/math/test_typing.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/__init__.py
+-rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/standalone.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/package_with/__init__.py
+-rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/package_with/outer_1.py
+-rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/package_with/outer_2.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/package_with/subpackage/__init__.py
+-rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/package_with/subpackage/inner_1.py
+-rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/package_with/subpackage/inner_2.py
+-rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/package_with/subpackage/inner_3.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/package_without/__init__.py
+-rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/package_without/module_1.py
+-rw-r--r--   0        0        0      220 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/modules/package_without/module_2.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/numpy/__init__.py
+-rw-r--r--   0        0        0    45512 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/numpy/test_numpy.py
+-rw-r--r--   0        0        0    16201 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/numpy/test_typing.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/pandas/__init__.py
+-rw-r--r--   0        0        0    10922 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/pandas/test_pandas.py
+-rw-r--r--   0        0        0     1912 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/pandas/test_typing.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/sqlalchemy/__init__.py
+-rw-r--r--   0        0        0     1508 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/sqlalchemy/test_fastparquet.py
+-rw-r--r--   0        0        0    14095 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/sqlalchemy/test_pandas.py
+-rw-r--r--   0        0        0    38826 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/sqlalchemy/test_sqlalchemy.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/xarray/__init__.py
+-rw-r--r--   0        0        0     2756 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/xarray/test_typing.py
+-rw-r--r--   0        0        0      182 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/xarray/test_xarray.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/zarr/__init__.py
+-rw-r--r--   0        0        0     7324 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/zarr/test_xarray.py
+-rw-r--r--   0        0        0    10301 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/tests/zarr/test_zarr.py
+-rw-r--r--   0        0        0       22 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/__init__.py
+-rw-r--r--   0        0        0      410 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/airium.py
+-rw-r--r--   0        0        0     1223 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/atomicwrites.py
+-rw-r--r--   0        0        0      338 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/beartype.py
+-rw-r--r--   0        0        0      696 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/bidict.py
+-rw-r--r--   0        0        0      321 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/class_name.py
+-rw-r--r--   0        0        0      793 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/cryptography.py
+-rw-r--r--   0        0        0     9151 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/cvxpy.py
+-rw-r--r--   0        0        0     7475 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/datetime.py
+-rw-r--r--   0        0        0     2166 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/email.py
+-rw-r--r--   0        0        0     1767 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/enum.py
+-rw-r--r--   0        0        0      719 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/errors.py
+-rw-r--r--   0        0        0      746 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/fastapi.py
+-rw-r--r--   0        0        0     6479 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/fastparquet.py
+-rw-r--r--   0        0        0     2190 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/fpdf2.py
+-rw-r--r--   0        0        0       46 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/getpass.py
+-rw-r--r--   0        0        0     1479 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/git.py
+-rw-r--r--   0        0        0      393 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/hashlib.py
+-rw-r--r--   0        0        0      592 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/hatch.py
+-rw-r--r--   0        0        0      737 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/iterables.py
+-rw-r--r--   0        0        0     1254 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/json.py
+-rw-r--r--   0        0        0      566 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/logging.py
+-rw-r--r--   0        0        0     6924 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/loguru.py
+-rw-r--r--   0        0        0      881 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/memory_profiler.py
+-rw-r--r--   0        0        0     2279 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/modules.py
+-rw-r--r--   0        0        0      920 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/more_itertools.py
+-rw-r--r--   0        0        0     1278 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/os.py
+-rw-r--r--   0        0        0      501 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/pathlib.py
+-rw-r--r--   0        0        0      588 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/pickle.py
+-rw-r--r--   0        0        0     8490 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/pqdm.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/py.typed
+-rw-r--r--   0        0        0      706 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/pyinstrument.py
+-rw-r--r--   0        0        0     3526 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/pytest.py
+-rw-r--r--   0        0        0      402 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/pytest_check.py
+-rw-r--r--   0        0        0       64 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/random.py
+-rw-r--r--   0        0        0     1403 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/re.py
+-rw-r--r--   0        0        0     1053 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/scipy.py
+-rw-r--r--   0        0        0      282 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/semver.py
+-rw-r--r--   0        0        0      599 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/sentinel.py
+-rw-r--r--   0        0        0       57 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/socket.py
+-rw-r--r--   0        0        0     2961 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/subprocess.py
+-rw-r--r--   0        0        0      147 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/sys.py
+-rw-r--r--   0        0        0      920 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/tempfile.py
+-rw-r--r--   0        0        0      947 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/text.py
+-rw-r--r--   0        0        0     2150 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/timer.py
+-rw-r--r--   0        0        0     4292 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/tqdm.py
+-rw-r--r--   0        0        0     5853 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/typed_settings.py
+-rw-r--r--   0        0        0      516 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/types.py
+-rw-r--r--   0        0        0      299 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/typing.py
+-rw-r--r--   0        0        0     1678 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/warnings.py
+-rw-r--r--   0        0        0      601 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/zipfile.py
+-rw-r--r--   0        0        0       70 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/zoneinfo.py
+-rw-r--r--   0        0        0     1384 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/attrs/__init__.py
+-rw-r--r--   0        0        0      362 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/attrs/xarray.py
+-rw-r--r--   0        0        0     3616 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/clean_dir/__init__.py
+-rw-r--r--   0        0        0      116 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/clean_dir/__main__.py
+-rw-r--r--   0        0        0      845 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/clean_dir/classes.py
+-rw-r--r--   0        0        0     3123 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/click/__init__.py
+-rw-r--r--   0        0        0      566 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/click/luigi.py
+-rw-r--r--   0        0        0      621 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/click/sqlalchemy.py
+-rw-r--r--   0        0        0      701 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/holoviews/__init__.py
+-rw-r--r--   0        0        0     1510 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/holoviews/xarray.py
+-rw-r--r--   0        0        0     9369 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/hypothesis/__init__.py
+-rw-r--r--   0        0        0      426 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/hypothesis/luigi.py
+-rw-r--r--   0        0        0     8800 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/hypothesis/numpy.py
+-rw-r--r--   0        0        0     4448 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/hypothesis/pandas.py
+-rw-r--r--   0        0        0     2533 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/hypothesis/semver.py
+-rw-r--r--   0        0        0      797 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/hypothesis/sqlalchemy.py
+-rw-r--r--   0        0        0      194 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/hypothesis/typing.py
+-rw-r--r--   0        0        0     6071 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/hypothesis/xarray.py
+-rw-r--r--   0        0        0    11310 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/luigi/__init__.py
+-rw-r--r--   0        0        0     6928 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/luigi/attrs.py
+-rw-r--r--   0        0        0      701 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/luigi/semver.py
+-rw-r--r--   0        0        0     1898 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/luigi/sqlalchemy.py
+-rw-r--r--   0        0        0     1636 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/luigi/server/__init__.py
+-rw-r--r--   0        0        0      119 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/luigi/server/__main__.py
+-rw-r--r--   0        0        0      810 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/luigi/server/classes.py
+-rw-r--r--   0        0        0     2171 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/math/__init__.py
+-rw-r--r--   0        0        0    14378 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/math/typing.py
+-rw-r--r--   0        0        0     2853 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/monitor_memory/__init__.py
+-rw-r--r--   0        0        0      121 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/monitor_memory/__main__.py
+-rw-r--r--   0        0        0     1116 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/monitor_memory/classes.py
+-rw-r--r--   0        0        0    17246 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/numpy/__init__.py
+-rw-r--r--   0        0        0    29381 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/numpy/typing.py
+-rw-r--r--   0        0        0     6650 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/pandas/__init__.py
+-rw-r--r--   0        0        0     1876 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/pandas/typing.py
+-rw-r--r--   0        0        0     1887 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/pypi_server/__init__.py
+-rw-r--r--   0        0        0      118 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/pypi_server/__main__.py
+-rw-r--r--   0        0        0      753 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/pypi_server/classes.py
+-rw-r--r--   0        0        0    25497 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/sqlalchemy/__init__.py
+-rw-r--r--   0        0        0     1331 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/sqlalchemy/fastparquet.py
+-rw-r--r--   0        0        0    10357 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/sqlalchemy/pandas.py
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/xarray/__init__.py
+-rw-r--r--   0        0        0     2036 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/xarray/typing.py
+-rw-r--r--   0        0        0    10192 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/zarr/__init__.py
+-rw-r--r--   0        0        0     5074 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/utilities/zarr/xarray.py
+-rw-r--r--   0        0        0     3127 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/.gitignore
+-rw-r--r--   0        0        0     1628 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/README.md
+-rw-r--r--   0        0        0     7921 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/pyproject.toml
+-rw-r--r--   0        0        0     9135 2020-02-02 00:00:00.000000 dycw_utilities-0.8.2/PKG-INFO
```

### Comparing `dycw_utilities-0.8.1/.pre-commit-config.yaml` & `dycw_utilities-0.8.2/.pre-commit-config.yaml`

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 repos:
   # fixers
   - repo: https://github.com/charliermarsh/ruff-pre-commit
-    rev: v0.0.260
+    rev: v0.0.261
     hooks:
       - id: ruff
         args: [--fix]
   - repo: https://github.com/dycw/pre-commit-hooks
     rev: 0.8.23
     hooks:
       - id: run-hatch-version
```

### Comparing `dycw_utilities-0.8.1/noxfile.py` & `dycw_utilities-0.8.2/noxfile.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/requirements-dev.txt` & `dycw_utilities-0.8.2/requirements-dev.txt`

 * *Files 1% similar despite different names*

```diff
@@ -329,25 +329,25 @@
     # via osqp
 requests==2.28.2
     # via panel
 rfc3986[idna2008]==1.5.0
     # via httpx
 rich==13.3.3
     # via hatch
-ruff==0.0.260
+ruff==0.0.261
     # via dycw-utilities (pyproject.toml)
 scipy==1.10.1
     # via
     #   cvxpy
     #   dycw-utilities (pyproject.toml)
     #   ecos
     #   osqp
     #   qdldl
     #   scs
-scs==3.2.2
+scs==3.2.3
     # via cvxpy
 secretstorage==3.3.3
     # via keyring
 selenium==4.8.3
     # via dycw-utilities (pyproject.toml)
 semver==3.0.0
     # via dycw-utilities (pyproject.toml)
@@ -363,15 +363,15 @@
     #   httpcore
     #   httpx
     #   trio
 sortedcontainers==2.4.0
     # via
     #   hypothesis
     #   trio
-sqlalchemy==2.0.8
+sqlalchemy==2.0.9
     # via
     #   dycw-utilities (pyproject.toml)
     #   hypothesis-sqlalchemy
 starlette==0.26.1
     # via fastapi
 tenacity==8.2.2
     # via luigi
```

### Comparing `dycw_utilities-0.8.1/.github/workflows/pull-request.yml` & `dycw_utilities-0.8.2/.github/workflows/pull-request.yml`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/.github/workflows/push.yml` & `dycw_utilities-0.8.2/.github/workflows/push.yml`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_airium.py` & `dycw_utilities-0.8.2/tests/test_airium.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_atomicwrites.py` & `dycw_utilities-0.8.2/tests/test_atomicwrites.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_beartype.py` & `dycw_utilities-0.8.2/tests/test_beartype.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_bidict.py` & `dycw_utilities-0.8.2/tests/test_bidict.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_class_name.py` & `dycw_utilities-0.8.2/tests/test_class_name.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_clean_dir.py` & `dycw_utilities-0.8.2/tests/test_clean_dir.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_cryptography.py` & `dycw_utilities-0.8.2/tests/test_cryptography.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_cvxpy.py` & `dycw_utilities-0.8.2/tests/test_cvxpy.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_datetime.py` & `dycw_utilities-0.8.2/tests/test_datetime.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_email.py` & `dycw_utilities-0.8.2/tests/test_email.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_enum.py` & `dycw_utilities-0.8.2/tests/test_enum.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_errors.py` & `dycw_utilities-0.8.2/tests/test_errors.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_fastapi.py` & `dycw_utilities-0.8.2/tests/test_fastapi.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_fastparquet.py` & `dycw_utilities-0.8.2/tests/test_fastparquet.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_fpdf2.py` & `dycw_utilities-0.8.2/tests/test_fpdf2.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_git.py` & `dycw_utilities-0.8.2/tests/test_git.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_hashlib.py` & `dycw_utilities-0.8.2/tests/test_hashlib.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_iterables.py` & `dycw_utilities-0.8.2/tests/test_iterables.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_json.py` & `dycw_utilities-0.8.2/tests/test_json.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_modules.py` & `dycw_utilities-0.8.2/tests/test_modules.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_monitor_memory.py` & `dycw_utilities-0.8.2/tests/test_monitor_memory.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_more_itertools.py` & `dycw_utilities-0.8.2/tests/test_more_itertools.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_os.py` & `dycw_utilities-0.8.2/tests/test_os.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_pathlib.py` & `dycw_utilities-0.8.2/tests/test_pathlib.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_pickle.py` & `dycw_utilities-0.8.2/tests/test_pickle.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_pqdm.py` & `dycw_utilities-0.8.2/tests/test_pqdm.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_pypi_server.py` & `dycw_utilities-0.8.2/tests/test_pypi_server.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_pytest.py` & `dycw_utilities-0.8.2/tests/test_pytest.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_pytest_check.py` & `dycw_utilities-0.8.2/tests/test_pytest_check.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_re.py` & `dycw_utilities-0.8.2/tests/test_re.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_scipy.py` & `dycw_utilities-0.8.2/tests/test_scipy.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_subprocess.py` & `dycw_utilities-0.8.2/tests/test_subprocess.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_tempfile.py` & `dycw_utilities-0.8.2/tests/test_tempfile.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_text.py` & `dycw_utilities-0.8.2/tests/test_text.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_timer.py` & `dycw_utilities-0.8.2/tests/test_timer.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_tqdm.py` & `dycw_utilities-0.8.2/tests/test_tqdm.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_typed_settings.py` & `dycw_utilities-0.8.2/tests/test_typed_settings.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_types.py` & `dycw_utilities-0.8.2/tests/test_types.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_warnings.py` & `dycw_utilities-0.8.2/tests/test_warnings.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/test_zipfile.py` & `dycw_utilities-0.8.2/tests/test_zipfile.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/attrs/test_attrs.py` & `dycw_utilities-0.8.2/tests/attrs/test_attrs.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/attrs/test_xarray.py` & `dycw_utilities-0.8.2/tests/attrs/test_xarray.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/click/test_click.py` & `dycw_utilities-0.8.2/tests/click/test_click.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/click/test_luigi.py` & `dycw_utilities-0.8.2/tests/click/test_luigi.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/click/test_sqlalchemy.py` & `dycw_utilities-0.8.2/tests/click/test_sqlalchemy.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/holoviews/test_holoviews.py` & `dycw_utilities-0.8.2/tests/holoviews/test_holoviews.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/holoviews/test_xarray.py` & `dycw_utilities-0.8.2/tests/holoviews/test_xarray.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/hypothesis/test_hypothesis.py` & `dycw_utilities-0.8.2/tests/hypothesis/test_hypothesis.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/hypothesis/test_luigi.py` & `dycw_utilities-0.8.2/tests/hypothesis/test_luigi.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/hypothesis/test_pandas.py` & `dycw_utilities-0.8.2/tests/hypothesis/test_pandas.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/hypothesis/test_semver.py` & `dycw_utilities-0.8.2/tests/hypothesis/test_semver.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/hypothesis/test_sqlalchemy.py` & `dycw_utilities-0.8.2/tests/hypothesis/test_sqlalchemy.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/hypothesis/test_xarray.py` & `dycw_utilities-0.8.2/tests/hypothesis/test_xarray.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/loguru/script_to_test_luigi.py` & `dycw_utilities-0.8.2/tests/loguru/script_to_test_luigi.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/loguru/test_loguru.py` & `dycw_utilities-0.8.2/tests/loguru/test_loguru.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/luigi/test_attrs.py` & `dycw_utilities-0.8.2/tests/luigi/test_attrs.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/luigi/test_luigi.py` & `dycw_utilities-0.8.2/tests/luigi/test_luigi.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/luigi/test_server.py` & `dycw_utilities-0.8.2/tests/luigi/test_server.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/luigi/test_sqlalchemy.py` & `dycw_utilities-0.8.2/tests/luigi/test_sqlalchemy.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/math/test_math.py` & `dycw_utilities-0.8.2/tests/math/test_math.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/math/test_typing.py` & `dycw_utilities-0.8.2/tests/math/test_typing.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/numpy/test_numpy.py` & `dycw_utilities-0.8.2/tests/numpy/test_numpy.py`

 * *Files 2% similar despite different names*

```diff
@@ -22,32 +22,41 @@
 )
 from numpy.testing import assert_allclose, assert_equal
 from pandas import DatetimeTZDtype, Series
 from pytest import mark, param, raises
 
 from utilities.datetime import UTC
 from utilities.hypothesis import datetimes_utc
-from utilities.hypothesis.numpy import float_arrays
+from utilities.hypothesis.numpy import (
+    datetime64_dtypes,
+    datetime64_units,
+    datetime64s,
+    float_arrays,
+)
 from utilities.numpy import (
     DateOverflowError,
+    Datetime64Unit,
     EmptyNumpyConcatenateError,
     InfElementsError,
     InvalidDTypeError,
     LossOfNanosecondsError,
     MultipleTrueElementsError,
     NanElementsError,
     NonIntegralElementsError,
     NoTrueElementsError,
     ZeroPercentageChangeSpanError,
     ZeroShiftError,
     array_indexer,
     as_int,
     date_to_datetime64,
+    datetime64_dtype_to_unit,
     datetime64_to_date,
     datetime64_to_datetime,
+    datetime64_to_int,
+    datetime64_unit_to_dtype,
     datetime64D,
     datetime64ns,
     datetime64us,
     datetime64Y,
     datetime_to_datetime64,
     discretize,
     ffill,
@@ -812,14 +821,32 @@
     )
     @beartype
     def test_error(self, datetime: str, dtype: str, error: type[Exception]) -> None:
         with raises(error):
             _ = datetime64_to_date(datetime64(datetime, dtype))
 
 
+class TestDatetime64ToInt:
+    @beartype
+    def test_example(self) -> None:
+        assert datetime64_to_int(datetime64("2000-01-01", "D")) == 10957
+
+    @given(datetime=datetime64s())
+    @beartype
+    def test_main(self, datetime: datetime64) -> None:
+        _ = datetime64_to_int(datetime)
+
+    @given(data=data(), unit=datetime64_units())
+    @beartype
+    def test_round_trip(self, data: DataObject, unit: Datetime64Unit) -> None:
+        datetime = data.draw(datetime64s(unit=unit))
+        result = datetime64(datetime64_to_int(datetime), unit)
+        assert result == datetime
+
+
 class TestDatetime64ToDatetime:
     @beartype
     def test_example_ms(self) -> None:
         assert datetime64_to_datetime(
             datetime64("2000-01-01 00:00:00.123", "ms")
         ) == dt.datetime(2000, 1, 1, 0, 0, 0, 123000, tzinfo=UTC)
 
@@ -846,14 +873,44 @@
     )
     @beartype
     def test_error(self, datetime: str, dtype: str, error: type[Exception]) -> None:
         with raises(error):
             _ = datetime64_to_datetime(datetime64(datetime, dtype))
 
 
+class TestDatetime64DTypeToUnit:
+    @mark.parametrize(
+        ("dtype", "expected"),
+        [param(datetime64D, "D"), param(datetime64Y, "Y"), param(datetime64ns, "ns")],
+    )
+    @beartype
+    def test_example(self, dtype: Any, expected: Datetime64Unit) -> None:
+        assert datetime64_dtype_to_unit(dtype) == expected
+
+    @given(dtype=datetime64_dtypes())
+    @beartype
+    def test_round_trip(self, dtype: Any) -> None:
+        assert datetime64_unit_to_dtype(datetime64_dtype_to_unit(dtype)) == dtype
+
+
+class TestDatetime64DUnitToType:
+    @mark.parametrize(
+        ("unit", "expected"),
+        [param("D", datetime64D), param("Y", datetime64Y), param("ns", datetime64ns)],
+    )
+    @beartype
+    def test_example(self, unit: Datetime64Unit, expected: Any) -> None:
+        assert datetime64_unit_to_dtype(unit) == expected
+
+    @given(unit=datetime64_units())
+    @beartype
+    def test_round_trip(self, unit: Datetime64Unit) -> None:
+        assert datetime64_dtype_to_unit(datetime64_unit_to_dtype(unit)) == unit
+
+
 class TestDiscretize:
     @given(arr=float_arrays(shape=integers(0, 10), min_value=-1.0, max_value=1.0))
     @beartype
     def test_1_bin(self, arr: NDArrayF1) -> None:
         result = discretize(arr, 1)
         expected = zeros_like(arr, dtype=float)
         assert_equal(result, expected)
```

### Comparing `dycw_utilities-0.8.1/tests/numpy/test_typing.py` & `dycw_utilities-0.8.2/tests/numpy/test_typing.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/pandas/test_pandas.py` & `dycw_utilities-0.8.2/tests/pandas/test_pandas.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/pandas/test_typing.py` & `dycw_utilities-0.8.2/tests/pandas/test_typing.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/sqlalchemy/test_fastparquet.py` & `dycw_utilities-0.8.2/tests/sqlalchemy/test_fastparquet.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/sqlalchemy/test_pandas.py` & `dycw_utilities-0.8.2/tests/sqlalchemy/test_pandas.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/sqlalchemy/test_sqlalchemy.py` & `dycw_utilities-0.8.2/tests/sqlalchemy/test_sqlalchemy.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/xarray/test_typing.py` & `dycw_utilities-0.8.2/tests/xarray/test_typing.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/zarr/test_xarray.py` & `dycw_utilities-0.8.2/tests/zarr/test_xarray.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/tests/zarr/test_zarr.py` & `dycw_utilities-0.8.2/tests/zarr/test_zarr.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/atomicwrites.py` & `dycw_utilities-0.8.2/utilities/atomicwrites.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/bidict.py` & `dycw_utilities-0.8.2/utilities/bidict.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/cryptography.py` & `dycw_utilities-0.8.2/utilities/cryptography.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/cvxpy.py` & `dycw_utilities-0.8.2/utilities/cvxpy.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/datetime.py` & `dycw_utilities-0.8.2/utilities/datetime.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/email.py` & `dycw_utilities-0.8.2/utilities/email.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/enum.py` & `dycw_utilities-0.8.2/utilities/enum.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/errors.py` & `dycw_utilities-0.8.2/utilities/errors.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/fastapi.py` & `dycw_utilities-0.8.2/utilities/fastapi.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/fastparquet.py` & `dycw_utilities-0.8.2/utilities/fastparquet.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/fpdf2.py` & `dycw_utilities-0.8.2/utilities/fpdf2.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/git.py` & `dycw_utilities-0.8.2/utilities/git.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/hatch.py` & `dycw_utilities-0.8.2/utilities/hatch.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/iterables.py` & `dycw_utilities-0.8.2/utilities/iterables.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/json.py` & `dycw_utilities-0.8.2/utilities/json.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/logging.py` & `dycw_utilities-0.8.2/utilities/logging.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/loguru.py` & `dycw_utilities-0.8.2/utilities/loguru.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/memory_profiler.py` & `dycw_utilities-0.8.2/utilities/memory_profiler.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/modules.py` & `dycw_utilities-0.8.2/utilities/modules.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/more_itertools.py` & `dycw_utilities-0.8.2/utilities/more_itertools.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/os.py` & `dycw_utilities-0.8.2/utilities/os.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/pickle.py` & `dycw_utilities-0.8.2/utilities/pickle.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/pqdm.py` & `dycw_utilities-0.8.2/utilities/pqdm.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/pyinstrument.py` & `dycw_utilities-0.8.2/utilities/pyinstrument.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/pytest.py` & `dycw_utilities-0.8.2/utilities/pytest.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/re.py` & `dycw_utilities-0.8.2/utilities/re.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/scipy.py` & `dycw_utilities-0.8.2/utilities/scipy.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/sentinel.py` & `dycw_utilities-0.8.2/utilities/sentinel.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/subprocess.py` & `dycw_utilities-0.8.2/utilities/subprocess.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/tempfile.py` & `dycw_utilities-0.8.2/utilities/tempfile.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/text.py` & `dycw_utilities-0.8.2/utilities/text.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/timer.py` & `dycw_utilities-0.8.2/utilities/timer.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/tqdm.py` & `dycw_utilities-0.8.2/utilities/tqdm.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/typed_settings.py` & `dycw_utilities-0.8.2/utilities/typed_settings.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/types.py` & `dycw_utilities-0.8.2/utilities/types.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/warnings.py` & `dycw_utilities-0.8.2/utilities/warnings.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/zipfile.py` & `dycw_utilities-0.8.2/utilities/zipfile.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/attrs/__init__.py` & `dycw_utilities-0.8.2/utilities/attrs/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/clean_dir/__init__.py` & `dycw_utilities-0.8.2/utilities/clean_dir/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/clean_dir/classes.py` & `dycw_utilities-0.8.2/utilities/clean_dir/classes.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/click/__init__.py` & `dycw_utilities-0.8.2/utilities/click/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/click/luigi.py` & `dycw_utilities-0.8.2/utilities/click/luigi.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/click/sqlalchemy.py` & `dycw_utilities-0.8.2/utilities/click/sqlalchemy.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/holoviews/__init__.py` & `dycw_utilities-0.8.2/utilities/holoviews/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/holoviews/xarray.py` & `dycw_utilities-0.8.2/utilities/holoviews/xarray.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/hypothesis/__init__.py` & `dycw_utilities-0.8.2/utilities/hypothesis/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/hypothesis/numpy.py` & `dycw_utilities-0.8.2/utilities/hypothesis/numpy.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,33 +1,45 @@
-from typing import Any, Optional
+from typing import Any, Optional, Union
 
 from beartype import beartype
-from hypothesis.extra.numpy import array_shapes, arrays, from_dtype
-from hypothesis.strategies import SearchStrategy, booleans, composite, integers, none
+from hypothesis import assume
+from hypothesis.extra.numpy import array_shapes, arrays
+from hypothesis.strategies import (
+    SearchStrategy,
+    booleans,
+    composite,
+    integers,
+    none,
+    sampled_from,
+)
 from numpy import (
     concatenate,
-    dtype,
+    datetime64,
     expand_dims,
     iinfo,
     int32,
     int64,
     uint32,
     uint64,
     zeros,
 )
 from numpy.typing import NDArray
 
 from utilities.hypothesis import floats_extra, lift_draw, lists_fixed_length, text_ascii
 from utilities.hypothesis.typing import MaybeSearchStrategy, Shape
 from utilities.math.typing import IntNonNeg
 from utilities.numpy import (
+    Datetime64Unit,
     EmptyNumpyConcatenateError,
+    datetime64_to_int,
+    datetime64_unit_to_dtype,
+    datetime64D,
     redirect_to_empty_numpy_concatenate_error,
 )
-from utilities.numpy.typing import NDArrayB, NDArrayF, NDArrayI, NDArrayO
+from utilities.numpy.typing import NDArrayB, NDArrayDD, NDArrayF, NDArrayI, NDArrayO
 
 
 @composite
 @beartype
 def bool_arrays(
     _draw: Any,
     /,
@@ -70,14 +82,96 @@
             else:
                 shape = (size_, *fallback)
             return zeros(shape, dtype=dtype)
 
 
 @composite
 @beartype
+def datetime64D_arrays(  # noqa: N802
+    _draw: Any,
+    /,
+    *,
+    shape: MaybeSearchStrategy[Shape] = array_shapes(),
+    min_value: MaybeSearchStrategy[Optional[Union[int, datetime64]]] = None,
+    max_value: MaybeSearchStrategy[Optional[Union[int, datetime64]]] = None,
+    fill: Optional[SearchStrategy[Any]] = None,
+    unique: MaybeSearchStrategy[bool] = False,
+) -> NDArrayDD:
+    """Strategy for generating arrays of dates."""
+    draw = lift_draw(_draw)
+    return draw(
+        arrays(
+            datetime64D,
+            draw(shape),
+            elements=datetime64s(min_value=min_value, max_value=max_value, unit="D"),
+            fill=fill,
+            unique=draw(unique),
+        )
+    )
+
+
+@composite
+@beartype
+def datetime64s(
+    _draw: Any,
+    /,
+    *,
+    min_value: MaybeSearchStrategy[Optional[Union[datetime64, int]]] = None,
+    max_value: MaybeSearchStrategy[Optional[Union[datetime64, int]]] = None,
+    unit: MaybeSearchStrategy[Optional[Datetime64Unit]] = None,
+) -> datetime64:
+    """Strategy for generating datetime64s."""
+    draw = lift_draw(_draw)
+    min_value_, max_value_ = map(draw, [min_value, max_value])
+
+    @beartype
+    def convert(value: Optional[Union[int, datetime64]], /) -> Optional[int]:
+        if (value is None) or isinstance(value, int):
+            return value
+        return datetime64_to_int(value)
+
+    i = draw(int64s(min_value=convert(min_value_), max_value=convert(max_value_)))
+    _ = assume(i != iinfo(int64).min)
+    if (unit_ := draw(unit)) is None:
+        unit_ = draw(datetime64_units())
+    return datetime64(i, unit_)
+
+
+@composite
+@beartype
+def datetime64_dtypes(_draw: Any, /) -> Any:
+    """Strategy for generating datetime64 dtypes."""
+    draw = lift_draw(_draw)
+    unit = draw(datetime64_units())
+    return datetime64_unit_to_dtype(unit)
+
+
+@beartype
+def datetime64_units() -> SearchStrategy[Datetime64Unit]:
+    """Strategy for generating datetime64 units."""
+    units: list[Datetime64Unit] = [
+        "Y",
+        "M",
+        "W",
+        "D",
+        "h",
+        "m",
+        "s",
+        "ms",
+        "us",
+        "ns",
+        "ps",
+        "fs",
+        "as",
+    ]
+    return sampled_from(units)
+
+
+@composite
+@beartype
 def float_arrays(
     _draw: Any,
     /,
     *,
     shape: MaybeSearchStrategy[Shape] = array_shapes(),
     min_value: MaybeSearchStrategy[Optional[float]] = None,
     max_value: MaybeSearchStrategy[Optional[float]] = None,
@@ -126,23 +220,31 @@
     elements = integers(min_value=min_value_use, max_value=max_value_use)
     return draw(
         arrays(int, draw(shape), elements=elements, fill=fill, unique=draw(unique))
     )
 
 
 @beartype
-def int32s() -> SearchStrategy[int]:
+def int32s(
+    *,
+    min_value: MaybeSearchStrategy[Optional[int]] = None,
+    max_value: MaybeSearchStrategy[Optional[int]] = None,
+) -> SearchStrategy[int]:
     """Strategy for generating int32s."""
-    return from_dtype(dtype(int32)).map(int)
+    return _fixed_width_ints(int32, min_value=min_value, max_value=max_value)
 
 
 @beartype
-def int64s() -> SearchStrategy[int]:
+def int64s(
+    *,
+    min_value: MaybeSearchStrategy[Optional[int]] = None,
+    max_value: MaybeSearchStrategy[Optional[int]] = None,
+) -> SearchStrategy[int]:
     """Strategy for generating int64s."""
-    return from_dtype(dtype(int64)).map(int)
+    return _fixed_width_ints(int64, min_value=min_value, max_value=max_value)
 
 
 @composite
 @beartype
 def str_arrays(
     _draw: Any,
     /,
@@ -161,16 +263,43 @@
         elements |= none()
     return draw(
         arrays(object, draw(shape), elements=elements, fill=fill, unique=draw(unique))
     )
 
 
 @beartype
-def uint32s() -> SearchStrategy[int]:
+def uint32s(
+    *,
+    min_value: MaybeSearchStrategy[Optional[int]] = None,
+    max_value: MaybeSearchStrategy[Optional[int]] = None,
+) -> SearchStrategy[int]:
     """Strategy for generating uint32s."""
-    return from_dtype(dtype(uint32)).map(int)
+    return _fixed_width_ints(uint32, min_value=min_value, max_value=max_value)
 
 
 @beartype
-def uint64s() -> SearchStrategy[int]:
+def uint64s(
+    *,
+    min_value: MaybeSearchStrategy[Optional[int]] = None,
+    max_value: MaybeSearchStrategy[Optional[int]] = None,
+) -> SearchStrategy[int]:
     """Strategy for generating uint64s."""
-    return from_dtype(dtype(uint64)).map(int)
+    return _fixed_width_ints(uint64, min_value=min_value, max_value=max_value)
+
+
+@composite
+@beartype
+def _fixed_width_ints(
+    _draw: Any,
+    dtype: Any,
+    /,
+    *,
+    min_value: MaybeSearchStrategy[Optional[int]] = None,
+    max_value: MaybeSearchStrategy[Optional[int]] = None,
+) -> int:
+    """Strategy for generating int64s."""
+    draw = lift_draw(_draw)
+    min_value_, max_value_ = map(draw, [min_value, max_value])
+    info = iinfo(dtype)
+    min_value_use = info.min if min_value_ is None else max(info.min, min_value_)
+    max_value_use = info.max if max_value_ is None else min(info.max, max_value_)
+    return draw(integers(min_value_use, max_value_use))
```

### Comparing `dycw_utilities-0.8.1/utilities/hypothesis/pandas.py` & `dycw_utilities-0.8.2/utilities/hypothesis/pandas.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/hypothesis/semver.py` & `dycw_utilities-0.8.2/utilities/hypothesis/semver.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/hypothesis/sqlalchemy.py` & `dycw_utilities-0.8.2/utilities/hypothesis/sqlalchemy.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/hypothesis/xarray.py` & `dycw_utilities-0.8.2/utilities/hypothesis/xarray.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/luigi/__init__.py` & `dycw_utilities-0.8.2/utilities/luigi/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/luigi/attrs.py` & `dycw_utilities-0.8.2/utilities/luigi/attrs.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/luigi/semver.py` & `dycw_utilities-0.8.2/utilities/luigi/semver.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/luigi/sqlalchemy.py` & `dycw_utilities-0.8.2/utilities/luigi/sqlalchemy.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/luigi/server/__init__.py` & `dycw_utilities-0.8.2/utilities/luigi/server/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/luigi/server/classes.py` & `dycw_utilities-0.8.2/utilities/luigi/server/classes.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/math/__init__.py` & `dycw_utilities-0.8.2/utilities/math/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/math/typing.py` & `dycw_utilities-0.8.2/utilities/math/typing.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/monitor_memory/__init__.py` & `dycw_utilities-0.8.2/utilities/monitor_memory/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/monitor_memory/classes.py` & `dycw_utilities-0.8.2/utilities/monitor_memory/classes.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/numpy/__init__.py` & `dycw_utilities-0.8.2/utilities/numpy/__init__.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,20 +1,21 @@
 import datetime as dt
 from collections.abc import Iterable, Iterator
 from functools import reduce
 from itertools import repeat
-from typing import Any, NoReturn, Optional, Union, cast, overload
+from typing import Any, Literal, NoReturn, Optional, Union, cast, overload
 
 import numpy as np
 from beartype import beartype
 from bottleneck import push
 from numpy import (
     array,
     datetime64,
     digitize,
+    dtype,
     errstate,
     flatnonzero,
     flip,
     full_like,
     inf,
     isclose,
     isfinite,
@@ -88,14 +89,15 @@
     is_zero,
     is_zero_or_finite_and_non_micro,
     is_zero_or_finite_and_non_micro_or_nan,
     is_zero_or_nan,
     is_zero_or_non_micro,
     is_zero_or_non_micro_or_nan,
 )
+from utilities.re import extract_group
 
 _ = (
     datetime64D,
     datetime64Y,
     datetime64ns,
     is_at_least,
     is_at_least_or_nan,
@@ -137,14 +139,19 @@
     is_zero_or_finite_and_non_micro_or_nan,
     is_zero_or_nan,
     is_zero_or_non_micro,
     is_zero_or_non_micro_or_nan,
 )
 
 
+Datetime64Unit = Literal[
+    "Y", "M", "W", "D", "h", "m", "s", "ms", "us", "ns", "ps", "fs", "as"
+]
+
+
 @beartype
 def array_indexer(
     i: int, ndim: int, /, *, axis: int = -1
 ) -> tuple[Union[int, slice], ...]:
     """Get the indexer which returns the `ith` slice of an array along an axis."""
     indexer: list[Union[int, slice]] = list(repeat(slice(None), times=ndim))
     indexer[axis] = i
@@ -187,37 +194,48 @@
 @beartype
 def date_to_datetime64(date: dt.date, /) -> datetime64:
     """Convert a `dt.date` to `numpy.datetime64`."""
 
     return datetime64(date, "D")
 
 
+DATE_MIN_AS_DATETIME64 = date_to_datetime64(dt.date.min)
+DATE_MAX_AS_DATETIME64 = date_to_datetime64(dt.date.max)
+
+
 @beartype
 def datetime_to_datetime64(datetime: dt.datetime, /) -> datetime64:
     """Convert a `dt.datetime` to `numpy.datetime64`."""
 
     return datetime64(datetime, "us")
 
 
 @beartype
 def datetime64_to_date(datetime: datetime64, /) -> dt.date:
     """Convert a `numpy.datetime64` to a `dt.date`."""
 
-    as_int = datetime.astype(int).item()
+    as_int = datetime64_to_int(datetime)
     if (dtype := datetime.dtype) == datetime64D:
         try:
             return (EPOCH_UTC + dt.timedelta(days=as_int)).date()
         except OverflowError:
             msg = f"{datetime=}, {dtype=}"
             raise DateOverflowError(msg) from None
     msg = f"{datetime=}, {dtype=}"
     raise NotImplementedError(msg)
 
 
 @beartype
+def datetime64_to_int(datetime: datetime64, /) -> int:
+    """Convert a `numpy.datetime64` to an `int`."""
+
+    return datetime.astype(int).item()
+
+
+@beartype
 def datetime64_to_datetime(datetime: datetime64, /) -> dt.datetime:
     """Convert a `numpy.datetime64` to a `dt.datetime`."""
 
     as_int = datetime.astype(int).item()
     if (dtype := datetime.dtype) == datetime64ms:
         try:
             return EPOCH_UTC + dt.timedelta(milliseconds=as_int)
@@ -233,14 +251,26 @@
             raise LossOfNanosecondsError(msg)
         return EPOCH_UTC + dt.timedelta(microseconds=microseconds)
     else:
         msg = f"{datetime=}, {dtype=}"
         raise NotImplementedError(msg)
 
 
+@beartype
+def datetime64_dtype_to_unit(dtype: Any, /) -> Datetime64Unit:
+    """Convert a `datetime64` dtype to a unit."""
+    return cast(Datetime64Unit, extract_group(r"^<M8\[(\w+)\]$", dtype.str))
+
+
+@beartype
+def datetime64_unit_to_dtype(unit: Datetime64Unit, /) -> Any:
+    """Convert a `datetime64` unit to a dtype."""
+    return dtype(f"datetime64[{unit}]")
+
+
 class DateOverflowError(ValueError):
     """Raised when a date overflows."""
 
 
 class LossOfNanosecondsError(ValueError):
     """Raised when nanoseconds are lost."""
```

### Comparing `dycw_utilities-0.8.1/utilities/numpy/typing.py` & `dycw_utilities-0.8.2/utilities/numpy/typing.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/pandas/__init__.py` & `dycw_utilities-0.8.2/utilities/pandas/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/pandas/typing.py` & `dycw_utilities-0.8.2/utilities/pandas/typing.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/pypi_server/__init__.py` & `dycw_utilities-0.8.2/utilities/pypi_server/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/pypi_server/classes.py` & `dycw_utilities-0.8.2/utilities/pypi_server/classes.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/sqlalchemy/__init__.py` & `dycw_utilities-0.8.2/utilities/sqlalchemy/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/sqlalchemy/fastparquet.py` & `dycw_utilities-0.8.2/utilities/sqlalchemy/fastparquet.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/sqlalchemy/pandas.py` & `dycw_utilities-0.8.2/utilities/sqlalchemy/pandas.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/xarray/typing.py` & `dycw_utilities-0.8.2/utilities/xarray/typing.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/zarr/__init__.py` & `dycw_utilities-0.8.2/utilities/zarr/__init__.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/utilities/zarr/xarray.py` & `dycw_utilities-0.8.2/utilities/zarr/xarray.py`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/.gitignore` & `dycw_utilities-0.8.2/.gitignore`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/README.md` & `dycw_utilities-0.8.2/README.md`

 * *Files identical despite different names*

### Comparing `dycw_utilities-0.8.1/pyproject.toml` & `dycw_utilities-0.8.2/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -116,15 +116,15 @@
   "loguru >= 0.6.0",
   "typed-settings[click] >= 23.0.0",
 ]
 semver = ["semver >= 3.0.0"]
 sqlalchemy = [
   "bidict >= 0.22.1",
   "more-itertools >= 9.1.0",
-  "sqlalchemy >= 2.0.7",
+  "sqlalchemy >= 2.0.9",
   "timeout-decorator >= 0.5.0, < 0.6",
 ]
 tqdm = ["tqdm >= 4.65.0"]
 typed-settings = ["typed-settings[click] >= 23.0.0"]
 xarray = [
   "bottleneck >= 1.3.7",
   "numpy >= 1.23.5",
@@ -152,15 +152,15 @@
   "more-itertools >= 9.1.0",
   "numpy >= 1.23.5",
   "pandas >= 1.5.3",
   "pqdm >= 0.2.0",
   "selenium >= 4.8.3",
   "semver >= 3.0.0",
   "scipy >= 1.10.1, < 1.11",
-  "sqlalchemy >= 2.0.7",
+  "sqlalchemy >= 2.0.9",
   "timeout-decorator >= 0.5.0, < 0.6",
   "tqdm >= 4.65.0",
   "typed-settings[click] >= 23.0.0",
   "xarray >= 2023.2.0",
   "zarr >= 2.14.2",
 ]
 test = [
```

### Comparing `dycw_utilities-0.8.1/PKG-INFO` & `dycw_utilities-0.8.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dycw-utilities
-Version: 0.8.1
+Version: 0.8.2
 Author-email: Derek Wan <d.wan@icloud.com>
 Requires-Python: >=3.9
 Requires-Dist: beartype>=0.12.0
 Requires-Dist: typing-extensions>=4.4.0
 Provides-Extra: airium
 Requires-Dist: airium>=0.2.5; extra == 'airium'
 Provides-Extra: atomicwrites
@@ -32,15 +32,15 @@
 Requires-Dist: more-itertools>=9.1.0; extra == 'core'
 Requires-Dist: numpy>=1.23.5; extra == 'core'
 Requires-Dist: pandas>=1.5.3; extra == 'core'
 Requires-Dist: pqdm>=0.2.0; extra == 'core'
 Requires-Dist: scipy<1.11,>=1.10.1; extra == 'core'
 Requires-Dist: selenium>=4.8.3; extra == 'core'
 Requires-Dist: semver>=3.0.0; extra == 'core'
-Requires-Dist: sqlalchemy>=2.0.7; extra == 'core'
+Requires-Dist: sqlalchemy>=2.0.9; extra == 'core'
 Requires-Dist: timeout-decorator<0.6,>=0.5.0; extra == 'core'
 Requires-Dist: tqdm>=4.65.0; extra == 'core'
 Requires-Dist: typed-settings[click]>=23.0.0; extra == 'core'
 Requires-Dist: xarray>=2023.2.0; extra == 'core'
 Requires-Dist: zarr>=2.14.2; extra == 'core'
 Provides-Extra: cryptography
 Requires-Dist: cryptography>=40.0.1; extra == 'cryptography'
@@ -153,15 +153,15 @@
 Requires-Dist: loguru>=0.6.0; extra == 'scripts'
 Requires-Dist: typed-settings[click]>=23.0.0; extra == 'scripts'
 Provides-Extra: semver
 Requires-Dist: semver>=3.0.0; extra == 'semver'
 Provides-Extra: sqlalchemy
 Requires-Dist: bidict>=0.22.1; extra == 'sqlalchemy'
 Requires-Dist: more-itertools>=9.1.0; extra == 'sqlalchemy'
-Requires-Dist: sqlalchemy>=2.0.7; extra == 'sqlalchemy'
+Requires-Dist: sqlalchemy>=2.0.9; extra == 'sqlalchemy'
 Requires-Dist: timeout-decorator<0.6,>=0.5.0; extra == 'sqlalchemy'
 Provides-Extra: test
 Requires-Dist: atomicwrites>=1.4.1; extra == 'test'
 Requires-Dist: hypothesis>=6.70.1; extra == 'test'
 Requires-Dist: pytest-check>=2.1.4; extra == 'test'
 Requires-Dist: pytest>=7.2.2; extra == 'test'
 Provides-Extra: tqdm
```

