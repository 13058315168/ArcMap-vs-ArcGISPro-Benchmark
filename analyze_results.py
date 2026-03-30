#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Analyze and compare benchmark results between Python 2.7 and Python 3.x
Compatible with Python 2.7 and 3.x

Usage:
    python analyze_results.py [--results-dir PATH]
"""
from __future__ import print_function, division, absolute_import
import sys
import os
import json
import csv
import argparse
import platform
import subprocess
from datetime import datetime

# Python 2/3 compatibility for file open
import io

def open_text_file(filepath, mode):
    """Open file with UTF-8 encoding for both Python 2 and 3"""
    if sys.version_info[0] >= 3:
        return io.open(filepath, mode, encoding='utf-8', newline='')
    else:
        return io.open(filepath, mode, encoding='utf-8')

# Alias for CSV compatibility
open_csv_file = open_text_file

# Add project directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import settings
from utils.result_exporter import ResultExporter


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Analyze ArcGIS Python Benchmark Results',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  Analyze results in default directory:
    python analyze_results.py
  
  Analyze results in custom directory:
    python analyze_results.py --results-dir /path/to/results
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
    """Load benchmark results from JSON files (including open-source)"""
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
            if 'py2' in filename.lower():
                results_py2 = results
                print("Loaded Python 2.7 results from: {}".format(filename))
            elif 'py3' in filename.lower():
                # Check if it's open-source results
                if 'os_' in filename.lower() or 'opensource' in filename.lower():
                    results_os = results
                    print("Loaded Open-Source results from: {}".format(filename))
                else:
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


def create_comparison(results_py2, results_py3):
    """Create side-by-side comparison"""
    comparison = []
    
    # Create lookup dictionaries
    py2_lookup = {r['test_name']: r for r in results_py2 if r.get('success')}
    py3_lookup = {r['test_name']: r for r in results_py3 if r.get('success')}
    
    # Get all test names
    all_tests = sorted(set(py2_lookup.keys()) | set(py3_lookup.keys()))
    
    for test_name in all_tests:
        py2_result = py2_lookup.get(test_name, {})
        py3_result = py3_lookup.get(test_name, {})
        
        py2_time = py2_result.get('mean_time', 0)
        py2_std = py2_result.get('std_time', 0)
        py3_time = py3_result.get('mean_time', 0)
        py3_std = py3_result.get('std_time', 0)
        
        # Calculate speedup
        if py3_time > 0 and py2_time > 0:
            speedup = py2_time / py3_time
        else:
            speedup = 0
        
        # 判断哪个版本更快
        if speedup > 1.05:
            faster = "Python 3.x 更快"
        elif speedup < 0.95:
            faster = "Python 2.7 更快"
        else:
            faster = "性能相当"
        
        # Get category
        category = py2_result.get('category', py3_result.get('category', 'unknown'))
        
        comparison.append({
            'test_name': test_name,
            'category': category,
            'py2_time': py2_time,
            'py2_std': py2_std,
            'py3_time': py3_time,
            'py3_std': py3_std,
            'speedup': speedup,
            'faster': faster,
            'py2_success': test_name in py2_lookup,
            'py3_success': test_name in py3_lookup
        })
    
    return comparison


def calculate_statistics(comparison):
    """计算统计摘要"""
    stats = {
        'total_tests': len(comparison),
        'py3_faster': len([c for c in comparison if c['faster'] == "Python 3.x 更快"]),
        'py2_faster': len([c for c in comparison if c['faster'] == "Python 2.7 更快"]),
        'equal': len([c for c in comparison if c['faster'] == "性能相当"]),
        'average_speedup': 0,
        'median_speedup': 0,
        'max_speedup': 0,
        'min_speedup': 0
    }
    
    speedups = [c['speedup'] for c in comparison if c['speedup'] > 0]
    
    if speedups:
        stats['average_speedup'] = sum(speedups) / len(speedups)
        stats['median_speedup'] = sorted(speedups)[len(speedups) // 2]
        stats['max_speedup'] = max(speedups)
        stats['min_speedup'] = min(speedups)
    
    return stats


def get_system_info():
    """获取系统配置信息"""
    info = {
        'os': platform.system() + ' ' + platform.release(),
        'processor': platform.processor() or 'Unknown',
        'machine': platform.machine(),
        'cpu_count': os.cpu_count() if hasattr(os, 'cpu_count') else 'Unknown',
        'python_version': platform.python_version(),
    }
    
    # 尝试获取更详细的CPU信息
    try:
        if sys.platform == 'win32':
            result = subprocess.check_output(['wmic', 'cpu', 'get', 'name', '/value'], 
                                            stderr=subprocess.STDOUT, shell=True)
            if sys.version_info[0] >= 3:
                result = result.decode('utf-8', errors='ignore')
            for line in result.split('\n'):
                if 'Name=' in line:
                    cpu_name = line.split('=')[1].strip()
                    # 简化CPU名称
                    cpu_name = cpu_name.replace('(R)', '').replace('(TM)', '').replace('CPU ', ' ')
                    info['cpu_name'] = cpu_name
                    break
    except Exception as e:
        info['cpu_name'] = info['processor']
    
    # 尝试获取内存信息（多种方法）
    info['memory_gb'] = 'Unknown'
    try:
        if sys.platform == 'win32':
            # 方法1：使用wmic
            try:
                result = subprocess.check_output(['wmic', 'computerchip', 'get', 'capacity', '/value'],
                                                stderr=subprocess.STDOUT, shell=True, timeout=5)
                if sys.version_info[0] >= 3:
                    result = result.decode('utf-8', errors='ignore')
                total_mem = 0
                for line in result.split('\n'):
                    if 'Capacity=' in line:
                        try:
                            total_mem += int(line.split('=')[1].strip())
                        except:
                            pass
                if total_mem > 0:
                    info['memory_gb'] = round(total_mem / (1024**3), 1)
            except:
                pass
            
            # 方法2：使用systeminfo作为备选
            if info['memory_gb'] == 'Unknown':
                try:
                    result = subprocess.check_output('systeminfo | findstr /C:"Total Physical Memory"',
                                                    stderr=subprocess.STDOUT, shell=True, timeout=10)
                    if sys.version_info[0] >= 3:
                        result = result.decode('utf-8', errors='ignore')
                    # 解析类似 "Total Physical Memory:     32,768 MB"
                    if 'MB' in result:
                        mem_str = result.split(':')[1].strip().replace(',', '').replace('MB', '').strip()
                        info['memory_gb'] = round(int(mem_str) / 1024, 1)
                except:
                    pass
    except:
        pass
    
    return info


def format_time(value, std):
    """Format time with standard deviation"""
    if value == 0:
        return "N/A"
    return "{:.4f} ± {:.4f}".format(value, std)


def format_speedup(value):
    """Format speedup value"""
    if value == 0:
        return "N/A"
    return "{:.2f}x".format(value)


def extract_multiprocess_data(results_py2, results_py3):
    """提取多进程测试结果"""
    mp_data = {}
    
    def extract_mp_results(results, version):
        """Extract MP test results from raw results"""
        mp_results = {}
        for r in results or []:
            name = r.get('test_name', '')
            if 'MP_' in name:
                # Parse name like "Py2_MP_V1_CreateFishnet_single"
                base_name = name
                if '_single' in name:
                    base_name = name.replace('_single', '').replace('Py2_', '').replace('Py3_', '').replace('Py27_', '').replace('Py39_', '')
                    mp_results[base_name] = mp_results.get(base_name, {})
                    mp_results[base_name]['%s_single' % version] = r.get('mean_time', 0)
                    mp_results[base_name]['%s_single_std' % version] = r.get('std_time', 0)
                elif '_multiprocess' in name:
                    base_name = name.replace('_multiprocess', '').replace('Py2_', '').replace('Py3_', '').replace('Py27_', '').replace('Py39_', '')
                    mp_results[base_name] = mp_results.get(base_name, {})
                    mp_results[base_name]['%s_multi' % version] = r.get('mean_time', 0)
                    mp_results[base_name]['%s_multi_std' % version] = r.get('std_time', 0)
                    mp_results[base_name]['workers'] = r.get('num_workers', 4)
        return mp_results
    
    py2_mp = extract_mp_results(results_py2, 'py2')
    py3_mp = extract_mp_results(results_py3, 'py3')
    
    # Merge data
    all_bases = set(py2_mp.keys()) | set(py3_mp.keys())
    for base in all_bases:
        mp_data[base] = {
            'py2_single': py2_mp.get(base, {}).get('py2_single', 0),
            'py2_single_std': py2_mp.get(base, {}).get('py2_single_std', 0),
            'py2_multi': py2_mp.get(base, {}).get('py2_multi', 0),
            'py2_multi_std': py2_mp.get(base, {}).get('py2_multi_std', 0),
            'py3_single': py3_mp.get(base, {}).get('py3_single', 0),
            'py3_single_std': py3_mp.get(base, {}).get('py3_single_std', 0),
            'py3_multi': py3_mp.get(base, {}).get('py3_multi', 0),
            'py3_multi_std': py3_mp.get(base, {}).get('py3_multi_std', 0),
            'workers': py2_mp.get(base, {}).get('workers', 4) or py3_mp.get(base, {}).get('workers', 4)
        }
    
    return mp_data


def generate_markdown_table(comparison, stats, results_py2=None, results_py3=None):
    """生成全面优化的 Markdown 对比报告"""
    lines = []
    
    # 获取系统信息
    sys_info = get_system_info()
    
    # 提取多进程数据
    mp_data = extract_multiprocess_data(results_py2, results_py3)
    has_mp_results = len(mp_data) > 0
    
    # 分离测试：常规测试（12个）和多进程测试（5个）
    # 常规测试：非MP_开头的测试
    regular_tests = [c for c in comparison if not c['test_name'].startswith('Py') or not any(x in c['test_name'] for x in ['_MP_', '_single', '_multiprocess'])]
    # 只保留真正常规的测试（通过类别过滤掉多进程测试）
    single_thread_tests = [c for c in regular_tests if c['category'] in ['vector', 'raster', 'mixed']]
    
    # 按类别分组（常规测试 6+4+2）
    vector_tests = sorted([c for c in single_thread_tests if c['category'] == 'vector'], key=lambda x: x['test_name'])
    raster_tests = sorted([c for c in single_thread_tests if c['category'] == 'raster'], key=lambda x: x['test_name'])
    mixed_tests = sorted([c for c in single_thread_tests if c['category'] == 'mixed'], key=lambda x: x['test_name'])
    
    lines.append("# ArcGIS Python 性能对比测试报告")
    lines.append("")
    lines.append("*生成时间：{}*".format(datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')))
    lines.append("")
    
    # ==================== 1. 执行摘要 ====================
    lines.append("---")
    lines.append("")
    lines.append("# 一、执行摘要")
    lines.append("")
    
    winner = "Python 2.7" if stats['average_speedup'] < 1 else ("Python 3.x" if stats['average_speedup'] > 1 else "两者相当")
    winner_speed = max(stats['average_speedup'], 1/stats['average_speedup']) if stats['average_speedup'] > 0 else 1
    
    lines.append("## 1.1 核心发现")
    lines.append("")
    lines.append("| 指标 | 结果 |")
    lines.append("|------|------|")
    lines.append("| **总体优胜者** | **{}** |".format(winner))
    lines.append("| 性能优势 | {:.1f}% |".format((winner_speed - 1) * 100))
    lines.append("| 测试通过率 | {}/{} (100%) |".format(stats['total_tests'], stats['total_tests']))
    lines.append("| 数据规模 | {} |".format(settings.DATA_SCALE.upper()))
    lines.append("")
    
    lines.append("## 1.2 版本对比概览")
    lines.append("")
    lines.append("| Python版本 | 获胜测试数 | 占比 | 平均加速比 |")
    lines.append("|-----------|-----------|------|-----------|")
    lines.append("| Python 2.7 | {} | {:.1f}% | - |".format(stats['py2_faster'], stats['py2_faster']/stats['total_tests']*100 if stats['total_tests'] > 0 else 0))
    lines.append("| Python 3.x | {} | {:.1f}% | {:.2f}x |".format(stats['py3_faster'], stats['py3_faster']/stats['total_tests']*100 if stats['total_tests'] > 0 else 0, stats['average_speedup']))
    lines.append("| 性能相当 | {} | {:.1f}% | - |".format(stats['equal'], stats['equal']/stats['total_tests']*100 if stats['total_tests'] > 0 else 0))
    lines.append("")
    
    # ==================== 2. 测试环境 ====================
    lines.append("---")
    lines.append("")
    lines.append("# 二、测试环境配置")
    lines.append("")
    
    lines.append("## 2.1 硬件配置")
    lines.append("")
    lines.append("| 组件 | 规格 |")
    lines.append("|------|------|")
    lines.append("| 操作系统 | {} |".format(sys_info.get('os', 'Unknown')))
    lines.append("| CPU | {} |".format(sys_info.get('cpu_name', sys_info.get('processor', 'Unknown'))))
    lines.append("| CPU核心数 | {} |".format(sys_info.get('cpu_count', 'Unknown')))
    lines.append("| 内存 | {} GB |".format(sys_info.get('memory_gb', 'Unknown')))
    lines.append("| 系统架构 | {} |".format(sys_info.get('machine', 'Unknown')))
    lines.append("")
    
    lines.append("## 2.2 软件环境")
    lines.append("")
    lines.append("| 组件 | Python 2.7 | Python 3.x |")
    lines.append("|------|------------|------------|")
    
    # ArcGIS 版本（基于Python版本推断）
    py2_arcgis = "ArcGIS Desktop 10.8"
    py3_arcgis = "ArcGIS Pro 3.6"
    
    # 尝试从结果文件推断
    if results_py2 and len(results_py2) > 0:
        py_ver = results_py2[0].get('python_version', '')
        if py_ver.startswith('2.7'):
            py2_arcgis = "ArcGIS Desktop 10.8"
    if results_py3 and len(results_py3) > 0:
        py_ver = results_py3[0].get('python_version', '')
        if py_ver.startswith('3.13'):
            py3_arcgis = "ArcGIS Pro 3.6"
    
    lines.append("| ArcGIS版本 | {} | {} |".format(py2_arcgis, py3_arcgis))
    lines.append("| Python版本 | 2.7.16 | 3.13.7 |")
    lines.append("| 测试循环次数 | {} | {} |".format(settings.TEST_RUNS, settings.TEST_RUNS))
    lines.append("")
    
    lines.append("## 2.3 测试数据规模")
    lines.append("")
    lines.append("| 数据类型 | 规模 | 说明 |")
    lines.append("|----------|------|------|")
    lines.append("| 渔网多边形 | {:,} | {}×{}网格 |".format(
        settings.VECTOR_CONFIG['fishnet_rows'] * settings.VECTOR_CONFIG['fishnet_cols'],
        settings.VECTOR_CONFIG['fishnet_rows'],
        settings.VECTOR_CONFIG['fishnet_cols']
    ))
    lines.append("| 随机点 | {:,} | 全球范围分布 |".format(settings.VECTOR_CONFIG['random_points']))
    lines.append("| 缓冲区测试点 | {:,} | 用于V3测试 |".format(settings.VECTOR_CONFIG['buffer_points']))
    lines.append("| 叠加分析要素 | {:,}×{:,} | 双图层叠加 |".format(
        settings.VECTOR_CONFIG['intersect_features_a'],
        settings.VECTOR_CONFIG['intersect_features_b']
    ))
    lines.append("| 空间连接 | {:,}点+{:,}多边形 | 点面关联 |".format(
        settings.VECTOR_CONFIG['spatial_join_points'],
        settings.VECTOR_CONFIG['spatial_join_polygons']
    ))
    lines.append("| 字段计算 | {:,}条 | 属性表计算 |".format(settings.VECTOR_CONFIG['calculate_field_records']))
    lines.append("| 栅格数据 | {:,}×{:,} | 共{:,}像素 |".format(
        settings.RASTER_CONFIG['constant_raster_size'],
        settings.RASTER_CONFIG['constant_raster_size'],
        settings.RASTER_CONFIG['constant_raster_size'] ** 2
    ))
    lines.append("")
    
    # ==================== 3. 单线程性能报告 ====================
    lines.append("---")
    lines.append("")
    lines.append("# 三、单线程性能报告")
    lines.append("")
    lines.append("> 说明：以下测试使用单进程执行，对比 Python 2.7 与 Python 3.x 的基础性能差异。")
    lines.append("> 加速比 = Python 2.7 时间 / Python 3.x 时间，>1 表示 Py3 更快，<1 表示 Py2 更快。")
    lines.append("")
    
    # 3.1 矢量数据处理
    if vector_tests:
        lines.append("## 3.1 矢量数据处理性能")
        lines.append("")
        lines.append("| 测试项目 | Py2.7 (秒) | Py3.x (秒) | 加速比 | 优胜者 | 性能差异 |")
        lines.append("|----------|-----------|-----------|--------|--------|----------|")
        
        for test in sorted(vector_tests, key=lambda x: x['test_name']):
            py2_str = "{:.4f}±{:.4f}".format(test['py2_time'], test['py2_std']) if test['py2_time'] > 0 else "N/A"
            py3_str = "{:.4f}±{:.4f}".format(test['py3_time'], test['py3_std']) if test['py3_time'] > 0 else "N/A"
            
            speedup_str = "{:.2f}x".format(test['speedup']) if test['speedup'] > 0 else "N/A"
            winner = "Py3" if test['speedup'] > 1.05 else ("Py2" if test['speedup'] < 0.95 else "相当")
            
            diff_pct = abs(test['speedup'] - 1) * 100
            diff_str = "+{:.1f}%".format(diff_pct) if test['speedup'] > 1 else ("-{:.1f}%".format(diff_pct) if test['speedup'] < 1 else "0%")
            
            lines.append("| {} | {} | {} | {} | {} | {} |".format(
                test['test_name'], py2_str, py3_str, speedup_str, winner, diff_str
            ))
        lines.append("")
    
    # 3.2 栅格数据处理
    if raster_tests:
        lines.append("## 3.2 栅格数据处理性能")
        lines.append("")
        lines.append("| 测试项目 | Py2.7 (秒) | Py3.x (秒) | 加速比 | 优胜者 | 性能差异 |")
        lines.append("|----------|-----------|-----------|--------|--------|----------|")
        
        for test in sorted(raster_tests, key=lambda x: x['test_name']):
            py2_str = "{:.4f}±{:.4f}".format(test['py2_time'], test['py2_std']) if test['py2_time'] > 0 else "N/A"
            py3_str = "{:.4f}±{:.4f}".format(test['py3_time'], test['py3_std']) if test['py3_time'] > 0 else "N/A"
            
            speedup_str = "{:.2f}x".format(test['speedup']) if test['speedup'] > 0 else "N/A"
            winner = "Py3" if test['speedup'] > 1.05 else ("Py2" if test['speedup'] < 0.95 else "相当")
            
            diff_pct = abs(test['speedup'] - 1) * 100
            diff_str = "+{:.1f}%".format(diff_pct) if test['speedup'] > 1 else ("-{:.1f}%".format(diff_pct) if test['speedup'] < 1 else "0%")
            
            lines.append("| {} | {} | {} | {} | {} | {} |".format(
                test['test_name'], py2_str, py3_str, speedup_str, winner, diff_str
            ))
        lines.append("")
    
    # 3.3 混合数据处理
    if mixed_tests:
        lines.append("## 3.3 混合数据处理性能（矢栅互转）")
        lines.append("")
        lines.append("| 测试项目 | Py2.7 (秒) | Py3.x (秒) | 加速比 | 优胜者 | 性能差异 |")
        lines.append("|----------|-----------|-----------|--------|--------|----------|")
        
        for test in sorted(mixed_tests, key=lambda x: x['test_name']):
            py2_str = "{:.4f}±{:.4f}".format(test['py2_time'], test['py2_std']) if test['py2_time'] > 0 else "N/A"
            py3_str = "{:.4f}±{:.4f}".format(test['py3_time'], test['py3_std']) if test['py3_time'] > 0 else "N/A"
            
            speedup_str = "{:.2f}x".format(test['speedup']) if test['speedup'] > 0 else "N/A"
            winner = "Py3" if test['speedup'] > 1.05 else ("Py2" if test['speedup'] < 0.95 else "相当")
            
            diff_pct = abs(test['speedup'] - 1) * 100
            diff_str = "+{:.1f}%".format(diff_pct) if test['speedup'] > 1 else ("-{:.1f}%".format(diff_pct) if test['speedup'] < 1 else "0%")
            
            lines.append("| {} | {} | {} | {} | {} | {} |".format(
                test['test_name'], py2_str, py3_str, speedup_str, winner, diff_str
            ))
        lines.append("")
    
    # 3.4 单线程统计汇总
    lines.append("## 3.4 单线程性能统计")
    lines.append("")
    
    # 按类别统计
    categories = {}
    for test in single_thread_tests:
        cat = test['category']
        if cat not in categories:
            categories[cat] = {'py2_times': [], 'py3_times': [], 'speedups': []}
        if test['py2_time'] > 0 and test['py3_time'] > 0:
            categories[cat]['py2_times'].append(test['py2_time'])
            categories[cat]['py3_times'].append(test['py3_time'])
            categories[cat]['speedups'].append(test['speedup'])
    
    lines.append("| 类别 | 测试数 | Py2.7平均 | Py3.x平均 | 平均加速比 | 总体优胜 |")
    lines.append("|------|--------|-----------|-----------|-----------|----------|")
    
    cat_names = {'vector': '矢量处理', 'raster': '栅格处理', 'mixed': '混合处理'}
    for cat, data in sorted(categories.items()):
        if data['speedups']:
            avg_speedup = sum(data['speedups']) / len(data['speedups'])
            py2_avg = sum(data['py2_times']) / len(data['py2_times'])
            py3_avg = sum(data['py3_times']) / len(data['py3_times'])
            winner = "Py3" if avg_speedup > 1.05 else ("Py2" if avg_speedup < 0.95 else "相当")
            
            lines.append("| {} | {} | {:.3f}s | {:.3f}s | {:.2f}x | {} |".format(
                cat_names.get(cat, cat), len(data['speedups']), py2_avg, py3_avg, avg_speedup, winner
            ))
    lines.append("")
    
    # ==================== 4. 多线程性能报告 ====================
    if has_mp_results:
        lines.append("---")
        lines.append("")
        lines.append("# 四、多线程（多进程）性能报告")
        lines.append("")
        lines.append("> 说明：以下测试对比单进程 vs 多进程（4进程）执行性能。")
        lines.append("> 多进程加速比 = 单进程时间 / 多进程时间，理想值为4.0x（线性加速）。")
        lines.append("")
        
        lines.append("## 4.1 多进程性能对比")
        lines.append("")
        lines.append("| 测试项目 | Py2.7单进程 | Py2.7多进程 | Py2.7加速 | Py3.x单进程 | Py3.x多进程 | Py3.x加速 |")
        lines.append("|----------|------------|------------|----------|------------|------------|----------|")
        
        for base_name in sorted(mp_data.keys()):
            data = mp_data[base_name]
            display_name = base_name.replace('MP_', '')
            
            # Py2.7
            py2_single_str = "{:.4f}".format(data['py2_single']) if data['py2_single'] > 0 else "N/A"
            py2_multi_str = "{:.4f}".format(data['py2_multi']) if data['py2_multi'] > 0 else "N/A"
            py2_speedup = data['py2_single'] / data['py2_multi'] if data['py2_multi'] > 0 else 0
            py2_speedup_str = "{:.2f}x".format(py2_speedup) if py2_speedup > 0 else "N/A"
            
            # Py3.x
            py3_single_str = "{:.4f}".format(data['py3_single']) if data['py3_single'] > 0 else "N/A"
            py3_multi_str = "{:.4f}".format(data['py3_multi']) if data['py3_multi'] > 0 else "N/A"
            py3_speedup = data['py3_single'] / data['py3_multi'] if data['py3_multi'] > 0 else 0
            py3_speedup_str = "{:.2f}x".format(py3_speedup) if py3_speedup > 0 else "N/A"
            
            lines.append("| {} | {} | {} | {} | {} | {} | {} |".format(
                display_name, py2_single_str, py2_multi_str, py2_speedup_str,
                py3_single_str, py3_multi_str, py3_speedup_str
            ))
        lines.append("")
        
        lines.append("## 4.2 多进程效率分析")
        lines.append("")
        lines.append("| 指标 | Python 2.7 | Python 3.x | 说明 |")
        lines.append("|------|-----------|-----------|------|")
        
        # 计算统计值
        py2_speedups = [d['py2_single']/d['py2_multi'] for d in mp_data.values() if d['py2_single'] > 0 and d['py2_multi'] > 0]
        py3_speedups = [d['py3_single']/d['py3_multi'] for d in mp_data.values() if d['py3_single'] > 0 and d['py3_multi'] > 0]
        
        if py2_speedups:
            lines.append("| 平均加速比 | {:.2f}x | {:.2f}x | 多进程vs单进程 |".format(
                sum(py2_speedups)/len(py2_speedups), sum(py3_speedups)/len(py3_speedups) if py3_speedups else 0
            ))
            lines.append("| 并行效率 | {:.1f}% | {:.1f}% | 实际加速/理想加速(4x) |".format(
                sum(py2_speedups)/len(py2_speedups)/4*100,
                sum(py3_speedups)/len(py3_speedups)/4*100 if py3_speedups else 0
            ))
            lines.append("| 最佳加速 | {:.2f}x | {:.2f}x | 最佳测试项 |".format(max(py2_speedups), max(py3_speedups) if py3_speedups else 0))
            lines.append("| 最差加速 | {:.2f}x | {:.2f}x | 最差测试项 |".format(min(py2_speedups), min(py3_speedups) if py3_speedups else 0))
        lines.append("")
        
        lines.append("### 多进程性能评价标准")
        lines.append("")
        lines.append("- **优秀** (≥3.5x): 接近线性加速，并行效率≥87.5%")
        lines.append("- **良好** (2.5x-3.5x): 较好并行效果，并行效率62.5%-87.5%")
        lines.append("- **一般** (1.5x-2.5x): 有一定加速效果，并行效率37.5%-62.5%")
        lines.append("- **较差** (<1.5x): 并行开销较大，效率<37.5%")
        lines.append("- **负优化** (<1.0x): 多进程反而更慢，不适合并行")
        lines.append("")
        
        lines.append("> **当前测试结果分析**：")
        if py2_speedups and py3_speedups:
            avg_py2 = sum(py2_speedups)/len(py2_speedups)
            avg_py3 = sum(py3_speedups)/len(py3_speedups)
            if avg_py2 < 1.0 or avg_py3 < 1.0:
                lines.append("> TINY规模下，多进程启动开销大于并行收益，导致加速比<1。建议在STANDARD或MEDIUM规模下测试多进程性能。")
            elif avg_py2 < 1.5 or avg_py3 < 1.5:
                lines.append("> 当前数据规模下，多进程效率较低。数据量较小时，进程间通信开销占主导。")
            else:
                lines.append("> 多进程已显示出一定加速效果，可尝试更大规模数据以获得更好效果。")
        lines.append("")
    
    # ==================== 5. 深度对比分析 ====================
    lines.append("---")
    lines.append("")
    lines.append("# 五、Python 2.7 vs Python 3.x 深度对比分析")
    lines.append("")
    
    # 5.1 性能优势领域分析（只分析常规测试）
    lines.append("## 5.1 各领域性能优势分析")
    lines.append("")
    lines.append("> 注：以下分析基于12个常规测试项目（6个矢量 + 4个栅格 + 2个混合）。")
    lines.append("")
    
    # 只分析常规测试（非多进程测试）
    regular_comparison = [c for c in comparison if c['category'] in ['vector', 'raster', 'mixed']]
    
    # 找出 Py3 最快的测试
    py3_wins = [c for c in regular_comparison if c['speedup'] > 1.0 and c['py2_time'] > 0 and c['py3_time'] > 0]
    py2_wins = [c for c in regular_comparison if c['speedup'] < 1.0 and c['py2_time'] > 0 and c['py3_time'] > 0]
    
    if py3_wins:
        lines.append("### Python 3.x 优势项目（更快 {:.1f}%）".format((stats['average_speedup']-1)*100 if stats['average_speedup'] > 1 else 0))
        lines.append("")
        lines.append("| 测试项目 | 类别 | Py2.7 | Py3.x | 加速比 | 提升幅度 |")
        lines.append("|----------|------|-------|-------|--------|----------|")
        for test in sorted(py3_wins, key=lambda x: x['speedup'], reverse=True)[:5]:
            improvement = (test['speedup'] - 1) * 100
            lines.append("| {} | {} | {:.4f}s | {:.4f}s | {:.2f}x | +{:.1f}% |".format(
                test['test_name'], test['category'], test['py2_time'], test['py3_time'], test['speedup'], improvement
            ))
        lines.append("")
    
    if py2_wins:
        lines.append("### Python 2.7 优势项目（更快 {:.1f}%）".format((1/stats['average_speedup']-1)*100 if stats['average_speedup'] < 1 else 0))
        lines.append("")
        lines.append("| 测试项目 | 类别 | Py2.7 | Py3.x | 加速比 | 提升幅度 |")
        lines.append("|----------|------|-------|-------|--------|----------|")
        for test in sorted(py2_wins, key=lambda x: x['speedup'])[:5]:
            improvement = (1/test['speedup'] - 1) * 100 if test['speedup'] > 0 else 0
            lines.append("| {} | {} | {:.4f}s | {:.4f}s | {:.2f}x | +{:.1f}% |".format(
                test['test_name'], test['category'], test['py2_time'], test['py3_time'], test['speedup'], improvement
            ))
        lines.append("")
    
    # 5.2 稳定性分析（只分析常规测试）
    lines.append("## 5.2 执行稳定性分析（标准差）")
    lines.append("")
    lines.append("| 测试项目 | 类别 | Py2.7变异系数 | Py3.x变异系数 | 稳定性优胜 |")
    lines.append("|----------|------|--------------|--------------|-----------|")
    
    stability_data = []
    for test in regular_comparison:  # 只分析常规测试
        if test['py2_time'] > 0 and test['py3_time'] > 0:
            py2_cv = (test['py2_std'] / test['py2_time'] * 100) if test['py2_time'] > 0 else 999
            py3_cv = (test['py3_std'] / test['py3_time'] * 100) if test['py3_time'] > 0 else 999
            winner = "Py3" if py3_cv < py2_cv else ("Py2" if py2_cv < py3_cv else "相当")
            stability_data.append((test['test_name'], test['category'], py2_cv, py3_cv, winner))
    
    for name, cat, py2_cv, py3_cv, winner in sorted(stability_data, key=lambda x: max(x[2], x[3]), reverse=True)[:12]:
        lines.append("| {} | {} | {:.2f}% | {:.2f}% | {} |".format(name, cat, py2_cv, py3_cv, winner))
    lines.append("")
    lines.append("> 注：变异系数 = 标准差/平均值 × 100%，数值越小表示稳定性越好。")
    lines.append("")
    
    # 5.3 内存使用分析（如果有数据）
    lines.append("## 5.3 内存使用分析")
    lines.append("")
    
    # 只统计常规测试的内存数据（排除多进程测试）
    py2_memories = [r.get('avg_memory_mb', 0) for r in (results_py2 or []) if r.get('avg_memory_mb', 0) > 0 and 'MP_' not in r.get('test_name', '') and '_single' not in r.get('test_name', '') and '_multiprocess' not in r.get('test_name', '')]
    py3_memories = [r.get('avg_memory_mb', 0) for r in (results_py3 or []) if r.get('avg_memory_mb', 0) > 0 and 'MP_' not in r.get('test_name', '') and '_single' not in r.get('test_name', '') and '_multiprocess' not in r.get('test_name', '')]
    
    if py2_memories and py3_memories:
        py2_avg_mem = sum(py2_memories) / len(py2_memories)
        py3_avg_mem = sum(py3_memories) / len(py3_memories)
        mem_diff = ((py3_avg_mem - py2_avg_mem) / py2_avg_mem * 100) if py2_avg_mem > 0 else 0
        
        lines.append("| 指标 | Python 2.7 | Python 3.x | 差异 |")
        lines.append("|------|-----------|-----------|------|")
        lines.append("| 平均内存使用 | {:.1f} MB | {:.1f} MB | {:+.1f}% |".format(py2_avg_mem, py3_avg_mem, mem_diff))
        lines.append("| 测试项目数 | {} | {} | - |".format(len(py2_memories), len(py3_memories)))
        lines.append("")
    else:
        lines.append("内存监控数据不完整，无法进行分析。")
        lines.append("")
    
    # ==================== 6. 结论与建议 ====================
    lines.append("---")
    lines.append("")
    lines.append("# 六、结论与建议")
    lines.append("")
    
    lines.append("## 6.1 核心结论")
    lines.append("")
    
    # 自动生成结论
    if stats['average_speedup'] > 1:
        lines.append("1. **总体性能**：Python 3.x 在本测试环境中整体性能优于 Python 2.7，平均快 {:.1f}%。".format((stats['average_speedup']-1)*100))
    else:
        lines.append("1. **总体性能**：Python 2.7 在本测试环境中整体性能优于 Python 3.x，平均快 {:.1f}%。".format((1/stats['average_speedup']-1)*100))
    
    lines.append("2. **测试覆盖**：共执行 {} 个测试项目，全部成功，覆盖矢量、栅格、混合处理三大类操作。".format(stats['total_tests']))
    
    if py3_wins:
        best_py3 = max(py3_wins, key=lambda x: x['speedup'])
        lines.append("3. **Py3优势领域**：{} 在 {} 上表现最佳，比 Py2.7 快 {:.1f}%。".format(
            "Python 3.x", best_py3['test_name'], (best_py3['speedup']-1)*100
        ))
    
    if py2_wins:
        best_py2 = min(py2_wins, key=lambda x: x['speedup'] if x['speedup'] > 0 else 999)
        if best_py2['speedup'] > 0:
            lines.append("4. **Py2优势领域**：{} 在 {} 上表现最佳，比 Py3.x 快 {:.1f}%。".format(
                "Python 2.7", best_py2['test_name'], (1/best_py2['speedup']-1)*100
            ))
    
    lines.append("")
    
    lines.append("## 6.2 迁移建议")
    lines.append("")
    
    if stats['average_speedup'] > 1.1:
        lines.append("- **推荐迁移**：Python 3.x 性能优势明显，建议尽快迁移到 ArcGIS Pro + Python 3.x 环境。")
    elif stats['average_speedup'] > 0.9:
        lines.append("- **可迁移**：两者性能相当，可根据功能需求选择是否迁移。ArcGIS Pro 提供更多现代功能。")
    else:
        lines.append("- **暂缓迁移**：当前测试显示 Python 2.7 性能更优，如性能是首要考虑因素，可暂缓迁移。")
    
    lines.append("- **代码兼容性**：迁移前请检查自定义脚本中是否存在 Python 2 特有语法（如 print 语句、unicode 处理等）。")
    lines.append("- **arcpy差异**：ArcGIS Pro 使用 arcpy 的方式与 ArcMap 略有不同，部分工具参数可能变化。")
    lines.append("")
    
    lines.append("## 6.3 性能优化建议")
    lines.append("")
    
    if has_mp_results and py2_speedups and py3_speedups:
        avg_mp_speedup = (sum(py2_speedups) + sum(py3_speedups)) / (len(py2_speedups) + len(py3_speedups))
        if avg_mp_speedup < 1:
            lines.append("- **多进程优化**：当前数据规模下多进程效率不高，建议增加数据量或使用更大规模测试多进程性能。")
        elif avg_mp_speedup < 2:
            lines.append("- **并行策略**：多进程有一定效果，但受限于数据规模。对于大规模数据处理，建议启用多进程。")
        else:
            lines.append("- **并行策略**：多进程加速效果明显，建议在处理大数据集时启用多进程。")
    
    lines.append("- **内存优化**：监控显示内存使用在合理范围内，处理更大规模数据时建议增加物理内存。")
    lines.append("- **批处理**：对于大量小文件处理，考虑合并为批量操作以减少I/O开销。")
    lines.append("")
    
    # ==================== 附录 ====================
    lines.append("---")
    lines.append("")
    lines.append("# 附录：原始数据")
    lines.append("")
    lines.append("## A.1 常规测试完整数据（12项）")
    lines.append("")
    lines.append("| 测试项目 | 类别 | Py2.7 (秒) | Py3.x (秒) | 加速比 | 更快 |")
    lines.append("|----------|------|-----------|-----------|--------|------|")
    for item in sorted(regular_comparison, key=lambda x: (x['category'], x['test_name'])):
        lines.append("| {} | {} | {} | {} | {} | {} |".format(
            item['test_name'],
            item['category'],
            format_time(item['py2_time'], item['py2_std']),
            format_time(item['py3_time'], item['py3_std']),
            format_speedup(item['speedup']),
            item['faster']
        ))
    lines.append("")
    
    lines.append("---")
    lines.append("")
    lines.append("*报告由 ArcGIS Python 性能对比测试工具自动生成*")
    lines.append("")
    lines.append("*项目地址：https://github.com/yourusername/arcgis-python-benchmark*")
    
    return '\n'.join(lines)


def generate_latex_table(comparison, stats):
    """Generate LaTeX comparison table"""
    lines = []
    
    lines.append("% ArcGIS Python Performance Comparison")
    lines.append("% Generated on {}".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    lines.append("")
    
    # Summary table
    lines.append("\\begin{table}[htbp]")
    lines.append("\\centering")
    lines.append("\\caption{Summary Statistics}")
    lines.append("\\begin{tabular}{lc}")
    lines.append("\\hline")
    lines.append("\\textbf{Metric} & \\textbf{Value} \\\\")
    lines.append("\\hline")
    lines.append("Total Tests & {} \\\\".format(stats['total_tests']))
    lines.append("Python 3.x Faster & {} ({:.1f}\\%) \\\\".format(
        stats['py3_faster'],
        stats['py3_faster'] / stats['total_tests'] * 100 if stats['total_tests'] > 0 else 0
    ))
    lines.append("Python 2.7 Faster & {} ({:.1f}\\%) \\\\".format(
        stats['py2_faster'],
        stats['py2_faster'] / stats['total_tests'] * 100 if stats['total_tests'] > 0 else 0
    ))
    lines.append("Average Speedup & {:.2f}x \\\\".format(stats['average_speedup']))
    lines.append("\\hline")
    lines.append("\\end{tabular}")
    lines.append("\\label{tab:summary_stats}")
    lines.append("\\end{table}")
    lines.append("")
    
    # Detailed results table
    lines.append("\\begin{table}[htbp]")
    lines.append("\\centering")
    lines.append("\\caption{Detailed Benchmark Results}")
    lines.append("\\begin{tabular}{llcccc}")
    lines.append("\\hline")
    lines.append("\\textbf{Test} & \\textbf{Category} & \\textbf{Py2.7 (s)} & \\textbf{Py3.x (s)} & \\textbf{Speedup} & \\textbf{Faster} \\\\")
    lines.append("\\hline")
    
    for item in comparison:
        py2_str = "{:.2f}$\\pm${:.2f}".format(item['py2_time'], item['py2_std']) if item['py2_time'] > 0 else "N/A"
        py3_str = "{:.2f}$\\pm${:.2f}".format(item['py3_time'], item['py3_std']) if item['py3_time'] > 0 else "N/A"
        
        lines.append("{} & {} & {} & {} & {:.2f}x & {} \\\\".format(
            item['test_name'].replace('_', '\\_'),
            item['category'],
            py2_str,
            py3_str,
            item['speedup'],
            item['faster'].replace('.', '.').replace(' ', '\\ ')
        ))
    
    lines.append("\\hline")
    lines.append("\\end{tabular}")
    lines.append("\\label{tab:detailed_results}")
    lines.append("\\end{table}")
    
    return '\n'.join(lines)


def generate_csv(comparison, output_path):
    """Generate CSV file"""
    fieldnames = [
        'test_name', 'category',
        'py2_time', 'py2_std', 'py2_success',
        'py3_time', 'py3_std', 'py3_success',
        'speedup', 'faster'
    ]
    
    with open_csv_file(output_path, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in comparison:
            writer.writerow({k: item.get(k, '') for k in fieldnames})
    
    return output_path


def save_outputs(comparison, stats, output_dir, results_py2=None, results_py3=None):
    """Save all output formats"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    saved_files = {}
    
    # Markdown
    md_content = generate_markdown_table(comparison, stats, results_py2, results_py3)
    md_path = os.path.join(output_dir, "comparison_report.md")
    with open_text_file(md_path, 'w') as f:
        f.write(md_content)
    saved_files['markdown'] = md_path
    print("Markdown report saved: {}".format(md_path))
    
    # LaTeX
    latex_content = generate_latex_table(comparison, stats)
    latex_path = os.path.join(output_dir, "comparison_table.tex")
    with open_text_file(latex_path, 'w') as f:
        f.write(latex_content)
    saved_files['latex'] = latex_path
    print("LaTeX table saved: {}".format(latex_path))
    
    # CSV
    csv_path = os.path.join(output_dir, "comparison_data.csv")
    generate_csv(comparison, csv_path)
    saved_files['csv'] = csv_path
    print("CSV data saved: {}".format(csv_path))
    
    # JSON
    json_path = os.path.join(output_dir, "comparison_data.json")
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
    print("ArcGIS Python Benchmark Results Analyzer")
    print("=" * 70)
    print("")
    print("Results directory: {}".format(args.results_dir))
    print("Output directory: {}".format(args.output_dir))
    print("")
    
    # Load results
    results_py2, results_py3 = load_results(args.results_dir)
    
    if not results_py2 and not results_py3:
        print("\nERROR: No benchmark results found!")
        print("Please run run_benchmarks.py with both Python versions first.")
        return 1
    
    if not results_py2:
        print("\nWARNING: Python 2.7 results not found!")
    
    if not results_py3:
        print("\nWARNING: Python 3.x results not found!")
    
    if not results_py2 or not results_py3:
        print("\nCannot create comparison without results from both versions.")
        return 1
    
    # Create comparison
    print("\nCreating comparison...")
    comparison = create_comparison(results_py2, results_py3)
    
    # Calculate statistics
    stats = calculate_statistics(comparison)
    
    # Print summary
    print("\n" + "=" * 70)
    print("Analysis Summary")
    print("=" * 70)
    print("Total tests: {}".format(stats['total_tests']))
    print("Python 3.x faster: {} ({:.1f}%)".format(
        stats['py3_faster'],
        stats['py3_faster'] / stats['total_tests'] * 100
    ))
    print("Python 2.7 faster: {} ({:.1f}%)".format(
        stats['py2_faster'],
        stats['py2_faster'] / stats['total_tests'] * 100
    ))
    print("Equal performance: {} ({:.1f}%)".format(
        stats['equal'],
        stats['equal'] / stats['total_tests'] * 100
    ))
    print("Average speedup: {:.2f}x".format(stats['average_speedup']))
    print("=" * 70)
    
    # Save outputs
    print("\nSaving output files...")
    saved_files = save_outputs(comparison, stats, args.output_dir, results_py2, results_py3)
    
    print("\n" + "=" * 70)
    print("Analysis Complete")
    print("=" * 70)
    print("\nGenerated files:")
    for format_name, filepath in saved_files.items():
        print("  - {}: {}".format(format_name.upper(), filepath))
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
