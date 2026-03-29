# Benchmark Results (py2)

*Generated on 2026-03-29 23:56:03*

## Summary

| Test Name | Mean Time | Std Time | Min Time | Max Time |
|---|---|---|---|---|
| V1_CreateFishnet | 1.0960 | 0 | 1.0960 | 1.0960 |
| V2_CreateRandomPoints | 0.3820 | 0 | 0.3820 | 0.3820 |
| V3_Buffer | 0.1721 | 0 | 0.1721 | 0.1721 |
| V4_Intersect | 0.3203 | 0 | 0.3203 | 0.3203 |
| V5_SpatialJoin |  |  |  |  |
| V6_CalculateField | 7.8887 | 0 | 7.8887 | 7.8887 |
| R1_CreateConstantRaster | 0.1541 | 0 | 0.1541 | 0.1541 |
| R2_Resample | 0.2920 | 0 | 0.2920 | 0.2920 |
| R3_Clip | 0.2748 | 0 | 0.2748 | 0.2748 |
| R4_RasterCalculator | 0.4547 | 0 | 0.4547 | 0.4547 |
| M1_PolygonToRaster |  |  |  |  |
| M2_RasterToPoint | 51.3160 | 0 | 51.3160 | 51.3160 |

## Detailed Results

### V1_CreateFishnet

- **all_times**: [1.0960285]
- **avg_memory_mb**: 193.1796875
- **category**: vector
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 1.0960285
- **mean_time**: 1.0960285
- **min_time**: 1.0960285
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: V1_CreateFishnet
- **total_runs**: 1

### V2_CreateRandomPoints

- **all_times**: [0.38197539999999996]
- **avg_memory_mb**: 195.53515625
- **category**: vector
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 0.3819754
- **mean_time**: 0.3819754
- **min_time**: 0.3819754
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: V2_CreateRandomPoints
- **total_runs**: 1

### V3_Buffer

- **all_times**: [0.17212240000000012]
- **avg_memory_mb**: 196.296875
- **category**: vector
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 0.1721224
- **mean_time**: 0.1721224
- **min_time**: 0.1721224
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: V3_Buffer
- **total_runs**: 1

### V4_Intersect

- **all_times**: [0.3202715999999999]
- **avg_memory_mb**: 199.66015625
- **category**: vector
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 0.3202716
- **mean_time**: 0.3202716
- **min_time**: 0.3202716
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: V4_Intersect
- **total_runs**: 1

### V5_SpatialJoin

- **category**: vector
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: V5_SpatialJoin
- **total_runs**: 1

### V6_CalculateField

- **all_times**: [7.888712100000001]
- **avg_memory_mb**: 232.34765625
- **category**: vector
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 7.8887121
- **mean_time**: 7.8887121
- **min_time**: 7.8887121
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: V6_CalculateField
- **total_runs**: 1

### R1_CreateConstantRaster

- **all_times**: [0.15412979999999976]
- **avg_memory_mb**: 232.3515625
- **category**: raster
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 0.1541298
- **mean_time**: 0.1541298
- **min_time**: 0.1541298
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: R1_CreateConstantRaster
- **total_runs**: 1

### R2_Resample

- **all_times**: [0.2920380999999992]
- **avg_memory_mb**: 238.96875
- **category**: raster
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 0.2920381
- **mean_time**: 0.2920381
- **min_time**: 0.2920381
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: R2_Resample
- **total_runs**: 1

### R3_Clip

- **all_times**: [0.2747697999999996]
- **avg_memory_mb**: 239.01953125
- **category**: raster
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 0.2747698
- **mean_time**: 0.2747698
- **min_time**: 0.2747698
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: R3_Clip
- **total_runs**: 1

### R4_RasterCalculator

- **all_times**: [0.45465489999999953]
- **avg_memory_mb**: 239.8203125
- **category**: raster
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 0.4546549
- **mean_time**: 0.4546549
- **min_time**: 0.4546549
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: R4_RasterCalculator
- **total_runs**: 1

### M1_PolygonToRaster

- **category**: mixed
- **error**: All runs failed
- **success**: False
- **successful_runs**: 0
- **test_name**: M1_PolygonToRaster
- **total_runs**: 1

### M2_RasterToPoint

- **all_times**: [51.316027500000004]
- **avg_memory_mb**: 242.54296875
- **category**: mixed
- **cv_percent**: 0.0
- **failed_runs**: 0
- **max_time**: 51.3160275
- **mean_time**: 51.3160275
- **min_time**: 51.3160275
- **python_version**: 2.7.16
- **std_time**: 0
- **success**: True
- **successful_runs**: 1
- **test_name**: M2_RasterToPoint
- **total_runs**: 1
