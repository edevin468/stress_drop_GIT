Calculation of the ground motion fields for a scenario
======================================================

+----------------+----------------------+
| checksum32     | 1_456_907_710        |
+----------------+----------------------+
| date           | 2021-10-31T03:16:48  |
+----------------+----------------------+
| engine_version | 3.13.0-git04a140fc38 |
+----------------+----------------------+
| input_size     | 10_666               |
+----------------+----------------------+

num_sites = 11, num_levels = 1, num_rlzs = ?

Parameters
----------
+---------------------------------+----------------------------------------+
| parameter                       | value                                  |
+---------------------------------+----------------------------------------+
| calculation_mode                | 'scenario'                             |
+---------------------------------+----------------------------------------+
| number_of_logic_tree_samples    | 0                                      |
+---------------------------------+----------------------------------------+
| maximum_distance                | {'default': [[1.0, 200], [10.0, 200]]} |
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
| minimum_intensity               | {}                                     |
+---------------------------------+----------------------------------------+
| random_seed                     | 42                                     |
+---------------------------------+----------------------------------------+
| master_seed                     | 123456789                              |
+---------------------------------+----------------------------------------+
| ses_seed                        | 3                                      |
+---------------------------------+----------------------------------------+

Input files
-----------
+---------------+--------------------------------------------+
| Name          | File                                       |
+---------------+--------------------------------------------+
| exposure      | `exposure_model.xml <exposure_model.xml>`_ |
+---------------+--------------------------------------------+
| job_ini       | `job_haz.ini <job_haz.ini>`_               |
+---------------+--------------------------------------------+
| rupture_model | `fault_rupture.xml <fault_rupture.xml>`_   |
+---------------+--------------------------------------------+

Exposure model
--------------
+-------------+----+
| #assets     | 11 |
+-------------+----+
| #taxonomies | 4  |
+-------------+----+

+----------+-----------+---------+--------+-----+-----+------------+
| taxonomy | num_sites | mean    | stddev | min | max | num_assets |
+----------+-----------+---------+--------+-----+-----+------------+
| W        | 2         | 1.00000 | 0%     | 1   | 1   | 2          |
+----------+-----------+---------+--------+-----+-----+------------+
| A        | 5         | 1.00000 | 0%     | 1   | 1   | 5          |
+----------+-----------+---------+--------+-----+-----+------------+
| DS       | 2         | 1.00000 | 0%     | 1   | 1   | 2          |
+----------+-----------+---------+--------+-----+-----+------------+
| UFB      | 2         | 1.00000 | 0%     | 1   | 1   | 2          |
+----------+-----------+---------+--------+-----+-----+------------+
| *ALL*    | 11        | 1.00000 | 0%     | 1   | 1   | 11         |
+----------+-----------+---------+--------+-----+-----+------------+

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
+------------------+----------+-----------+--------+
| calc_564         | time_sec | memory_mb | counts |
+------------------+----------+-----------+--------+
| importing inputs | 0.03997  | 0.0       | 1      |
+------------------+----------+-----------+--------+
| reading exposure | 0.01719  | 0.0       | 1      |
+------------------+----------+-----------+--------+