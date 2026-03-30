#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Run full test with OS multiprocess support
"""
import sys
sys.path.insert(0, '.')
from config import settings
settings.set_scale('tiny')

from benchmarks.vector_benchmarks import VectorBenchmarks
from benchmarks.raster_benchmarks import RasterBenchmarks
from benchmarks.mixed_benchmarks import MixedBenchmarks
from benchmarks.vector_benchmarks_os import VectorBenchmarksOS
from benchmarks.raster_benchmarks_os import RasterBenchmarksOS
from benchmarks.mixed_benchmarks_os import MixedBenchmarksOS
from benchmarks.multiprocess_tests import get_multiprocess_benchmarks
from benchmarks.multiprocess_tests_os import MultiprocessTestsOS
from utils.result_exporter import ResultExporter

all_results = []
num_runs = 1
warmup_runs = 0
num_workers = 4

print('='*70)
print('Running ArcPy Benchmarks')
print('='*70)

# ArcPy benchmarks
for bm in VectorBenchmarks.get_all_benchmarks():
    stats = bm.run(num_runs=num_runs, warmup_runs=warmup_runs)
    all_results.append(stats)
    print("[OK] {}: {:.4f}s".format(bm.name, stats.get('mean_time', 0)))

for bm in RasterBenchmarks.get_all_benchmarks():
    stats = bm.run(num_runs=num_runs, warmup_runs=warmup_runs)
    all_results.append(stats)
    print("[OK] {}: {:.4f}s".format(bm.name, stats.get('mean_time', 0)))

for bm in MixedBenchmarks.get_all_benchmarks():
    stats = bm.run(num_runs=num_runs, warmup_runs=warmup_runs)
    all_results.append(stats)
    print("[OK] {}: {:.4f}s".format(bm.name, stats.get('mean_time', 0)))

print('\n' + '='*70)
print('Running Open-Source Benchmarks')
print('='*70)

# OS benchmarks
for bm in VectorBenchmarksOS.get_all_benchmarks():
    stats = bm.run(num_runs=num_runs, warmup_runs=warmup_runs)
    all_results.append(stats)
    print("[OK] {}: {:.4f}s".format(bm.name, stats.get('mean_time', 0)))

for bm in RasterBenchmarksOS.get_all_benchmarks():
    stats = bm.run(num_runs=num_runs, warmup_runs=warmup_runs)
    all_results.append(stats)
    print("[OK] {}: {:.4f}s".format(bm.name, stats.get('mean_time', 0)))

for bm in MixedBenchmarksOS.get_all_benchmarks():
    stats = bm.run(num_runs=num_runs, warmup_runs=warmup_runs)
    all_results.append(stats)
    print("[OK] {}: {:.4f}s".format(bm.name, stats.get('mean_time', 0)))

print('\n' + '='*70)
print('Running ArcPy Multiprocess Benchmarks')
print('='*70)

# ArcPy multiprocess
mp_benchmarks = get_multiprocess_benchmarks()
for benchmark in mp_benchmarks:
    # Single process
    fresh_bm = benchmark.__class__()
    fresh_bm.setup()
    stats_single = fresh_bm.run(num_runs=num_runs, warmup_runs=warmup_runs, use_multiprocess=False)
    fresh_bm.teardown()
    stats_single['test_name'] = "Py3_{}_single".format(benchmark.name)
    all_results.append(stats_single)
    print("[OK] {}_single: {:.4f}s".format(benchmark.name, stats_single.get('mean_time', 0)))
    
    # Multiprocess
    fresh_bm = benchmark.__class__()
    fresh_bm.setup()
    stats_mp = fresh_bm.run(num_runs=num_runs, warmup_runs=warmup_runs, use_multiprocess=True)
    fresh_bm.teardown()
    stats_mp['test_name'] = "Py3_{}_multiprocess".format(benchmark.name)
    stats_mp['num_workers'] = num_workers
    all_results.append(stats_mp)
    print("[OK] {}_multiprocess: {:.4f}s".format(benchmark.name, stats_mp.get('mean_time', 0)))

print('\n' + '='*70)
print('Running Open-Source Multiprocess Benchmarks')
print('='*70)

# OS multiprocess
os_mp_benchmarks = MultiprocessTestsOS.get_all_benchmarks()
for benchmark in os_mp_benchmarks:
    # Single process
    fresh_bm = benchmark.__class__()
    fresh_bm.setup()
    stats_single = fresh_bm.run(num_runs=num_runs, warmup_runs=warmup_runs, use_multiprocess=False)
    fresh_bm.teardown()
    stats_single['test_name'] = "OS_{}_single".format(benchmark.name)
    all_results.append(stats_single)
    print("[OK] {}_single: {:.4f}s".format(benchmark.name, stats_single.get('mean_time', 0)))
    
    # Multiprocess
    fresh_bm = benchmark.__class__()
    fresh_bm.setup()
    stats_mp = fresh_bm.run(num_runs=num_runs, warmup_runs=warmup_runs, use_multiprocess=True)
    fresh_bm.teardown()
    stats_mp['test_name'] = "OS_{}_multiprocess".format(benchmark.name)
    stats_mp['num_workers'] = num_workers
    all_results.append(stats_mp)
    print("[OK] {}_multiprocess: {:.4f}s".format(benchmark.name, stats_mp.get('mean_time', 0)))

print('\n' + '='*70)
print('Saving Results')
print('='*70)

exporter = ResultExporter(settings.RAW_RESULTS_DIR)
exporter.export_json(all_results, 'benchmark_results_py3.json')
print('Saved {} results'.format(len(all_results)))

success_count = sum(1 for r in all_results if r['success'])
print("Success: {}/{}".format(success_count, len(all_results)))
