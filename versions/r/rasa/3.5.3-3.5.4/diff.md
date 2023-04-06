# Comparing `tmp/rasa-3.5.3.tar.gz` & `tmp/rasa-3.5.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rasa-3.5.3.tar", max compression
+gzip compressed data, was "rasa-3.5.4.tar", max compression
```

## Comparing `rasa-3.5.3.tar` & `rasa-3.5.4.tar`

### file list

```diff
@@ -1,315 +1,315 @@
--rw-r--r--   0        0        0    11352 2023-03-30 17:06:09.124909 rasa-3.5.3/LICENSE.txt
--rw-r--r--   0        0        0    20292 2023-03-30 17:06:09.124909 rasa-3.5.3/README.md
--rw-r--r--   0        0        0     8865 2023-03-30 17:06:09.308910 rasa-3.5.3/pyproject.toml
--rw-r--r--   0        0        0      280 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/__init__.py
--rw-r--r--   0        0        0     5188 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/__main__.py
--rw-r--r--   0        0        0     5314 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/api.py
--rw-r--r--   0        0        0      115 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/__init__.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/__init__.py
--rw-r--r--   0        0        0     2388 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/data.py
--rw-r--r--   0        0        0     5242 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/default_arguments.py
--rw-r--r--   0        0        0     2199 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/evaluate.py
--rw-r--r--   0        0        0     1499 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/export.py
--rw-r--r--   0        0        0     2685 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/interactive.py
--rw-r--r--   0        0        0     5674 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/run.py
--rw-r--r--   0        0        0      367 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/shell.py
--rw-r--r--   0        0        0     6853 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/test.py
--rw-r--r--   0        0        0     7355 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/train.py
--rw-r--r--   0        0        0      861 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/visualize.py
--rw-r--r--   0        0        0     1027 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/arguments/x.py
--rw-r--r--   0        0        0     8906 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/data.py
--rw-r--r--   0        0        0     7948 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/evaluate.py
--rw-r--r--   0        0        0     8204 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/export.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/initial_project/actions/__init__.py
--rw-r--r--   0        0        0      742 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/initial_project/actions/actions.py
--rw-r--r--   0        0        0     1505 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/initial_project/config.yml
--rw-r--r--   0        0        0      998 2023-03-30 17:06:09.308910 rasa-3.5.3/rasa/cli/initial_project/credentials.yml
--rw-r--r--   0        0        0     1433 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/initial_project/data/nlu.yml
--rw-r--r--   0        0        0      244 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/initial_project/data/rules.yml
--rw-r--r--   0        0        0      542 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/initial_project/data/stories.yml
--rw-r--r--   0        0        0      565 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/initial_project/domain.yml
--rw-r--r--   0        0        0     1411 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/initial_project/endpoints.yml
--rw-r--r--   0        0        0     1664 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/initial_project/tests/test_stories.yml
--rw-r--r--   0        0        0     5827 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/interactive.py
--rw-r--r--   0        0        0     4196 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/run.py
--rw-r--r--   0        0        0     6846 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/scaffold.py
--rw-r--r--   0        0        0     4264 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/shell.py
--rw-r--r--   0        0        0     3118 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/telemetry.py
--rw-r--r--   0        0        0     8888 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/test.py
--rw-r--r--   0        0        0     6871 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/train.py
--rw-r--r--   0        0        0     9628 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/utils.py
--rw-r--r--   0        0        0     1256 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/visualize.py
--rw-r--r--   0        0        0     6785 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/cli/x.py
--rw-r--r--   0        0        0     1172 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/constants.py
--rw-r--r--   0        0        0      123 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/__init__.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/actions/__init__.py
--rw-r--r--   0        0        0    45583 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/actions/action.py
--rw-r--r--   0        0        0       78 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/actions/constants.py
--rw-r--r--   0        0        0    25982 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/actions/forms.py
--rw-r--r--   0        0        0     3322 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/actions/loops.py
--rw-r--r--   0        0        0     6078 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/actions/two_stage_fallback.py
--rw-r--r--   0        0        0    20366 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/agent.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/brokers/__init__.py
--rw-r--r--   0        0        0     4398 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/brokers/broker.py
--rw-r--r--   0        0        0     1801 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/brokers/file.py
--rw-r--r--   0        0        0    11397 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/brokers/kafka.py
--rw-r--r--   0        0        0    13495 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/brokers/pika.py
--rw-r--r--   0        0        0     2754 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/brokers/sql.py
--rw-r--r--   0        0        0     1656 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/__init__.py
--rw-r--r--   0        0        0    11686 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/botframework.py
--rw-r--r--   0        0        0     2746 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/callback.py
--rw-r--r--   0        0        0    13331 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/channel.py
--rw-r--r--   0        0        0     8073 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/console.py
--rw-r--r--   0        0        0    15789 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/facebook.py
--rw-r--r--   0        0        0    11532 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/hangouts.py
--rw-r--r--   0        0        0     7743 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/mattermost.py
--rw-r--r--   0        0        0     4814 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/rasa_chat.py
--rw-r--r--   0        0        0     6937 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/rest.py
--rw-r--r--   0        0        0     5999 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/rocketchat.py
--rw-r--r--   0        0        0    24359 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/slack.py
--rw-r--r--   0        0        0    10163 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/socketio.py
--rw-r--r--   0        0        0    10630 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/telegram.py
--rw-r--r--   0        0        0     5389 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/twilio.py
--rw-r--r--   0        0        0    13181 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/twilio_voice.py
--rw-r--r--   0        0        0     4845 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/channels/webexteams.py
--rw-r--r--   0        0        0     3047 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/constants.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/evaluation/__init__.py
--rw-r--r--   0        0        0     9154 2023-03-30 17:06:09.312910 rasa-3.5.3/rasa/core/evaluation/marker.py
--rw-r--r--   0        0        0    36811 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/evaluation/marker_base.py
--rw-r--r--   0        0        0    12086 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/evaluation/marker_stats.py
--rw-r--r--   0        0        0     3658 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/evaluation/marker_tracker_loader.py
--rw-r--r--   0        0        0      901 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/exceptions.py
--rw-r--r--   0        0        0    10220 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/exporter.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/featurizers/__init__.py
--rw-r--r--   0        0        0    17964 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/featurizers/precomputation.py
--rw-r--r--   0        0        0    15447 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/featurizers/single_state_featurizer.py
--rw-r--r--   0        0        0    43363 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/featurizers/tracker_featurizers.py
--rw-r--r--   0        0        0     2906 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/http_interpreter.py
--rw-r--r--   0        0        0     2018 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/jobs.py
--rw-r--r--   0        0        0     4719 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/lock.py
--rw-r--r--   0        0        0    11678 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/lock_store.py
--rw-r--r--   0        0        0    14821 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/migrate.py
--rw-r--r--   0        0        0      240 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/nlg/__init__.py
--rw-r--r--   0        0        0     3745 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/nlg/callback.py
--rw-r--r--   0        0        0     3285 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/nlg/generator.py
--rw-r--r--   0        0        0     2794 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/nlg/interpolator.py
--rw-r--r--   0        0        0     7503 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/nlg/response.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/policies/__init__.py
--rw-r--r--   0        0        0    12959 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/policies/ensemble.py
--rw-r--r--   0        0        0    19062 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/policies/memoization.py
--rw-r--r--   0        0        0    25038 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/policies/policy.py
--rw-r--r--   0        0        0    50189 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/policies/rule_policy.py
--rw-r--r--   0        0        0    86521 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/policies/ted_policy.py
--rw-r--r--   0        0        0    39329 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/policies/unexpected_intent_policy.py
--rw-r--r--   0        0        0    39091 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/processor.py
--rw-r--r--   0        0        0     9150 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/run.py
--rw-r--r--   0        0        0    48935 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/test.py
--rw-r--r--   0        0        0    58214 2023-03-30 17:06:09.316910 rasa-3.5.3/rasa/core/tracker_store.py
--rw-r--r--   0        0        0     3543 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/core/train.py
--rw-r--r--   0        0        0     3218 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/core/training/__init__.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/core/training/converters/__init__.py
--rw-r--r--   0        0        0     3889 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/core/training/converters/responses_prefix_converter.py
--rw-r--r--   0        0        0    59595 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/core/training/interactive.py
--rw-r--r--   0        0        0    13604 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/core/training/story_conflict.py
--rw-r--r--   0        0        0     3067 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/core/training/training.py
--rw-r--r--   0        0        0    10782 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/core/utils.py
--rw-r--r--   0        0        0     2125 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/core/visualize.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/__init__.py
--rw-r--r--   0        0        0    16744 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/caching.py
--rw-r--r--   0        0        0      469 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/constants.py
--rw-r--r--   0        0        0      437 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/exceptions.py
--rw-r--r--   0        0        0    22059 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/graph.py
--rw-r--r--   0        0        0     1384 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/loader.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/recipes/__init__.py
--rw-r--r--   0        0        0     1139 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/recipes/config_files/default_config.yml
--rw-r--r--   0        0        0     3244 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/recipes/default_components.py
--rw-r--r--   0        0        0    42860 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/recipes/default_recipe.py
--rw-r--r--   0        0        0     3260 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/recipes/graph_recipe.py
--rw-r--r--   0        0        0     3354 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/recipes/recipe.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/runner/__init__.py
--rw-r--r--   0        0        0     4302 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/runner/dask.py
--rw-r--r--   0        0        0     1672 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/runner/interface.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/storage/__init__.py
--rw-r--r--   0        0        0     9534 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/storage/local_model_storage.py
--rw-r--r--   0        0        0     3931 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/storage/resource.py
--rw-r--r--   0        0        0     6739 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/storage/storage.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/training/__init__.py
--rw-r--r--   0        0        0     6524 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/training/components.py
--rw-r--r--   0        0        0     1848 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/training/fingerprinting.py
--rw-r--r--   0        0        0    10516 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/training/graph_trainer.py
--rw-r--r--   0        0        0     5036 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/training/hooks.py
--rw-r--r--   0        0        0    22639 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/engine/validation.py
--rw-r--r--   0        0        0     2132 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/exceptions.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/__init__.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/converters/__init__.py
--rw-r--r--   0        0        0     1576 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/converters/nlu_message_converter.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/providers/__init__.py
--rw-r--r--   0        0        0     3832 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/providers/domain_for_core_training_provider.py
--rw-r--r--   0        0        0     2571 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/providers/domain_provider.py
--rw-r--r--   0        0        0     1294 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/providers/forms_provider.py
--rw-r--r--   0        0        0     2119 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/providers/nlu_training_data_provider.py
--rw-r--r--   0        0        0     1354 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/providers/responses_provider.py
--rw-r--r--   0        0        0     1540 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/providers/rule_only_provider.py
--rw-r--r--   0        0        0     1466 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/providers/story_graph_provider.py
--rw-r--r--   0        0        0     1965 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/providers/training_tracker_provider.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/validators/__init__.py
--rw-r--r--   0        0        0    22668 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/validators/default_recipe_validator.py
--rw-r--r--   0        0        0    12863 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/graph_components/validators/finetuning_validator.py
--rw-r--r--   0        0        0     1782 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/jupyter.py
--rw-r--r--   0        0        0      101 2023-03-30 17:06:29.044972 rasa-3.5.3/rasa/keys
--rw-r--r--   0        0        0     3490 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/model.py
--rw-r--r--   0        0        0    14961 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/model_testing.py
--rw-r--r--   0        0        0    16760 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/model_training.py
--rw-r--r--   0        0        0      123 2023-03-30 17:06:09.320910 rasa-3.5.3/rasa/nlu/__init__.py
--rw-r--r--   0        0        0      118 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/classifiers/__init__.py
--rw-r--r--   0        0        0      133 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/classifiers/classifier.py
--rw-r--r--   0        0        0    71640 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/classifiers/diet_classifier.py
--rw-r--r--   0        0        0     7150 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/classifiers/fallback_classifier.py
--rw-r--r--   0        0        0     7581 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/classifiers/keyword_intent_classifier.py
--rw-r--r--   0        0        0     7568 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/classifiers/logistic_regression_classifier.py
--rw-r--r--   0        0        0     5559 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/classifiers/mitie_intent_classifier.py
--rw-r--r--   0        0        0     1989 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/classifiers/regex_message_handler.py
--rw-r--r--   0        0        0    11915 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/classifiers/sklearn_intent_classifier.py
--rw-r--r--   0        0        0     2757 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/constants.py
--rw-r--r--   0        0        0     1317 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/convert.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/emulators/__init__.py
--rw-r--r--   0        0        0     1748 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/emulators/dialogflow.py
--rw-r--r--   0        0        0     1367 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/emulators/emulator.py
--rw-r--r--   0        0        0     3032 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/emulators/luis.py
--rw-r--r--   0        0        0      334 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/emulators/no_emulator.py
--rw-r--r--   0        0        0     1930 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/emulators/wit.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/extractors/__init__.py
--rw-r--r--   0        0        0    26499 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/extractors/crf_entity_extractor.py
--rw-r--r--   0        0        0     7685 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/extractors/duckling_entity_extractor.py
--rw-r--r--   0        0        0     7160 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/extractors/entity_synonyms.py
--rw-r--r--   0        0        0    17530 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/extractors/extractor.py
--rw-r--r--   0        0        0    10973 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/extractors/mitie_entity_extractor.py
--rw-r--r--   0        0        0     8289 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/extractors/regex_entity_extractor.py
--rw-r--r--   0        0        0     3366 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/extractors/spacy_entity_extractor.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/__init__.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/dense_featurizer/__init__.py
--rw-r--r--   0        0        0    17142 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/dense_featurizer/convert_featurizer.py
--rw-r--r--   0        0        0     2433 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/dense_featurizer/dense_featurizer.py
--rw-r--r--   0        0        0    30361 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/dense_featurizer/lm_featurizer.py
--rw-r--r--   0        0        0     5861 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/dense_featurizer/mitie_featurizer.py
--rw-r--r--   0        0        0     4888 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/dense_featurizer/spacy_featurizer.py
--rw-r--r--   0        0        0     3347 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/featurizer.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/sparse_featurizer/__init__.py
--rw-r--r--   0        0        0    33295 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/sparse_featurizer/count_vectors_featurizer.py
--rw-r--r--   0        0        0    21810 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/sparse_featurizer/lexical_syntactic_featurizer.py
--rw-r--r--   0        0        0    10289 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/sparse_featurizer/regex_featurizer.py
--rw-r--r--   0        0        0      220 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/featurizers/sparse_featurizer/sparse_featurizer.py
--rw-r--r--   0        0        0      557 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/model.py
--rw-r--r--   0        0        0     8333 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/persistor.py
--rw-r--r--   0        0        0      803 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/run.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/selectors/__init__.py
--rw-r--r--   0        0        0    39012 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/selectors/response_selector.py
--rw-r--r--   0        0        0    66681 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/test.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/tokenizers/__init__.py
--rw-r--r--   0        0        0     5276 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/tokenizers/jieba_tokenizer.py
--rw-r--r--   0        0        0     2520 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/tokenizers/mitie_tokenizer.py
--rw-r--r--   0        0        0     2280 2023-03-30 17:06:09.324910 rasa-3.5.3/rasa/nlu/tokenizers/spacy_tokenizer.py
--rw-r--r--   0        0        0     7655 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/nlu/tokenizers/tokenizer.py
--rw-r--r--   0        0        0     3652 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/nlu/tokenizers/whitespace_tokenizer.py
--rw-r--r--   0        0        0      928 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/nlu/utils/__init__.py
--rw-r--r--   0        0        0    14703 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/nlu/utils/bilou_utils.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/nlu/utils/hugging_face/__init__.py
--rw-r--r--   0        0        0     3380 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/nlu/utils/hugging_face/registry.py
--rw-r--r--   0        0        0     9143 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/nlu/utils/hugging_face/transformers_pre_post_processors.py
--rw-r--r--   0        0        0     3887 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/nlu/utils/mitie_utils.py
--rw-r--r--   0        0        0     5386 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/nlu/utils/pattern_utils.py
--rw-r--r--   0        0        0    11795 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/nlu/utils/spacy_utils.py
--rw-r--r--   0        0        0     2248 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/plugin.py
--rw-r--r--   0        0        0    55474 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/server.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/__init__.py
--rw-r--r--   0        0        0     4294 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/constants.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/__init__.py
--rw-r--r--   0        0        0     4346 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/constants.py
--rw-r--r--   0        0        0     1366 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/conversation.py
--rw-r--r--   0        0        0    75018 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/domain.py
--rw-r--r--   0        0        0    65833 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/events.py
--rw-r--r--   0        0        0    35597 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/generator.py
--rw-r--r--   0        0        0     8130 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/slot_mappings.py
--rw-r--r--   0        0        0    16371 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/slots.py
--rw-r--r--   0        0        0    33176 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/trackers.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/__init__.py
--rw-r--r--   0        0        0     2895 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/loading.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/story_reader/__init__.py
--rw-r--r--   0        0        0     4449 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/story_reader/story_reader.py
--rw-r--r--   0        0        0     6671 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/story_reader/story_step_builder.py
--rw-r--r--   0        0        0    32873 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/story_reader/yaml_story_reader.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/story_writer/__init__.py
--rw-r--r--   0        0        0     2543 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/story_writer/story_writer.py
--rw-r--r--   0        0        0    14903 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/story_writer/yaml_story_writer.py
--rw-r--r--   0        0        0    29313 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/structures.py
--rw-r--r--   0        0        0     3500 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/visualization.html
--rw-r--r--   0        0        0    20341 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/core/training_data/visualization.py
--rw-r--r--   0        0        0     5479 2023-03-30 17:06:09.328910 rasa-3.5.3/rasa/shared/data.py
--rw-r--r--   0        0        0     3633 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/exceptions.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/importers/__init__.py
--rw-r--r--   0        0        0    21555 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/importers/importer.py
--rw-r--r--   0        0        0     7836 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/importers/multi_project.py
--rw-r--r--   0        0        0     3388 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/importers/rasa.py
--rw-r--r--   0        0        0      861 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/importers/utils.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/__init__.py
--rw-r--r--   0        0        0     1388 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/constants.py
--rw-r--r--   0        0        0      188 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/interpreter.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/__init__.py
--rw-r--r--   0        0        0     6759 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/entities_parser.py
--rw-r--r--   0        0        0    14835 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/features.py
--rw-r--r--   0        0        0      453 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/formats/__init__.py
--rw-r--r--   0        0        0     6123 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/formats/dialogflow.py
--rw-r--r--   0        0        0     3014 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/formats/luis.py
--rw-r--r--   0        0        0     4495 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/formats/rasa.py
--rw-r--r--   0        0        0    22353 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/formats/rasa_yaml.py
--rw-r--r--   0        0        0     8540 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/formats/readerwriter.py
--rw-r--r--   0        0        0     1820 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/formats/wit.py
--rw-r--r--   0        0        0     4258 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/loading.py
--rw-r--r--   0        0        0     1116 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/lookup_tables_parser.py
--rw-r--r--   0        0        0    16662 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/message.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/schemas/__init__.py
--rw-r--r--   0        0        0     2565 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/schemas/data_schema.py
--rw-r--r--   0        0        0     1179 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/schemas/nlu.yml
--rw-r--r--   0        0        0     1595 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/schemas/responses.yml
--rw-r--r--   0        0        0     1476 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/synonyms_parser.py
--rw-r--r--   0        0        0    28493 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/training_data.py
--rw-r--r--   0        0        0     7040 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/nlu/training_data/util.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/__init__.py
--rw-r--r--   0        0        0     1129 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/cli.py
--rw-r--r--   0        0        0     8731 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/common.py
--rw-r--r--   0        0        0    19456 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/io.py
--rw-r--r--   0        0        0      883 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/pykwalify_extensions.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/schemas/__init__.py
--rw-r--r--   0        0        0       27 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/schemas/config.yml
--rw-r--r--   0        0        0     3267 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/schemas/domain.yml
--rw-r--r--   0        0        0     5569 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/schemas/events.py
--rw-r--r--   0        0        0      779 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/schemas/model_config.yml
--rw-r--r--   0        0        0     4034 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/schemas/stories.yml
--rw-r--r--   0        0        0    10178 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/shared/utils/validation.py
--rw-r--r--   0        0        0    36084 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/telemetry.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/__init__.py
--rw-r--r--   0        0        0    19852 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/common.py
--rw-r--r--   0        0        0     1647 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/converter.py
--rw-r--r--   0        0        0     8796 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/endpoints.py
--rw-r--r--   0        0        0     7831 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/io.py
--rw-r--r--   0        0        0    12246 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/plotting.py
--rw-r--r--   0        0        0        0 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/tensorflow/__init__.py
--rw-r--r--   0        0        0     4036 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/tensorflow/callback.py
--rw-r--r--   0        0        0     3140 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/tensorflow/constants.py
--rw-r--r--   0        0        0     9020 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/tensorflow/crf.py
--rw-r--r--   0        0        0    15526 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/tensorflow/data_generator.py
--rw-r--r--   0        0        0     5576 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/tensorflow/environment.py
--rw-r--r--   0        0        0      168 2023-03-30 17:06:09.332910 rasa-3.5.3/rasa/utils/tensorflow/exceptions.py
--rw-r--r--   0        0        0    59313 2023-03-30 17:06:09.336910 rasa-3.5.3/rasa/utils/tensorflow/layers.py
--rw-r--r--   0        0        0     3319 2023-03-30 17:06:09.336910 rasa-3.5.3/rasa/utils/tensorflow/layers_utils.py
--rw-r--r--   0        0        0    34572 2023-03-30 17:06:09.336910 rasa-3.5.3/rasa/utils/tensorflow/model_data.py
--rw-r--r--   0        0        0    18667 2023-03-30 17:06:09.336910 rasa-3.5.3/rasa/utils/tensorflow/model_data_utils.py
--rw-r--r--   0        0        0    36004 2023-03-30 17:06:09.336910 rasa-3.5.3/rasa/utils/tensorflow/models.py
--rw-r--r--   0        0        0    49066 2023-03-30 17:06:09.336910 rasa-3.5.3/rasa/utils/tensorflow/rasa_layers.py
--rw-r--r--   0        0        0    25509 2023-03-30 17:06:09.336910 rasa-3.5.3/rasa/utils/tensorflow/transformer.py
--rw-r--r--   0        0        0      204 2023-03-30 17:06:09.336910 rasa-3.5.3/rasa/utils/tensorflow/types.py
--rw-r--r--   0        0        0    20984 2023-03-30 17:06:09.336910 rasa-3.5.3/rasa/utils/train_utils.py
--rw-r--r--   0        0        0    17708 2023-03-30 17:06:09.336910 rasa-3.5.3/rasa/validator.py
--rw-r--r--   0        0        0      116 2023-03-30 17:06:09.336910 rasa-3.5.3/rasa/version.py
--rw-r--r--   0        0        0    27172 1970-01-01 00:00:00.000000 rasa-3.5.3/setup.py
--rw-r--r--   0        0        0    26346 1970-01-01 00:00:00.000000 rasa-3.5.3/PKG-INFO
+-rw-r--r--   0        0        0    11352 2023-04-05 14:19:12.706149 rasa-3.5.4/LICENSE.txt
+-rw-r--r--   0        0        0    20292 2023-04-05 14:19:12.706149 rasa-3.5.4/README.md
+-rw-r--r--   0        0        0     8910 2023-04-05 14:19:12.886150 rasa-3.5.4/pyproject.toml
+-rw-r--r--   0        0        0      280 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/__init__.py
+-rw-r--r--   0        0        0     5188 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/__main__.py
+-rw-r--r--   0        0        0     5314 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/api.py
+-rw-r--r--   0        0        0      115 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/__init__.py
+-rw-r--r--   0        0        0     2388 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/data.py
+-rw-r--r--   0        0        0     5242 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/default_arguments.py
+-rw-r--r--   0        0        0     2199 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/evaluate.py
+-rw-r--r--   0        0        0     1499 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/export.py
+-rw-r--r--   0        0        0     2685 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/interactive.py
+-rw-r--r--   0        0        0     5674 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/run.py
+-rw-r--r--   0        0        0      367 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/shell.py
+-rw-r--r--   0        0        0     6853 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/test.py
+-rw-r--r--   0        0        0     7355 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/train.py
+-rw-r--r--   0        0        0      861 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/visualize.py
+-rw-r--r--   0        0        0     1027 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/arguments/x.py
+-rw-r--r--   0        0        0     8906 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/data.py
+-rw-r--r--   0        0        0     7948 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/evaluate.py
+-rw-r--r--   0        0        0     8204 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/export.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/initial_project/actions/__init__.py
+-rw-r--r--   0        0        0      742 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/initial_project/actions/actions.py
+-rw-r--r--   0        0        0     1505 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/initial_project/config.yml
+-rw-r--r--   0        0        0      998 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/initial_project/credentials.yml
+-rw-r--r--   0        0        0     1433 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/initial_project/data/nlu.yml
+-rw-r--r--   0        0        0      244 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/initial_project/data/rules.yml
+-rw-r--r--   0        0        0      542 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/initial_project/data/stories.yml
+-rw-r--r--   0        0        0      565 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/initial_project/domain.yml
+-rw-r--r--   0        0        0     1411 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/initial_project/endpoints.yml
+-rw-r--r--   0        0        0     1664 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/initial_project/tests/test_stories.yml
+-rw-r--r--   0        0        0     5827 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/interactive.py
+-rw-r--r--   0        0        0     4196 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/run.py
+-rw-r--r--   0        0        0     6846 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/scaffold.py
+-rw-r--r--   0        0        0     4264 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/shell.py
+-rw-r--r--   0        0        0     3118 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/telemetry.py
+-rw-r--r--   0        0        0     8888 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/test.py
+-rw-r--r--   0        0        0     6871 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/train.py
+-rw-r--r--   0        0        0     9628 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/utils.py
+-rw-r--r--   0        0        0     1256 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/visualize.py
+-rw-r--r--   0        0        0     6785 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/cli/x.py
+-rw-r--r--   0        0        0     1172 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/constants.py
+-rw-r--r--   0        0        0      123 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/actions/__init__.py
+-rw-r--r--   0        0        0    45583 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/actions/action.py
+-rw-r--r--   0        0        0       78 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/actions/constants.py
+-rw-r--r--   0        0        0    25982 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/actions/forms.py
+-rw-r--r--   0        0        0     3322 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/actions/loops.py
+-rw-r--r--   0        0        0     6078 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/actions/two_stage_fallback.py
+-rw-r--r--   0        0        0    20361 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/agent.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/brokers/__init__.py
+-rw-r--r--   0        0        0     4398 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/brokers/broker.py
+-rw-r--r--   0        0        0     1801 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/brokers/file.py
+-rw-r--r--   0        0        0    11397 2023-04-05 14:19:12.886150 rasa-3.5.4/rasa/core/brokers/kafka.py
+-rw-r--r--   0        0        0    13495 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/brokers/pika.py
+-rw-r--r--   0        0        0     2754 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/brokers/sql.py
+-rw-r--r--   0        0        0     1656 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/__init__.py
+-rw-r--r--   0        0        0    11686 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/botframework.py
+-rw-r--r--   0        0        0     2746 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/callback.py
+-rw-r--r--   0        0        0    13331 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/channel.py
+-rw-r--r--   0        0        0     8073 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/console.py
+-rw-r--r--   0        0        0    15789 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/facebook.py
+-rw-r--r--   0        0        0    11532 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/hangouts.py
+-rw-r--r--   0        0        0     7743 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/mattermost.py
+-rw-r--r--   0        0        0     4814 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/rasa_chat.py
+-rw-r--r--   0        0        0     6937 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/rest.py
+-rw-r--r--   0        0        0     5999 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/rocketchat.py
+-rw-r--r--   0        0        0    24359 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/slack.py
+-rw-r--r--   0        0        0    10163 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/socketio.py
+-rw-r--r--   0        0        0    10630 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/telegram.py
+-rw-r--r--   0        0        0     5389 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/twilio.py
+-rw-r--r--   0        0        0    13181 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/twilio_voice.py
+-rw-r--r--   0        0        0     4845 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/channels/webexteams.py
+-rw-r--r--   0        0        0     3047 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/constants.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/evaluation/__init__.py
+-rw-r--r--   0        0        0     9154 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/evaluation/marker.py
+-rw-r--r--   0        0        0    36811 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/evaluation/marker_base.py
+-rw-r--r--   0        0        0    12086 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/evaluation/marker_stats.py
+-rw-r--r--   0        0        0     3658 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/evaluation/marker_tracker_loader.py
+-rw-r--r--   0        0        0      901 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/exceptions.py
+-rw-r--r--   0        0        0    10220 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/exporter.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/featurizers/__init__.py
+-rw-r--r--   0        0        0    17964 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/featurizers/precomputation.py
+-rw-r--r--   0        0        0    15447 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/featurizers/single_state_featurizer.py
+-rw-r--r--   0        0        0    43363 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/featurizers/tracker_featurizers.py
+-rw-r--r--   0        0        0     2906 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/http_interpreter.py
+-rw-r--r--   0        0        0     2018 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/jobs.py
+-rw-r--r--   0        0        0     4719 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/lock.py
+-rw-r--r--   0        0        0    11678 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/lock_store.py
+-rw-r--r--   0        0        0    14821 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/migrate.py
+-rw-r--r--   0        0        0      240 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/nlg/__init__.py
+-rw-r--r--   0        0        0     3745 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/nlg/callback.py
+-rw-r--r--   0        0        0     3285 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/nlg/generator.py
+-rw-r--r--   0        0        0     2794 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/nlg/interpolator.py
+-rw-r--r--   0        0        0     7503 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/nlg/response.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/policies/__init__.py
+-rw-r--r--   0        0        0    12959 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/policies/ensemble.py
+-rw-r--r--   0        0        0    19062 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/policies/memoization.py
+-rw-r--r--   0        0        0    25038 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/policies/policy.py
+-rw-r--r--   0        0        0    50189 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/policies/rule_policy.py
+-rw-r--r--   0        0        0    86521 2023-04-05 14:19:12.890149 rasa-3.5.4/rasa/core/policies/ted_policy.py
+-rw-r--r--   0        0        0    39329 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/policies/unexpected_intent_policy.py
+-rw-r--r--   0        0        0    39091 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/processor.py
+-rw-r--r--   0        0        0     9150 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/run.py
+-rw-r--r--   0        0        0    48935 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/test.py
+-rw-r--r--   0        0        0    58298 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/tracker_store.py
+-rw-r--r--   0        0        0     3543 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/train.py
+-rw-r--r--   0        0        0     3218 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/training/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/training/converters/__init__.py
+-rw-r--r--   0        0        0     3889 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/training/converters/responses_prefix_converter.py
+-rw-r--r--   0        0        0    59595 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/training/interactive.py
+-rw-r--r--   0        0        0    13604 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/training/story_conflict.py
+-rw-r--r--   0        0        0     3067 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/training/training.py
+-rw-r--r--   0        0        0    10782 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/utils.py
+-rw-r--r--   0        0        0     2125 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/core/visualize.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/__init__.py
+-rw-r--r--   0        0        0    16744 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/caching.py
+-rw-r--r--   0        0        0      469 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/constants.py
+-rw-r--r--   0        0        0      437 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/exceptions.py
+-rw-r--r--   0        0        0    22059 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/graph.py
+-rw-r--r--   0        0        0     1384 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/loader.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/recipes/__init__.py
+-rw-r--r--   0        0        0     1139 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/recipes/config_files/default_config.yml
+-rw-r--r--   0        0        0     3244 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/recipes/default_components.py
+-rw-r--r--   0        0        0    42860 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/recipes/default_recipe.py
+-rw-r--r--   0        0        0     3260 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/recipes/graph_recipe.py
+-rw-r--r--   0        0        0     3354 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/recipes/recipe.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/runner/__init__.py
+-rw-r--r--   0        0        0     4302 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/runner/dask.py
+-rw-r--r--   0        0        0     1672 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/runner/interface.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/storage/__init__.py
+-rw-r--r--   0        0        0     9534 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/storage/local_model_storage.py
+-rw-r--r--   0        0        0     3931 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/storage/resource.py
+-rw-r--r--   0        0        0     6739 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/storage/storage.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/training/__init__.py
+-rw-r--r--   0        0        0     6524 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/training/components.py
+-rw-r--r--   0        0        0     1848 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/training/fingerprinting.py
+-rw-r--r--   0        0        0    10516 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/training/graph_trainer.py
+-rw-r--r--   0        0        0     5036 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/training/hooks.py
+-rw-r--r--   0        0        0    22639 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/engine/validation.py
+-rw-r--r--   0        0        0     2132 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/exceptions.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/converters/__init__.py
+-rw-r--r--   0        0        0     1576 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/converters/nlu_message_converter.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/providers/__init__.py
+-rw-r--r--   0        0        0     3832 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/providers/domain_for_core_training_provider.py
+-rw-r--r--   0        0        0     2571 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/providers/domain_provider.py
+-rw-r--r--   0        0        0     1294 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/providers/forms_provider.py
+-rw-r--r--   0        0        0     2119 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/providers/nlu_training_data_provider.py
+-rw-r--r--   0        0        0     1354 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/providers/responses_provider.py
+-rw-r--r--   0        0        0     1540 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/providers/rule_only_provider.py
+-rw-r--r--   0        0        0     1466 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/providers/story_graph_provider.py
+-rw-r--r--   0        0        0     1965 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/providers/training_tracker_provider.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/validators/__init__.py
+-rw-r--r--   0        0        0    22668 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/validators/default_recipe_validator.py
+-rw-r--r--   0        0        0    12863 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/graph_components/validators/finetuning_validator.py
+-rw-r--r--   0        0        0     1782 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/jupyter.py
+-rw-r--r--   0        0        0      101 2023-04-05 14:19:30.754159 rasa-3.5.4/rasa/keys
+-rw-r--r--   0        0        0     3490 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/model.py
+-rw-r--r--   0        0        0    14961 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/model_testing.py
+-rw-r--r--   0        0        0    16760 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/model_training.py
+-rw-r--r--   0        0        0      123 2023-04-05 14:19:12.894149 rasa-3.5.4/rasa/nlu/__init__.py
+-rw-r--r--   0        0        0      118 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/classifiers/__init__.py
+-rw-r--r--   0        0        0      133 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/classifiers/classifier.py
+-rw-r--r--   0        0        0    71640 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/classifiers/diet_classifier.py
+-rw-r--r--   0        0        0     7150 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/classifiers/fallback_classifier.py
+-rw-r--r--   0        0        0     7581 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/classifiers/keyword_intent_classifier.py
+-rw-r--r--   0        0        0     7568 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/classifiers/logistic_regression_classifier.py
+-rw-r--r--   0        0        0     5559 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/classifiers/mitie_intent_classifier.py
+-rw-r--r--   0        0        0     1989 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/classifiers/regex_message_handler.py
+-rw-r--r--   0        0        0    11915 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/classifiers/sklearn_intent_classifier.py
+-rw-r--r--   0        0        0     2757 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/constants.py
+-rw-r--r--   0        0        0     1317 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/convert.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/emulators/__init__.py
+-rw-r--r--   0        0        0     1748 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/emulators/dialogflow.py
+-rw-r--r--   0        0        0     1367 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/emulators/emulator.py
+-rw-r--r--   0        0        0     3032 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/emulators/luis.py
+-rw-r--r--   0        0        0      334 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/emulators/no_emulator.py
+-rw-r--r--   0        0        0     1930 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/emulators/wit.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/extractors/__init__.py
+-rw-r--r--   0        0        0    26499 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/extractors/crf_entity_extractor.py
+-rw-r--r--   0        0        0     7685 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/extractors/duckling_entity_extractor.py
+-rw-r--r--   0        0        0     7160 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/extractors/entity_synonyms.py
+-rw-r--r--   0        0        0    17530 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/extractors/extractor.py
+-rw-r--r--   0        0        0    10973 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/extractors/mitie_entity_extractor.py
+-rw-r--r--   0        0        0     8289 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/extractors/regex_entity_extractor.py
+-rw-r--r--   0        0        0     3366 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/extractors/spacy_entity_extractor.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/dense_featurizer/__init__.py
+-rw-r--r--   0        0        0    17142 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/dense_featurizer/convert_featurizer.py
+-rw-r--r--   0        0        0     2433 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/dense_featurizer/dense_featurizer.py
+-rw-r--r--   0        0        0    30361 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/dense_featurizer/lm_featurizer.py
+-rw-r--r--   0        0        0     5861 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/dense_featurizer/mitie_featurizer.py
+-rw-r--r--   0        0        0     4888 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/dense_featurizer/spacy_featurizer.py
+-rw-r--r--   0        0        0     3347 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/featurizer.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/sparse_featurizer/__init__.py
+-rw-r--r--   0        0        0    33295 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/sparse_featurizer/count_vectors_featurizer.py
+-rw-r--r--   0        0        0    21810 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/sparse_featurizer/lexical_syntactic_featurizer.py
+-rw-r--r--   0        0        0    10289 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/sparse_featurizer/regex_featurizer.py
+-rw-r--r--   0        0        0      220 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/featurizers/sparse_featurizer/sparse_featurizer.py
+-rw-r--r--   0        0        0      557 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/model.py
+-rw-r--r--   0        0        0     8333 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/persistor.py
+-rw-r--r--   0        0        0      803 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/run.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/selectors/__init__.py
+-rw-r--r--   0        0        0    39012 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/selectors/response_selector.py
+-rw-r--r--   0        0        0    66681 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/test.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/tokenizers/__init__.py
+-rw-r--r--   0        0        0     5276 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/tokenizers/jieba_tokenizer.py
+-rw-r--r--   0        0        0     2520 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/tokenizers/mitie_tokenizer.py
+-rw-r--r--   0        0        0     2280 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/tokenizers/spacy_tokenizer.py
+-rw-r--r--   0        0        0     7655 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/tokenizers/tokenizer.py
+-rw-r--r--   0        0        0     3652 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/tokenizers/whitespace_tokenizer.py
+-rw-r--r--   0        0        0      928 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/utils/__init__.py
+-rw-r--r--   0        0        0    14703 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/utils/bilou_utils.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.898149 rasa-3.5.4/rasa/nlu/utils/hugging_face/__init__.py
+-rw-r--r--   0        0        0     3380 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/nlu/utils/hugging_face/registry.py
+-rw-r--r--   0        0        0     9143 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/nlu/utils/hugging_face/transformers_pre_post_processors.py
+-rw-r--r--   0        0        0     3887 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/nlu/utils/mitie_utils.py
+-rw-r--r--   0        0        0     5386 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/nlu/utils/pattern_utils.py
+-rw-r--r--   0        0        0    11795 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/nlu/utils/spacy_utils.py
+-rw-r--r--   0        0        0     2241 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/plugin.py
+-rw-r--r--   0        0        0    55474 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/server.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/__init__.py
+-rw-r--r--   0        0        0     4294 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/constants.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/__init__.py
+-rw-r--r--   0        0        0     4346 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/constants.py
+-rw-r--r--   0        0        0     1366 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/conversation.py
+-rw-r--r--   0        0        0    75018 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/domain.py
+-rw-r--r--   0        0        0    65833 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/events.py
+-rw-r--r--   0        0        0    35597 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/generator.py
+-rw-r--r--   0        0        0     8130 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/slot_mappings.py
+-rw-r--r--   0        0        0    16371 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/slots.py
+-rw-r--r--   0        0        0    33176 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/trackers.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/__init__.py
+-rw-r--r--   0        0        0     2895 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/loading.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/story_reader/__init__.py
+-rw-r--r--   0        0        0     4449 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/story_reader/story_reader.py
+-rw-r--r--   0        0        0     6671 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/story_reader/story_step_builder.py
+-rw-r--r--   0        0        0    32873 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/story_reader/yaml_story_reader.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/story_writer/__init__.py
+-rw-r--r--   0        0        0     2543 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/story_writer/story_writer.py
+-rw-r--r--   0        0        0    14903 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/story_writer/yaml_story_writer.py
+-rw-r--r--   0        0        0    29313 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/structures.py
+-rw-r--r--   0        0        0     3500 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/visualization.html
+-rw-r--r--   0        0        0    20341 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/core/training_data/visualization.py
+-rw-r--r--   0        0        0     5479 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/data.py
+-rw-r--r--   0        0        0     3633 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/exceptions.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/importers/__init__.py
+-rw-r--r--   0        0        0    21555 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/importers/importer.py
+-rw-r--r--   0        0        0     7836 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/importers/multi_project.py
+-rw-r--r--   0        0        0     3388 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/importers/rasa.py
+-rw-r--r--   0        0        0      861 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/importers/utils.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/__init__.py
+-rw-r--r--   0        0        0     1388 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/constants.py
+-rw-r--r--   0        0        0      188 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/interpreter.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/__init__.py
+-rw-r--r--   0        0        0     6759 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/entities_parser.py
+-rw-r--r--   0        0        0    14835 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/features.py
+-rw-r--r--   0        0        0      453 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/formats/__init__.py
+-rw-r--r--   0        0        0     6123 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/formats/dialogflow.py
+-rw-r--r--   0        0        0     3014 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/formats/luis.py
+-rw-r--r--   0        0        0     4495 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/formats/rasa.py
+-rw-r--r--   0        0        0    22353 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/formats/rasa_yaml.py
+-rw-r--r--   0        0        0     8540 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/formats/readerwriter.py
+-rw-r--r--   0        0        0     1820 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/formats/wit.py
+-rw-r--r--   0        0        0     4258 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/loading.py
+-rw-r--r--   0        0        0     1116 2023-04-05 14:19:12.902150 rasa-3.5.4/rasa/shared/nlu/training_data/lookup_tables_parser.py
+-rw-r--r--   0        0        0    16662 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/nlu/training_data/message.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/nlu/training_data/schemas/__init__.py
+-rw-r--r--   0        0        0     2565 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/nlu/training_data/schemas/data_schema.py
+-rw-r--r--   0        0        0     1179 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/nlu/training_data/schemas/nlu.yml
+-rw-r--r--   0        0        0     1595 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/nlu/training_data/schemas/responses.yml
+-rw-r--r--   0        0        0     1476 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/nlu/training_data/synonyms_parser.py
+-rw-r--r--   0        0        0    28493 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/nlu/training_data/training_data.py
+-rw-r--r--   0        0        0     7040 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/nlu/training_data/util.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/__init__.py
+-rw-r--r--   0        0        0     1129 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/cli.py
+-rw-r--r--   0        0        0     8731 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/common.py
+-rw-r--r--   0        0        0    19456 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/io.py
+-rw-r--r--   0        0        0      883 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/pykwalify_extensions.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/schemas/__init__.py
+-rw-r--r--   0        0        0       27 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/schemas/config.yml
+-rw-r--r--   0        0        0     3267 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/schemas/domain.yml
+-rw-r--r--   0        0        0     5569 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/schemas/events.py
+-rw-r--r--   0        0        0      779 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/schemas/model_config.yml
+-rw-r--r--   0        0        0     4034 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/schemas/stories.yml
+-rw-r--r--   0        0        0    10178 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/shared/utils/validation.py
+-rw-r--r--   0        0        0    36084 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/telemetry.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/__init__.py
+-rw-r--r--   0        0        0    19852 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/common.py
+-rw-r--r--   0        0        0     1647 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/converter.py
+-rw-r--r--   0        0        0     8796 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/endpoints.py
+-rw-r--r--   0        0        0     7831 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/io.py
+-rw-r--r--   0        0        0    12246 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/plotting.py
+-rw-r--r--   0        0        0        0 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/__init__.py
+-rw-r--r--   0        0        0     4036 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/callback.py
+-rw-r--r--   0        0        0     3140 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/constants.py
+-rw-r--r--   0        0        0     9020 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/crf.py
+-rw-r--r--   0        0        0    15526 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/data_generator.py
+-rw-r--r--   0        0        0     5576 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/environment.py
+-rw-r--r--   0        0        0      168 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/exceptions.py
+-rw-r--r--   0        0        0    59313 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/layers.py
+-rw-r--r--   0        0        0     3319 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/layers_utils.py
+-rw-r--r--   0        0        0    34572 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/model_data.py
+-rw-r--r--   0        0        0    18667 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/model_data_utils.py
+-rw-r--r--   0        0        0    36004 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/models.py
+-rw-r--r--   0        0        0    49066 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/rasa_layers.py
+-rw-r--r--   0        0        0    25509 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/transformer.py
+-rw-r--r--   0        0        0      204 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/tensorflow/types.py
+-rw-r--r--   0        0        0    20984 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/utils/train_utils.py
+-rw-r--r--   0        0        0    17708 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/validator.py
+-rw-r--r--   0        0        0      116 2023-04-05 14:19:12.906149 rasa-3.5.4/rasa/version.py
+-rw-r--r--   0        0        0    27169 1970-01-01 00:00:00.000000 rasa-3.5.4/setup.py
+-rw-r--r--   0        0        0    26357 1970-01-01 00:00:00.000000 rasa-3.5.4/PKG-INFO
```

### Comparing `rasa-3.5.3/LICENSE.txt` & `rasa-3.5.4/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/README.md` & `rasa-3.5.4/README.md`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/pyproject.toml` & `rasa-3.5.4/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 [tool.black]
 line-length = 88
 target-version = [ "py37", "py38", "py39", "py310",]
 exclude = "((.eggs | .git | .pytest_cache | build | dist))"
 
 [tool.poetry]
 name = "rasa"
-version = "3.5.3"
+version = "3.5.4"
 description = "Open source machine learning framework to automate text- and voice-based conversations: NLU, dialogue management, connect to Slack, Facebook, and more - Create chatbots and voice assistants"
 authors = [ "Rasa Technologies GmbH <hi@rasa.com>",]
 maintainers = [ "Tom Bocklisch <tom@rasa.com>",]
 homepage = "https://rasa.com"
 repository = "https://github.com/rasahq/rasa"
 documentation = "https://rasa.com/docs"
 classifiers = [ "Development Status :: 5 - Production/Stable", "Intended Audience :: Developers", "License :: OSI Approved :: Apache Software License", "Topic :: Software Development :: Libraries",]
@@ -89,15 +89,15 @@
 [tool.poetry.dependencies]
 python = ">=3.7,<3.11"
 boto3 = "^1.12"
 requests = "^2.23"
 matplotlib = ">=3.1,<3.6"
 attrs = ">=19.3,<22.2"
 jsonpickle = ">=1.3,<3.1"
-redis = ">=3.4,<5.0"
+redis = ">=4.5.3, <5.0"
 absl-py = ">=0.9,<1.4"
 apscheduler = ">=3.6,<3.10"
 tqdm = "^4.31"
 networkx = ">=2.4,<2.7"
 fbmessenger = "~6.0.0"
 pykwalify = ">=1.7,<1.9"
 coloredlogs = ">=10,<16"
@@ -112,14 +112,16 @@
 pytz = ">=2019.1,<2023.0"
 rasa-sdk = "~3.5.0"
 colorclass = "~2.2"
 terminaltables = "~3.1.0"
 sanic = "~21.12"
 sanic-cors = "~2.0.0"
 sanic-jwt = "^1.6.0"
+sanic-routing = "^0.7.2"
+websockets = ">=10.0,<11.0"
 cloudpickle = ">=1.2,<2.3"
 aiohttp = ">=3.6,!=3.7.4.post0,<3.9"
 questionary = ">=1.5.1,<1.11.0"
 prompt-toolkit = "^3.0,<3.0.29"
 python-socketio = ">=4.4,<6"
 python-engineio = ">=4,<6,!=5.0.0"
 pydot = "~1.4"
@@ -131,23 +133,22 @@
 tensorflow_hub = "~0.12.0"
 tensorflow-addons = ">=0.18,<0.20"
 setuptools = ">=41.0.0"
 ujson = ">=1.35,<6.0"
 regex = ">=2020.6,<2022.11"
 joblib = ">=0.15.1,<1.3.0"
 sentry-sdk = ">=0.17.0,<1.15.0"
-aio-pika = ">=6.7.1,<9.0.0"
+aio-pika = ">=6.7.1,<8.2.4"
 aiogram = "<2.26"
 typing-extensions = ">=4.1.1,<5.0.0"
 typing-utils = "^0.1.0"
 tarsafe = "^0.0.3"
 google-auth = "<3"
 CacheControl = "^0.12.9"
 randomname = "^0.1.5"
-sanic-routing = "^0.7.2"
 pluggy = "^1.0.0"
 slack-sdk = "^3.19.2"
 confluent-kafka = "^1.9.2"
 [[tool.poetry.dependencies.dask]]
 version = "2022.2.0"
 python = "~=3.7.0"
 
@@ -253,23 +254,23 @@
 log_cli_level = "WARNING"
 log_cli = true
 markers = [ "skip_on_windows", "skip_on_ci", "sequential", "category_cli", "category_core_featurizers", "category_policies", "category_nlu_featurizers", "category_nlu_predictors", "category_full_model_training", "category_other_unit_tests", "category_performance", "flaky",]
 timeout = 60
 timeout_func_only = true
 
 [tool.poetry.dependencies.tensorflow]
-version = "~2.11.0"
+version = "2.11.0"
 markers = "sys_platform != 'darwin' or platform_machine != 'arm64'"
 
 [tool.poetry.dependencies.tensorflow-intel]
-version = "~2.11.0"
+version = "2.11.0"
 markers = "sys_platform == 'win32'"
 
 [tool.poetry.dependencies.tensorflow-cpu-aws]
-version = "~2.11.0"
+version = "2.11.0"
 markers = "sys_platform == 'linux' and (platform_machine == 'arm64' or platform_machine == 'aarch64')"
 
 [tool.poetry.dependencies.tensorflow-macos]
 version = "2.11.0"
 markers = "sys_platform == 'darwin' and platform_machine == 'arm64'"
 
 [tool.poetry.dependencies.PyJWT]
@@ -282,15 +283,15 @@
 
 [tool.poetry.dependencies.tensorflow-metal]
 version = "0.5.1"
 markers = "sys_platform == 'darwin' and platform_machine == 'arm64'"
 optional = true
 
 [tool.poetry.dependencies.tensorflow-text]
-version = "~2.11.0"
+version = "2.11.0"
 markers = "sys_platform!='win32' and platform_machine!='arm64'"
 
 [tool.poetry.dependencies."github3.py"]
 version = "~3.2.0"
 optional = true
 
 [tool.poetry.dependencies.transformers]
@@ -312,7 +313,8 @@
 
 [tool.poetry.dev-dependencies.pytest-sanic]
 git = "https://github.com/RasaHQ/pytest-sanic"
 branch = "fix_signal_issue"
 
 [tool.poetry.group.dev.dependencies]
 ruff = "^0.0.255"
+docker = "^6.0.1"
```

### Comparing `rasa-3.5.3/rasa/__main__.py` & `rasa-3.5.4/rasa/__main__.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/api.py` & `rasa-3.5.4/rasa/api.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/arguments/data.py` & `rasa-3.5.4/rasa/cli/arguments/data.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/arguments/default_arguments.py` & `rasa-3.5.4/rasa/cli/arguments/default_arguments.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/arguments/evaluate.py` & `rasa-3.5.4/rasa/cli/arguments/evaluate.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/arguments/export.py` & `rasa-3.5.4/rasa/cli/arguments/export.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/arguments/interactive.py` & `rasa-3.5.4/rasa/cli/arguments/interactive.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/arguments/run.py` & `rasa-3.5.4/rasa/cli/arguments/run.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/arguments/test.py` & `rasa-3.5.4/rasa/cli/arguments/test.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/arguments/train.py` & `rasa-3.5.4/rasa/cli/arguments/train.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/arguments/visualize.py` & `rasa-3.5.4/rasa/cli/arguments/visualize.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/arguments/x.py` & `rasa-3.5.4/rasa/cli/arguments/x.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/data.py` & `rasa-3.5.4/rasa/cli/data.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/evaluate.py` & `rasa-3.5.4/rasa/cli/evaluate.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/export.py` & `rasa-3.5.4/rasa/cli/export.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/initial_project/actions/actions.py` & `rasa-3.5.4/rasa/cli/initial_project/actions/actions.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/initial_project/config.yml` & `rasa-3.5.4/rasa/cli/initial_project/config.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/initial_project/credentials.yml` & `rasa-3.5.4/rasa/cli/initial_project/credentials.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/initial_project/data/nlu.yml` & `rasa-3.5.4/rasa/cli/initial_project/data/nlu.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/initial_project/data/stories.yml` & `rasa-3.5.4/rasa/cli/initial_project/data/stories.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/initial_project/domain.yml` & `rasa-3.5.4/rasa/cli/initial_project/domain.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/initial_project/endpoints.yml` & `rasa-3.5.4/rasa/cli/initial_project/endpoints.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/initial_project/tests/test_stories.yml` & `rasa-3.5.4/rasa/cli/initial_project/tests/test_stories.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/interactive.py` & `rasa-3.5.4/rasa/cli/interactive.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/run.py` & `rasa-3.5.4/rasa/cli/run.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/scaffold.py` & `rasa-3.5.4/rasa/cli/scaffold.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/shell.py` & `rasa-3.5.4/rasa/cli/shell.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/telemetry.py` & `rasa-3.5.4/rasa/cli/telemetry.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/test.py` & `rasa-3.5.4/rasa/cli/test.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/train.py` & `rasa-3.5.4/rasa/cli/train.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/utils.py` & `rasa-3.5.4/rasa/cli/utils.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/visualize.py` & `rasa-3.5.4/rasa/cli/visualize.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/cli/x.py` & `rasa-3.5.4/rasa/cli/x.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/constants.py` & `rasa-3.5.4/rasa/constants.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/actions/action.py` & `rasa-3.5.4/rasa/core/actions/action.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/actions/forms.py` & `rasa-3.5.4/rasa/core/actions/forms.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/actions/loops.py` & `rasa-3.5.4/rasa/core/actions/loops.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/actions/two_stage_fallback.py` & `rasa-3.5.4/rasa/core/actions/two_stage_fallback.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/agent.py` & `rasa-3.5.4/rasa/core/agent.py`

 * *Files 0% similar despite different names*

```diff
@@ -389,16 +389,15 @@
         Args:
             message_data (Text): Contain the received message in text or\
             intent payload format.
 
         Returns:
             The parsed message.
 
-            Example:
-
+        Example:
                 {\
                     "text": '/greet{"name":"Rasa"}',\
                     "intent": {"name": "greet", "confidence": 1.0},\
                     "intent_ranking": [{"name": "greet", "confidence": 1.0}],\
                     "entities": [{"entity": "name", "start": 6,\
                                   "end": 21, "value": "Rasa"}],\
                 }
```

### Comparing `rasa-3.5.3/rasa/core/brokers/broker.py` & `rasa-3.5.4/rasa/core/brokers/broker.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/brokers/file.py` & `rasa-3.5.4/rasa/core/brokers/file.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/brokers/kafka.py` & `rasa-3.5.4/rasa/core/brokers/kafka.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/brokers/pika.py` & `rasa-3.5.4/rasa/core/brokers/pika.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/brokers/sql.py` & `rasa-3.5.4/rasa/core/brokers/sql.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/__init__.py` & `rasa-3.5.4/rasa/core/channels/__init__.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/botframework.py` & `rasa-3.5.4/rasa/core/channels/botframework.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/callback.py` & `rasa-3.5.4/rasa/core/channels/callback.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/channel.py` & `rasa-3.5.4/rasa/core/channels/channel.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/console.py` & `rasa-3.5.4/rasa/core/channels/console.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/facebook.py` & `rasa-3.5.4/rasa/core/channels/facebook.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/hangouts.py` & `rasa-3.5.4/rasa/core/channels/hangouts.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/mattermost.py` & `rasa-3.5.4/rasa/core/channels/mattermost.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/rasa_chat.py` & `rasa-3.5.4/rasa/core/channels/rasa_chat.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/rest.py` & `rasa-3.5.4/rasa/core/channels/rest.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/rocketchat.py` & `rasa-3.5.4/rasa/core/channels/rocketchat.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/slack.py` & `rasa-3.5.4/rasa/core/channels/slack.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/socketio.py` & `rasa-3.5.4/rasa/core/channels/socketio.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/telegram.py` & `rasa-3.5.4/rasa/core/channels/telegram.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/twilio.py` & `rasa-3.5.4/rasa/core/channels/twilio.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/twilio_voice.py` & `rasa-3.5.4/rasa/core/channels/twilio_voice.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/channels/webexteams.py` & `rasa-3.5.4/rasa/core/channels/webexteams.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/constants.py` & `rasa-3.5.4/rasa/core/constants.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/evaluation/marker.py` & `rasa-3.5.4/rasa/core/evaluation/marker.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/evaluation/marker_base.py` & `rasa-3.5.4/rasa/core/evaluation/marker_base.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/evaluation/marker_stats.py` & `rasa-3.5.4/rasa/core/evaluation/marker_stats.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/evaluation/marker_tracker_loader.py` & `rasa-3.5.4/rasa/core/evaluation/marker_tracker_loader.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/exceptions.py` & `rasa-3.5.4/rasa/core/exceptions.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/exporter.py` & `rasa-3.5.4/rasa/core/exporter.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/featurizers/precomputation.py` & `rasa-3.5.4/rasa/core/featurizers/precomputation.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/featurizers/single_state_featurizer.py` & `rasa-3.5.4/rasa/core/featurizers/single_state_featurizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/featurizers/tracker_featurizers.py` & `rasa-3.5.4/rasa/core/featurizers/tracker_featurizers.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/http_interpreter.py` & `rasa-3.5.4/rasa/core/http_interpreter.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/jobs.py` & `rasa-3.5.4/rasa/core/jobs.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/lock.py` & `rasa-3.5.4/rasa/core/lock.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/lock_store.py` & `rasa-3.5.4/rasa/core/lock_store.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/migrate.py` & `rasa-3.5.4/rasa/core/migrate.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/nlg/callback.py` & `rasa-3.5.4/rasa/core/nlg/callback.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/nlg/generator.py` & `rasa-3.5.4/rasa/core/nlg/generator.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/nlg/interpolator.py` & `rasa-3.5.4/rasa/core/nlg/interpolator.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/nlg/response.py` & `rasa-3.5.4/rasa/core/nlg/response.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/policies/ensemble.py` & `rasa-3.5.4/rasa/core/policies/ensemble.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/policies/memoization.py` & `rasa-3.5.4/rasa/core/policies/memoization.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/policies/policy.py` & `rasa-3.5.4/rasa/core/policies/policy.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/policies/rule_policy.py` & `rasa-3.5.4/rasa/core/policies/rule_policy.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/policies/ted_policy.py` & `rasa-3.5.4/rasa/core/policies/ted_policy.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/policies/unexpected_intent_policy.py` & `rasa-3.5.4/rasa/core/policies/unexpected_intent_policy.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/processor.py` & `rasa-3.5.4/rasa/core/processor.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/run.py` & `rasa-3.5.4/rasa/core/run.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/test.py` & `rasa-3.5.4/rasa/core/test.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/tracker_store.py` & `rasa-3.5.4/rasa/core/tracker_store.py`

 * *Files 0% similar despite different names*

```diff
@@ -164,14 +164,15 @@
 
         try:
             _tracker_store = plugin_manager().hook.create_tracker_store(
                 endpoint_config=obj,
                 domain=domain,
                 event_broker=event_broker,
             )
+
             tracker_store = (
                 _tracker_store
                 if _tracker_store
                 else create_tracker_store(obj, domain, event_broker)
             )
 
             return tracker_store
@@ -310,14 +311,15 @@
             )
 
         return tracker
 
     async def stream_events(self, tracker: DialogueStateTracker) -> None:
         """Streams events to a message broker."""
         if self.event_broker is None:
+            logger.debug("No event broker configured. Skipping streaming events.")
             return None
 
         offset = await self.number_of_existing_events(tracker.sender_id)
         events = tracker.events
         new_events = list(itertools.islice(events, offset, len(events)))
 
         await self._stream_new_events(self.event_broker, new_events, tracker.sender_id)
```

### Comparing `rasa-3.5.3/rasa/core/train.py` & `rasa-3.5.4/rasa/core/train.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/training/__init__.py` & `rasa-3.5.4/rasa/core/training/__init__.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/training/converters/responses_prefix_converter.py` & `rasa-3.5.4/rasa/core/training/converters/responses_prefix_converter.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/training/interactive.py` & `rasa-3.5.4/rasa/core/training/interactive.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/training/story_conflict.py` & `rasa-3.5.4/rasa/core/training/story_conflict.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/training/training.py` & `rasa-3.5.4/rasa/core/training/training.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/utils.py` & `rasa-3.5.4/rasa/core/utils.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/core/visualize.py` & `rasa-3.5.4/rasa/core/visualize.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/caching.py` & `rasa-3.5.4/rasa/engine/caching.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/graph.py` & `rasa-3.5.4/rasa/engine/graph.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/loader.py` & `rasa-3.5.4/rasa/engine/loader.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/recipes/config_files/default_config.yml` & `rasa-3.5.4/rasa/engine/recipes/config_files/default_config.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/recipes/default_components.py` & `rasa-3.5.4/rasa/engine/recipes/default_components.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/recipes/default_recipe.py` & `rasa-3.5.4/rasa/engine/recipes/default_recipe.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/recipes/graph_recipe.py` & `rasa-3.5.4/rasa/engine/recipes/graph_recipe.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/recipes/recipe.py` & `rasa-3.5.4/rasa/engine/recipes/recipe.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/runner/dask.py` & `rasa-3.5.4/rasa/engine/runner/dask.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/runner/interface.py` & `rasa-3.5.4/rasa/engine/runner/interface.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/storage/local_model_storage.py` & `rasa-3.5.4/rasa/engine/storage/local_model_storage.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/storage/resource.py` & `rasa-3.5.4/rasa/engine/storage/resource.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/storage/storage.py` & `rasa-3.5.4/rasa/engine/storage/storage.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/training/components.py` & `rasa-3.5.4/rasa/engine/training/components.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/training/fingerprinting.py` & `rasa-3.5.4/rasa/engine/training/fingerprinting.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/training/graph_trainer.py` & `rasa-3.5.4/rasa/engine/training/graph_trainer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/training/hooks.py` & `rasa-3.5.4/rasa/engine/training/hooks.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/engine/validation.py` & `rasa-3.5.4/rasa/engine/validation.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/exceptions.py` & `rasa-3.5.4/rasa/exceptions.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/graph_components/converters/nlu_message_converter.py` & `rasa-3.5.4/rasa/graph_components/converters/nlu_message_converter.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/graph_components/providers/domain_for_core_training_provider.py` & `rasa-3.5.4/rasa/graph_components/providers/domain_for_core_training_provider.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/graph_components/providers/domain_provider.py` & `rasa-3.5.4/rasa/graph_components/providers/domain_provider.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/graph_components/providers/forms_provider.py` & `rasa-3.5.4/rasa/graph_components/providers/forms_provider.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/graph_components/providers/nlu_training_data_provider.py` & `rasa-3.5.4/rasa/graph_components/providers/nlu_training_data_provider.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/graph_components/providers/responses_provider.py` & `rasa-3.5.4/rasa/graph_components/providers/responses_provider.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/graph_components/providers/rule_only_provider.py` & `rasa-3.5.4/rasa/graph_components/providers/rule_only_provider.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/graph_components/providers/story_graph_provider.py` & `rasa-3.5.4/rasa/graph_components/providers/story_graph_provider.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/graph_components/providers/training_tracker_provider.py` & `rasa-3.5.4/rasa/graph_components/providers/training_tracker_provider.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/graph_components/validators/default_recipe_validator.py` & `rasa-3.5.4/rasa/graph_components/validators/default_recipe_validator.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/graph_components/validators/finetuning_validator.py` & `rasa-3.5.4/rasa/graph_components/validators/finetuning_validator.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/jupyter.py` & `rasa-3.5.4/rasa/jupyter.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/model.py` & `rasa-3.5.4/rasa/model.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/model_testing.py` & `rasa-3.5.4/rasa/model_testing.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/model_training.py` & `rasa-3.5.4/rasa/model_training.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/classifiers/diet_classifier.py` & `rasa-3.5.4/rasa/nlu/classifiers/diet_classifier.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/classifiers/fallback_classifier.py` & `rasa-3.5.4/rasa/nlu/classifiers/fallback_classifier.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/classifiers/keyword_intent_classifier.py` & `rasa-3.5.4/rasa/nlu/classifiers/keyword_intent_classifier.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/classifiers/logistic_regression_classifier.py` & `rasa-3.5.4/rasa/nlu/classifiers/logistic_regression_classifier.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/classifiers/mitie_intent_classifier.py` & `rasa-3.5.4/rasa/nlu/classifiers/mitie_intent_classifier.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/classifiers/regex_message_handler.py` & `rasa-3.5.4/rasa/nlu/classifiers/regex_message_handler.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/classifiers/sklearn_intent_classifier.py` & `rasa-3.5.4/rasa/nlu/classifiers/sklearn_intent_classifier.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/constants.py` & `rasa-3.5.4/rasa/nlu/constants.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/convert.py` & `rasa-3.5.4/rasa/nlu/convert.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/emulators/dialogflow.py` & `rasa-3.5.4/rasa/nlu/emulators/dialogflow.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/emulators/emulator.py` & `rasa-3.5.4/rasa/nlu/emulators/emulator.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/emulators/luis.py` & `rasa-3.5.4/rasa/nlu/emulators/luis.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/emulators/wit.py` & `rasa-3.5.4/rasa/nlu/emulators/wit.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/extractors/crf_entity_extractor.py` & `rasa-3.5.4/rasa/nlu/extractors/crf_entity_extractor.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/extractors/duckling_entity_extractor.py` & `rasa-3.5.4/rasa/nlu/extractors/duckling_entity_extractor.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/extractors/entity_synonyms.py` & `rasa-3.5.4/rasa/nlu/extractors/entity_synonyms.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/extractors/extractor.py` & `rasa-3.5.4/rasa/nlu/extractors/extractor.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/extractors/mitie_entity_extractor.py` & `rasa-3.5.4/rasa/nlu/extractors/mitie_entity_extractor.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/extractors/regex_entity_extractor.py` & `rasa-3.5.4/rasa/nlu/extractors/regex_entity_extractor.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/extractors/spacy_entity_extractor.py` & `rasa-3.5.4/rasa/nlu/extractors/spacy_entity_extractor.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/featurizers/dense_featurizer/convert_featurizer.py` & `rasa-3.5.4/rasa/nlu/featurizers/dense_featurizer/convert_featurizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/featurizers/dense_featurizer/dense_featurizer.py` & `rasa-3.5.4/rasa/nlu/featurizers/dense_featurizer/dense_featurizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/featurizers/dense_featurizer/lm_featurizer.py` & `rasa-3.5.4/rasa/nlu/featurizers/dense_featurizer/lm_featurizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/featurizers/dense_featurizer/mitie_featurizer.py` & `rasa-3.5.4/rasa/nlu/featurizers/dense_featurizer/mitie_featurizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/featurizers/dense_featurizer/spacy_featurizer.py` & `rasa-3.5.4/rasa/nlu/featurizers/dense_featurizer/spacy_featurizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/featurizers/featurizer.py` & `rasa-3.5.4/rasa/nlu/featurizers/featurizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/featurizers/sparse_featurizer/count_vectors_featurizer.py` & `rasa-3.5.4/rasa/nlu/featurizers/sparse_featurizer/count_vectors_featurizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/featurizers/sparse_featurizer/lexical_syntactic_featurizer.py` & `rasa-3.5.4/rasa/nlu/featurizers/sparse_featurizer/lexical_syntactic_featurizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/featurizers/sparse_featurizer/regex_featurizer.py` & `rasa-3.5.4/rasa/nlu/featurizers/sparse_featurizer/regex_featurizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/model.py` & `rasa-3.5.4/rasa/nlu/model.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/persistor.py` & `rasa-3.5.4/rasa/nlu/persistor.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/run.py` & `rasa-3.5.4/rasa/nlu/run.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/selectors/response_selector.py` & `rasa-3.5.4/rasa/nlu/selectors/response_selector.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/test.py` & `rasa-3.5.4/rasa/nlu/test.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/tokenizers/jieba_tokenizer.py` & `rasa-3.5.4/rasa/nlu/tokenizers/jieba_tokenizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/tokenizers/mitie_tokenizer.py` & `rasa-3.5.4/rasa/nlu/tokenizers/mitie_tokenizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/tokenizers/spacy_tokenizer.py` & `rasa-3.5.4/rasa/nlu/tokenizers/spacy_tokenizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/tokenizers/tokenizer.py` & `rasa-3.5.4/rasa/nlu/tokenizers/tokenizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/tokenizers/whitespace_tokenizer.py` & `rasa-3.5.4/rasa/nlu/tokenizers/whitespace_tokenizer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/utils/__init__.py` & `rasa-3.5.4/rasa/nlu/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/utils/bilou_utils.py` & `rasa-3.5.4/rasa/nlu/utils/bilou_utils.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/utils/hugging_face/registry.py` & `rasa-3.5.4/rasa/nlu/utils/hugging_face/registry.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/utils/hugging_face/transformers_pre_post_processors.py` & `rasa-3.5.4/rasa/nlu/utils/hugging_face/transformers_pre_post_processors.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/utils/mitie_utils.py` & `rasa-3.5.4/rasa/nlu/utils/mitie_utils.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/utils/pattern_utils.py` & `rasa-3.5.4/rasa/nlu/utils/pattern_utils.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/nlu/utils/spacy_utils.py` & `rasa-3.5.4/rasa/nlu/utils/spacy_utils.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/plugin.py` & `rasa-3.5.4/rasa/plugin.py`

 * *Files 2% similar despite different names*

```diff
@@ -66,10 +66,10 @@
     """Hook specification for initialising managers."""
 
 
 @hookspec(firstresult=True)  # type: ignore[misc]
 def create_tracker_store(  # type: ignore[empty-body]
     endpoint_config: Union["TrackerStore", "EndpointConfig"],
     domain: "Domain",
-    event_broker: Optional["EventBroker"] = None,
+    event_broker: Optional["EventBroker"],
 ) -> "TrackerStore":
     """Hook specification for wrapping with AuthRetryTrackerStore."""
```

### Comparing `rasa-3.5.3/rasa/server.py` & `rasa-3.5.4/rasa/server.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/constants.py` & `rasa-3.5.4/rasa/shared/constants.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/constants.py` & `rasa-3.5.4/rasa/shared/core/constants.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/conversation.py` & `rasa-3.5.4/rasa/shared/core/conversation.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/domain.py` & `rasa-3.5.4/rasa/shared/core/domain.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/events.py` & `rasa-3.5.4/rasa/shared/core/events.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/generator.py` & `rasa-3.5.4/rasa/shared/core/generator.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/slot_mappings.py` & `rasa-3.5.4/rasa/shared/core/slot_mappings.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/slots.py` & `rasa-3.5.4/rasa/shared/core/slots.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/trackers.py` & `rasa-3.5.4/rasa/shared/core/trackers.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/training_data/loading.py` & `rasa-3.5.4/rasa/shared/core/training_data/loading.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/training_data/story_reader/story_reader.py` & `rasa-3.5.4/rasa/shared/core/training_data/story_reader/story_reader.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/training_data/story_reader/story_step_builder.py` & `rasa-3.5.4/rasa/shared/core/training_data/story_reader/story_step_builder.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/training_data/story_reader/yaml_story_reader.py` & `rasa-3.5.4/rasa/shared/core/training_data/story_reader/yaml_story_reader.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/training_data/story_writer/story_writer.py` & `rasa-3.5.4/rasa/shared/core/training_data/story_writer/story_writer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/training_data/story_writer/yaml_story_writer.py` & `rasa-3.5.4/rasa/shared/core/training_data/story_writer/yaml_story_writer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/training_data/structures.py` & `rasa-3.5.4/rasa/shared/core/training_data/structures.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/training_data/visualization.html` & `rasa-3.5.4/rasa/shared/core/training_data/visualization.html`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/core/training_data/visualization.py` & `rasa-3.5.4/rasa/shared/core/training_data/visualization.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/data.py` & `rasa-3.5.4/rasa/shared/data.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/exceptions.py` & `rasa-3.5.4/rasa/shared/exceptions.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/importers/importer.py` & `rasa-3.5.4/rasa/shared/importers/importer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/importers/multi_project.py` & `rasa-3.5.4/rasa/shared/importers/multi_project.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/importers/rasa.py` & `rasa-3.5.4/rasa/shared/importers/rasa.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/importers/utils.py` & `rasa-3.5.4/rasa/shared/importers/utils.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/constants.py` & `rasa-3.5.4/rasa/shared/nlu/constants.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/entities_parser.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/entities_parser.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/features.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/features.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/formats/dialogflow.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/formats/dialogflow.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/formats/luis.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/formats/luis.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/formats/rasa.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/formats/rasa.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/formats/rasa_yaml.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/formats/rasa_yaml.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/formats/readerwriter.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/formats/readerwriter.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/formats/wit.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/formats/wit.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/loading.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/loading.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/lookup_tables_parser.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/lookup_tables_parser.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/message.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/message.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/schemas/data_schema.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/schemas/data_schema.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/schemas/nlu.yml` & `rasa-3.5.4/rasa/shared/nlu/training_data/schemas/nlu.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/schemas/responses.yml` & `rasa-3.5.4/rasa/shared/nlu/training_data/schemas/responses.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/synonyms_parser.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/synonyms_parser.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/training_data.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/training_data.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/nlu/training_data/util.py` & `rasa-3.5.4/rasa/shared/nlu/training_data/util.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/utils/cli.py` & `rasa-3.5.4/rasa/shared/utils/cli.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/utils/common.py` & `rasa-3.5.4/rasa/shared/utils/common.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/utils/io.py` & `rasa-3.5.4/rasa/shared/utils/io.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/utils/pykwalify_extensions.py` & `rasa-3.5.4/rasa/shared/utils/pykwalify_extensions.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/utils/schemas/domain.yml` & `rasa-3.5.4/rasa/shared/utils/schemas/domain.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/utils/schemas/events.py` & `rasa-3.5.4/rasa/shared/utils/schemas/events.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/utils/schemas/model_config.yml` & `rasa-3.5.4/rasa/shared/utils/schemas/model_config.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/utils/schemas/stories.yml` & `rasa-3.5.4/rasa/shared/utils/schemas/stories.yml`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/shared/utils/validation.py` & `rasa-3.5.4/rasa/shared/utils/validation.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/telemetry.py` & `rasa-3.5.4/rasa/telemetry.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/common.py` & `rasa-3.5.4/rasa/utils/common.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/converter.py` & `rasa-3.5.4/rasa/utils/converter.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/endpoints.py` & `rasa-3.5.4/rasa/utils/endpoints.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/io.py` & `rasa-3.5.4/rasa/utils/io.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/plotting.py` & `rasa-3.5.4/rasa/utils/plotting.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/callback.py` & `rasa-3.5.4/rasa/utils/tensorflow/callback.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/constants.py` & `rasa-3.5.4/rasa/utils/tensorflow/constants.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/crf.py` & `rasa-3.5.4/rasa/utils/tensorflow/crf.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/data_generator.py` & `rasa-3.5.4/rasa/utils/tensorflow/data_generator.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/environment.py` & `rasa-3.5.4/rasa/utils/tensorflow/environment.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/layers.py` & `rasa-3.5.4/rasa/utils/tensorflow/layers.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/layers_utils.py` & `rasa-3.5.4/rasa/utils/tensorflow/layers_utils.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/model_data.py` & `rasa-3.5.4/rasa/utils/tensorflow/model_data.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/model_data_utils.py` & `rasa-3.5.4/rasa/utils/tensorflow/model_data_utils.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/models.py` & `rasa-3.5.4/rasa/utils/tensorflow/models.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/rasa_layers.py` & `rasa-3.5.4/rasa/utils/tensorflow/rasa_layers.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/tensorflow/transformer.py` & `rasa-3.5.4/rasa/utils/tensorflow/transformer.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/utils/train_utils.py` & `rasa-3.5.4/rasa/utils/train_utils.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/rasa/validator.py` & `rasa-3.5.4/rasa/validator.py`

 * *Files identical despite different names*

### Comparing `rasa-3.5.3/setup.py` & `rasa-3.5.4/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -59,15 +59,15 @@
  'rasa.engine.recipes': ['config_files/*']}
 
 install_requires = \
 ['CacheControl>=0.12.9,<0.13.0',
  'PyJWT[crypto]>=2.0.0,<3.0.0',
  'SQLAlchemy>=1.4.0,<1.5.0',
  'absl-py>=0.9,<1.4',
- 'aio-pika>=6.7.1,<9.0.0',
+ 'aio-pika>=6.7.1,<8.2.4',
  'aiogram<2.26',
  'aiohttp>=3.6,!=3.7.4.post0,<3.9',
  'apscheduler>=3.6,<3.10',
  'attrs>=19.3,<22.2',
  'boto3>=1.12,<2.0',
  'cloudpickle>=1.2,<2.3',
  'colorclass>=2.2,<2.3',
@@ -93,15 +93,15 @@
  'python-dateutil>=2.8,<2.9',
  'python-engineio>=4,<6,!=5.0.0',
  'python-socketio>=4.4,<6',
  'pytz>=2019.1,<2023.0',
  'questionary>=1.5.1,<1.11.0',
  'randomname>=0.1.5,<0.2.0',
  'rasa-sdk>=3.5.0,<3.6.0',
- 'redis>=3.4,<5.0',
+ 'redis>=4.5.3,<5.0',
  'regex>=2020.6,<2022.11',
  'requests>=2.23,<3.0',
  'rocketchat_API>=0.6.31,<1.29.0',
  'ruamel.yaml>=0.16.5,<0.18.0',
  'sanic-cors>=2.0.0,<2.1.0',
  'sanic-jwt>=1.6.0,<2.0.0',
  'sanic-routing>=0.7.2,<0.8.0',
@@ -115,30 +115,31 @@
  'tensorflow_hub>=0.12.0,<0.13.0',
  'terminaltables>=3.1.0,<3.2.0',
  'tqdm>=4.31,<5.0',
  'twilio>=6.26,<7.15',
  'typing-extensions>=4.1.1,<5.0.0',
  'typing-utils>=0.1.0,<0.2.0',
  'ujson>=1.35,<6.0',
- 'webexteamssdk>=1.1.1,<1.7.0']
+ 'webexteamssdk>=1.1.1,<1.7.0',
+ 'websockets>=10.0,<11.0']
 
 extras_require = \
 {':python_full_version >= "3.7.0" and python_full_version < "3.8.0"': ['dask==2022.2.0',
                                                                        'numpy>=1.19.2,<1.22.0',
                                                                        'scipy>=1.4.1,<1.8.0',
                                                                        'scikit-learn>=0.22,<1.1'],
  ':python_version >= "3.8" and python_version < "3.11"': ['dask==2022.10.2',
                                                           'numpy>=1.19.2,<1.25.0',
                                                           'scipy>=1.4.1,<1.9.0',
                                                           'scikit-learn>=0.22,<1.2'],
- ':sys_platform != "darwin" or platform_machine != "arm64"': ['tensorflow>=2.11.0,<2.12.0'],
- ':sys_platform != "win32" and platform_machine != "arm64"': ['tensorflow-text>=2.11.0,<2.12.0'],
+ ':sys_platform != "darwin" or platform_machine != "arm64"': ['tensorflow==2.11.0'],
+ ':sys_platform != "win32" and platform_machine != "arm64"': ['tensorflow-text==2.11.0'],
  ':sys_platform == "darwin" and platform_machine == "arm64"': ['tensorflow-macos==2.11.0'],
- ':sys_platform == "linux" and (platform_machine == "arm64" or platform_machine == "aarch64")': ['tensorflow-cpu-aws>=2.11.0,<2.12.0'],
- ':sys_platform == "win32"': ['tensorflow-intel>=2.11.0,<2.12.0',
+ ':sys_platform == "linux" and (platform_machine == "arm64" or platform_machine == "aarch64")': ['tensorflow-cpu-aws==2.11.0'],
+ ':sys_platform == "win32"': ['tensorflow-intel==2.11.0',
                               'colorama>=0.4.4,<0.5.0'],
  'full': ['transformers>=4.13.0,<=4.26.0',
           'sentencepiece[sentencepiece]>=0.1.96,<0.2.0',
           'jieba>=0.39,<0.43'],
  'full:sys_platform != "darwin" or platform_machine != "arm64"': ['spacy>=3.1,<3.5',
                                                                   'spacy>=3.1,<3.5'],
  'full:sys_platform == "darwin" and platform_machine == "arm64"': ['spacy>=3.4,<4.0',
@@ -154,15 +155,15 @@
                   'sentencepiece[sentencepiece]>=0.1.96,<0.2.0']}
 
 entry_points = \
 {'console_scripts': ['rasa = rasa.__main__:main']}
 
 setup_kwargs = {
     'name': 'rasa',
-    'version': '3.5.3',
+    'version': '3.5.4',
     'description': 'Open source machine learning framework to automate text- and voice-based conversations: NLU, dialogue management, connect to Slack, Facebook, and more - Create chatbots and voice assistants',
     'long_description': '<h1 align="center">Rasa Open Source</h1>\n\n<div align="center">\n\n[![Join the chat on Rasa Community Forum](https://img.shields.io/badge/forum-join%20discussions-brightgreen.svg)](https://forum.rasa.com/?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)\n[![PyPI version](https://badge.fury.io/py/rasa.svg)](https://badge.fury.io/py/rasa)\n[![Supported Python Versions](https://img.shields.io/pypi/pyversions/rasa.svg)](https://pypi.python.org/pypi/rasa)\n[![Build Status](https://github.com/RasaHQ/rasa/workflows/Continuous%20Integration/badge.svg)](https://github.com/RasaHQ/rasa/actions)\n[![Coverage Status](https://api.codeclimate.com/v1/badges/756dc6fea1d5d3e127f7/test_coverage)](https://codeclimate.com/github/RasaHQ/rasa/)\n[![Documentation Status](https://img.shields.io/badge/docs-stable-brightgreen.svg)](https://rasa.com/docs)\n![Documentation Build](https://img.shields.io/netlify/d2e447e4-5a5e-4dc7-be5d-7c04ae7ff706?label=Documentation%20Build)\n[![FOSSA Status](https://app.fossa.com/api/projects/custom%2B8141%2Fgit%40github.com%3ARasaHQ%2Frasa.git.svg?type=shield)](https://app.fossa.com/projects/custom%2B8141%2Fgit%40github.com%3ARasaHQ%2Frasa.git?ref=badge_shield)\n[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/orgs/RasaHQ/projects/23)\n\n</div>\n\n<hr />\n\n💡 **We\'re migrating issues to Jira** 💡\n\nStarting January 2023, issues for Rasa Open Source are located in\n[this Jira board](https://rasa-open-source.atlassian.net/browse/OSS). You can browse issues without being logged in;\nif you want to create issues, you\'ll need to create a Jira account.\n\n<hr />\n\n<img align="right" height="255" src="https://www.rasa.com/assets/img/sara/sara-open-source-2.0.png" alt="An image of Sara, the Rasa mascot bird, holding a flag that reads Open Source with one wing, and a wrench in the other" title="Rasa Open Source">\n\nRasa is an open source machine learning framework to automate text and voice-based conversations. With Rasa, you can build contextual assistants on:\n- Facebook Messenger\n- Slack\n- Google Hangouts\n- Webex Teams\n- Microsoft Bot Framework\n- Rocket.Chat\n- Mattermost\n- Telegram\n- Twilio\n- Your own custom conversational channels\n\nor voice assistants as:\n- Alexa Skills\n- Google Home Actions\n\nRasa helps you build contextual assistants capable of having layered conversations with\nlots of back-and-forth. In order for a human to have a meaningful exchange with a contextual\nassistant, the assistant needs to be able to use context to build on things that were previously\ndiscussed – Rasa enables you to build assistants that can do this in a scalable way.\n\nThere\'s a lot more background information in this\n[blog post](https://medium.com/rasa-blog/a-new-approach-to-conversational-software-2e64a5d05f2a).\n\n---\n- 🤔 [Learn more about Rasa](https://rasa.community/)\n\n- 🤓 [Read The Docs](https://rasa.com/docs/rasa/)\n\n- 😁 [Install Rasa](https://rasa.com/docs/rasa/installation/environment-set-up)\n\n- 🚀 [Dive deeper in the learning center](https://learning.rasa.com/)\n\n- 🤗 [Contribute](#how-to-contribute)\n\n- ❓ [Get enterprise-grade support](https://rasa.com/support/)\n\n- 🏢 [Explore the features of our commercial platform](https://rasa.com/product/rasa-platform/)\n\n- 📚 [Learn more about research papers that leverage Rasa](https://scholar.google.com/scholar?oi=bibs&hl=en&authuser=1&cites=16243802403383697687,353275993797024115,14567308604105196228,9067977709825839723,9855847065463746011&as_sdt=5)\n\n\n\n---\n## Where to get help\n\nThere is extensive documentation in the [Rasa Docs](https://rasa.com/docs/rasa).\nMake sure to select the correct version so you are looking at\nthe docs for the version you installed.\n\nPlease use [Rasa Community Forum](https://forum.rasa.com) for quick answers to\nquestions.\n\n### README Contents:\n- [How to contribute](#how-to-contribute)\n- [Development Internals](#development-internals)\n- [Releases](#releases)\n- [License](#license)\n\n### How to contribute\nWe are very happy to receive and merge your contributions into this repository!\n\nTo contribute via pull request, follow these steps:\n\n1. Create an issue describing the feature you want to work on (or\n   have a look at the [contributor board](https://github.com/orgs/RasaHQ/projects/23))\n2. Write your code, tests and documentation, and format them with ``black``\n3. Create a pull request describing your changes\n\nFor more detailed instructions on how to contribute code, check out these [code contributor guidelines](CONTRIBUTING.md).\n\nYou can find more information about how to contribute to Rasa (in lots of\ndifferent ways!) [on our website.](http://rasa.community).\n\nYour pull request will be reviewed by a maintainer, who will get\nback to you about any necessary changes or questions. You will\nalso be asked to sign a\n[Contributor License Agreement](https://cla-assistant.io/RasaHQ/rasa).\n\n\n## Development Internals\n\n### Installing Poetry\n\nRasa uses Poetry for packaging and dependency management. If you want to build it from source,\nyou have to install Poetry first. Please follow\n[the official guide](https://python-poetry.org/docs/#installation) to see all possible options.\n\n### Managing environments\n\nThe official [Poetry guide](https://python-poetry.org/docs/managing-environments/) suggests to use\n[pyenv](https://github.com/pyenv/pyenv) or any other similar tool to easily switch between Python versions.\nThis is how it can be done:\n\n```bash\npyenv install 3.7.9\npyenv local 3.7.9  # Activate Python 3.7.9 for the current project\n```\n*Note*: If you have trouble installing a specific version of python on your system\nit might be worth trying other supported versions.\n\nBy default, Poetry will try to use the currently activated Python version to create the virtual environment\nfor the current project automatically. You can also create and activate a virtual environment manually — in this\ncase, Poetry should pick it up and use it to install the dependencies. For example:\n\n```bash\npython -m venv .venv\nsource .venv/bin/activate\n```\n\nYou can make sure that the environment is picked up by executing\n\n```bash\npoetry env info\n```\n\n### Building from source\n\nTo install dependencies and `rasa` itself in editable mode execute\n\n```bash\nmake install\n```\n\n*Note for macOS users*: under macOS Big Sur we\'ve seen some compiler issues for\ndependencies. Using `export SYSTEM_VERSION_COMPAT=1` before the installation helped.\n\n\n#### Installing optional dependencies\n\nIn order to install rasa\'s optional dependencies, you need to run:\n\n```bash\nmake install-full\n```\n\n*Note for macOS users*: The command `make install-full` could result in a failure while installing `tokenizers`\n(issue described in depth [here](https://github.com/huggingface/tokenizers/issues/1050)).\n\nIn order to resolve it, you must follow these steps to install a Rust compiler:\n```bash\nbrew install rustup\nrustup-init\n```\n\nAfter initialising the Rust compiler, you should restart the console and check its installation:\n```bash\nrustc --version\n```\n\nIn case the PATH variable had not been automatically setup, run:\n```bash\nexport PATH="$HOME/.cargo/bin:$PATH"\n```\n\n\n### Running and changing the documentation\n\nFirst of all, install all the required dependencies:\n\n```bash\nmake install install-docs\n```\n\nAfter the installation has finished, you can run and view the documentation\nlocally using:\n\n```bash\nmake livedocs\n```\n\nIt should open a new tab with the local version of the docs in your browser;\nif not, visit http://localhost:3000 in your browser.\nYou can now change the docs locally and the web page will automatically reload\nand apply your changes.\n\n### Running the Tests\n\nIn order to run the tests, make sure that you have the development requirements installed:\n\n```bash\nmake prepare-tests-ubuntu # Only on Ubuntu and Debian based systems\nmake prepare-tests-macos  # Only on macOS\n```\n\nThen, run the tests:\n\n```bash\nmake test\n```\n\nThey can also be run at multiple jobs to save some time:\n\n```bash\nJOBS=[n] make test\n```\n\nWhere `[n]` is the number of jobs desired. If omitted, `[n]` will be automatically chosen by pytest.\n\n\n### Running the Integration Tests\n\nIn order to run the integration tests, make sure that you have the development requirements installed:\n\n```bash\nmake prepare-tests-ubuntu # Only on Ubuntu and Debian based systems\nmake prepare-tests-macos  # Only on macOS\n```\n\nThen, you\'ll need to start services with the following command which uses\n[Docker Compose](https://docs.docker.com/compose/install/):\n\n```bash\nmake run-integration-containers\n```\n\nFinally, you can run the integration tests like this:\n\n```bash\nmake test-integration\n```\n\n\n### Resolving merge conflicts\n\nPoetry doesn\'t include any solution that can help to resolve merge conflicts in\nthe lock file `poetry.lock` by default.\nHowever, there is a great tool called [poetry-merge-lock](https://poetry-merge-lock.readthedocs.io/en/latest/).\nHere is how you can install it:\n\n```bash\npip install poetry-merge-lock\n```\n\nJust execute this command to resolve merge conflicts in `poetry.lock` automatically:\n\n```bash\npoetry-merge-lock\n```\n\n### Build a Docker image locally\n\nIn order to build a Docker image on your local machine execute the following command:\n\n```bash\nmake build-docker\n```\n\nThe Docker image is available on your local machine as `rasa:localdev`.\n\n### Code Style\n\nTo ensure a standardized code style we use the formatter [black](https://github.com/ambv/black).\nTo ensure our type annotations are correct we use the type checker [pytype](https://github.com/google/pytype).\nIf your code is not formatted properly or doesn\'t type check, GitHub will fail to build.\n\n#### Formatting\n\nIf you want to automatically format your code on every commit, you can use [pre-commit](https://pre-commit.com/).\nJust install it via `pip install pre-commit` and execute `pre-commit install` in the root folder.\nThis will add a hook to the repository, which reformats files on every commit.\n\nIf you want to set it up manually, install black via `poetry install`.\nTo reformat files execute\n```\nmake formatter\n```\n\n#### Type Checking\n\nIf you want to check types on the codebase, install `mypy` using `poetry install`.\nTo check the types execute\n```\nmake types\n```\n\n### Deploying documentation updates\n\nWe use `Docusaurus v2` to build docs for tagged versions and for the `main` branch.\nThe static site that gets built is pushed to the `documentation` branch of this repo.\n\nWe host the site on netlify. On `main` branch builds (see `.github/workflows/documentation.yml`), we push the built docs to\nthe `documentation` branch. Netlify automatically re-deploys the docs pages whenever there is a change to that branch.\n\n## Releases\nRasa has implemented robust policies governing version naming, as well as release pace for major, minor, and patch releases.\n\nThe values for a given version number (MAJOR.MINOR.PATCH) are incremented as follows:\n- MAJOR version for incompatible API changes or other breaking changes.\n- MINOR version for functionality added in a backward compatible manner.\n- PATCH version for backward compatible bug fixes.\n\nThe following table describes the version types and their expected *release cadence*:\n\n| Version Type |                                                                  Description                                                                  |  Target Cadence |\n|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------|\n| Major        | For significant changes, or when any backward-incompatible changes are introduced to the API or data model.                                   | Every 1 - 2 yrs |\n| Minor        | For when new backward-compatible functionality is introduced, a minor feature is introduced, or when a set of smaller features is rolled out. | +/- Quarterly   |\n| Patch        | For backward-compatible bug fixes that fix incorrect behavior.                                                                                | As needed       |\n\nWhile this table represents our target release frequency, we reserve the right to modify it based on changing market conditions and technical requirements.\n\n### Maintenance Policy\nOur End of Life policy defines how long a given release is considered supported, as well as how long a release is\nconsidered to be still in active development or maintenance.\n\nThe maintentance duration and end of life for every release are shown on our website as part of the [Product Release and Maintenance Policy](https://rasa.com/rasa-product-release-and-maintenance-policy/).\n\n### Cutting a Major / Minor release\n#### A week before release day\n\n1. **Make sure the [milestone](https://github.com/RasaHQ/rasa/milestones) already exists and is scheduled for the\ncorrect date.**\n2. **Take a look at the issues & PRs that are in the milestone**: does it look about right for the release highlights\nwe are planning to ship? Does it look like anything is missing? Don\'t worry about being aware of every PR that should\nbe in, but it\'s useful to take a moment to evaluate what\'s assigned to the milestone.\n3. **Post a message on the engineering Slack channel**, letting the team know you\'ll be the one cutting the upcoming\nrelease, as well as:\n    1. Providing the link to the appropriate milestone\n    2. Reminding everyone to go over their issues and PRs and please assign them to the milestone\n    3. Reminding everyone of the scheduled date for the release\n\n#### A day before release day\n\n1. **Go over the milestone and evaluate the status of any PR merging that\'s happening. Follow up with people on their\nbugs and fixes.** If the release introduces new bugs or regressions that can\'t be fixed in time, we should discuss on\nSlack about this and take a decision on how to move forward. If the issue is not ready to be merged in time, we remove the issue / PR from the milestone and notify the PR owner and the product manager on Slack about it. The PR / issue owners are responsible for\ncommunicating any issues which might be release relevant. Postponing the release should be considered as an edge case scenario.\n\n#### Release day! 🚀\n\n1. **At the start of the day, post a small message on slack announcing release day!** Communicate you\'ll be handling\nthe release, and the time you\'re aiming to start releasing (again, no later than 4pm, as issues may arise and\ncause delays). This message should be posted early in the morning and before moving forward with any of the steps of the release,\n   in order to give enough time to people to check their PRs and issues. That way they can plan any remaining work. A template of the slack message can be found [here](https://rasa-hq.slack.com/archives/C36SS4N8M/p1613032208137500?thread_ts=1612876410.068400&cid=C36SS4N8M).\n   The release time should be communicated transparently so that others can plan potentially necessary steps accordingly. If there are bigger changes this should be communicated.\n2. Make sure the milestone is empty (everything has been either merged or moved to the next milestone)\n3. Once everything in the milestone is taken care of, post a small message on Slack communicating you are about to\nstart the release process (in case anything is missing).\n4. **You may now do the release by following the instructions outlined in the\n[Rasa Open Source README](#steps-to-release-a-new-version) !**\n\n#### After a Major release\n\nAfter a Major release has been completed, please follow [these instructions to complete the documentation update](./docs/README.md#manual-steps-after-a-new-version).\n\n### Steps to release a new version\nReleasing a new version is quite simple, as the packages are build and distributed by GitHub Actions.\n\n*Release steps*:\n1. Make sure all dependencies are up to date (**especially Rasa SDK**)\n    - For Rasa SDK, except in the case of a patch release, that means first creating a [new Rasa SDK release](https://github.com/RasaHQ/rasa-sdk#steps-to-release-a-new-version) (make sure the version numbers between the new Rasa and Rasa SDK releases match)\n    - Once the tag with the new Rasa SDK release is pushed and the package appears on [pypi](https://pypi.org/project/rasa-sdk/), the dependency in the rasa repository can be resolved (see below).\n2. If this is a minor / major release: Make sure all fixes from currently supported minor versions have been merged from their respective release branches (e.g. 3.3.x) back into main.\n3. In case of a minor release, create a new branch that corresponds to the new release, e.g.\n   ```bash\n    git checkout -b 1.2.x\n    git push origin 1.2.x\n    ```\n4. Switch to the branch you want to cut the release from (`main` in case of a major, the `<major>.<minor>.x` branch for minors and patches)\n    - Update the `rasa-sdk` entry in `pyproject.toml` with the new release version and run `poetry update`. This creates a new `poetry.lock` file with all dependencies resolved.\n    - Commit the changes with `git commit -am "bump rasa-sdk dependency"` but do not push them. They will be automatically picked up by the following step.\n5. If this is a major release, update the list of actively maintained versions [in the README](#actively-maintained-versions) and in [the docs](./docs/docs/actively-maintained-versions.mdx).\n6. Run `make release`\n7. Create a PR against the release branch (e.g. `1.2.x`)\n8. Once your PR is merged, tag a new release (this SHOULD always happen on the release branch), e.g. using\n    ```bash\n    git checkout 1.2.x\n    git pull origin 1.2.x\n    git tag 1.2.0 -m "next release"\n    git push origin 1.2.0 --tags\n    ```\n    GitHub will build this tag and publish the build artifacts.\n9. After all the steps are completed and if everything goes well then we should see a message automatically posted in the company\'s Slack (`product` channel) like this [one](https://rasa-hq.slack.com/archives/C7B08Q5FX/p1614354499046600)\n10. If no message appears in the channel then you can do the following checks:\n    - Check the workflows in [Github Actions](https://github.com/RasaHQ/rasa/actions) and make sure that the merged PR of the current release is completed successfully. To easily find your PR you can use the filters `event: push` and `branch: <version number>` (example on release 2.4 you can see [here](https://github.com/RasaHQ/rasa/actions/runs/643344876))\n    - If the workflow is not completed, then try to re run the workflow in case that solves the problem\n    - If the problem persists, check also the log files and try to find the root cause of the issue\n    - If you still cannot resolve the error, contact the infrastructure team by providing any helpful information from your investigation\n11.  After the message is posted correctly in the `product` channel, check also in the `product-engineering-alerts` channel if there are any alerts related to the Rasa Open Source release like this [one](https://rasa-hq.slack.com/archives/C01585AN2NP/p1615486087001000)\n\n### Cutting a Patch release\n\nPatch releases are simpler to cut, since they are meant to contain only bugfixes.\n\n**The only things you need to do to cut a patch release are:**\n\n1. Notify the engineering team on Slack that you are planning to cut a patch, in case someone has an important fix\nto add.\n2. Make sure the bugfix(es) are in the release branch you will use (p.e if you are cutting a `2.0.4` patch, you will\nneed your fixes to be on the `2.0.x` release branch). All patch releases must come from a `.x` branch!\n3. Once you\'re ready to release the Rasa Open Source patch, checkout the branch, run `make release` and follow the\nsteps + get the PR merged.\n4. Once the PR is in, pull the `.x` branch again and push the tag!\n\n### Actively maintained versions\n\nWe\'re actively maintaining _any minor on our latest major release_ and _the latest minor of the previous major release_.\nCurrently, this means the following minor versions will receive bugfixes updates:\n- 2.8\n- Every minor version on 3.x\n\n## License\nLicensed under the Apache License, Version 2.0.\nCopyright 2022 Rasa Technologies GmbH. [Copy of the license](LICENSE.txt).\n\nA list of the Licenses of the dependencies of the project can be found at\nthe bottom of the\n[Libraries Summary](https://libraries.io/github/RasaHQ/rasa).\n',
     'author': 'Rasa Technologies GmbH',
     'author_email': 'hi@rasa.com',
     'maintainer': 'Tom Bocklisch',
     'maintainer_email': 'tom@rasa.com',
     'url': 'https://rasa.com',
```

### Comparing `rasa-3.5.3/PKG-INFO` & `rasa-3.5.4/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rasa
-Version: 3.5.3
+Version: 3.5.4
 Summary: Open source machine learning framework to automate text- and voice-based conversations: NLU, dialogue management, connect to Slack, Facebook, and more - Create chatbots and voice assistants
 Home-page: https://rasa.com
 License: Apache-2.0
 Keywords: nlp,machine-learning,machine-learning-library,bot,bots,botkit,rasa conversational-agents,conversational-ai,chatbot,chatbot-framework,bot-framework
 Author: Rasa Technologies GmbH
 Author-email: hi@rasa.com
 Maintainer: Tom Bocklisch
@@ -25,15 +25,15 @@
 Provides-Extra: metal
 Provides-Extra: spacy
 Provides-Extra: transformers
 Requires-Dist: CacheControl (>=0.12.9,<0.13.0)
 Requires-Dist: PyJWT[crypto] (>=2.0.0,<3.0.0)
 Requires-Dist: SQLAlchemy (>=1.4.0,<1.5.0)
 Requires-Dist: absl-py (>=0.9,<1.4)
-Requires-Dist: aio-pika (>=6.7.1,<9.0.0)
+Requires-Dist: aio-pika (>=6.7.1,<8.2.4)
 Requires-Dist: aiogram (<2.26)
 Requires-Dist: aiohttp (>=3.6,!=3.7.4.post0,<3.9)
 Requires-Dist: apscheduler (>=3.6,<3.10)
 Requires-Dist: attrs (>=19.3,<22.2)
 Requires-Dist: boto3 (>=1.12,<2.0)
 Requires-Dist: cloudpickle (>=1.2,<2.3)
 Requires-Dist: colorama (>=0.4.4,<0.5.0); sys_platform == "win32"
@@ -67,15 +67,15 @@
 Requires-Dist: python-dateutil (>=2.8,<2.9)
 Requires-Dist: python-engineio (>=4,<6,!=5.0.0)
 Requires-Dist: python-socketio (>=4.4,<6)
 Requires-Dist: pytz (>=2019.1,<2023.0)
 Requires-Dist: questionary (>=1.5.1,<1.11.0)
 Requires-Dist: randomname (>=0.1.5,<0.2.0)
 Requires-Dist: rasa-sdk (>=3.5.0,<3.6.0)
-Requires-Dist: redis (>=3.4,<5.0)
+Requires-Dist: redis (>=4.5.3,<5.0)
 Requires-Dist: regex (>=2020.6,<2022.11)
 Requires-Dist: requests (>=2.23,<3.0)
 Requires-Dist: rocketchat_API (>=0.6.31,<1.29.0)
 Requires-Dist: ruamel.yaml (>=0.16.5,<0.18.0)
 Requires-Dist: sanic (>=21.12,<21.13)
 Requires-Dist: sanic-cors (>=2.0.0,<2.1.0)
 Requires-Dist: sanic-jwt (>=1.6.0,<2.0.0)
@@ -88,30 +88,31 @@
 Requires-Dist: sentry-sdk (>=0.17.0,<1.15.0)
 Requires-Dist: setuptools (>=41.0.0)
 Requires-Dist: sklearn-crfsuite (>=0.3,<0.4)
 Requires-Dist: slack-sdk (>=3.19.2,<4.0.0)
 Requires-Dist: spacy (>=3.1,<3.5); (sys_platform != "darwin" or platform_machine != "arm64") and (extra == "spacy" or extra == "full")
 Requires-Dist: spacy (>=3.4,<4.0); (sys_platform == "darwin" and platform_machine == "arm64") and (extra == "spacy" or extra == "full")
 Requires-Dist: tarsafe (>=0.0.3,<0.0.4)
-Requires-Dist: tensorflow (>=2.11.0,<2.12.0); sys_platform != "darwin" or platform_machine != "arm64"
+Requires-Dist: tensorflow (==2.11.0); sys_platform != "darwin" or platform_machine != "arm64"
 Requires-Dist: tensorflow-addons (>=0.18,<0.20)
-Requires-Dist: tensorflow-cpu-aws (>=2.11.0,<2.12.0); sys_platform == "linux" and (platform_machine == "arm64" or platform_machine == "aarch64")
-Requires-Dist: tensorflow-intel (>=2.11.0,<2.12.0); sys_platform == "win32"
+Requires-Dist: tensorflow-cpu-aws (==2.11.0); sys_platform == "linux" and (platform_machine == "arm64" or platform_machine == "aarch64")
+Requires-Dist: tensorflow-intel (==2.11.0); sys_platform == "win32"
 Requires-Dist: tensorflow-macos (==2.11.0); sys_platform == "darwin" and platform_machine == "arm64"
 Requires-Dist: tensorflow-metal (==0.5.1); (sys_platform == "darwin" and platform_machine == "arm64") and (extra == "metal")
-Requires-Dist: tensorflow-text (>=2.11.0,<2.12.0); sys_platform != "win32" and platform_machine != "arm64"
+Requires-Dist: tensorflow-text (==2.11.0); sys_platform != "win32" and platform_machine != "arm64"
 Requires-Dist: tensorflow_hub (>=0.12.0,<0.13.0)
 Requires-Dist: terminaltables (>=3.1.0,<3.2.0)
 Requires-Dist: tqdm (>=4.31,<5.0)
 Requires-Dist: transformers (>=4.13.0,<=4.26.0); extra == "transformers" or extra == "full"
 Requires-Dist: twilio (>=6.26,<7.15)
 Requires-Dist: typing-extensions (>=4.1.1,<5.0.0)
 Requires-Dist: typing-utils (>=0.1.0,<0.2.0)
 Requires-Dist: ujson (>=1.35,<6.0)
 Requires-Dist: webexteamssdk (>=1.1.1,<1.7.0)
+Requires-Dist: websockets (>=10.0,<11.0)
 Project-URL: Documentation, https://rasa.com/docs
 Project-URL: Repository, https://github.com/rasahq/rasa
 Description-Content-Type: text/markdown
 
 <h1 align="center">Rasa Open Source</h1>
 
 <div align="center">
```

