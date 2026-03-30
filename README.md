# ArcGIS Python 2.7 vs Python 3.x 性能对比测试工具

## 项目简介

本工具用于对比分析 ArcGIS Desktop (Python 2.7) 与 ArcGIS Pro (Python 3.x) 在相同硬件环境下处理 GIS 数据的性能差异。

## 文件组织结构

```
📁 根目录（用户操作区）
├── 📄 README.md              ← 本文件，项目说明
├── 📄 QUICKSTART.md          ← 快速上手指南（先看这个）
├── 📄 requirements.txt       ← Python依赖包清单
├── 🖥️ benchmark_gui.py       ← 【主要】图形界面工具
├── ⚡ run_benchmarks.py      ← 【主要】命令行测试脚本
├── 📊 analyze_results.py     ← 【主要】生成对比报告
├── 🚀 launch_gui.bat         ← 快速启动GUI（带窗口）
├── 🚀 start_gui_hidden.vbs   ← 快速启动GUI（无窗口）
├── 🧹 cleanup_temp.bat       ← 清理临时数据
│
📁 docs/                      ← 详细文档
│   ├── GUI_GUIDE.md          ← GUI使用详解
│   ├── DESKTOP_TEST_GUIDE.md ← 桌面自动化测试指南
│   ├── README_SIMPLE.md      ← 简化版说明
│   └── ...                   ← 其他技术文档
│
📁 benchmarks/                ← 基准测试代码（无需修改）
📁 config/                    ← 配置文件
│   └── settings.py           ← 测试参数配置（可调整）
📁 data/                      ← 测试数据生成代码
📁 results/                   ← 测试结果输出目录
│   ├── raw/                  ← 原始JSON/CSV数据
│   └── tables/               ← 生成的对比报告
📁 scripts/                   ← 辅助脚本
│   ├── run_both_versions.py  ← 同时运行Py2+Py3测试
│   ├── test_setup.py         ← 环境检查脚本
│   └── test_mp_quick.py      ← 多进程快速测试
📁 utils/                     ← 工具函数库
└── desktop_automation/       ← 桌面自动化测试代码
```

### 文档导航

| 文档 | 位置 | 说明 |
|------|------|------|
| **快速开始** | `QUICKSTART.md` | ⭐ 新用户先看这个，5分钟上手 |
| **详细指南** | `docs/GUI_GUIDE.md` | GUI界面各功能详解 |
| **桌面测试** | `docs/DESKTOP_TEST_GUIDE.md` | 桌面自动化测试说明 |
| **技术对比** | `docs/DESKTOP_VS_STANDALONE.md` | Desktop vs Standalone对比 |
| **研究扩展** | `docs/RESEARCH_EXTENSION_SUMMARY.md` | 研究论文相关扩展功能 |

## 快速开始

### 1. 启动工具

**推荐方式** - 双击启动（无黑窗口）：
```
启动工具.vbs
```

或命令行方式：
```bash
python benchmark_gui.py
```

### 2. 运行测试

- 在 GUI 中选择数据规模（超小/小型/标准/中型/大型）
- 勾选「多进程对比」（可选）
- 点击「开始全自动测试」按钮
- 等待测试完成

### 3. 查看报告

测试完成后，报告会自动保存到 `results/tables/comparison_report.md`
也可点击「导出报告」按钮手动导出。

## 测试内容

### 矢量数据测试 (6项)
| 测试项 | 说明 |
|--------|------|
| V1_CreateFishnet | 创建渔网多边形 |
| V2_CreateRandomPoints | 生成随机点 |
| V3_Buffer | 缓冲区分析 |
| V4_Intersect | 叠加分析 |
| V5_SpatialJoin | 空间连接 |
| V6_CalculateField | 字段计算 |

### 栅格数据测试 (4项)
| 测试项 | 说明 |
|--------|------|
| R1_CreateConstantRaster | 创建常量栅格 |
| R2_Resample | 栅格重采样 |
| R3_Clip | 栅格裁剪 |
| R4_RasterCalculator | 栅格计算 |

### 混合测试 (2项)
| 测试项 | 说明 |
|--------|------|
| M1_PolygonToRaster | 矢转栅 |
| M2_RasterToPoint | 栅转矢 |

## 数据规模

| 规模 | 数据量 | 预计时间 | 适用场景 |
|------|--------|----------|----------|
| 超小 | 标准1/100 | 1-2分钟 | 快速验证 |
| 小型 | 标准1/10 | 5-10分钟 | 快速测试 |
| 中型 | 标准规模 | 30-60分钟 | 日常测试（推荐） |
| 大型 | 超大规格 | 2-4小时 | 学术论文 |

### 中型测试详细参数

**矢量数据测试：**

| 测试项 | 参数 | 数据规模 |
|--------|------|----------|
| V1 渔网 | 1000×1000 网格 | **100万个**多边形 |
| V2 随机点 | 生成点数 | **10万个**点 |
| V3 缓冲区 | 缓冲区点数 | **10万个**点 |
| V4 叠加分析 | A/B两组数据 | 各**100万个**多边形 |
| V5 空间连接 | 点/多边形 | **50万个**点 + **1万个**多边形 |
| V6 字段计算 | 计算记录数 | **100万条**记录 |

**栅格数据测试：**

| 测试项 | 参数 | 数据规模 |
|--------|------|----------|
| R1 常量栅格 | 栅格尺寸 | **10000×10000** 像素 (1亿像素) |
| R2 重采样 | 源/目标尺寸 | 10000×10000 → 5000×5000 |
| R3 裁剪 | 裁剪比例 | 50% (0.5) |
| R4 栅格计算 | 双栅格运算 | 大规模栅格计算 |

**混合测试：**

| 测试项 | 说明 |
|--------|------|
| M1 矢转栅 | 将矢量多边形转换为栅格 |
| M2 栅转矢 | 将栅格转换为点要素 |

**测试配置：**
- 运行次数：3次正式测试 + 1次预热
- 内存监控：开启（采样间隔0.5秒）

## 输出报告

测试完成后自动生成以下报告：

- **comparison_report.md** - Markdown格式报告（可直接阅读）
- **comparison_table.tex** - LaTeX表格（可直接插入论文）
- **comparison_data.csv** - Excel数据（可进一步分析）
- **comparison_data.json** - JSON原始数据

## 系统要求

- Windows 操作系统
- ArcGIS Desktop 10.x (Python 2.7)
- ArcGIS Pro 3.x (Python 3.x)
- 建议 16GB 以上内存
- 磁盘空间：C:\temp 需要有足够空间

### 磁盘空间需求

| 规模 | 测试数据大小 | 建议预留空间 |
|------|--------------|--------------|
| 超小 | ~500MB | 2GB |
| 小型 | ~2GB | 5GB |
| 中型 | ~10GB | 20GB |
| 大型 | ~30GB | 50GB |

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

### 2. 编码错误（GBK codec）
**症状：** `'gbk' codec can't decode byte`

**解决：**
- 已修复：GUI 自动使用 UTF-8 编码处理子进程输出
- 无法解码的字符会显示为 `�`，不影响测试结果

### 3. 找不到 Python 环境
**症状：** 环境验证失败

**解决：**
- 确保 ArcGIS Desktop 和 ArcGIS Pro 已正确安装
- 检查 `benchmark_gui.py` 中的路径配置：
  - `PYTHON27_PATH = r"C:\Python27\ArcGIS10.8\python.exe"`
  - `PYTHON3_PATH = r"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"`

## 测试结果示例

中型测试典型结果（仅供参考）：

```
测试项目          | Python 2.7 | Python 3.x | 加速比
------------------|------------|------------|--------
CreateFishnet     | 0.998s     | 1.040s     | 0.96x
CreateRandomPoints| 0.371s     | 0.437s     | 0.85x
Buffer            | 1.193s     | 1.088s     | 1.10x
Intersect         | 11.974s    | 7.463s     | 1.60x
SpatialJoin       | 5.130s     | 6.029s     | 0.85x
CalculateField    | 9.101s     | 6.746s     | 1.35x
------------------|------------|------------|--------
平均加速比        |            |            | 1.12x
```

## 许可证

本工具仅供学术研究使用。

## 作者

ArcGIS Python 性能研究小组
