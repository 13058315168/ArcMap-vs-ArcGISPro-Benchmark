# ArcGIS Python 2.7 vs Python 3.x Performance Comparison

*Generated on 2026-03-29 19:26:26*

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total Tests | 12 |
| Python 3.x Faster | 5 (41.7%) |
| Python 2.7 Faster | 6 (50.0%) |
| Equal Performance | 1 (8.3%) |
| Average Speedup | 0.97x |
| Median Speedup | 1.01x |
| Max Speedup | 1.55x |
| Min Speedup | 0.14x |

## Detailed Results

| Test | Category | Python 2.7 (s) | Python 3.x (s) | Speedup | Faster |
|------|----------|----------------|----------------|---------|--------|
| M1_PolygonToRaster | mixed | 1.0483 ± 0.0000 | 0.7265 ± 0.0000 | 1.44x | Python 3.x |
| M2_RasterToPoint | mixed | 15.3937 ± 0.0000 | 9.9464 ± 0.0000 | 1.55x | Python 3.x |
| R1_CreateConstantRaster | raster | 0.1768 ± 0.0000 | 1.2322 ± 0.0000 | 0.14x | Python 2.7 |
| R2_Resample | raster | 0.2600 ± 0.0000 | 0.4549 ± 0.0000 | 0.57x | Python 2.7 |
| R3_Clip | raster | 0.3209 ± 0.0000 | 0.2975 ± 0.0000 | 1.08x | Python 3.x |
| R4_RasterCalculator | raster | 0.4566 ± 0.0000 | 0.5389 ± 0.0000 | 0.85x | Python 2.7 |
| V1_CreateFishnet | vector | 0.6632 ± 0.0000 | 0.8013 ± 0.0000 | 0.83x | Python 2.7 |
| V2_CreateRandomPoints | vector | 0.1030 ± 0.0000 | 0.1431 ± 0.0000 | 0.72x | Python 2.7 |
| V3_Buffer | vector | 0.1986 ± 0.0000 | 0.2668 ± 0.0000 | 0.74x | Python 2.7 |
| V4_Intersect | vector | 0.4374 ± 0.0000 | 0.3111 ± 0.0000 | 1.41x | Python 3.x |
| V5_SpatialJoin | vector | 1.6846 ± 0.0000 | 1.6751 ± 0.0000 | 1.01x | Equal |
| V6_CalculateField | vector | 1.4162 ± 0.0000 | 1.0779 ± 0.0000 | 1.31x | Python 3.x |

## Notes

- **Times**: Mean ± Standard Deviation (in seconds)
- **Speedup**: Ratio of Python 2.7 time to Python 3.x time
  - Speedup > 1: Python 3.x is faster
  - Speedup < 1: Python 2.7 is faster
  - Speedup = 1: Equal performance
- **Faster**: Which Python version performed better

## Interpretation

Based on the benchmark results:
- On average, **Python 2.7 is 1.03x faster** than Python 3.x
- Python 3.x was faster in 5 out of 12 tests (41.7%)