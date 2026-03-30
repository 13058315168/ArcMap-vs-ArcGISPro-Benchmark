# Benchmark Results (py2)

*Generated on 2026-03-30 11:39:26*

## Summary

| Test Name | Mean Time | Std Time | Min Time | Max Time |
|---|---|---|---|---|
| V1_CreateFishnet | 0.4278 | 0.3079 | 0.2101 | 0.6455 |
| V2_CreateRandomPoints | 0.0907 | 0.0080 | 0.0851 | 0.0964 |
| V3_Buffer | 0.1819 | 0.0078 | 0.1764 | 0.1874 |
| V4_Intersect | 0.3412 | 0.0036 | 0.3387 | 0.3437 |
| V5_SpatialJoin | 0.9168 | 0.2009 | 0.7747 | 1.0588 |
| V6_CalculateField | 1.1299 | 0.0027 | 1.1280 | 1.1319 |
| R1_CreateConstantRaster | 0.1301 | 0.0223 | 0.1143 | 0.1458 |
| R2_Resample | 0.2263 | 0.0015 | 0.2253 | 0.2274 |
| R3_Clip | 0.2750 | 0.0155 | 0.2641 | 0.2859 |
| R4_RasterCalculator | 0.3207 | 0.0192 | 0.3072 | 0.3343 |
| M1_PolygonToRaster | 1.2005 | 0.1402 | 1.1014 | 1.2996 |
| M2_RasterToPoint | 13.7702 | 0.3787 | 13.5024 | 14.0379 |
| Py2_MP_V1_CreateFishnet_single | 0.2602 | 0.0093 | 0.2537 | 0.2668 |
| Py2_MP_V1_CreateFishnet_multiprocess | 1.0134 | 0.0481 | 0.9794 | 1.0474 |
| Py2_MP_V2_CreateRandomPoints_single | 0.1189 | 0.0185 | 0.1058 | 0.1319 |
| Py2_MP_V2_CreateRandomPoints_multiprocess | 0.5069 | 0.0263 | 0.4883 | 0.5255 |
| Py2_MP_V3_Buffer_single | 4.9114 | 0.0250 | 4.8937 | 4.9291 |
| Py2_MP_V3_Buffer_multiprocess | 5.6928 | 0.7266 | 5.1790 | 6.2065 |
| Py2_MP_V4_Intersect_single | 0.3004 | 0.0053 | 0.2967 | 0.3041 |
| Py2_MP_V4_Intersect_multiprocess | 3.8274 | 0.5477 | 3.4402 | 4.2147 |
| Py2_MP_R1_CreateConstantRaster_single | 0.1051 | 0.0174 | 0.0927 | 0.1174 |
| Py2_MP_R1_CreateConstantRaster_multiprocess | 0.7616 | 0.0687 | 0.7131 | 0.8102 |

## Detailed Results

### V1_CreateFishnet

- **all_times**: [0.6455407000000001, 0.21008629999999995]
- **avg_memory_mb**: 195.0703125
- **category**: vector
- **cv_percent**: 71.9735957695
- **failed_runs**: 0
- **max_time**: 0.6455407
- **mean_time**: 0.4278135
- **min_time**: 0.2100863
- **python_version**: 2.7.16
- **std_time**: 0.307912759138
- **success**: True
- **successful_runs**: 2
- **test_name**: V1_CreateFishnet
- **total_runs**: 2

### V2_CreateRandomPoints

- **all_times**: [0.0850651, 0.09642010000000001]
- **avg_memory_mb**: 196.69921875
- **category**: vector
- **cv_percent**: 8.84832206744
- **failed_runs**: 0
- **max_time**: 0.0964201
- **mean_time**: 0.0907426
- **min_time**: 0.0850651
- **python_version**: 2.7.16
- **std_time**: 0.00802919750037
- **success**: True
- **successful_runs**: 2
- **test_name**: V2_CreateRandomPoints
- **total_runs**: 2

### V3_Buffer

- **all_times**: [0.1763944999999998, 0.18735890000000044]
- **avg_memory_mb**: 198.669921875
- **category**: vector
- **cv_percent**: 4.26277890001
- **failed_runs**: 0
- **max_time**: 0.1873589
- **mean_time**: 0.1818767
- **min_time**: 0.1763945
- **python_version**: 2.7.16
- **std_time**: 0.00775300159164
- **success**: True
- **successful_runs**: 2
- **test_name**: V3_Buffer
- **total_runs**: 2

### V4_Intersect

- **all_times**: [0.3437353999999999, 0.33868279999999995]
- **avg_memory_mb**: 201.17578125
- **category**: vector
- **cv_percent**: 1.04707867481
- **failed_runs**: 0
- **max_time**: 0.3437354
- **mean_time**: 0.3412091
- **min_time**: 0.3386828
- **python_version**: 2.7.16
- **std_time**: 0.00357272772262
- **success**: True
- **successful_runs**: 2
- **test_name**: V4_Intersect
- **total_runs**: 2

### V5_SpatialJoin

- **all_times**: [1.0587926999999997, 0.7747260000000002]
- **avg_memory_mb**: 233.84375
- **category**: vector
- **cv_percent**: 21.910383557
- **failed_runs**: 0
- **max_time**: 1.0587927
- **mean_time**: 0.91675935
- **min_time**: 0.774726
- **python_version**: 2.7.16
- **std_time**: 0.200865489879
- **success**: True
- **successful_runs**: 2
- **test_name**: V5_SpatialJoin
- **total_runs**: 2

### V6_CalculateField

- **all_times**: [1.1280055000000004, 1.1318788999999985]
- **avg_memory_mb**: 233.275390625
- **category**: vector
- **cv_percent**: 0.242393584933
- **failed_runs**: 0
- **max_time**: 1.1318789
- **mean_time**: 1.1299422
- **min_time**: 1.1280055
- **python_version**: 2.7.16
- **std_time**: 0.00273890740625
- **success**: True
- **successful_runs**: 2
- **test_name**: V6_CalculateField
- **total_runs**: 2

### R1_CreateConstantRaster

- **all_times**: [0.14584969999999942, 0.11433200000000099]
- **avg_memory_mb**: 236.298828125
- **category**: raster
- **cv_percent**: 17.1313965566
- **failed_runs**: 0
- **max_time**: 0.1458497
- **mean_time**: 0.13009085
- **min_time**: 0.114332
- **python_version**: 2.7.16
- **std_time**: 0.0222863793974
- **success**: True
- **successful_runs**: 2
- **test_name**: R1_CreateConstantRaster
- **total_runs**: 2

### R2_Resample

- **all_times**: [0.22528609999999993, 0.2273721000000002]
- **avg_memory_mb**: 240.203125
- **category**: raster
- **cv_percent**: 0.651716790088
- **failed_runs**: 0
- **max_time**: 0.2273721
- **mean_time**: 0.2263291
- **min_time**: 0.2252861
- **python_version**: 2.7.16
- **std_time**: 0.00147502474556
- **success**: True
- **successful_runs**: 2
- **test_name**: R2_Resample
- **total_runs**: 2

### R3_Clip

- **all_times**: [0.2640597000000007, 0.2859102]
- **avg_memory_mb**: 240.5546875
- **category**: raster
- **cv_percent**: 5.61872085084
- **failed_runs**: 0
- **max_time**: 0.2859102
- **mean_time**: 0.27498495
- **min_time**: 0.2640597
- **python_version**: 2.7.16
- **std_time**: 0.0154506367223
- **success**: True
- **successful_runs**: 2
- **test_name**: R3_Clip
- **total_runs**: 2

### R4_RasterCalculator

- **all_times**: [0.3071652999999994, 0.3343126999999999]
- **avg_memory_mb**: 241.400390625
- **category**: raster
- **cv_percent**: 5.98496304833
- **failed_runs**: 0
- **max_time**: 0.3343127
- **mean_time**: 0.320739
- **min_time**: 0.3071653
- **python_version**: 2.7.16
- **std_time**: 0.0191961106316
- **success**: True
- **successful_runs**: 2
- **test_name**: R4_RasterCalculator
- **total_runs**: 2

### M1_PolygonToRaster

- **all_times**: [1.1013832000000008, 1.2996294000000006]
- **avg_memory_mb**: 242.0078125
- **category**: mixed
- **cv_percent**: 11.6768427092
- **failed_runs**: 0
- **max_time**: 1.2996294
- **mean_time**: 1.2005063
- **min_time**: 1.1013832
- **python_version**: 2.7.16
- **std_time**: 0.140181232364
- **success**: True
- **successful_runs**: 2
- **test_name**: M1_PolygonToRaster
- **total_runs**: 2

### M2_RasterToPoint

- **all_times**: [13.502435899999998, 14.037949700000006]
- **avg_memory_mb**: 244.1796875
- **category**: mixed
- **cv_percent**: 2.74989206686
- **failed_runs**: 0
- **max_time**: 14.0379497
- **mean_time**: 13.7701928
- **min_time**: 13.5024359
- **python_version**: 2.7.16
- **std_time**: 0.378665439399
- **success**: True
- **successful_runs**: 2
- **test_name**: M2_RasterToPoint
- **total_runs**: 2

### Py2_MP_V1_CreateFishnet_single

- **all_times**: [0.2536904999999976, 0.2668005000000022]
- **avg_memory_mb**: 243.62890625
- **category**: vector_multiprocess
- **cv_percent**: 3.56208653036
- **failed_runs**: 0
- **max_time**: 0.2668005
- **mean_time**: 0.2602455
- **min_time**: 0.2536905
- **python_version**: 2.7.16
- **std_time**: 0.00927016990136
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V1_CreateFishnet_single
- **total_runs**: 2

### Py2_MP_V1_CreateFishnet_multiprocess

- **all_times**: [0.9794185999999954, 1.0474122999999977]
- **avg_memory_mb**: 245.015625
- **category**: vector_multiprocess
- **cv_percent**: 4.74423459283
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 1.0474123
- **mean_time**: 1.01341545
- **min_time**: 0.9794186
- **num_workers**: 2
- **parallel_efficiency**: 12.840020349
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.25680040698
- **std_time**: 0.048078806348
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V1_CreateFishnet_multiprocess
- **total_runs**: 2

### Py2_MP_V2_CreateRandomPoints_single

- **all_times**: [0.10578339999999997, 0.13194339999999727]
- **avg_memory_mb**: 245.5859375
- **category**: vector_multiprocess
- **cv_percent**: 15.5623290229
- **failed_runs**: 0
- **max_time**: 0.1319434
- **mean_time**: 0.1188634
- **min_time**: 0.1057834
- **python_version**: 2.7.16
- **std_time**: 0.0184979133958
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V2_CreateRandomPoints_single
- **total_runs**: 2

### Py2_MP_V2_CreateRandomPoints_multiprocess

- **all_times**: [0.4883430000000004, 0.5255216000000047]
- **avg_memory_mb**: 245.52734375
- **category**: vector_multiprocess
- **cv_percent**: 5.18594695485
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 0.5255216
- **mean_time**: 0.5069323
- **min_time**: 0.488343
- **num_workers**: 2
- **parallel_efficiency**: 11.7237942818
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.234475885636
- **std_time**: 0.026289240175
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V2_CreateRandomPoints_multiprocess
- **total_runs**: 2

### Py2_MP_V3_Buffer_single

- **all_times**: [4.893674400000002, 4.929093200000004]
- **avg_memory_mb**: 246.3125
- **category**: vector_multiprocess
- **cv_percent**: 0.509935176752
- **failed_runs**: 0
- **max_time**: 4.9290932
- **mean_time**: 4.9113838
- **min_time**: 4.8936744
- **python_version**: 2.7.16
- **std_time**: 0.0250448736615
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V3_Buffer_single
- **total_runs**: 2

### Py2_MP_V3_Buffer_multiprocess

- **all_times**: [6.206524399999992, 5.1789895]
- **avg_memory_mb**: 250.767578125
- **category**: vector_multiprocess
- **cv_percent**: 12.7631813913
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 6.2065244
- **mean_time**: 5.69275695
- **min_time**: 5.1789895
- **num_workers**: 2
- **parallel_efficiency**: 43.1371288388
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.862742576776
- **std_time**: 0.726576895696
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V3_Buffer_multiprocess
- **total_runs**: 2

### Py2_MP_V4_Intersect_single

- **all_times**: [0.2966612999999967, 0.3041389000000123]
- **avg_memory_mb**: 255.681640625
- **category**: vector_multiprocess
- **cv_percent**: 1.76013978258
- **failed_runs**: 0
- **max_time**: 0.3041389
- **mean_time**: 0.3004001
- **min_time**: 0.2966613
- **python_version**: 2.7.16
- **std_time**: 0.00528746166701
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V4_Intersect_single
- **total_runs**: 2

### Py2_MP_V4_Intersect_multiprocess

- **all_times**: [3.4401874000000134, 4.2147032999999965]
- **avg_memory_mb**: 258.236328125
- **category**: vector_multiprocess
- **cv_percent**: 14.3089030658
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 4.2147033
- **mean_time**: 3.82744535
- **min_time**: 3.4401874
- **num_workers**: 2
- **parallel_efficiency**: 3.92428986609
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.0784857973217
- **std_time**: 0.547665445027
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V4_Intersect_multiprocess
- **total_runs**: 2

### Py2_MP_R1_CreateConstantRaster_single

- **all_times**: [0.09273880000000645, 0.11739090000000374]
- **avg_memory_mb**: 259.001953125
- **category**: raster_multiprocess
- **cv_percent**: 16.5913405677
- **failed_runs**: 0
- **max_time**: 0.1173909
- **mean_time**: 0.10506485
- **min_time**: 0.0927388
- **python_version**: 2.7.16
- **std_time**: 0.0174316670805
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_R1_CreateConstantRaster_single
- **total_runs**: 2

### Py2_MP_R1_CreateConstantRaster_multiprocess

- **all_times**: [0.8102011000000005, 0.7130895000000095]
- **avg_memory_mb**: 259.296875
- **category**: raster_multiprocess
- **cv_percent**: 9.01578082237
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 0.8102011
- **mean_time**: 0.7616453
- **min_time**: 0.7130895
- **num_workers**: 2
- **parallel_efficiency**: 6.89722958968
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.137944591794
- **std_time**: 0.0686682708919
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_R1_CreateConstantRaster_multiprocess
- **total_runs**: 2
