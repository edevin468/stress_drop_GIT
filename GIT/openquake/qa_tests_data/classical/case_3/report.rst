Classical Hazard QA Test, Case 3
================================

+----------------+----------------------+
| checksum32     | 3_979_728_005        |
+----------------+----------------------+
| date           | 2021-10-31T03:19:40  |
+----------------+----------------------+
| engine_version | 3.13.0-git04a140fc38 |
+----------------+----------------------+
| input_size     | 7_486                |
+----------------+----------------------+

num_sites = 1, num_levels = 3, num_rlzs = 1

Parameters
----------
+---------------------------------+--------------------------------------------+
| parameter                       | value                                      |
+---------------------------------+--------------------------------------------+
| calculation_mode                | 'preclassical'                             |
+---------------------------------+--------------------------------------------+
| number_of_logic_tree_samples    | 0                                          |
+---------------------------------+--------------------------------------------+
| maximum_distance                | {'default': [[1.0, 200.0], [10.0, 200.0]]} |
+---------------------------------+--------------------------------------------+
| investigation_time              | 1.0                                        |
+---------------------------------+--------------------------------------------+
| ses_per_logic_tree_path         | 1                                          |
+---------------------------------+--------------------------------------------+
| truncation_level                | 0.0                                        |
+---------------------------------+--------------------------------------------+
| rupture_mesh_spacing            | 1.0                                        |
+---------------------------------+--------------------------------------------+
| complex_fault_mesh_spacing      | 1.0                                        |
+---------------------------------+--------------------------------------------+
| width_of_mfd_bin                | 1.0                                        |
+---------------------------------+--------------------------------------------+
| area_source_discretization      | 0.1                                        |
+---------------------------------+--------------------------------------------+
| pointsource_distance            | None                                       |
+---------------------------------+--------------------------------------------+
| ground_motion_correlation_model | None                                       |
+---------------------------------+--------------------------------------------+
| minimum_intensity               | {}                                         |
+---------------------------------+--------------------------------------------+
| random_seed                     | 1066                                       |
+---------------------------------+--------------------------------------------+
| master_seed                     | 123456789                                  |
+---------------------------------+--------------------------------------------+
| ses_seed                        | 42                                         |
+---------------------------------+--------------------------------------------+

Input files
-----------
+-------------------------+--------------------------------------------------------------+
| Name                    | File                                                         |
+-------------------------+--------------------------------------------------------------+
| gsim_logic_tree         | `gsim_logic_tree.xml <gsim_logic_tree.xml>`_                 |
+-------------------------+--------------------------------------------------------------+
| job_ini                 | `job.ini <job.ini>`_                                         |
+-------------------------+--------------------------------------------------------------+
| source_model_logic_tree | `source_model_logic_tree.xml <source_model_logic_tree.xml>`_ |
+-------------------------+--------------------------------------------------------------+

Composite source model
----------------------
+--------+--------------------+------+
| grp_id | gsim               | rlzs |
+--------+--------------------+------+
| 0      | '[SadighEtAl1997]' | 0    |
+--------+--------------------+------+

Required parameters per tectonic region type
--------------------------------------------
+----------------------+--------------------+-----------+------------+------------+
| trt_smr              | gsims              | distances | siteparams | ruptparams |
+----------------------+--------------------+-----------+------------+------------+
| active shallow crust | '[SadighEtAl1997]' | rrup      | vs30       | mag rake   |
+----------------------+--------------------+-----------+------------+------------+

Slowest sources
---------------
+-----------+------+-----------+-----------+--------------+
| source_id | code | calc_time | num_sites | eff_ruptures |
+-----------+------+-----------+-----------+--------------+
| 1         | A    | 4.75107   | 1         | 7_819        |
+-----------+------+-----------+-----------+--------------+

Computation times by source typology
------------------------------------
+------+-----------+-----------+--------------+
| code | calc_time | num_sites | eff_ruptures |
+------+-----------+-----------+--------------+
| A    | 4.75107   | 1         | 7_819        |
+------+-----------+-----------+--------------+

Information about the tasks
---------------------------
+--------------------+--------+---------+--------+---------+---------+
| operation-duration | counts | mean    | stddev | min     | max     |
+--------------------+--------+---------+--------+---------+---------+
| preclassical       | 1      | 2.83889 | nan    | 2.83889 | 2.83889 |
+--------------------+--------+---------+--------+---------+---------+
| read_source_model  | 1      | 0.00488 | nan    | 0.00488 | 0.00488 |
+--------------------+--------+---------+--------+---------+---------+

Data transfer
-------------
+-------------------+------+----------+
| task              | sent | received |
+-------------------+------+----------+
| read_source_model |      | 2.68 KB  |
+-------------------+------+----------+
| preclassical      |      | 1.51 MB  |
+-------------------+------+----------+

Slowest operations
------------------
+-------------------------+----------+-----------+--------+
| calc_703, maxmem=0.9 GB | time_sec | memory_mb | counts |
+-------------------------+----------+-----------+--------+
| total preclassical      | 2.83889  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| splitting sources       | 2.38932  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| weighting sources       | 0.44625  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| importing inputs        | 0.13539  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| composite source model  | 0.13275  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| total read_source_model | 0.00488  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+