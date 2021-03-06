Test case for the SplitSigma modified GMPE
==========================================

+----------------+----------------------+
| checksum32     | 2_422_345_153        |
+----------------+----------------------+
| date           | 2021-10-31T03:17:12  |
+----------------+----------------------+
| engine_version | 3.13.0-git04a140fc38 |
+----------------+----------------------+
| input_size     | 4_458                |
+----------------+----------------------+

num_sites = 36, num_levels = 40, num_rlzs = 1

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
| investigation_time              | 5.0                                        |
+---------------------------------+--------------------------------------------+
| ses_per_logic_tree_path         | 1                                          |
+---------------------------------+--------------------------------------------+
| truncation_level                | 3.0                                        |
+---------------------------------+--------------------------------------------+
| rupture_mesh_spacing            | 2.0                                        |
+---------------------------------+--------------------------------------------+
| complex_fault_mesh_spacing      | 2.0                                        |
+---------------------------------+--------------------------------------------+
| width_of_mfd_bin                | 0.2                                        |
+---------------------------------+--------------------------------------------+
| area_source_discretization      | 10.0                                       |
+---------------------------------+--------------------------------------------+
| pointsource_distance            | None                                       |
+---------------------------------+--------------------------------------------+
| ground_motion_correlation_model | None                                       |
+---------------------------------+--------------------------------------------+
| minimum_intensity               | {}                                         |
+---------------------------------+--------------------------------------------+
| random_seed                     | 23                                         |
+---------------------------------+--------------------------------------------+
| master_seed                     | 123456789                                  |
+---------------------------------+--------------------------------------------+
| ses_seed                        | 24                                         |
+---------------------------------+--------------------------------------------+

Input files
-----------
+-------------------------+--------------------------+
| Name                    | File                     |
+-------------------------+--------------------------+
| gsim_logic_tree         | `gmmLt.xml <gmmLt.xml>`_ |
+-------------------------+--------------------------+
| job_ini                 | `job.ini <job.ini>`_     |
+-------------------------+--------------------------+
| source_model_logic_tree | `ssmLt.xml <ssmLt.xml>`_ |
+-------------------------+--------------------------+

Composite source model
----------------------
+--------+-----------------------------------------------------------------------+------+
| grp_id | gsim                                                                  | rlzs |
+--------+-----------------------------------------------------------------------+------+
| 0      | '[SplitSigmaGMPE]\ngmpe_name = "Campbell2003"\nwithin_absolute = 0.3' | 0    |
+--------+-----------------------------------------------------------------------+------+

Required parameters per tectonic region type
--------------------------------------------
+----------------------+-----------------------------------------------------------------------+-----------+------------+------------+
| trt_smr              | gsims                                                                 | distances | siteparams | ruptparams |
+----------------------+-----------------------------------------------------------------------+-----------+------------+------------+
| Active Shallow Crust | '[SplitSigmaGMPE]\ngmpe_name = "Campbell2003"\nwithin_absolute = 0.3' | rrup      |            | mag        |
+----------------------+-----------------------------------------------------------------------+-----------+------------+------------+

Slowest sources
---------------
+-----------+------+-----------+-----------+--------------+
| source_id | code | calc_time | num_sites | eff_ruptures |
+-----------+------+-----------+-----------+--------------+
| 1         | A    | 0.08404   | 36        | 416          |
+-----------+------+-----------+-----------+--------------+

Computation times by source typology
------------------------------------
+------+-----------+-----------+--------------+
| code | calc_time | num_sites | eff_ruptures |
+------+-----------+-----------+--------------+
| A    | 0.08404   | 36        | 416          |
+------+-----------+-----------+--------------+

Information about the tasks
---------------------------
+--------------------+--------+---------+--------+---------+---------+
| operation-duration | counts | mean    | stddev | min     | max     |
+--------------------+--------+---------+--------+---------+---------+
| preclassical       | 1      | 0.04726 | nan    | 0.04726 | 0.04726 |
+--------------------+--------+---------+--------+---------+---------+
| read_source_model  | 1      | 0.00244 | nan    | 0.00244 | 0.00244 |
+--------------------+--------+---------+--------+---------+---------+

Data transfer
-------------
+-------------------+------+----------+
| task              | sent | received |
+-------------------+------+----------+
| read_source_model |      | 1.75 KB  |
+-------------------+------+----------+
| preclassical      |      | 11.42 KB |
+-------------------+------+----------+

Slowest operations
------------------
+-------------------------+----------+-----------+--------+
| calc_594, maxmem=0.6 GB | time_sec | memory_mb | counts |
+-------------------------+----------+-----------+--------+
| importing inputs        | 0.12082  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| composite source model  | 0.11839  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| total preclassical      | 0.04726  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| splitting sources       | 0.04236  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| weighting sources       | 0.00440  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| total read_source_model | 0.00244  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+