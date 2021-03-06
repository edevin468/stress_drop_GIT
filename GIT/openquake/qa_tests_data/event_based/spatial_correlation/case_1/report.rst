Probabilistic Event-Based QA Test with Spatial Correlation, case 1
==================================================================

+----------------+----------------------+
| checksum32     | 3_378_192_640        |
+----------------+----------------------+
| date           | 2021-10-31T03:17:25  |
+----------------+----------------------+
| engine_version | 3.13.0-git04a140fc38 |
+----------------+----------------------+
| input_size     | 3_241                |
+----------------+----------------------+

num_sites = 2, num_levels = 1, num_rlzs = 1

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
| investigation_time              | 50.0                                       |
+---------------------------------+--------------------------------------------+
| ses_per_logic_tree_path         | 125                                        |
+---------------------------------+--------------------------------------------+
| truncation_level                | None                                       |
+---------------------------------+--------------------------------------------+
| rupture_mesh_spacing            | 2.0                                        |
+---------------------------------+--------------------------------------------+
| complex_fault_mesh_spacing      | 2.0                                        |
+---------------------------------+--------------------------------------------+
| width_of_mfd_bin                | 0.1                                        |
+---------------------------------+--------------------------------------------+
| area_source_discretization      | 20.0                                       |
+---------------------------------+--------------------------------------------+
| pointsource_distance            | None                                       |
+---------------------------------+--------------------------------------------+
| ground_motion_correlation_model | 'JB2009'                                   |
+---------------------------------+--------------------------------------------+
| minimum_intensity               | {}                                         |
+---------------------------------+--------------------------------------------+
| random_seed                     | 42                                         |
+---------------------------------+--------------------------------------------+
| master_seed                     | 123456789                                  |
+---------------------------------+--------------------------------------------+
| ses_seed                        | 123456789                                  |
+---------------------------------+--------------------------------------------+

Input files
-----------
+-------------------------+--------------------------------------------------------------+
| Name                    | File                                                         |
+-------------------------+--------------------------------------------------------------+
| gsim_logic_tree         | `gmpe_logic_tree.xml <gmpe_logic_tree.xml>`_                 |
+-------------------------+--------------------------------------------------------------+
| job_ini                 | `job.ini <job.ini>`_                                         |
+-------------------------+--------------------------------------------------------------+
| source_model_logic_tree | `source_model_logic_tree.xml <source_model_logic_tree.xml>`_ |
+-------------------------+--------------------------------------------------------------+

Composite source model
----------------------
+--------+-----------------------+------+
| grp_id | gsim                  | rlzs |
+--------+-----------------------+------+
| 0      | '[BooreAtkinson2008]' | 0    |
+--------+-----------------------+------+

Required parameters per tectonic region type
--------------------------------------------
+----------------------+-----------------------+-----------+------------+------------+
| trt_smr              | gsims                 | distances | siteparams | ruptparams |
+----------------------+-----------------------+-----------+------------+------------+
| Active Shallow Crust | '[BooreAtkinson2008]' | rjb       | vs30       | mag rake   |
+----------------------+-----------------------+-----------+------------+------------+

Slowest sources
---------------
+-----------+------+-----------+-----------+--------------+
| source_id | code | calc_time | num_sites | eff_ruptures |
+-----------+------+-----------+-----------+--------------+
| 1         | P    | 3.238E-04 | 2         | 1            |
+-----------+------+-----------+-----------+--------------+

Computation times by source typology
------------------------------------
+------+-----------+-----------+--------------+
| code | calc_time | num_sites | eff_ruptures |
+------+-----------+-----------+--------------+
| P    | 3.238E-04 | 2         | 1            |
+------+-----------+-----------+--------------+

Information about the tasks
---------------------------
+--------------------+--------+---------+--------+---------+---------+
| operation-duration | counts | mean    | stddev | min     | max     |
+--------------------+--------+---------+--------+---------+---------+
| preclassical       | 1      | 0.00121 | nan    | 0.00121 | 0.00121 |
+--------------------+--------+---------+--------+---------+---------+
| read_source_model  | 1      | 0.00139 | nan    | 0.00139 | 0.00139 |
+--------------------+--------+---------+--------+---------+---------+

Data transfer
-------------
+-------------------+------+----------+
| task              | sent | received |
+-------------------+------+----------+
| read_source_model |      | 1.43 KB  |
+-------------------+------+----------+
| preclassical      |      | 1.43 KB  |
+-------------------+------+----------+

Slowest operations
------------------
+-------------------------+-----------+-----------+--------+
| calc_603, maxmem=0.4 GB | time_sec  | memory_mb | counts |
+-------------------------+-----------+-----------+--------+
| importing inputs        | 0.09768   | 0.0       | 1      |
+-------------------------+-----------+-----------+--------+
| composite source model  | 0.09513   | 0.0       | 1      |
+-------------------------+-----------+-----------+--------+
| total read_source_model | 0.00139   | 0.0       | 1      |
+-------------------------+-----------+-----------+--------+
| total preclassical      | 0.00121   | 0.0       | 1      |
+-------------------------+-----------+-----------+--------+
| weighting sources       | 4.461E-04 | 0.0       | 1      |
+-------------------------+-----------+-----------+--------+
| splitting sources       | 3.657E-04 | 0.0       | 1      |
+-------------------------+-----------+-----------+--------+