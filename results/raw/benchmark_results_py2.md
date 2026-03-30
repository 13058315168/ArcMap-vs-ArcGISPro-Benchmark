# Benchmark Results (py2)

*Generated on 2026-03-30 21:49:01*

## Summary

| Test Name | Mean Time | Std Time | Min Time | Max Time |
|---|---|---|---|---|
| V1_CreateFishnet | 0.4938 | 0.4175 | 0.1986 | 0.7890 |
| V2_CreateRandomPoints | 0.0895 | 0.0043 | 0.0864 | 0.0926 |
| V3_Buffer | 0.1688 | 0.0019 | 0.1674 | 0.1702 |
| V4_Intersect | 0.3635 | 0.0094 | 0.3568 | 0.3701 |
| V5_SpatialJoin | 0.9678 | 0.3315 | 0.7334 | 1.2022 |
| V6_CalculateField | 1.0741 | 0.0132 | 1.0648 | 1.0834 |
| R1_CreateConstantRaster | 0.1605 | 0.0880 | 0.0983 | 0.2227 |
| R2_Resample | 0.2105 | 0.0073 | 0.2054 | 0.2157 |
| R3_Clip | 0.2595 | 0.0171 | 0.2475 | 0.2716 |
| R4_RasterCalculator | 0.3160 | 0.0197 | 0.3020 | 0.3299 |
| M1_PolygonToRaster | 1.0547 | 0.0181 | 1.0419 | 1.0675 |
| M2_RasterToPoint | 12.7751 | 0.0241 | 12.7580 | 12.7921 |
| Py2_MP_V1_CreateFishnet_single | 0.1895 | 0.0094 | 0.1829 | 0.1961 |
| Py2_MP_V1_CreateFishnet_multiprocess | 0.7057 | 0.0090 | 0.6993 | 0.7121 |
| Py2_MP_V2_CreateRandomPoints_single | 0.0846 | 0.0006 | 0.0842 | 0.0850 |
| Py2_MP_V2_CreateRandomPoints_multiprocess | 0.3661 | 0.0155 | 0.3552 | 0.3771 |
| Py2_MP_V3_Buffer_single | 3.6607 | 0.3312 | 3.4265 | 3.8948 |
| Py2_MP_V3_Buffer_multiprocess | 4.7888 | 0.3775 | 4.5219 | 5.0558 |
| Py2_MP_V4_Intersect_single | 0.2931 | 0.0212 | 0.2781 | 0.3081 |
| Py2_MP_V4_Intersect_multiprocess | 2.9163 | 0.0204 | 2.9019 | 2.9307 |
| Py2_MP_R1_CreateConstantRaster_single | 0.0878 | 0.0143 | 0.0776 | 0.0979 |
| Py2_MP_R1_CreateConstantRaster_multiprocess | 0.5920 | 0.0977 | 0.5228 | 0.6611 |

## Detailed Results

### V1_CreateFishnet

- **all_times**: [0.788995, 0.19859800000000005]
- **avg_memory_mb**: 194.2109375
- **category**: vector
- **cv_percent**: 84.5436778698
- **failed_runs**: 0
- **max_time**: 0.788995
- **mean_time**: 0.4937965
- **min_time**: 0.198598
- **python_version**: 2.7.16
- **std_time**: 0.417473722292
- **success**: True
- **successful_runs**: 2
- **test_name**: V1_CreateFishnet
- **total_runs**: 2

### V2_CreateRandomPoints

- **all_times**: [0.09257660000000012, 0.0864499999999997]
- **avg_memory_mb**: 195.9140625
- **category**: vector
- **cv_percent**: 4.83968349465
- **failed_runs**: 0
- **max_time**: 0.0925766
- **mean_time**: 0.0895133
- **min_time**: 0.08645
- **python_version**: 2.7.16
- **std_time**: 0.00433216040562
- **success**: True
- **successful_runs**: 2
- **test_name**: V2_CreateRandomPoints
- **total_runs**: 2

### V3_Buffer

- **all_times**: [0.1674306999999997, 0.17018759999999977]
- **avg_memory_mb**: 197.91796875
- **category**: vector
- **cv_percent**: 1.15480866117
- **failed_runs**: 0
- **max_time**: 0.1701876
- **mean_time**: 0.16880915
- **min_time**: 0.1674307
- **python_version**: 2.7.16
- **std_time**: 0.00194942268505
- **success**: True
- **successful_runs**: 2
- **test_name**: V3_Buffer
- **total_runs**: 2

### V4_Intersect

- **all_times**: [0.37009620000000076, 0.3568407999999996]
- **avg_memory_mb**: 201.275390625
- **category**: vector
- **cv_percent**: 2.57876080798
- **failed_runs**: 0
- **max_time**: 0.3700962
- **mean_time**: 0.3634685
- **min_time**: 0.3568408
- **python_version**: 2.7.16
- **std_time**: 0.00937298322734
- **success**: True
- **successful_runs**: 2
- **test_name**: V4_Intersect
- **total_runs**: 2

### V5_SpatialJoin

- **all_times**: [1.2022203999999999, 0.7333822000000003]
- **avg_memory_mb**: 231.517578125
- **category**: vector
- **cv_percent**: 34.2548279796
- **failed_runs**: 0
- **max_time**: 1.2022204
- **mean_time**: 0.9678013
- **min_time**: 0.7333822
- **python_version**: 2.7.16
- **std_time**: 0.331518670499
- **success**: True
- **successful_runs**: 2
- **test_name**: V5_SpatialJoin
- **total_runs**: 2

### V6_CalculateField

- **all_times**: [1.0834403000000012, 1.064759500000001]
- **avg_memory_mb**: 231.99609375
- **category**: vector
- **cv_percent**: 1.22980370429
- **failed_runs**: 0
- **max_time**: 1.0834403
- **mean_time**: 1.0740999
- **min_time**: 1.0647595
- **python_version**: 2.7.16
- **std_time**: 0.013209320358
- **success**: True
- **successful_runs**: 2
- **test_name**: V6_CalculateField
- **total_runs**: 2

### R1_CreateConstantRaster

- **all_times**: [0.22271559999999901, 0.09827759999999941]
- **avg_memory_mb**: 235.099609375
- **category**: raster
- **cv_percent**: 54.8241854577
- **failed_runs**: 0
- **max_time**: 0.2227156
- **mean_time**: 0.1604966
- **min_time**: 0.0982776
- **python_version**: 2.7.16
- **std_time**: 0.0879909536373
- **success**: True
- **successful_runs**: 2
- **test_name**: R1_CreateConstantRaster
- **total_runs**: 2

### R2_Resample

- **all_times**: [0.20537419999999962, 0.2157138000000014]
- **avg_memory_mb**: 238.888671875
- **category**: raster
- **cv_percent**: 3.47252891308
- **failed_runs**: 0
- **max_time**: 0.2157138
- **mean_time**: 0.210544
- **min_time**: 0.2053742
- **python_version**: 2.7.16
- **std_time**: 0.00731120127476
- **success**: True
- **successful_runs**: 2
- **test_name**: R2_Resample
- **total_runs**: 2

### R3_Clip

- **all_times**: [0.24745219999999968, 0.271621399999999]
- **avg_memory_mb**: 239.24609375
- **category**: raster
- **cv_percent**: 6.58488708185
- **failed_runs**: 0
- **max_time**: 0.2716214
- **mean_time**: 0.2595368
- **min_time**: 0.2474522
- **python_version**: 2.7.16
- **std_time**: 0.0170902052159
- **success**: True
- **successful_runs**: 2
- **test_name**: R3_Clip
- **total_runs**: 2

### R4_RasterCalculator

- **all_times**: [0.32994459999999926, 0.3020271999999995]
- **avg_memory_mb**: 240.08984375
- **category**: raster
- **cv_percent**: 6.24729864627
- **failed_runs**: 0
- **max_time**: 0.3299446
- **mean_time**: 0.3159859
- **min_time**: 0.3020272
- **python_version**: 2.7.16
- **std_time**: 0.0197405828531
- **success**: True
- **successful_runs**: 2
- **test_name**: R4_RasterCalculator
- **total_runs**: 2

### M1_PolygonToRaster

- **all_times**: [1.0674642999999975, 1.0418537000000008]
- **avg_memory_mb**: 240.1796875
- **category**: mixed
- **cv_percent**: 1.71708854997
- **failed_runs**: 0
- **max_time**: 1.0674643
- **mean_time**: 1.054659
- **min_time**: 1.0418537
- **python_version**: 2.7.16
- **std_time**: 0.0181094289303
- **success**: True
- **successful_runs**: 2
- **test_name**: M1_PolygonToRaster
- **total_runs**: 2

### M2_RasterToPoint

- **all_times**: [12.792110199999996, 12.7579967]
- **avg_memory_mb**: 242.927734375
- **category**: mixed
- **cv_percent**: 0.188820244662
- **failed_runs**: 0
- **max_time**: 12.7921102
- **mean_time**: 12.77505345
- **min_time**: 12.7579967
- **python_version**: 2.7.16
- **std_time**: 0.02412188718
- **success**: True
- **successful_runs**: 2
- **test_name**: M2_RasterToPoint
- **total_runs**: 2

### Py2_MP_V1_CreateFishnet_single

- **all_times**: [0.1828634999999963, 0.19608949999999936]
- **avg_memory_mb**: 241.08984375
- **category**: vector_multiprocess
- **cv_percent**: 4.93580696708
- **failed_runs**: 0
- **max_time**: 0.1960895
- **mean_time**: 0.1894765
- **min_time**: 0.1828635
- **python_version**: 2.7.16
- **std_time**: 0.00935219428798
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V1_CreateFishnet_single
- **total_runs**: 2

### Py2_MP_V1_CreateFishnet_multiprocess

- **all_times**: [0.699335799999993, 0.7120783000000017]
- **avg_memory_mb**: 242.90234375
- **category**: vector_multiprocess
- **cv_percent**: 1.27677740491
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 0.7120783
- **mean_time**: 0.70570705
- **min_time**: 0.6993358
- **num_workers**: 4
- **parallel_efficiency**: 6.71229301167
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.268491720467
- **std_time**: 0.00901030815928
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V1_CreateFishnet_multiprocess
- **total_runs**: 2

### Py2_MP_V2_CreateRandomPoints_single

- **all_times**: [0.0841861000000037, 0.08496819999999872]
- **avg_memory_mb**: 243.748046875
- **category**: vector_multiprocess
- **cv_percent**: 0.653874259847
- **failed_runs**: 0
- **max_time**: 0.0849682
- **mean_time**: 0.08457715
- **min_time**: 0.0841861
- **python_version**: 2.7.16
- **std_time**: 0.000553028213562
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V2_CreateRandomPoints_single
- **total_runs**: 2

### Py2_MP_V2_CreateRandomPoints_multiprocess

- **all_times**: [0.3552008999999998, 0.3770753999999954]
- **avg_memory_mb**: 243.787109375
- **category**: vector_multiprocess
- **cv_percent**: 4.22452762299
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 0.3770754
- **mean_time**: 0.36613815
- **min_time**: 0.3552009
- **num_workers**: 4
- **parallel_efficiency**: 5.77494792608
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.230997917043
- **std_time**: 0.0154676072851
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V2_CreateRandomPoints_multiprocess
- **total_runs**: 2

### Py2_MP_V3_Buffer_single

- **all_times**: [3.426498600000002, 3.894840000000002]
- **avg_memory_mb**: 244.4375
- **category**: vector_multiprocess
- **cv_percent**: 9.04663471924
- **failed_runs**: 0
- **max_time**: 3.89484
- **mean_time**: 3.6606693
- **min_time**: 3.4264986
- **python_version**: 2.7.16
- **std_time**: 0.33116737985
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V3_Buffer_single
- **total_runs**: 2

### Py2_MP_V3_Buffer_multiprocess

- **all_times**: [5.055753300000006, 4.5219100999999995]
- **avg_memory_mb**: 248.494140625
- **category**: vector_multiprocess
- **cv_percent**: 7.88259371926
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 5.0557533
- **mean_time**: 4.7888317
- **min_time**: 4.5219101
- **num_workers**: 4
- **parallel_efficiency**: 19.1104507807
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.764418031229
- **std_time**: 0.37748414681
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V3_Buffer_multiprocess
- **total_runs**: 2

### Py2_MP_V4_Intersect_single

- **all_times**: [0.2780817999999954, 0.30809039999999754]
- **avg_memory_mb**: 253.982421875
- **category**: vector_multiprocess
- **cv_percent**: 7.23994913233
- **failed_runs**: 0
- **max_time**: 0.3080904
- **mean_time**: 0.2930861
- **min_time**: 0.2780818
- **python_version**: 2.7.16
- **std_time**: 0.0212192845539
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V4_Intersect_single
- **total_runs**: 2

### Py2_MP_V4_Intersect_multiprocess

- **all_times**: [2.9307388000000003, 2.901920700000005]
- **avg_memory_mb**: 255.9375
- **category**: vector_multiprocess
- **cv_percent**: 0.698736963161
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 2.9307388
- **mean_time**: 2.91632975
- **min_time**: 2.9019207
- **num_workers**: 4
- **parallel_efficiency**: 2.51245679608
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.100498271843
- **std_time**: 0.0203774739309
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V4_Intersect_multiprocess
- **total_runs**: 2

### Py2_MP_R1_CreateConstantRaster_single

- **all_times**: [0.07762710000000084, 0.09789200000000164]
- **avg_memory_mb**: 257.203125
- **category**: raster_multiprocess
- **cv_percent**: 16.3280784941
- **failed_runs**: 0
- **max_time**: 0.097892
- **mean_time**: 0.08775955
- **min_time**: 0.0776271
- **python_version**: 2.7.16
- **std_time**: 0.0143294482101
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_R1_CreateConstantRaster_single
- **total_runs**: 2

### Py2_MP_R1_CreateConstantRaster_multiprocess

- **all_times**: [0.6610656000000006, 0.5228361000000064]
- **avg_memory_mb**: 258.037109375
- **category**: raster_multiprocess
- **cv_percent**: 16.5120156192
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 0.6610656
- **mean_time**: 0.59195085
- **min_time**: 0.5228361
- **num_workers**: 4
- **parallel_efficiency**: 3.70636979405
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.148254791762
- **std_time**: 0.09774301681
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_R1_CreateConstantRaster_multiprocess
- **total_runs**: 2
