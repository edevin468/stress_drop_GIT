Scenario Risk for Nepal with 20 assets
======================================

+----------------+----------------------+
| checksum32     | 3_953_598_800        |
+----------------+----------------------+
| date           | 2021-10-31T03:16:32  |
+----------------+----------------------+
| engine_version | 3.13.0-git04a140fc38 |
+----------------+----------------------+
| input_size     | 19_143               |
+----------------+----------------------+

num_sites = 20, num_levels = 1, num_rlzs = 1

Parameters
----------
+---------------------------------+----------------------------------------+
| parameter                       | value                                  |
+---------------------------------+----------------------------------------+
| calculation_mode                | 'scenario_risk'                        |
+---------------------------------+----------------------------------------+
| number_of_logic_tree_samples    | 0                                      |
+---------------------------------+----------------------------------------+
| maximum_distance                | {'default': [[1.0, 500], [10.0, 500]]} |
+---------------------------------+----------------------------------------+
| investigation_time              | None                                   |
+---------------------------------+----------------------------------------+
| ses_per_logic_tree_path         | 1                                      |
+---------------------------------+----------------------------------------+
| truncation_level                | 3.0                                    |
+---------------------------------+----------------------------------------+
| rupture_mesh_spacing            | 15.0                                   |
+---------------------------------+----------------------------------------+
| complex_fault_mesh_spacing      | 15.0                                   |
+---------------------------------+----------------------------------------+
| width_of_mfd_bin                | None                                   |
+---------------------------------+----------------------------------------+
| area_source_discretization      | None                                   |
+---------------------------------+----------------------------------------+
| pointsource_distance            | None                                   |
+---------------------------------+----------------------------------------+
| ground_motion_correlation_model | None                                   |
+---------------------------------+----------------------------------------+
| minimum_intensity               | {'PGA': 0.0001}                        |
+---------------------------------+----------------------------------------+
| random_seed                     | 42                                     |
+---------------------------------+----------------------------------------+
| master_seed                     | 123456789                              |
+---------------------------------+----------------------------------------+
| ses_seed                        | 42                                     |
+---------------------------------+----------------------------------------+
| avg_losses                      | True                                   |
+---------------------------------+----------------------------------------+

Input files
-----------
+--------------------------+----------------------------------------------------------------------------+
| Name                     | File                                                                       |
+--------------------------+----------------------------------------------------------------------------+
| exposure                 | `exposure_model.xml <exposure_model.xml>`_                                 |
+--------------------------+----------------------------------------------------------------------------+
| job_ini                  | `job.ini <job.ini>`_                                                       |
+--------------------------+----------------------------------------------------------------------------+
| rupture_model            | `fault_rupture.xml <fault_rupture.xml>`_                                   |
+--------------------------+----------------------------------------------------------------------------+
| structural_vulnerability | `structural_vulnerability_model.xml <structural_vulnerability_model.xml>`_ |
+--------------------------+----------------------------------------------------------------------------+

Composite source model
----------------------
+--------+---------------------+------+
| grp_id | gsim                | rlzs |
+--------+---------------------+------+
| 0      | '[ChiouYoungs2008]' | 0    |
+--------+---------------------+------+

Required parameters per tectonic region type
--------------------------------------------
+---------+---------------------+-------------+-------------------------+-------------------+
| trt_smr | gsims               | distances   | siteparams              | ruptparams        |
+---------+---------------------+-------------+-------------------------+-------------------+
| *       | '[ChiouYoungs2008]' | rjb rrup rx | vs30 vs30measured z1pt0 | dip mag rake ztor |
+---------+---------------------+-------------+-------------------------+-------------------+

Exposure model
--------------
+-------------+----+
| #assets     | 20 |
+-------------+----+
| #taxonomies | 4  |
+-------------+----+

+----------------------------+-----------+---------+--------+-----+-----+------------+
| taxonomy                   | num_sites | mean    | stddev | min | max | num_assets |
+----------------------------+-----------+---------+--------+-----+-----+------------+
| Wood                       | 8         | 1.00000 | 0%     | 1   | 1   | 8          |
+----------------------------+-----------+---------+--------+-----+-----+------------+
| Adobe                      | 3         | 1.00000 | 0%     | 1   | 1   | 3          |
+----------------------------+-----------+---------+--------+-----+-----+------------+
| Stone-Masonry              | 4         | 1.00000 | 0%     | 1   | 1   | 4          |
+----------------------------+-----------+---------+--------+-----+-----+------------+
| Unreinforced-Brick-Masonry | 5         | 1.00000 | 0%     | 1   | 1   | 5          |
+----------------------------+-----------+---------+--------+-----+-----+------------+
| *ALL*                      | 20        | 1.00000 | 0%     | 1   | 1   | 20         |
+----------------------------+-----------+---------+--------+-----+-----+------------+

Information about the tasks
---------------------------
Not available

Data transfer
-------------
+------+------+----------+
| task | sent | received |
+------+------+----------+

Slowest operations
------------------
+--------------------------+----------+-----------+--------+
| calc_541                 | time_sec | memory_mb | counts |
+--------------------------+----------+-----------+--------+
| EventBasedCalculator.run | 0.11775  | 0.21875   | 1      |
+--------------------------+----------+-----------+--------+
| importing inputs         | 0.05157  | 0.21875   | 1      |
+--------------------------+----------+-----------+--------+
| reading exposure         | 0.01735  | 0.0       | 1      |
+--------------------------+----------+-----------+--------+