# Benchmark Results (py3)

*Generated on 2026-03-30 11:41:04*

## Summary

| Test Name | Mean Time | Std Time | Min Time | Max Time |
|---|---|---|---|---|
| V1_CreateFishnet | 0.6714 | 0.3537 | 0.4214 | 0.9215 |
| V2_CreateRandomPoints | 0.2560 | 0.0482 | 0.2219 | 0.2900 |
| V3_Buffer | 0.4086 | 0.0070 | 0.4037 | 0.4136 |
| V4_Intersect | 0.4543 | 0.0369 | 0.4282 | 0.4804 |
| V5_SpatialJoin | 2.3392 | 0.1063 | 2.2640 | 2.4144 |
| V6_CalculateField | 1.5055 | 0.0152 | 1.4947 | 1.5162 |
| V1_CreateFishnet_OS | 0.1044 | 0.0321 | 0.0817 | 0.1270 |
| V2_CreateRandomPoints_OS | 0.0506 | 0.0360 | 0.0251 | 0.0761 |
| V3_Buffer_OS |  |  |  |  |
| V4_Intersect_OS |  |  |  |  |
| V5_SpatialJoin_OS |  |  |  |  |
| V6_CalculateField_OS |  |  |  |  |
| R1_CreateConstantRaster | 1.1418 | 1.0930 | 0.3689 | 1.9146 |
| R2_Resample | 0.6264 | 0.0779 | 0.5713 | 0.6816 |
| R3_Clip | 0.4372 | 0.0941 | 0.3707 | 0.5038 |
| R4_RasterCalculator | 0.4297 | 0.1262 | 0.3404 | 0.5189 |
| R1_CreateConstantRaster_OS | 0.0130 | 0.0114 | 0.0050 | 0.0211 |
| R2_Resample_OS |  |  |  |  |
| R3_Clip_OS |  |  |  |  |
| R4_RasterCalculator_OS |  |  |  |  |
| M1_PolygonToRaster | 0.9559 | 0.0690 | 0.9071 | 1.0047 |
| M2_RasterToPoint | 12.1078 | 0.0591 | 12.0660 | 12.1497 |
| M1_PolygonToRaster_OS |  |  |  |  |
| M2_RasterToPoint_OS |  |  |  |  |
| Py3_MP_V1_CreateFishnet_single | 0.4224 | 0.0534 | 0.3847 | 0.4602 |
| Py3_MP_V1_CreateFishnet_multiprocess | 1.2908 | 0.0599 | 1.2484 | 1.3332 |
| Py3_MP_V2_CreateRandomPoints_single | 0.2527 | 0.0437 | 0.2219 | 0.2836 |
| Py3_MP_V2_CreateRandomPoints_multiprocess | 0.8698 | 0.0778 | 0.8148 | 0.9249 |
| Py3_MP_V3_Buffer_single | 0.9270 | 0.0033 | 0.9246 | 0.9293 |
| Py3_MP_V3_Buffer_multiprocess | 2.4018 | 0.1823 | 2.2728 | 2.5307 |
| Py3_MP_V4_Intersect_single | 0.3602 | 0.0457 | 0.3279 | 0.3925 |
| Py3_MP_V4_Intersect_multiprocess | 2.7917 | 0.1089 | 2.7147 | 2.8687 |
| Py3_MP_R1_CreateConstantRaster_single | 0.2089 | 0.0598 | 0.1666 | 0.2512 |
| Py3_MP_R1_CreateConstantRaster_multiprocess | 1.0869 | 0.0873 | 1.0252 | 1.1486 |

## Detailed Results

### V1_CreateFishnet

- **all_times**: [0.9215147000213619, 0.42135079999570735]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 52.67382108012384
- **failed_runs**: 0
- **max_time**: 0.9215147000213619
- **mean_time**: 0.6714327500085346
- **min_time**: 0.42135079999570735
- **python_version**: 3.13.7
- **std_time**: 0.35366928541285075
- **success**: True
- **successful_runs**: 2
- **test_name**: V1_CreateFishnet
- **total_runs**: 2

### V2_CreateRandomPoints

- **all_times**: [0.22190440000849776, 0.2900087999878451]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 18.81455022233516
- **failed_runs**: 0
- **max_time**: 0.2900087999878451
- **mean_time**: 0.25595659999817144
- **min_time**: 0.22190440000849776
- **python_version**: 3.13.7
- **std_time**: 0.048157083054037486
- **success**: True
- **successful_runs**: 2
- **test_name**: V2_CreateRandomPoints
- **total_runs**: 2

### V3_Buffer

- **all_times**: [0.403706199984299, 0.41355999998631887]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 1.7051210002652144
- **failed_runs**: 0
- **max_time**: 0.41355999998631887
- **mean_time**: 0.40863309998530895
- **min_time**: 0.403706199984299
- **python_version**: 3.13.7
- **std_time**: 0.006967688801884253
- **success**: True
- **successful_runs**: 2
- **test_name**: V3_Buffer
- **total_runs**: 2

### V4_Intersect

- **all_times**: [0.42816129999118857, 0.48037900001509115]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 8.128090693304689
- **failed_runs**: 0
- **max_time**: 0.48037900001509115
- **mean_time**: 0.45427015000313986
- **min_time**: 0.42816129999118857
- **python_version**: 3.13.7
- **std_time**: 0.03692348978486646
- **success**: True
- **successful_runs**: 2
- **test_name**: V4_Intersect
- **total_runs**: 2

### V5_SpatialJoin

- **all_times**: [2.264009599981364, 2.4143796999996994]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 4.545483951542674
- **failed_runs**: 0
- **max_time**: 2.4143796999996994
- **mean_time**: 2.3391946499905316
- **min_time**: 2.264009599981364
- **python_version**: 3.13.7
- **std_time**: 0.10632771741066444
- **success**: True
- **successful_runs**: 2
- **test_name**: V5_SpatialJoin
- **total_runs**: 2

### V6_CalculateField

- **all_times**: [1.4946945999981835, 1.5162219000048935]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 1.0111273305232005
- **failed_runs**: 0
- **max_time**: 1.5162219000048935
- **mean_time**: 1.5054582500015385
- **min_time**: 1.4946945999981835
- **python_version**: 3.13.7
- **std_time**: 0.015222099815381846
- **success**: True
- **successful_runs**: 2
- **test_name**: V6_CalculateField
- **total_runs**: 2

### V1_CreateFishnet_OS

- **all_times**: [0.08166470000287518, 0.12704910000320524]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 30.751792166479852
- **failed_runs**: 0
- **max_time**: 0.12704910000320524
- **mean_time**: 0.10435690000304021
- **min_time**: 0.08166470000287518
- **python_version**: 3.13.7
- **std_time**: 0.03209161700031613
- **success**: True
- **successful_runs**: 2
- **test_name**: V1_CreateFishnet_OS
- **total_runs**: 2

### V2_CreateRandomPoints_OS

- **all_times**: [0.025148099986836314, 0.07608210001490079]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 71.15619017285782
- **failed_runs**: 0
- **max_time**: 0.07608210001490079
- **mean_time**: 0.05061510000086855
- **min_time**: 0.025148099986836314
- **python_version**: 3.13.7
- **std_time**: 0.03601577681280019
- **success**: True
- **successful_runs**: 2
- **test_name**: V2_CreateRandomPoints_OS
- **total_runs**: 2

### V3_Buffer_OS

- **category**: vector_os
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: V3_Buffer_OS
- **total_runs**: 2

### V4_Intersect_OS

- **category**: vector_os
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: V4_Intersect_OS
- **total_runs**: 2

### V5_SpatialJoin_OS

- **category**: vector_os
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: V5_SpatialJoin_OS
- **total_runs**: 2

### V6_CalculateField_OS

- **category**: vector_os
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: V6_CalculateField_OS
- **total_runs**: 2

### R1_CreateConstantRaster

- **all_times**: [1.9146468999970239, 0.36893210001289845]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 95.72564967924771
- **failed_runs**: 0
- **max_time**: 1.9146468999970239
- **mean_time**: 1.1417895000049612
- **min_time**: 0.36893210001289845
- **python_version**: 3.13.7
- **std_time**: 1.092985416849183
- **success**: True
- **successful_runs**: 2
- **test_name**: R1_CreateConstantRaster
- **total_runs**: 2

### R2_Resample

- **all_times**: [0.5713261000055354, 0.6815566000004765]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 12.442463135556507
- **failed_runs**: 0
- **max_time**: 0.6815566000004765
- **mean_time**: 0.6264413500030059
- **min_time**: 0.5713261000055354
- **python_version**: 3.13.7
- **std_time**: 0.07794473404000651
- **success**: True
- **successful_runs**: 2
- **test_name**: R2_Resample
- **total_runs**: 2

### R3_Clip

- **all_times**: [0.37071560000185855, 0.5037512999842875]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 21.514924258188593
- **failed_runs**: 0
- **max_time**: 0.5037512999842875
- **mean_time**: 0.437233449993073
- **min_time**: 0.37071560000185855
- **python_version**: 3.13.7
- **std_time**: 0.09407044559747456
- **success**: True
- **successful_runs**: 2
- **test_name**: R3_Clip
- **total_runs**: 2

### R4_RasterCalculator

- **all_times**: [0.5188934000034351, 0.3404234999907203]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 29.371533723480603
- **failed_runs**: 0
- **max_time**: 0.5188934000034351
- **mean_time**: 0.4296584499970777
- **min_time**: 0.3404234999907203
- **python_version**: 3.13.7
- **std_time**: 0.12619727653667573
- **success**: True
- **successful_runs**: 2
- **test_name**: R4_RasterCalculator
- **total_runs**: 2

### R1_CreateConstantRaster_OS

- **all_times**: [0.021116300020366907, 0.004968699999153614]
- **avg_memory_mb**: 0.0
- **category**: raster_os
- **cv_percent**: 87.5451597956168
- **failed_runs**: 0
- **max_time**: 0.021116300020366907
- **mean_time**: 0.01304250000976026
- **min_time**: 0.004968699999153614
- **python_version**: 3.13.7
- **std_time**: 0.011418077474887958
- **success**: True
- **successful_runs**: 2
- **test_name**: R1_CreateConstantRaster_OS
- **total_runs**: 2

### R2_Resample_OS

- **category**: raster_os
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: R2_Resample_OS
- **total_runs**: 2

### R3_Clip_OS

- **category**: raster_os
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: R3_Clip_OS
- **total_runs**: 2

### R4_RasterCalculator_OS

- **category**: raster_os
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: R4_RasterCalculator_OS
- **total_runs**: 2

### M1_PolygonToRaster

- **all_times**: [0.907105699996464, 1.004733900015708]
- **avg_memory_mb**: 0.0
- **category**: mixed
- **cv_percent**: 7.221689755584583
- **failed_runs**: 0
- **max_time**: 1.004733900015708
- **mean_time**: 0.955919800006086
- **min_time**: 0.907105699996464
- **python_version**: 3.13.7
- **std_time**: 0.06903356226864414
- **success**: True
- **successful_runs**: 2
- **test_name**: M1_PolygonToRaster
- **total_runs**: 2

### M2_RasterToPoint

- **all_times**: [12.066033400013112, 12.149661799980095]
- **avg_memory_mb**: 0.0
- **category**: mixed
- **cv_percent**: 0.48839571383811603
- **failed_runs**: 0
- **max_time**: 12.149661799980095
- **mean_time**: 12.107847599996603
- **min_time**: 12.066033400013112
- **python_version**: 3.13.7
- **std_time**: 0.059134208716434614
- **success**: True
- **successful_runs**: 2
- **test_name**: M2_RasterToPoint
- **total_runs**: 2

### M1_PolygonToRaster_OS

- **category**: mixed_os
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: M1_PolygonToRaster_OS
- **total_runs**: 2

### M2_RasterToPoint_OS

- **category**: mixed_os
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: M2_RasterToPoint_OS
- **total_runs**: 2

### Py3_MP_V1_CreateFishnet_single

- **all_times**: [0.3846886999963317, 0.460198799992213]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 12.639245758964574
- **failed_runs**: 0
- **max_time**: 0.460198799992213
- **mean_time**: 0.42244374999427237
- **min_time**: 0.3846886999963317
- **python_version**: 3.13.7
- **std_time**: 0.053393703755161975
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V1_CreateFishnet_single
- **total_runs**: 2

### Py3_MP_V1_CreateFishnet_multiprocess

- **all_times**: [1.248422100004973, 1.3331818000006024]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 4.643172303707595
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 1.3331818000006024
- **mean_time**: 1.2908019500027876
- **min_time**: 1.248422100004973
- **num_workers**: 2
- **parallel_efficiency**: 16.36361604479138
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.32727232089582764
- **std_time**: 0.05993415863824699
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V1_CreateFishnet_multiprocess
- **total_runs**: 2

### Py3_MP_V2_CreateRandomPoints_single

- **all_times**: [0.2218546999793034, 0.28361990000121295]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 17.280627662999954
- **failed_runs**: 0
- **max_time**: 0.28361990000121295
- **mean_time**: 0.2527372999902582
- **min_time**: 0.2218546999793034
- **python_version**: 3.13.7
- **std_time**: 0.04367459177683573
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V2_CreateRandomPoints_single
- **total_runs**: 2

### Py3_MP_V2_CreateRandomPoints_multiprocess

- **all_times**: [0.8147811000235379, 0.9248635999974795]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 8.948963224571273
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 0.9248635999974795
- **mean_time**: 0.8698223500105087
- **min_time**: 0.8147811000235379
- **num_workers**: 2
- **parallel_efficiency**: 14.528098754142427
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.29056197508284853
- **std_time**: 0.07784008222154204
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V2_CreateRandomPoints_multiprocess
- **total_runs**: 2

### Py3_MP_V3_Buffer_single

- **all_times**: [0.9293103000090923, 0.9245902999828104]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 0.3600564157322359
- **failed_runs**: 0
- **max_time**: 0.9293103000090923
- **mean_time**: 0.9269502999959514
- **min_time**: 0.9245902999828104
- **python_version**: 3.13.7
- **std_time**: 0.0033375440257846305
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V3_Buffer_single
- **total_runs**: 2

### Py3_MP_V3_Buffer_multiprocess

- **all_times**: [2.530700200004503, 2.2728447999979835]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 7.591530917690388
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 2.530700200004503
- **mean_time**: 2.4017725000012433
- **min_time**: 2.2728447999979835
- **num_workers**: 2
- **parallel_efficiency**: 19.297212787544854
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.3859442557508971
- **std_time**: 0.18233130191017977
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V3_Buffer_multiprocess
- **total_runs**: 2

### Py3_MP_V4_Intersect_single

- **all_times**: [0.3279133999894839, 0.3925181000086013]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 12.681961152493205
- **failed_runs**: 0
- **max_time**: 0.3925181000086013
- **mean_time**: 0.3602157499990426
- **min_time**: 0.3279133999894839
- **python_version**: 3.13.7
- **std_time**: 0.04568242148004062
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V4_Intersect_single
- **total_runs**: 2

### Py3_MP_V4_Intersect_multiprocess

- **all_times**: [2.714665600011358, 2.8687320000026375]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 3.902333453256478
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 2.8687320000026375
- **mean_time**: 2.7916988000069978
- **min_time**: 2.714665600011358
- **num_workers**: 2
- **parallel_efficiency**: 6.451551112858946
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.1290310222571789
- **std_time**: 0.10894139618683275
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V4_Intersect_multiprocess
- **total_runs**: 2

### Py3_MP_R1_CreateConstantRaster_single

- **all_times**: [0.16664270000183024, 0.25123639998491853]
- **avg_memory_mb**: 0.0
- **category**: raster_multiprocess
- **cv_percent**: 28.628748796290072
- **failed_runs**: 0
- **max_time**: 0.25123639998491853
- **mean_time**: 0.20893954999337438
- **min_time**: 0.16664270000183024
- **python_version**: 3.13.7
- **std_time**: 0.059816778903702066
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_R1_CreateConstantRaster_single
- **total_runs**: 2

### Py3_MP_R1_CreateConstantRaster_multiprocess

- **all_times**: [1.02519499999471, 1.1486262000107672]
- **avg_memory_mb**: 0.0
- **category**: raster_multiprocess
- **cv_percent**: 8.03001079767988
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 1.1486262000107672
- **mean_time**: 1.0869106000027386
- **min_time**: 1.02519499999471
- **num_workers**: 2
- **parallel_efficiency**: 9.611625371619704
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.1922325074323941
- **std_time**: 0.08727903854134708
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_R1_CreateConstantRaster_multiprocess
- **total_runs**: 2
