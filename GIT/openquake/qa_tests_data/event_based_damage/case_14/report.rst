Stochastic Event-Based Damage Demo (Nepal)
==========================================

+----------------+----------------------+
| checksum32     | 2_973_522_147        |
+----------------+----------------------+
| date           | 2021-10-31T03:16:29  |
+----------------+----------------------+
| engine_version | 3.13.0-git04a140fc38 |
+----------------+----------------------+
| input_size     | 990_503              |
+----------------+----------------------+

num_sites = 407, num_levels = 1, num_rlzs = 1

Parameters
----------
+---------------------------------+--------------------------------------------+
| parameter                       | value                                      |
+---------------------------------+--------------------------------------------+
| calculation_mode                | 'event_based_damage'                       |
+---------------------------------+--------------------------------------------+
| number_of_logic_tree_samples    | 1                                          |
+---------------------------------+--------------------------------------------+
| maximum_distance                | {'default': [[1.0, 200.0], [10.0, 200.0]]} |
+---------------------------------+--------------------------------------------+
| investigation_time              | 50.0                                       |
+---------------------------------+--------------------------------------------+
| ses_per_logic_tree_path         | 10                                         |
+---------------------------------+--------------------------------------------+
| truncation_level                | None                                       |
+---------------------------------+--------------------------------------------+
| rupture_mesh_spacing            | 5.0                                        |
+---------------------------------+--------------------------------------------+
| complex_fault_mesh_spacing      | 5.0                                        |
+---------------------------------+--------------------------------------------+
| width_of_mfd_bin                | None                                       |
+---------------------------------+--------------------------------------------+
| area_source_discretization      | None                                       |
+---------------------------------+--------------------------------------------+
| pointsource_distance            | None                                       |
+---------------------------------+--------------------------------------------+
| ground_motion_correlation_model | None                                       |
+---------------------------------+--------------------------------------------+
| minimum_intensity               | {'PGA': 1e-10}                             |
+---------------------------------+--------------------------------------------+
| random_seed                     | 42                                         |
+---------------------------------+--------------------------------------------+
| master_seed                     | 123456789                                  |
+---------------------------------+--------------------------------------------+
| ses_seed                        | 42                                         |
+---------------------------------+--------------------------------------------+

Input files
-----------
+----------------------+--------------------------------------------------------------------+
| Name                 | File                                                               |
+----------------------+--------------------------------------------------------------------+
| exposure             | `exposure_model.xml <exposure_model.xml>`_                         |
+----------------------+--------------------------------------------------------------------+
| gmfs                 | `nepal.hdf5 <nepal.hdf5>`_                                         |
+----------------------+--------------------------------------------------------------------+
| job_ini              | `job.ini <job.ini>`_                                               |
+----------------------+--------------------------------------------------------------------+
| reqv:taxonomy        | `consequences_by_taxonomy.csv <consequences_by_taxonomy.csv>`_     |
+----------------------+--------------------------------------------------------------------+
| structural_fragility | `structural_fragility_model.xml <structural_fragility_model.xml>`_ |
+----------------------+--------------------------------------------------------------------+

Composite source model
----------------------
+--------+--------------+------+
| grp_id | gsim         | rlzs |
+--------+--------------+------+
| 0      | '[FromFile]' | 0    |
+--------+--------------+------+

Required parameters per tectonic region type
--------------------------------------------
+---------+--------------+-----------+------------+------------+
| trt_smr | gsims        | distances | siteparams | ruptparams |
+---------+--------------+-----------+------------+------------+
| *       | '[FromFile]' |           |            |            |
+---------+--------------+-----------+------------+------------+

Exposure model
--------------
+-------------+-------+
| #assets     | 9_063 |
+-------------+-------+
| #taxonomies | 5     |
+-------------+-------+

+----------------------------+-----------+---------+--------+-----+-----+------------+
| taxonomy                   | num_sites | mean    | stddev | min | max | num_assets |
+----------------------------+-----------+---------+--------+-----+-----+------------+
| Wood                       | 407       | 5.53563 | 39%    | 1   | 10  | 2_253      |
+----------------------------+-----------+---------+--------+-----+-----+------------+
| Adobe                      | 407       | 5.53563 | 39%    | 1   | 10  | 2_253      |
+----------------------------+-----------+---------+--------+-----+-----+------------+
| Stone-Masonry              | 407       | 5.53563 | 39%    | 1   | 10  | 2_253      |
+----------------------------+-----------+---------+--------+-----+-----+------------+
| Unreinforced-Brick-Masonry | 407       | 5.53563 | 39%    | 1   | 10  | 2_253      |
+----------------------------+-----------+---------+--------+-----+-----+------------+
| Concrete                   | 37        | 1.37838 | 61%    | 1   | 5   | 51         |
+----------------------------+-----------+---------+--------+-----+-----+------------+
| *ALL*                      | 407       | 22.3    | 39%    | 4   | 42  | 9_063      |
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
+------------------+----------+-----------+--------+
| calc_535         | time_sec | memory_mb | counts |
+------------------+----------+-----------+--------+
| importing inputs | 0.80934  | 11.4      | 1      |
+------------------+----------+-----------+--------+
| reading exposure | 0.69124  | 10.4      | 1      |
+------------------+----------+-----------+--------+