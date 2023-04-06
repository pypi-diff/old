# Comparing `tmp/clean_copy-0.1.0.tar.gz` & `tmp/clean_copy-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "clean_copy-0.1.0.tar", max compression
+gzip compressed data, was "clean_copy-0.1.1.tar", max compression
```

## Comparing `clean_copy-0.1.0.tar` & `clean_copy-0.1.1.tar`

### file list

```diff
@@ -1,6 +1,6 @@
--rw-r--r--   0        0        0        0 2023-04-04 15:17:56.931391 clean_copy-0.1.0/README.md
--rw-r--r--   0        0        0       77 2023-04-05 06:50:26.960311 clean_copy-0.1.0/clean_copy/__init__.py
--rw-r--r--   0        0        0     2498 2023-04-05 06:56:38.727332 clean_copy-0.1.0/clean_copy/clean_copy.py
--rw-r--r--   0        0        0     1363 2023-04-05 06:56:05.995423 clean_copy-0.1.0/clean_copy/cli.py
--rw-r--r--   0        0        0      399 2023-04-05 07:02:28.222328 clean_copy-0.1.0/pyproject.toml
--rw-r--r--   0        0        0      416 1970-01-01 00:00:00.000000 clean_copy-0.1.0/PKG-INFO
+-rw-r--r--   0        0        0      169 2023-04-05 07:12:48.047596 clean_copy-0.1.1/README.md
+-rw-r--r--   0        0        0       77 2023-04-05 06:50:26.960311 clean_copy-0.1.1/clean_copy/__init__.py
+-rw-r--r--   0        0        0     2444 2023-04-05 07:08:05.181322 clean_copy-0.1.1/clean_copy/clean_copy.py
+-rw-r--r--   0        0        0     1329 2023-04-05 07:08:05.169322 clean_copy-0.1.1/clean_copy/cli.py
+-rw-r--r--   0        0        0      508 2023-04-06 08:03:48.708188 clean_copy-0.1.1/pyproject.toml
+-rw-r--r--   0        0        0      684 1970-01-01 00:00:00.000000 clean_copy-0.1.1/PKG-INFO
```

### Comparing `clean_copy-0.1.0/clean_copy/clean_copy.py` & `clean_copy-0.1.1/clean_copy/clean_copy.py`

 * *Files 2% similar despite different names*

```diff
@@ -43,19 +43,15 @@
 
     all_rules = parent_rules + local_rules
     path_spec = PathSpec.from_lines(GitWildMatchPattern, all_rules)
 
     for entry in folder_path.iterdir():
         relative_path = str(entry.relative_to(root_path))
 
-        if (
-            entry.is_file()
-            and not path_spec.match_file(relative_path)
-            and not entry.name == ignore_spec
-        ):
+        if entry.is_file() and not path_spec.match_file(relative_path) and not entry.name == ignore_spec:
             unignored_files.append(relative_path)
         elif entry.is_dir() and not path_spec.match_file(relative_path):
             unignored_files.extend(
                 get_unignored_files(
                     root_path=root_path,
                     folder_path=entry,
                     parent_rules=all_rules,
@@ -64,17 +60,15 @@
             )
         else:
             logger.debug("Ignoring %s", relative_path)
 
     return unignored_files
 
 
-def copy_files(
-    source_path: Path, target_path: Path, unignored_files: List[str]
-) -> None:
+def copy_files(source_path: Path, target_path: Path, unignored_files: List[str]) -> None:
     num_to_be_copied = len(unignored_files)
     file_size = 0
 
     for file_path in unignored_files:
         source_file = source_path / file_path
         target_file = target_path / file_path
         if not target_file.parent.exists():
```

### Comparing `clean_copy-0.1.0/clean_copy/cli.py` & `clean_copy-0.1.1/clean_copy/cli.py`

 * *Files 3% similar despite different names*

```diff
@@ -9,17 +9,15 @@
 @click.command()
 @click.argument("source", type=click.Path(exists=True, file_okay=False))
 @click.argument("destination", type=click.Path())
 @click.option("--quiet", default=False, is_flag=True)
 @click.option("--ignore-spec", default=".copyignore", type=str)
 @click.option("--dry-run", default=False, is_flag=True)
 @click.option("--include-parent-ignore", default=True, is_flag=True)
-def clean_copy_cli(
-    source, destination, quiet, ignore_spec, include_parent_ignore, dry_run
-):
+def clean_copy_cli(source, destination, quiet, ignore_spec, include_parent_ignore, dry_run):
     if quiet:
         logging.basicConfig(level=logging.ERROR)
     else:
         logging.basicConfig(level=logging.DEBUG)
 
     source = Path(source)
     destination = Path(destination)
@@ -30,17 +28,13 @@
 
     unignored_files = get_unignored_files(
         root_path=source,
         folder_path=None,
         parent_rules=parent_rules,
         ignore_spec=".copyignore",
     )
-    copy_count, file_size = copy_files(
-        source, destination, unignored_files=unignored_files
-    )
-    click.echo(
-        f"Copied {copy_count} files ({file_size} MB) from {source} to {destination}"
-    )
+    copy_count, file_size = copy_files(source, destination, unignored_files=unignored_files)
+    click.echo(f"Copied {copy_count} files ({file_size} MB) from {source} to {destination}")
 
 
 if __name__ == "__main__":
     clean_copy_cli()
```

