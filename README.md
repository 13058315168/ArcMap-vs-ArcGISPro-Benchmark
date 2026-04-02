# ArcGIS Python2、3 与开源库性能对比测试工具

## 项目简介

本工具用于对比分析 ArcGIS Desktop (Python 2.7)、ArcGIS Pro (Python 3.x) 以及开源库方案在相同硬件环境下处理 GIS 数据的性能差异。

**新增功能**：支持开源库（GeoPandas/Rasterio）三向性能对比，评估使用开源方案替代 ArcGIS/arcpy 的可行性。

## 文件组织结构

```
📁 根目录（用户操作区）
├── 📄 README.md              ← 本文件，项目说明
├── 📄 QUICKSTART.md          ← 快速上手指南（先看这个）
├── 📄 requirements.txt       ← Python依赖包清单
├── 🖥️ benchmark_gui_modern.py ← 【主要】图形界面工具
├── ⚡ run_benchmarks.py      ← 【主要】命令行测试脚本
├── 📊 analyze_results.py     ← 【主要】生成对比报告（支持三向对比）
├── 🚀 launch_gui.bat         ← 快速启动GUI（带窗口）
├── 🚀 start_gui_hidden.vbs   ← 快速启动GUI（无窗口）
├── 🧹 cleanup_temp.bat       ← 清理临时数据
│
📁 benchmarks/                ← 基准测试代码
│   ├── vector_benchmarks.py      ← arcpy 矢量测试
│   ├── vector_benchmarks_os.py   ← 开源库矢量测试 (GeoPandas)
│   ├── raster_benchmarks.py      ← arcpy 栅格测试
│   ├── raster_benchmarks_os.py   ← 开源库栅格测试 (Rasterio)
│   ├── mixed_benchmarks.py       ← arcpy 混合测试
│   ├── mixed_benchmarks_os.py    ← 开源库混合测试
│   └── base_benchmark.py         ← 基础测试类
│
📁 config/                    ← 配置文件
│   └── settings.py           ← 测试参数配置（五级数据规模）
📁 data/                      ← 测试数据生成代码
📁 C:\temp\arcgis_benchmark_data\<时间戳>\<规模>\  ← 运行时生成的测试结果目录
│   ├── data\py2             ← Python 2.7 原始数据与结果
│   ├── data\py3             ← Python 3.x 原始数据与结果
│   ├── data\os              ← 开源库原始数据与结果
│   └── comparison_report.md  ← 最终对比报告（根目录输出）
📁 utils/                     ← 工具函数库
└── desktop_automation/       ← 桌面自动化测试代码
```

## 快速开始

### 1. 启动工具

**推荐方式** - 双击启动（无黑窗口）：
```
启动工具.vbs
```

或命令行方式：
```bash
python benchmark_gui_modern.py
```

### 2. 运行测试

- 在 GUI 中选择数据规模（超小/小型/标准/中型/大型）
- 勾选「多进程对比」（可选）
- 勾选「开源库对比」（可选，Python 3.x 环境）
- 点击「开始全自动测试」按钮
- 等待测试完成

### 3. 查看报告

测试完成后，报告会自动保存到 `C:\temp\arcgis_benchmark_data\<时间戳>\<规模>\comparison_report.md`，包含：
- **两向对比**：Python 2.7 vs Python 3.x
- **三向对比**：Python 2.7 vs Python 3.x vs 开源库

## 测试内容

### 矢量数据测试 (6项 × 2方案)

| 测试项 | arcpy 实现 | 开源实现 | 说明 |
|--------|-----------|----------|------|
| V1_CreateFishnet | ✅ | ✅ (GeoPandas) | 创建渔网多边形 |
| V2_CreateRandomPoints | ✅ | ✅ (GeoPandas) | 生成随机点 |
| V3_Buffer | ✅ | ✅ (GeoPandas) | 缓冲区分析 |
| V4_Intersect | ✅ | ✅ (GeoPandas) | 叠加分析 |
| V5_SpatialJoin | ✅ | ✅ (GeoPandas) | 空间连接 |
| V6_CalculateField | ✅ | ✅ (GeoPandas) | 字段计算 |

### 栅格数据测试 (4项 × 2方案)

| 测试项 | arcpy 实现 | 开源实现 | 说明 |
|--------|-----------|----------|------|
| R1_CreateConstantRaster | ✅ | ✅ (Rasterio) | 创建常量栅格 |
| R2_Resample | ✅ | ✅ (Rasterio) | 栅格重采样 |
| R3_Clip | ✅ | ✅ (Rasterio) | 栅格裁剪 |
| R4_RasterCalculator | ✅ | ✅ (Rasterio) | 栅格计算 |

### 混合测试 (2项 × 2方案)

| 测试项 | arcpy 实现 | 开源实现 | 说明 |
|--------|-----------|----------|------|
| M1_PolygonToRaster | ✅ | ✅ | 矢转栅 |
| M2_RasterToPoint | ✅ | ✅ | 栅转矢 |

## 数据规模

| 规模 | 数据量 | 预计时间 | 适用场景 |
|------|--------|----------|----------|
| 超小 (tiny) | 标准1/100 | 1-2分钟 | 快速验证/调试 |
| 小型 (small) | 标准1/10 | 5-10分钟 | 功能测试 |
| 标准 (standard) | 中等规模 | 15-30分钟 | 日常测试 |
| 中型 (medium) | 标准规模 | 30-60分钟 | 性能对比（推荐）|
| 大型 (large) | 超大规格 | 2-4小时 | 学术研究 |

### 各级别详细参数

| 规模 | 渔网多边形 | 随机点 | 叠加分析 | 栅格尺寸 |
|------|-----------|--------|----------|----------|
| 超小 | 2,500 (50×50) | 1,000 | 10,000×10,000 | 500×500 |
| 小型 | 10,000 (100×100) | 10,000 | 100,000×100,000 | 1,000×1,000 |
| 标准 | 250,000 (500×500) | 50,000 | 300,000×300,000 | 5,000×5,000 |
| 中型 | 1,000,000 (1000×1000) | 100,000 | 1,000,000×1,000,000 | 10,000×10,000 |
| 大型 | 25,000,000 (5000×5000) | 500,000 | 5,000,000×5,000,000 | 30,000×30,000 |

## 命令行使用

### 基本用法

```bash
# 运行所有测试（默认配置）
python run_benchmarks.py

# 指定数据规模
python run_benchmarks.py --scale medium

# 包含开源库对比（Python 3.x 环境）
python run_benchmarks.py --scale medium --opensource

# 启用多进程对比
python run_benchmarks.py --scale medium --multiprocess --mp-workers 4

# 完整参数示例
python run_benchmarks.py --scale medium --runs 3 --warmup 1 --opensource --multiprocess --mp-workers 4
```

### 参数说明

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--scale` | 数据规模：tiny/small/standard/medium/large | 从 settings.py 读取 |
| `--runs` | 每项测试运行次数 | 3 |
| `--warmup` | 预热运行次数 | 0 |
| `--category` | 测试类别：vector/raster/mixed/all | all |
| `--opensource` | 启用开源库对比 | False |
| `--multiprocess` | 启用多进程对比 | False |
| `--mp-workers` | 多进程工作进程数 | 4 |
| `--generate-data` | 强制重新生成测试数据 | False |

### 分析结果

```bash
# 生成对比报告
python analyze_results.py

# 指定结果目录
python analyze_results.py --results-dir C:\temp\arcgis_benchmark_data\<时间戳>\<规模> --output-dir C:\temp\arcgis_benchmark_data\<时间戳>\<规模>
```

## 输出报告

测试完成后自动生成以下报告：

- **comparison_report.md** - Markdown格式报告（可直接阅读）
  - 两向对比表格（Py2.7 vs Py3.x）
  - 三向对比表格（Py2.7 vs Py3.x vs 开源库）
  - 统计摘要和性能分析
- **comparison_table.tex** - LaTeX表格（可直接插入论文）
- **comparison_data.csv** - Excel数据（可进一步分析）
- **comparison_data.json** - JSON原始数据

## 系统要求

### 必需组件

- Windows 操作系统（10 或 11）
- ArcGIS Desktop 10.x (Python 2.7) 或 ArcGIS Pro 3.x (Python 3.x)
- 至少一个 ArcGIS 许可（用于 arcpy 测试）

### 可选组件（开源对比）

```bash
# 安装开源库（Python 3.x 环境）
pip install geopandas rasterio shapely pyogrio numpy
```

### 硬件要求

| 规模 | 建议内存 | 磁盘空间 |
|------|----------|----------|
| 超小/小型 | 8GB | 5GB |
| 标准/中型 | 16GB | 20GB |
| 大型 | 32GB+ | 50GB+ |

## 数据存储

测试数据将存储在 `C:\temp\arcgis_benchmark_data`，而非软件目录：
- ✅ 便于统一管理临时数据
- ✅ 可随时手动删除清理
- ✅ 避免占用项目目录空间

测试结果（小文件）仍存储在软件目录的 `results` 文件夹中。

**自动清理：** 每次开始新测试时，会自动清理之前的测试数据，避免文件锁定问题。

## 故障排除

### 1. 测试数据生成失败（文件锁定）
**症状：** `ERROR 000464: 无法获取独占方案锁`

**解决：**
- 关闭所有 ArcGIS 相关程序（ArcMap、ArcGIS Pro）
- 手动删除 `C:\temp\arcgis_benchmark_data` 目录
- 重新运行测试

### 2. 开源库测试失败
**症状：** `ModuleNotFoundError: No module named 'geopandas'`

**解决：**
```bash
# 在 ArcGIS Pro Python 环境中安装
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" -m pip install geopandas rasterio shapely pyogrio
```

### 3. 找不到 Python 环境
**症状：** 环境验证失败

**解决：**
- 确保 ArcGIS Desktop 和 ArcGIS Pro 已正确安装
- 检查 `benchmark_gui_modern.py` 中的路径配置
- 或创建 `python_paths.config` 文件指定路径：
```
PYTHON27=C:\Python27\ArcGIS10.8\python.exe
PYTHON3=C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe
```

## 测试结果示例

### 三向对比示例（中型规模）

```
测试项目          | Python 2.7 | Python 3.x | 开源库 | Py3加速 | OS加速
------------------|------------|------------|--------|---------|--------
CreateFishnet     | 0.998s     | 1.040s     | 0.161s | 0.96x   | 6.20x
CreateRandomPoints| 0.371s     | 0.437s     | 0.075s | 0.85x   | 4.95x
Buffer            | 1.193s     | 1.088s     | N/A    | 1.10x   | N/A
Intersect         | 11.974s    | 7.463s     | N/A    | 1.60x   | N/A
SpatialJoin       | 5.130s     | 6.029s     | N/A    | 0.85x   | N/A
CalculateField    | 9.101s     | 6.746s     | N/A    | 1.35x   | N/A
------------------|------------|------------|--------|---------|--------
平均加速比        |            |            |        | 1.12x   | 5.57x
```

> 注：开源库（GeoPandas/Rasterio）在部分测试中显示出显著性能优势。

## 更新日志

### 最新版本

- ✅ **新增**：开源库（GeoPandas/Rasterio）三向性能对比
- ✅ **新增**：`--scale` CLI 参数支持动态切换数据规模
- ✅ **新增**：`--opensource` 参数启用开源库测试
- ✅ **修复**：`BaseBenchmark` 使 arcpy 成为可选依赖
- ✅ **修复**：开源测试结果正确分离和对比
- ✅ **优化**：数据规模配置（tiny/small/standard/medium/large）
- ✅ **优化**：分析报告支持三向对比表格

## 许可证

本工具仅供学术研究使用。

## 作者

ArcGIS Python 性能研究小组

---

*如有问题或建议，欢迎提交 Issue 或 Pull Request。*
