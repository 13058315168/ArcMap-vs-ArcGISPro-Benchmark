# Benchmark Results (py3)

*Generated on 2026-03-30 23:25:06*

## Summary

| Test Name | Mean Time | Std Time | Min Time | Max Time |
|---|---|---|---|---|
| V1_CreateFishnet | 0.3855 | 0.0110 | 0.3772 | 0.3979 |
| V2_CreateRandomPoints | 0.2596 | 0.0128 | 0.2475 | 0.2730 |
| V3_Buffer | 0.3461 | 0.0035 | 0.3440 | 0.3501 |
| V4_Intersect | 0.3908 | 0.0013 | 0.3894 | 0.3919 |
| V5_SpatialJoin | 2.2440 | 0.0252 | 2.2152 | 2.2619 |
| V6_CalculateField | 1.5960 | 0.3469 | 1.3780 | 1.9959 |
| R1_CreateConstantRaster | 0.3264 | 0.0127 | 0.3143 | 0.3397 |
| R2_Resample | 0.6073 | 0.0172 | 0.5968 | 0.6271 |
| R3_Clip | 0.4217 | 0.0108 | 0.4102 | 0.4317 |
| R4_RasterCalculator | 0.2852 | 0.0081 | 0.2803 | 0.2946 |
| M1_PolygonToRaster | 0.8400 | 0.0142 | 0.8242 | 0.8516 |
| M2_RasterToPoint | N/A | N/A | N/A | N/A |
| V1_CreateFishnet_OS | 0.0853 | 0.0039 | 0.0822 | 0.0897 |
| V2_CreateRandomPoints_OS | 0.0554 | 0.0103 | 0.0466 | 0.0668 |
| V3_Buffer_OS | 0.1049 | 0.0015 | 0.1033 | 0.1063 |
| V4_Intersect_OS | 1.2908 | 0.0042 | 1.2861 | 1.2940 |
| V5_SpatialJoin_OS | 0.1655 | 0.0069 | 0.1599 | 0.1732 |
| V6_CalculateField_OS | 0.2326 | 0.0233 | 0.2110 | 0.2573 |
| R1_CreateConstantRaster_OS | 0.0050 | 0.0010 | 0.0040 | 0.0060 |
| R2_Resample_OS | 0.0070 | 0.0012 | 0.0057 | 0.0082 |
| R3_Clip_OS | 0.0065 | 0.0011 | 0.0053 | 0.0072 |
| R4_RasterCalculator_OS | 0.0060 | 0.0008 | 0.0052 | 0.0067 |
| M1_PolygonToRaster_OS | 0.3911 | 0.0177 | 0.3800 | 0.4115 |
| M2_RasterToPoint_OS | 2.4182 | 0.0079 | 2.4112 | 2.4267 |
| Py3_MP_V1_CreateFishnet_single | 0.4068 | 0.0088 | 0.3974 | 0.4149 |
| Py3_MP_V1_CreateFishnet_multiprocess | 1.2428 | 0.0158 | 1.2305 | 1.2607 |
| Py3_MP_V2_CreateRandomPoints_single | 0.2689 | 0.0054 | 0.2643 | 0.2748 |
| Py3_MP_V2_CreateRandomPoints_multiprocess | 0.8524 | 0.0554 | 0.8190 | 0.9164 |
| Py3_MP_V3_Buffer_single | 0.7907 | 0.0096 | 0.7802 | 0.7992 |
| Py3_MP_V3_Buffer_multiprocess | 2.3736 | 0.1103 | 2.2747 | 2.4925 |
| Py3_MP_V4_Intersect_single | 0.4054 | 0.0148 | 0.3934 | 0.4220 |
| Py3_MP_V4_Intersect_multiprocess | 3.2162 | 0.0586 | 3.1486 | 3.2529 |
| Py3_MP_R1_CreateConstantRaster_single | 0.2623 | 0.0008 | 0.2615 | 0.2631 |
| Py3_MP_R1_CreateConstantRaster_multiprocess | 1.1812 | 0.0123 | 1.1703 | 1.1946 |
| OS_MP_V1_CreateFishnet_single | 0.0884 | 0.0050 | 0.0825 | 0.0913 |
| OS_MP_V1_CreateFishnet_multiprocess | 11.7341 | 1.8977 | 9.5910 | 13.2010 |
| OS_MP_V2_CreateRandomPoints_single | 0.0563 | 0.0006 | 0.0558 | 0.0569 |
| OS_MP_V2_CreateRandomPoints_multiprocess | 10.4311 | 0.8469 | 9.4542 | 10.9571 |
| OS_MP_V3_Buffer_single | 0.1241 | 0.0048 | 0.1198 | 0.1293 |
| OS_MP_V3_Buffer_multiprocess | 9.4857 | 1.5733 | 8.0943 | 11.1930 |

## Detailed Results

### V1_CreateFishnet

- **all_times**: [0.3979418000089936, 0.3771835000079591, 0.38126660001580603]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 2.8529982215136465
- **failed_runs**: 0
- **max_time**: 0.3979418000089936
- **mean_time**: 0.38546396667758626
- **min_time**: 0.3771835000079591
- **python_version**: 3.13.7
- **std_time**: 0.010997280113887491
- **success**: True
- **successful_runs**: 3
- **test_name**: V1_CreateFishnet
- **total_runs**: 3

### V2_CreateRandomPoints

- **all_times**: [0.2583992999861948, 0.24746550002600998, 0.2729698999901302]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 4.92864896586107
- **failed_runs**: 0
- **max_time**: 0.2729698999901302
- **mean_time**: 0.259611566667445
- **min_time**: 0.24746550002600998
- **python_version**: 3.13.7
- **std_time**: 0.012795342795810752
- **success**: True
- **successful_runs**: 3
- **test_name**: V2_CreateRandomPoints
- **total_runs**: 3

### V3_Buffer

- **all_times**: [0.34410759998718277, 0.34403380000730976, 0.35005370000726543]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 0.9982180855524609
- **failed_runs**: 0
- **max_time**: 0.35005370000726543
- **mean_time**: 0.3460650333339193
- **min_time**: 0.34403380000730976
- **python_version**: 3.13.7
- **std_time**: 0.003454483750512335
- **success**: True
- **successful_runs**: 3
- **test_name**: V3_Buffer
- **total_runs**: 3

### V4_Intersect

- **all_times**: [0.3894161000207532, 0.39116630001808517, 0.39187500000116415]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 0.3238526194885794
- **failed_runs**: 0
- **max_time**: 0.39187500000116415
- **mean_time**: 0.3908191333466675
- **min_time**: 0.3894161000207532
- **python_version**: 3.13.7
- **std_time**: 0.0012656780008057469
- **success**: True
- **successful_runs**: 3
- **test_name**: V4_Intersect
- **total_runs**: 3

### V5_SpatialJoin

- **all_times**: [2.2151716999942437, 2.2548453000199515, 2.2619203999929596]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 1.122894937513631
- **failed_runs**: 0
- **max_time**: 2.2619203999929596
- **mean_time**: 2.2439791333357184
- **min_time**: 2.2151716999942437
- **python_version**: 3.13.7
- **std_time**: 0.025197528087089034
- **success**: True
- **successful_runs**: 3
- **test_name**: V5_SpatialJoin
- **total_runs**: 3

### V6_CalculateField

- **all_times**: [1.9959462999831885, 1.3779717000143137, 1.4139555000001565]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 21.73410210412009
- **failed_runs**: 0
- **max_time**: 1.9959462999831885
- **mean_time**: 1.5959578333325528
- **min_time**: 1.3779717000143137
- **python_version**: 3.13.7
- **std_time**: 0.34686710503519974
- **success**: True
- **successful_runs**: 3
- **test_name**: V6_CalculateField
- **total_runs**: 3

### R1_CreateConstantRaster

- **all_times**: [0.3397134999977425, 0.3143240000063088, 0.32526459998916835]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 3.901273290527803
- **failed_runs**: 0
- **max_time**: 0.3397134999977425
- **mean_time**: 0.3264340333310732
- **min_time**: 0.3143240000063088
- **python_version**: 3.13.7
- **std_time**: 0.012735083753537782
- **success**: True
- **successful_runs**: 3
- **test_name**: R1_CreateConstantRaster
- **total_runs**: 3

### R2_Resample

- **all_times**: [0.5968320999818388, 0.5978660000255331, 0.6270535999792628]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 2.8254760563485504
- **failed_runs**: 0
- **max_time**: 0.6270535999792628
- **mean_time**: 0.6072505666622116
- **min_time**: 0.5968320999818388
- **python_version**: 3.13.7
- **std_time**: 0.017157719363081678
- **success**: True
- **successful_runs**: 3
- **test_name**: R2_Resample
- **total_runs**: 3

### R3_Clip

- **all_times**: [0.41020040001603775, 0.4231961000186857, 0.43173270000261255]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 2.5711593958320464
- **failed_runs**: 0
- **max_time**: 0.43173270000261255
- **mean_time**: 0.42170973334577866
- **min_time**: 0.41020040001603775
- **python_version**: 3.13.7
- **std_time**: 0.010842829432058257
- **success**: True
- **successful_runs**: 3
- **test_name**: R3_Clip
- **total_runs**: 3

### R4_RasterCalculator

- **all_times**: [0.2946251000103075, 0.2802992000069935, 0.28081460000248626]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 2.8488944909218943
- **failed_runs**: 0
- **max_time**: 0.2946251000103075
- **mean_time**: 0.28524630000659573
- **min_time**: 0.2802992000069935
- **python_version**: 3.13.7
- **std_time**: 0.008126366126446445
- **success**: True
- **successful_runs**: 3
- **test_name**: R4_RasterCalculator
- **total_runs**: 3

### M1_PolygonToRaster

- **all_times**: [0.8242059999902267, 0.8515759000147227, 0.8443463000003248]
- **avg_memory_mb**: 0.0
- **category**: mixed
- **cv_percent**: 1.6884121572968318
- **failed_runs**: 0
- **max_time**: 0.8515759000147227
- **mean_time**: 0.8400427333350914
- **min_time**: 0.8242059999902267
- **python_version**: 3.13.7
- **std_time**: 0.014183383636118287
- **success**: True
- **successful_runs**: 3
- **test_name**: M1_PolygonToRaster
- **total_runs**: 3

### M2_RasterToPoint

- **category**: mixed
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: M2_RasterToPoint
- **total_runs**: 3

### V1_CreateFishnet_OS

- **all_times**: [0.08971319999545813, 0.08216260001063347, 0.08404349998454563]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 4.607553398432032
- **failed_runs**: 0
- **max_time**: 0.08971319999545813
- **mean_time**: 0.08530643333021241
- **min_time**: 0.08216260001063347
- **python_version**: 3.13.7
- **std_time**: 0.0039305394679873575
- **success**: True
- **successful_runs**: 3
- **test_name**: V1_CreateFishnet_OS
- **total_runs**: 3

### V2_CreateRandomPoints_OS

- **all_times**: [0.06676359998527914, 0.04662310000276193, 0.05277350000687875]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 18.635181571318483
- **failed_runs**: 0
- **max_time**: 0.06676359998527914
- **mean_time**: 0.05538673333163994
- **min_time**: 0.04662310000276193
- **python_version**: 3.13.7
- **std_time**: 0.010321418322773076
- **success**: True
- **successful_runs**: 3
- **test_name**: V2_CreateRandomPoints_OS
- **total_runs**: 3

### V3_Buffer_OS

- **all_times**: [0.10634510000818409, 0.10326269999495707, 0.10498800000641495]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 1.4731864086469335
- **failed_runs**: 0
- **max_time**: 0.10634510000818409
- **mean_time**: 0.10486526666985203
- **min_time**: 0.10326269999495707
- **python_version**: 3.13.7
- **std_time**: 0.001544860855971623
- **success**: True
- **successful_runs**: 3
- **test_name**: V3_Buffer_OS
- **total_runs**: 3

### V4_Intersect_OS

- **all_times**: [1.2940487999876495, 1.2923232000030112, 1.28609010000946]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 0.32434310626447543
- **failed_runs**: 0
- **max_time**: 1.2940487999876495
- **mean_time**: 1.2908207000000402
- **min_time**: 1.28609010000946
- **python_version**: 3.13.7
- **std_time**: 0.004186687954684976
- **success**: True
- **successful_runs**: 3
- **test_name**: V4_Intersect_OS
- **total_runs**: 3

### V5_SpatialJoin_OS

- **all_times**: [0.17320699998526834, 0.1598849000001792, 0.16328879998764023]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 4.183126528950944
- **failed_runs**: 0
- **max_time**: 0.17320699998526834
- **mean_time**: 0.16546023332436258
- **min_time**: 0.1598849000001792
- **python_version**: 3.13.7
- **std_time**: 0.006921410915055541
- **success**: True
- **successful_runs**: 3
- **test_name**: V5_SpatialJoin_OS
- **total_runs**: 3

### V6_CalculateField_OS

- **all_times**: [0.22942310001235455, 0.25731630000518635, 0.2109844999795314]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 10.029521847670503
- **failed_runs**: 0
- **max_time**: 0.25731630000518635
- **mean_time**: 0.23257463333235742
- **min_time**: 0.2109844999795314
- **python_version**: 3.13.7
- **std_time**: 0.023326123662208355
- **success**: True
- **successful_runs**: 3
- **test_name**: V6_CalculateField_OS
- **total_runs**: 3

### R1_CreateConstantRaster_OS

- **all_times**: [0.005970400001388043, 0.0051654999842867255, 0.00401209999108687]
- **avg_memory_mb**: 0.0
- **category**: raster_os
- **cv_percent**: 19.493755737677787
- **failed_runs**: 0
- **max_time**: 0.005970400001388043
- **mean_time**: 0.005049333325587213
- **min_time**: 0.00401209999108687
- **python_version**: 3.13.7
- **std_time**: 0.000984304704871134
- **success**: True
- **successful_runs**: 3
- **test_name**: R1_CreateConstantRaster_OS
- **total_runs**: 3

### R2_Resample_OS

- **all_times**: [0.006968799978494644, 0.00819469999987632, 0.005727599986130372]
- **avg_memory_mb**: 0.0
- **category**: raster_os
- **cv_percent**: 17.71411628833172
- **failed_runs**: 0
- **max_time**: 0.00819469999987632
- **mean_time**: 0.006963699988167112
- **min_time**: 0.005727599986130372
- **python_version**: 3.13.7
- **std_time**: 0.0012335579138744645
- **success**: True
- **successful_runs**: 3
- **test_name**: R2_Resample_OS
- **total_runs**: 3

### R3_Clip_OS

- **all_times**: [0.006917699996847659, 0.0072023999819066375, 0.005251800001133233]
- **avg_memory_mb**: 0.0
- **category**: raster_os
- **cv_percent**: 16.317249257337643
- **failed_runs**: 0
- **max_time**: 0.0072023999819066375
- **mean_time**: 0.006457299993295844
- **min_time**: 0.005251800001133233
- **python_version**: 3.13.7
- **std_time**: 0.0010536537352001298
- **success**: True
- **successful_runs**: 3
- **test_name**: R3_Clip_OS
- **total_runs**: 3

### R4_RasterCalculator_OS

- **all_times**: [0.005202300002565607, 0.006738900003256276, 0.006186699989484623]
- **avg_memory_mb**: 0.0
- **category**: raster_os
- **cv_percent**: 12.881213460781685
- **failed_runs**: 0
- **max_time**: 0.006738900003256276
- **mean_time**: 0.006042633331768836
- **min_time**: 0.005202300002565607
- **python_version**: 3.13.7
- **std_time**: 0.0007783644981174882
- **success**: True
- **successful_runs**: 3
- **test_name**: R4_RasterCalculator_OS
- **total_runs**: 3

### M1_PolygonToRaster_OS

- **all_times**: [0.37998729999526404, 0.4115163999958895, 0.38184950000140816]
- **avg_memory_mb**: 0.0
- **category**: mixed_os
- **cv_percent**: 4.523007398164903
- **failed_runs**: 0
- **max_time**: 0.4115163999958895
- **mean_time**: 0.3911177333308539
- **min_time**: 0.37998729999526404
- **python_version**: 3.13.7
- **std_time**: 0.0176902840140894
- **success**: True
- **successful_runs**: 3
- **test_name**: M1_PolygonToRaster_OS
- **total_runs**: 3

### M2_RasterToPoint_OS

- **all_times**: [2.411169600003632, 2.4166071000217926, 2.426673500012839]
- **avg_memory_mb**: 0.0
- **category**: mixed_os
- **cv_percent**: 0.32530137375407836
- **failed_runs**: 0
- **max_time**: 2.426673500012839
- **mean_time**: 2.4181500666794213
- **min_time**: 2.411169600003632
- **python_version**: 3.13.7
- **std_time**: 0.00786627538634332
- **success**: True
- **successful_runs**: 3
- **test_name**: M2_RasterToPoint_OS
- **total_runs**: 3

### Py3_MP_V1_CreateFishnet_single

- **all_times**: [0.3973563999752514, 0.4081603999948129, 0.41487980002420954]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 2.173232536479679
- **failed_runs**: 0
- **max_time**: 0.41487980002420954
- **mean_time**: 0.40679886666475795
- **min_time**: 0.3973563999752514
- **python_version**: 3.13.7
- **std_time**: 0.008840685328389107
- **success**: True
- **successful_runs**: 3
- **test_name**: Py3_MP_V1_CreateFishnet_single
- **total_runs**: 3

### Py3_MP_V1_CreateFishnet_multiprocess

- **all_times**: [1.2373005999834277, 1.2607078999863006, 1.2305085000116378]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 1.2747572119566761
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 1.2607078999863006
- **mean_time**: 1.2428389999937888
- **min_time**: 1.2305085000116378
- **num_workers**: 4
- **parallel_efficiency**: 8.182855274633138
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.32731421098532554
- **std_time**: 0.015843179785431056
- **success**: True
- **successful_runs**: 3
- **test_name**: Py3_MP_V1_CreateFishnet_multiprocess
- **total_runs**: 3

### Py3_MP_V2_CreateRandomPoints_single

- **all_times**: [0.2748470999940764, 0.2676627000037115, 0.26427730001159944]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 2.0070303031735683
- **failed_runs**: 0
- **max_time**: 0.2748470999940764
- **mean_time**: 0.26892903333646245
- **min_time**: 0.26427730001159944
- **python_version**: 3.13.7
- **std_time**: 0.005397487193094549
- **success**: True
- **successful_runs**: 3
- **test_name**: Py3_MP_V2_CreateRandomPoints_single
- **total_runs**: 3

### Py3_MP_V2_CreateRandomPoints_multiprocess

- **all_times**: [0.9163782999967225, 0.821898299996974, 0.8189677999762353]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 6.50075426889664
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 0.9163782999967225
- **mean_time**: 0.8524147999899773
- **min_time**: 0.8189677999762353
- **num_workers**: 4
- **parallel_efficiency**: 7.887270180539583
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.31549080722158335
- **std_time**: 0.0554133914990552
- **success**: True
- **successful_runs**: 3
- **test_name**: Py3_MP_V2_CreateRandomPoints_multiprocess
- **total_runs**: 3

### Py3_MP_V3_Buffer_single

- **all_times**: [0.7926443000033032, 0.7802273000124842, 0.7991979999933392]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 1.2185790993111754
- **failed_runs**: 0
- **max_time**: 0.7991979999933392
- **mean_time**: 0.7906898666697089
- **min_time**: 0.7802273000124842
- **python_version**: 3.13.7
- **std_time**: 0.009635181455608472
- **success**: True
- **successful_runs**: 3
- **test_name**: Py3_MP_V3_Buffer_single
- **total_runs**: 3

### Py3_MP_V3_Buffer_multiprocess

- **all_times**: [2.2746855999866966, 2.353525799990166, 2.4925189999921713]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 4.646668514389909
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 2.4925189999921713
- **mean_time**: 2.373576799989678
- **min_time**: 2.2746855999866966
- **num_workers**: 4
- **parallel_efficiency**: 8.328041741404233
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.3331216696561693
- **std_time**: 0.11029224582998393
- **success**: True
- **successful_runs**: 3
- **test_name**: Py3_MP_V3_Buffer_multiprocess
- **total_runs**: 3

### Py3_MP_V4_Intersect_single

- **all_times**: [0.3933979000139516, 0.40080900001339614, 0.42197150000720285]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 3.6576994312161957
- **failed_runs**: 0
- **max_time**: 0.42197150000720285
- **mean_time**: 0.40539280001151684
- **min_time**: 0.3933979000139516
- **python_version**: 3.13.7
- **std_time**: 0.014828050140212662
- **success**: True
- **successful_runs**: 3
- **test_name**: Py3_MP_V4_Intersect_single
- **total_runs**: 3

### Py3_MP_V4_Intersect_multiprocess

- **all_times**: [3.1485983000020497, 3.247105399990687, 3.2528885999927297]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 1.8224607481044721
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 3.2528885999927297
- **mean_time**: 3.216197433328489
- **min_time**: 3.1485983000020497
- **num_workers**: 4
- **parallel_efficiency**: 3.1511809241758053
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.1260472369670322
- **std_time**: 0.05861393580395521
- **success**: True
- **successful_runs**: 3
- **test_name**: Py3_MP_V4_Intersect_multiprocess
- **total_runs**: 3

### Py3_MP_R1_CreateConstantRaster_single

- **all_times**: [0.26305440001306124, 0.26238410000223666, 0.2615477000072133]
- **avg_memory_mb**: 0.0
- **category**: raster_multiprocess
- **cv_percent**: 0.2877589385184663
- **failed_runs**: 0
- **max_time**: 0.26305440001306124
- **mean_time**: 0.26232873334083706
- **min_time**: 0.2615477000072133
- **python_version**: 3.13.7
- **std_time**: 0.0007548743784905307
- **success**: True
- **successful_runs**: 3
- **test_name**: Py3_MP_R1_CreateConstantRaster_single
- **total_runs**: 3

### Py3_MP_R1_CreateConstantRaster_multiprocess

- **all_times**: [1.1703437000105623, 1.1945778999943286, 1.178717400005553]
- **avg_memory_mb**: 0.0
- **category**: raster_multiprocess
- **cv_percent**: 1.0420081441890783
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 1.1945778999943286
- **mean_time**: 1.1812130000034813
- **min_time**: 1.1703437000105623
- **num_workers**: 4
- **parallel_efficiency**: 5.552104771537054
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.22208419086148215
- **std_time**: 0.012308335660256414
- **success**: True
- **successful_runs**: 3
- **test_name**: Py3_MP_R1_CreateConstantRaster_multiprocess
- **total_runs**: 3

### OS_MP_V1_CreateFishnet_single

- **all_times**: [0.09119629999622703, 0.0825306000187993, 0.09133289998862892]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 5.707813593070041
- **failed_runs**: 0
- **max_time**: 0.09133289998862892
- **mean_time**: 0.08835326666788508
- **min_time**: 0.0825306000187993
- **num_workers**: 1
- **python_version**: 3.13.7
- **std_time**: 0.005043039764790966
- **success**: True
- **successful_runs**: 3
- **test_name**: OS_MP_V1_CreateFishnet_single
- **total_runs**: 3

### OS_MP_V1_CreateFishnet_multiprocess

- **all_times**: [12.410366900003282, 13.2010437999852, 9.590973700018367]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 16.172170570210525
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 13.2010437999852
- **mean_time**: 11.734128133335616
- **min_time**: 9.590973700018367
- **num_workers**: 4
- **parallel_efficiency**: 0.18823994774882613
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.007529597909953045
- **std_time**: 1.8976632166500962
- **success**: True
- **successful_runs**: 3
- **test_name**: OS_MP_V1_CreateFishnet_multiprocess
- **total_runs**: 3

### OS_MP_V2_CreateRandomPoints_single

- **all_times**: [0.055964099999982864, 0.05584129999624565, 0.05694539999240078]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 1.0757748136594851
- **failed_runs**: 0
- **max_time**: 0.05694539999240078
- **mean_time**: 0.056250266662876434
- **min_time**: 0.05584129999624565
- **num_workers**: 1
- **python_version**: 3.13.7
- **std_time**: 0.0006051262013755225
- **success**: True
- **successful_runs**: 3
- **test_name**: OS_MP_V2_CreateRandomPoints_single
- **total_runs**: 3

### OS_MP_V2_CreateRandomPoints_multiprocess

- **all_times**: [10.957121699990239, 10.881930899980944, 9.45418050000444]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 8.11855436228123
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 10.957121699990239
- **mean_time**: 10.431077699991874
- **min_time**: 9.45418050000444
- **num_workers**: 4
- **parallel_efficiency**: 0.13481413014237315
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.005392565205694926
- **std_time**: 0.8468527136456349
- **success**: True
- **successful_runs**: 3
- **test_name**: OS_MP_V2_CreateRandomPoints_multiprocess
- **total_runs**: 3

### OS_MP_V3_Buffer_single

- **all_times**: [0.12323269998887554, 0.11983760001021437, 0.12929919999442063]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 3.86168183315067
- **failed_runs**: 0
- **max_time**: 0.12929919999442063
- **mean_time**: 0.12412316666450351
- **min_time**: 0.11983760001021437
- **num_workers**: 1
- **python_version**: 3.13.7
- **std_time**: 0.004793241777814461
- **success**: True
- **successful_runs**: 3
- **test_name**: OS_MP_V3_Buffer_single
- **total_runs**: 3

### OS_MP_V3_Buffer_multiprocess

- **all_times**: [9.169749699998647, 11.19304790001479, 8.09434730000794]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 16.586290960561193
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 11.19304790001479
- **mean_time**: 9.485714966673791
- **min_time**: 8.09434730000794
- **num_workers**: 4
- **parallel_efficiency**: 0.3271318163696307
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.013085272654785226
- **std_time**: 1.5733282840620153
- **success**: True
- **successful_runs**: 3
- **test_name**: OS_MP_V3_Buffer_multiprocess
- **total_runs**: 3
