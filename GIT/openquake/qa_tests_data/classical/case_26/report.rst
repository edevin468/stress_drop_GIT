Classical PSHA — Area Source
============================

+----------------+----------------------+
| checksum32     | 272_664_341          |
+----------------+----------------------+
| date           | 2021-10-31T03:17:59  |
+----------------+----------------------+
| engine_version | 3.13.0-git04a140fc38 |
+----------------+----------------------+
| input_size     | 3_774                |
+----------------+----------------------+

num_sites = 1, num_levels = 19, num_rlzs = 1

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
| area_source_discretization      | 5.0                                        |
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
| ses_seed                        | 42                                         |
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
| 1         | A    | 0.25964   | 1         | 11_132       |
+-----------+------+-----------+-----------+--------------+

Computation times by source typology
------------------------------------
+------+-----------+-----------+--------------+
| code | calc_time | num_sites | eff_ruptures |
+------+-----------+-----------+--------------+
| A    | 0.25964   | 1         | 11_132       |
+------+-----------+-----------+--------------+

Information about the tasks
---------------------------
+--------------------+--------+---------+--------+---------+---------+
| operation-duration | counts | mean    | stddev | min     | max     |
+--------------------+--------+---------+--------+---------+---------+
| preclassical       | 1      | 0.19818 | nan    | 0.19818 | 0.19818 |
+--------------------+--------+---------+--------+---------+---------+
| read_source_model  | 1      | 0.00380 | nan    | 0.00380 | 0.00380 |
+--------------------+--------+---------+--------+---------+---------+

Data transfer
-------------
+-------------------+------+----------+
| task              | sent | received |
+-------------------+------+----------+
| read_source_model |      | 1.8 KB   |
+-------------------+------+----------+
| preclassical      |      | 96.23 KB |
+-------------------+------+----------+

Slowest operations
------------------
+-------------------------+----------+-----------+--------+
| calc_640, maxmem=0.6 GB | time_sec | memory_mb | counts |
+-------------------------+----------+-----------+--------+
| total preclassical      | 0.19818  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| splitting sources       | 0.13013  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| importing inputs        | 0.07360  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| composite source model  | 0.07100  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| weighting sources       | 0.06734  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| total read_source_model | 0.00380  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+