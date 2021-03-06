Event-Based Hazard QA Test, Case 4
==================================

+----------------+----------------------+
| checksum32     | 1_935_819_891        |
+----------------+----------------------+
| date           | 2021-10-31T03:17:21  |
+----------------+----------------------+
| engine_version | 3.13.0-git04a140fc38 |
+----------------+----------------------+
| input_size     | 3_404                |
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
| ses_per_logic_tree_path         | 50                                         |
+---------------------------------+--------------------------------------------+
| truncation_level                | 0.0                                        |
+---------------------------------+--------------------------------------------+
| rupture_mesh_spacing            | 2.0                                        |
+---------------------------------+--------------------------------------------+
| complex_fault_mesh_spacing      | 2.0                                        |
+---------------------------------+--------------------------------------------+
| width_of_mfd_bin                | 1.0                                        |
+---------------------------------+--------------------------------------------+
| area_source_discretization      | 20.0                                       |
+---------------------------------+--------------------------------------------+
| pointsource_distance            | None                                       |
+---------------------------------+--------------------------------------------+
| ground_motion_correlation_model | None                                       |
+---------------------------------+--------------------------------------------+
| minimum_intensity               | {}                                         |
+---------------------------------+--------------------------------------------+
| random_seed                     | 42                                         |
+---------------------------------+--------------------------------------------+
| master_seed                     | 123456789                                  |
+---------------------------------+--------------------------------------------+
| ses_seed                        | 1066                                       |
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
| 1         | S    | 0.00945   | 1         | 5            |
+-----------+------+-----------+-----------+--------------+

Computation times by source typology
------------------------------------
+------+-----------+-----------+--------------+
| code | calc_time | num_sites | eff_ruptures |
+------+-----------+-----------+--------------+
| S    | 0.00945   | 1         | 5            |
+------+-----------+-----------+--------------+

Information about the tasks
---------------------------
+--------------------+--------+---------+--------+---------+---------+
| operation-duration | counts | mean    | stddev | min     | max     |
+--------------------+--------+---------+--------+---------+---------+
| preclassical       | 1      | 0.00710 | nan    | 0.00710 | 0.00710 |
+--------------------+--------+---------+--------+---------+---------+
| read_source_model  | 1      | 0.00216 | nan    | 0.00216 | 0.00216 |
+--------------------+--------+---------+--------+---------+---------+

Data transfer
-------------
+-------------------+------+----------+
| task              | sent | received |
+-------------------+------+----------+
| read_source_model |      | 1.42 KB  |
+-------------------+------+----------+
| preclassical      |      | 1.41 KB  |
+-------------------+------+----------+

Slowest operations
------------------
+-------------------------+----------+-----------+--------+
| calc_599, maxmem=0.3 GB | time_sec | memory_mb | counts |
+-------------------------+----------+-----------+--------+
| importing inputs        | 0.06766  | 0.00391   | 1      |
+-------------------------+----------+-----------+--------+
| composite source model  | 0.06530  | 0.00391   | 1      |
+-------------------------+----------+-----------+--------+
| total preclassical      | 0.00710  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| splitting sources       | 0.00495  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| total read_source_model | 0.00216  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| weighting sources       | 0.00164  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+