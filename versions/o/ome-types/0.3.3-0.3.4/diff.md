# Comparing `tmp/ome_types-0.3.3.tar.gz` & `tmp/ome_types-0.3.4.tar.gz`

## Comparing `ome_types-0.3.3.tar` & `ome_types-0.3.4.tar`

### file list

```diff
@@ -1,168 +1,168 @@
--rw-r--r--   0        0        0    16024 2020-02-02 00:00:00.000000 ome_types-0.3.3/CHANGELOG.md
--rw-r--r--   0        0        0    40116 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_autogen.py
--rw-r--r--   0        0        0     1127 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/__init__.py
--rw-r--r--   0        0        0     6327 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/_base_type.py
--rw-r--r--   0        0        0      287 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/_constants.py
--rw-r--r--   0        0        0     6618 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/_convenience.py
--rw-r--r--   0        0        0     5454 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/_lxml.py
--rw-r--r--   0        0        0      862 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/_napari_plugin.py
--rw-r--r--   0        0        0      315 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/_units.py
--rw-r--r--   0        0        0    11500 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/_xmlschema.py
--rw-r--r--   0        0        0   285655 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/ome-2016-06.xsd
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/py.typed
--rw-r--r--   0        0        0      279 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/schema.py
--rw-r--r--   0        0        0     3450 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/util.py
--rw-r--r--   0        0        0     5316 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/widgets.py
--rw-r--r--   0        0        0    42098 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/__init__.py
--rw-r--r--   0        0        0      417 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/affine_transform.py
--rw-r--r--   0        0        0     1135 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/annotation.py
--rw-r--r--   0        0        0      349 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/annotation_ref.py
--rw-r--r--   0        0        0     1345 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/arc.py
--rw-r--r--   0        0        0      700 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/basic_annotation.py
--rw-r--r--   0        0        0     1165 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/bin_data.py
--rw-r--r--   0        0        0      618 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/binary_file.py
--rw-r--r--   0        0        0     1067 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/boolean_annotation.py
--rw-r--r--   0        0        0     7641 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/channel.py
--rw-r--r--   0        0        0      247 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/channel_ref.py
--rw-r--r--   0        0        0     1042 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/comment_annotation.py
--rw-r--r--   0        0        0     1788 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/dataset.py
--rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/dataset_ref.py
--rw-r--r--   0        0        0     2841 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/detector.py
--rw-r--r--   0        0        0     2390 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/detector_settings.py
--rw-r--r--   0        0        0      842 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/dichroic.py
--rw-r--r--   0        0        0      252 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/dichroic_ref.py
--rw-r--r--   0        0        0     1075 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/double_annotation.py
--rw-r--r--   0        0        0     2795 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/ellipse.py
--rw-r--r--   0        0        0     2124 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/experiment.py
--rw-r--r--   0        0        0      262 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/experiment_ref.py
--rw-r--r--   0        0        0     1932 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/experimenter.py
--rw-r--r--   0        0        0     1072 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/experimenter_group.py
--rw-r--r--   0        0        0      394 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/experimenter_group_ref.py
--rw-r--r--   0        0        0      407 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/experimenter_ref.py
--rw-r--r--   0        0        0      881 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/external.py
--rw-r--r--   0        0        0     1406 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/filament.py
--rw-r--r--   0        0        0     1098 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/file_annotation.py
--rw-r--r--   0        0        0     2092 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/filter.py
--rw-r--r--   0        0        0      242 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/filter_ref.py
--rw-r--r--   0        0        0     1161 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/filter_set.py
--rw-r--r--   0        0        0      257 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/filter_set_ref.py
--rw-r--r--   0        0        0     1271 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/folder.py
--rw-r--r--   0        0        0      477 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/folder_ref.py
--rw-r--r--   0        0        0     1334 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/generic_excitation_source.py
--rw-r--r--   0        0        0     4429 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/image.py
--rw-r--r--   0        0        0      284 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/image_ref.py
--rw-r--r--   0        0        0     1357 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/imaging_environment.py
--rw-r--r--   0        0        0     2944 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/instrument.py
--rw-r--r--   0        0        0      371 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/instrument_ref.py
--rw-r--r--   0        0        0     2714 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/label.py
--rw-r--r--   0        0        0     4219 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/laser.py
--rw-r--r--   0        0        0      391 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/leader.py
--rw-r--r--   0        0        0     2229 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/light_emitting_diode.py
--rw-r--r--   0        0        0      879 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/light_path.py
--rw-r--r--   0        0        0     1606 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/light_source.py
--rw-r--r--   0        0        0      392 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/light_source_group.py
--rw-r--r--   0        0        0      883 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/light_source_settings.py
--rw-r--r--   0        0        0     2927 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/line.py
--rw-r--r--   0        0        0      883 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/list_annotation.py
--rw-r--r--   0        0        0     1067 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/long_annotation.py
--rw-r--r--   0        0        0      834 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/manufacturer_spec.py
--rw-r--r--   0        0        0      883 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/map.py
--rw-r--r--   0        0        0      880 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/map_annotation.py
--rw-r--r--   0        0        0     2981 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/mask.py
--rw-r--r--   0        0        0     1590 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/microbeam_manipulation.py
--rw-r--r--   0        0        0      317 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/microbeam_manipulation_ref.py
--rw-r--r--   0        0        0      790 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/microscope.py
--rw-r--r--   0        0        0      720 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/numeric_annotation.py
--rw-r--r--   0        0        0     3904 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/objective.py
--rw-r--r--   0        0        0     1047 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/objective_settings.py
--rw-r--r--   0        0        0     7107 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/ome.py
--rw-r--r--   0        0        0     5752 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/pixels.py
--rw-r--r--   0        0        0     2494 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/plane.py
--rw-r--r--   0        0        0     4334 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/plate.py
--rw-r--r--   0        0        0     1658 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/plate_acquisition.py
--rw-r--r--   0        0        0     2495 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/point.py
--rw-r--r--   0        0        0     2717 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/polygon.py
--rw-r--r--   0        0        0     2935 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/polyline.py
--rw-r--r--   0        0        0     1395 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/project.py
--rw-r--r--   0        0        0      403 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/project_ref.py
--rw-r--r--   0        0        0      395 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/pump.py
--rw-r--r--   0        0        0      995 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/reagent.py
--rw-r--r--   0        0        0      247 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/reagent_ref.py
--rw-r--r--   0        0        0     2775 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/rectangle.py
--rw-r--r--   0        0        0      805 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/reference.py
--rw-r--r--   0        0        0      584 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/rights.py
--rw-r--r--   0        0        0     1723 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/roi.py
--rw-r--r--   0        0        0      227 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/roi_ref.py
--rw-r--r--   0        0        0     3036 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/screen.py
--rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/settings.py
--rw-r--r--   0        0        0     3818 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/shape.py
--rw-r--r--   0        0        0      378 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/shape_group.py
--rw-r--r--   0        0        0    10674 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/simple_types.py
--rw-r--r--   0        0        0     1162 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/stage_label.py
--rw-r--r--   0        0        0     1909 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/structured_annotations.py
--rw-r--r--   0        0        0     1058 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/tag_annotation.py
--rw-r--r--   0        0        0     1041 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/term_annotation.py
--rw-r--r--   0        0        0      698 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/text_annotation.py
--rw-r--r--   0        0        0     1840 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/tiff_data.py
--rw-r--r--   0        0        0     1103 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/timestamp_annotation.py
--rw-r--r--   0        0        0     2023 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/transmittance_range.py
--rw-r--r--   0        0        0      698 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/type_annotation.py
--rw-r--r--   0        0        0     2663 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/well.py
--rw-r--r--   0        0        0     1885 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/well_sample.py
--rw-r--r--   0        0        0      313 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/well_sample_ref.py
--rw-r--r--   0        0        0     2012 2020-02-02 00:00:00.000000 ome_types-0.3.3/src/ome_types/model/xml_annotation.py
--rw-r--r--   0        0        0      610 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/test_autogen.py
--rw-r--r--   0        0        0      428 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/test_invalid_schema.py
--rw-r--r--   0        0        0     8110 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/test_model.py
--rw-r--r--   0        0        0      713 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/test_serialization.py
--rw-r--r--   0        0        0     2427 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/test_units.py
--rw-r--r--   0        0        0      353 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/test_widget.py
--rw-r--r--   0        0        0    12646 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/util.py
--rw-r--r--   0        0        0     2341 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/OverViewScan.ome.xml
--rw-r--r--   0        0        0     2697 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/ROI.ome.xml
--rw-r--r--   0        0        0      788 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/bad.ome.xml
--rw-r--r--   0        0        0      981 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/commentannotation.ome.xml
--rw-r--r--   0        0        0    47901 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/example.ome.xml
--rw-r--r--   0        0        0     8070 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/fake-plate-rows-2.ome.xml
--rw-r--r--   0        0        0     3915 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/filter.ome.xml
--rw-r--r--   0        0        0   267379 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/folders-larger-taxonomy.ome.xml
--rw-r--r--   0        0        0   264656 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/folders-simple-taxonomy.ome.xml
--rw-r--r--   0        0        0     2419 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/hcs.ome.xml
--rw-r--r--   0        0        0     4417 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/instrument-units-alternate.ome.xml
--rw-r--r--   0        0        0     4388 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/instrument-units-default.ome.xml
--rw-r--r--   0        0        0     3528 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/instrument.ome.xml
--rw-r--r--   0        0        0     3894 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/invalid_xml_annotation.ome.xml
--rw-r--r--   0        0        0     1333 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/mapannotation.ome.xml
--rw-r--r--   0        0        0      669 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/metadata-only.ome.xml
--rw-r--r--   0        0        0      682 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/minimum-specification.ome.xml
--rw-r--r--   0        0        0     7229 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/multi-channel-time-series.ome.xml
--rw-r--r--   0        0        0    33349 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/multi-channel-z-series-time-series.ome.xml
--rw-r--r--   0        0        0     7229 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/multi-channel-z-series.ome.xml
--rw-r--r--   0        0        0     1287 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/multi-channel.ome.xml
--rw-r--r--   0        0        0      741 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/no-date.ome.xml
--rw-r--r--   0        0        0     1166 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/ome.tiff
--rw-r--r--   0        0        0    12159 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/ome_ns.ome.xml
--rw-r--r--   0        0        0     8221 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/one-screen-one-plate-four-wells.ome.xml
--rw-r--r--   0        0        0     6373 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/shape-union.ome.xml
--rw-r--r--   0        0        0      796 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/single-image.ome.xml
--rw-r--r--   0        0        0     1794 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/small.ome.xml
--rw-r--r--   0        0        0    23160 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/spim.ome.xml
--rw-r--r--   0        0        0     1550 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/tagannotation.ome.xml
--rw-r--r--   0        0        0     3908 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/time-series.ome.xml
--rw-r--r--   0        0        0     8804 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/timestampannotation-posix-only.ome.xml
--rw-r--r--   0        0        0    10151 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/timestampannotation.ome.xml
--rw-r--r--   0        0        0     8041 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/transformations-downgrade.ome.xml
--rw-r--r--   0        0        0     8348 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/transformations-upgrade.ome.xml
--rw-r--r--   0        0        0    13260 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/tubhiswt.ome.xml
--rw-r--r--   0        0        0    15861 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/two-screens-two-plates-four-wells.ome.xml
--rw-r--r--   0        0        0     1473 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/xmlannotation-body-space.ome.xml
--rw-r--r--   0        0        0     1143 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/xmlannotation-multi-value.ome.xml
--rw-r--r--   0        0        0     3364 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/xmlannotation-svg.ome.xml
--rw-r--r--   0        0        0    16972 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/z-series-time-series.ome.xml
--rw-r--r--   0        0        0     3912 2020-02-02 00:00:00.000000 ome_types-0.3.3/tests/data/z-series.ome.xml
--rw-r--r--   0        0        0     1328 2020-02-02 00:00:00.000000 ome_types-0.3.3/.gitignore
--rw-r--r--   0        0        0     1071 2020-02-02 00:00:00.000000 ome_types-0.3.3/LICENSE
--rw-r--r--   0        0        0     9466 2020-02-02 00:00:00.000000 ome_types-0.3.3/README.md
--rw-r--r--   0        0        0      412 2020-02-02 00:00:00.000000 ome_types-0.3.3/hatch_build.py
--rw-r--r--   0        0        0     4376 2020-02-02 00:00:00.000000 ome_types-0.3.3/pyproject.toml
--rw-r--r--   0        0        0    11470 2020-02-02 00:00:00.000000 ome_types-0.3.3/PKG-INFO
+-rw-r--r--   0        0        0    16554 2020-02-02 00:00:00.000000 ome_types-0.3.4/CHANGELOG.md
+-rw-r--r--   0        0        0    40113 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_autogen.py
+-rw-r--r--   0        0        0     1127 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/__init__.py
+-rw-r--r--   0        0        0     6327 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/_base_type.py
+-rw-r--r--   0        0        0      287 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/_constants.py
+-rw-r--r--   0        0        0     6700 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/_convenience.py
+-rw-r--r--   0        0        0     7055 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/_lxml.py
+-rw-r--r--   0        0        0      862 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/_napari_plugin.py
+-rw-r--r--   0        0        0      315 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/_units.py
+-rw-r--r--   0        0        0    11599 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/_xmlschema.py
+-rw-r--r--   0        0        0   285655 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/ome-2016-06.xsd
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/py.typed
+-rw-r--r--   0        0        0      279 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/schema.py
+-rw-r--r--   0        0        0     3450 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/util.py
+-rw-r--r--   0        0        0     5382 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/widgets.py
+-rw-r--r--   0        0        0    42098 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/__init__.py
+-rw-r--r--   0        0        0      417 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/affine_transform.py
+-rw-r--r--   0        0        0     1135 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/annotation.py
+-rw-r--r--   0        0        0      349 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/annotation_ref.py
+-rw-r--r--   0        0        0     1345 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/arc.py
+-rw-r--r--   0        0        0      700 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/basic_annotation.py
+-rw-r--r--   0        0        0     1165 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/bin_data.py
+-rw-r--r--   0        0        0      618 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/binary_file.py
+-rw-r--r--   0        0        0     1067 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/boolean_annotation.py
+-rw-r--r--   0        0        0     7641 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/channel.py
+-rw-r--r--   0        0        0      247 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/channel_ref.py
+-rw-r--r--   0        0        0     1042 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/comment_annotation.py
+-rw-r--r--   0        0        0     1788 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/dataset.py
+-rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/dataset_ref.py
+-rw-r--r--   0        0        0     2841 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/detector.py
+-rw-r--r--   0        0        0     2390 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/detector_settings.py
+-rw-r--r--   0        0        0      842 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/dichroic.py
+-rw-r--r--   0        0        0      252 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/dichroic_ref.py
+-rw-r--r--   0        0        0     1075 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/double_annotation.py
+-rw-r--r--   0        0        0     2795 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/ellipse.py
+-rw-r--r--   0        0        0     2124 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/experiment.py
+-rw-r--r--   0        0        0      262 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/experiment_ref.py
+-rw-r--r--   0        0        0     1932 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/experimenter.py
+-rw-r--r--   0        0        0     1072 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/experimenter_group.py
+-rw-r--r--   0        0        0      394 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/experimenter_group_ref.py
+-rw-r--r--   0        0        0      407 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/experimenter_ref.py
+-rw-r--r--   0        0        0      881 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/external.py
+-rw-r--r--   0        0        0     1406 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/filament.py
+-rw-r--r--   0        0        0     1098 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/file_annotation.py
+-rw-r--r--   0        0        0     2092 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/filter.py
+-rw-r--r--   0        0        0      242 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/filter_ref.py
+-rw-r--r--   0        0        0     1161 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/filter_set.py
+-rw-r--r--   0        0        0      257 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/filter_set_ref.py
+-rw-r--r--   0        0        0     1271 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/folder.py
+-rw-r--r--   0        0        0      477 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/folder_ref.py
+-rw-r--r--   0        0        0     1334 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/generic_excitation_source.py
+-rw-r--r--   0        0        0     4429 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/image.py
+-rw-r--r--   0        0        0      284 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/image_ref.py
+-rw-r--r--   0        0        0     1357 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/imaging_environment.py
+-rw-r--r--   0        0        0     2944 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/instrument.py
+-rw-r--r--   0        0        0      371 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/instrument_ref.py
+-rw-r--r--   0        0        0     2714 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/label.py
+-rw-r--r--   0        0        0     4219 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/laser.py
+-rw-r--r--   0        0        0      391 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/leader.py
+-rw-r--r--   0        0        0     2229 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/light_emitting_diode.py
+-rw-r--r--   0        0        0      879 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/light_path.py
+-rw-r--r--   0        0        0     1606 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/light_source.py
+-rw-r--r--   0        0        0      392 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/light_source_group.py
+-rw-r--r--   0        0        0      883 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/light_source_settings.py
+-rw-r--r--   0        0        0     2927 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/line.py
+-rw-r--r--   0        0        0      883 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/list_annotation.py
+-rw-r--r--   0        0        0     1067 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/long_annotation.py
+-rw-r--r--   0        0        0      834 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/manufacturer_spec.py
+-rw-r--r--   0        0        0      883 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/map.py
+-rw-r--r--   0        0        0      880 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/map_annotation.py
+-rw-r--r--   0        0        0     2981 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/mask.py
+-rw-r--r--   0        0        0     1590 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/microbeam_manipulation.py
+-rw-r--r--   0        0        0      317 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/microbeam_manipulation_ref.py
+-rw-r--r--   0        0        0      790 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/microscope.py
+-rw-r--r--   0        0        0      720 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/numeric_annotation.py
+-rw-r--r--   0        0        0     3904 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/objective.py
+-rw-r--r--   0        0        0     1047 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/objective_settings.py
+-rw-r--r--   0        0        0     7107 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/ome.py
+-rw-r--r--   0        0        0     5752 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/pixels.py
+-rw-r--r--   0        0        0     2494 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/plane.py
+-rw-r--r--   0        0        0     4334 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/plate.py
+-rw-r--r--   0        0        0     1658 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/plate_acquisition.py
+-rw-r--r--   0        0        0     2495 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/point.py
+-rw-r--r--   0        0        0     2717 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/polygon.py
+-rw-r--r--   0        0        0     2935 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/polyline.py
+-rw-r--r--   0        0        0     1395 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/project.py
+-rw-r--r--   0        0        0      403 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/project_ref.py
+-rw-r--r--   0        0        0      395 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/pump.py
+-rw-r--r--   0        0        0      995 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/reagent.py
+-rw-r--r--   0        0        0      247 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/reagent_ref.py
+-rw-r--r--   0        0        0     2775 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/rectangle.py
+-rw-r--r--   0        0        0      805 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/reference.py
+-rw-r--r--   0        0        0      584 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/rights.py
+-rw-r--r--   0        0        0     1723 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/roi.py
+-rw-r--r--   0        0        0      227 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/roi_ref.py
+-rw-r--r--   0        0        0     3036 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/screen.py
+-rw-r--r--   0        0        0      447 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/settings.py
+-rw-r--r--   0        0        0     3818 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/shape.py
+-rw-r--r--   0        0        0      378 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/shape_group.py
+-rw-r--r--   0        0        0    10674 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/simple_types.py
+-rw-r--r--   0        0        0     1162 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/stage_label.py
+-rw-r--r--   0        0        0     1909 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/structured_annotations.py
+-rw-r--r--   0        0        0     1058 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/tag_annotation.py
+-rw-r--r--   0        0        0     1041 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/term_annotation.py
+-rw-r--r--   0        0        0      698 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/text_annotation.py
+-rw-r--r--   0        0        0     1840 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/tiff_data.py
+-rw-r--r--   0        0        0     1103 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/timestamp_annotation.py
+-rw-r--r--   0        0        0     2023 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/transmittance_range.py
+-rw-r--r--   0        0        0      698 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/type_annotation.py
+-rw-r--r--   0        0        0     2663 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/well.py
+-rw-r--r--   0        0        0     1885 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/well_sample.py
+-rw-r--r--   0        0        0      313 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/well_sample_ref.py
+-rw-r--r--   0        0        0     2012 2020-02-02 00:00:00.000000 ome_types-0.3.4/src/ome_types/model/xml_annotation.py
+-rw-r--r--   0        0        0      610 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/test_autogen.py
+-rw-r--r--   0        0        0      428 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/test_invalid_schema.py
+-rw-r--r--   0        0        0     8197 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/test_model.py
+-rw-r--r--   0        0        0      713 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/test_serialization.py
+-rw-r--r--   0        0        0     2427 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/test_units.py
+-rw-r--r--   0        0        0      353 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/test_widget.py
+-rw-r--r--   0        0        0    12646 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/util.py
+-rw-r--r--   0        0        0     2341 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/OverViewScan.ome.xml
+-rw-r--r--   0        0        0     2697 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/ROI.ome.xml
+-rw-r--r--   0        0        0      788 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/bad.ome.xml
+-rw-r--r--   0        0        0      981 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/commentannotation.ome.xml
+-rw-r--r--   0        0        0    47901 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/example.ome.xml
+-rw-r--r--   0        0        0     8070 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/fake-plate-rows-2.ome.xml
+-rw-r--r--   0        0        0     3915 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/filter.ome.xml
+-rw-r--r--   0        0        0   267379 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/folders-larger-taxonomy.ome.xml
+-rw-r--r--   0        0        0   264656 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/folders-simple-taxonomy.ome.xml
+-rw-r--r--   0        0        0     2419 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/hcs.ome.xml
+-rw-r--r--   0        0        0     4417 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/instrument-units-alternate.ome.xml
+-rw-r--r--   0        0        0     4388 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/instrument-units-default.ome.xml
+-rw-r--r--   0        0        0     3528 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/instrument.ome.xml
+-rw-r--r--   0        0        0     3894 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/invalid_xml_annotation.ome.xml
+-rw-r--r--   0        0        0     1333 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/mapannotation.ome.xml
+-rw-r--r--   0        0        0      669 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/metadata-only.ome.xml
+-rw-r--r--   0        0        0      682 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/minimum-specification.ome.xml
+-rw-r--r--   0        0        0     7229 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/multi-channel-time-series.ome.xml
+-rw-r--r--   0        0        0    33349 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/multi-channel-z-series-time-series.ome.xml
+-rw-r--r--   0        0        0     7229 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/multi-channel-z-series.ome.xml
+-rw-r--r--   0        0        0     1287 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/multi-channel.ome.xml
+-rw-r--r--   0        0        0      741 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/no-date.ome.xml
+-rw-r--r--   0        0        0     1166 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/ome.tiff
+-rw-r--r--   0        0        0    12159 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/ome_ns.ome.xml
+-rw-r--r--   0        0        0     8221 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/one-screen-one-plate-four-wells.ome.xml
+-rw-r--r--   0        0        0     6373 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/shape-union.ome.xml
+-rw-r--r--   0        0        0      796 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/single-image.ome.xml
+-rw-r--r--   0        0        0     1794 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/small.ome.xml
+-rw-r--r--   0        0        0    23160 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/spim.ome.xml
+-rw-r--r--   0        0        0     1550 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/tagannotation.ome.xml
+-rw-r--r--   0        0        0     3908 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/time-series.ome.xml
+-rw-r--r--   0        0        0     8804 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/timestampannotation-posix-only.ome.xml
+-rw-r--r--   0        0        0    10151 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/timestampannotation.ome.xml
+-rw-r--r--   0        0        0     8041 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/transformations-downgrade.ome.xml
+-rw-r--r--   0        0        0     8348 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/transformations-upgrade.ome.xml
+-rw-r--r--   0        0        0    13260 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/tubhiswt.ome.xml
+-rw-r--r--   0        0        0    15861 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/two-screens-two-plates-four-wells.ome.xml
+-rw-r--r--   0        0        0     1473 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/xmlannotation-body-space.ome.xml
+-rw-r--r--   0        0        0     1143 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/xmlannotation-multi-value.ome.xml
+-rw-r--r--   0        0        0     3364 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/xmlannotation-svg.ome.xml
+-rw-r--r--   0        0        0    16972 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/z-series-time-series.ome.xml
+-rw-r--r--   0        0        0     3912 2020-02-02 00:00:00.000000 ome_types-0.3.4/tests/data/z-series.ome.xml
+-rw-r--r--   0        0        0     1328 2020-02-02 00:00:00.000000 ome_types-0.3.4/.gitignore
+-rw-r--r--   0        0        0     1071 2020-02-02 00:00:00.000000 ome_types-0.3.4/LICENSE
+-rw-r--r--   0        0        0     9466 2020-02-02 00:00:00.000000 ome_types-0.3.4/README.md
+-rw-r--r--   0        0        0      412 2020-02-02 00:00:00.000000 ome_types-0.3.4/hatch_build.py
+-rw-r--r--   0        0        0     4382 2020-02-02 00:00:00.000000 ome_types-0.3.4/pyproject.toml
+-rw-r--r--   0        0        0    11475 2020-02-02 00:00:00.000000 ome_types-0.3.4/PKG-INFO
```

### Comparing `ome_types-0.3.3/CHANGELOG.md` & `ome_types-0.3.4/CHANGELOG.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,21 @@
 # Changelog
 
+## [0.3.4](https://github.com/tlambert03/ome-types/tree/0.3.4) (2023-04-06)
+
+[Full Changelog](https://github.com/tlambert03/ome-types/compare/v0.3.3...0.3.4)
+
+**Implemented enhancements:**
+
+- feat: make lxml optional \(but don't yet remove from requirements\) [\#166](https://github.com/tlambert03/ome-types/pull/166) ([tlambert03](https://github.com/tlambert03))
+
+**Fixed bugs:**
+
+- fix: always get schema in xmlschema2dict [\#169](https://github.com/tlambert03/ome-types/pull/169) ([tlambert03](https://github.com/tlambert03))
+
 ## [v0.3.3](https://github.com/tlambert03/ome-types/tree/v0.3.3) (2023-01-29)
 
 [Full Changelog](https://github.com/tlambert03/ome-types/compare/v0.3.2...v0.3.3)
 
 **Fixed bugs:**
 
 - fix: prevent unset color from getting output in the XML [\#164](https://github.com/tlambert03/ome-types/pull/164) ([tlambert03](https://github.com/tlambert03))
```

### Comparing `ome_types-0.3.3/src/ome_autogen.py` & `ome_types-0.3.4/src/ome_autogen.py`

 * *Files 1% similar despite different names*

```diff
@@ -361,15 +361,14 @@
         fields='kind: Literal["ellipse"] = "ellipse"',
         imports="from typing_extensions import Literal",
     ),
 }
 
 
 def autoflake(text: str, **kwargs: Any) -> str:
-
     kwargs.setdefault("remove_all_unused_imports", True)
     kwargs.setdefault("remove_unused_variables", True)
     return fix_code(text, **kwargs)
 
 
 def black_format(text: str, line_length: int = 88) -> str:
     return black.format_str(text, mode=black.FileMode(line_length=line_length))
@@ -778,15 +777,15 @@
     def body(self) -> str:
         if self.key in OVERRIDES:
             return OVERRIDES[self.key].body or ""
         return ""
 
     @property
     def type_string(self) -> str:
-        """single type, without Optional, etc..."""
+        """Single type, without Optional, etc..."""
         if self.key in OVERRIDES:
             return OVERRIDES[self.key].type_
         if isinstance(self.component, (XsdAnyElement, XsdAnyAttribute)):
             return "Any"
         if self.component.ref is not None:
             if not self.component.ref.is_global():
                 raise ValueError("local ref not supported")
@@ -809,15 +808,15 @@
                 return self.component.local_name
             if self.type.base_type.local_name == "string":
                 return "str"
         return ""
 
     @property
     def full_type_string(self) -> str:
-        """full type, like Optional[List[str]]."""
+        """Full type, like Optional[List[str]]."""
         if self.key in OVERRIDES and self.type_string:
             return f": {self.type_string}"
         type_string = self.type_string
         if not type_string:
             return ""
         if not self.max_occurs:
             LISTS[self.parent_name].add(self.component.local_name)
@@ -915,15 +914,15 @@
     def has_non_default_args(self) -> bool:
         return any(not m.default_val_str for m in self._members)
 
     def has_nonref_id(self) -> bool:
         return any(m.is_nonref_id for m in self._members)
 
     @property
-    def non_defaults(self) -> "MemberSet":
+    def non_defaults(self) -> MemberSet:
         return MemberSet(m for m in self._members if not m.default_val_str)
 
     def __iter__(self) -> Iterator[Member]:
         return iter(self._members)
 
     def docstring(self, summary: str = "") -> str:
         ds = NumpyDocString(summary)
```

### Comparing `ome_types-0.3.3/src/ome_types/__init__.py` & `ome_types-0.3.4/src/ome_types/__init__.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/_base_type.py` & `ome_types-0.3.4/src/ome_types/_base_type.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/_convenience.py` & `ome_types-0.3.4/src/ome_types/_convenience.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,19 @@
 import os
 from pathlib import Path
-from typing import Any, Dict, Optional, Union, cast
+from typing import TYPE_CHECKING, Any, Dict, Optional, Union, cast
 from warnings import warn
 
 from typing_extensions import Protocol
 
 from .model import OME
 
+if TYPE_CHECKING:
+    from ._xmlschema import XMLSourceType
+
 
 class Parser(Protocol):
     # Used for type checks on xml parsers
     def __call__(
         self, path_or_str: Union[Path, str, bytes], validate: Optional[bool] = False
     ) -> Dict[str, Any]:
         ...
@@ -56,25 +59,28 @@
             FutureWarning,
             stacklevel=2,
         )
         parser = "xmlschema"
 
     if isinstance(parser, str):
         if parser == "lxml":
-            from ._lxml import lxml2dict
+            from ._lxml import xml2dict
 
-            parser = cast(Parser, lxml2dict)
+            parser = cast(Parser, xml2dict)
         elif parser == "xmlschema":
             from ._xmlschema import xmlschema2dict
 
             parser = cast(Parser, xmlschema2dict)
         else:
             raise KeyError("parser string must be one of {'lxml', 'xmlschema'}")
 
-    d = parser(xml) if validate is None else parser(xml, validate=validate)
+    if validate is True:
+        validate_xml(xml)
+
+    d = parser(xml)
     for key in list(d.keys()):
         if key.startswith(("xml", "xsi")):
             d.pop(key)
     return d
 
 
 def from_xml(
@@ -212,11 +218,11 @@
         The XML string of the OME object.
     """
     from ._xmlschema import to_xml
 
     return to_xml(ome, **kwargs)
 
 
-def validate_xml(xml: str, schema: Any = None) -> None:
+def validate_xml(xml: "XMLSourceType", schema: Any = None) -> None:
     from ._xmlschema import validate
 
     validate(xml, schema=schema)
```

### Comparing `ome_types-0.3.3/src/ome_types/_napari_plugin.py` & `ome_types-0.3.4/src/ome_types/_napari_plugin.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/_xmlschema.py` & `ome_types-0.3.4/src/ome_types/_xmlschema.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,19 +1,22 @@
+from __future__ import annotations
+
 import os.path
 from collections import defaultdict
 from datetime import datetime
 from enum import Enum
 from functools import lru_cache
-from typing import Any, Dict, Optional, Tuple, Union
+from pathlib import Path
+from typing import IO, Any, Union
 from xml.etree import ElementTree
 
 import xmlschema
 from xmlschema import ElementData, XMLSchemaParseError
 from xmlschema.converters import XMLSchemaConverter
-from xmlschema.documents import XMLSchemaValueError
+from xmlschema.exceptions import XMLSchemaValueError
 
 from ome_types._base_type import OMEType
 
 from . import util
 from ._constants import NS_OME, NS_XSI, OME_2016_06_XSD, SCHEMA_LOC_OME, URI_OME
 from .model import (
     OME,
@@ -21,22 +24,24 @@
     _camel_to_snake,
     _plural_to_singular,
     _singular_to_plural,
     _snake_to_camel,
     simple_types,
 )
 
-__cache__: Dict[str, xmlschema.XMLSchema] = {}
-_XMLSCHEMA_VERSION: Tuple[int, ...] = tuple(
+__cache__: dict[str, xmlschema.XMLSchema] = {}
+_XMLSCHEMA_VERSION: tuple[int, ...] = tuple(
     int(v) if v.isnumeric() else v for v in xmlschema.__version__.split(".")
 )
 
+XMLSourceType = Union[str, bytes, Path, IO[str], IO[bytes]]
+
 
 @lru_cache(maxsize=8)
-def _build_schema(ns: str, uri: Optional[str] = None) -> xmlschema.XMLSchema:
+def _build_schema(ns: str, uri: str | None = None) -> xmlschema.XMLSchema:
     """Return Schema object for a url.
 
     For the special case of retrieving the 2016-06 OME Schema, use local file.
     """
     if ns == URI_OME:
         schema = xmlschema.XMLSchema(OME_2016_06_XSD)
         # FIXME Hack to work around xmlschema poor support for keyrefs to
@@ -45,15 +50,15 @@
         ls_id_maps = schema.maps.identities[f"{NS_OME}LightSourceIDKey"]
         ls_id_maps.elements = {e: None for e in ls_sgs}
     else:
         schema = xmlschema.XMLSchema(uri)
     return schema
 
 
-def get_schema(source: Union[xmlschema.XMLResource, str]) -> xmlschema.XMLSchema:
+def get_schema(source: xmlschema.XMLResource | XMLSourceType) -> xmlschema.XMLSchema:
     """Fetch an XMLSchema object given XML source.
 
     Parameters
     ----------
     source : XMLResource or str
         can be an :class:`xmlschema.XMLResource` instance, a file-like object, a path
         to a file or an URI of a resource or an Element instance or an ElementTree
@@ -71,22 +76,22 @@
         try:
             return _build_schema(ns, uri)
         except XMLSchemaParseError:
             pass
     raise XMLSchemaValueError(f"Could not find a schema for XML resource {source!r}.")
 
 
-def validate(xml: str, schema: Optional[xmlschema.XMLSchema] = None) -> None:
+def validate(xml: XMLSourceType, schema: xmlschema.XMLSchema | None = None) -> None:
     schema = schema or get_schema(xml)
     schema.validate(xml)
 
 
 class OMEConverter(XMLSchemaConverter):
     def __init__(
-        self, namespaces: Optional[Dict[str, Any]] = None, **kwargs: Dict[Any, Any]
+        self, namespaces: dict[str, Any] | None = None, **kwargs: dict[Any, Any]
     ):
         self._ome_ns = ""
         super().__init__(namespaces, attr_prefix="")
         for name, uri in self._namespaces.items():
             if uri == URI_OME:
                 self._ome_ns = name
 
@@ -218,24 +223,23 @@
                     names = [name] * len(value)
                 content.extend([(f"{NS_OME}{n}", v) for n, v in zip(names, value)])
         return ElementData(tag, text, content, attributes)
 
 
 def xmlschema2dict(
     xml: str,
-    schema: Optional[xmlschema.XMLSchema] = None,
+    schema: xmlschema.XMLSchema | None = None,
     converter: XMLSchemaConverter = OMEConverter,
     validate: bool = False,
     **kwargs: Any,
-) -> Dict[str, Any]:
+) -> dict[str, Any]:
     if isinstance(xml, bytes):
         xml = xml.decode("utf-8")
 
-    if validate:
-        schema = schema or get_schema(xml)
+    schema = schema or get_schema(xml)
 
     if _XMLSCHEMA_VERSION >= (2,):
         kwargs["validation"] = "strict" if validate else "lax"
 
     result = xmlschema.to_dict(xml, schema=schema, converter=converter, **kwargs)
 
     if _XMLSCHEMA_VERSION >= (2,) and not validate:
@@ -252,15 +256,15 @@
                 # determine if we're dealing with a raw XML string or a filepath
                 # very long XML strings will raise ValueError on Windows.
                 try:
                     _xml = xml if os.path.exists(xml) else StringIO(xml)
                 except ValueError:
                     _xml = StringIO(xml)
 
-                tree = ElementTree.parse(_xml)  # type: ignore
+                tree = ElementTree.parse(_xml)  # type: ignore  # noqa: S314
             aid = annotation["id"]
             elt = tree.find(f".//{NS_OME}XMLAnnotation[@ID='{aid}']/{NS_OME}Value")
             annotation["value"] = elt
     return result
 
 
 def to_xml_element(ome: OME) -> ElementTree.Element:
```

### Comparing `ome_types-0.3.3/src/ome_types/ome-2016-06.xsd` & `ome_types-0.3.4/src/ome_types/ome-2016-06.xsd`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/util.py` & `ome_types-0.3.4/src/ome_types/util.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/widgets.py` & `ome_types-0.3.4/src/ome_types/widgets.py`

 * *Files 2% similar despite different names*

```diff
@@ -95,18 +95,20 @@
                 return
             try:
                 if ome.endswith(".xml"):
                     _ome = OME.from_xml(ome)
                 elif ome.lower().endswith((".tif", ".tiff")):
                     _ome = OME.from_tiff(ome)
                 else:
-                    warnings.warn(f"Unrecognized file type: {ome}")
+                    warnings.warn(f"Unrecognized file type: {ome}", stacklevel=2)
                     return
             except Exception as e:
-                warnings.warn(f"Could not parse OME metadata from {ome}: {e}")
+                warnings.warn(
+                    f"Could not parse OME metadata from {ome}: {e}", stacklevel=2
+                )
                 return
             self.headerItem().setText(0, os.path.basename(ome))
             self._current_path = ome
         else:
             raise TypeError("must be OME object or string")
         self._fill_item(_ome.dict(exclude_unset=True))
```

### Comparing `ome_types-0.3.3/src/ome_types/model/__init__.py` & `ome_types-0.3.4/src/ome_types/model/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -1267,51 +1267,51 @@
 
 _lists = {
     "Annotation": {"AnnotationRef"},
     "LightSource": {"AnnotationRef"},
     "Map": {"M"},
     "Shape": {"AnnotationRef"},
     "OME": {
-        "Experimenter",
         "Dataset",
         "Instrument",
-        "Screen",
+        "Experimenter",
+        "Experiment",
+        "Folder",
         "ExperimenterGroup",
-        "Image",
         "Project",
-        "Experiment",
         "ROI",
-        "Folder",
+        "Image",
+        "Screen",
         "Plate",
     },
-    "Image": {"MicrobeamManipulationRef", "AnnotationRef", "ROIRef"},
-    "Pixels": {"Plane", "TiffData", "Channel", "BinData"},
+    "Image": {"MicrobeamManipulationRef", "ROIRef", "AnnotationRef"},
+    "Pixels": {"TiffData", "Channel", "BinData", "Plane"},
     "Plane": {"AnnotationRef"},
     "Channel": {"AnnotationRef"},
-    "MicrobeamManipulation": {"Type", "ROIRef", "LightSourceSettings"},
+    "MicrobeamManipulation": {"LightSourceSettings", "ROIRef", "Type"},
     "Instrument": {
-        "Filter",
-        "FilterSet",
-        "Detector",
+        "Dichroic",
         "AnnotationRef",
         "Objective",
-        "Dichroic",
+        "Detector",
+        "Filter",
+        "FilterSet",
     },
-    "Project": {"DatasetRef", "AnnotationRef"},
-    "ExperimenterGroup": {"Leader", "AnnotationRef", "ExperimenterRef"},
+    "Project": {"AnnotationRef", "DatasetRef"},
+    "ExperimenterGroup": {"Leader", "ExperimenterRef", "AnnotationRef"},
     "Dataset": {"ImageRef", "AnnotationRef"},
-    "Experiment": {"Type", "MicrobeamManipulation"},
+    "Experiment": {"MicrobeamManipulation", "Type"},
     "Experimenter": {"AnnotationRef"},
-    "Folder": {"FolderRef", "AnnotationRef", "ImageRef", "ROIRef"},
+    "Folder": {"ImageRef", "ROIRef", "AnnotationRef", "FolderRef"},
     "Objective": {"AnnotationRef"},
     "Detector": {"AnnotationRef"},
     "FilterSet": {"ExcitationFilterRef", "EmissionFilterRef"},
     "Filter": {"AnnotationRef"},
     "Dichroic": {"AnnotationRef"},
-    "LightPath": {"ExcitationFilterRef", "AnnotationRef", "EmissionFilterRef"},
+    "LightPath": {"ExcitationFilterRef", "EmissionFilterRef", "AnnotationRef"},
     "ROI": {"AnnotationRef"},
-    "Plate": {"PlateAcquisition", "AnnotationRef", "Well"},
+    "Plate": {"AnnotationRef", "PlateAcquisition", "Well"},
     "Reagent": {"AnnotationRef"},
-    "Screen": {"Reagent", "AnnotationRef", "PlateRef"},
-    "PlateAcquisition": {"WellSampleRef", "AnnotationRef"},
-    "Well": {"AnnotationRef", "WellSample"},
+    "Screen": {"AnnotationRef", "PlateRef", "Reagent"},
+    "PlateAcquisition": {"AnnotationRef", "WellSampleRef"},
+    "Well": {"WellSample", "AnnotationRef"},
 }
```

### Comparing `ome_types-0.3.3/src/ome_types/model/annotation.py` & `ome_types-0.3.4/src/ome_types/model/annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/arc.py` & `ome_types-0.3.4/src/ome_types/model/arc.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/basic_annotation.py` & `ome_types-0.3.4/src/ome_types/model/basic_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/bin_data.py` & `ome_types-0.3.4/src/ome_types/model/bin_data.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/binary_file.py` & `ome_types-0.3.4/src/ome_types/model/binary_file.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/boolean_annotation.py` & `ome_types-0.3.4/src/ome_types/model/boolean_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/channel.py` & `ome_types-0.3.4/src/ome_types/model/channel.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/comment_annotation.py` & `ome_types-0.3.4/src/ome_types/model/comment_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/dataset.py` & `ome_types-0.3.4/src/ome_types/model/dataset.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/detector.py` & `ome_types-0.3.4/src/ome_types/model/detector.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/detector_settings.py` & `ome_types-0.3.4/src/ome_types/model/detector_settings.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/dichroic.py` & `ome_types-0.3.4/src/ome_types/model/dichroic.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/double_annotation.py` & `ome_types-0.3.4/src/ome_types/model/double_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/ellipse.py` & `ome_types-0.3.4/src/ome_types/model/ellipse.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/experiment.py` & `ome_types-0.3.4/src/ome_types/model/experiment.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/experimenter.py` & `ome_types-0.3.4/src/ome_types/model/experimenter.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/experimenter_group.py` & `ome_types-0.3.4/src/ome_types/model/experimenter_group.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/external.py` & `ome_types-0.3.4/src/ome_types/model/external.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/filament.py` & `ome_types-0.3.4/src/ome_types/model/filament.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/file_annotation.py` & `ome_types-0.3.4/src/ome_types/model/file_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/filter.py` & `ome_types-0.3.4/src/ome_types/model/filter.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/filter_set.py` & `ome_types-0.3.4/src/ome_types/model/filter_set.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/folder.py` & `ome_types-0.3.4/src/ome_types/model/folder.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/generic_excitation_source.py` & `ome_types-0.3.4/src/ome_types/model/generic_excitation_source.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/image.py` & `ome_types-0.3.4/src/ome_types/model/image.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/imaging_environment.py` & `ome_types-0.3.4/src/ome_types/model/imaging_environment.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/instrument.py` & `ome_types-0.3.4/src/ome_types/model/instrument.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/label.py` & `ome_types-0.3.4/src/ome_types/model/label.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/laser.py` & `ome_types-0.3.4/src/ome_types/model/laser.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/light_emitting_diode.py` & `ome_types-0.3.4/src/ome_types/model/light_emitting_diode.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/light_path.py` & `ome_types-0.3.4/src/ome_types/model/light_path.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/light_source.py` & `ome_types-0.3.4/src/ome_types/model/light_source.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/light_source_settings.py` & `ome_types-0.3.4/src/ome_types/model/light_source_settings.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/line.py` & `ome_types-0.3.4/src/ome_types/model/line.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/list_annotation.py` & `ome_types-0.3.4/src/ome_types/model/list_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/long_annotation.py` & `ome_types-0.3.4/src/ome_types/model/long_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/manufacturer_spec.py` & `ome_types-0.3.4/src/ome_types/model/manufacturer_spec.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/map.py` & `ome_types-0.3.4/src/ome_types/model/map.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/map_annotation.py` & `ome_types-0.3.4/src/ome_types/model/map_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/mask.py` & `ome_types-0.3.4/src/ome_types/model/mask.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/microbeam_manipulation.py` & `ome_types-0.3.4/src/ome_types/model/microbeam_manipulation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/microscope.py` & `ome_types-0.3.4/src/ome_types/model/microscope.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/numeric_annotation.py` & `ome_types-0.3.4/src/ome_types/model/numeric_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/objective.py` & `ome_types-0.3.4/src/ome_types/model/objective.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/objective_settings.py` & `ome_types-0.3.4/src/ome_types/model/objective_settings.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/ome.py` & `ome_types-0.3.4/src/ome_types/model/ome.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/pixels.py` & `ome_types-0.3.4/src/ome_types/model/pixels.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/plane.py` & `ome_types-0.3.4/src/ome_types/model/plane.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/plate.py` & `ome_types-0.3.4/src/ome_types/model/plate.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/plate_acquisition.py` & `ome_types-0.3.4/src/ome_types/model/plate_acquisition.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/point.py` & `ome_types-0.3.4/src/ome_types/model/point.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/polygon.py` & `ome_types-0.3.4/src/ome_types/model/polygon.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/polyline.py` & `ome_types-0.3.4/src/ome_types/model/polyline.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/project.py` & `ome_types-0.3.4/src/ome_types/model/project.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/reagent.py` & `ome_types-0.3.4/src/ome_types/model/reagent.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/rectangle.py` & `ome_types-0.3.4/src/ome_types/model/rectangle.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/reference.py` & `ome_types-0.3.4/src/ome_types/model/reference.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/rights.py` & `ome_types-0.3.4/src/ome_types/model/rights.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/roi.py` & `ome_types-0.3.4/src/ome_types/model/roi.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/screen.py` & `ome_types-0.3.4/src/ome_types/model/screen.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/shape.py` & `ome_types-0.3.4/src/ome_types/model/shape.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/simple_types.py` & `ome_types-0.3.4/src/ome_types/model/simple_types.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/stage_label.py` & `ome_types-0.3.4/src/ome_types/model/stage_label.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/structured_annotations.py` & `ome_types-0.3.4/src/ome_types/model/structured_annotations.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/tag_annotation.py` & `ome_types-0.3.4/src/ome_types/model/tag_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/term_annotation.py` & `ome_types-0.3.4/src/ome_types/model/term_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/text_annotation.py` & `ome_types-0.3.4/src/ome_types/model/text_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/tiff_data.py` & `ome_types-0.3.4/src/ome_types/model/tiff_data.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/timestamp_annotation.py` & `ome_types-0.3.4/src/ome_types/model/timestamp_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/transmittance_range.py` & `ome_types-0.3.4/src/ome_types/model/transmittance_range.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/type_annotation.py` & `ome_types-0.3.4/src/ome_types/model/type_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/well.py` & `ome_types-0.3.4/src/ome_types/model/well.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/well_sample.py` & `ome_types-0.3.4/src/ome_types/model/well_sample.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/src/ome_types/model/xml_annotation.py` & `ome_types-0.3.4/src/ome_types/model/xml_annotation.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/test_autogen.py` & `ome_types-0.3.4/tests/test_autogen.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/test_model.py` & `ome_types-0.3.4/tests/test_model.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,22 +2,30 @@
 import re
 from pathlib import Path
 from unittest import mock
 from xml.dom import minidom
 from xml.etree import ElementTree
 
 import pytest
-from lxml.etree import XMLSchemaValidateError
 from pydantic import ValidationError
 from xmlschema.validators.exceptions import XMLSchemaValidationError
 
 import util
 from ome_types import from_tiff, from_xml, model, to_xml
 from ome_types._xmlschema import NS_OME, URI_OME, get_schema, to_xml_element
 
+ValidationErrors = [ValidationError, XMLSchemaValidationError]
+try:
+    from lxml.etree import XMLSchemaValidateError
+
+    ValidationErrors.append(XMLSchemaValidateError)
+except ImportError:
+    pass
+
+
 SHOULD_FAIL_READ = {
     # Some timestamps have negative years which datetime doesn't support.
     "timestampannotation",
 }
 SHOULD_FAIL_VALIDATION = {"invalid_xml_annotation"}
 SHOULD_RAISE_READ = {"bad"}
 SHOULD_FAIL_ROUNDTRIP = {
@@ -78,20 +86,17 @@
 parser = ["lxml", "xmlschema"]
 
 
 @pytest.mark.parametrize("xml", xml_read, ids=true_stem)
 @pytest.mark.parametrize("parser", parser)
 @pytest.mark.parametrize("validate", validate)
 def test_from_xml(xml, parser: str, validate: bool, benchmark):
-
     should_raise = SHOULD_RAISE_READ.union(SHOULD_FAIL_VALIDATION if validate else [])
     if true_stem(xml) in should_raise:
-        with pytest.raises(
-            (XMLSchemaValidateError, ValidationError, XMLSchemaValidationError)
-        ):
+        with pytest.raises(tuple(ValidationErrors)):
             assert benchmark(from_xml, xml, parser=parser, validate=validate)
     else:
         assert benchmark(from_xml, xml, parser=parser, validate=validate)
 
 
 @pytest.mark.parametrize("parser", parser)
 @pytest.mark.parametrize("validate", validate)
@@ -137,18 +142,18 @@
     original = canonicalize(xml, True)
     ome = from_xml(xml, parser=parser, validate=validate)
     rexml = benchmark(to_xml, ome)
 
     try:
         assert canonicalize(rexml, False) == original
     except AssertionError:
-        # Special xfail catch since two files fail only with lxml2dict
+        # Special xfail catch since two files fail only with xml2dict
         if true_stem(Path(xml)) in SHOULD_FAIL_ROUNDTRIP_LXML and parser == "lxml":
             pytest.xfail(
-                f"Expected failure on roundtrip using lxml2dict on file: {stem}"
+                f"Expected failure on roundtrip using xml2dict on file: {stem}"
             )
         else:
             raise
 
 
 @pytest.mark.parametrize("parser", parser)
 @pytest.mark.parametrize("validate", validate)
```

### Comparing `ome_types-0.3.3/tests/test_serialization.py` & `ome_types-0.3.4/tests/test_serialization.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/test_units.py` & `ome_types-0.3.4/tests/test_units.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/util.py` & `ome_types-0.3.4/tests/util.py`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/OverViewScan.ome.xml` & `ome_types-0.3.4/tests/data/OverViewScan.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/ROI.ome.xml` & `ome_types-0.3.4/tests/data/ROI.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/bad.ome.xml` & `ome_types-0.3.4/tests/data/bad.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/commentannotation.ome.xml` & `ome_types-0.3.4/tests/data/commentannotation.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/example.ome.xml` & `ome_types-0.3.4/tests/data/example.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/fake-plate-rows-2.ome.xml` & `ome_types-0.3.4/tests/data/fake-plate-rows-2.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/filter.ome.xml` & `ome_types-0.3.4/tests/data/filter.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/folders-larger-taxonomy.ome.xml` & `ome_types-0.3.4/tests/data/folders-larger-taxonomy.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/folders-simple-taxonomy.ome.xml` & `ome_types-0.3.4/tests/data/folders-simple-taxonomy.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/hcs.ome.xml` & `ome_types-0.3.4/tests/data/hcs.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/instrument-units-alternate.ome.xml` & `ome_types-0.3.4/tests/data/instrument-units-alternate.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/instrument-units-default.ome.xml` & `ome_types-0.3.4/tests/data/instrument-units-default.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/instrument.ome.xml` & `ome_types-0.3.4/tests/data/instrument.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/invalid_xml_annotation.ome.xml` & `ome_types-0.3.4/tests/data/invalid_xml_annotation.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/mapannotation.ome.xml` & `ome_types-0.3.4/tests/data/mapannotation.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/metadata-only.ome.xml` & `ome_types-0.3.4/tests/data/metadata-only.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/minimum-specification.ome.xml` & `ome_types-0.3.4/tests/data/minimum-specification.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/multi-channel-time-series.ome.xml` & `ome_types-0.3.4/tests/data/multi-channel-time-series.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/multi-channel-z-series-time-series.ome.xml` & `ome_types-0.3.4/tests/data/multi-channel-z-series-time-series.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/multi-channel-z-series.ome.xml` & `ome_types-0.3.4/tests/data/multi-channel-z-series.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/multi-channel.ome.xml` & `ome_types-0.3.4/tests/data/multi-channel.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/no-date.ome.xml` & `ome_types-0.3.4/tests/data/no-date.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/ome.tiff` & `ome_types-0.3.4/tests/data/ome.tiff`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/ome_ns.ome.xml` & `ome_types-0.3.4/tests/data/ome_ns.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/one-screen-one-plate-four-wells.ome.xml` & `ome_types-0.3.4/tests/data/one-screen-one-plate-four-wells.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/shape-union.ome.xml` & `ome_types-0.3.4/tests/data/shape-union.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/single-image.ome.xml` & `ome_types-0.3.4/tests/data/single-image.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/small.ome.xml` & `ome_types-0.3.4/tests/data/small.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/spim.ome.xml` & `ome_types-0.3.4/tests/data/spim.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/tagannotation.ome.xml` & `ome_types-0.3.4/tests/data/tagannotation.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/time-series.ome.xml` & `ome_types-0.3.4/tests/data/time-series.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/timestampannotation-posix-only.ome.xml` & `ome_types-0.3.4/tests/data/timestampannotation-posix-only.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/timestampannotation.ome.xml` & `ome_types-0.3.4/tests/data/timestampannotation.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/transformations-downgrade.ome.xml` & `ome_types-0.3.4/tests/data/transformations-downgrade.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/transformations-upgrade.ome.xml` & `ome_types-0.3.4/tests/data/transformations-upgrade.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/tubhiswt.ome.xml` & `ome_types-0.3.4/tests/data/tubhiswt.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/two-screens-two-plates-four-wells.ome.xml` & `ome_types-0.3.4/tests/data/two-screens-two-plates-four-wells.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/xmlannotation-body-space.ome.xml` & `ome_types-0.3.4/tests/data/xmlannotation-body-space.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/xmlannotation-multi-value.ome.xml` & `ome_types-0.3.4/tests/data/xmlannotation-multi-value.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/xmlannotation-svg.ome.xml` & `ome_types-0.3.4/tests/data/xmlannotation-svg.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/z-series-time-series.ome.xml` & `ome_types-0.3.4/tests/data/z-series-time-series.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/tests/data/z-series.ome.xml` & `ome_types-0.3.4/tests/data/z-series.ome.xml`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/.gitignore` & `ome_types-0.3.4/.gitignore`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/LICENSE` & `ome_types-0.3.4/LICENSE`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/README.md` & `ome_types-0.3.4/README.md`

 * *Files identical despite different names*

### Comparing `ome_types-0.3.3/pyproject.toml` & `ome_types-0.3.4/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -47,16 +47,16 @@
   "Programming Language :: Python :: 3.10",
   "Programming Language :: Python :: 3.11",
 ]
 dynamic = ["version"]
 dependencies = [
   "Pint >=0.15",
   "lxml >=4.8.0",
-  "pydantic[email] >=1.0",
-  "xmlschema >=1.4.1",
+  "pydantic[email] >=1.0, <2.0",
+  "xmlschema >=2.0.0",
 ]
 
 [project.urls]
 Source = "https://github.com/tlambert03/ome-types"
 Tracker = "https://github.com/tlambert03/ome-types/issues"
 Documentation = "https://ome-types.readthedocs.io/en/latest/"
```

### Comparing `ome_types-0.3.3/PKG-INFO` & `ome_types-0.3.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ome-types
-Version: 0.3.3
+Version: 0.3.4
 Summary: Python dataclasses for the OME data model
 Project-URL: Source, https://github.com/tlambert03/ome-types
 Project-URL: Tracker, https://github.com/tlambert03/ome-types/issues
 Project-URL: Documentation, https://ome-types.readthedocs.io/en/latest/
 Author-email: Talley Lambert <talley.lambert@gmail.com>
 License: MIT
 License-File: LICENSE
@@ -21,16 +21,16 @@
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Requires-Python: >=3.7
 Requires-Dist: lxml>=4.8.0
 Requires-Dist: pint>=0.15
-Requires-Dist: pydantic[email]>=1.0
-Requires-Dist: xmlschema>=1.4.1
+Requires-Dist: pydantic[email]<2.0,>=1.0
+Requires-Dist: xmlschema>=2.0.0
 Provides-Extra: autogen
 Requires-Dist: autoflake; extra == 'autogen'
 Requires-Dist: black; extra == 'autogen'
 Requires-Dist: isort>=5.0; extra == 'autogen'
 Requires-Dist: numpydoc; extra == 'autogen'
 Provides-Extra: docs
 Requires-Dist: autoflake; extra == 'docs'
```

