# -*- coding: utf-8 -*-
"""Base class for all benchmarks.

Compatible with Python 2.7 and 3.x.
"""

from __future__ import print_function, division, absolute_import

import sys
import os
import json
import time

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings
from utils.gis_cleanup import clear_workspace_cache
from utils.timer import BenchmarkTimer, ProgressHeartbeat


def _median(values):
    values = sorted(values or [])
    if not values:
        return 0
    mid = len(values) // 2
    if len(values) % 2:
        return values[mid]
    return (values[mid - 1] + values[mid]) / 2.0


def _median_quartiles(values):
    values = sorted(values or [])
    if not values:
        return 0, 0, 0, 0
    median = _median(values)
    if len(values) == 1:
        return median, median, median, 0
    mid = len(values) // 2
    if len(values) % 2:
        lower = values[:mid]
        upper = values[mid + 1:]
    else:
        lower = values[:mid]
        upper = values[mid:]
    q1 = _median(lower) if lower else median
    q3 = _median(upper) if upper else median
    return median, q1, q3, q3 - q1


def _safe_text(value):
    """Return printable text that is safe on Py2 consoles."""
    try:
        if sys.version_info[0] < 3:
            try:
                unicode_type = unicode  # noqa: F821
            except Exception:
                unicode_type = str
            if isinstance(value, unicode_type):
                return value
            if isinstance(value, bytes):
                return value.decode('utf-8', 'replace')
            return unicode_type(value)
        return str(value)
    except Exception:
        try:
            return repr(value)
        except Exception:
            return 'Unknown error'


class BaseBenchmark(object):
    """Abstract base class for all benchmarks."""

    def __init__(self, name, category="general"):
        self.name = name
        self.category = category
        self.results = []
        self.warmup_results = []
        self.env_info = {}
        self.timer = None
        # Import arcpy if available (optional for open-source benchmarks)
        self.arcpy = None
        try:
            import arcpy
            self.arcpy = arcpy
        except ImportError:
            # arcpy is optional - open-source benchmarks don't need it
            pass

    def _stat_passthrough_keys(self, successful_results):
        """Return result keys that should be promoted into summary statistics."""
        skip_keys = set([
            'success',
            'error',
            'error_type',
            'traceback',
            'elapsed_seconds',
            'memory_mb',
        ])
        keys = []
        for result in successful_results:
            for key in result.keys():
                if key in skip_keys or key.startswith('_'):
                    continue
                if key not in keys:
                    keys.append(key)
        return keys

    def _promote_result_fields(self, stats, successful_results):
        """Promote stable validation/result fields from raw runs to summary stats."""
        for key in self._stat_passthrough_keys(successful_results):
            values = [result.get(key) for result in successful_results if key in result]
            if not values:
                continue
            if key == 'validation_passed':
                stats[key] = len(values) == len(successful_results) and all(bool(v) for v in values)
                continue
            first_value = values[0]
            is_consistent = True
            for value in values[1:]:
                if value != first_value:
                    is_consistent = False
                    break
            if is_consistent:
                stats[key] = first_value
            else:
                stats[key] = first_value
                stats[key + '_consistent'] = False
                stats[key + '_values'] = values
        return stats

    def setup(self):
        """Setup before benchmark - override in subclass."""
        pass

    def teardown(self):
        """Cleanup after benchmark - override in subclass."""
        pass

    def run_single(self):
        """Run a single benchmark iteration - must be implemented by subclass."""
        raise NotImplementedError("Subclasses must implement run_single()")

    def run(self, num_runs=None, warmup_runs=None):
        """Run benchmark with multiple iterations."""
        if num_runs is None:
            num_runs = settings.TEST_RUNS
        if warmup_runs is None:
            warmup_runs = settings.WARMUP_RUNS

        # 显示 Python 版本
        py_version = "Py{}.{}".format(sys.version_info[0], sys.version_info[1])
        print("\n [{}] 初始化测试: {}".format(py_version, self.name))
        print(" 类别: {}".format(self.category))

        try:
            # Setup
            print(" 执行 setup()...")
            with ProgressHeartbeat("{} setup()".format(self.name)):
                self.setup()
            print(" [OK] setup() 完成")

            # Warmup runs
            if warmup_runs > 0:
                print(" 预热运行 ({} 次)...".format(warmup_runs))
                for i in range(warmup_runs):
                    print(" 预热 {}/{}...".format(i + 1, warmup_runs))
                    result = self._run_single_iteration(
                        progress_label="预热 {}/{}".format(i + 1, warmup_runs)
                    )
                    self.warmup_results.append(result)
                    if result.get('success'):
                        print(" 耗时: {:.4f}秒".format(result.get('elapsed_seconds', 0)))
                    else:
                        print(" 失败: {}".format(result.get('error', 'Unknown error')))

            # Actual benchmark runs
            print(" 正式测试运行 ({} 次)...".format(num_runs))
            for i in range(num_runs):
                print(" 运行 {}/{}...".format(i + 1, num_runs))
                result = self._run_single_iteration(
                    progress_label="正式 {}/{}".format(i + 1, num_runs)
                )
                self.results.append(result)
                if result.get('success'):
                    elapsed = result.get('elapsed_seconds', 0)
                    memory_info = ""
                    if 'memory_mb' in result and result['memory_mb'].get('peak_mb'):
                        memory_info = " [内存峰值: {:.1f}MB]".format(result['memory_mb']['peak_mb'])
                    print(" [OK] 耗时: {:.4f}秒{}".format(elapsed, memory_info))
                else:
                    print(" [FAILED] {}".format(_safe_text(result.get('error', 'Unknown error'))))
        finally:
            # Teardown
            print(" 执行 teardown()...")
            try:
                with ProgressHeartbeat("{} teardown()".format(self.name)):
                    self.teardown()
            finally:
                clear_workspace_cache(settings.DATA_DIR)
                print(" [OK] teardown() 完成")

        # Calculate statistics
        return self.get_statistics()

    def _run_single_iteration(self, progress_label=None):
        """Run a single iteration with timing."""
        heartbeat_label = self.name
        if progress_label:
            heartbeat_label = "{} - {}".format(self.name, progress_label)

        with BenchmarkTimer(name=self.name, monitor_memory=settings.ENABLE_MEMORY_MONITORING) as bt:
            with ProgressHeartbeat(heartbeat_label):
                try:
                    repeat_count = int(getattr(self, 'repeat_count', 1) or 1)
                    if repeat_count > 1 and getattr(self, 'enable_repeat_count', False):
                        result = None
                        for _ in range(repeat_count):
                            result = self.run_single()
                    else:
                        # Run the actual benchmark
                        result = self.run_single()
                    result['success'] = True
                except Exception as e:
                    import traceback

                    error_detail = traceback.format_exc()
                    result = {
                        'success': False,
                        'error': str(e),
                        'error_type': type(e).__name__,
                        'traceback': error_detail,
                    }

        # Combine timing results with benchmark result
        timing_results = bt.get_results()
        result.update(timing_results)
        clear_workspace_cache(settings.DATA_DIR)
        return result

    def get_statistics(self):
        """Calculate statistics from results."""
        successful = [r for r in self.results if r.get('success')]
        if not successful:
            return {
                'test_name': self.name,
                'category': self.category,
                'success': False,
                'error': 'All runs failed',
                'total_runs': len(self.results),
                'successful_runs': 0,
            }

        # Extract timing values
        times = [r['elapsed_seconds'] for r in successful]

        # Calculate statistics
        raw_mean_time = sum(times) / len(times)
        min_time = min(times)
        max_time = max(times)

        if len(times) > 1:
            raw_variance = sum((t - raw_mean_time) ** 2 for t in times) / (len(times) - 1)
            raw_std_time = raw_variance ** 0.5
        else:
            raw_std_time = 0

        median_time, q1_time, q3_time, iqr_time = _median_quartiles(times)
        target_band_min = getattr(settings, 'TARGET_RUNTIME_MIN_SECONDS', 120)
        target_band_max = getattr(settings, 'TARGET_RUNTIME_MAX_SECONDS', 300)
        in_target_band = target_band_min <= median_time <= target_band_max

        # Memory statistics
        if settings.ENABLE_MEMORY_MONITORING:
            peak_memories = [r.get('memory_mb', {}).get('peak_mb', 0) for r in successful if 'memory_mb' in r]
            avg_memory = sum(peak_memories) / len(peak_memories) if peak_memories else 0
            min_memory = min(peak_memories) if peak_memories else 0
            max_memory = max(peak_memories) if peak_memories else 0
            if len(peak_memories) > 1:
                memory_variance = sum((m - avg_memory) ** 2 for m in peak_memories) / (len(peak_memories) - 1)
                memory_std = memory_variance ** 0.5
            else:
                memory_std = 0
        else:
            avg_memory = 0
            min_memory = 0
            max_memory = 0
            memory_std = 0

        stats = {
            'test_name': self.name,
            'category': self.category,
            'success': True,
            'total_runs': len(self.results),
            'successful_runs': len(successful),
            'failed_runs': len(self.results) - len(successful),
            'mean_time_raw': raw_mean_time,
            'std_time_raw': raw_std_time,
            'mean_time': median_time,
            'std_time': iqr_time,
            'median_time': median_time,
            'q1_time': q1_time,
            'q3_time': q3_time,
            'iqr_time': iqr_time,
            'target_band_min_seconds': target_band_min,
            'target_band_max_seconds': target_band_max,
            'target_band_label': "{}-{} 分钟".format(int(target_band_min / 60), int(target_band_max / 60)),
            'in_target_band': in_target_band,
            'cv_percent': (raw_std_time / raw_mean_time * 100) if raw_mean_time > 0 else 0,
            'avg_memory_mb': avg_memory,
            'min_memory_mb': min_memory,
            'max_memory_mb': max_memory,
            'std_memory_mb': memory_std,
            'all_times': times,
            'python_version': "{}.{}.{}".format(
                sys.version_info[0],
                sys.version_info[1],
                sys.version_info[2],
            ),
        }
        return self._promote_result_fields(stats, successful)

    def get_raw_results(self):
        """Get all raw results."""
        return self.results

    def save_results(self, output_dir=None):
        """Save results to file."""
        if output_dir is None:
            output_dir = settings.RAW_RESULTS_DIR
        stats = self.get_statistics()
        filename_base = self.name
        if self.name.endswith('_OS'):
            filename_base = self.name[:-3]
            suffix = 'os'
        elif str(self.category).endswith('_os'):
            suffix = 'os'
        else:
            suffix = "py{}".format(sys.version_info[0])
        filename = "{}_{}.json".format(filename_base, suffix)
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w') as f:
            json.dump({
                'statistics': stats,
                'raw_results': self.results,
                'warmup_results': self.warmup_results,
            }, f, indent=2)
        print("\nResults saved to: {}".format(filepath))
        return filepath


class BenchmarkSuite(object):
    """Suite of multiple benchmarks."""

    def __init__(self, name="Benchmark Suite"):
        self.name = name
        self.benchmarks = []
        self.results = []

    def add(self, benchmark):
        """Add a benchmark to the suite."""
        self.benchmarks.append(benchmark)

    def run_all(self, num_runs=None, warmup_runs=None):
        """Run all benchmarks in the suite."""
        print("\n" + "=" * 70)
        print("Running Benchmark Suite: {}".format(self.name))
        print("Total benchmarks: {}".format(len(self.benchmarks)))
        print("=" * 70)
        self.results = []
        for i, benchmark in enumerate(self.benchmarks, 1):
            print("\n[{}/{}]".format(i, len(self.benchmarks)))
            stats = benchmark.run(num_runs, warmup_runs)
            self.results.append(stats)
            benchmark.save_results()
        print("\n" + "=" * 70)
        print("Benchmark Suite Complete")
        print("=" * 70)
        return self.results

    def get_summary(self):
        """Get summary of all results."""
        return {
            'suite_name': self.name,
            'total_benchmarks': len(self.benchmarks),
            'successful': len([r for r in self.results if r.get('success')]),
            'failed': len([r for r in self.results if not r.get('success')]),
            'results': self.results,
        }


if __name__ == '__main__':
    # Test base benchmark class
    class TestBenchmark(BaseBenchmark):
        def run_single(self):
            time.sleep(0.1)
            return {'operation': 'test'}

    test = TestBenchmark("TestBenchmark", "test")
    stats = test.run(num_runs=3, warmup_runs=1)
    print("\nStatistics:")
    for key, value in stats.items():
        print(" {}: {}".format(key, value))
