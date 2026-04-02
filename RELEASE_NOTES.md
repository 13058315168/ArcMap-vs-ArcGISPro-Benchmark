# 发布说明

本仓库当前版本已整理为可正式发布状态，名称与入口已统一为“ArcGIS Python2、3 与开源库性能对比测试工具”。

## 已完成收口

- 主入口统一为 `benchmark_gui_modern.py`
- 窗口标题、顶部 Banner、快捷方式描述已同步为新名称
- 所有启动方式统一指向现代 GUI：`启动工具.vbs`、`launch_gui.py`、`launch_gui.bat`、`launch.vbs`、`start_gui_hidden.vbs`
- 结果输出按时间戳根目录组织，版本数据落入 `data/py2`、`data/py3`、`data/os`
- 报告已加入任务级内存占用章节，并支持三方对比
- 开源多进程任务已补全 V4 与 R1，并纳入最终报告
- 仓库已加入忽略规则，避免编译缓存和运行产物污染发布包

## 正式发布前建议复核

1. 重新运行一次完整 `tiny` 规模验证。
2. 确认 `启动工具.vbs` 可以正常拉起 GUI。
3. 检查最终导出的 `comparison_report.md`、`comparison_data.csv`、`comparison_table.tex` 是否完整。
