#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Complete test script: Py2 + Py3 + OS + Multiprocess
保留所有测试数据供检查
"""
from __future__ import print_function, division, absolute_import
import sys
import os
import subprocess
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Python paths
PYTHON27 = r"C:\Python27\ArcGIS10.8\python.exe"
PYTHON3 = r"C:\Program Files\ArcGIS\Pro\bin\Python\envs\arcgispro-py3\python.exe"

def run_command(cmd, desc):
    """Run command and return success status"""
    print("\n" + "="*70)
    print("Running: {}".format(desc))
    print("="*70)
    print("Command: {}".format(cmd))
    
    start = time.time()
    try:
        result = subprocess.call(cmd, shell=True)
        elapsed = time.time() - start
        print("\nCompleted in {:.1f}s (exit code: {})".format(elapsed, result))
        return result == 0
    except Exception as e:
        print("\nError: {}".format(str(e)))
        return False

def main():
    print("="*70)
    print("Complete ArcGIS Benchmark Test - TINY Scale")
    print("="*70)
    print("This will run:")
    print("  1. Python 2.7 (arcpy)")
    print("  2. Python 3.x (arcpy + open-source)")
    print("  3. Multiprocess tests")
    print("  4. Generate comparison report")
    print("="*70)
    
    # Change to script directory
    os.chdir(SCRIPT_DIR)
    
    # Step 1: Python 2.7 test
    if not run_command('"{}" run_benchmarks.py --scale tiny --runs 1 --warmup 0'.format(PYTHON27), 
                       "Python 2.7 arcpy tests"):
        print("\n[ERROR] Python 2.7 tests failed!")
        return 1
    
    # Step 2: Python 3.x test (with opensource)
    if not run_command('"{}" run_benchmarks.py --scale tiny --runs 1 --warmup 0 --opensource --multiprocess --mp-workers 4'.format(PYTHON3),
                       "Python 3.x arcpy + open-source + multiprocess tests"):
        print("\n[ERROR] Python 3.x tests failed!")
        return 1
    
    # Step 3: Analyze results
    if not run_command('"{}" analyze_results.py'.format(PYTHON3),
                       "Generate comparison report"):
        print("\n[ERROR] Report generation failed!")
        return 1
    
    print("\n" + "="*70)
    print("ALL TESTS COMPLETED SUCCESSFULLY!")
    print("="*70)
    print("\nData location: C:\\temp\\arcgis_benchmark_data\\")
    print("Report location: results\\tables\\comparison_report.md")
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
