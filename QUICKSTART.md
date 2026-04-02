# 快速开始指南

## 推荐使用图形界面

最简单的方式是使用图形界面：

```bash
# 双击启动（Windows）
launch_gui.bat

# 或使用 Python 启动
python launch_gui.py
```

然后按照界面上的 1→2→3→4→5 步骤点击执行即可。

---

## 命令行方式（备选）

如果 GUI 无法使用，可以使用命令行：

### 1. 验证环境

```bash
# Python 2.7
C:\Python27\ArcGIS10.8\python.exe test_setup.py

# Python 3.x
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" test_setup.py
```

### 2. 运行完整测试流程

```bash
# 步骤1：使用 Python 2.7 生成数据并运行测试
C:\Python27\ArcGIS10.8\python.exe run_benchmarks.py --scale medium

# 步骤2：使用 Python 3.x 运行测试（使用已生成的数据）
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" run_benchmarks.py --scale medium

# 步骤3：分析结果（使用任一 Python 版本）
python analyze_results.py
```

### 3. 包含开源库对比（Python 3.x 环境）

```bash
# 确保已安装开源库
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" -m pip install geopandas rasterio shapely pyogrio

# 运行测试（包含开源对比）
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" run_benchmarks.py --scale medium --opensource
```

### 4. 自动运行两个版本

```bash
python run_both_versions.py
```

---

## 查看结果

分析完成后，查看生成的报告：

```bash
# Markdown 报告（可直接在浏览器或 Markdown 编辑器中查看）
C:\temp\arcgis_benchmark_data\<时间戳>\<规模>\comparison_report.md

# LaTeX 表格（可直接插入论文）
C:\temp\arcgis_benchmark_data\<时间戳>\<规模>\comparison_table.tex

# CSV 数据（可用 Excel 打开）
C:\temp\arcgis_benchmark_data\<时间戳>\<规模>\comparison_data.csv
```

---

## 调整测试设置

### 数据规模

在 GUI 界面的「测试设置」区域选择数据规模：

| 规模 | 名称 | 预计时间 | 适用场景 |
|------|------|----------|----------|
| tiny | 超小 | 1-2分钟 | 快速验证/调试 |
| small | 小型 | 5-10分钟 | 功能测试 |
| standard | 标准 | 15-30分钟 | 日常测试 |
| medium | 中型 | 30-60分钟 | 性能对比（推荐）|
| large | 大型 | 2-4小时 | 学术研究 |

### 命令行参数

```bash
# 指定数据规模
run_benchmarks.py --scale medium

# 增加测试次数（提高统计可靠性）
run_benchmarks.py --scale medium --runs 5 --warmup 2

# 启用多进程对比
run_benchmarks.py --scale medium --multiprocess --mp-workers 4

# 启用开源库对比
run_benchmarks.py --scale medium --opensource

# 完整参数
run_benchmarks.py --scale medium --runs 3 --warmup 1 --opensource --multiprocess --mp-workers 4
```

### 手动编辑配置

编辑 `config/settings.py`：

```python
# 数据规模（tiny/small/standard/medium/large）
DATA_SCALE = 'medium'

# 循环次数
TEST_RUNS = 3

# 预热次数
WARMUP_RUNS = 0
```

---

## 常用命令

```bash
# 仅运行矢量测试
run_benchmarks.py --category vector --scale medium

# 仅运行栅格测试
run_benchmarks.py --category raster --scale medium

# 仅运行开源测试
run_benchmarks.py --category all --scale medium --opensource

# 指定输出目录
run_benchmarks.py --scale medium --output-dir D:\benchmark_results

# 强制重新生成测试数据
run_benchmarks.py --scale medium --generate-data
```

---

## 故障排除

### GUI 无法启动

1. 检查是否安装了 ArcGIS Pro（推荐）或 ArcGIS Desktop
2. 尝试使用命令行方式运行
3. 检查 Python 路径是否正确

### 问题：arcpy 不可用
**解决**：确保使用 ArcGIS 自带的 Python 解释器运行脚本

### 问题：开源库未找到
**解决**：
```bash
# 安装开源依赖
"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe" -m pip install geopandas rasterio shapely pyogrio numpy
```

### 问题：内存不足
**解决**：在 GUI 或命令行中选择更小的数据规模（tiny 或 small）

### 问题：许可错误
**解决**：确保 ArcGIS 许可为 Advanced 级别

### 问题：结果文件未生成
**解决**：检查输出根目录是否有写入权限

### 问题：文件锁定（File Lock）
**解决**：
1. 关闭所有 ArcGIS 程序（ArcMap、ArcGIS Pro）
2. 手动删除 `C:\temp\arcgis_benchmark_data` 目录
3. 重新运行测试

---

## 论文写作建议

1. **方法部分**：描述测试环境、数据规模、测试项目
2. **结果部分**：使用生成的表格和图表
3. **讨论部分**：分析 Python 3.x 性能优势的原因

生成的 LaTeX 表格示例：

```latex
\begin{table}[htbp]
\centering
\caption{ArcGIS Python 性能对比}
\input{<输出根目录>/comparison_table.tex}
\end{table}
```

三向对比结果示例：
```
测试项目          | Python 2.7 | Python 3.x | 开源库 | Py3加速 | OS加速
------------------|------------|------------|--------|---------|--------
CreateFishnet     | 0.998s     | 1.040s     | 0.161s | 0.96x   | 6.20x
RasterResample    | 0.550s     | 1.261s     | 0.021s | 0.44x   | 26.4x
```
