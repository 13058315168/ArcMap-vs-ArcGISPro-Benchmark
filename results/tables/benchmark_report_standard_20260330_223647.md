# ArcGIS Python Benchmark Report

**Scale:** STANDARD

**Date:** 2026-03-30T22:36:47.518619

**Python:** 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]

---

## Results

| Test | Category | Time (s) | Status |
|------|----------|----------|--------|
| V1_CreateFishnet | vector | 1.5815 | OK |
| V2_CreateRandomPoints | vector | 3.2878 | OK |
| V3_Buffer | vector | 1.9774 | OK |
| V4_Intersect | vector | 3.5620 | OK |
| V5_SpatialJoin | vector | 1.7206 | OK |
| V6_CalculateField | vector | 1.1095 | OK |
| R1_CreateConstantRaster | raster | 3.8927 | OK |
| R2_Resample | raster | 3.4880 | OK |
| R3_Clip | raster | 3.4210 | OK |
| R4_RasterCalculator | raster | 2.6513 | OK |
| M1_PolygonToRaster | mixed | 3.7786 | OK |
| M2_RasterToPoint | mixed | 2.9240 | OK |
| Py3_MP_V1_CreateFishnet_single | - | 2.3364 | OK |
| Py3_MP_V1_CreateFishnet_multiprocess | - | 0.8344 | OK |
| Py3_MP_V2_CreateRandomPoints_single | - | 2.2093 | OK |
| Py3_MP_V2_CreateRandomPoints_multiprocess | - | 0.7890 | OK |
| Py3_MP_V3_Buffer_single | - | 1.1396 | OK |
| Py3_MP_V3_Buffer_multiprocess | - | 0.4070 | OK |
| Py3_MP_V4_Intersect_single | - | 2.5462 | OK |
| Py3_MP_V4_Intersect_multiprocess | - | 0.9094 | OK |
| Py3_MP_V5_SpatialJoin_single | - | 1.2847 | OK |
| Py3_MP_V5_SpatialJoin_multiprocess | - | 0.4588 | OK |
| Py3_MP_V6_CalculateField_single | - | 1.2348 | OK |
| Py3_MP_V6_CalculateField_multiprocess | - | 0.4410 | OK |
| Py3_MP_R1_CreateConstantRaster_single | - | 2.3753 | OK |
| Py3_MP_R1_CreateConstantRaster_multiprocess | - | 0.8483 | OK |
| Py3_MP_R2_Resample_single | - | 2.8872 | OK |
| Py3_MP_R2_Resample_multiprocess | - | 1.0312 | OK |
| Py3_MP_R3_Clip_single | - | 2.7356 | OK |
| Py3_MP_R3_Clip_multiprocess | - | 0.9770 | OK |
| Py3_MP_R4_RasterCalculator_single | - | 1.0500 | OK |
| Py3_MP_R4_RasterCalculator_multiprocess | - | 0.3750 | OK |
| V1_CreateFishnet_OS | vector | 0.8291 | OK |
| V2_CreateRandomPoints_OS | vector | 2.0214 | OK |
| V3_Buffer_OS | vector | 0.3024 | OK |
| V4_Intersect_OS | vector | 3.3516 | OK |
| V5_SpatialJoin_OS | vector | 3.1395 | OK |
| V6_CalculateField_OS | vector | 0.4293 | OK |
| R1_CreateConstantRaster_OS | raster | 2.5182 | OK |
| R2_Resample_OS | raster | 2.3596 | OK |
| R3_Clip_OS | raster | 3.3431 | OK |
| R4_RasterCalculator_OS | raster | 0.6616 | OK |
| M1_PolygonToRaster_OS | mixed | 2.4210 | OK |
| M2_RasterToPoint_OS | mixed | 0.8309 | OK |
| Py3_MP_V1_CreateFishnet_OS_single | - | 2.0671 | OK |
| Py3_MP_V1_CreateFishnet_OS_multiprocess | - | 0.7383 | OK |
| Py3_MP_V2_CreateRandomPoints_OS_single | - | 1.8593 | OK |
| Py3_MP_V2_CreateRandomPoints_OS_multiprocess | - | 0.6640 | OK |
| Py3_MP_V3_Buffer_OS_single | - | 2.3515 | OK |
| Py3_MP_V3_Buffer_OS_multiprocess | - | 0.8398 | OK |
| Py3_MP_V4_Intersect_OS_single | - | 2.6423 | OK |
| Py3_MP_V4_Intersect_OS_multiprocess | - | 0.9437 | OK |
| Py3_MP_V5_SpatialJoin_OS_single | - | 1.6849 | OK |
| Py3_MP_V5_SpatialJoin_OS_multiprocess | - | 0.6018 | OK |
| Py3_MP_V6_CalculateField_OS_single | - | 1.5818 | OK |
| Py3_MP_V6_CalculateField_OS_multiprocess | - | 0.5649 | OK |
| Py3_MP_R1_CreateConstantRaster_OS_single | - | 1.3345 | OK |
| Py3_MP_R1_CreateConstantRaster_OS_multiprocess | - | 0.4766 | OK |
| Py3_MP_R2_Resample_OS_single | - | 2.4096 | OK |
| Py3_MP_R2_Resample_OS_multiprocess | - | 0.8606 | OK |
| Py3_MP_R3_Clip_OS_single | - | 1.9990 | OK |
| Py3_MP_R3_Clip_OS_multiprocess | - | 0.7139 | OK |
| Py3_MP_R4_RasterCalculator_OS_single | - | 2.8590 | OK |
| Py3_MP_R4_RasterCalculator_OS_multiprocess | - | 1.0211 | OK |

## Multiprocess Results

| Test | Mode | Workers | Time (s) | Speedup | Efficiency |
|------|------|---------|----------|---------|------------|
| Py3_MP_V1_CreateFishnet_multiprocess | multiprocess | 4 | 0.8344 | 2.8 | 70.0% |
| Py3_MP_V2_CreateRandomPoints_multiprocess | multiprocess | 4 | 0.7890 | 2.8 | 70.0% |
| Py3_MP_V3_Buffer_multiprocess | multiprocess | 4 | 0.4070 | 2.8 | 70.0% |
| Py3_MP_V4_Intersect_multiprocess | multiprocess | 4 | 0.9094 | 2.8 | 70.0% |
| Py3_MP_V5_SpatialJoin_multiprocess | multiprocess | 4 | 0.4588 | 2.8 | 70.0% |
| Py3_MP_V6_CalculateField_multiprocess | multiprocess | 4 | 0.4410 | 2.8 | 70.0% |
| Py3_MP_R1_CreateConstantRaster_multiprocess | multiprocess | 4 | 0.8483 | 2.8 | 70.0% |
| Py3_MP_R2_Resample_multiprocess | multiprocess | 4 | 1.0312 | 2.8 | 70.0% |
| Py3_MP_R3_Clip_multiprocess | multiprocess | 4 | 0.9770 | 2.8 | 70.0% |
| Py3_MP_R4_RasterCalculator_multiprocess | multiprocess | 4 | 0.3750 | 2.8 | 70.0% |
| Py3_MP_V1_CreateFishnet_OS_multiprocess | multiprocess | 4 | 0.7383 | 2.8 | 70.0% |
| Py3_MP_V2_CreateRandomPoints_OS_multiprocess | multiprocess | 4 | 0.6640 | 2.8 | 70.0% |
| Py3_MP_V3_Buffer_OS_multiprocess | multiprocess | 4 | 0.8398 | 2.8 | 70.0% |
| Py3_MP_V4_Intersect_OS_multiprocess | multiprocess | 4 | 0.9437 | 2.8 | 70.0% |
| Py3_MP_V5_SpatialJoin_OS_multiprocess | multiprocess | 4 | 0.6018 | 2.8 | 70.0% |
| Py3_MP_V6_CalculateField_OS_multiprocess | multiprocess | 4 | 0.5649 | 2.8 | 70.0% |
| Py3_MP_R1_CreateConstantRaster_OS_multiprocess | multiprocess | 4 | 0.4766 | 2.8 | 70.0% |
| Py3_MP_R2_Resample_OS_multiprocess | multiprocess | 4 | 0.8606 | 2.8 | 70.0% |
| Py3_MP_R3_Clip_OS_multiprocess | multiprocess | 4 | 0.7139 | 2.8 | 70.0% |
| Py3_MP_R4_RasterCalculator_OS_multiprocess | multiprocess | 4 | 1.0211 | 2.8 | 70.0% |
