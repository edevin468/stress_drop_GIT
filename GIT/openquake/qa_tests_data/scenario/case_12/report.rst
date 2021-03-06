Scenario with IPE DowrickRhoades2005Asc
=======================================

+----------------+----------------------+
| checksum32     | 648_256_452          |
+----------------+----------------------+
| date           | 2021-10-31T03:16:28  |
+----------------+----------------------+
| engine_version | 3.13.0-git04a140fc38 |
+----------------+----------------------+
| input_size     | 1_290                |
+----------------+----------------------+

num_sites = 1, num_levels = 1, num_rlzs = ?

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
| truncation_level                | 1.0                                    |
+---------------------------------+----------------------------------------+
| rupture_mesh_spacing            | 1.0                                    |
+---------------------------------+----------------------------------------+
| complex_fault_mesh_spacing      | 1.0                                    |
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
+---------------+------------------------------------------+
| Name          | File                                     |
+---------------+------------------------------------------+
| job_ini       | `job.ini <job.ini>`_                     |
+---------------+------------------------------------------+
| rupture_model | `rupture_model.xml <rupture_model.xml>`_ |
+---------------+------------------------------------------+

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
| calc_531         | time_sec | memory_mb | counts |
+------------------+----------+-----------+--------+
| importing inputs | 0.00836  | 0.0       | 1      |
+------------------+----------+-----------+--------+