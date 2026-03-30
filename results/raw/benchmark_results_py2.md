# Benchmark Results (py2)

<<<<<<< HEAD
*Generated on 2026-03-30 13:03:39*
=======
*Generated on 2026-03-30 08:31:58*
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce

## Summary

| Test Name | Mean Time | Std Time | Min Time | Max Time |
|---|---|---|---|---|
<<<<<<< HEAD
| V1_CreateFishnet | 1.0930 | 0.7486 | 0.5636 | 1.6223 |
| V2_CreateRandomPoints | 0.2399 | 0.0092 | 0.2334 | 0.2465 |
| V3_Buffer | 0.4847 | 0.0161 | 0.4733 | 0.4961 |
| V4_Intersect | 0.7910 | 0.0652 | 0.7449 | 0.8371 |
| V5_SpatialJoin | 2.3605 | 0.4275 | 2.0582 | 2.6627 |
| V6_CalculateField | 2.9756 | 0.0425 | 2.9456 | 3.0057 |
| R1_CreateConstantRaster | 0.2755 | 0.0495 | 0.2405 | 0.3105 |
| R2_Resample | 0.5141 | 0.0134 | 0.5046 | 0.5235 |
| R3_Clip | 0.6606 | 0.0765 | 0.6064 | 0.7147 |
| R4_RasterCalculator | 0.7641 | 0.0467 | 0.7311 | 0.7971 |
| M1_PolygonToRaster | 2.6191 | 0.0011 | 2.6183 | 2.6198 |
| M2_RasterToPoint | 31.4910 | 0.2342 | 31.3254 | 31.6566 |
| Py2_MP_V1_CreateFishnet_single | 0.6259 | 0.0088 | 0.6197 | 0.6321 |
| Py2_MP_V1_CreateFishnet_multiprocess | 2.2302 | 0.2960 | 2.0209 | 2.4396 |
| Py2_MP_V2_CreateRandomPoints_single | 0.2474 | 0.0343 | 0.2231 | 0.2717 |
| Py2_MP_V2_CreateRandomPoints_multiprocess | 1.0631 | 0.0666 | 1.0160 | 1.1102 |
| Py2_MP_V3_Buffer_single | 7.8428 | 0.0179 | 7.8301 | 7.8554 |
| Py2_MP_V3_Buffer_multiprocess | 10.4952 | 0.0015 | 10.4941 | 10.4962 |
| Py2_MP_V4_Intersect_single | 0.7387 | 0.0071 | 0.7336 | 0.7437 |
| Py2_MP_V4_Intersect_multiprocess | 7.7479 | 0.1514 | 7.6408 | 7.8549 |
| Py2_MP_R1_CreateConstantRaster_single | 0.1936 | 0.0397 | 0.1656 | 0.2217 |
| Py2_MP_R1_CreateConstantRaster_multiprocess | 1.5738 | 0.1861 | 1.4422 | 1.7054 |
=======
| V1_CreateFishnet | 0.6754 | 0 | 0.6754 | 0.6754 |
| V2_CreateRandomPoints | 0.0851 | 0 | 0.0851 | 0.0851 |
| V3_Buffer | 0.1787 | 0 | 0.1787 | 0.1787 |
| V4_Intersect | 0.3539 | 0 | 0.3539 | 0.3539 |
| V5_SpatialJoin | 1.0737 | 0 | 1.0737 | 1.0737 |
| V6_CalculateField | 1.1907 | 0 | 1.1907 | 1.1907 |
| R1_CreateConstantRaster | 0.1539 | 0 | 0.1539 | 0.1539 |
| R2_Resample | 0.2564 | 0 | 0.2564 | 0.2564 |
| R3_Clip | 0.3174 | 0 | 0.3174 | 0.3174 |
| R4_RasterCalculator | 0.4539 | 0 | 0.4539 | 0.4539 |
| M1_PolygonToRaster | 1.0905 | 0 | 1.0905 | 1.0905 |
| M2_RasterToPoint | 13.3960 | 0 | 13.3960 | 13.3960 |
| Py2_MP_V1_CreateFishnet_single | 0.2007 | 0 | 0.2007 | 0.2007 |
| Py2_MP_V1_CreateFishnet_multiprocess | 0.4761 | 0.3894 | 0.2007 | 0.7514 |
| Py2_MP_V2_CreateRandomPoints_single | 0.0807 | 0 | 0.0807 | 0.0807 |
| Py2_MP_V2_CreateRandomPoints_multiprocess | 0.2510 | 0.2409 | 0.0807 | 0.4213 |
| Py2_MP_V3_Buffer_single | 3.6863 | 0 | 3.6863 | 3.6863 |
| Py2_MP_V3_Buffer_multiprocess | 3.6863 | 0 | 3.6863 | 3.6863 |
| Py2_MP_V4_Intersect_single | 0.3399 | 0 | 0.3399 | 0.3399 |
| Py2_MP_V4_Intersect_multiprocess | 0.3399 | 0 | 0.3399 | 0.3399 |
| Py2_MP_R1_CreateConstantRaster_single | 0.0741 | 0 | 0.0741 | 0.0741 |
| Py2_MP_R1_CreateConstantRaster_multiprocess | 0.0741 | 0 | 0.0741 | 0.0741 |
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce

## Detailed Results

### V1_CreateFishnet

<<<<<<< HEAD
- **all_times**: [1.6223391, 0.5636398000000002]
- **avg_memory_mb**: 195.037109375
=======
- **all_times**: [0.6753775]
- **avg_memory_mb**: 193.8984375
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **category**: vector
- **cv_percent**: 68.4922854715
- **failed_runs**: 0
<<<<<<< HEAD
- **max_time**: 1.6223391
- **mean_time**: 1.09298945
- **min_time**: 0.5636398
=======
- **max_time**: 0.6753775
- **mean_time**: 0.6753775
- **min_time**: 0.6753775
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **python_version**: 2.7.16
- **std_time**: 0.748613454267
- **success**: True
- **successful_runs**: 2
- **test_name**: V1_CreateFishnet
- **total_runs**: 2

### V2_CreateRandomPoints

<<<<<<< HEAD
- **all_times**: [0.23340869999999958, 0.24645759999999983]
- **avg_memory_mb**: 196.609375
=======
- **all_times**: [0.08511650000000004]
- **avg_memory_mb**: 196.234375
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **category**: vector
- **cv_percent**: 3.84564020313
- **failed_runs**: 0
<<<<<<< HEAD
- **max_time**: 0.2464576
- **mean_time**: 0.23993315
- **min_time**: 0.2334087
=======
- **max_time**: 0.0851165
- **mean_time**: 0.0851165
- **min_time**: 0.0851165
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **python_version**: 2.7.16
- **std_time**: 0.00922696567703
- **success**: True
- **successful_runs**: 2
- **test_name**: V2_CreateRandomPoints
- **total_runs**: 2

### V3_Buffer

<<<<<<< HEAD
- **all_times**: [0.4732649999999996, 0.4960528000000002]
- **avg_memory_mb**: 198.87109375
=======
- **all_times**: [0.17873910000000004]
- **avg_memory_mb**: 196.74609375
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **category**: vector
- **cv_percent**: 3.32469039737
- **failed_runs**: 0
<<<<<<< HEAD
- **max_time**: 0.4960528
- **mean_time**: 0.4846589
- **min_time**: 0.473265
=======
- **max_time**: 0.1787391
- **mean_time**: 0.1787391
- **min_time**: 0.1787391
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **python_version**: 2.7.16
- **std_time**: 0.0161134079083
- **success**: True
- **successful_runs**: 2
- **test_name**: V3_Buffer
- **total_runs**: 2

### V4_Intersect

<<<<<<< HEAD
- **all_times**: [0.8370724000000003, 0.7449225999999998]
- **avg_memory_mb**: 202.67578125
=======
- **all_times**: [0.3538709999999998]
- **avg_memory_mb**: 200.37890625
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **category**: vector
- **cv_percent**: 8.23766806658
- **failed_runs**: 0
<<<<<<< HEAD
- **max_time**: 0.8370724
- **mean_time**: 0.7909975
- **min_time**: 0.7449226
=======
- **max_time**: 0.353871
- **mean_time**: 0.353871
- **min_time**: 0.353871
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **python_version**: 2.7.16
- **std_time**: 0.065159748465
- **success**: True
- **successful_runs**: 2
- **test_name**: V4_Intersect
- **total_runs**: 2

### V5_SpatialJoin

<<<<<<< HEAD
- **all_times**: [2.6627399, 2.0581682999999984]
- **avg_memory_mb**: 233.73828125
- **category**: vector
- **cv_percent**: 18.1107812295
- **failed_runs**: 0
- **max_time**: 2.6627399
- **mean_time**: 2.3604541
- **min_time**: 2.0581683
- **python_version**: 2.7.16
- **std_time**: 0.427496678073
- **success**: True
- **successful_runs**: 2
=======
- **all_times**: [1.0736854999999998]
- **avg_memory_mb**: 233.49609375
- **category**: vector
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 1.0736855
- **mean_time**: 1.0736855
- **min_time**: 1.0736855
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **test_name**: V5_SpatialJoin
- **total_runs**: 2

### V6_CalculateField

<<<<<<< HEAD
- **all_times**: [3.0057108999999986, 2.9455624]
- **avg_memory_mb**: 234.28515625
=======
- **all_times**: [1.1907050999999997]
- **avg_memory_mb**: 233.87890625
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **category**: vector
- **cv_percent**: 1.429321427
- **failed_runs**: 0
<<<<<<< HEAD
- **max_time**: 3.0057109
- **mean_time**: 2.97563665
- **min_time**: 2.9455624
=======
- **max_time**: 1.1907051
- **mean_time**: 1.1907051
- **min_time**: 1.1907051
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **python_version**: 2.7.16
- **std_time**: 0.0425314122282
- **success**: True
- **successful_runs**: 2
- **test_name**: V6_CalculateField
- **total_runs**: 2

### R1_CreateConstantRaster

<<<<<<< HEAD
- **all_times**: [0.3104939000000009, 0.24052839999999875]
- **avg_memory_mb**: 237.052734375
=======
- **all_times**: [0.15386070000000007]
- **avg_memory_mb**: 233.99609375
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **category**: raster
- **cv_percent**: 17.9568338701
- **failed_runs**: 0
<<<<<<< HEAD
- **max_time**: 0.3104939
- **mean_time**: 0.27551115
- **min_time**: 0.2405284
=======
- **max_time**: 0.1538607
- **mean_time**: 0.1538607
- **min_time**: 0.1538607
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **python_version**: 2.7.16
- **std_time**: 0.0494730794991
- **success**: True
- **successful_runs**: 2
- **test_name**: R1_CreateConstantRaster
- **total_runs**: 2

### R2_Resample

<<<<<<< HEAD
- **all_times**: [0.5045813000000017, 0.5235410999999992]
- **avg_memory_mb**: 240.66015625
=======
- **all_times**: [0.2564013000000003]
- **avg_memory_mb**: 240.37890625
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **category**: raster
- **cv_percent**: 2.60797802867
- **failed_runs**: 0
<<<<<<< HEAD
- **max_time**: 0.5235411
- **mean_time**: 0.5140612
- **min_time**: 0.5045813
=======
- **max_time**: 0.2564013
- **mean_time**: 0.2564013
- **min_time**: 0.2564013
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **python_version**: 2.7.16
- **std_time**: 0.0134066031499
- **success**: True
- **successful_runs**: 2
- **test_name**: R2_Resample
- **total_runs**: 2

### R3_Clip

<<<<<<< HEAD
- **all_times**: [0.6064447000000008, 0.714678199999998]
- **avg_memory_mb**: 241.09375
=======
- **all_times**: [0.31737140000000075]
- **avg_memory_mb**: 240.87109375
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **category**: raster
- **cv_percent**: 11.5859988199
- **failed_runs**: 0
<<<<<<< HEAD
- **max_time**: 0.7146782
- **mean_time**: 0.66056145
- **min_time**: 0.6064447
=======
- **max_time**: 0.3173714
- **mean_time**: 0.3173714
- **min_time**: 0.3173714
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **python_version**: 2.7.16
- **std_time**: 0.0765326418016
- **success**: True
- **successful_runs**: 2
- **test_name**: R3_Clip
- **total_runs**: 2

### R4_RasterCalculator

<<<<<<< HEAD
- **all_times**: [0.7310710999999976, 0.7971491999999998]
- **avg_memory_mb**: 241.876953125
=======
- **all_times**: [0.45389130000000044]
- **avg_memory_mb**: 240.89453125
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **category**: raster
- **cv_percent**: 6.11486087417
- **failed_runs**: 0
<<<<<<< HEAD
- **max_time**: 0.7971492
- **mean_time**: 0.76411015
- **min_time**: 0.7310711
=======
- **max_time**: 0.4538913
- **mean_time**: 0.4538913
- **min_time**: 0.4538913
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **python_version**: 2.7.16
- **std_time**: 0.0467242725979
- **success**: True
- **successful_runs**: 2
- **test_name**: R4_RasterCalculator
- **total_runs**: 2

### M1_PolygonToRaster

<<<<<<< HEAD
- **all_times**: [2.619849000000002, 2.6182753000000005]
- **avg_memory_mb**: 241.78515625
- **category**: mixed
- **cv_percent**: 0.0424874965855
- **failed_runs**: 0
- **max_time**: 2.619849
- **mean_time**: 2.61906215
- **min_time**: 2.6182753
- **python_version**: 2.7.16
- **std_time**: 0.00111277394155
- **success**: True
- **successful_runs**: 2
=======
- **all_times**: [1.0905257000000006]
- **avg_memory_mb**: 242.87109375
- **category**: mixed
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 1.0905257
- **mean_time**: 1.0905257
- **min_time**: 1.0905257
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **test_name**: M1_PolygonToRaster
- **total_runs**: 2

### M2_RasterToPoint

<<<<<<< HEAD
- **all_times**: [31.325380700000004, 31.656568699999994]
- **avg_memory_mb**: 244.080078125
=======
- **all_times**: [13.395961900000001]
- **avg_memory_mb**: 244.84375
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **category**: mixed
- **cv_percent**: 0.743658406507
- **failed_runs**: 0
<<<<<<< HEAD
- **max_time**: 31.6565687
- **mean_time**: 31.4909747
- **min_time**: 31.3253807
=======
- **max_time**: 13.3959619
- **mean_time**: 13.3959619
- **min_time**: 13.3959619
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **python_version**: 2.7.16
- **std_time**: 0.234185280648
- **success**: True
- **successful_runs**: 2
- **test_name**: M2_RasterToPoint
<<<<<<< HEAD
- **total_runs**: 2

### Py2_MP_V1_CreateFishnet_single

- **all_times**: [0.6320908000000003, 0.6197027999999989]
- **avg_memory_mb**: 244.265625
- **category**: vector_multiprocess
- **cv_percent**: 1.39953404544
- **failed_runs**: 0
- **max_time**: 0.6320908
- **mean_time**: 0.6258968
- **min_time**: 0.6197028
- **python_version**: 2.7.16
- **std_time**: 0.00875963880534
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V1_CreateFishnet_single
- **total_runs**: 2

### Py2_MP_V1_CreateFishnet_multiprocess

- **all_times**: [2.0209270000000004, 2.4395554999999973]
- **avg_memory_mb**: 245.171875
- **category**: vector_multiprocess
- **cv_percent**: 13.2727816396
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 2.4395555
- **mean_time**: 2.23024125
- **min_time**: 2.020927
- **num_workers**: 4
- **parallel_efficiency**: 7.01602124882
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.280640849953
- **std_time**: 0.296015051148
=======
- **total_runs**: 1

### Py2_MP_V1_CreateFishnet_single

- **all_times**: [0.20073400000000063]
- **avg_memory_mb**: 245.0234375
- **category**: vector_multiprocess
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 0.200734
- **mean_time**: 0.200734
- **min_time**: 0.200734
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: Py2_MP_V1_CreateFishnet_single
- **total_runs**: 1

### Py2_MP_V1_CreateFishnet_multiprocess

- **all_times**: [0.20073400000000063, 0.7514424999999996]
- **avg_memory_mb**: 245.5234375
- **category**: vector_multiprocess
- **cv_percent**: 81.7935991504
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 0.7514425
- **mean_time**: 0.47608825
- **min_time**: 0.200734
- **num_workers**: 4
- **parallel_efficiency**: 10.5407978458
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.421631913831
- **std_time**: 0.389409714807
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V1_CreateFishnet_multiprocess
- **total_runs**: 2

### Py2_MP_V2_CreateRandomPoints_single

<<<<<<< HEAD
- **all_times**: [0.22313610000000494, 0.27165370000000166]
- **avg_memory_mb**: 245.59765625
- **category**: vector_multiprocess
- **cv_percent**: 13.8673529515
- **failed_runs**: 0
- **max_time**: 0.2716537
- **mean_time**: 0.2473949
- **min_time**: 0.2231361
- **python_version**: 2.7.16
- **std_time**: 0.0343071239669
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V2_CreateRandomPoints_single
- **total_runs**: 2

### Py2_MP_V2_CreateRandomPoints_multiprocess

- **all_times**: [1.0159815000000094, 1.1102121999999923]
- **avg_memory_mb**: 245.62109375
- **category**: vector_multiprocess
- **cv_percent**: 6.26764785974
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 1.1102122
- **mean_time**: 1.06309685
- **min_time**: 1.0159815
- **num_workers**: 4
- **parallel_efficiency**: 5.8177883793
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.232711535172
- **std_time**: 0.0666311669659
=======
- **all_times**: [0.08068859999999844]
- **avg_memory_mb**: 246.0234375
- **category**: vector_multiprocess
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 0.0806886
- **mean_time**: 0.0806886
- **min_time**: 0.0806886
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: Py2_MP_V2_CreateRandomPoints_single
- **total_runs**: 1

### Py2_MP_V2_CreateRandomPoints_multiprocess

- **all_times**: [0.08068859999999844, 0.42132900000000006]
- **avg_memory_mb**: 246.0234375
- **category**: vector_multiprocess
- **cv_percent**: 95.9604351665
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 0.421329
- **mean_time**: 0.2510088
- **min_time**: 0.0806886
- **num_workers**: 4
- **parallel_efficiency**: 8.03643139205
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.321457255682
- **std_time**: 0.240869136786
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V2_CreateRandomPoints_multiprocess
- **total_runs**: 2

### Py2_MP_V3_Buffer_single

<<<<<<< HEAD
- **all_times**: [7.830135499999997, 7.855441800000008]
- **avg_memory_mb**: 245.80078125
- **category**: vector_multiprocess
- **cv_percent**: 0.228161909434
- **failed_runs**: 0
- **max_time**: 7.8554418
- **mean_time**: 7.84278865
- **min_time**: 7.8301355
- **python_version**: 2.7.16
- **std_time**: 0.0178942563367
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V3_Buffer_single
- **total_runs**: 2

### Py2_MP_V3_Buffer_multiprocess

- **all_times**: [10.496244400000023, 10.494056900000004]
- **avg_memory_mb**: 252.810546875
- **category**: vector_multiprocess
- **cv_percent**: 0.0147381980063
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 10.4962444
- **mean_time**: 10.49515065
- **min_time**: 10.4940569
- **num_workers**: 4
- **parallel_efficiency**: 18.6819344275
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.7472773771
- **std_time**: 0.00154679608386
- **success**: True
- **successful_runs**: 2
=======
- **all_times**: [3.6862604999999995]
- **avg_memory_mb**: 247.52734375
- **category**: vector_multiprocess
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 3.6862605
- **mean_time**: 3.6862605
- **min_time**: 3.6862605
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: Py2_MP_V3_Buffer_single
- **total_runs**: 1

### Py2_MP_V3_Buffer_multiprocess

- **all_times**: [3.6862604999999995]
- **avg_memory_mb**: 247.52734375
- **category**: vector_multiprocess
- **cv_percent**: 0.0
- **execution_mode**: multiprocess
- **failed_runs**: 1
- **max_time**: 3.6862605
- **mean_time**: 3.6862605
- **min_time**: 3.6862605
- **num_workers**: 4
- **parallel_efficiency**: 25.0
- **python_version**: 2.7.16
- **speedup_vs_single**: 1.0
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **test_name**: Py2_MP_V3_Buffer_multiprocess
- **total_runs**: 2

### Py2_MP_V4_Intersect_single

<<<<<<< HEAD
- **all_times**: [0.7336409999999773, 0.7437478000000226]
- **avg_memory_mb**: 256.25
- **category**: vector_multiprocess
- **cv_percent**: 0.967461891701
- **failed_runs**: 0
- **max_time**: 0.7437478
- **mean_time**: 0.7386944
- **min_time**: 0.733641
- **python_version**: 2.7.16
- **std_time**: 0.00714658681613
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_V4_Intersect_single
- **total_runs**: 2

### Py2_MP_V4_Intersect_multiprocess

- **all_times**: [7.640829099999991, 7.854947400000015]
- **avg_memory_mb**: 257.9609375
- **category**: vector_multiprocess
- **cv_percent**: 1.95413894755
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 7.8549474
- **mean_time**: 7.74788825
- **min_time**: 7.6408291
- **num_workers**: 4
- **parallel_efficiency**: 2.38353463603
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.0953413854414
- **std_time**: 0.151404501906
- **success**: True
- **successful_runs**: 2
=======
- **all_times**: [0.33987319999999954]
- **avg_memory_mb**: 247.5625
- **category**: vector_multiprocess
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 0.3398732
- **mean_time**: 0.3398732
- **min_time**: 0.3398732
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: Py2_MP_V4_Intersect_single
- **total_runs**: 1

### Py2_MP_V4_Intersect_multiprocess

- **all_times**: [0.33987319999999954]
- **avg_memory_mb**: 247.5625
- **category**: vector_multiprocess
- **cv_percent**: 0.0
- **execution_mode**: multiprocess
- **failed_runs**: 1
- **max_time**: 0.3398732
- **mean_time**: 0.3398732
- **min_time**: 0.3398732
- **num_workers**: 4
- **parallel_efficiency**: 25.0
- **python_version**: 2.7.16
- **speedup_vs_single**: 1.0
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **test_name**: Py2_MP_V4_Intersect_multiprocess
- **total_runs**: 2

### Py2_MP_R1_CreateConstantRaster_single

<<<<<<< HEAD
- **all_times**: [0.1655647999999985, 0.2216525000000047]
- **avg_memory_mb**: 258.69921875
- **category**: raster_multiprocess
- **cv_percent**: 20.4846183325
- **failed_runs**: 0
- **max_time**: 0.2216525
- **mean_time**: 0.19360865
- **min_time**: 0.1655648
- **python_version**: 2.7.16
- **std_time**: 0.0396599930112
- **success**: True
- **successful_runs**: 2
- **test_name**: Py2_MP_R1_CreateConstantRaster_single
- **total_runs**: 2

### Py2_MP_R1_CreateConstantRaster_multiprocess

- **all_times**: [1.7054219999999987, 1.4421705000000031]
- **avg_memory_mb**: 259.587890625
- **category**: raster_multiprocess
- **cv_percent**: 11.8278920037
- **execution_mode**: multiprocess
- **failed_runs**: 0
- **max_time**: 1.705422
- **mean_time**: 1.57379625
- **min_time**: 1.4421705
- **num_workers**: 4
- **parallel_efficiency**: 3.07550373817
- **python_version**: 2.7.16
- **speedup_vs_single**: 0.123020149527
- **std_time**: 0.186146920808
- **success**: True
- **successful_runs**: 2
=======
- **all_times**: [0.07408990000000415]
- **avg_memory_mb**: 245.36328125
- **category**: raster_multiprocess
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 0.0740899
- **mean_time**: 0.0740899
- **min_time**: 0.0740899
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: Py2_MP_R1_CreateConstantRaster_single
- **total_runs**: 1

### Py2_MP_R1_CreateConstantRaster_multiprocess

- **all_times**: [0.07408990000000415]
- **avg_memory_mb**: 245.36328125
- **category**: raster_multiprocess
- **cv_percent**: 0.0
- **execution_mode**: multiprocess
- **failed_runs**: 1
- **max_time**: 0.0740899
- **mean_time**: 0.0740899
- **min_time**: 0.0740899
- **num_workers**: 4
- **parallel_efficiency**: 25.0
- **python_version**: 2.7.16
- **speedup_vs_single**: 1.0
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
>>>>>>> 40b57fe01d65ffa95c50ace2d064180f92d37bce
- **test_name**: Py2_MP_R1_CreateConstantRaster_multiprocess
- **total_runs**: 2
