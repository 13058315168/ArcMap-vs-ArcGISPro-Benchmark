# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an ArcGIS Python Performance Benchmark tool for comparing ArcGIS Desktop (Python 2.7), ArcGIS Pro (Python 3.x), and open-source GIS libraries (GeoPandas, Rasterio, etc.). It provides both a modern Tkinter GUI and a web-based verification console for running benchmarks.

## Common Commands

### GUI Launch

```bash
# Recommended - no console window
启动工具.vbs

# Direct Python launch
python benchmark_gui_modern.py

# Launch with specific Python
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" benchmark_gui_modern.py
```

### Environment Verification

```bash
# Test ArcGIS Desktop Python 2.7 setup
C:\Python27\ArcGIS10.8\python.exe scripts/test_setup.py

# Test ArcGIS Pro Python 3.x setup
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" scripts/test_setup.py
```

### Running Benchmarks (Command Line)

```bash
# Run with ArcGIS Pro Python
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" run_benchmarks.py --scale tiny --generate-data

# Run with Python 2.7 (ArcGIS Desktop)
C:\Python27\ArcGIS10.8\python.exe run_benchmarks.py --scale tiny --generate-data

# Run with open-source stack
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" run_benchmarks.py --scale tiny --opensource --generate-data

# Full command with all options
python run_benchmarks.py --scale standard --runs 3 --warmup 1 --generate-data --stack arcpy_pro --format SHP --complexity simple
```

### Web Verification Console

```bash
# Start web console
打开网页控制台.bat

# Or directly
python verification_console/server.py
# Then open http://127.0.0.1:8765
```

### Installing Open-Source Dependencies

```bash
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" -m pip install geopandas rasterio shapely pyogrio numpy psutil
```

## High-Level Architecture

### Entry Points

- **`benchmark_gui_modern.py`** - Main Tkinter GUI application. Handles user configuration, runs benchmarks via subprocess, and displays progress/logs.
- **`run_benchmarks.py`** - Command-line entry point. Parses arguments and delegates to `RunnerEngine`.
- **`verification_console/server.py`** - Flask-based web UI for quick validation runs.

### Core Engine

**`runner/engine.py`** - `RunnerEngine` class orchestrates benchmark execution:
- Loads benchmark matrix from `configs/matrix.json`
- Generates test data via `data/generate_test_data.py`
- Instantiates benchmarks via `tasks/task_interface.py`
- Exports results via `utils/result_exporter.py`

### Benchmark Architecture

**`benchmarks/base_benchmark.py`** - `BaseBenchmark` abstract class:
- `setup()` / `teardown()` - Prepare/cleanup test environment
- `run_single()` - Execute one iteration (must be implemented by subclasses)
- `run()` - Orchestrate warmup + timed runs with memory monitoring
- `save_results()` - Persist results as JSON

**`tasks/task_interface.py`** - Factory for benchmark classes:
- Maps `(task_id, stack)` to benchmark classes
- `get_benchmark_class(task_id, stack)` returns appropriate class
- Stacks: `arcpy_desktop`, `arcpy_pro`, `oss`
- Task IDs: `Buffer`, `Intersect`, `SpatialJoin`, `Resample`, `Clip`, `PolygonToRaster`

**`tasks/task_specs.py`** - Defines the 6-core task matrix and legacy name mappings.

### Benchmark Implementations

- **`benchmarks/vector_benchmarks.py`** - ArcPy vector tests (V1-V6)
- **`benchmarks/raster_benchmarks.py`** - ArcPy raster tests (R1-R4)
- **`benchmarks/mixed_benchmarks.py`** - ArcPy mixed tests (M1-M2)
- **`benchmarks/vector_benchmarks_os.py`** - Open-source vector tests
- **`benchmarks/raster_benchmarks_os.py`** - Open-source raster tests
- **`benchmarks/mixed_benchmarks_os.py`** - Open-source mixed tests

### Configuration

**`config/settings.py`** - Central configuration:
- Scale configs: `VECTOR_CONFIG_TINY`, `RASTER_CONFIG_TINY`, etc. through `LARGE`
- `STANDARD_VECTOR_CONFIG_BY_TEST` / `STANDARD_RASTER_CONFIG_BY_TEST` - Per-test overrides for standard scale
- `set_timestamped_dirs()` - Creates `C:\temp\arcgis_benchmark_data\YYYYMMDD_HHMMSS` structure
- `set_scale(scale)` - Dynamically switch data scale

### Data Generation

**`data/generate_test_data.py`** - `TestDataGenerator` class:
- Creates test datasets based on active scale configuration
- Outputs to `SHP`, `GPKG`, or `GDB` format based on `ACTIVE_OUTPUT_FORMAT`
- Generates `constant_raster.tif` and `analysis_raster_R*.tif` for raster tests

### Results & Analysis

**`analyze_results.py`** - Compares py2/py3/os results and generates comparison reports
**`analyze_results_3way.py`** - Three-way comparison (py2 + py3 + os)

Output directory structure:
```
C:\temp\arcgis_benchmark_data\YYYYMMDD_HHMMSS\
├── tiny\ (or other scale)
│   ├── comparison_report.md
│   ├── benchmark_results_py2.json
│   ├── benchmark_results_py3.json
│   ├── benchmark_results_os.json
│   ├── benchmark_run.log
│   ├── benchmark_manifest.json
│   └── data\ (intermediate datasets)
```

### Key Utilities

- **`utils/settings_manager.py`** - GUI settings persistence (JSON-based)
- **`utils/timer.py`** - `BenchmarkTimer` with memory monitoring, `ProgressHeartbeat` for long tasks
- **`utils/gis_cleanup.py`** - Workspace cache clearing for ArcPy
- **`utils/benchmark_manifest.py`** - Run metadata tracking

## Development Notes

### Python 2/3 Compatibility

All code must be compatible with both Python 2.7 and 3.x:
- Use `from __future__ import print_function, division, absolute_import`
- Use `.format()` instead of f-strings
- Use `io.open()` for file operations
- Avoid type hints in shared modules

### Adding New Benchmarks

1. Create benchmark class extending `BaseBenchmark` in appropriate module
2. Implement `setup()`, `run_single()`, `teardown()`
3. Add task ID to `tasks/task_specs.py` `CORE_TASK_IDS`
4. Add legacy name mappings to `LEGACY_BENCHMARK_NAMES` and `LEGACY_BENCHMARK_NAMES_OS`
5. Update `configs/matrix.json` if needed

### Scale Configuration

For `standard` scale, per-test overrides are supported via:
- `STANDARD_VECTOR_CONFIG_BY_TEST['V3']` for vector test overrides
- `STANDARD_RASTER_CONFIG_BY_TEST['R2']` for raster test overrides

Use `get_vector_config_for_test(test_id)` and `get_raster_config_for_test(test_id)` to retrieve the active config.

### Path Handling

- Test data: `C:\temp\arcgis_benchmark_data\` (configurable)
- GDB name stored in `settings.DEFAULT_GDB_NAME` (filename only, not full path)
- Use `settings.get_default_gdb_path()` for full path

### Subprocess Execution

When GUI spawns benchmark processes:
- Use absolute paths for scripts: `os.path.join(script_dir, 'run_benchmarks.py')`
- Set `cwd=script_dir` in `subprocess.Popen()` to ensure correct working directory
- Handle encoding with UTF-8/GBK fallback for Chinese output
