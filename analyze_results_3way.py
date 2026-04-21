#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
三向对比分析脚本：Python 2.7 vs Python 3.x vs Open-Source Libraries
Compatible with Python 2.7 and 3.x

Usage:
    python analyze_results_3way.py [--results-dir PATH]
"""
from __future__ import print_function, division, absolute_import
import sys
import os
import json
import csv
import argparse
from datetime import datetime

# Python 2/3 compatibility for file open
import io

def open_text_file(filepath, mode):
    """Open file with UTF-8 encoding for both Python 2 and 3"""
    if sys.version_info[0] >= 3:
        return io.open(filepath, mode, encoding='utf-8', newline='')
    else:
        return io.open(filepath, mode, encoding='utf-8')

open_csv_file = open_text_file

# Add project directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import settings


def _normalize_test_name(name):
    """Normalize benchmark names across legacy OS prefix/suffix variants."""
    name = str(name or '')
    if name.startswith('OS_'):
        return name[3:]
    if name.endswith('_OS'):
        return name[:-3]
    return name


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Analyze ArcGIS Python Benchmark Results (3-way comparison)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  Analyze results in default directory:
    python analyze_results_3way.py
  
  Analyze results in custom directory:
    python analyze_results_3way.py --results-dir /path/to/results
        '''
    )
    
    parser.add_argument(
        '--results-dir',
        type=str,
        default=settings.RAW_RESULTS_DIR,
        help='Directory containing result JSON files (default: from settings)'
    )
    
    parser.add_argument(
        '--output-dir',
        type=str,
        default=settings.TABLES_DIR,
        help='Output directory for generated tables'
    )
    
    # Python 2/3 compatibility for argparse
    if len(sys.argv) == 1:
        return parser.parse_args([])
    
    return parser.parse_args()


def load_results(results_dir):
    """Load benchmark results from JSON files (3-way)"""
    results_py2 = None
    results_py3 = None
    results_os = None
    
    # Look for result files
    for filename in os.listdir(results_dir):
        if filename.endswith('.json') and 'benchmark_results' in filename:
            filepath = os.path.join(results_dir, filename)
            
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            results = data.get('results', [])
            
            # Determine Python version from filename or content
            lower_name = filename.lower()
            if 'py2' in lower_name:
                results_py2 = results
                print("Loaded Python 2.7 results from: {}".format(filename))
            elif ('benchmark_results_os' in lower_name or
                  lower_name.endswith('_os.json') or
                  'os_' in lower_name or
                  'opensource' in lower_name):
                results_os = results
                print("Loaded Open-Source results from: {}".format(filename))
            elif 'py3' in lower_name:
                results_py3 = results
                print("Loaded Python 3.x results from: {}".format(filename))
            else:
                # Try to detect from content
                if results and 'python_version' in results[0]:
                    py_ver = results[0]['python_version']
                    if py_ver.startswith('2.'):
                        results_py2 = results
                        print("Loaded Python 2.7 results from: {}".format(filename))
                    elif any('OS_' in r.get('test_name', '') for r in results[:5]):
                        results_os = results
                        print("Loaded Open-Source results from: {}".format(filename))
                    else:
                        results_py3 = results
                        print("Loaded Python 3.x results from: {}".format(filename))
    
    return results_py2, results_py3, results_os


def create_3way_comparison(results_py2, results_py3, results_os):
    """Create three-way side-by-side comparison"""
    comparison = []
    
    # Create lookup dictionaries
    py2_lookup = {_normalize_test_name(r['test_name']): r for r in (results_py2 or []) if r.get('success')}
    py3_lookup = {_normalize_test_name(r['test_name']): r for r in (results_py3 or []) if r.get('success')}
    os_lookup = {_normalize_test_name(r['test_name']): r for r in (results_os or []) if r.get('success')}
    
    # Get all base test names (without OS_ prefix)
    all_tests = set()
    for name in list(py2_lookup.keys()) + list(py3_lookup.keys()):
        all_tests.add(name)
    for name in os_lookup.keys():
        # Remove OS_ prefix to match with base tests
        base_name = name.replace('OS_', '')
        all_tests.add(base_name)
    
    for test_name in sorted(all_tests):
        py2_result = py2_lookup.get(test_name, {})
        py3_result = py3_lookup.get(test_name, {})
        os_result = os_lookup.get(test_name, {})
        
        py2_time = py2_result.get('mean_time', 0)
        py3_time = py3_result.get('mean_time', 0)
        os_time = os_result.get('mean_time', 0)
        
        # Calculate speedup vs Py2.7
        if py3_time > 0 and py2_time > 0:
            py3_speedup = py2_time / py3_time
        else:
            py3_speedup = 0
            
        if os_time > 0 and py2_time > 0:
            os_speedup = py2_time / os_time
        elif os_time > 0 and py3_time > 0:
            os_speedup = py3_time / os_time
        else:
            os_speedup = 0
        
        # Determine fastest
        times = {'Python 2.7': py2_time, 'Python 3.x': py3_time, 'Open-Source': os_time}
        valid_times = {k: v for k, v in times.items() if v > 0}
        if valid_times:
            fastest = min(valid_times, key=valid_times.get)
        else:
            fastest = "N/A"
        
        # Get category
        category = py2_result.get('category', py3_result.get('category', os_result.get('category', 'unknown')))
        
        comparison.append({
            'test_name': test_name,
            'category': category,
            'py2_time': py2_time,
            'py2_std': py2_result.get('std_time', 0),
            'py3_time': py3_time,
            'py3_std': py3_result.get('std_time', 0),
            'os_time': os_time,
            'os_std': os_result.get('std_time', 0),
            'py3_speedup': py3_speedup,
            'os_speedup': os_speedup,
            'fastest': fastest,
            'py2_success': test_name in py2_lookup,
            'py3_success': test_name in py3_lookup,
            'os_success': test_name in os_lookup
        })
    
    return comparison


def calculate_3way_statistics(comparison):
    """Calculate 3-way statistics summary"""
    stats = {
        'total_tests': len(comparison),
        'py2_faster': 0,
        'py3_faster': 0,
        'os_faster': 0,
        'py3_vs_py2_avg': 0,
        'os_vs_py2_avg': 0,
        'os_vs_py3_avg': 0,
    }
    
    for c in comparison:
        if c['fastest'] == 'Python 2.7':
            stats['py2_faster'] += 1
        elif c['fastest'] == 'Python 3.x':
            stats['py3_faster'] += 1
        elif c['fastest'] == 'Open-Source':
            stats['os_faster'] += 1
    
    # Calculate average speedups
    py3_speedups = [c['py3_speedup'] for c in comparison if c['py3_speedup'] > 0]
    os_speedups = [c['os_speedup'] for c in comparison if c['os_speedup'] > 0]
    
    if py3_speedups:
        stats['py3_vs_py2_avg'] = sum(py3_speedups) / len(py3_speedups)
    if os_speedups:
        stats['os_vs_py2_avg'] = sum(os_speedups) / len(os_speedups)
    
    return stats


def generate_3way_markdown(comparison, stats, results_py2=None, results_py3=None, results_os=None):
    """Generate 3-way Markdown comparison report"""
    lines = []
    
    lines.append("# ArcGIS Python 三向性能对比测试报告")
    lines.append("")
    lines.append("*生成时间：{}*".format(datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')))
    lines.append("")
    
    # ==================== 1. 执行摘要 ====================
    lines.append("---")
    lines.append("")
    lines.append("# 一、执行摘要")
    lines.append("")
    
    lines.append("本报告对比三种GIS处理方案的性能：")
    lines.append("")
    lines.append("| 方案 | 描述 | 适用场景 |")
    lines.append("|------|------|----------|")
    lines.append("| **Python 2.7 + ArcMap** | arcpy + Python 2.7 | 传统ArcGIS桌面环境 |")
    lines.append("| **Python 3.x + ArcGIS Pro** | arcpy + Python 3.x | 现代ArcGIS Pro环境 |")
    lines.append("| **Python 3.x + 开源库** | GeoPandas + Rasterio + NumPy | 纯Python开源方案 |")
    lines.append("")
    
    # ==================== 2. 统计摘要 ====================
    lines.append("---")
    lines.append("")
    lines.append("# 二、统计摘要")
    lines.append("")
    
    lines.append("## 2.1 总体对比")
    lines.append("")
    lines.append("| 指标 | 数值 | 说明 |")
    lines.append("|------|------|------|")
    lines.append("| 测试项目总数 | {} | 矢量/栅格/混合 |".format(stats['total_tests']))
    lines.append("| Python 2.7 最快 | {} ({:.1f}%) | 基准参照 |".format(stats['py2_faster'], stats['py2_faster']/stats['total_tests']*100 if stats['total_tests'] > 0 else 0))
    lines.append("| Python 3.x 最快 | {} ({:.1f}%) | vs Py2.7 |".format(stats['py3_faster'], stats['py3_faster']/stats['total_tests']*100 if stats['total_tests'] > 0 else 0))
    lines.append("| 开源库 最快 | {} ({:.1f}%) | vs Py2.7/Py3.x |".format(stats['os_faster'], stats['os_faster']/stats['total_tests']*100 if stats['total_tests'] > 0 else 0))
    lines.append("")
    
    lines.append("## 2.2 平均加速比")
    lines.append("")
    lines.append("| 对比 | 平均加速比 | 说明 |")
    lines.append("|------|-----------|------|")
    lines.append("| Python 3.x vs Py2.7 | {:.2f}x | 越高越好 |".format(stats['py3_vs_py2_avg']))
    lines.append("| 开源库 vs Py2.7 | {:.2f}x | 越高越好 |".format(stats['os_vs_py2_avg']))
    lines.append("")
    
    # ==================== 3. 详细对比表 ====================
    lines.append("---")
    lines.append("")
    lines.append("# 三、详细性能对比")
    lines.append("")
    lines.append("## 3.1 完整对比表")
    lines.append("")
    lines.append("| 测试项目 | 类别 | Py2.7 (秒) | Py3.x (秒) | Py3加速 | 开源库 (秒) | OS加速 | 最快 |")
    lines.append("|----------|------|-----------|-----------|--------|------------|--------|------|")
    
    for item in sorted(comparison, key=lambda x: (x['category'], x['test_name'])):
        py2_str = "{:.4f}".format(item['py2_time']) if item['py2_time'] > 0 else "N/A"
        py3_str = "{:.4f}".format(item['py3_time']) if item['py3_time'] > 0 else "N/A"
        os_str = "{:.4f}".format(item['os_time']) if item['os_time'] > 0 else "N/A"
        py3_speed = "{:.2f}x".format(item['py3_speedup']) if item['py3_speedup'] > 0 else "N/A"
        os_speed = "{:.2f}x".format(item['os_speedup']) if item['os_speedup'] > 0 else "N/A"
        
        lines.append("| {} | {} | {} | {} | {} | {} | {} | {} |".format(
            item['test_name'], item['category'], py2_str, py3_str, py3_speed, os_str, os_speed, item['fastest']
        ))
    lines.append("")
    
    # ==================== 4. 类别分析 ====================
    lines.append("---")
    lines.append("")
    lines.append("# 四、类别分析")
    lines.append("")
    
    categories = ['vector', 'raster', 'mixed']
    cat_names = {'vector': '矢量处理', 'raster': '栅格处理', 'mixed': '混合处理'}
    
    for cat in categories:
        cat_tests = [c for c in comparison if c['category'] == cat]
        if not cat_tests:
            continue
            
        lines.append("## 4.{} {}".format(categories.index(cat) + 1, cat_names.get(cat, cat)))
        lines.append("")
        
        # Find fastest in each test for this category
        cat_fastest = {}
        for c in cat_tests:
            cat_fastest[c['test_name']] = c['fastest']
        
        py2_wins = len([v for v in cat_fastest.values() if v == 'Python 2.7'])
        py3_wins = len([v for v in cat_fastest.values() if v == 'Python 3.x'])
        os_wins = len([v for v in cat_fastest.values() if v == 'Open-Source'])
        
        lines.append("- **Python 2.7 最快**: {} 项".format(py2_wins))
        lines.append("- **Python 3.x 最快**: {} 项".format(py3_wins))
        lines.append("- **开源库 最快**: {} 项".format(os_wins))
        lines.append("")
    
    # ==================== 5. 结论 ====================
    lines.append("---")
    lines.append("")
    lines.append("# 五、结论与建议")
    lines.append("")
    
    lines.append("## 5.1 核心发现")
    lines.append("")
    
    fastest_overall = max([
        ('Python 2.7', stats['py2_faster']),
        ('Python 3.x', stats['py3_faster']),
        ('开源库 (GeoPandas/Rasterio)', stats['os_faster'])
    ], key=lambda x: x[1])
    
    lines.append("1. **整体性能排名**: {} 在最多测试项目中表现最佳".format(fastest_overall[0]))
    lines.append("2. **Python 3.x 改进**: 相比 Python 2.7 平均加速 {:.1f}%".format((stats['py3_vs_py2_avg']-1)*100 if stats['py3_vs_py2_avg'] > 0 else 0))
    lines.append("3. **开源库表现**: 相比传统方案平均加速 {:.1f}%".format((stats['os_vs_py2_avg']-1)*100 if stats['os_vs_py2_avg'] > 0 else 0))
    lines.append("")
    
    lines.append("## 5.2 迁移建议")
    lines.append("")
    lines.append("| 场景 | 推荐方案 | 理由 |")
    lines.append("|------|----------|------|")
    lines.append("| 现有ArcMap项目 | Python 2.7 | 保持兼容性 |")
    lines.append("| 新项目开发 | Python 3.x + ArcGIS Pro | 性能+现代特性 |")
    lines.append("| 开源优先环境 | GeoPandas + Rasterio | 无商业许可限制 |")
    lines.append("| 混合工作流 | Python 3.x (两者兼顾) | 与arcpy互操作 |")
    lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("*报告由 ArcGIS Python 三向性能对比工具自动生成*")
    lines.append("")
    lines.append("*项目地址：https://github.com/yourusername/arcgis-python-benchmark*")
    
    return '\n'.join(lines)


def save_3way_outputs(comparison, stats, output_dir, results_py2=None, results_py3=None, results_os=None):
    """Save all 3-way output formats"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    saved_files = {}
    
    # Markdown
    md_content = generate_3way_markdown(comparison, stats, results_py2, results_py3, results_os)
    md_path = os.path.join(output_dir, "comparison_report_3way.md")
    with open_text_file(md_path, 'w') as f:
        f.write(md_content)
    saved_files['markdown'] = md_path
    print("Markdown report saved: {}".format(md_path))
    
    # JSON
    json_path = os.path.join(output_dir, "comparison_data_3way.json")
    with open_text_file(json_path, 'w') as f:
        json.dump({
            'comparison': comparison,
            'statistics': stats,
            'generated': datetime.now().isoformat()
        }, f, indent=2)
    saved_files['json'] = json_path
    print("JSON data saved: {}".format(json_path))
    
    return saved_files


def main():
    """Main function"""
    # Parse arguments
    args = parse_args()
    
    # Print banner
    print("=" * 70)
    print("ArcGIS Python Benchmark - 3-Way Comparison Analyzer")
    print("=" * 70)
    print("")
    print("Results directory: {}".format(args.results_dir))
    print("Output directory: {}".format(args.output_dir))
    print("")
    
    # Load results
    results_py2, results_py3, results_os = load_results(args.results_dir)
    
    if not results_py2 and not results_py3 and not results_os:
        print("\nERROR: No benchmark results found!")
        print("Please run run_benchmarks.py first.")
        return 1
    
    if not results_os:
        print("\nNOTE: Open-source results not found.")
        print("Run with --opensource flag to generate open-source benchmark results.")
        print("Falling back to standard 2-way comparison...")
        return 1
    
    # Create comparison
    print("\nCreating 3-way comparison...")
    comparison = create_3way_comparison(results_py2, results_py3, results_os)
    
    # Calculate statistics
    stats = calculate_3way_statistics(comparison)
    
    # Print summary
    print("\n" + "=" * 70)
    print("Analysis Summary")
    print("=" * 70)
    print("Total tests: {}".format(stats['total_tests']))
    print("Python 2.7 faster: {} ({:.1f}%)".format(stats['py2_faster'], stats['py2_faster']/stats['total_tests']*100))
    print("Python 3.x faster: {} ({:.1f}%)".format(stats['py3_faster'], stats['py3_faster']/stats['total_tests']*100))
    print("Open-Source faster: {} ({:.1f}%)".format(stats['os_faster'], stats['os_faster']/stats['total_tests']*100))
    print("Py3 vs Py2 avg speedup: {:.2f}x".format(stats['py3_vs_py2_avg']))
    print("OS vs Py2 avg speedup: {:.2f}x".format(stats['os_vs_py2_avg']))
    print("=" * 70)
    
    # Save outputs
    print("\nSaving output files...")
    saved_files = save_3way_outputs(comparison, stats, args.output_dir, results_py2, results_py3, results_os)
    
    print("\n" + "=" * 70)
    print("Analysis Complete")
    print("=" * 70)
    print("\nGenerated files:")
    for format_name, filepath in saved_files.items():
        print("  - {}: {}".format(format_name.upper(), filepath))
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
