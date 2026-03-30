# Benchmark Results (py3)

*Generated on 2026-03-30 13:07:06*

## Summary

| Test Name | Mean Time | Std Time | Min Time | Max Time |
|---|---|---|---|---|
| V1_CreateFishnet | 1.2425 | 0.6805 | 0.7613 | 1.7237 |
| V2_CreateRandomPoints | 0.4593 | 0.0841 | 0.3999 | 0.5187 |
| V3_Buffer | 0.8116 | 0.0706 | 0.7617 | 0.8615 |
| V4_Intersect | 0.7707 | 0.0162 | 0.7592 | 0.7821 |
| V5_SpatialJoin | 5.0861 | 0.2370 | 4.9186 | 5.2537 |
| V6_CalculateField | 3.0112 | 0.0619 | 2.9674 | 3.0550 |
| V1_CreateFishnet_OS | 0.2121 | 0.0515 | 0.1757 | 0.2484 |
| V2_CreateRandomPoints_OS | 0.1161 | 0.0547 | 0.0774 | 0.1548 |
| V3_Buffer_OS | 0.3673 | 0.1211 | 0.2817 | 0.4529 |
| V4_Intersect_OS | 3.1443 | 0.3090 | 2.9257 | 3.3628 |
| V5_SpatialJoin_OS | 0.5559 | 0.0244 | 0.5386 | 0.5731 |
| V6_CalculateField_OS | 0.6821 | 0.0200 | 0.6680 | 0.6963 |
| R1_CreateConstantRaster | 2.4405 | 2.1860 | 0.8948 | 3.9862 |
| R2_Resample | 1.3479 | 0.1276 | 1.2577 | 1.4381 |
| R3_Clip | 0.7670 | 0.0532 | 0.7294 | 0.8046 |
| R4_RasterCalculator | 0.5280 | 0.1038 | 0.4546 | 0.6014 |
| R1_CreateConstantRaster_OS | 0.0453 | 0.0137 | 0.0356 | 0.0550 |
| R2_Resample_OS | 0.0317 | 0.0110 | 0.0239 | 0.0395 |
| R3_Clip_OS | 0.0518 | 0.0169 | 0.0398 | 0.0638 |
| R4_RasterCalculator_OS | 0.0404 | 0.0056 | 0.0364 | 0.0444 |
| M1_PolygonToRaster | 1.7205 | 0.1485 | 1.6154 | 1.8255 |
| M2_RasterToPoint | 22.4147 | 0.2358 | 22.2479 | 22.5814 |
| M1_PolygonToRaster_OS | 0.9247 | 0.0131 | 0.9154 | 0.9340 |
| M2_RasterToPoint_OS | 6.7153 | 0.5033 | 6.3594 | 7.0712 |
| Py3_MP_V1_CreateFishnet_single | 0.7251 | 0.0915 | 0.6604 | 0.7898 |
| Py3_MP_V1_CreateFishnet_multiprocess | 2.6645 | 0.1100 | 2.5867 | 2.7422 |
| Py3_MP_V2_CreateRandomPoints_single | 0.4501 | 0.0490 | 0.4154 | 0.4848 |
| Py3_MP_V2_CreateRandomPoints_multiprocess | 1.9469 | 0.1110 | 1.8684 | 2.0254 |
| Py3_MP_V3_Buffer_single | 2.2413 | 0.0087 | 2.2351 | 2.2475 |
| Py3_MP_V3_Buffer_multiprocess | 5.7457 | 0.1113 | 5.6670 | 5.8244 |
| Py3_MP_V4_Intersect_single | 0.8094 | 0.0387 | 0.7821 | 0.8368 |
| Py3_MP_V4_Intersect_multiprocess | 8.8714 | 2.3085 | 7.2391 | 10.5038 |
| Py3_MP_R1_CreateConstantRaster_single | 0.7526 | 0.2011 | 0.6104 | 0.8948 |
| Py3_MP_R1_CreateConstantRaster_multiprocess | 3.6534 | 0.2447 | 3.4804 | 3.8264 |

## Detailed Results

### V1_CreateFishnet

- **all_times**: [1.7236555000126828, 0.7613224000087939]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 54.76686619765437
- **failed_runs**: 0
- **max_time**: 1.7236555000126828
- **mean_time**: 1.2424889500107383
- **min_time**: 0.7613224000087939
- **python_version**: 3.13.7
- **std_time**: 0.6804722607730218
- **success**: True
- **successful_runs**: 2
- **test_name**: V1_CreateFishnet
- **total_runs**: 2

### V2_CreateRandomPoints

- **all_times**: [0.39986669999780133, 0.5187361999996938]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 18.300275239240303
- **failed_runs**: 0
- **max_time**: 0.5187361999996938
- **mean_time**: 0.45930144999874756
- **min_time**: 0.39986669999780133
- **python_version**: 3.13.7
- **std_time**: 0.08405342952759248
- **success**: True
- **successful_runs**: 2
- **test_name**: V2_CreateRandomPoints
- **total_runs**: 2

### V3_Buffer

- **all_times**: [0.7616565000207629, 0.8614807999983896]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 8.69753155700963
- **failed_runs**: 0
- **max_time**: 0.8614807999983896
- **mean_time**: 0.8115686500095762
- **min_time**: 0.7616565000207629
- **python_version**: 3.13.7
- **std_time**: 0.07058643944137993
- **success**: True
- **successful_runs**: 2
- **test_name**: V3_Buffer
- **total_runs**: 2

### V4_Intersect

- **all_times**: [0.7592215000186116, 0.7820999999821652]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 2.0991782009913953
- **failed_runs**: 0
- **max_time**: 0.7820999999821652
- **mean_time**: 0.7706607500003884
- **min_time**: 0.7592215000186116
- **python_version**: 3.13.7
- **std_time**: 0.016177542467604947
- **success**: True
- **successful_runs**: 2
- **test_name**: V4_Intersect
- **total_runs**: 2

### V5_SpatialJoin

- **all_times**: [4.918557199998759, 5.253703299997142]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 4.659418228567323
- **failed_runs**: 0
- **max_time**: 5.253703299997142
- **mean_time**: 5.08613024999795
- **min_time**: 4.918557199998759
- **python_version**: 3.13.7
- **std_time**: 0.23698407999708127
- **success**: True
- **successful_runs**: 2
- **test_name**: V5_SpatialJoin
- **total_runs**: 2

### V6_CalculateField

- **all_times**: [3.0549773999955505, 2.9674061000114307]
- **avg_memory_mb**: 0.0
- **category**: vector
- **cv_percent**: 2.0564037496456593
- **failed_runs**: 0
- **max_time**: 3.0549773999955505
- **mean_time**: 3.0111917500034906
- **min_time**: 2.9674061000114307
- **python_version**: 3.13.7
- **std_time**: 0.06192226005609253
- **success**: True
- **successful_runs**: 2
- **test_name**: V6_CalculateField
- **total_runs**: 2

### V1_CreateFishnet_OS

- **all_times**: [0.17567649998818524, 0.24843879998661578]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 24.262607713834946
- **failed_runs**: 0
- **max_time**: 0.24843879998661578
- **mean_time**: 0.2120576499874005
- **min_time**: 0.17567649998818524
- **python_version**: 3.13.7
- **std_time**: 0.051450715743620146
- **success**: True
- **successful_runs**: 2
- **test_name**: V1_CreateFishnet_OS
- **total_runs**: 2

### V2_CreateRandomPoints_OS

- **all_times**: [0.077401499991538, 0.15480920000118203]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 47.14296937616507
- **failed_runs**: 0
- **max_time**: 0.15480920000118203
- **mean_time**: 0.11610534999636002
- **min_time**: 0.077401499991538
- **python_version**: 3.13.7
- **std_time**: 0.05473550959287327
- **success**: True
- **successful_runs**: 2
- **test_name**: V2_CreateRandomPoints_OS
- **total_runs**: 2

### V3_Buffer_OS

- **all_times**: [0.45291459999862127, 0.2817044999974314]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 32.959617499495664
- **failed_runs**: 0
- **max_time**: 0.45291459999862127
- **mean_time**: 0.36730954999802634
- **min_time**: 0.2817044999974314
- **python_version**: 3.13.7
- **std_time**: 0.12106382271846827
- **success**: True
- **successful_runs**: 2
- **test_name**: V3_Buffer_OS
- **total_runs**: 2

### V4_Intersect_OS

- **all_times**: [2.9257401000068057, 3.3627925000037067]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 9.828770412071886
- **failed_runs**: 0
- **max_time**: 3.3627925000037067
- **mean_time**: 3.144266300005256
- **min_time**: 2.9257401000068057
- **python_version**: 3.13.7
- **std_time**: 0.3090427157716641
- **success**: True
- **successful_runs**: 2
- **test_name**: V4_Intersect_OS
- **total_runs**: 2

### V5_SpatialJoin_OS

- **all_times**: [0.538647100009257, 0.5731202999886591]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 4.385131903432478
- **failed_runs**: 0
- **max_time**: 0.5731202999886591
- **mean_time**: 0.555883699998958
- **min_time**: 0.538647100009257
- **python_version**: 3.13.7
- **std_time**: 0.024376233474635193
- **success**: True
- **successful_runs**: 2
- **test_name**: V5_SpatialJoin_OS
- **total_runs**: 2

### V6_CalculateField_OS

- **all_times**: [0.6680080000078306, 0.6962705999903847]
- **avg_memory_mb**: 0.0
- **category**: vector_os
- **cv_percent**: 2.9297060148349385
- **failed_runs**: 0
- **max_time**: 0.6962705999903847
- **mean_time**: 0.6821392999991076
- **min_time**: 0.6680080000078306
- **python_version**: 3.13.7
- **std_time**: 0.0199846761016268
- **success**: True
- **successful_runs**: 2
- **test_name**: V6_CalculateField_OS
- **total_runs**: 2

### R1_CreateConstantRaster

- **all_times**: [3.9862030999793205, 0.8947611000039615]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 89.57163020515357
- **failed_runs**: 0
- **max_time**: 3.9862030999793205
- **mean_time**: 2.440482099991641
- **min_time**: 0.8947611000039615
- **python_version**: 3.13.7
- **std_time**: 2.185979601827479
- **success**: True
- **successful_runs**: 2
- **test_name**: R1_CreateConstantRaster
- **total_runs**: 2

### R2_Resample

- **all_times**: [1.2577102999784984, 1.4381073000258766]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 9.46354397560162
- **failed_runs**: 0
- **max_time**: 1.4381073000258766
- **mean_time**: 1.3479088000021875
- **min_time**: 1.2577102999784984
- **python_version**: 3.13.7
- **std_time**: 0.1275599420392111
- **success**: True
- **successful_runs**: 2
- **test_name**: R2_Resample
- **total_runs**: 2

### R3_Clip

- **all_times**: [0.7293781999906059, 0.804572900000494]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 6.932513335866897
- **failed_runs**: 0
- **max_time**: 0.804572900000494
- **mean_time**: 0.76697554999555
- **min_time**: 0.7293781999906059
- **python_version**: 3.13.7
- **std_time**: 0.05317068228627998
- **success**: True
- **successful_runs**: 2
- **test_name**: R3_Clip
- **total_runs**: 2

### R4_RasterCalculator

- **all_times**: [0.4545668999780901, 0.601379600004293]
- **avg_memory_mb**: 0.0
- **category**: raster
- **cv_percent**: 19.662408228933277
- **failed_runs**: 0
- **max_time**: 0.601379600004293
- **mean_time**: 0.5279732499911916
- **min_time**: 0.4545668999780901
- **python_version**: 3.13.7
- **std_time**: 0.10381225575283452
- **success**: True
- **successful_runs**: 2
- **test_name**: R4_RasterCalculator
- **total_runs**: 2

### R1_CreateConstantRaster_OS

- **all_times**: [0.054978799977106974, 0.03558070000144653]
- **avg_memory_mb**: 0.0
- **category**: raster_os
- **cv_percent**: 30.29285284961264
- **failed_runs**: 0
- **max_time**: 0.054978799977106974
- **mean_time**: 0.04527974998927675
- **min_time**: 0.03558070000144653
- **python_version**: 3.13.7
- **std_time**: 0.013716528034924102
- **success**: True
- **successful_runs**: 2
- **test_name**: R1_CreateConstantRaster_OS
- **total_runs**: 2

### R2_Resample_OS

- **all_times**: [0.02393520000623539, 0.03954989998601377]
- **avg_memory_mb**: 0.0
- **category**: raster_os
- **cv_percent**: 34.78378467779922
- **failed_runs**: 0
- **max_time**: 0.03954989998601377
- **mean_time**: 0.03174254999612458
- **min_time**: 0.02393520000623539
- **python_version**: 3.13.7
- **std_time**: 0.011041260241894738
- **success**: True
- **successful_runs**: 2
- **test_name**: R2_Resample_OS
- **total_runs**: 2

### R3_Clip_OS

- **all_times**: [0.06380360000184737, 0.039835100003983825]
- **avg_memory_mb**: 0.0
- **category**: raster_os
- **cv_percent**: 32.70648682857943
- **failed_runs**: 0
- **max_time**: 0.06380360000184737
- **mean_time**: 0.0518193500029156
- **min_time**: 0.039835100003983825
- **python_version**: 3.13.7
- **std_time**: 0.016948288883359065
- **success**: True
- **successful_runs**: 2
- **test_name**: R3_Clip_OS
- **total_runs**: 2

### R4_RasterCalculator_OS

- **all_times**: [0.04438170001958497, 0.036417000024812296]
- **avg_memory_mb**: 0.0
- **category**: raster_os
- **cv_percent**: 13.940554423092461
- **failed_runs**: 0
- **max_time**: 0.04438170001958497
- **mean_time**: 0.04039935002219863
- **min_time**: 0.036417000024812296
- **python_version**: 3.13.7
- **std_time**: 0.005631893376420217
- **success**: True
- **successful_runs**: 2
- **test_name**: R4_RasterCalculator_OS
- **total_runs**: 2

### M1_PolygonToRaster

- **all_times**: [1.6154218000010587, 1.8254925000073854]
- **avg_memory_mb**: 0.0
- **category**: mixed
- **cv_percent**: 8.633892247924567
- **failed_runs**: 0
- **max_time**: 1.8254925000073854
- **mean_time**: 1.720457150004222
- **min_time**: 1.6154218000010587
- **python_version**: 3.13.7
- **std_time**: 0.14854241650307848
- **success**: True
- **successful_runs**: 2
- **test_name**: M1_PolygonToRaster
- **total_runs**: 2

### M2_RasterToPoint

- **all_times**: [22.581449999997858, 22.247948500007624]
- **avg_memory_mb**: 0.0
- **category**: mixed
- **cv_percent**: 1.052082696041309
- **failed_runs**: 0
- **max_time**: 22.581449999997858
- **mean_time**: 22.41469925000274
- **min_time**: 22.247948500007624
- **python_version**: 3.13.7
- **std_time**: 0.23582117217897988
- **success**: True
- **successful_runs**: 2
- **test_name**: M2_RasterToPoint
- **total_runs**: 2

### M1_PolygonToRaster_OS

- **all_times**: [0.9154121000028681, 0.9339548999851104]
- **avg_memory_mb**: 0.0
- **category**: mixed_os
- **cv_percent**: 1.4179705390779163
- **failed_runs**: 0
- **max_time**: 0.9339548999851104
- **mean_time**: 0.9246834999939892
- **min_time**: 0.9154121000028681
- **python_version**: 3.13.7
- **std_time**: 0.013111739609629313
- **success**: True
- **successful_runs**: 2
- **test_name**: M1_PolygonToRaster_OS
- **total_runs**: 2

### M2_RasterToPoint_OS

- **all_times**: [7.071231199981412, 6.359422600013204]
- **avg_memory_mb**: 0.0
- **category**: mixed_os
- **cv_percent**: 7.495162863100889
- **failed_runs**: 0
- **max_time**: 7.071231199981412
- **mean_time**: 6.715326899997308
- **min_time**: 6.359422600013204
- **python_version**: 3.13.7
- **std_time**: 0.5033246879444224
- **success**: True
- **successful_runs**: 2
- **test_name**: M2_RasterToPoint_OS
- **total_runs**: 2

### Py3_MP_V1_CreateFishnet_single

- **all_times**: [0.6603950000135228, 0.7898134000133723]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 12.620617595169012
- **failed_runs**: 0
- **max_time**: 0.7898134000133723
- **mean_time**: 0.7251042000134476
- **min_time**: 0.6603950000135228
- **python_version**: 3.13.7
- **std_time**: 0.09151262825020666
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V1_CreateFishnet_single
- **total_runs**: 2

### Py3_MP_V1_CreateFishnet_multiprocess

- **all_times**: [2.5866928000177722, 2.742220799991628]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 4.1274793213273595
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 2.742220799991628
- **mean_time**: 2.6644568000047
- **min_time**: 2.5866928000177722
- **num_workers**: 4
- **parallel_efficiency**: 6.803489927216763
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.2721395970886705
- **std_time**: 0.1099749034458947
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V1_CreateFishnet_multiprocess
- **total_runs**: 2

### Py3_MP_V2_CreateRandomPoints_single

- **all_times**: [0.4154309000005014, 0.4847758999967482]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 10.89401229559186
- **failed_runs**: 0
- **max_time**: 0.4847758999967482
- **mean_time**: 0.4501033999986248
- **min_time**: 0.4154309000005014
- **python_version**: 3.13.7
- **std_time**: 0.049034319738727204
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V2_CreateRandomPoints_single
- **total_runs**: 2

### Py3_MP_V2_CreateRandomPoints_multiprocess

- **all_times**: [1.868377699982375, 2.025389999995241]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 5.70267517856458
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 2.025389999995241
- **mean_time**: 1.946883849988808
- **min_time**: 1.868377699982375
- **num_workers**: 4
- **parallel_efficiency**: 5.779792667153877
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.23119170668615507
- **std_time**: 0.11102446206879422
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V2_CreateRandomPoints_multiprocess
- **total_runs**: 2

### Py3_MP_V3_Buffer_single

- **all_times**: [2.247512000001734, 2.235141899989685]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 0.3902590651708552
- **failed_runs**: 0
- **max_time**: 2.247512000001734
- **mean_time**: 2.2413269499957096
- **min_time**: 2.235141899989685
- **python_version**: 3.13.7
- **std_time**: 0.008746981602475697
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V3_Buffer_single
- **total_runs**: 2

### Py3_MP_V3_Buffer_multiprocess

- **all_times**: [5.666979400004493, 5.824428299994906]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 1.937677050194462
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 5.824428299994906
- **mean_time**: 5.7457038499997
- **min_time**: 5.666979400004493
- **num_workers**: 4
- **parallel_efficiency**: 9.752186192105198
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.3900874476842079
- **std_time**: 0.11133318487358382
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V3_Buffer_multiprocess
- **total_runs**: 2

### Py3_MP_V4_Intersect_single

- **all_times**: [0.836765700019896, 0.7820845999813173]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 4.77689340885813
- **failed_runs**: 0
- **max_time**: 0.836765700019896
- **mean_time**: 0.8094251500006067
- **min_time**: 0.7820845999813173
- **python_version**: 3.13.7
- **std_time**: 0.03866537664001901
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V4_Intersect_single
- **total_runs**: 2

### Py3_MP_V4_Intersect_multiprocess

- **all_times**: [7.239074699988123, 10.503800400008913]
- **avg_memory_mb**: 0.0
- **category**: vector_multiprocess
- **cv_percent**: 26.021821922187627
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 10.503800400008913
- **mean_time**: 8.871437549998518
- **min_time**: 7.239074699988123
- **num_workers**: 4
- **parallel_efficiency**: 2.2809864394546233
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.09123945757818493
- **std_time**: 2.308509681198699
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_V4_Intersect_multiprocess
- **total_runs**: 2

### Py3_MP_R1_CreateConstantRaster_single

- **all_times**: [0.610409199987771, 0.8948094999941532]
- **avg_memory_mb**: 0.0
- **category**: raster_multiprocess
- **cv_percent**: 26.720553060949392
- **failed_runs**: 0
- **max_time**: 0.8948094999941532
- **mean_time**: 0.7526093499909621
- **min_time**: 0.610409199987771
- **python_version**: 3.13.7
- **std_time**: 0.20110138070600134
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_R1_CreateConstantRaster_single
- **total_runs**: 2

### Py3_MP_R1_CreateConstantRaster_multiprocess

- **all_times**: [3.8264078000211157, 3.480417800019495]
- **avg_memory_mb**: 0.0
- **category**: raster_multiprocess
- **cv_percent**: 6.696529754932695
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 3.8264078000211157
- **mean_time**: 3.6534128000203054
- **min_time**: 3.480417800019495
- **num_workers**: 4
- **parallel_efficiency**: 5.150043200612172
- **python_version**: 3.13.7
- **speedup_vs_single**: 0.20600172802448688
- **std_time**: 0.24465187522387946
- **success**: True
- **successful_runs**: 2
- **test_name**: Py3_MP_R1_CreateConstantRaster_multiprocess
- **total_runs**: 2
