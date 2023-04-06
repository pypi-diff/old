# Comparing `tmp/ScriptCollection-3.3.8-py3-none-any.whl.zip` & `tmp/ScriptCollection-3.3.9-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,17 +1,17 @@
-Zip file size: 47420 bytes, number of entries: 15
+Zip file size: 47520 bytes, number of entries: 15
 -rw-rw-rw-  2.0 fat    15739 b- defN 22-Nov-14 12:37 ScriptCollection/Executables.py
 -rw-rw-rw-  2.0 fat    31649 b- defN 22-Oct-16 16:59 ScriptCollection/GeneralUtilities.py
 -rw-rw-rw-  2.0 fat     3421 b- defN 22-Aug-29 05:45 ScriptCollection/Hardening.py
 -rw-rw-rw-  2.0 fat     1937 b- defN 22-Aug-30 21:59 ScriptCollection/ProgramRunnerBase.py
 -rw-rw-rw-  2.0 fat     6273 b- defN 22-Oct-16 19:55 ScriptCollection/ProgramRunnerEpew.py
 -rw-rw-rw-  2.0 fat     3023 b- defN 22-Aug-30 21:59 ScriptCollection/ProgramRunnerPopen.py
--rw-rw-rw-  2.0 fat    75969 b- defN 22-Nov-18 07:40 ScriptCollection/ScriptCollectionCore.py
--rw-rw-rw-  2.0 fat    74143 b- defN 22-Nov-18 07:40 ScriptCollection/TasksForCommonProjectStructure.py
+-rw-rw-rw-  2.0 fat    75969 b- defN 22-Nov-18 12:58 ScriptCollection/ScriptCollectionCore.py
+-rw-rw-rw-  2.0 fat    74893 b- defN 22-Nov-18 12:58 ScriptCollection/TasksForCommonProjectStructure.py
 -rw-rw-rw-  2.0 fat     7918 b- defN 22-Aug-30 21:59 ScriptCollection/UpdateCertificates.py
 -rw-rw-rw-  2.0 fat        0 b- defN 22-Aug-29 05:45 ScriptCollection/__init__.py
--rw-rw-rw-  2.0 fat     7146 b- defN 22-Nov-18 07:40 ScriptCollection-3.3.8.dist-info/METADATA
--rw-rw-rw-  2.0 fat       92 b- defN 22-Nov-18 07:40 ScriptCollection-3.3.8.dist-info/WHEEL
--rw-rw-rw-  2.0 fat     1697 b- defN 22-Nov-18 07:40 ScriptCollection-3.3.8.dist-info/entry_points.txt
--rw-rw-rw-  2.0 fat       17 b- defN 22-Nov-18 07:40 ScriptCollection-3.3.8.dist-info/top_level.txt
-?rw-rw-r--  2.0 fat     1375 b- defN 22-Nov-18 07:40 ScriptCollection-3.3.8.dist-info/RECORD
-15 files, 230399 bytes uncompressed, 45104 bytes compressed:  80.4%
+-rw-rw-rw-  2.0 fat     7146 b- defN 22-Nov-18 12:58 ScriptCollection-3.3.9.dist-info/METADATA
+-rw-rw-rw-  2.0 fat       92 b- defN 22-Nov-18 12:58 ScriptCollection-3.3.9.dist-info/WHEEL
+-rw-rw-rw-  2.0 fat     1697 b- defN 22-Nov-18 12:58 ScriptCollection-3.3.9.dist-info/entry_points.txt
+-rw-rw-rw-  2.0 fat       17 b- defN 22-Nov-18 12:58 ScriptCollection-3.3.9.dist-info/top_level.txt
+?rw-rw-r--  2.0 fat     1375 b- defN 22-Nov-18 12:58 ScriptCollection-3.3.9.dist-info/RECORD
+15 files, 231149 bytes uncompressed, 45204 bytes compressed:  80.4%
```

## zipnote {}

```diff
@@ -24,23 +24,23 @@
 
 Filename: ScriptCollection/UpdateCertificates.py
 Comment: 
 
 Filename: ScriptCollection/__init__.py
 Comment: 
 
-Filename: ScriptCollection-3.3.8.dist-info/METADATA
+Filename: ScriptCollection-3.3.9.dist-info/METADATA
 Comment: 
 
-Filename: ScriptCollection-3.3.8.dist-info/WHEEL
+Filename: ScriptCollection-3.3.9.dist-info/WHEEL
 Comment: 
 
-Filename: ScriptCollection-3.3.8.dist-info/entry_points.txt
+Filename: ScriptCollection-3.3.9.dist-info/entry_points.txt
 Comment: 
 
-Filename: ScriptCollection-3.3.8.dist-info/top_level.txt
+Filename: ScriptCollection-3.3.9.dist-info/top_level.txt
 Comment: 
 
-Filename: ScriptCollection-3.3.8.dist-info/RECORD
+Filename: ScriptCollection-3.3.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## ScriptCollection/ScriptCollectionCore.py

```diff
@@ -21,15 +21,15 @@
 from PyPDF2 import PdfFileMerger
 from .GeneralUtilities import GeneralUtilities
 from .ProgramRunnerBase import ProgramRunnerBase
 from .ProgramRunnerPopen import ProgramRunnerPopen
 from .ProgramRunnerEpew import ProgramRunnerEpew, CustomEpewArgument
 
 
-version = "3.3.8"
+version = "3.3.9"
 __version__ = version
 
 
 class ScriptCollectionCore:
 
     # The purpose of this property is to use it when testing your code which uses scriptcollection for external program-calls.
     # Do not change this value for productive environments.
```

## ScriptCollection/TasksForCommonProjectStructure.py

```diff
@@ -257,14 +257,23 @@
         if result is None:
             return default_value
         else:
             return result
 
     @staticmethod
     @GeneralUtilities.check_arguments
+    def get_additionalargumentsfile_from_commandline_arguments(commandline_arguments: list[str],  default_value: str) -> str:
+        result = TasksForCommonProjectStructure.get_property_from_commandline_arguments(commandline_arguments, "additionalargumentsfile")
+        if result is None:
+            return default_value
+        else:
+            return result
+
+    @staticmethod
+    @GeneralUtilities.check_arguments
     def get_filestosign_from_commandline_arguments(commandline_arguments: list[str],  default_value: dict[str, str]) -> dict[str, str]():
         result_plain = TasksForCommonProjectStructure.get_property_from_commandline_arguments(commandline_arguments, "sign")
         if result_plain is None:
             return default_value
         else:
             result: dict[str, str] = dict[str, str]()
             files_tuples = GeneralUtilities.to_list(result_plain, ";")
@@ -397,28 +406,28 @@
 
     @GeneralUtilities.check_arguments
     def standardized_tasks_linting_for_python_codeunit_in_common_project_structure(self, linting_script_file: str, verbosity: int, buildenvironment: str, commandline_arguments: list[str]):
         codeunitname: str = Path(os.path.dirname(linting_script_file)).parent.parent.name
         verbosity = TasksForCommonProjectStructure.get_verbosity_from_commandline_arguments(commandline_arguments,  verbosity)
         repository_folder: str = str(Path(os.path.dirname(linting_script_file)).parent.parent.parent.absolute())
         errors_found = False
-        GeneralUtilities.write_message_to_stdout(f"Check for linting-issues in codeunit {codeunitname}")
+        GeneralUtilities.write_message_to_stdout(f"Check for linting-issues in codeunit {codeunitname}.")
         src_folder = os.path.join(repository_folder, codeunitname, codeunitname)
         tests_folder = src_folder+"Tests"
         for file in GeneralUtilities.get_all_files_of_folder(src_folder)+GeneralUtilities.get_all_files_of_folder(tests_folder):
             relative_file_path_in_repository = os.path.relpath(file, repository_folder)
             if file.endswith(".py") and os.path.getsize(file) > 0 and not self.__sc.file_is_git_ignored(relative_file_path_in_repository, repository_folder):
-                GeneralUtilities.write_message_to_stdout(f"Check for linting-issues in {os.path.relpath(file,os.path.join(repository_folder,codeunitname))}")
+                GeneralUtilities.write_message_to_stdout(f"Check for linting-issues in {os.path.relpath(file,os.path.join(repository_folder,codeunitname))}.")
                 linting_result = self.__sc.python_file_has_errors(file, repository_folder)
                 if (linting_result[0]):
                     errors_found = True
                     for error in linting_result[1]:
                         GeneralUtilities.write_message_to_stderr(error)
         if errors_found:
-            raise Exception("Linting-issues occurred")
+            raise Exception("Linting-issues occurred.")
         else:
             GeneralUtilities.write_message_to_stdout("No linting-issues found.")
 
     @GeneralUtilities.check_arguments
     def standardized_tasks_generate_coverage_report(self, repository_folder: str, codeunitname: str, verbosity: int, generate_badges: bool, buildenvironment: str, commandline_arguments: list[str]):
         """This script expects that the file '<repositorybasefolder>/<codeunitname>/Other/Artifacts/TestCoverage/TestCoverage.xml'
         which contains a test-coverage-report in the cobertura-format exists.
@@ -476,15 +485,15 @@
         versionregex = "\\d+\\.\\d+\\.\\d+"
         versiononlyregex = f"^{versionregex}$"
         pattern = re.compile(versiononlyregex)
         if pattern.match(current_version):
             GeneralUtilities.write_text_to_file(codeunit_file, re.sub(f"<codeunit:version>{versionregex}<\\/codeunit:version>",
                                                                       f"<codeunit:version>{current_version}</codeunit:version>", GeneralUtilities.read_text_from_file(codeunit_file)))
         else:
-            raise ValueError(f"Version '{current_version}' does not match version-regex '{versiononlyregex}'")
+            raise ValueError(f"Version '{current_version}' does not match version-regex '{versiononlyregex}'.")
 
     @GeneralUtilities.check_arguments
     def standardized_tasks_linting_for_dotnet_project_in_common_project_structure(self, linting_script_file: str, verbosity: int, buildenvironment: str, commandline_arguments: list[str]):
         verbosity = TasksForCommonProjectStructure.get_verbosity_from_commandline_arguments(commandline_arguments,  verbosity)
         # TODO implement function
 
     @GeneralUtilities.check_arguments
@@ -553,15 +562,15 @@
             GeneralUtilities.ensure_directory_exists(target_folder_for_codeunit)
             shutil.copytree(os.path.join(codeunit_folder, "Other", "Artifacts"), os.path.join(target_folder_for_codeunit, "Artifacts"))
 
         for codeunitname, codeunit_configuration in information.codeunits.items():
             push_artifact_to_registry_script = codeunit_configuration.push_to_registry_script
             folder = os.path.dirname(push_artifact_to_registry_script)
             file = os.path.basename(push_artifact_to_registry_script)
-            GeneralUtilities.write_message_to_stdout(f"Push buildartifact of codeunit {codeunitname}")
+            GeneralUtilities.write_message_to_stdout(f"Push buildartifact of codeunit {codeunitname}.")
             self.__sc.run_program("python", file, folder, verbosity=information.verbosity, throw_exception_if_exitcode_is_not_zero=True)
 
             # Copy reference of codeunit to reference-repository
             self.__export_codeunit_reference_content_to_reference_repository(f"v{project_version}", False, reference_repository_target_for_project, information.repository,
                                                                              codeunitname, information.projectname, codeunit_version, information.public_repository_url,
                                                                              f"v{project_version}")
             self.__export_codeunit_reference_content_to_reference_repository("Latest", True, reference_repository_target_for_project, information.repository,
@@ -648,15 +657,15 @@
         self.__sc.git_merge(repository_folder, new_version_branch_name, main_branch_name, False, True, f'Merge branch {new_version_branch_name} into {main_branch_name}')
         self.__sc.git_checkout(repository_folder, main_branch_name)
         self.__sc.git_commit(build_repository_folder, f"Updated submodule {repository_name}")
 
     @GeneralUtilities.check_arguments
     def create_release_for_project_in_standardized_release_repository_format(self, create_release_file: str, createReleaseConfiguration: CreateReleaseConfiguration):
 
-        GeneralUtilities.write_message_to_stdout(f"Create release for project {createReleaseConfiguration.projectname}")
+        GeneralUtilities.write_message_to_stdout(f"Create release for project {createReleaseConfiguration.projectname}.")
         folder_of_create_release_file_file = os.path.abspath(os.path.dirname(create_release_file))
 
         build_repository_folder = GeneralUtilities.resolve_relative_path(f"..{os.path.sep}..", folder_of_create_release_file_file)
         self.assert_no_uncommitted_changes(build_repository_folder)
 
         self.__sc.git_checkout(build_repository_folder, createReleaseConfiguration.build_repository_branch)
 
@@ -678,15 +687,15 @@
         self.__standardized_tasks_release_buildartifact_for_project_in_common_project_format(createReleaseInformation)
 
         self.__sc.git_commit(createReleaseInformation.reference_repository, f"Added reference of {createReleaseConfiguration.projectname} v{new_project_version}")
         if createReleaseConfiguration.reference_repository_remote_name is not None:
             self.__sc.git_push(createReleaseInformation.reference_repository, createReleaseConfiguration.reference_repository_remote_name, createReleaseConfiguration.reference_repository_branch_name,
                                createReleaseConfiguration.reference_repository_branch_name,  verbosity=createReleaseConfiguration.verbosity)
         self.__sc.git_commit(build_repository_folder, f"Added {createReleaseConfiguration.projectname} release v{new_project_version}")
-        GeneralUtilities.write_message_to_stdout(f"Finished release for project {createReleaseConfiguration.projectname} successfully")
+        GeneralUtilities.write_message_to_stdout(f"Finished release for project {createReleaseConfiguration.projectname} successfully.")
         return new_project_version
 
     @GeneralUtilities.check_arguments
     def create_release_starter_for_repository_in_standardized_format(self, create_release_file: str, logfile: str, verbosity: int, addLogOverhead: bool,
                                                                      commandline_arguments: list[str]):
         # hint: arguments can be overwritten by commandline_arguments
         folder_of_this_file = os.path.dirname(create_release_file)
@@ -705,18 +714,18 @@
         self.assert_no_uncommitted_changes(information.repository)
         self.__sc.git_checkout(information.repository, information.sourcebranch)
         self.__sc.run_program("git", "clean -dfx", information.repository,  verbosity=information.verbosity, throw_exception_if_exitcode_is_not_zero=True)
         project_version = self.__sc.get_semver_version_from_gitversion(information.repository)
         success = False
         try:
             for _, codeunit in information.codeunits.items():
-                GeneralUtilities.write_message_to_stdout(f"Start processing codeunit {codeunit.name}")
+                GeneralUtilities.write_message_to_stdout(f"Start processing codeunit {codeunit.name}.")
                 self.build_codeunit(os.path.join(information.repository, codeunit.name), information.verbosity,
                                     information.build_environment_for_qualitycheck, codeunit.additional_arguments_file)
-                GeneralUtilities.write_message_to_stdout(f"Finished processing codeunit {codeunit.name}")
+                GeneralUtilities.write_message_to_stdout(f"Finished processing codeunit {codeunit.name}.")
 
             self.assert_no_uncommitted_changes(information.repository)
             success = True
         except Exception as exception:
             GeneralUtilities.write_exception_to_stderr(exception, "Error while doing merge-tasks. Merge will be aborted.")
 
         if not success:
@@ -941,66 +950,71 @@
         codeunits = []
         subfolders = GeneralUtilities.get_direct_folders_of_folder(repository_folder)
         for subfolder in subfolders:
             codeunit_name = os.path.basename(subfolder)
             codeunit_file = os.path.join(subfolder, f"{codeunit_name}.codeunit.xml")
             if os.path.exists(codeunit_file):
                 codeunits.append(codeunit_name)
-        # TODO set order
+        # TODO set order (the "last" should be first to not overwrite its artifacts)
         for codeunit in codeunits:
             self.build_codeunit(os.path.join(repository_folder, codeunit), verbosity, build_environment, additional_arguments_file)
 
     @GeneralUtilities.check_arguments
     def build_codeunit(self, codeunit_folder: str, verbosity: int = 1, build_environment: str = "QualityCheck", additional_arguments_file: str = None) -> None:
         now = datetime.now()
         codeunit_folder = GeneralUtilities.resolve_relative_path_from_current_working_directory(codeunit_folder)
         codeunit_name: str = os.path.basename(codeunit_folder)
         codeunit_file = os.path.join(codeunit_folder, f"{codeunit_name}.codeunit.xml")
         if(not os.path.isfile(codeunit_file)):
             raise ValueError(f'"{codeunit_folder}" is no codeunit-folder.')
+        artifacts_folder = os.path.join(codeunit_folder, "Other", "Artifacts")
         GeneralUtilities.write_message_to_stdout(f"Start building codeunit {codeunit_name}.")
         GeneralUtilities.write_message_to_stdout(f"Build-environment: {build_environment}")
+        GeneralUtilities.ensure_directory_does_not_exist(artifacts_folder)
+
         other_folder = os.path.join(codeunit_folder, "Other")
         build_folder = os.path.join(other_folder, "Build")
         quality_folder = os.path.join(other_folder, "QualityCheck")
         reference_folder = os.path.join(other_folder, "Reference")
         sc = ScriptCollectionCore()
         additional_arguments_c: str = ""
         additional_arguments_b: str = ""
         additional_arguments_r: str = ""
         additional_arguments_l: str = ""
         additional_arguments_g: str = ""
-        if additional_arguments_file is not None:
+        general_argument = f'--overwrite_verbosity={str(verbosity)} --overwrite_buildenvironment={build_environment}'
+        if additional_arguments_file:
+            c_additional_argument = ""
+        else:
             config = configparser.ConfigParser()
             config.read(additional_arguments_file)
             section_name = f"{codeunit_name}_Configuration"
             if config.has_option(section_name, "ArgumentsForCommonTasks"):
                 additional_arguments_c = config.get(section_name, "ArgumentsForCommonTasks")
             if config.has_option(section_name, "ArgumentsForBuild"):
                 additional_arguments_b = config.get(section_name, "ArgumentsForBuild")
             if config.has_option(section_name, "ArgumentsForRunTestcases"):
                 additional_arguments_r = config.get(section_name, "ArgumentsForRunTestcases")
             if config.has_option(section_name, "ArgumentsForLinting"):
                 additional_arguments_l = config.get(section_name, "ArgumentsForLinting")
             if config.has_option(section_name, "ArgumentsForGenerateReference"):
                 additional_arguments_g = config.get(section_name, "ArgumentsForGenerateReference")
-        general_argument = f"--overwrite_verbosity={str(verbosity)} --overwrite_buildenvironment={build_environment}"
+            c_additional_argument = f'--overwrite_additionalargumentsfile="{additional_arguments_file}"'
 
         GeneralUtilities.write_message_to_stdout('Run "CommonTasks.py"...')
-        sc.run_program("python", f"CommonTasks.py {additional_arguments_c} {general_argument}", other_folder, verbosity=verbosity)
+        sc.run_program("python", f"CommonTasks.py {additional_arguments_c} {general_argument} {c_additional_argument}", other_folder, verbosity=verbosity)
         GeneralUtilities.write_message_to_stdout('Run "Build.py"...')
         sc.run_program("python", f"Build.py {additional_arguments_b} {general_argument}",  build_folder, verbosity=verbosity)
         GeneralUtilities.write_message_to_stdout('Run "RunTestcases.py"...')
         sc.run_program("python", f"RunTestcases.py {additional_arguments_r} {general_argument}", quality_folder, verbosity=verbosity)
         GeneralUtilities.write_message_to_stdout('Run "Linting.py"...')
         sc.run_program("python", f"Linting.py {additional_arguments_l} {general_argument}", quality_folder, verbosity=verbosity)
         GeneralUtilities.write_message_to_stdout('Run "GenerateReference.py"...')
         sc.run_program("python", f"GenerateReference.py {additional_arguments_g} {general_argument}", reference_folder, verbosity=verbosity)
 
-        artifacts_folder = os.path.join(codeunit_folder, "Other", "Artifacts")
         build_codeunit_info_file = os.path.join(artifacts_folder, f"{codeunit_name}.artifactsinformation.xml")
         version = self.get_version_of_codeunit(codeunit_file)
         GeneralUtilities.ensure_file_exists(build_codeunit_info_file)
         artifacts_list = []
         for artifact_folder in GeneralUtilities.get_direct_folders_of_folder(artifacts_folder):
             artifact_name = os.path.basename(artifact_folder)
             artifacts_list.append(f"        <codeunit:artifact>{artifact_name}<codeunit:artifact>")
```

## Comparing `ScriptCollection-3.3.8.dist-info/METADATA` & `ScriptCollection-3.3.9.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ScriptCollection
-Version: 3.3.8
+Version: 3.3.9
 Summary: The ScriptCollection is the place for reusable scripts.
 Author-email: Marius Göcke <marius.goecke@gmail.com>
 Project-URL: Homepage, https://github.com/anionDev/ScriptCollection
 Project-URL: Bug Tracker, https://github.com/anionDev/ScriptCollection/issues
 Classifier: Programming Language :: Python :: 3.10
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX :: Linux
```

## Comparing `ScriptCollection-3.3.8.dist-info/entry_points.txt` & `ScriptCollection-3.3.9.dist-info/entry_points.txt`

 * *Files identical despite different names*

## Comparing `ScriptCollection-3.3.8.dist-info/RECORD` & `ScriptCollection-3.3.9.dist-info/RECORD`

 * *Files 12% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 ScriptCollection/Executables.py,sha256=jUbHFxCj2DLIxnwc2jRZI4DyfN6qIoS_QOhOvSefPXQ,15739
 ScriptCollection/GeneralUtilities.py,sha256=HVQ80reebBZryk9NOhstxvD5gP9di0KO_-AI5G36WLc,31649
 ScriptCollection/Hardening.py,sha256=XRbyd3f2MEp0EDucPrKbXjvC9qqa6fYTAFWX59HYJx8,3421
 ScriptCollection/ProgramRunnerBase.py,sha256=2kyOuoM3oFjBfLc9Q5t5RTz7Ya2CjUxFtB1rBBDmnjU,1937
 ScriptCollection/ProgramRunnerEpew.py,sha256=ZiBZVMcsphmo49z2BwUwQYXo2uTKXPu33QW3IxCT46E,6273
 ScriptCollection/ProgramRunnerPopen.py,sha256=HOs1QVnXiQtwXy1_xvH79bWBdd0i-2tUyyLloQBvMto,3023
-ScriptCollection/ScriptCollectionCore.py,sha256=jqrNjHSoMYpRTEt3iwhPktgRHBx5x_tHec_Gfbp6Pco,75969
-ScriptCollection/TasksForCommonProjectStructure.py,sha256=KOPw7dlxlo8A6bomSEeFE6-3LGPcdkVOKotgOaHD57k,74143
+ScriptCollection/ScriptCollectionCore.py,sha256=3aH8OdFUwxBO-Z7oPDElDhMXKqJ4rmQTVX2uUAsYkI8,75969
+ScriptCollection/TasksForCommonProjectStructure.py,sha256=MwBwyyyO-eaEIppYHs9JrOtqbMVP_Uh7gv0xj6vcyTY,74893
 ScriptCollection/UpdateCertificates.py,sha256=Go-JJK-YTi7aBB1phlLxypa8GHkmFHBEPB0_TT9G-bw,7918
 ScriptCollection/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
-ScriptCollection-3.3.8.dist-info/METADATA,sha256=zY4-0-TNhTpHSpw33-pBMgUyrE5dmIjPpMPg55HuSNQ,7146
-ScriptCollection-3.3.8.dist-info/WHEEL,sha256=2wepM1nk4DS4eFpYrW1TTqPcoGNfHhhO_i5m4cOimbo,92
-ScriptCollection-3.3.8.dist-info/entry_points.txt,sha256=eppw-Ajd-LdXe2-4X6pgBmcqXg3TGchaiPcjRwY4R8w,1697
-ScriptCollection-3.3.8.dist-info/top_level.txt,sha256=hY2hOVH0V0Ce51WB76zKkIWTUNwMUdHo4XDkR2vYVwg,17
-ScriptCollection-3.3.8.dist-info/RECORD,,
+ScriptCollection-3.3.9.dist-info/METADATA,sha256=F-wsv1fW6XJ-KMXLHsO1yM_0swTn7lOHEhpz1y3AYnI,7146
+ScriptCollection-3.3.9.dist-info/WHEEL,sha256=2wepM1nk4DS4eFpYrW1TTqPcoGNfHhhO_i5m4cOimbo,92
+ScriptCollection-3.3.9.dist-info/entry_points.txt,sha256=eppw-Ajd-LdXe2-4X6pgBmcqXg3TGchaiPcjRwY4R8w,1697
+ScriptCollection-3.3.9.dist-info/top_level.txt,sha256=hY2hOVH0V0Ce51WB76zKkIWTUNwMUdHo4XDkR2vYVwg,17
+ScriptCollection-3.3.9.dist-info/RECORD,,
```

