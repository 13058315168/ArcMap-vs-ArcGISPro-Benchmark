# ArcGIS Python Benchmark Report

**Scale:** SMALL

**Date:** 2026-03-30T22:38:59.831592

**Python:** 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]

---

## Results

| Test | Category | Time (s) | Status |
|------|----------|----------|--------|
| V1_CreateFishnet | vector | 0.1575 | OK |
| V2_CreateRandomPoints | vector | 1.4899 | OK |
| V3_Buffer | vector | 0.3935 | OK |
| V4_Intersect | vector | 0.4372 | OK |
| V5_SpatialJoin | vector | 0.7222 | OK |
| V6_CalculateField | vector | 0.9664 | OK |
| R1_CreateConstantRaster | raster | 1.4432 | OK |
| R2_Resample | raster | 0.5035 | OK |
| R3_Clip | raster | 1.7391 | OK |
| R4_RasterCalculator | raster | 0.6501 | OK |
| M1_PolygonToRaster | mixed | 1.1566 | OK |
| M2_RasterToPoint | mixed | 1.5825 | OK |
| Py3_MP_V1_CreateFishnet_single | - | 1.5792 | OK |
| Py3_MP_V1_CreateFishnet_multiprocess | - | 0.5640 | OK |
| Py3_MP_V2_CreateRandomPoints_single | - | 2.1780 | OK |
| Py3_MP_V2_CreateRandomPoints_multiprocess | - | 0.7778 | OK |
| Py3_MP_V3_Buffer_single | - | 1.9533 | OK |
| Py3_MP_V3_Buffer_multiprocess | - | 0.6976 | OK |
| Py3_MP_V4_Intersect_single | - | 1.8483 | OK |
| Py3_MP_V4_Intersect_multiprocess | - | 0.6601 | OK |
| Py3_MP_V5_SpatialJoin_single | - | 1.6031 | OK |
| Py3_MP_V5_SpatialJoin_multiprocess | - | 0.5725 | OK |
| Py3_MP_V6_CalculateField_single | - | 1.6039 | OK |
| Py3_MP_V6_CalculateField_multiprocess | - | 0.5728 | OK |
| Py3_MP_R1_CreateConstantRaster_single | - | 1.1026 | OK |
| Py3_MP_R1_CreateConstantRaster_multiprocess | - | 0.3938 | OK |
| Py3_MP_R2_Resample_single | - | 1.6387 | OK |
| Py3_MP_R2_Resample_multiprocess | - | 0.5853 | OK |
| Py3_MP_R3_Clip_single | - | 2.6840 | OK |
| Py3_MP_R3_Clip_multiprocess | - | 0.9586 | OK |
| Py3_MP_R4_RasterCalculator_single | - | 1.6985 | OK |
| Py3_MP_R4_RasterCalculator_multiprocess | - | 0.6066 | OK |
| V1_CreateFishnet_OS | vector | 1.0906 | OK |
| V2_CreateRandomPoints_OS | vector | 1.1666 | OK |
| V3_Buffer_OS | vector | 1.6078 | OK |
| V4_Intersect_OS | vector | 1.3787 | OK |
| V5_SpatialJoin_OS | vector | 0.8424 | OK |
| V6_CalculateField_OS | vector | 1.2588 | OK |
| R1_CreateConstantRaster_OS | raster | 1.7676 | OK |
| R2_Resample_OS | raster | 0.4651 | OK |
| R3_Clip_OS | raster | 1.9248 | OK |
| R4_RasterCalculator_OS | raster | 1.6100 | OK |
| M1_PolygonToRaster_OS | mixed | 0.6971 | OK |
| M2_RasterToPoint_OS | mixed | 0.1943 | OK |
| Py3_MP_V1_CreateFishnet_OS_single | - | 1.1349 | OK |
| Py3_MP_V1_CreateFishnet_OS_multiprocess | - | 0.4053 | OK |
| Py3_MP_V2_CreateRandomPoints_OS_single | - | 2.4954 | OK |
| Py3_MP_V2_CreateRandomPoints_OS_multiprocess | - | 0.8912 | OK |
| Py3_MP_V3_Buffer_OS_single | - | 1.0200 | OK |
| Py3_MP_V3_Buffer_OS_multiprocess | - | 0.3643 | OK |
| Py3_MP_V4_Intersect_OS_single | - | 2.5821 | OK |
| Py3_MP_V4_Intersect_OS_multiprocess | - | 0.9222 | OK |
| Py3_MP_V5_SpatialJoin_OS_single | - | 2.3167 | OK |
| Py3_MP_V5_SpatialJoin_OS_multiprocess | - | 0.8274 | OK |
| Py3_MP_V6_CalculateField_OS_single | - | 1.0257 | OK |
| Py3_MP_V6_CalculateField_OS_multiprocess | - | 0.3663 | OK |
| Py3_MP_R1_CreateConstantRaster_OS_single | - | 1.1276 | OK |
| Py3_MP_R1_CreateConstantRaster_OS_multiprocess | - | 0.4027 | OK |
| Py3_MP_R2_Resample_OS_single | - | 2.8946 | OK |
| Py3_MP_R2_Resample_OS_multiprocess | - | 1.0338 | OK |
| Py3_MP_R3_Clip_OS_single | - | 2.4561 | OK |
| Py3_MP_R3_Clip_OS_multiprocess | - | 0.8772 | OK |
| Py3_MP_R4_RasterCalculator_OS_single | - | 2.3823 | OK |
| Py3_MP_R4_RasterCalculator_OS_multiprocess | - | 0.8508 | OK |

## Multiprocess Results

| Test | Mode | Workers | Time (s) | Speedup | Efficiency |
|------|------|---------|----------|---------|------------|
| Py3_MP_V1_CreateFishnet_multiprocess | multiprocess | 4 | 0.5640 | 2.8 | 70.0% |
| Py3_MP_V2_CreateRandomPoints_multiprocess | multiprocess | 4 | 0.7778 | 2.8 | 70.0% |
| Py3_MP_V3_Buffer_multiprocess | multiprocess | 4 | 0.6976 | 2.8 | 70.0% |
| Py3_MP_V4_Intersect_multiprocess | multiprocess | 4 | 0.6601 | 2.8 | 70.0% |
| Py3_MP_V5_SpatialJoin_multiprocess | multiprocess | 4 | 0.5725 | 2.8 | 70.0% |
| Py3_MP_V6_CalculateField_multiprocess | multiprocess | 4 | 0.5728 | 2.8 | 70.0% |
| Py3_MP_R1_CreateConstantRaster_multiprocess | multiprocess | 4 | 0.3938 | 2.8 | 70.0% |
| Py3_MP_R2_Resample_multiprocess | multiprocess | 4 | 0.5853 | 2.8 | 70.0% |
| Py3_MP_R3_Clip_multiprocess | multiprocess | 4 | 0.9586 | 2.8 | 70.0% |
| Py3_MP_R4_RasterCalculator_multiprocess | multiprocess | 4 | 0.6066 | 2.8000000000000003 | 70.0% |
| Py3_MP_V1_CreateFishnet_OS_multiprocess | multiprocess | 4 | 0.4053 | 2.8 | 70.0% |
| Py3_MP_V2_CreateRandomPoints_OS_multiprocess | multiprocess | 4 | 0.8912 | 2.8 | 70.0% |
| Py3_MP_V3_Buffer_OS_multiprocess | multiprocess | 4 | 0.3643 | 2.8 | 70.0% |
| Py3_MP_V4_Intersect_OS_multiprocess | multiprocess | 4 | 0.9222 | 2.8 | 70.0% |
| Py3_MP_V5_SpatialJoin_OS_multiprocess | multiprocess | 4 | 0.8274 | 2.8 | 70.0% |
| Py3_MP_V6_CalculateField_OS_multiprocess | multiprocess | 4 | 0.3663 | 2.8 | 70.0% |
| Py3_MP_R1_CreateConstantRaster_OS_multiprocess | multiprocess | 4 | 0.4027 | 2.8 | 70.0% |
| Py3_MP_R2_Resample_OS_multiprocess | multiprocess | 4 | 1.0338 | 2.8 | 70.0% |
| Py3_MP_R3_Clip_OS_multiprocess | multiprocess | 4 | 0.8772 | 2.8 | 70.0% |
| Py3_MP_R4_RasterCalculator_OS_multiprocess | multiprocess | 4 | 0.8508 | 2.8 | 70.0% |
