# Comparing `tmp/edwh_restic_plugin-0.1.0.tar.gz` & `tmp/edwh_restic_plugin-0.1.1.tar.gz`

## Comparing `edwh_restic_plugin-0.1.0.tar` & `edwh_restic_plugin-0.1.1.tar`

### file list

```diff
@@ -1,59 +1,59 @@
--rw-r--r--   0        0        0      553 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/.env
--rw-r--r--   0        0        0       18 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/README.md
--rw-r--r--   0        0        0     1474 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/docker-compose.yml
--rw-r--r--   0        0        0      590 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/init_setup.sh
--rw-r--r--   0        0        0      155 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/b2/edwh-backup-test/backup-testapplication/config
--rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/b2/edwh-backup-test/backup-testapplication/keys/c478566461172905eccfdbcae6dc998ca254ecfe9df93e83ff34ad56541376e7
--rw-r--r--   0        0        0      155 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup-testapplication/config
--rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup-testapplication/keys/c23d582a6200d01d036c9306375dd8b4d29af639e5652845ffd1425a26eb2d18
--rw-r--r--   0        0        0      155 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/config
--rw-r--r--   0        0        0      410 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/data/17/179c7738522485b9492ee2497fd2fbdd8e70bd355f2b9414189f9b2f0bbd78fe
--rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/data/2a/2a9a28749c08e8e50b7fa16e60e828dd28e7c8a33faeaf07107a2b04573e3ade
--rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/data/2c/2c558eaaab62dc034164cb3fc9c32cf108141aa287b1aa09089979a8597720fc
--rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/data/5b/5bd380c6acf0811fd7f88d703a601200958b5958b207eea99276889184ff56b2
--rw-r--r--   0        0        0      109 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/data/6c/6cb2fe6bda65a60fa99dea7f8d1963f7aab7441c20f05e724c051122e913b4a5
--rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/data/94/948414318785a325373e30c2b395245ac66859ffa924e1a197eec5d6b6ce19c1
--rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/data/b1/b1e6c0ec5d9c7fa036614ac6ba4a7ce563b3aeadac7cd3c618a744b529a7ccac
--rw-r--r--   0        0        0      407 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/data/c4/c471141549f29b81b2d633657258bf78974eddf4405fc63b804b404e81def891
--rw-r--r--   0        0        0      117 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/data/cd/cd57dae9e1f907c8620c7a4ef796aa6f4345133f36f9e6baf3e851923df19bcf
--rw-r--r--   0        0        0      141 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/data/de/dede3d5b53f1fc272b2c43ac3bb944dbb44c600abaeb9907d53aef216088c18d
--rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/data/f1/f16a53bbc6937701666485ad5c1b27944550439bc6bfe013ee0c17c81d0cc79d
--rw-r--r--   0        0        0      435 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/index/2e9f9bd3dbac4b6fcf559be5e79a17b80870f12d70833d25ab234f3ce5bde2b5
--rw-r--r--   0        0        0      240 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/index/345bb728ded155b0024e1e43e630b69e2b24f1b5cc5b94d381a125392a8ca333
--rw-r--r--   0        0        0      435 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/index/60d6718f6b0826a7d4e32336a0df8ca363a069db760583ab9bd2991d93c3a26e
--rw-r--r--   0        0        0      240 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/index/b0c7314b6cccbff38a9de3c76ecdadd41b31a2dd7341d02367dd97c971d71b8e
--rw-r--r--   0        0        0      435 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/index/b63a3413e88d25d9d7a7f621c7ae19c4fbee01387227c1a5609f8587adce2e0c
--rw-r--r--   0        0        0      240 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/index/cdadd5d27853a715eefe24ff021757f057ba9427695fdb5966a716a7414fe5ca
--rw-r--r--   0        0        0      240 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/index/dc3d219839d964c77d338aa2c57c47cba99fdf228c0d6fae2712261690bbc63d
--rw-r--r--   0        0        0      240 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/index/e620ce7d15942886c9e6bc2b6c1fe1fa94abf459511939970902d63d043dabcf
--rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/keys/7aa0b0f309774b9f50b1815876d7d209883a3871af3cd6dacd0e01a59cd366d0
--rw-r--r--   0        0        0      332 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/snapshots/0732d073c4d1472182138abed6678e816ae26dfa23a3f0cdb6846e6e75f810eb
--rw-r--r--   0        0        0      256 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/snapshots/2fd78da7ecad3601ffd6d65d3a80a15677a4cd3b7a707a48b606e5958efcf852
--rw-r--r--   0        0        0      332 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/snapshots/71cde9e83949215467674538aa7f2db6855a0226a6e7e7a69bb2b76814c0911d
--rw-r--r--   0        0        0      332 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/snapshots/bce9095d5e93309c557d51e1936ff43cb32a13e48fa91d94d177a933e5222402
--rw-r--r--   0        0        0      332 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/snapshots/d4605772b65f85628fa57a794c31750770dc0b4d6c1beff42aaf5ce8863dcd4e
--rw-r--r--   0        0        0      339 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/snapshots/d845dc99d7fdfd3c2b6aad7c61b127ee0aa7cd75a22515774358855554c02f52
--rw-r--r--   0        0        0      332 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/snapshots/e21355a8d91ec8450d646758deb64f5dfbcdc95278ffcb894f39be4effb1e213
--rw-r--r--   0        0        0      340 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/backup_test/snapshots/e2766b0a431988be73c17ff21d7612501a6df58c047532790ad4e46547a02c02
--rwxr-xr-x   0        0        0      120 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/captain-hooks/backup_files_pg.sh
--rwxr-xr-x   0        0        0      181 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/captain-hooks/backup_files_sql.sh
--rwxr-xr-x   0        0        0      279 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/captain-hooks/backup_stream_sql.sh
--rwxr-xr-x   0        0        0       69 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/captain-hooks/restore_stream_pg.sh
--rwxr-xr-x   0        0        0       77 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/captain-hooks/restore_stream_sql.sh
--rw-r--r--   0        0        0      590 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/recover_data/init_setup.sh
--rwxr-xr-x   0        0        0       24 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/recover_data/captain-hooks/backup_files.sh
--rwxr-xr-x   0        0        0       74 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/recover_data/captain-hooks/backup_files_pg.sh
--rwxr-xr-x   0        0        0        0 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/recover_data/captain-hooks/backup_files_sql.sh
--rwxr-xr-x   0        0        0        0 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/recover_data/captain-hooks/backup_stream_pg.sh
--rwxr-xr-x   0        0        0        0 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/recover_data/captain-hooks/backup_stream_sql.sh
--rwxr-xr-x   0        0        0       69 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/recover_data/captain-hooks/restore_stream_pg.sh
--rwxr-xr-x   0        0        0       28 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/examples/recover_data/captain-hooks/restore_stream_sql.sh
--rw-r--r--   0        0        0      139 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/src/edwh_restic_plugin/__about__.py
--rw-r--r--   0        0        0      117 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/src/edwh_restic_plugin/__init__.py
--rw-r--r--   0        0        0    23449 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/src/edwh_restic_plugin/tasks.py
--rw-r--r--   0        0        0      117 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/tests/__init__.py
--rw-r--r--   0        0        0       12 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/.gitignore
--rw-r--r--   0        0        0     1109 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/LICENSE.txt
--rw-r--r--   0        0        0     2844 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/README.md
--rw-r--r--   0        0        0     3322 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/pyproject.toml
--rw-r--r--   0        0        0     3802 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.0/PKG-INFO
+-rw-r--r--   0        0        0      553 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/.env
+-rw-r--r--   0        0        0       18 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/README.md
+-rw-r--r--   0        0        0     1474 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/docker-compose.yml
+-rw-r--r--   0        0        0      590 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/init_setup.sh
+-rw-r--r--   0        0        0      155 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/b2/edwh-backup-test/backup-testapplication/config
+-rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/b2/edwh-backup-test/backup-testapplication/keys/c478566461172905eccfdbcae6dc998ca254ecfe9df93e83ff34ad56541376e7
+-rw-r--r--   0        0        0      155 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup-testapplication/config
+-rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup-testapplication/keys/c23d582a6200d01d036c9306375dd8b4d29af639e5652845ffd1425a26eb2d18
+-rw-r--r--   0        0        0      155 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/config
+-rw-r--r--   0        0        0      410 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/data/17/179c7738522485b9492ee2497fd2fbdd8e70bd355f2b9414189f9b2f0bbd78fe
+-rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/data/2a/2a9a28749c08e8e50b7fa16e60e828dd28e7c8a33faeaf07107a2b04573e3ade
+-rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/data/2c/2c558eaaab62dc034164cb3fc9c32cf108141aa287b1aa09089979a8597720fc
+-rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/data/5b/5bd380c6acf0811fd7f88d703a601200958b5958b207eea99276889184ff56b2
+-rw-r--r--   0        0        0      109 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/data/6c/6cb2fe6bda65a60fa99dea7f8d1963f7aab7441c20f05e724c051122e913b4a5
+-rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/data/94/948414318785a325373e30c2b395245ac66859ffa924e1a197eec5d6b6ce19c1
+-rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/data/b1/b1e6c0ec5d9c7fa036614ac6ba4a7ce563b3aeadac7cd3c618a744b529a7ccac
+-rw-r--r--   0        0        0      407 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/data/c4/c471141549f29b81b2d633657258bf78974eddf4405fc63b804b404e81def891
+-rw-r--r--   0        0        0      117 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/data/cd/cd57dae9e1f907c8620c7a4ef796aa6f4345133f36f9e6baf3e851923df19bcf
+-rw-r--r--   0        0        0      141 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/data/de/dede3d5b53f1fc272b2c43ac3bb944dbb44c600abaeb9907d53aef216088c18d
+-rw-r--r--   0        0        0      413 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/data/f1/f16a53bbc6937701666485ad5c1b27944550439bc6bfe013ee0c17c81d0cc79d
+-rw-r--r--   0        0        0      435 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/index/2e9f9bd3dbac4b6fcf559be5e79a17b80870f12d70833d25ab234f3ce5bde2b5
+-rw-r--r--   0        0        0      240 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/index/345bb728ded155b0024e1e43e630b69e2b24f1b5cc5b94d381a125392a8ca333
+-rw-r--r--   0        0        0      435 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/index/60d6718f6b0826a7d4e32336a0df8ca363a069db760583ab9bd2991d93c3a26e
+-rw-r--r--   0        0        0      240 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/index/b0c7314b6cccbff38a9de3c76ecdadd41b31a2dd7341d02367dd97c971d71b8e
+-rw-r--r--   0        0        0      435 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/index/b63a3413e88d25d9d7a7f621c7ae19c4fbee01387227c1a5609f8587adce2e0c
+-rw-r--r--   0        0        0      240 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/index/cdadd5d27853a715eefe24ff021757f057ba9427695fdb5966a716a7414fe5ca
+-rw-r--r--   0        0        0      240 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/index/dc3d219839d964c77d338aa2c57c47cba99fdf228c0d6fae2712261690bbc63d
+-rw-r--r--   0        0        0      240 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/index/e620ce7d15942886c9e6bc2b6c1fe1fa94abf459511939970902d63d043dabcf
+-rw-r--r--   0        0        0      449 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/keys/7aa0b0f309774b9f50b1815876d7d209883a3871af3cd6dacd0e01a59cd366d0
+-rw-r--r--   0        0        0      332 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/snapshots/0732d073c4d1472182138abed6678e816ae26dfa23a3f0cdb6846e6e75f810eb
+-rw-r--r--   0        0        0      256 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/snapshots/2fd78da7ecad3601ffd6d65d3a80a15677a4cd3b7a707a48b606e5958efcf852
+-rw-r--r--   0        0        0      332 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/snapshots/71cde9e83949215467674538aa7f2db6855a0226a6e7e7a69bb2b76814c0911d
+-rw-r--r--   0        0        0      332 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/snapshots/bce9095d5e93309c557d51e1936ff43cb32a13e48fa91d94d177a933e5222402
+-rw-r--r--   0        0        0      332 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/snapshots/d4605772b65f85628fa57a794c31750770dc0b4d6c1beff42aaf5ce8863dcd4e
+-rw-r--r--   0        0        0      339 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/snapshots/d845dc99d7fdfd3c2b6aad7c61b127ee0aa7cd75a22515774358855554c02f52
+-rw-r--r--   0        0        0      332 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/snapshots/e21355a8d91ec8450d646758deb64f5dfbcdc95278ffcb894f39be4effb1e213
+-rw-r--r--   0        0        0      340 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/backup_test/snapshots/e2766b0a431988be73c17ff21d7612501a6df58c047532790ad4e46547a02c02
+-rwxr-xr-x   0        0        0      120 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/captain-hooks/backup_files_pg.sh
+-rwxr-xr-x   0        0        0      181 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/captain-hooks/backup_files_sql.sh
+-rwxr-xr-x   0        0        0      279 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/captain-hooks/backup_stream_sql.sh
+-rwxr-xr-x   0        0        0       69 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/captain-hooks/restore_stream_pg.sh
+-rwxr-xr-x   0        0        0       77 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/captain-hooks/restore_stream_sql.sh
+-rw-r--r--   0        0        0      590 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/recover_data/init_setup.sh
+-rwxr-xr-x   0        0        0       24 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/recover_data/captain-hooks/backup_files.sh
+-rwxr-xr-x   0        0        0       74 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/recover_data/captain-hooks/backup_files_pg.sh
+-rwxr-xr-x   0        0        0        0 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/recover_data/captain-hooks/backup_files_sql.sh
+-rwxr-xr-x   0        0        0        0 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/recover_data/captain-hooks/backup_stream_pg.sh
+-rwxr-xr-x   0        0        0        0 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/recover_data/captain-hooks/backup_stream_sql.sh
+-rwxr-xr-x   0        0        0       69 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/recover_data/captain-hooks/restore_stream_pg.sh
+-rwxr-xr-x   0        0        0       28 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/examples/recover_data/captain-hooks/restore_stream_sql.sh
+-rw-r--r--   0        0        0      139 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/src/edwh_restic_plugin/__about__.py
+-rw-r--r--   0        0        0      117 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/src/edwh_restic_plugin/__init__.py
+-rw-r--r--   0        0        0    23435 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/src/edwh_restic_plugin/tasks.py
+-rw-r--r--   0        0        0      117 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/tests/__init__.py
+-rw-r--r--   0        0        0       12 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/.gitignore
+-rw-r--r--   0        0        0     1109 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/LICENSE.txt
+-rw-r--r--   0        0        0     2844 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/README.md
+-rw-r--r--   0        0        0     3322 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/pyproject.toml
+-rw-r--r--   0        0        0     3802 2020-02-02 00:00:00.000000 edwh_restic_plugin-0.1.1/PKG-INFO
```

### Comparing `edwh_restic_plugin-0.1.0/examples/.env` & `edwh_restic_plugin-0.1.1/examples/.env`

 * *Files identical despite different names*

### Comparing `edwh_restic_plugin-0.1.0/examples/docker-compose.yml` & `edwh_restic_plugin-0.1.1/examples/docker-compose.yml`

 * *Files identical despite different names*

### Comparing `edwh_restic_plugin-0.1.0/examples/init_setup.sh` & `edwh_restic_plugin-0.1.1/examples/init_setup.sh`

 * *Files identical despite different names*

### Comparing `edwh_restic_plugin-0.1.0/examples/recover_data/init_setup.sh` & `edwh_restic_plugin-0.1.1/examples/recover_data/init_setup.sh`

 * *Files identical despite different names*

### Comparing `edwh_restic_plugin-0.1.0/src/edwh_restic_plugin/tasks.py` & `edwh_restic_plugin-0.1.1/src/edwh_restic_plugin/tasks.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,19 +1,20 @@
+from collections import defaultdict, OrderedDict
+
 import invoke
-from invoke import task
+from invoke import task, run, Result, Context
+
 import datetime
 import io
 import os
+from pathlib import Path
 import re
 import sys
 import typing
 import json
-from pathlib import Path
-from collections import defaultdict, OrderedDict
-
 
 # the path where the restic command is going to be executed
 DEFAULT_BACKUP_FOLDER = Path("captain-hooks")
 # the path where the environment variables are going
 DOTENV = Path(".env")
 _dotenv_settings = {}
 
@@ -589,20 +590,20 @@
     except:
         print(f"[ERROR] while backing up to {connection_choice or 'default connection'}")
         raise
 
 
 @task
 def restore(
-        c,
-        connection_choice=None,
-        snapshot="latest",
-        target="",
-        verbose=False,
-) -> None:
+    c,
+    connection_choice=None,
+    snapshot="latest",
+    target="",
+    verbose=False
+):
     """
     IMPORTANT: please fill in -t for a path where the restore can go. Also remember to put in a -c for at what service
     you stored the backup.
 
     the restore function restores the latest backup-ed files by default and puts it into a restore folder.
     :param c: invoke
     :param connection_choice: service where the files are backed op, think about local or openstack
@@ -636,15 +637,15 @@
             c.run("docker volume rm " + volume_name)
 
     cli_repo(c, connection_choice).restore(c, verbose, target, "restore", snapshot)
     # print("`inv up` om de services te herstarten ")
 
 
 @task(iterable=['tag'])
-def snapshots(c, connection_choice=None, tag=None, n=1) -> None:
+def snapshots(c, connection_choice=None, tag=None, n=1):
     """
     With this je can see per repo which repo is made when and where, the repo-id can be used at inv restore as an option
     :param c: invoke
     :param connection_choice: service
     :param tag: files, stream ect
     :param n: amount of snapshot to view, default=1(latest)
     :return: None
```

### Comparing `edwh_restic_plugin-0.1.0/LICENSE.txt` & `edwh_restic_plugin-0.1.1/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `edwh_restic_plugin-0.1.0/README.md` & `edwh_restic_plugin-0.1.1/README.md`

 * *Files identical despite different names*

### Comparing `edwh_restic_plugin-0.1.0/pyproject.toml` & `edwh_restic_plugin-0.1.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `edwh_restic_plugin-0.1.0/PKG-INFO` & `edwh_restic_plugin-0.1.1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: edwh-restic-plugin
-Version: 0.1.0
+Version: 0.1.1
 Project-URL: Documentation, https://github.com/unknown/edwh-restic-plugin#readme
 Project-URL: Issues, https://github.com/unknown/edwh-restic-plugin/issues
 Project-URL: Source, https://github.com/unknown/edwh-restic-plugin
 Author-email: Remco Boerma <remco.b@educationwarehouse.nl>
 License-Expression: MIT
 License-File: LICENSE.txt
 Classifier: Development Status :: 4 - Beta
```

