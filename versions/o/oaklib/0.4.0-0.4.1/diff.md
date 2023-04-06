# Comparing `tmp/oaklib-0.4.0.tar.gz` & `tmp/oaklib-0.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "oaklib-0.4.0.tar", max compression
+gzip compressed data, was "oaklib-0.4.1.tar", max compression
```

## Comparing `oaklib-0.4.0.tar` & `oaklib-0.4.1.tar`

### file list

```diff
@@ -1,246 +1,246 @@
--rw-r--r--   0        0        0    11357 2023-04-03 20:14:17.522743 oaklib-0.4.0/LICENSE
--rw-r--r--   0        0        0     7241 2023-04-03 20:14:17.522743 oaklib-0.4.0/README.md
--rw-r--r--   0        0        0     1726 2023-04-03 20:14:59.919744 oaklib-0.4.0/pyproject.toml
--rw-r--r--   0        0        0      271 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/__init__.py
--rw-r--r--   0        0        0   184103 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/cli.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/conf/__init__.py
--rw-r--r--   0        0        0     1903 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/conf/lexmatch-rules-oboinowl-default.yaml
--rw-r--r--   0        0        0     4537 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/conf/obograph-style.json
--rw-r--r--   0        0        0      256 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/conf/omo-to-skos.sssom.tsv
--rw-r--r--   0        0        0      131 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/conf/value-set-expander.conf.yaml
--rw-r--r--   0        0        0      128 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/constants.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/converters/__init__.py
--rw-r--r--   0        0        0     1456 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/converters/data_model_converter.py
--rw-r--r--   0        0        0     2561 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/converters/logical_definition_flattener.py
--rw-r--r--   0        0        0     2371 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/converters/obo_graph_to_cx_converter.py
--rw-r--r--   0        0        0    12121 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/converters/obo_graph_to_fhir_converter.py
--rw-r--r--   0        0        0     5713 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/converters/obo_graph_to_obo_format_converter.py
--rw-r--r--   0        0        0     5155 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/converters/obo_graph_to_rdf_owl_converter.py
--rw-r--r--   0        0        0       60 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/__init__.py
--rw-r--r--   0        0        0     4034 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/association.owl.ttl
--rw-r--r--   0        0        0    10999 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/association.py
--rw-r--r--   0        0        0     2738 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/association.yaml
--rw-r--r--   0        0        0     6165 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/class_enrichment.owl.ttl
--rw-r--r--   0        0        0    10853 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/class_enrichment.py
--rw-r--r--   0        0        0     2648 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/class_enrichment.yaml
--rw-r--r--   0        0        0    19083 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/cross_ontology_diff.owl.ttl
--rw-r--r--   0        0        0    24246 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/cross_ontology_diff.py
--rw-r--r--   0        0        0    10687 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/cross_ontology_diff.yaml
--rw-r--r--   0        0        0    15826 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/fhir.owl.ttl
--rw-r--r--   0        0        0    35704 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/fhir.py
--rw-r--r--   0        0        0     5044 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/fhir.yaml
--rw-r--r--   0        0        0     8984 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/lexical_index.owl.ttl
--rw-r--r--   0        0        0    17256 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/lexical_index.py
--rw-r--r--   0        0        0     6429 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/lexical_index.schema.json
--rw-r--r--   0        0        0     4016 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/lexical_index.yaml
--rw-r--r--   0        0        0    26434 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/mapping_cluster_datamodel.py
--rw-r--r--   0        0        0     7317 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/mapping_cluster_datamodel.yaml
--rw-r--r--   0        0        0    17785 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/mapping_rules_datamodel.owl.ttl
--rw-r--r--   0        0        0    29752 2023-04-03 20:14:17.642746 oaklib-0.4.0/src/oaklib/datamodels/mapping_rules_datamodel.py
--rw-r--r--   0        0        0    11456 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/mapping_rules_datamodel.schema.json
--rw-r--r--   0        0        0     3220 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/mapping_rules_datamodel.yaml
--rw-r--r--   0        0        0    25354 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/obograph.owl.ttl
--rw-r--r--   0        0        0    45533 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/obograph.py
--rw-r--r--   0        0        0    22375 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/obograph.schema.json
--rw-r--r--   0        0        0    17625 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/obograph.yaml
--rw-r--r--   0        0        0    59793 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/ontology_metadata.owl.ttl
--rw-r--r--   0        0        0   116551 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/ontology_metadata.py
--rw-r--r--   0        0        0    95288 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/ontology_metadata.schema.json
--rw-r--r--   0        0        0    30318 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/ontology_metadata.yaml
--rw-r--r--   0        0        0    14759 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/oxo.owl.ttl
--rw-r--r--   0        0        0    21914 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/oxo.py
--rw-r--r--   0        0        0     4392 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/oxo.yaml
--rw-r--r--   0        0        0     3232 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/search.py
--rw-r--r--   0        0        0    16948 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/search_datamodel.owl.ttl
--rw-r--r--   0        0        0    25145 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/search_datamodel.py
--rw-r--r--   0        0        0     6683 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/search_datamodel.yaml
--rw-r--r--   0        0        0    12767 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/similarity.owl.ttl
--rw-r--r--   0        0        0    22125 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/similarity.py
--rw-r--r--   0        0        0     5512 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/similarity.yaml
--rw-r--r--   0        0        0    31217 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/summary_statistics_datamodel.owl.ttl
--rw-r--r--   0        0        0    50746 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/summary_statistics_datamodel.py
--rw-r--r--   0        0        0    21176 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/summary_statistics_datamodel.schema.json
--rw-r--r--   0        0        0    16249 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/summary_statistics_datamodel.yaml
--rw-r--r--   0        0        0     9909 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/taxon_constraints.owl.ttl
--rw-r--r--   0        0        0    18433 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/taxon_constraints.py
--rw-r--r--   0        0        0     5882 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/taxon_constraints.yaml
--rw-r--r--   0        0        0    11599 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/text_annotator.owl.ttl
--rw-r--r--   0        0        0    20421 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/text_annotator.py
--rw-r--r--   0        0        0     2464 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/text_annotator.schema.json
--rw-r--r--   0        0        0     4222 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/text_annotator.yaml
--rw-r--r--   0        0        0    13670 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/validation_datamodel.owl.ttl
--rw-r--r--   0        0        0    25351 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/validation_datamodel.py
--rw-r--r--   0        0        0    10783 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/validation_datamodel.schema.json
--rw-r--r--   0        0        0     7510 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/validation_datamodel.yaml
--rw-r--r--   0        0        0     6640 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/value_set_configuration.owl.ttl
--rw-r--r--   0        0        0     8458 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/value_set_configuration.py
--rw-r--r--   0        0        0     2276 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/value_set_configuration.yaml
--rw-r--r--   0        0        0     5378 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/datamodels/vocabulary.py
--rw-r--r--   0        0        0     5079 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/implementations/__init__.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/implementations/aggregator/__init__.py
--rw-r--r--   0        0        0     5454 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/implementations/aggregator/aggregator_implementation.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/implementations/amigo/__init__.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/implementations/cx/__init__.py
--rw-r--r--   0        0        0     1985 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/implementations/cx/cx_implementation.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/implementations/fhir/__init__.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/implementations/funowl/__init__.py
--rw-r--r--   0        0        0     8331 2023-04-03 20:14:17.646746 oaklib-0.4.0/src/oaklib/implementations/funowl/funowl_implementation.py
--rw-r--r--   0        0        0     2313 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/gilda.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/kgx/__init__.py
--rw-r--r--   0        0        0    30623 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/kgx/kgx_implementation.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/neo4j/__init__.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/obograph/__init__.py
--rw-r--r--   0        0        0    15746 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/obograph/obograph_implementation.py
--rw-r--r--   0        0        0      267 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ols/__init__.py
--rw-r--r--   0        0        0      132 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ols/constants.py
--rw-r--r--   0        0        0     7942 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ols/ols_implementation.py
--rw-r--r--   0        0        0      686 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ols/oxo_utils.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ontobee/__init__.py
--rw-r--r--   0        0        0     1383 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ontobee/ontobee_implementation.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ontoportal/__init__.py
--rw-r--r--   0        0        0      382 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ontoportal/agroportal_implementation.py
--rw-r--r--   0        0        0      817 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ontoportal/bioportal_implementation.py
--rw-r--r--   0        0        0      378 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ontoportal/ecoportal_implementation.py
--rw-r--r--   0        0        0      378 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ontoportal/matportal_implementation.py
--rw-r--r--   0        0        0    12106 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ontoportal/ontoportal_implementation_base.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/owlery/__init__.py
--rw-r--r--   0        0        0      427 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/owlery/owlery_implementation.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/pronto/__init__.py
--rw-r--r--   0        0        0    34045 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/pronto/pronto_implementation.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/robot/__init__.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/scigraph/__init__.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/simpleobo/__init__.py
--rw-r--r--   0        0        0    33315 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/simpleobo/simple_obo_implementation.py
--rw-r--r--   0        0        0    19710 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/simpleobo/simple_obo_parser.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/skos/__init__.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/solor/__init__.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/solr/__init__.py
--rw-r--r--   0        0        0       96 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/sparql/__init__.py
--rw-r--r--   0        0        0    36179 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/sparql/abstract_sparql_implementation.py
--rw-r--r--   0        0        0      885 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/sparql/lov_implementation.py
--rw-r--r--   0        0        0     1721 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/sparql/oak_metamodel_implementation.py
--rw-r--r--   0        0        0     2525 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/sparql/sparql_implementation.py
--rw-r--r--   0        0        0     2326 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/sparql/sparql_query.py
--rw-r--r--   0        0        0       96 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/sqldb/__init__.py
--rw-r--r--   0        0        0    97839 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/sqldb/sql_implementation.py
--rw-r--r--   0        0        0     1903 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/sqldb/sqlite_utils.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/tccm/__init__.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/translator/__init__.py
--rw-r--r--   0        0        0     3111 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/translator/translator_implementation.py
--rw-r--r--   0        0        0      108 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ubergraph/__init__.py
--rw-r--r--   0        0        0    19389 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/ubergraph/ubergraph_implementation.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/umls/__init__.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/uniprot/__init__.py
--rw-r--r--   0        0        0     9599 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/uniprot/uniprot_implementation.py
--rw-r--r--   0        0        0       96 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/wikidata/__init__.py
--rw-r--r--   0        0        0    17117 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/implementations/wikidata/wikidata_implementation.py
--rw-r--r--   0        0        0      913 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/__init__.py
--rw-r--r--   0        0        0     7616 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/association_provider_interface.py
--rw-r--r--   0        0        0    38972 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/basic_ontology_interface.py
--rw-r--r--   0        0        0     5083 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/class_enrichment_calculation_interface.py
--rw-r--r--   0        0        0    10467 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/differ_interface.py
--rw-r--r--   0        0        0     2649 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/dumper_interface.py
--rw-r--r--   0        0        0     3361 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/mapping_provider_interface.py
--rw-r--r--   0        0        0     3262 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/merge_interface.py
--rw-r--r--   0        0        0     3103 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/metadata_interface.py
--rw-r--r--   0        0        0    17700 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/obograph_interface.py
--rw-r--r--   0        0        0      999 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/obolegacy_interface.py
--rw-r--r--   0        0        0      784 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/ontology_interface.py
--rw-r--r--   0        0        0    10988 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/owl_interface.py
--rw-r--r--   0        0        0     8236 2023-04-03 20:14:17.650746 oaklib-0.4.0/src/oaklib/interfaces/patcher_interface.py
--rw-r--r--   0        0        0     1955 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/interfaces/rdf_interface.py
--rw-r--r--   0        0        0     2459 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/interfaces/relation_graph_interface.py
--rw-r--r--   0        0        0     1386 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/interfaces/search_interface.py
--rw-r--r--   0        0        0    12778 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/interfaces/semsim_interface.py
--rw-r--r--   0        0        0     1063 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/interfaces/skos_interface.py
--rw-r--r--   0        0        0     2112 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/interfaces/subsetter_interface.py
--rw-r--r--   0        0        0    10140 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/interfaces/summary_statistics_interface.py
--rw-r--r--   0        0        0    18296 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/interfaces/taxon_constraint_interface.py
--rw-r--r--   0        0        0     7511 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/interfaces/text_annotator_interface.py
--rw-r--r--   0        0        0     3033 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/interfaces/validator_interface.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/__init__.py
--rw-r--r--   0        0        0     1539 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/heatmap_writer.py
--rw-r--r--   0        0        0     1698 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/html_writer.py
--rw-r--r--   0        0        0     1379 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/obograph_writer.py
--rw-r--r--   0        0        0     3444 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/rollup_report_writer.py
--rw-r--r--   0        0        0      739 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_axiom_writer.py
--rw-r--r--   0        0        0     6519 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_csv_writer.py
--rw-r--r--   0        0        0     1284 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_fhir_writer.py
--rw-r--r--   0        0        0     2353 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_info_writer.py
--rw-r--r--   0        0        0     1231 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_json_lines_writer.py
--rw-r--r--   0        0        0     1806 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_json_writer.py
--rw-r--r--   0        0        0      741 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_kgcl_writer.py
--rw-r--r--   0        0        0     2088 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_markdown_writer.py
--rw-r--r--   0        0        0     1152 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_nl_writer.py
--rw-r--r--   0        0        0     1117 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_obo_json_writer.py
--rw-r--r--   0        0        0     3496 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_obo_writer.py
--rw-r--r--   0        0        0     1270 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_owl_functional_writer.py
--rw-r--r--   0        0        0     2244 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_rdf_writer.py
--rw-r--r--   0        0        0     4438 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_writer.py
--rw-r--r--   0        0        0     1301 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/io/streaming_yaml_writer.py
--rw-r--r--   0        0        0      113 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/mappers/__init__.py
--rw-r--r--   0        0        0     3717 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/mappers/base_mapper.py
--rw-r--r--   0        0        0     1849 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/mappers/ontology_metadata_mapper.py
--rw-r--r--   0        0        0     1434 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/__init__.py
--rw-r--r--   0        0        0      650 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/association_parser.py
--rw-r--r--   0        0        0      312 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/association_parser_factory.py
--rw-r--r--   0        0        0     4731 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/boomer_parser.py
--rw-r--r--   0        0        0     1178 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/gaf_association_parser.py
--rw-r--r--   0        0        0      563 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/hpoa_association_parser.py
--rw-r--r--   0        0        0      602 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/hpoa_g2p_association_parser.py
--rw-r--r--   0        0        0      653 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/kgx_association_parser.py
--rw-r--r--   0        0        0      525 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/pairwise_association_parser.py
--rw-r--r--   0        0        0     1328 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/parser_base.py
--rw-r--r--   0        0        0      707 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/phaf_association_parser.py
--rw-r--r--   0        0        0     6128 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/parsers/xaf_association_parser.py
--rw-r--r--   0        0        0     2210 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/resource.py
--rw-r--r--   0        0        0     7859 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/selector.py
--rw-r--r--   0        0        0      177 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/types.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/__init__.py
--rw-r--r--   0        0        0     1613 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/apikey_manager.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/associations/__init__.py
--rw-r--r--   0        0        0     2810 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/associations/association_differ.py
--rw-r--r--   0        0        0     2865 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/associations/association_index.py
--rw-r--r--   0        0        0     1182 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/basic_utils.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/graph/__init__.py
--rw-r--r--   0        0        0     2490 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/graph/networkx_bridge.py
--rw-r--r--   0        0        0     2918 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/graph/relationship_walker.py
--rw-r--r--   0        0        0      981 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/identifier_utils.py
--rw-r--r--   0        0        0      999 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/iterator_utils.py
--rw-r--r--   0        0        0     3345 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/kgcl_utilities.py
--rw-r--r--   0        0        0      850 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/label_utilities.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/lexical/__init__.py
--rw-r--r--   0        0        0    19516 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/lexical/lexical_indexer.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/mapping/__init__.py
--rw-r--r--   0        0        0    14443 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/mapping/boomer_utils.py
--rw-r--r--   0        0        0    15328 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/mapping/cross_ontology_diffs.py
--rw-r--r--   0        0        0      751 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/mapping/mapping_propagator.py
--rw-r--r--   0        0        0     2270 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/mapping/mapping_validation.py
--rw-r--r--   0        0        0     2694 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/mapping/sssom_utils.py
--rw-r--r--   0        0        0      684 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/ner_utilities.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/nlp/__init__.py
--rw-r--r--   0        0        0     3358 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/nlp/natual_language_generation.py
--rw-r--r--   0        0        0      136 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/oboformat_utils.py
--rw-r--r--   0        0        0    22266 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/obograph_utils.py
--rw-r--r--   0        0        0     2275 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/ontology_builder.py
--rw-r--r--   0        0        0      379 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/rate_limiter.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/reasoning/__init__.py
--rw-r--r--   0        0        0      569 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/reasoning/relation_graph.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/semsim/__init__.py
--rw-r--r--   0        0        0     1739 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/semsim/similarity_utils.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/stats/__init__.py
--rw-r--r--   0        0        0     1511 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/stats/hypergeometric.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/subsets/__init__.py
--rw-r--r--   0        0        0     2676 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/subsets/slimmer_utils.py
--rw-r--r--   0        0        0     4701 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/subsets/subset_analysis.py
--rw-r--r--   0        0        0    11592 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/subsets/value_set_expander.py
--rw-r--r--   0        0        0    13200 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/table_filler.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/taxon/__init__.py
--rw-r--r--   0        0        0     1743 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/taxon/taxon_constraint_utils.py
--rw-r--r--   0        0        0        0 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/validation/__init__.py
--rw-r--r--   0        0        0    10097 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/validation/definition_ontology_rule.py
--rw-r--r--   0        0        0     7492 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/validation/disjointness_rule.py
--rw-r--r--   0        0        0     1729 2023-04-03 20:14:17.654747 oaklib-0.4.0/src/oaklib/utilities/validation/lint_utils.py
--rw-r--r--   0        0        0     1402 2023-04-03 20:14:17.658747 oaklib-0.4.0/src/oaklib/utilities/validation/ontology_rule.py
--rw-r--r--   0        0        0     1313 2023-04-03 20:14:17.658747 oaklib-0.4.0/src/oaklib/utilities/validation/rule_runner.py
--rw-r--r--   0        0        0     8922 1970-01-01 00:00:00.000000 oaklib-0.4.0/PKG-INFO
+-rw-r--r--   0        0        0    11357 2023-04-06 15:15:58.436868 oaklib-0.4.1/LICENSE
+-rw-r--r--   0        0        0     7241 2023-04-06 15:15:58.436868 oaklib-0.4.1/README.md
+-rw-r--r--   0        0        0     1728 2023-04-06 15:16:44.705722 oaklib-0.4.1/pyproject.toml
+-rw-r--r--   0        0        0      271 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/__init__.py
+-rw-r--r--   0        0        0   185955 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/cli.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/conf/__init__.py
+-rw-r--r--   0        0        0     1903 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/conf/lexmatch-rules-oboinowl-default.yaml
+-rw-r--r--   0        0        0     4537 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/conf/obograph-style.json
+-rw-r--r--   0        0        0      256 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/conf/omo-to-skos.sssom.tsv
+-rw-r--r--   0        0        0      131 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/conf/value-set-expander.conf.yaml
+-rw-r--r--   0        0        0      128 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/constants.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/converters/__init__.py
+-rw-r--r--   0        0        0     1456 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/converters/data_model_converter.py
+-rw-r--r--   0        0        0     2561 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/converters/logical_definition_flattener.py
+-rw-r--r--   0        0        0     2371 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/converters/obo_graph_to_cx_converter.py
+-rw-r--r--   0        0        0    12163 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/converters/obo_graph_to_fhir_converter.py
+-rw-r--r--   0        0        0     5713 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/converters/obo_graph_to_obo_format_converter.py
+-rw-r--r--   0        0        0     5155 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/converters/obo_graph_to_rdf_owl_converter.py
+-rw-r--r--   0        0        0       60 2023-04-06 15:15:58.552870 oaklib-0.4.1/src/oaklib/datamodels/__init__.py
+-rw-r--r--   0        0        0     4034 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/association.owl.ttl
+-rw-r--r--   0        0        0    10999 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/association.py
+-rw-r--r--   0        0        0     2738 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/association.yaml
+-rw-r--r--   0        0        0     6165 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/class_enrichment.owl.ttl
+-rw-r--r--   0        0        0    10853 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/class_enrichment.py
+-rw-r--r--   0        0        0     2648 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/class_enrichment.yaml
+-rw-r--r--   0        0        0    19083 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/cross_ontology_diff.owl.ttl
+-rw-r--r--   0        0        0    24246 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/cross_ontology_diff.py
+-rw-r--r--   0        0        0    10687 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/cross_ontology_diff.yaml
+-rw-r--r--   0        0        0    15826 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/fhir.owl.ttl
+-rw-r--r--   0        0        0    35744 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/fhir.py
+-rw-r--r--   0        0        0     5064 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/fhir.yaml
+-rw-r--r--   0        0        0     8984 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/lexical_index.owl.ttl
+-rw-r--r--   0        0        0    17256 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/lexical_index.py
+-rw-r--r--   0        0        0     6429 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/lexical_index.schema.json
+-rw-r--r--   0        0        0     4016 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/lexical_index.yaml
+-rw-r--r--   0        0        0    26434 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/mapping_cluster_datamodel.py
+-rw-r--r--   0        0        0     7317 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/mapping_cluster_datamodel.yaml
+-rw-r--r--   0        0        0    17785 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/mapping_rules_datamodel.owl.ttl
+-rw-r--r--   0        0        0    29752 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/mapping_rules_datamodel.py
+-rw-r--r--   0        0        0    11456 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/mapping_rules_datamodel.schema.json
+-rw-r--r--   0        0        0     3220 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/mapping_rules_datamodel.yaml
+-rw-r--r--   0        0        0    25354 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/obograph.owl.ttl
+-rw-r--r--   0        0        0    45533 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/obograph.py
+-rw-r--r--   0        0        0    22375 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/obograph.schema.json
+-rw-r--r--   0        0        0    17625 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/obograph.yaml
+-rw-r--r--   0        0        0    59793 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/ontology_metadata.owl.ttl
+-rw-r--r--   0        0        0   116551 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/ontology_metadata.py
+-rw-r--r--   0        0        0    95288 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/ontology_metadata.schema.json
+-rw-r--r--   0        0        0    30318 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/ontology_metadata.yaml
+-rw-r--r--   0        0        0    14759 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/oxo.owl.ttl
+-rw-r--r--   0        0        0    21914 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/oxo.py
+-rw-r--r--   0        0        0     4392 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/oxo.yaml
+-rw-r--r--   0        0        0     3240 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/search.py
+-rw-r--r--   0        0        0    16948 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/search_datamodel.owl.ttl
+-rw-r--r--   0        0        0    25145 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/search_datamodel.py
+-rw-r--r--   0        0        0     6683 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/search_datamodel.yaml
+-rw-r--r--   0        0        0    12767 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/similarity.owl.ttl
+-rw-r--r--   0        0        0    22125 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/similarity.py
+-rw-r--r--   0        0        0     5512 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/similarity.yaml
+-rw-r--r--   0        0        0    31217 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/summary_statistics_datamodel.owl.ttl
+-rw-r--r--   0        0        0    50746 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/summary_statistics_datamodel.py
+-rw-r--r--   0        0        0    21176 2023-04-06 15:15:58.556870 oaklib-0.4.1/src/oaklib/datamodels/summary_statistics_datamodel.schema.json
+-rw-r--r--   0        0        0    16249 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/summary_statistics_datamodel.yaml
+-rw-r--r--   0        0        0     9909 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/taxon_constraints.owl.ttl
+-rw-r--r--   0        0        0    18433 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/taxon_constraints.py
+-rw-r--r--   0        0        0     5882 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/taxon_constraints.yaml
+-rw-r--r--   0        0        0    11599 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/text_annotator.owl.ttl
+-rw-r--r--   0        0        0    20421 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/text_annotator.py
+-rw-r--r--   0        0        0     2464 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/text_annotator.schema.json
+-rw-r--r--   0        0        0     4222 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/text_annotator.yaml
+-rw-r--r--   0        0        0    13670 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/validation_datamodel.owl.ttl
+-rw-r--r--   0        0        0    25351 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/validation_datamodel.py
+-rw-r--r--   0        0        0    10783 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/validation_datamodel.schema.json
+-rw-r--r--   0        0        0     7510 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/validation_datamodel.yaml
+-rw-r--r--   0        0        0     6640 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/value_set_configuration.owl.ttl
+-rw-r--r--   0        0        0     8458 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/value_set_configuration.py
+-rw-r--r--   0        0        0     2276 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/value_set_configuration.yaml
+-rw-r--r--   0        0        0     5378 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/datamodels/vocabulary.py
+-rw-r--r--   0        0        0     5079 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/aggregator/__init__.py
+-rw-r--r--   0        0        0     5454 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/aggregator/aggregator_implementation.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/amigo/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/cx/__init__.py
+-rw-r--r--   0        0        0     1985 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/cx/cx_implementation.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/fhir/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/funowl/__init__.py
+-rw-r--r--   0        0        0     8331 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/funowl/funowl_implementation.py
+-rw-r--r--   0        0        0     2313 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/gilda.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/kgx/__init__.py
+-rw-r--r--   0        0        0    30631 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/kgx/kgx_implementation.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/neo4j/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/obograph/__init__.py
+-rw-r--r--   0        0        0    15754 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/obograph/obograph_implementation.py
+-rw-r--r--   0        0        0      267 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ols/__init__.py
+-rw-r--r--   0        0        0      132 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ols/constants.py
+-rw-r--r--   0        0        0     7942 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ols/ols_implementation.py
+-rw-r--r--   0        0        0      686 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ols/oxo_utils.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ontobee/__init__.py
+-rw-r--r--   0        0        0     1391 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ontobee/ontobee_implementation.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ontoportal/__init__.py
+-rw-r--r--   0        0        0      382 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ontoportal/agroportal_implementation.py
+-rw-r--r--   0        0        0      821 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ontoportal/bioportal_implementation.py
+-rw-r--r--   0        0        0      378 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ontoportal/ecoportal_implementation.py
+-rw-r--r--   0        0        0      378 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ontoportal/matportal_implementation.py
+-rw-r--r--   0        0        0    12106 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ontoportal/ontoportal_implementation_base.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/owlery/__init__.py
+-rw-r--r--   0        0        0      427 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/owlery/owlery_implementation.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/pronto/__init__.py
+-rw-r--r--   0        0        0    34424 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/pronto/pronto_implementation.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/robot/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/scigraph/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/simpleobo/__init__.py
+-rw-r--r--   0        0        0    33470 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/simpleobo/simple_obo_implementation.py
+-rw-r--r--   0        0        0    20498 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/simpleobo/simple_obo_parser.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/skos/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/solor/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/solr/__init__.py
+-rw-r--r--   0        0        0       96 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/sparql/__init__.py
+-rw-r--r--   0        0        0    36179 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/sparql/abstract_sparql_implementation.py
+-rw-r--r--   0        0        0      885 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/sparql/lov_implementation.py
+-rw-r--r--   0        0        0     1721 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/sparql/oak_metamodel_implementation.py
+-rw-r--r--   0        0        0     2525 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/sparql/sparql_implementation.py
+-rw-r--r--   0        0        0     2326 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/sparql/sparql_query.py
+-rw-r--r--   0        0        0       96 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/sqldb/__init__.py
+-rw-r--r--   0        0        0    99520 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/sqldb/sql_implementation.py
+-rw-r--r--   0        0        0     1903 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/sqldb/sqlite_utils.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/tccm/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/translator/__init__.py
+-rw-r--r--   0        0        0     3111 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/translator/translator_implementation.py
+-rw-r--r--   0        0        0      108 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ubergraph/__init__.py
+-rw-r--r--   0        0        0    19393 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/ubergraph/ubergraph_implementation.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.560870 oaklib-0.4.1/src/oaklib/implementations/umls/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/implementations/uniprot/__init__.py
+-rw-r--r--   0        0        0     9603 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/implementations/uniprot/uniprot_implementation.py
+-rw-r--r--   0        0        0       96 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/implementations/wikidata/__init__.py
+-rw-r--r--   0        0        0    17121 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/implementations/wikidata/wikidata_implementation.py
+-rw-r--r--   0        0        0      913 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/__init__.py
+-rw-r--r--   0        0        0     7725 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/association_provider_interface.py
+-rw-r--r--   0        0        0    38972 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/basic_ontology_interface.py
+-rw-r--r--   0        0        0     6960 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/class_enrichment_calculation_interface.py
+-rw-r--r--   0        0        0    11720 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/differ_interface.py
+-rw-r--r--   0        0        0     2649 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/dumper_interface.py
+-rw-r--r--   0        0        0     3365 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/mapping_provider_interface.py
+-rw-r--r--   0        0        0     3262 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/merge_interface.py
+-rw-r--r--   0        0        0     3103 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/metadata_interface.py
+-rw-r--r--   0        0        0    17700 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/obograph_interface.py
+-rw-r--r--   0        0        0     1003 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/obolegacy_interface.py
+-rw-r--r--   0        0        0      784 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/ontology_interface.py
+-rw-r--r--   0        0        0    10988 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/owl_interface.py
+-rw-r--r--   0        0        0     8236 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/patcher_interface.py
+-rw-r--r--   0        0        0     1955 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/rdf_interface.py
+-rw-r--r--   0        0        0     2459 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/relation_graph_interface.py
+-rw-r--r--   0        0        0     1386 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/search_interface.py
+-rw-r--r--   0        0        0    12778 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/semsim_interface.py
+-rw-r--r--   0        0        0     1063 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/skos_interface.py
+-rw-r--r--   0        0        0     2112 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/subsetter_interface.py
+-rw-r--r--   0        0        0    10140 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/summary_statistics_interface.py
+-rw-r--r--   0        0        0    18296 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/taxon_constraint_interface.py
+-rw-r--r--   0        0        0     7511 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/text_annotator_interface.py
+-rw-r--r--   0        0        0     3033 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/interfaces/validator_interface.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/__init__.py
+-rw-r--r--   0        0        0     1539 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/heatmap_writer.py
+-rw-r--r--   0        0        0     1698 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/html_writer.py
+-rw-r--r--   0        0        0     1379 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/obograph_writer.py
+-rw-r--r--   0        0        0     3444 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/rollup_report_writer.py
+-rw-r--r--   0        0        0      739 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_axiom_writer.py
+-rw-r--r--   0        0        0     6519 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_csv_writer.py
+-rw-r--r--   0        0        0     1284 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_fhir_writer.py
+-rw-r--r--   0        0        0     2353 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_info_writer.py
+-rw-r--r--   0        0        0     1231 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_json_lines_writer.py
+-rw-r--r--   0        0        0     1806 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_json_writer.py
+-rw-r--r--   0        0        0      741 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_kgcl_writer.py
+-rw-r--r--   0        0        0     2088 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_markdown_writer.py
+-rw-r--r--   0        0        0     1152 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_nl_writer.py
+-rw-r--r--   0        0        0     1117 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_obo_json_writer.py
+-rw-r--r--   0        0        0     3496 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_obo_writer.py
+-rw-r--r--   0        0        0     1270 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_owl_functional_writer.py
+-rw-r--r--   0        0        0     2244 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_rdf_writer.py
+-rw-r--r--   0        0        0     4438 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_writer.py
+-rw-r--r--   0        0        0     1301 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/io/streaming_yaml_writer.py
+-rw-r--r--   0        0        0      113 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/mappers/__init__.py
+-rw-r--r--   0        0        0     3717 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/mappers/base_mapper.py
+-rw-r--r--   0        0        0     1849 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/mappers/ontology_metadata_mapper.py
+-rw-r--r--   0        0        0     1742 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/__init__.py
+-rw-r--r--   0        0        0      650 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/association_parser.py
+-rw-r--r--   0        0        0      446 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/association_parser_factory.py
+-rw-r--r--   0        0        0     4731 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/boomer_parser.py
+-rw-r--r--   0        0        0     1178 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/gaf_association_parser.py
+-rw-r--r--   0        0        0      563 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/hpoa_association_parser.py
+-rw-r--r--   0        0        0      602 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/hpoa_g2p_association_parser.py
+-rw-r--r--   0        0        0      653 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/kgx_association_parser.py
+-rw-r--r--   0        0        0      525 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/pairwise_association_parser.py
+-rw-r--r--   0        0        0     1328 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/parser_base.py
+-rw-r--r--   0        0        0      707 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/phaf_association_parser.py
+-rw-r--r--   0        0        0     6128 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/parsers/xaf_association_parser.py
+-rw-r--r--   0        0        0     2210 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/resource.py
+-rw-r--r--   0        0        0     7867 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/selector.py
+-rw-r--r--   0        0        0      177 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/types.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/__init__.py
+-rw-r--r--   0        0        0     1613 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/apikey_manager.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/associations/__init__.py
+-rw-r--r--   0        0        0     2810 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/associations/association_differ.py
+-rw-r--r--   0        0        0     2865 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/associations/association_index.py
+-rw-r--r--   0        0        0     1182 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/basic_utils.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/graph/__init__.py
+-rw-r--r--   0        0        0     2490 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/graph/networkx_bridge.py
+-rw-r--r--   0        0        0     2918 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/graph/relationship_walker.py
+-rw-r--r--   0        0        0      993 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/identifier_utils.py
+-rw-r--r--   0        0        0      999 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/iterator_utils.py
+-rw-r--r--   0        0        0     3345 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/kgcl_utilities.py
+-rw-r--r--   0        0        0      850 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/label_utilities.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/lexical/__init__.py
+-rw-r--r--   0        0        0    19516 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/lexical/lexical_indexer.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/mapping/__init__.py
+-rw-r--r--   0        0        0    14443 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/mapping/boomer_utils.py
+-rw-r--r--   0        0        0    15328 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/mapping/cross_ontology_diffs.py
+-rw-r--r--   0        0        0      751 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/mapping/mapping_propagator.py
+-rw-r--r--   0        0        0     2270 2023-04-06 15:15:58.564870 oaklib-0.4.1/src/oaklib/utilities/mapping/mapping_validation.py
+-rw-r--r--   0        0        0     2694 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/mapping/sssom_utils.py
+-rw-r--r--   0        0        0      684 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/ner_utilities.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/nlp/__init__.py
+-rw-r--r--   0        0        0     3358 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/nlp/natual_language_generation.py
+-rw-r--r--   0        0        0      136 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/oboformat_utils.py
+-rw-r--r--   0        0        0    22266 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/obograph_utils.py
+-rw-r--r--   0        0        0     2275 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/ontology_builder.py
+-rw-r--r--   0        0        0      379 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/rate_limiter.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/reasoning/__init__.py
+-rw-r--r--   0        0        0      569 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/reasoning/relation_graph.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/semsim/__init__.py
+-rw-r--r--   0        0        0     1739 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/semsim/similarity_utils.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/stats/__init__.py
+-rw-r--r--   0        0        0     1511 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/stats/hypergeometric.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/subsets/__init__.py
+-rw-r--r--   0        0        0     2676 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/subsets/slimmer_utils.py
+-rw-r--r--   0        0        0     4701 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/subsets/subset_analysis.py
+-rw-r--r--   0        0        0    11592 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/subsets/value_set_expander.py
+-rw-r--r--   0        0        0    13212 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/table_filler.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/taxon/__init__.py
+-rw-r--r--   0        0        0     1743 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/taxon/taxon_constraint_utils.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/validation/__init__.py
+-rw-r--r--   0        0        0    10097 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/validation/definition_ontology_rule.py
+-rw-r--r--   0        0        0     7492 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/validation/disjointness_rule.py
+-rw-r--r--   0        0        0     1729 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/validation/lint_utils.py
+-rw-r--r--   0        0        0     1402 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/validation/ontology_rule.py
+-rw-r--r--   0        0        0     1313 2023-04-06 15:15:58.568870 oaklib-0.4.1/src/oaklib/utilities/validation/rule_runner.py
+-rw-r--r--   0        0        0     8923 1970-01-01 00:00:00.000000 oaklib-0.4.1/PKG-INFO
```

### Comparing `oaklib-0.4.0/LICENSE` & `oaklib-0.4.1/LICENSE`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/README.md` & `oaklib-0.4.1/README.md`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/pyproject.toml` & `oaklib-0.4.1/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,31 +1,31 @@
 [tool.poetry]
 name = "oaklib"
-version = "v0.4.0"
+version = "v0.4.1"
 description = "Ontology Access Kit: Python library for common ontology operations over a variety of backends"
 authors = ["cmungall <cjm@berkeleybop.org>"]
 
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = ">=3.9,<4.0.0"
 curies = "^0.4.0"
 nxontology = "^0.4.0"
 pronto = "^2.5.0"
 SPARQLWrapper = "*"
 SQLAlchemy = "^1.4.32"
 linkml-runtime = "^1.2.15"
 networkx = "^2.7.1"
-sssom-schema = "^0.9.3"
-sssom = "^0.3.25"
+sssom-schema = "^0.11.0"
+sssom = "^0.3.26"
 ratelimit = "^2.2.1"
 appdirs = "^1.4.4"
 semsql = "^0.3.1"
 lark = "^1.1.2"
-kgcl-schema = "^0.3.1"
+kgcl-schema = "^0.3.5"
 funowl = "^0.1.12"
 gilda = {version = "^0.10.1", optional = true}
 kgcl-rdflib = "^0.3.0"
 pystow = "^0.5.0"
 class-resolver = "^0.3.10"
 ontoportal-client = "0.0.3"
 bioregistry = "^0.6.35"
@@ -34,21 +34,21 @@
 pandas = "^1.5.1"
 linkml-renderer = "^0.1.2"
 airium = "^0.2.5"
 ndex2 = "^3.5.0"
 
 [tool.poetry.dev-dependencies]
 pytest = "^7.1.3"
-Sphinx = "^4.4.0"
+Sphinx = ">=6.1.3"
 jupyter = "^1.0.0"
 sphinx-rtd-theme = "^1.0.0"
 sphinx-click = "^3.1.0"
-myst-parser = "^0.17.0"
+myst-parser = ">=1.0.0"
 linkml = "^1.2.14"
-sphinxcontrib-mermaid = "^0.7.1"
+sphinxcontrib-mermaid = "^0.8.1"
 sphinx-copybutton = "0.5.1"
 coverage = "^6.3.2"
 
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
```

### Comparing `oaklib-0.4.0/src/oaklib/cli.py` & `oaklib-0.4.1/src/oaklib/cli.py`

 * *Files 1% similar despite different names*

```diff
@@ -642,15 +642,15 @@
                     yield x
                 else:
                     remaining.append(x)
             for x in rest:
                 if x not in remaining:
                     yield x
             query_terms = []
-        elif term == ".not" or terms == ".minus":
+        elif term == ".not" or term == ".minus":
             # boolean term: consume the result of the query and subtract
             rest = list(query_terms_iterator(query_terms, impl))
             for x in results:
                 if x not in rest:
                     yield x
             query_terms = []
         elif term == ".or":
@@ -1783,15 +1783,15 @@
 
     Example:
 
         runoak -i envo.db tree ENVO:00000372 -p i,p
 
     This produces output like:
 
-    .code::
+    .packages::
 
                         * [i] ENVO:00000094 ! volcanic feature
                             * [i] ENVO:00000247 ! volcano
                                 * [i] ENVO:00000403 ! shield volcano
                                     * [i] **ENVO:00000372 ! pyroclastic shield volcano**
 
 
@@ -4122,76 +4122,120 @@
 
 @main.command()
 @output_option
 @predicates_option
 @autolabel_option
 @output_type_option
 @output_option
-@if_absent_option
-@set_value_option
 @click.option(
-    "--cutoff", type=click.FLOAT, default=0.05, show_default=True, help="The cutoff for the p-value"
+    "--ontology-only/--no-ontology-only",
+    default=False,
+    show_default=True,
+    help="If true, perform a pseudo-enrichment analysis treating each term as an association to itself.",
+)
+@click.option(
+    "--cutoff",
+    type=click.FLOAT,
+    default=0.05,
+    show_default=True,
+    help="The cutoff for the p-value; any p-values greater than this are not reported.",
 )
 @click.option(
     "--sample-file",
     "-U",
+    required=True,
     type=click.File(mode="r"),
     help="file containing input list of entity IDs (e.g. gene IDs)",
 )
 @click.option(
     "--background-file",
     "-B",
     type=click.File(mode="r"),
     help="file containing background list of entity IDs (e.g. gene IDs)",
 )
 @click.option(
     "--association-predicates",
     help="A comma-separated list of predicates for the association relation",
 )
+@click.option(
+    "--filter-redundant/--no-filter-redundant",
+    default=False,
+    help="If true, filter out redundant terms",
+)
 @click.argument("terms", nargs=-1)
 def enrichment(
     terms,
     predicates: str,
     association_predicates: str,
     cutoff: float,
     autolabel: bool,
     output_type: str,
     output: str,
     sample_file: TextIO,
     background_file: TextIO,
-    if_absent: bool,
-    set_value: str,
+    ontology_only: bool,
+    **kwargs,
 ):
     """
     Run class enrichment analysis.
+
+    Given a sample file of identifiers (e.g. gene IDs), plus a set of associations (e.g. gene to term
+    associations, return the terms that are over-represented in the sample set.
+
+    Example:
+
+        runoak -i sqlite:obo:uberon -g gene2anat.txt -G g2t enrichment -U my-genes.txt -O csv
+
+    This runs an enrichment using Uberon on my-genes.txt, using the gene2anat.txt file as the
+    association file (assuming simple gene-to-term format). The output is in CSV format.
+
+    It is recommended you always provide a background set, including all the entity identifiers
+    considered in the experiment.
+
+    You can specify --filter-redundant to filter out redundant terms. This will block reporting
+    of any terms that are either subsumed by or subsume a lower p-value term that is already
+    reported.
+
+    For a full example, see:
+
+       https://github.com/INCATools/ontology-access-kit/blob/main/notebooks/Commands/Enrichment.ipynb
+
+    Note that it is possible to run "pseudo-enrichments" on term lists only by passing
+    no associations and using --ontology-only. This creates a fake association set that is simply
+    reflexive relations between each term and itself. This can be useful for summarizing term lists,
+    but note that P-values may not be meaningful.
     """
     impl = settings.impl
     actual_predicates = _process_predicates_arg(predicates)
     actual_association_predicates = _process_predicates_arg(association_predicates)
     subjects = list(curies_from_file(sample_file))
     background = list(curies_from_file(background_file)) if background_file else None
-    if isinstance(impl, ClassEnrichmentCalculationInterface):
-        writer = _get_writer(output_type, impl, StreamingYamlWriter)
-        writer.autolabel = autolabel
-        writer.output = output
-        curies = list(query_terms_iterator(terms, impl))
-        results = impl.enriched_classes(
-            subjects,
-            predicates=actual_association_predicates,
-            object_closure_predicates=actual_predicates,
-            hypotheses=curies if curies else None,
-            background=background,
-            cutoff=cutoff,
-            autolabel=autolabel,
-        )
-        for result in results:
-            writer.emit(result)
-        writer.finish()
-    else:
+    if not isinstance(impl, ClassEnrichmentCalculationInterface):
         raise NotImplementedError(f"Cannot execute this using {impl} of type {type(impl)}")
+    if not ontology_only and not any(True for _ in impl.associations()):
+        raise click.UsageError("no associations -- specify --ontology-only or load associations")
+    if ontology_only:
+        impl.create_self_associations()
+    writer = _get_writer(output_type, impl, StreamingYamlWriter)
+    writer.autolabel = autolabel
+    writer.output = output
+    curies = list(query_terms_iterator(terms, impl))
+    results = impl.enriched_classes(
+        subjects,
+        predicates=actual_association_predicates,
+        object_closure_predicates=actual_predicates,
+        hypotheses=curies if curies else None,
+        background=background,
+        cutoff=cutoff,
+        autolabel=autolabel,
+        **kwargs,
+    )
+    for result in results:
+        writer.emit(result)
+    writer.finish()
 
 
 @main.command()
 @output_option
 @predicates_option
 @autolabel_option
 @output_type_option
```

### Comparing `oaklib-0.4.0/src/oaklib/conf/lexmatch-rules-oboinowl-default.yaml` & `oaklib-0.4.1/src/oaklib/conf/lexmatch-rules-oboinowl-default.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/conf/obograph-style.json` & `oaklib-0.4.1/src/oaklib/conf/obograph-style.json`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/converters/data_model_converter.py` & `oaklib-0.4.1/src/oaklib/converters/data_model_converter.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/converters/logical_definition_flattener.py` & `oaklib-0.4.1/src/oaklib/converters/logical_definition_flattener.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/converters/obo_graph_to_cx_converter.py` & `oaklib-0.4.1/src/oaklib/converters/obo_graph_to_cx_converter.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/converters/obo_graph_to_fhir_converter.py` & `oaklib-0.4.1/src/oaklib/converters/obo_graph_to_fhir_converter.py`

 * *Files 5% similar despite different names*

```diff
@@ -53,15 +53,15 @@
 
 @dataclass
 class OboGraphToFHIRConverter(DataModelConverter):
     """Converts from OboGraph to FHIR.
 
     - An ontology is mapped to a FHIR `CodeSystem <https://build.fhir.org/codesystem.html>`_.
     - Each node in the OboGraph is converted to a _FHIR Concept_.
-    - Each CURIE/URI in the OboGraph is treated as a CURIE when it becomes a code (e.g. "HP:0000001")
+    - Each CURIE/URI in the OboGraph is treated as a CURIE when it becomes a packages (e.g. "HP:0000001")
 
     - Each edge in the OboGraph is converted to a _FHIR ConceptProperty_ if the `include_all_predicates` param is
       True. Otherwise, will only convert edges if the predicate is in the `DIRECT_PREDICATE_MAP`.
     - Each synonym in the OboGraph is converted to a _FHIR ConceptDesignation_.
 
         - The synonym predicate is mapped to a _FHIR Coding_, using the `SCOPE_MAP`.
 
@@ -127,23 +127,23 @@
         >>> graph = json_loader.load("tests/input/hp_test.json", target_class=GraphDocument)
         >>> code_system = converter.convert(graph)
         >>> print(json_dumper.dumps(code_system))
         <BLANKLINE>
         ...
          "concept": [
             {
-            "code": "HP:0012639",
+            "packages": "HP:0012639",
             "display": "Abnormal nervous system morphology",
             "definition": "A structural anomaly of the nervous system.",
             "designation": [
          ...
 
-        :param code_system_id: The code system ID to use for identification on the server uploaded to.
+        :param code_system_id: The packages system ID to use for identification on the server uploaded to.
                                See: https://hl7.org/fhir/resource-definitions.html#Resource.id
-        :param code_system_url: Canonical URL for the code system.
+        :param code_system_url: Canonical URL for the packages system.
                                 See: https://hl7.org/fhir/codesystem-definitions.html#CodeSystem.url
         :param native_uri_stems: A list of URI stems that will be used to determine whether a
                                  concept is native to the CodeSystem. (not implemented)
                                  For example, for OMIM, the following URI stems are native:
                                  https://omim.org/entry/, https://omim.org/phenotypicSeries/PS
         :param include_all_predicates: Include the maximal amount of predicates.
                                        Changes the default behavior from only
@@ -152,16 +152,16 @@
                                            concepts that are native to a given CodeSystem. With this option,
                                            references will be CURIEs instead. (not implemented)
         :param use_curies_foreign_concepts: Typical FHIR CodeSystems do not contain any
                                             concepts that are not native to that CodeSystem. In cases where they
                                             do appear, this converter defaults to URIs
                                             for references, unless this flag is present, in which case the converter
                                             will attempt to construct CURIEs. (not implemented)
-        :param predicate_period_replacement: Predicates URIs populated into `CodeSystem.concept.property.code`
-                                             and `CodeSystem.concept.property.code`, but the popular FHIR server "HAPI"
+        :param predicate_period_replacement: Predicates URIs populated into `CodeSystem.concept.property.packages`
+                                             and `CodeSystem.concept.property.packages`, but the HAPI FHIR server
                                              has a bug in whih periods '.' cause errors. If this flag is present,
                                              periods will be replaced with underscores '_'.
         :return: FHIR CodeSystem object
         """
         if target is None:
             target = CodeSystem()
         target.resourceType = CodeSystem.__name__
@@ -179,15 +179,15 @@
         if not code_system_id:
             del target.id
         if code_system_id:
             target.url = code_system_url
         return target
 
     def code(self, uri: CURIE) -> str:
-        """Convert a code.
+        """Convert a packages.
 
         This is a wrapper onto curie_converter.compress
 
         :param uri: URI or CURIE to convert
         :return: CURIE
         """
         if not self.curie_converter:
@@ -223,21 +223,21 @@
                 native_uri_stems=native_uri_stems,
                 use_curies_native_concepts=use_curies_native_concepts,
                 use_curies_foreign_concepts=use_curies_foreign_concepts,
                 predicate_period_replacement=predicate_period_replacement,
             )
         # CodeSystem.property
         # todo's
-        #  i. code: mostly URIs, which don't conform to [^\s]+(\s[^\s]+)* (https://hl7.org/fhir/datatypes.html#code)
+        #  i. packages: mostly URIs, which don't conform to [^\s]+(\s[^\s]+)* (https://hl7.org/fhir/datatypes.html#code)
         #  ii. description: can get, but tedious; downloading and caching and looking up in source ontologies
-        #  iii. type: ideally Coding (https://build.fhir.org/datatypes.html#Coding). The property value is a code
-        #  defined in an external code system. This may be used for translations, but is not the intent.
+        #  iii. type: ideally Coding (https://build.fhir.org/datatypes.html#Coding). The property value is a packages
+        #  defined in an external packages system. This may be used for translations, but is not the intent.
         #  https://hl7.org/fhir/codesystem-concept-property-type.htm
         target.property = [
-            CodeSystemProperty(code=x, uri=x, type="code") for x in self.predicates_to_export
+            CodeSystemProperty(code=x, uri=x, type="packages") for x in self.predicates_to_export
         ]
         return target
 
     def _convert_node(
         self,
         source: Node,
         index: Dict[Union[URI, CURIE], List[Edge]],
@@ -247,15 +247,15 @@
         use_curies_native_concepts: bool = False,
         use_curies_foreign_concepts: bool = True,
         predicate_period_replacement: bool = False,
     ) -> Concept:
         """Converts a node to a FHIR Concept. Also collects predicates to be included in CodeSystem.property."""
         # TODO: Use new flags
         #  self.uri(source.id)  # <--- self.uri does not exist
-        #  self.code is actually a curie. change to self.curie and add a self.code func?
+        #  self.packages is actually a curie. change to self.curie and add a self.packages func?
         _id = self.code(source.id)
         logging.debug(f"Converting node {_id} from {source}")
         concept = Concept(code=_id, display=source.lbl)
         target.concept.append(concept)
         if source.meta:
             self._convert_meta(source, concept)
         for e in index.get(source.id, []):
```

### Comparing `oaklib-0.4.0/src/oaklib/converters/obo_graph_to_obo_format_converter.py` & `oaklib-0.4.1/src/oaklib/converters/obo_graph_to_obo_format_converter.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/converters/obo_graph_to_rdf_owl_converter.py` & `oaklib-0.4.1/src/oaklib/converters/obo_graph_to_rdf_owl_converter.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/association.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/association.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/association.py` & `oaklib-0.4.1/src/oaklib/datamodels/association.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/association.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/association.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/class_enrichment.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/class_enrichment.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/class_enrichment.py` & `oaklib-0.4.1/src/oaklib/datamodels/class_enrichment.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/class_enrichment.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/class_enrichment.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/cross_ontology_diff.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/cross_ontology_diff.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/cross_ontology_diff.py` & `oaklib-0.4.1/src/oaklib/datamodels/cross_ontology_diff.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/cross_ontology_diff.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/cross_ontology_diff.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/fhir.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/fhir.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/fhir.py` & `oaklib-0.4.1/src/oaklib/datamodels/fhir.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # Auto generated from fhir.yaml by pythongen.py version: 0.9.0
 # Generation date: 2023-02-27T10:18:53
 # Schema: fhir
 #
 # id: https://w3id.org/oak/fhir
 # description: Schema for working with FHIR objects (Partial). This is currently intentionally incomplete. The
 #              sole purpose of this rendering of FHIR is purely for the purposes of using OAK to convert native
-#              OAK data models into FHIR using Python code.
+#              OAK data models into FHIR using Python packages.
 # license: https://creativecommons.org/publicdomain/zero/1.0/
 
 import dataclasses
 import re
 import sys
 from dataclasses import dataclass
 from typing import Any, ClassVar, Dict, List, Optional, Union
@@ -64,15 +64,15 @@
 
 # Class references
 
 
 @dataclass
 class CodeSystem(YAMLRoot):
     """
-    Declares the existence of and describes a code system or code system supplement
+    Declares the existence of and describes a packages system or packages system supplement
     """
 
     _inherited_slots: ClassVar[List[str]] = []
 
     class_class_uri: ClassVar[URIRef] = FHIR.codesystem
     class_class_curie: ClassVar[str] = "fhir:codesystem"
     class_name: ClassVar[str] = "CodeSystem"
@@ -301,15 +301,15 @@
     code: str = None
     value: str = None
     description: Optional[str] = None
     operator: Optional[Union[str, List[str]]] = empty_list()
 
     def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
         if self._is_empty(self.code):
-            self.MissingRequiredField("code")
+            self.MissingRequiredField("packages")
         if not isinstance(self.code, str):
             self.code = str(self.code)
 
         if self._is_empty(self.value):
             self.MissingRequiredField("value")
         if not isinstance(self.value, str):
             self.value = str(self.value)
@@ -336,15 +336,15 @@
     code: str = None
     type: str = None
     uri: Optional[Union[str, URIorCURIE]] = None
     description: Optional[str] = None
 
     def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
         if self._is_empty(self.code):
-            self.MissingRequiredField("code")
+            self.MissingRequiredField("packages")
         if not isinstance(self.code, str):
             self.code = str(self.code)
 
         if self._is_empty(self.type):
             self.MissingRequiredField("type")
         if not isinstance(self.type, str):
             self.type = str(self.type)
@@ -672,15 +672,15 @@
     domain=None,
     range=Optional[Union[Union[dict, Concept], List[Union[dict, Concept]]]],
 )
 
 slots.concept__code = Slot(
     uri=FHIR.code,
     name="concept__code",
-    curie=FHIR.curie("code"),
+    curie=FHIR.curie("packages"),
     model_uri=FHIR.concept__code,
     domain=None,
     range=Optional[str],
 )
 
 slots.concept__display = Slot(
     uri=FHIR.display,
@@ -726,15 +726,15 @@
     domain=None,
     range=Optional[Union[Union[dict, Concept], List[Union[dict, Concept]]]],
 )
 
 slots.conceptProperty__code = Slot(
     uri=FHIR.code,
     name="conceptProperty__code",
-    curie=FHIR.curie("code"),
+    curie=FHIR.curie("packages"),
     model_uri=FHIR.conceptProperty__code,
     domain=None,
     range=Optional[str],
 )
 
 slots.conceptProperty__valueCode = Slot(
     uri=FHIR.valueCode,
@@ -825,15 +825,15 @@
     domain=None,
     range=Optional[str],
 )
 
 slots.codeSystemFilter__code = Slot(
     uri=FHIR.code,
     name="codeSystemFilter__code",
-    curie=FHIR.curie("code"),
+    curie=FHIR.curie("packages"),
     model_uri=FHIR.codeSystemFilter__code,
     domain=None,
     range=str,
 )
 
 slots.codeSystemFilter__description = Slot(
     uri=FHIR.description,
@@ -861,15 +861,15 @@
     domain=None,
     range=str,
 )
 
 slots.codeSystemProperty__code = Slot(
     uri=FHIR.code,
     name="codeSystemProperty__code",
-    curie=FHIR.curie("code"),
+    curie=FHIR.curie("packages"),
     model_uri=FHIR.codeSystemProperty__code,
     domain=None,
     range=str,
 )
 
 slots.codeSystemProperty__uri = Slot(
     uri=FHIR.uri,
@@ -915,15 +915,15 @@
     domain=None,
     range=Optional[str],
 )
 
 slots.coding__code = Slot(
     uri=FHIR.code,
     name="coding__code",
-    curie=FHIR.curie("code"),
+    curie=FHIR.curie("packages"),
     model_uri=FHIR.coding__code,
     domain=None,
     range=Optional[str],
 )
 
 slots.coding__display = Slot(
     uri=FHIR.display,
```

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/fhir.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/fhir.yaml`

 * *Files 3% similar despite different names*

```diff
@@ -24,15 +24,15 @@
 default_prefix: fhir
 default_range: string
 
 
 classes:
   CodeSystem:
     class_uri: fhir:codesystem
-    description: Declares the existence of and describes a code system or code system supplement
+    description: Declares the existence of and describes a packages system or packages system supplement
     attributes:
       id:
         range: string
         comments:
           - not formally defined in FHIR schema, but present in pyrophen
       resourceType:
         designates_type: true
@@ -42,15 +42,15 @@
         range: uriorcurie
       identifier:
         identifier: false
         multivalued: true
         #range: Identifier
       version:
       name:
-        description: Name for this code system (computer friendly)
+        description: Name for this packages system (computer friendly)
       title:
       status:
         #range: PublicationStatus
       experimental:
         range: boolean
       date:
         range: datetime
@@ -132,15 +132,15 @@
         required: true
       uri:
         required: false
         range: uri
       description:
         range: string
       type:
-        # TODO: type: an enum of: code | Coding | string | integer | boolean | dateTime | decimal
+        # TODO: type: an enum of: packages | Coding | string | integer | boolean | dateTime | decimal
         #  https://hl7:org/fhir/valueset-concept-property-type.html
         required: true
         range: string
 
   Coding:
     attributes:
       system:
@@ -164,15 +164,15 @@
         range: uriorcurie
       identifier:
         identifier: false
         multivalued: true
         #range: Identifier
       version:
       name:
-        description: Name for this code system (computer friendly)
+        description: Name for this packages system (computer friendly)
       title:
       status:
         #range: PublicationStatus
       experimental:
         range: boolean
       date:
         range: datetime
```

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/lexical_index.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/lexical_index.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/lexical_index.py` & `oaklib-0.4.1/src/oaklib/datamodels/lexical_index.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/lexical_index.schema.json` & `oaklib-0.4.1/src/oaklib/datamodels/lexical_index.schema.json`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/lexical_index.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/lexical_index.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/mapping_cluster_datamodel.py` & `oaklib-0.4.1/src/oaklib/datamodels/mapping_cluster_datamodel.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/mapping_cluster_datamodel.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/mapping_cluster_datamodel.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/mapping_rules_datamodel.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/mapping_rules_datamodel.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/mapping_rules_datamodel.py` & `oaklib-0.4.1/src/oaklib/datamodels/mapping_rules_datamodel.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/mapping_rules_datamodel.schema.json` & `oaklib-0.4.1/src/oaklib/datamodels/mapping_rules_datamodel.schema.json`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/mapping_rules_datamodel.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/mapping_rules_datamodel.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/obograph.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/obograph.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/obograph.py` & `oaklib-0.4.1/src/oaklib/datamodels/obograph.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/obograph.schema.json` & `oaklib-0.4.1/src/oaklib/datamodels/obograph.schema.json`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/obograph.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/obograph.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/ontology_metadata.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/ontology_metadata.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/ontology_metadata.py` & `oaklib-0.4.1/src/oaklib/datamodels/ontology_metadata.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/ontology_metadata.schema.json` & `oaklib-0.4.1/src/oaklib/datamodels/ontology_metadata.schema.json`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/ontology_metadata.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/ontology_metadata.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/oxo.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/oxo.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/oxo.py` & `oaklib-0.4.1/src/oaklib/datamodels/oxo.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/oxo.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/oxo.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/search.py` & `oaklib-0.4.1/src/oaklib/datamodels/search.py`

 * *Files 6% similar despite different names*

```diff
@@ -20,15 +20,15 @@
 
 def create_search_configuration(term: str) -> "SearchConfiguration":
     """
     Generates a search configuration based on search syntax
 
     term is either a plaintext search term, or a search term prefixed by
 
-    - 1. a property code, one of t, ., l (for term, anything, label)
+    - 1. a property packages, one of t, ., l (for term, anything, label)
     - 2. a match type indicator, one of "~","/","=","^"
 
     For more documentation, see `Search docs <https://incatools.github.io/ontology-access-kit/interfaces/search.html>`_
 
     :param term:
     :return:
     """
@@ -58,15 +58,15 @@
             elif prop == "l":
                 props = [SearchProperty.LABEL]
             elif prop == "i":
                 props = [SearchProperty.IDENTIFIER]
             elif prop == "x":
                 props = [SearchProperty.MAPPED_IDENTIFIER]
             else:
-                raise ValueError(f"Unknown property code: {prop}")
+                raise ValueError(f"Unknown property packages: {prop}")
             cfg.properties = [SearchProperty(p) for p in props]
         return cfg
     else:
         return SearchConfiguration([term], properties=DEFAULT_SEARCH_PROPERTIES)
 
 
 def search_properties_to_predicates(props: List[SearchProperty]) -> List[PRED_CURIE]:
```

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/search_datamodel.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/search_datamodel.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/search_datamodel.py` & `oaklib-0.4.1/src/oaklib/datamodels/search_datamodel.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/search_datamodel.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/search_datamodel.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/similarity.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/similarity.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/similarity.py` & `oaklib-0.4.1/src/oaklib/datamodels/similarity.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/similarity.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/similarity.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/summary_statistics_datamodel.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/summary_statistics_datamodel.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/summary_statistics_datamodel.py` & `oaklib-0.4.1/src/oaklib/datamodels/summary_statistics_datamodel.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/summary_statistics_datamodel.schema.json` & `oaklib-0.4.1/src/oaklib/datamodels/summary_statistics_datamodel.schema.json`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/summary_statistics_datamodel.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/summary_statistics_datamodel.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/taxon_constraints.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/taxon_constraints.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/taxon_constraints.py` & `oaklib-0.4.1/src/oaklib/datamodels/taxon_constraints.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/taxon_constraints.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/taxon_constraints.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/text_annotator.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/text_annotator.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/text_annotator.py` & `oaklib-0.4.1/src/oaklib/datamodels/text_annotator.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/text_annotator.schema.json` & `oaklib-0.4.1/src/oaklib/datamodels/text_annotator.schema.json`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/text_annotator.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/text_annotator.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/validation_datamodel.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/validation_datamodel.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/validation_datamodel.py` & `oaklib-0.4.1/src/oaklib/datamodels/validation_datamodel.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/validation_datamodel.schema.json` & `oaklib-0.4.1/src/oaklib/datamodels/validation_datamodel.schema.json`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/validation_datamodel.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/validation_datamodel.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/value_set_configuration.owl.ttl` & `oaklib-0.4.1/src/oaklib/datamodels/value_set_configuration.owl.ttl`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/value_set_configuration.py` & `oaklib-0.4.1/src/oaklib/datamodels/value_set_configuration.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/value_set_configuration.yaml` & `oaklib-0.4.1/src/oaklib/datamodels/value_set_configuration.yaml`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/datamodels/vocabulary.py` & `oaklib-0.4.1/src/oaklib/datamodels/vocabulary.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/__init__.py` & `oaklib-0.4.1/src/oaklib/implementations/__init__.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/aggregator/aggregator_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/aggregator/aggregator_implementation.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/cx/cx_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/cx/cx_implementation.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/funowl/funowl_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/funowl/funowl_implementation.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/gilda.py` & `oaklib-0.4.1/src/oaklib/implementations/gilda.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/kgx/kgx_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/kgx/kgx_implementation.py`

 * *Files 1% similar despite different names*

```diff
@@ -206,21 +206,21 @@
     """
     A :class:`OntologyInterface` implementation that wraps a KGX Relational Database.
 
     This could be a local file (accessed via SQL Lite) or a local/remote server (e.g PostgreSQL).
 
     To connect, either use KGXImplementation directly:
 
-    .. code:: python
+    .. packages:: python
 
         >>> oi = KGXImplementation(OntologyResource(slug=f"sqlite:///{path}"))
 
     Or use a selector:
 
-    .. code:: python
+    .. packages:: python
 
         >>> oi = get_implementation_from_shorthand('obojson:path/to/my/ontology.db')
 
     The schema is assumed to follow the `semantic-sql <https://github.com/incatools/semantic-sql>`_ schema.
 
     This uses SQLAlchemy ORM Models:
```

### Comparing `oaklib-0.4.0/src/oaklib/implementations/obograph/obograph_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/obograph/obograph_implementation.py`

 * *Files 0% similar despite different names*

```diff
@@ -71,15 +71,15 @@
     """
     OBO Graphs JSON backed implementation.
 
     This implementation works off of an in-memory GraphDocument object.
 
     To use:
 
-    .. code :: python
+    .. packages :: python
 
         >>> oi = get_implementation_from_shorthand('obojson:path/to/my/ontology.json')
         >>> for term in oi.entities():
         >>>     ...
     """
 
     obograph_document: GraphDocument = None
@@ -325,15 +325,15 @@
 
     # TODO: DRY
     def incoming_relationship_map(self, *args, **kwargs) -> RELATIONSHIP_MAP:
         return pairs_as_dict(self.incoming_relationships(*args, **kwargs))
 
     # TODO: DRY
     def basic_search(self, search_term: str, config: SearchConfiguration = None) -> Iterable[CURIE]:
-        # TODO: move up, avoid repeating code
+        # TODO: move up, avoid repeating packages
         if config is None:
             config = SearchConfiguration()
         matches = []
         mfunc = None
         if config.syntax == SearchTermSyntax(SearchTermSyntax.STARTS_WITH):
             mfunc = lambda label: str(label).startswith(search_term)
         elif config.syntax == SearchTermSyntax(SearchTermSyntax.REGULAR_EXPRESSION):
```

### Comparing `oaklib-0.4.0/src/oaklib/implementations/ols/ols_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/ols/ols_implementation.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/ols/oxo_utils.py` & `oaklib-0.4.1/src/oaklib/implementations/ols/oxo_utils.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/ontobee/ontobee_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/ontobee/ontobee_implementation.py`

 * *Files 6% similar despite different names*

```diff
@@ -16,23 +16,23 @@
     AbstractSparqlImplementation, SearchInterface, MappingProviderInterface, OboGraphInterface
 ):
     """
     Wraps the Ontobee sparql endpoint
 
     An OntobeeImplementation can be initialed by:
 
-        .. code:: python
+        .. packages:: python
 
            >>>  oi = OntobeeImplementation()
 
     The default ontobee endpoint will be assumed
 
     Alternatively, use a selector:
 
-    .. code :: python
+    .. packages :: python
 
         >>> oi = get_implementation_from_shorthand("ontobee:")
         >>> for a in oi.ancestors("UBERON:0002398", predicates=[IS_A]):
         >>>     ...
 
 
     See: `<https://www.ontobee.org/>`_
```

### Comparing `oaklib-0.4.0/src/oaklib/implementations/ontoportal/bioportal_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/ontoportal/bioportal_implementation.py`

 * *Files 2% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 @dataclass
 class BioPortalImplementation(OntoPortalImplementationBase):
     """
     A :ref:`OntoPortal` implementation that connects to a bioportal endpoint.
 
     Example:
 
-    .. code :: python
+    .. packages :: python
 
         >>> api_key = get_apikey_value(BioPortalImplementation.ontoportal_client_class.name)
         >>> oi = BioPortalImplementation(api_key=api_key)
         >>> text = "increased expression of Shh in interneuron populations in the forebrain"
         >>> for ann in oi.annotate_text(text)
         >>>     ...
```

### Comparing `oaklib-0.4.0/src/oaklib/implementations/ontoportal/ontoportal_implementation_base.py` & `oaklib-0.4.1/src/oaklib/implementations/ontoportal/ontoportal_implementation_base.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/pronto/pronto_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/pronto/pronto_implementation.py`

 * *Files 2% similar despite different names*

```diff
@@ -41,24 +41,24 @@
     SCOPE_TO_SYNONYM_PRED_MAP,
     SEMAPV,
     SKOS_CLOSE_MATCH,
     TERM_REPLACED_BY,
     TERMS_MERGED,
 )
 from oaklib.interfaces import TextAnnotatorInterface
-from oaklib.interfaces.association_provider_interface import (
-    AssociationProviderInterface,
-)
 from oaklib.interfaces.basic_ontology_interface import (
     ALIAS_MAP,
     METADATA_MAP,
     PRED_CURIE,
     RELATIONSHIP,
     RELATIONSHIP_MAP,
 )
+from oaklib.interfaces.class_enrichment_calculation_interface import (
+    ClassEnrichmentCalculationInterface,
+)
 from oaklib.interfaces.differ_interface import DifferInterface
 from oaklib.interfaces.dumper_interface import DumperInterface
 from oaklib.interfaces.mapping_provider_interface import MappingProviderInterface
 from oaklib.interfaces.merge_interface import MergeInterface
 from oaklib.interfaces.obograph_interface import OboGraphInterface
 from oaklib.interfaces.obolegacy_interface import OboLegacyInterface
 from oaklib.interfaces.patcher_interface import PatcherInterface
@@ -89,15 +89,16 @@
     RdfInterface,
     OboGraphInterface,
     OboLegacyInterface,
     SearchInterface,
     MappingProviderInterface,
     PatcherInterface,
     DifferInterface,
-    AssociationProviderInterface,
+    # AssociationProviderInterface,
+    ClassEnrichmentCalculationInterface,
     SemanticSimilarityInterface,
     TextAnnotatorInterface,
     SummaryStatisticsInterface,
     TaxonConstraintInterface,
     DumperInterface,
     MergeInterface,
 ):
@@ -106,29 +107,29 @@
 
     - obo
     - obojson
     - owl rdf/xml
 
     To load a local file:
 
-    .. code:: python
+    .. packages:: python
 
         >>> resource = OntologyResource(slug='go.obo', directory='input', local=True)
         >>> oi = ProntoImplementation(resource)
 
     To load from the OBO library:
 
-    .. code:: python
+    .. packages:: python
 
         >>> resource = OntologyResource(local=False, slug='go.obo'))
         >>> oi = ProntoImplementation(resource)
 
     Currently this implementation implements most of the BaseOntologyInterface
 
-    .. code:: python
+    .. packages:: python
 
         >>> rels = oi.outgoing_relationships('GO:0005773')
         >>> for rel, parents in rels.items():
         >>>    print(f'  {rel} ! {oi.label(rel)}')
         >>>        for parent in parents:
         >>>            print(f'    {parent} ! {oi.label(parent)}')
 
@@ -845,10 +846,16 @@
             # rather than forcing all synonyms to be related.
             scope = str(patch.qualifier.value).upper() if patch.qualifier else "RELATED"
             t.add_synonym(description=patch.new_value, scope=scope)
         elif isinstance(patch, kgcl.EdgeCreation):
             self.add_relationship(patch.subject, patch.predicate, patch.object)
         elif isinstance(patch, kgcl.EdgeDeletion):
             self.remove_relationship(patch.subject, patch.predicate, patch.object)
+        elif isinstance(patch, kgcl.RemoveSynonym):
+            t = self._entity(patch.about_node, strict=True)
+            synonym_to_remove = [
+                syn for syn in t._data().synonyms if syn.description == patch.old_value
+            ][0]
+            t._data().synonyms.discard(synonym_to_remove)
         else:
             raise NotImplementedError(f"cannot handle KGCL type {type(patch)}")
         return patch
```

### Comparing `oaklib-0.4.0/src/oaklib/implementations/simpleobo/simple_obo_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/simpleobo/simple_obo_implementation.py`

 * *Files 1% similar despite different names*

```diff
@@ -430,15 +430,15 @@
                 if p == LABEL_PREDICATE:
                     continue
                 for v in vs:
                     yield curie, SynonymPropertyValue(pred=p.replace("oio:", ""), val=v)
 
     def map_shorthand_to_curie(self, rel_code: PRED_CODE) -> PRED_CURIE:
         """
-        Maps either a true relationship type CURIE or a shorthand code to a CURIE.
+        Maps either a true relationship type CURIE or a shorthand packages to a CURIE.
 
         See `section 5.9 <https://owlcollab.github.io/oboformat/doc/obo-syntax.html#5.9>`_
 
         :param rel_code:
         :return:
         """
         for _, x in self.simple_mappings_by_curie(rel_code):
@@ -482,15 +482,15 @@
                     if predicates is not None and p not in predicates:
                         continue
                     if objects is not None and o not in objects:
                         continue
                     yield s, p, o
 
     def basic_search(self, search_term: str, config: SearchConfiguration = None) -> Iterable[CURIE]:
-        # TODO: move up, avoid repeating code
+        # TODO: move up, avoid repeating packages
         if config is None:
             config = SearchConfiguration()
         matches = []
         mfunc = None
         if config.syntax == SearchTermSyntax(SearchTermSyntax.STARTS_WITH):
             mfunc = lambda label: str(label).startswith(search_term)
         elif config.syntax == SearchTermSyntax(SearchTermSyntax.REGULAR_EXPRESSION):
@@ -768,16 +768,18 @@
         elif isinstance(patch, kgcl.NodeObsoletion):
             t = self._stanza(patch.about_node, strict=True)
             t.set_singular_tag(TAG_IS_OBSOLETE, "true")
             if isinstance(patch, kgcl.NodeObsoletionWithDirectReplacement):
                 t.set_singular_tag(TAG_REPLACED_BY, patch.has_direct_replacement)
             modified_entities.append(patch.about_node)
         elif isinstance(patch, kgcl.NodeDeletion):
-            t = self._stanza(patch.about_node, strict=True)
-            od.stanzas = [s for s in od.stanzas if s.id != patch.about_node]
+            try:
+                del od.stanzas[patch.about_node]
+            except KeyError:
+                logging.error(f"CURIE {patch.about_node} does not exist in the OBO file provided.")
         elif isinstance(patch, kgcl.NodeCreation):
             self.create_entity(patch.about_node, patch.name)
             modified_entities.append(patch.about_node)
         elif isinstance(patch, kgcl.ClassCreation):
             self.create_entity(patch.about_node, patch.name)
             modified_entities.append(patch.about_node)
         elif isinstance(patch, kgcl.SynonymReplacement):
@@ -788,39 +790,41 @@
                     syn = tv.as_synonym()
                     if syn[0] == patch.old_value:
                         tv.replace_quoted_part(patch.new_value)
                         n += 1
             if not n:
                 raise ValueError(f"Failed to find synonym {patch.old_value} for {t.id}")
             modified_entities.append(patch.about_node)
-        elif isinstance(patch, kgcl.NodeTextDefinitionChange):
-            t = self._stanza(patch.about_node, strict=True)
-            for tv in t.tag_values:
-                if tv == TAG_DEFINITION:
-                    tv.replace_quoted_part(patch.new_value)
         elif isinstance(patch, kgcl.NewTextDefinition):
             t = self._stanza(patch.about_node, strict=True)
             t.add_tag_value(TAG_DEFINITION, patch.new_value)
             modified_entities.append(patch.about_node)
+        elif isinstance(patch, kgcl.NodeTextDefinitionChange):
+            t = self._stanza(patch.about_node, strict=True)
+            for tv in t.tag_values:
+                if tv.tag == TAG_DEFINITION:
+                    tv.replace_quoted_part(patch.new_value.strip("'"))
         elif isinstance(patch, kgcl.NewSynonym):
             t = self._stanza(patch.about_node, strict=True)
             # Get scope from patch.qualifier
             # rather than forcing all synonyms to be related.
             if type(patch.qualifier) == str:
                 scope = patch.qualifier.upper()
             else:
                 scope = str(patch.qualifier.value).upper() if patch.qualifier else "RELATED"
             v = patch.new_value.replace('"', '\\"')
             t.add_tag_value(TAG_SYNONYM, f'"{v}" {scope} []')
             modified_entities.append(patch.about_node)
         elif isinstance(patch, kgcl.RemoveSynonym):
             t = self._stanza(patch.about_node, strict=True)
             # scope = str(patch.qualifier.value).upper() if patch.qualifier else "RELATED"
-            v = patch.old_value.replace('"', '\\"')
-            t.remove_simple_tag_value(TAG_SYNONYM, f'"{v}"')
+            v = patch.old_value.strip(
+                '"'
+            )  # Handling a bug where quotes are accidentally introduced.
+            t.remove_tag_quoted_value(TAG_SYNONYM, v)
         elif isinstance(patch, kgcl.EdgeCreation):
             self.add_relationship(patch.subject, patch.predicate, patch.object)
             modified_entities.append(patch.subject)
         elif isinstance(patch, kgcl.EdgeDeletion):
             self.remove_relationship(patch.subject, patch.predicate, patch.object)
         elif isinstance(patch, kgcl.NodeMove):
             logging.warning(f"Cannot handle {patch}")
```

### Comparing `oaklib-0.4.0/src/oaklib/implementations/simpleobo/simple_obo_parser.py` & `oaklib-0.4.1/src/oaklib/implementations/simpleobo/simple_obo_parser.py`

 * *Files 2% similar despite different names*

```diff
@@ -317,14 +317,17 @@
 
     tag_values: List[TagValue] = field(default_factory=lambda: [])
     """List of all tag-value pairs for this stanza or header"""
 
     def _simple_value(self, v) -> str:
         return v.split(" ")[0]
 
+    def _quoted_value(self, v) -> str:
+        return re.findall('"([^"]*)"', v)[0]
+
     def _values(self, tag: TAG) -> List[str]:
         return [tv.value for tv in self.tag_values if tv.tag == tag]
 
     def normalize_order(self):
         self.tag_values = sorted(self.tag_values, key=lambda x: x.order())
 
     def simple_values(self, tag: TAG) -> List[CURIE]:
@@ -398,19 +401,22 @@
         :param strict:
         :return:
         """
         vals = self._values(tag)
         if vals:
             if strict and len(vals) > 1:
                 raise ValueError(f"Multiple vals {vals} for {tag} in {self.id}")
-            m = re_quoted_simple.match(vals[0])
-            if m:
-                return m.group(1)
+            if "[" in vals[0]:
+                m = re_quoted_simple.match(vals[0])
+                if m:
+                    return m.group(1)
+                else:
+                    raise ValueError(f"Could not parse quoted string from {vals}")
             else:
-                raise ValueError(f"Could not parse quoted string from {vals}")
+                return vals[0]
 
     def synonyms(self) -> List[SYNONYM_TUPLE]:
         """
         All synonyms for a stanza
 
         :return: list of synonyms
         """
@@ -441,29 +447,49 @@
             self.add_tag_value(tag, val)
 
     def remove_simple_tag_value(self, tag: TAG, val: str) -> None:
         """
         removes a simple tag-value such as is_a
 
         :param tag:
-        :param val:
+        :param val: ID value.
         :return:
         """
         n = 0
         tvs = []
         for tv in self.tag_values:
             if tv.tag == tag:
                 if self._simple_value(tv.value) == val:
                     n += 1
                     continue
             tvs.append(tv)
         if not n:
             logging.warning(f"No values to remove for {tag} = {val} // {self}")
         self.tag_values = tvs
 
+    def remove_tag_quoted_value(self, tag: TAG, val: str) -> None:
+        """
+        removes a simple tag-value such as synonym or definition.
+
+        :param tag:
+        :param val: Quoted value.
+        :return:
+        """
+        n = 0
+        tvs = []
+        for tv in self.tag_values:
+            if tv.tag == tag:
+                if self._quoted_value(tv.value) == val:
+                    n += 1
+                    continue
+            tvs.append(tv)
+        if not n:
+            logging.warning(f"No values to remove for {tag} = {val} // {self}")
+        self.tag_values = tvs
+
     def remove_pairwise_tag_value(self, tag: TAG, val1: str, val2: str) -> None:
         """
         removes a simple tag-value such as is_a
 
         :param tag:
         :param val:
         :return:
```

### Comparing `oaklib-0.4.0/src/oaklib/implementations/sparql/abstract_sparql_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/sparql/abstract_sparql_implementation.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/sparql/lov_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/sparql/lov_implementation.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/sparql/oak_metamodel_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/sparql/oak_metamodel_implementation.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/sparql/sparql_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/sparql/sparql_implementation.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/sparql/sparql_query.py` & `oaklib-0.4.1/src/oaklib/implementations/sparql/sparql_query.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/sqldb/sql_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/sqldb/sql_implementation.py`

 * *Files 1% similar despite different names*

```diff
@@ -254,21 +254,21 @@
     """
     A :class:`OntologyInterface` implementation that wraps a SQL Relational Database.
 
     This could be a local file (accessed via SQL Lite) or a local/remote server (e.g PostgreSQL).
 
     To connect, either use SqlImplementation directly:
 
-    .. code:: python
+    .. packages:: python
 
         >>> oi = SqlImplementation(OntologyResource(slug=f"sqlite:///{path}"))
 
     Or use a selector:
 
-    .. code:: python
+    .. packages:: python
 
         >>> oi = get_implementation_from_shorthand('obojson:path/to/my/ontology.db')
 
     The schema is assumed to follow the `semantic-sql <https://github.com/incatools/semantic-sql>`_ schema.
 
     This uses SQLAlchemy ORM Models:
 
@@ -1592,15 +1592,15 @@
                 )
                 yield result
         if not is_used:
             return
         if slot.pattern:
             # check values against regexes
             # NOTE: this may be slow as we have to do this in
-            # code rather than SQL. Some SQL engines have regex support,
+            # packages rather than SQL. Some SQL engines have regex support,
             # and we should leverage that when it exists
             re_pattern = re.compile(slot.pattern)
             main_q = self.session.query(Statements).filter(Statements.predicate == predicate)
             for row in main_q:
                 val = row.value if row.value is not None else row.object
                 if val is not None:
                     if not re_pattern.match(val):
@@ -1907,14 +1907,28 @@
             elif isinstance(patch, kgcl.NewSynonym):
                 # TODO: synonym type
                 self._execute(
                     insert(Statements).values(
                         subject=about, predicate=HAS_EXACT_SYNONYM, value=patch.new_value
                     )
                 )
+            elif isinstance(patch, kgcl.RemoveSynonym):
+                q = self.session.query(Statements).filter(
+                    Statements.subject == about, Statements.value == patch.old_value
+                )
+                self._execute(
+                    delete(Statements).where(
+                        and_(
+                            Statements.subject == about,
+                            Statements.predicate.in_(SYNONYM_PREDICATES),
+                            Statements.value == patch.old_value,
+                        )
+                    )
+                )
+
             elif isinstance(patch, kgcl.NodeObsoletion):
                 self.check_node_exists(about)
                 self._set_predicate_value(
                     about, DEPRECATED_PREDICATE, value="true", datatype="xsd:string"
                 )
                 if isinstance(patch, kgcl.NodeObsoletionWithDirectReplacement):
                     # TODO: allow switching between value and object
@@ -1953,24 +1967,49 @@
                                 )
                 logging.debug(f"replacing synonym with predicate: {predicate}")
                 self._execute(
                     delete(Statements).where(
                         and_(
                             Statements.subject == about,
                             Statements.predicate == predicate,
-                            Statements.predicate == predicate,
                             Statements.value == patch.old_value,
                         )
                     )
                 )
                 self._execute(
                     insert(Statements).values(
                         subject=about, predicate=predicate, value=patch.new_value
                     )
                 )
+            elif isinstance(patch, kgcl.NewTextDefinition):
+                q = self.session.query(Statements).filter(
+                    Statements.subject == about, Statements.predicate == HAS_DEFINITION_CURIE
+                )
+                if q.count() == 0:
+                    self._execute(
+                        insert(Statements).values(
+                            subject=about, predicate=HAS_DEFINITION_CURIE, value=patch.new_value
+                        )
+                    )
+                else:
+                    self.apply_patch(
+                        kgcl.NodeTextDefinitionChange(subject=about, value=patch.new_value)
+                    )
+            elif isinstance(patch, kgcl.NodeTextDefinitionChange):
+                stmt = (
+                    update(Statements)
+                    .where(
+                        and_(
+                            Statements.subject == about,
+                            Statements.predicate == HAS_DEFINITION_CURIE,
+                        )
+                    )
+                    .values(value=patch.new_value)
+                )
+                self._execute(stmt)
             else:
                 raise NotImplementedError(f"Unknown patch type: {type(patch)}")
         elif isinstance(patch, kgcl.EdgeChange):
             about = patch.about_edge
             if isinstance(patch, kgcl.EdgeCreation):
                 self._execute(
                     insert(Statements).values(
```

### Comparing `oaklib-0.4.0/src/oaklib/implementations/sqldb/sqlite_utils.py` & `oaklib-0.4.1/src/oaklib/implementations/sqldb/sqlite_utils.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/translator/translator_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/translator/translator_implementation.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/implementations/ubergraph/ubergraph_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/ubergraph/ubergraph_implementation.py`

 * *Files 0% similar despite different names*

```diff
@@ -60,15 +60,15 @@
     See: `<https://github.com/INCATools/ubergraph>`_
 
     This is a specialization of the more generic :class:`.SparqlImplementation`, which
     has knowledge of some of the specialized patterns found in Ubergraph
 
     An UbergraphImplementation can be initialed by:
 
-        .. code:: python
+        .. packages:: python
 
            >>>  oi = UbergraphImplementation()
 
         The default ubergraph endpoint will be assumed
 
     """
```

### Comparing `oaklib-0.4.0/src/oaklib/implementations/uniprot/uniprot_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/uniprot/uniprot_implementation.py`

 * *Files 1% similar despite different names*

```diff
@@ -80,15 +80,15 @@
     Wraps the Uniprot sparql endpoint.
 
     This is a specialization of the more generic :class:`.SparqlImplementation`, which
     has knowledge of some of the specialized patterns found in Uniprot
 
     An UniprotImplementation can be initialed by:
 
-        .. code:: python
+        .. packages:: python
 
            >>>  oi = UniprotImplementation()
 
     The default Uniprot endpoint will be assumed
 
     """
```

### Comparing `oaklib-0.4.0/src/oaklib/implementations/wikidata/wikidata_implementation.py` & `oaklib-0.4.1/src/oaklib/implementations/wikidata/wikidata_implementation.py`

 * *Files 1% similar despite different names*

```diff
@@ -58,15 +58,15 @@
     See: `<https://github.com/INCATools/wikidata>`_
 
     This is a specialization of the more generic :class:`.SparqlImplementation`, which
     has knowledge of some of the specialized patterns found in wikidata
 
     An wikidataImplementation can be initialed by:
 
-        .. code:: python
+        .. packages:: python
 
            >>>  oi = WikidataImplementation.create()
 
         The default wikidata endpoint will be assumed
 
     """
```

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/__init__.py` & `oaklib-0.4.1/src/oaklib/interfaces/__init__.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/association_provider_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/association_provider_interface.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+import logging
 from abc import ABC
 from collections import defaultdict
 from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple
 
 from oaklib.datamodels.association import Association
 from oaklib.interfaces.basic_ontology_interface import BasicOntologyInterface
 from oaklib.interfaces.obograph_interface import OboGraphInterface
@@ -77,14 +78,17 @@
                 # TODO: use more efficient procedure when object has many descendants
                 objects = list(
                     self.descendants(list(objects), predicates=object_closure_predicates)
                 )
             else:
                 raise NotImplementedError
         ix = self._association_index
+        if ix is None:
+            logging.warning("No association index")
+            return
         for a in ix.lookup(subjects, predicates, objects):
             yield a
 
     def add_associations(self, associations: Iterable[Association]) -> bool:
         """
         Store a collection of associations for later retrievals.
```

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/basic_ontology_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/basic_ontology_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/differ_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/differ_interface.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,14 +1,21 @@
 import logging
 from abc import ABC
 from dataclasses import dataclass
 from typing import Any, Dict, Iterator, Optional, Tuple
 
 import kgcl_schema.datamodel.kgcl as kgcl
-from kgcl_schema.datamodel.kgcl import Change, ClassCreation, NodeCreation, NodeDeletion
+from kgcl_schema.datamodel.kgcl import (
+    Change,
+    ClassCreation,
+    NewTextDefinition,
+    NodeCreation,
+    NodeDeletion,
+    NodeTextDefinitionChange,
+)
 
 from oaklib.datamodels.vocabulary import (
     DEPRECATED_PREDICATE,
     HAS_OBSOLESCENCE_REASON,
     OWL_CLASS,
     TERM_REPLACED_BY,
     TERMS_MERGED,
@@ -52,14 +59,16 @@
         types are supported:
 
         - NodeCreation
         - NodeDeletion
         - NodeMove
         - NodeRename
         - PredicateChange
+        - NewTextDefinition
+        - NodeTextDefinitionChange
 
         :param other_ontology:
         :param configuration:
         :return: KGCL change object
         """
         if configuration is None:
             configuration = DiffConfiguration()
@@ -97,14 +106,37 @@
                                 yield kgcl.NodeObsoletionWithDirectReplacement(
                                     id=_gen_id(),
                                     about_node=e1,
                                     has_direct_replacement=e2_metadata[TERM_REPLACED_BY][0],
                                 )
                         else:
                             yield kgcl.NodeObsoletion(id=_gen_id(), about_node=e1)
+            # Check for definition change/addition
+            if self.definition(e1) != other_ontology.definition(e1):
+                if self.definition(e1) is None or other_ontology.definition(e1) is None:
+                    old_value = new_value = None
+                    if self.definition(e1):
+                        old_value = self.definition(e1)
+
+                    if other_ontology.definition(e1):
+                        new_value = other_ontology.definition(e1)
+
+                    yield NewTextDefinition(
+                        id=_gen_id(), about_node=e1, new_value=new_value, old_value=old_value
+                    )
+                elif self.definition(e1) is not None and other_ontology.definition(e1) is not None:
+                    yield NodeTextDefinitionChange(
+                        id=_gen_id(),
+                        about_node=e1,
+                        new_value=other_ontology.definition(e1),
+                        old_value=self.definition(e1),
+                    )
+                else:
+                    logging.info(f"Both ontologies have no definition for {e1}")
+
             differs = self.different_from(e1, other_ontology)
             if differs is not None and not differs:
                 continue
             e1_arels = set(self.alias_relationships(e1, exclude_labels=True))
             e2_arels = set(other_ontology.alias_relationships(e1, exclude_labels=True))
             for arel in e1_arels.difference(e2_arels):
                 pred, alias = arel
```

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/dumper_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/dumper_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/mapping_provider_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/mapping_provider_interface.py`

 * *Files 4% similar despite different names*

```diff
@@ -12,15 +12,15 @@
 
 class MappingProviderInterface(BasicOntologyInterface, ABC):
     """
     An ontology provider that provides SSSOM mappings.
 
     """
 
-    # TODO: move code from mapping-walker
+    # TODO: move packages from mapping-walker
 
     def inject_mapping_labels(self, mappings: Iterable[Mapping]) -> None:
         for mapping in mappings:
             if not mapping.subject_label:
                 mapping.subject_label = self.label(mapping.subject_id)
             if not mapping.object_label:
                 mapping.object_label = self.label(mapping.object_id)
```

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/merge_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/merge_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/metadata_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/metadata_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/obograph_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/obograph_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/obolegacy_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/obolegacy_interface.py`

 * *Files 12% similar despite different names*

```diff
@@ -12,15 +12,15 @@
     A BasicOntologyInterface that provides a bridge to legacy OBO Format concepts
 
     See <https://owlcollab.github.io/oboformat/doc/obo-syntax.html>_
     """
 
     def map_shorthand_to_curie(self, rel_code: PRED_CODE) -> PRED_CURIE:
         """
-        Maps either a true relationship type CURIE or a shorthand code to a CURIE.
+        Maps either a true relationship type CURIE or a shorthand packages to a CURIE.
 
         See `section 5.9 <https://owlcollab.github.io/oboformat/doc/obo-syntax.html#5.9>`_
 
         :param rel_code:
         :return:
         """
         raise NotImplementedError
```

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/ontology_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/ontology_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/owl_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/owl_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/patcher_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/patcher_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/rdf_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/rdf_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/relation_graph_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/relation_graph_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/search_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/search_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/semsim_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/semsim_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/skos_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/skos_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/subsetter_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/subsetter_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/summary_statistics_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/summary_statistics_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/taxon_constraint_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/taxon_constraint_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/text_annotator_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/text_annotator_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/interfaces/validator_interface.py` & `oaklib-0.4.1/src/oaklib/interfaces/validator_interface.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/heatmap_writer.py` & `oaklib-0.4.1/src/oaklib/io/heatmap_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/html_writer.py` & `oaklib-0.4.1/src/oaklib/io/html_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/obograph_writer.py` & `oaklib-0.4.1/src/oaklib/io/obograph_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/rollup_report_writer.py` & `oaklib-0.4.1/src/oaklib/io/rollup_report_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_axiom_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_axiom_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_csv_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_csv_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_fhir_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_fhir_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_info_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_info_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_json_lines_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_json_lines_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_json_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_json_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_kgcl_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_kgcl_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_markdown_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_markdown_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_nl_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_nl_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_obo_json_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_obo_json_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_obo_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_obo_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_owl_functional_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_owl_functional_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_rdf_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_rdf_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/io/streaming_yaml_writer.py` & `oaklib-0.4.1/src/oaklib/io/streaming_yaml_writer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/mappers/base_mapper.py` & `oaklib-0.4.1/src/oaklib/mappers/base_mapper.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/mappers/ontology_metadata_mapper.py` & `oaklib-0.4.1/src/oaklib/mappers/ontology_metadata_mapper.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/parsers/__init__.py` & `oaklib-0.4.1/src/oaklib/parsers/__init__.py`

 * *Files 24% similar despite different names*

```diff
@@ -18,23 +18,39 @@
     "PhafAssociationParser",
 ]
 
 from oaklib.parsers.hpoa_g2p_association_parser import HpoaG2PAssociationParser
 from oaklib.parsers.pairwise_association_parser import PairwiseAssociationParser
 
 GAF = "gaf"
+"""Gene Ontology GAF syntax"""
+
 G2T = "g2t"
+"""Simple pairwise gene to term 2 column syntax"""
+
 HPOA = "hpoa"
+"""HPO Annotation syntax"""
+
 HPOA_G2P = "hpoa_g2p"
+"""HPO Gene-to-Phenotype syntax"""
+
 KGX = "kgx"
+"""KGX TSV syntax"""
+
 PHAF = "phaf"
+"""PomBase Phenotype Association Format"""
 
 
 @cache
 def get_association_parser_resolver() -> ClassResolver[AssociationParser]:
+    """
+    Get a class resolver for association parsers.
+
+    :return: ClassResolver
+    """
     association_parser_resolver: ClassResolver[AssociationParser] = ClassResolver.from_subclasses(
         AssociationParser,
         suffix="AssociationParser",
     )
     association_parser_resolver.synonyms.update(
         {
             GAF: GafAssociationParser,
```

### Comparing `oaklib-0.4.0/src/oaklib/parsers/association_parser.py` & `oaklib-0.4.1/src/oaklib/parsers/association_parser.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/parsers/boomer_parser.py` & `oaklib-0.4.1/src/oaklib/parsers/boomer_parser.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/parsers/gaf_association_parser.py` & `oaklib-0.4.1/src/oaklib/parsers/gaf_association_parser.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/parsers/hpoa_association_parser.py` & `oaklib-0.4.1/src/oaklib/parsers/hpoa_association_parser.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/parsers/hpoa_g2p_association_parser.py` & `oaklib-0.4.1/src/oaklib/parsers/hpoa_g2p_association_parser.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/parsers/kgx_association_parser.py` & `oaklib-0.4.1/src/oaklib/parsers/kgx_association_parser.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/parsers/pairwise_association_parser.py` & `oaklib-0.4.1/src/oaklib/parsers/pairwise_association_parser.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/parsers/parser_base.py` & `oaklib-0.4.1/src/oaklib/parsers/parser_base.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/parsers/phaf_association_parser.py` & `oaklib-0.4.1/src/oaklib/parsers/phaf_association_parser.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/parsers/xaf_association_parser.py` & `oaklib-0.4.1/src/oaklib/parsers/xaf_association_parser.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/resource.py` & `oaklib-0.4.1/src/oaklib/resource.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/selector.py` & `oaklib-0.4.1/src/oaklib/selector.py`

 * *Files 1% similar despite different names*

```diff
@@ -30,15 +30,15 @@
     This function allows you to get an adapter for a given descriptor.
     A descriptor combines a *scheme* followed by a colon symbol, and then
     optionally additional information that specifies how to access a particular
     resource or ontology within that scheme.
 
     Example:
 
-    .. code :: python
+    .. packages :: python
 
         >>> from oaklib import get_adapter
         >>>
         >>> ## Use the simpleobo adapter to read a local OBO file:
         >>> adapter = get_adapter('simpleobo:tests/input/go-nucleus.obo')
         >>> print(adapter.label("GO:0005634"))
         nucleus
@@ -50,15 +50,15 @@
         >>> adapter = get_adapter('ubergraph:')
         >>> print(adapter.label("GO:0005634"))
         nucleus
 
     If you omit the scheme then OAK will try to guess the scheme based on the
     suffix of the descriptor
 
-    .. code :: python
+    .. packages :: python
 
         >>> from oaklib import get_adapter
         >>> ## Use an adapter that is able to read OBO Format:
         >>> ## (currently defaults to pronot)
         >>> adapter = get_adapter('tests/input/go-nucleus.obo')
         >>> print(adapter.label("GO:0005634"))
         nucleus
```

### Comparing `oaklib-0.4.0/src/oaklib/utilities/apikey_manager.py` & `oaklib-0.4.1/src/oaklib/utilities/apikey_manager.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/associations/association_differ.py` & `oaklib-0.4.1/src/oaklib/utilities/associations/association_differ.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/associations/association_index.py` & `oaklib-0.4.1/src/oaklib/utilities/associations/association_index.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/basic_utils.py` & `oaklib-0.4.1/src/oaklib/utilities/basic_utils.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/graph/networkx_bridge.py` & `oaklib-0.4.1/src/oaklib/utilities/graph/networkx_bridge.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/graph/relationship_walker.py` & `oaklib-0.4.1/src/oaklib/utilities/graph/relationship_walker.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/identifier_utils.py` & `oaklib-0.4.1/src/oaklib/utilities/identifier_utils.py`

 * *Files 22% similar despite different names*

```diff
@@ -11,29 +11,29 @@
     :return:
     """
     return f"base64:{base64.b64encode(input.encode()).decode()}"
 
 
 def synonym_type_code_from_curie(curie: CURIE) -> str:
     """
-    Get the synonym type code from a CURIE
+    Get the synonym type packages from a CURIE
 
     In many OBO ontologies, the synonym type is encoded as a hash URI, which compacts
     to a curie of form
 
     - obo:chebi#BRAND_NAME
     - obo:hp#layperson
 
-    In these cases, the code is the part after the hash
+    In these cases, the packages is the part after the hash
 
     See:
 
     - https://github.com/information-artifact-ontology/ontology-metadata/issues/122
     - https://github.com/INCATools/ontology-access-kit/issues/385
 
     :param curie: represents synonym type
-    :return: code for the synonym type, or if cannot be determined, the input curie
+    :return: packages for the synonym type, or if cannot be determined, the input curie
     """
     if "#" in curie:
         return curie.split("#")[-1]
     else:
         return curie
```

### Comparing `oaklib-0.4.0/src/oaklib/utilities/iterator_utils.py` & `oaklib-0.4.1/src/oaklib/utilities/iterator_utils.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/kgcl_utilities.py` & `oaklib-0.4.1/src/oaklib/utilities/kgcl_utilities.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/label_utilities.py` & `oaklib-0.4.1/src/oaklib/utilities/label_utilities.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/lexical/lexical_indexer.py` & `oaklib-0.4.1/src/oaklib/utilities/lexical/lexical_indexer.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/mapping/boomer_utils.py` & `oaklib-0.4.1/src/oaklib/utilities/mapping/boomer_utils.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/mapping/cross_ontology_diffs.py` & `oaklib-0.4.1/src/oaklib/utilities/mapping/cross_ontology_diffs.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/mapping/mapping_propagator.py` & `oaklib-0.4.1/src/oaklib/utilities/mapping/mapping_propagator.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/mapping/mapping_validation.py` & `oaklib-0.4.1/src/oaklib/utilities/mapping/mapping_validation.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/mapping/sssom_utils.py` & `oaklib-0.4.1/src/oaklib/utilities/mapping/sssom_utils.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/ner_utilities.py` & `oaklib-0.4.1/src/oaklib/utilities/ner_utilities.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/nlp/natual_language_generation.py` & `oaklib-0.4.1/src/oaklib/utilities/nlp/natual_language_generation.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/obograph_utils.py` & `oaklib-0.4.1/src/oaklib/utilities/obograph_utils.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/ontology_builder.py` & `oaklib-0.4.1/src/oaklib/utilities/ontology_builder.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/reasoning/relation_graph.py` & `oaklib-0.4.1/src/oaklib/utilities/reasoning/relation_graph.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/semsim/similarity_utils.py` & `oaklib-0.4.1/src/oaklib/utilities/semsim/similarity_utils.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/stats/hypergeometric.py` & `oaklib-0.4.1/src/oaklib/utilities/stats/hypergeometric.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/subsets/slimmer_utils.py` & `oaklib-0.4.1/src/oaklib/utilities/subsets/slimmer_utils.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/subsets/subset_analysis.py` & `oaklib-0.4.1/src/oaklib/utilities/subsets/subset_analysis.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/subsets/value_set_expander.py` & `oaklib-0.4.1/src/oaklib/utilities/subsets/value_set_expander.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/table_filler.py` & `oaklib-0.4.1/src/oaklib/utilities/table_filler.py`

 * *Files 2% similar despite different names*

```diff
@@ -214,18 +214,18 @@
             r.get(pk) for r in rows if r.get(pk, None) is not None and r.get(dc, None) is None
         }
         dc_vals = {
             r.get(dc) for r in rows if r.get(dc, None) is not None and r.get(pk, None) is None
         }
         fwd_mapping = {}
         rev_mapping = {}
-        # Note to developers: it may be tempting to genericize the code below,
+        # Note to developers: it may be tempting to genericize the packages below,
         # but be very careful before doing this. Logic for different properties
         # may be subtly different, and over-genericizing may lead to overly
-        # abstract or less efficient code
+        # abstract or less efficient packages
         if rel == LABEL_KEY:
             if pk_vals:
                 for curie, label in oi.labels(list(pk_vals)):
                     fwd_mapping[curie] = label
             if dc_vals:
                 for v in dc_vals:
                     curies = oi.curies_by_label(v)
@@ -323,15 +323,15 @@
 
         The primary_key in the dependency is the slot that is designated the identifier
 
         Labels, definitions, etc are determined from the slot_ur
 
         For example, with the following schema
 
-        .. code-block ::
+        .. packages-block ::
 
             classes:
               Person:
                 attributes:
                   id:
                     identifier: true
                   name:
```

### Comparing `oaklib-0.4.0/src/oaklib/utilities/taxon/taxon_constraint_utils.py` & `oaklib-0.4.1/src/oaklib/utilities/taxon/taxon_constraint_utils.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/validation/definition_ontology_rule.py` & `oaklib-0.4.1/src/oaklib/utilities/validation/definition_ontology_rule.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/validation/disjointness_rule.py` & `oaklib-0.4.1/src/oaklib/utilities/validation/disjointness_rule.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/validation/lint_utils.py` & `oaklib-0.4.1/src/oaklib/utilities/validation/lint_utils.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/validation/ontology_rule.py` & `oaklib-0.4.1/src/oaklib/utilities/validation/ontology_rule.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/src/oaklib/utilities/validation/rule_runner.py` & `oaklib-0.4.1/src/oaklib/utilities/validation/rule_runner.py`

 * *Files identical despite different names*

### Comparing `oaklib-0.4.0/PKG-INFO` & `oaklib-0.4.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: oaklib
-Version: 0.4.0
+Version: 0.4.1
 Summary: Ontology Access Kit: Python library for common ontology operations over a variety of backends
 Author: cmungall
 Author-email: cjm@berkeleybop.org
 Requires-Python: >=3.9,<4.0.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -18,31 +18,31 @@
 Requires-Dist: appdirs (>=1.4.4,<2.0.0)
 Requires-Dist: bioregistry (>=0.6.35,<0.7.0)
 Requires-Dist: class-resolver (>=0.3.10,<0.4.0)
 Requires-Dist: curies (>=0.4.0,<0.5.0)
 Requires-Dist: funowl (>=0.1.12,<0.2.0)
 Requires-Dist: gilda (>=0.10.1,<0.11.0) ; extra == "gilda"
 Requires-Dist: kgcl-rdflib (>=0.3.0,<0.4.0)
-Requires-Dist: kgcl-schema (>=0.3.1,<0.4.0)
+Requires-Dist: kgcl-schema (>=0.3.5,<0.4.0)
 Requires-Dist: lark (>=1.1.2,<2.0.0)
 Requires-Dist: linkml-renderer (>=0.1.2,<0.2.0)
 Requires-Dist: linkml-runtime (>=1.2.15,<2.0.0)
 Requires-Dist: ndex2 (>=3.5.0,<4.0.0)
 Requires-Dist: networkx (>=2.7.1,<3.0.0)
 Requires-Dist: nxontology (>=0.4.0,<0.5.0)
 Requires-Dist: ols-client (>=0.1.1,<0.2.0)
 Requires-Dist: ontoportal-client (==0.0.3)
 Requires-Dist: pandas (>=1.5.1,<2.0.0)
 Requires-Dist: prefixmaps (>=0.1.2,<0.2.0)
 Requires-Dist: pronto (>=2.5.0,<3.0.0)
 Requires-Dist: pystow (>=0.5.0,<0.6.0)
 Requires-Dist: ratelimit (>=2.2.1,<3.0.0)
 Requires-Dist: semsql (>=0.3.1,<0.4.0)
-Requires-Dist: sssom (>=0.3.25,<0.4.0)
-Requires-Dist: sssom-schema (>=0.9.3,<0.10.0)
+Requires-Dist: sssom (>=0.3.26,<0.4.0)
+Requires-Dist: sssom-schema (>=0.11.0,<0.12.0)
 Description-Content-Type: text/markdown
 
 # Ontology Access Kit (OAK)
 
 Python lib for common ontology operations over a variety of backends.
 
 <img src="docs/logos/oak-logo_black-icon.png" width="20%">
```

