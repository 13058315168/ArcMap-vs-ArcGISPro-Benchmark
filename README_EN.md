# ArcGIS / OSM Benchmark Toolkit

This repository benchmarks three GIS stacks:

- ArcGIS Desktop (Python 2.7)
- ArcGIS Pro (Python 3.x)
- Open-source GIS libraries

The current primary workflow is the **China national OSM package** with:

- 10 formal tasks
- GDB output for ArcGIS stacks
- GPKG output for the open-source stack
- a 3-way comparison report

## Formal Task Set

Defined in [configs/china_osm_matrix.json](configs/china_osm_matrix.json):

- `V1_CreateFishnet`
- `V2_CreateRandomPoints`
- `Buffer`
- `Intersect`
- `SpatialJoin`
- `R1_CreateConstantRaster`
- `Resample`
- `Clip`
- `PolygonToRaster`
- `M2_RasterToPoint`

## Typical Flow

```bash
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" scripts\prepare_china_osm_package.py
C:\Python27\ArcGIS10.8\python.exe run_benchmarks.py --region china --generate-data --runs 1 --warmup 0 --format GDB --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" run_benchmarks.py --region china --generate-data --runs 1 --warmup 0 --format GDB --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" run_benchmarks.py --region china --opensource --runs 1 --warmup 0 --format GPKG --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
python analyze_results_3way.py --results-dir C:\temp\arcgis_benchmark_data\china_fullflow --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
```

## Notes

- `--region china` selects the national profile.
- ArcGIS stacks write into a file geodatabase.
- The open-source stack uses GeoPackage when GDB write support is not ideal.
- Legacy scale modes are still available for compatibility, but they are no longer the main analysis axis.
