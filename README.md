# ArcGIS / OSM Benchmark Toolkit

一个用于对比 **ArcGIS Desktop (Python 2.7)**、**ArcGIS Pro (Python 3.x)** 和 **开源 GIS 栈** 的性能基准测试工具。

当前主线已经切换为：

- **中国全国 OSM 数据包**
- **10 个正式项目**
- **ArcGIS 输出统一为 GDB**
- **开源栈输出统一为更适合它的 GPKG**
- **三库统一生成结果报告**

## 当前正式套件

正式套件定义在 [configs/china_osm_matrix.json](configs/china_osm_matrix.json)，包含以下 10 个项目：

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

其中：

- **矢量**：5 项
- **栅格**：3 项
- **矢栅混合**：2 项

另外保留了一个 **5 项多进程支线**，用于并行性能观察。

## 目录结构

```text
C:\temp\arcgis_benchmark_data\<timestamp>\
├── data\
│   ├── benchmark_data_china.gdb
│   ├── staging\
│   ├── benchmark_manifest.json
│   └── benchmark_run.log
├── benchmark_results_py2.json
├── benchmark_results_py3.json
├── benchmark_results_os.json
├── benchmark_results_*.md
└── comparison_report.md
```

## 快速开始

### 1. 准备中国 OSM 包

```bash
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" scripts\prepare_china_osm_package.py
```

### 2. 跑三库正式流程

建议先用 1 次正式运行、0 次 warmup 做完整流程验证：

```bash
C:\Python27\ArcGIS10.8\python.exe run_benchmarks.py --region china --generate-data --runs 1 --warmup 0 --format GDB --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" run_benchmarks.py --region china --generate-data --runs 1 --warmup 0 --format GDB --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" run_benchmarks.py --region china --opensource --runs 1 --warmup 0 --format GPKG --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
```

### 3. 生成三方报告

```bash
python analyze_results_3way.py --results-dir C:\temp\arcgis_benchmark_data\china_fullflow --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
```

## 关键说明

- `--region china` 会自动切换到中国全国包和 national 量级。
- ArcGIS 栈默认写入 `GDB`。
- 开源栈默认写入 `GPKG`，避免与 ArcGIS 的 GDB 写入约束冲突。
- 默认每个项目是 `1` 次预热 + `3` 次正式运行；快检时可以手动改成 `--runs 1 --warmup 0`。
- 当前结构仍保留 legacy `tiny / small / standard / medium / large` 参数，以便兼容旧流程，但正式分析主线不再以它们为中心。

## 常见入口

- GUI：`ArcGIS基准测试工具.vbs`
- 命令行：`run_benchmarks.py`
- 三方分析：`analyze_results_3way.py`
- 中国 OSM 包准备：`scripts/prepare_china_osm_package.py`

## 依赖

- Windows
- ArcGIS Desktop 10.x
- ArcGIS Pro 3.x
- Python 3 环境中的开源 GIS 依赖：`geopandas`、`rasterio`、`shapely`、`pyogrio`、`numpy`

## 备注

如果你只想做最快的链路验证，可以先跑单任务快检；如果你要正式对比，就用上面的三库完整流程再出报告。
