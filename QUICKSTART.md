# 快速开始

这套工具现在的推荐主线是：

1. 中国全国 OSM 数据包
2. 10 个正式项目
3. 三库对比：Py2、Py3、OSS
4. ArcGIS 输出统一 `GDB`
5. 开源输出统一 `GPKG`

---

## 1. 准备环境

先确认两个 ArcGIS 解释器都可用：

```bash
C:\Python27\ArcGIS10.8\python.exe scripts/test_setup.py
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" scripts/test_setup.py
```

如果要跑开源栈，先安装依赖：

```bash
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" -m pip install geopandas rasterio shapely pyogrio numpy
```

---

## 2. 准备中国 OSM 包

```bash
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" scripts\prepare_china_osm_package.py
```

---

## 3. 跑正式流程

建议先用最小正式运行验证链路：

```bash
C:\Python27\ArcGIS10.8\python.exe run_benchmarks.py --region china --generate-data --runs 1 --warmup 0 --format GDB --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" run_benchmarks.py --region china --generate-data --runs 1 --warmup 0 --format GDB --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" run_benchmarks.py --region china --opensource --runs 1 --warmup 0 --format GPKG --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
```

说明：

- 第一条是 ArcGIS Desktop / Python 2.7
- 第二条是 ArcGIS Pro / Python 3.x
- 第三条是开源栈

如果你想跑多进程支线，在 ArcGIS Pro 命令后面加 `--multiprocess` 即可。

---

## 4. 生成报告

三库结果都完成后，跑三方分析：

```bash
python analyze_results_3way.py --results-dir C:\temp\arcgis_benchmark_data\china_fullflow --output-dir C:\temp\arcgis_benchmark_data\china_fullflow
```

生成后重点看这些文件：

- `benchmark_results_py2.json`
- `benchmark_results_py3.json`
- `benchmark_results_os.json`
- `comparison_report.md`
- `benchmark_run.log`

---

## 5. 结果目录长什么样

```text
C:\temp\arcgis_benchmark_data\china_fullflow\
├── data\
│   ├── benchmark_data_china.gdb
│   ├── staging\
│   ├── benchmark_manifest.json
│   └── benchmark_run.log
├── benchmark_results_py2.json
├── benchmark_results_py3.json
├── benchmark_results_os.json
└── comparison_report.md
```

---

## 6. 常见问题

- 如果 ArcPy 报锁定，先关闭 ArcGIS 的属性表和相关图层。
- 如果开源栈写 GDB 不稳，优先让它输出 `GPKG`。
- 如果只想快速验链路，可以先把 `--runs 1 --warmup 0` 保持不变。

