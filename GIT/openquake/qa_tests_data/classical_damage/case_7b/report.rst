Classical PSHA-Based Hazard
===========================

+----------------+----------------------+
| checksum32     | 2_952_475_925        |
+----------------+----------------------+
| date           | 2021-10-31T03:17:10  |
+----------------+----------------------+
| engine_version | 3.13.0-git04a140fc38 |
+----------------+----------------------+
| input_size     | 7_726                |
+----------------+----------------------+

num_sites = 7, num_levels = 90, num_rlzs = 1

Parameters
----------
+---------------------------------+-------------------------------------------------+
| parameter                       | value                                           |
+---------------------------------+-------------------------------------------------+
| calculation_mode                | 'preclassical'                                  |
+---------------------------------+-------------------------------------------------+
| number_of_logic_tree_samples    | 0                                               |
+---------------------------------+-------------------------------------------------+
| maximum_distance                | {'default': [[1.0, 200.0], [10.0, 200.0]]}      |
+---------------------------------+-------------------------------------------------+
| investigation_time              | 50.0                                            |
+---------------------------------+-------------------------------------------------+
| ses_per_logic_tree_path         | 1                                               |
+---------------------------------+-------------------------------------------------+
| truncation_level                | 3.0                                             |
+---------------------------------+-------------------------------------------------+
| rupture_mesh_spacing            | 2.0                                             |
+---------------------------------+-------------------------------------------------+
| complex_fault_mesh_spacing      | 2.0                                             |
+---------------------------------+-------------------------------------------------+
| width_of_mfd_bin                | 0.1                                             |
+---------------------------------+-------------------------------------------------+
| area_source_discretization      | 20.0                                            |
+---------------------------------+-------------------------------------------------+
| pointsource_distance            | None                                            |
+---------------------------------+-------------------------------------------------+
| ground_motion_correlation_model | None                                            |
+---------------------------------+-------------------------------------------------+
| minimum_intensity               | {'SA(0.3)': 0.05, 'SA(0.5)': 0.05, 'PGA': 0.05} |
+---------------------------------+-------------------------------------------------+
| random_seed                     | 42                                              |
+---------------------------------+-------------------------------------------------+
| master_seed                     | 123456789                                       |
+---------------------------------+-------------------------------------------------+
| ses_seed                        | 42                                              |
+---------------------------------+-------------------------------------------------+

Input files
-----------
+-------------------------+--------------------------------------------------------------+
| Name                    | File                                                         |
+-------------------------+--------------------------------------------------------------+
| exposure                | `exposure_model_7.xml <exposure_model_7.xml>`_               |
+-------------------------+--------------------------------------------------------------+
| gsim_logic_tree         | `gmpe_logic_tree.xml <gmpe_logic_tree.xml>`_                 |
+-------------------------+--------------------------------------------------------------+
| job_ini                 | `job_haz.ini <job_haz.ini>`_                                 |
+-------------------------+--------------------------------------------------------------+
| source_model_logic_tree | `source_model_logic_tree.xml <source_model_logic_tree.xml>`_ |
+-------------------------+--------------------------------------------------------------+
| structural_fragility    | `fragility_model.xml <fragility_model.xml>`_                 |
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
| Active Shallow Crust | '[SadighEtAl1997]' | rrup      | vs30       | mag rake   |
+----------------------+--------------------+-----------+------------+------------+

Exposure model
--------------
+-------------+---+
| #assets     | 7 |
+-------------+---+
| #taxonomies | 3 |
+-------------+---+

+----------+-----------+---------+--------+-----+-----+------------+
| taxonomy | num_sites | mean    | stddev | min | max | num_assets |
+----------+-----------+---------+--------+-----+-----+------------+
| Wood     | 3         | 1.00000 | 0%     | 1   | 1   | 3          |
+----------+-----------+---------+--------+-----+-----+------------+
| Concrete | 2         | 1.00000 | 0%     | 1   | 1   | 2          |
+----------+-----------+---------+--------+-----+-----+------------+
| Steel    | 2         | 1.00000 | 0%     | 1   | 1   | 2          |
+----------+-----------+---------+--------+-----+-----+------------+
| *ALL*    | 7         | 1.00000 | 0%     | 1   | 1   | 7          |
+----------+-----------+---------+--------+-----+-----+------------+

Slowest sources
---------------
+-----------+------+-----------+-----------+--------------+
| source_id | code | calc_time | num_sites | eff_ruptures |
+-----------+------+-----------+-----------+--------------+
| 1         | S    | 0.01675   | 7         | 482          |
+-----------+------+-----------+-----------+--------------+

Computation times by source typology
------------------------------------
+------+-----------+-----------+--------------+
| code | calc_time | num_sites | eff_ruptures |
+------+-----------+-----------+--------------+
| S    | 0.01675   | 7         | 482          |
+------+-----------+-----------+--------------+

Information about the tasks
---------------------------
+--------------------+--------+---------+--------+---------+---------+
| operation-duration | counts | mean    | stddev | min     | max     |
+--------------------+--------+---------+--------+---------+---------+
| preclassical       | 1      | 0.10305 | nan    | 0.10305 | 0.10305 |
+--------------------+--------+---------+--------+---------+---------+
| read_source_model  | 1      | 0.00154 | nan    | 0.00154 | 0.00154 |
+--------------------+--------+---------+--------+---------+---------+

Data transfer
-------------
+-------------------+------+----------+
| task              | sent | received |
+-------------------+------+----------+
| read_source_model |      | 1.39 KB  |
+-------------------+------+----------+
| preclassical      |      | 4.03 KB  |
+-------------------+------+----------+

Slowest operations
------------------
+-------------------------+----------+-----------+--------+
| calc_588, maxmem=0.6 GB | time_sec | memory_mb | counts |
+-------------------------+----------+-----------+--------+
| importing inputs        | 0.12799  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| total preclassical      | 0.10305  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| composite source model  | 0.10119  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| weighting sources       | 0.09399  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| splitting sources       | 0.00862  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| reading exposure        | 0.00303  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+
| total read_source_model | 0.00154  | 0.0       | 1      |
+-------------------------+----------+-----------+--------+