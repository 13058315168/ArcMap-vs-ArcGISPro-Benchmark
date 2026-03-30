# ArcGIS Python Benchmark Report

**Scale:** TINY

**Date:** 2026-03-30T23:29:04.957501

**Python:** 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]

---

## Results

| Test | Category | Time (s) | Status |
|------|----------|----------|--------|
| V1_CreateFishnet | vector | 0.6017 | OK |
| V2_CreateRandomPoints | vector | 0.8183 | OK |
| V3_Buffer | vector | 0.1013 | OK |
| V4_Intersect | vector | 0.6249 | OK |
| V5_SpatialJoin | vector | 0.7417 | OK |
| V6_CalculateField | vector | 0.2846 | OK |
| R1_CreateConstantRaster | raster | 0.2251 | OK |
| R2_Resample | raster | 0.2296 | OK |
| R3_Clip | raster | 0.6304 | OK |
| R4_RasterCalculator | raster | 0.5763 | OK |
| M1_PolygonToRaster | mixed | 0.2882 | OK |
| M2_RasterToPoint | mixed | 0.5050 | OK |
| Py3_MP_V1_CreateFishnet_single | - | 2.7053 | OK |
| Py3_MP_V1_CreateFishnet_multiprocess | - | 0.9662 | OK |
| Py3_MP_V2_CreateRandomPoints_single | - | 1.7944 | OK |
| Py3_MP_V2_CreateRandomPoints_multiprocess | - | 0.6409 | OK |
| Py3_MP_V3_Buffer_single | - | 2.9400 | OK |
| Py3_MP_V3_Buffer_multiprocess | - | 1.0500 | OK |
| Py3_MP_V4_Intersect_single | - | 2.0617 | OK |
| Py3_MP_V4_Intersect_multiprocess | - | 0.7363 | OK |
| Py3_MP_V5_SpatialJoin_single | - | 1.6162 | OK |
| Py3_MP_V5_SpatialJoin_multiprocess | - | 0.5772 | OK |
| Py3_MP_V6_CalculateField_single | - | 2.6309 | OK |
| Py3_MP_V6_CalculateField_multiprocess | - | 0.9396 | OK |
| Py3_MP_R1_CreateConstantRaster_single | - | 2.7784 | OK |
| Py3_MP_R1_CreateConstantRaster_multiprocess | - | 0.9923 | OK |
| Py3_MP_R2_Resample_single | - | 2.9215 | OK |
| Py3_MP_R2_Resample_multiprocess | - | 1.0434 | OK |
| Py3_MP_R3_Clip_single | - | 2.0891 | OK |
| Py3_MP_R3_Clip_multiprocess | - | 0.7461 | OK |
| Py3_MP_R4_RasterCalculator_single | - | 1.5980 | OK |
| Py3_MP_R4_RasterCalculator_multiprocess | - | 0.5707 | OK |
| V1_CreateFishnet_OS | vector | 0.8124 | OK |
| V2_CreateRandomPoints_OS | vector | 0.8607 | OK |
| V3_Buffer_OS | vector | 0.2794 | OK |
| V4_Intersect_OS | vector | 0.2273 | OK |
| V5_SpatialJoin_OS | vector | 0.3898 | OK |
| V6_CalculateField_OS | vector | 0.5891 | OK |
| R1_CreateConstantRaster_OS | raster | 0.2015 | OK |
| R2_Resample_OS | raster | 0.2546 | OK |
| R3_Clip_OS | raster | 0.9327 | OK |
| R4_RasterCalculator_OS | raster | 0.9640 | OK |
| M1_PolygonToRaster_OS | mixed | 0.1107 | OK |
| M2_RasterToPoint_OS | mixed | 0.3657 | OK |
| Py3_MP_V1_CreateFishnet_OS_single | - | 1.2080 | OK |
| Py3_MP_V1_CreateFishnet_OS_multiprocess | - | 0.4314 | OK |
| Py3_MP_V2_CreateRandomPoints_OS_single | - | 1.0295 | OK |
| Py3_MP_V2_CreateRandomPoints_OS_multiprocess | - | 0.3677 | OK |
| Py3_MP_V3_Buffer_OS_single | - | 1.3591 | OK |
| Py3_MP_V3_Buffer_OS_multiprocess | - | 0.4854 | OK |
| Py3_MP_V4_Intersect_OS_single | - | 1.5376 | OK |
| Py3_MP_V4_Intersect_OS_multiprocess | - | 0.5491 | OK |
| Py3_MP_V5_SpatialJoin_OS_single | - | 1.3489 | OK |
| Py3_MP_V5_SpatialJoin_OS_multiprocess | - | 0.4818 | OK |
| Py3_MP_V6_CalculateField_OS_single | - | 2.7344 | OK |
| Py3_MP_V6_CalculateField_OS_multiprocess | - | 0.9766 | OK |
| Py3_MP_R1_CreateConstantRaster_OS_single | - | 1.4779 | OK |
| Py3_MP_R1_CreateConstantRaster_OS_multiprocess | - | 0.5278 | OK |
| Py3_MP_R2_Resample_OS_single | - | 1.8009 | OK |
| Py3_MP_R2_Resample_OS_multiprocess | - | 0.6432 | OK |
| Py3_MP_R3_Clip_OS_single | - | 2.2741 | OK |
| Py3_MP_R3_Clip_OS_multiprocess | - | 0.8122 | OK |
| Py3_MP_R4_RasterCalculator_OS_single | - | 2.7688 | OK |
| Py3_MP_R4_RasterCalculator_OS_multiprocess | - | 0.9889 | OK |

## Multiprocess Results

| Test | Mode | Workers | Time (s) | Speedup | Efficiency |
|------|------|---------|----------|---------|------------|
| Py3_MP_V1_CreateFishnet_multiprocess | multiprocess | 4 | 0.9662 | 2.8 | 70.0% |
| Py3_MP_V2_CreateRandomPoints_multiprocess | multiprocess | 4 | 0.6409 | 2.8 | 70.0% |
| Py3_MP_V3_Buffer_multiprocess | multiprocess | 4 | 1.0500 | 2.8 | 70.0% |
| Py3_MP_V4_Intersect_multiprocess | multiprocess | 4 | 0.7363 | 2.8 | 70.0% |
| Py3_MP_V5_SpatialJoin_multiprocess | multiprocess | 4 | 0.5772 | 2.8 | 70.0% |
| Py3_MP_V6_CalculateField_multiprocess | multiprocess | 4 | 0.9396 | 2.8 | 70.0% |
| Py3_MP_R1_CreateConstantRaster_multiprocess | multiprocess | 4 | 0.9923 | 2.8 | 70.0% |
| Py3_MP_R2_Resample_multiprocess | multiprocess | 4 | 1.0434 | 2.8 | 70.0% |
| Py3_MP_R3_Clip_multiprocess | multiprocess | 4 | 0.7461 | 2.8 | 70.0% |
| Py3_MP_R4_RasterCalculator_multiprocess | multiprocess | 4 | 0.5707 | 2.8 | 70.0% |
| Py3_MP_V1_CreateFishnet_OS_multiprocess | multiprocess | 4 | 0.4314 | 2.8 | 70.0% |
| Py3_MP_V2_CreateRandomPoints_OS_multiprocess | multiprocess | 4 | 0.3677 | 2.8 | 70.0% |
| Py3_MP_V3_Buffer_OS_multiprocess | multiprocess | 4 | 0.4854 | 2.8 | 70.0% |
| Py3_MP_V4_Intersect_OS_multiprocess | multiprocess | 4 | 0.5491 | 2.8 | 70.0% |
| Py3_MP_V5_SpatialJoin_OS_multiprocess | multiprocess | 4 | 0.4818 | 2.8 | 70.0% |
| Py3_MP_V6_CalculateField_OS_multiprocess | multiprocess | 4 | 0.9766 | 2.8 | 70.0% |
| Py3_MP_R1_CreateConstantRaster_OS_multiprocess | multiprocess | 4 | 0.5278 | 2.8 | 70.0% |
| Py3_MP_R2_Resample_OS_multiprocess | multiprocess | 4 | 0.6432 | 2.8 | 70.0% |
| Py3_MP_R3_Clip_OS_multiprocess | multiprocess | 4 | 0.8122 | 2.8 | 70.0% |
| Py3_MP_R4_RasterCalculator_OS_multiprocess | multiprocess | 4 | 0.9889 | 2.8 | 70.0% |
