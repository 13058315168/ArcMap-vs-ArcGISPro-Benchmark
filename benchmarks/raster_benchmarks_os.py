# -*- coding: utf-8 -*-
"""
Raster data benchmarks using open-source libraries
Compatible with Python 3.x only
Uses Rasterio and NumPy
"""
from __future__ import print_function, division, absolute_import
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import open-source libraries
try:
    import rasterio
    from rasterio.transform import from_bounds
    from rasterio.windows import Window
    from rasterio.warp import reproject, Resampling
    from rasterio.mask import mask
    from rasterio import features
    HAS_OS_LIBS = True
except ImportError:
    HAS_OS_LIBS = False

from config import settings
from benchmarks.base_benchmark import BaseBenchmark
from utils.benchmark_inputs import (
    get_analysis_boundary_extent,
    get_analysis_crs,
    get_analysis_raster_path,
    get_benchmark_gdb_path,
)
from utils.benchmark_shapes import derive_block_size
from utils.raster_utils import expected_clip_dimension


def _constant_raster_bounds(size):
    """Return the synthetic local bounds used by raster benchmarks."""
    size = int(size)
    return 0.0, 0.0, float(size), float(size)


def _analysis_extent(size):
    """Return a projected square extent for fallback analysis rasters."""
    extent = get_analysis_boundary_extent(settings.DATA_DIR)
    if extent:
        return extent
    half = float(size) / 2.0
    return (-half, -half, half, half)


def _create_analysis_raster_fallback(output_path, raster_size):
    """Create a patterned analysis raster when the generated input is missing."""
    extent = _analysis_extent(raster_size)
    transform = from_bounds(extent[0], extent[1], extent[2], extent[3], raster_size, raster_size)
    row_idx = np.arange(raster_size, dtype=np.int32).reshape(-1, 1)
    col_idx = np.arange(raster_size, dtype=np.int32).reshape(1, -1)
    block_size = derive_block_size(int(raster_size), target_blocks_per_side=60, min_block_size=8)
    data = (((row_idx // max(1, block_size)) + (col_idx // max(1, block_size))) % 8 + 1).astype(np.uint8)
    profile = {
        'driver': 'GTiff',
        'height': raster_size,
        'width': raster_size,
        'count': 1,
        'dtype': data.dtype,
        'crs': 'EPSG:{}'.format(get_analysis_crs(settings.DATA_DIR)),
        'transform': transform,
        'compress': 'lzw'
    }
    with rasterio.open(output_path, 'w', **profile) as dst:
        dst.write(data, 1)
    return output_path


def _run_repeated_operation(repeat_count, cleanup_fn, operation_fn):
    """Run the same logical benchmark operation multiple times."""
    repeat_count = max(1, int(repeat_count or 1))
    result = None
    for _ in range(repeat_count):
        if cleanup_fn is not None:
            cleanup_fn()
        result = operation_fn()
    return result


def _heavy_raster_profile(height, width, transform, crs):
    """Return a heavier write profile for the national_heavy tier."""
    if settings.DATA_SCALE == 'national_heavy':
        return {
            'driver': 'GTiff',
            'height': height,
            'width': width,
            'count': 1,
            'dtype': np.float32,
            'crs': crs,
            'transform': transform,
            'compress': None
        }
    return {
        'driver': 'GTiff',
        'height': height,
        'width': width,
        'count': 1,
        'dtype': np.uint8,
        'crs': crs,
        'transform': transform,
        'compress': 'lzw'
    }


def _validated_raster_result(array, expected_width, expected_height, metric_name, expected_min=None, expected_max=None):
    """Validate array dimensions and optional value range."""
    actual_height = int(array.shape[0])
    actual_width = int(array.shape[1])

    if actual_width != int(expected_width) or actual_height != int(expected_height):
        raise RuntimeError(
            "{} 鏍￠獙澶辫触: 鏈熸湜 {}x{}锛屽疄闄?{}x{}".format(
                metric_name, int(expected_width), int(expected_height), actual_width, actual_height
            )
        )

    observed_value = "{}x{}".format(actual_width, actual_height)
    expected_value = "{}x{}".format(int(expected_width), int(expected_height))

    if expected_min is not None or expected_max is not None:
        min_value = float(np.min(array))
        max_value = float(np.max(array))
        if expected_min is not None and abs(min_value - float(expected_min)) > 1e-6:
            raise RuntimeError(
                "{} 鏍￠獙澶辫触: MINIMUM 鏈熸湜 {}锛屽疄闄?{}".format(metric_name, float(expected_min), min_value)
            )
        if expected_max is not None and abs(max_value - float(expected_max)) > 1e-6:
            raise RuntimeError(
                "{} 鏍￠獙澶辫触: MAXIMUM 鏈熸湜 {}锛屽疄闄?{}".format(metric_name, float(expected_max), max_value)
            )
        expected_value = "{}; value={}..{}".format(expected_value, expected_min, expected_max)
        observed_value = "{}; value={:.1f}..{:.1f}".format(observed_value, min_value, max_value)

    return {
        'output_width': actual_width,
        'output_height': actual_height,
        'validation_metric': metric_name,
        'validation_expected': expected_value,
        'validation_observed': observed_value,
        'validation_passed': True,
    }


class RasterBenchmarksOS(object):
    """Collection of raster data benchmarks using open-source libraries"""
    
    @staticmethod
    def get_all_benchmarks():
        """Get all open-source raster benchmark instances"""
        if not HAS_OS_LIBS:
            return []
        return [
            R1_CreateConstantRaster_OS(),
            R2_Resample_OS(),
            R3_Clip_OS(),
            R4_RasterCalculator_OS(),
        ]


class R1_CreateConstantRaster_OS(BaseBenchmark):
    """Benchmark: Create Constant Raster using Rasterio"""
    
    def __init__(self, output_format='GPKG'):
        super(R1_CreateConstantRaster_OS, self).__init__("R1_CreateConstantRaster_OS", "raster_os")
        cfg = settings.get_raster_config_for_test('R1')
        self.size = cfg['constant_raster_size']
        self.output_path = None
        self.output_format = output_format
        self.repeat_count = settings.get_workload_repeat_for_test('R1')
    
    def setup(self):
        if self.output_format == 'GDB':
            self.output_path = os.path.join(settings.DATA_DIR, "staging", "R1_constant_raster_os.tif")
        else:
            self.output_path = os.path.join(settings.DATA_DIR, "R1_constant_raster_os.tif")
        output_dir = os.path.dirname(self.output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    def teardown(self):
        if self.output_path and os.path.exists(self.output_path):
            try:
                os.remove(self.output_path)
            except:
                pass
    
    def run_single(self):
        def _cleanup():
            if self.output_path and os.path.exists(self.output_path):
                try:
                    os.remove(self.output_path)
                except:
                    pass

        def _run_once():
            height = self.size
            width = self.size

            bounds = _constant_raster_bounds(self.size)
            transform = from_bounds(bounds[0], bounds[1], bounds[2], bounds[3], width, height)
            data = np.ones((height, width), dtype=np.float32 if settings.DATA_SCALE == 'national_heavy' else np.uint8)
            profile = _heavy_raster_profile(height, width, transform, 'EPSG:4326')
            with rasterio.open(self.output_path, 'w', **profile) as dst:
                dst.write(data, 1)

            return _validated_raster_result(
                data,
                width,
                height,
                "constant_raster_dimensions",
                expected_min=1,
                expected_max=1
            )

        return _run_repeated_operation(self.repeat_count, _cleanup, _run_once)


class R2_Resample_OS(BaseBenchmark):
    """Benchmark: Raster Resample using Rasterio"""

    def __init__(self, output_format='GPKG'):
        super(R2_Resample_OS, self).__init__("R2_Resample_OS", "raster_os")
        self.output_format = output_format
        cfg = settings.get_raster_config_for_test('R2')
        self.source_size = cfg.get('resample_source_size', cfg.get('analysis_raster_size'))
        self.target_size = cfg.get('resample_target_size', cfg.get('analysis_raster_target_size'))
        self.input_path = None
        self.output_path = None
        self.repeat_count = settings.get_workload_repeat_for_test('R2')
    
    def setup(self):
        # Use a dedicated source raster so standard can tune R2 without affecting other tests.
        self.input_path = os.path.join(settings.DATA_DIR, "staging", "R2_resample_source_os.tif")
        if self.output_format == 'GDB':
            self.output_path = os.path.join(settings.DATA_DIR, "staging", "R2_resample_output_os.tif")
        else:
            self.output_path = os.path.join(settings.DATA_DIR, "R2_resample_output_os.tif")
        for path in (self.input_path, self.output_path):
            output_dir = os.path.dirname(path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)
        
        if not os.path.exists(self.input_path):
            _create_analysis_raster_fallback(self.input_path, self.source_size)
    
    def teardown(self):
        if self.output_path and os.path.exists(self.output_path):
            try:
                os.remove(self.output_path)
            except:
                pass
    
    def run_single(self):
        def _cleanup():
            if self.output_path and os.path.exists(self.output_path):
                try:
                    os.remove(self.output_path)
                except:
                    pass

        def _run_once():
            with rasterio.open(self.input_path) as src:
                data = src.read(1).astype(np.float32 if settings.DATA_SCALE == 'national_heavy' else src.dtypes[0])
                src_crs = src.crs
                src_transform = src.transform
                dst_transform = from_bounds(src.bounds[0], src.bounds[1], src.bounds[2], src.bounds[3], self.target_size, self.target_size)
                dst_data = np.empty((self.target_size, self.target_size), dtype=data.dtype)

                reproject(
                    source=data,
                    destination=dst_data,
                    src_transform=src_transform,
                    src_crs=src_crs,
                    dst_transform=dst_transform,
                    dst_crs=src_crs,
                    resampling=Resampling.nearest
                )

            profile = {
                'driver': 'GTiff',
                'height': self.target_size,
                'width': self.target_size,
                'count': 1,
                'dtype': dst_data.dtype,
                'crs': src_crs,
                'transform': dst_transform,
                'compress': None if settings.DATA_SCALE == 'national_heavy' else 'lzw'
            }

            with rasterio.open(self.output_path, 'w', **profile) as dst:
                dst.write(dst_data, 1)

            input_min = float(np.min(data))
            input_max = float(np.max(data))

            return _validated_raster_result(
                dst_data,
                self.target_size,
                self.target_size,
                "resample_raster_dimensions",
                expected_min=input_min,
                expected_max=input_max
            )

        return _run_repeated_operation(self.repeat_count, _cleanup, _run_once)


class R3_Clip_OS(BaseBenchmark):
    """Benchmark: Raster Clip using Rasterio"""

    def __init__(self, output_format='GPKG'):
        super(R3_Clip_OS, self).__init__("R3_Clip_OS", "raster_os")
        self.output_format = output_format
        cfg = settings.get_raster_config_for_test('R3')
        self.clip_ratio = cfg.get('analysis_raster_clip_ratio', cfg.get('clip_ratio'))
        self.input_path = None
        self.output_path = None
        self.repeat_count = settings.get_workload_repeat_for_test('R3')
    
    def setup(self):
        # Use a dedicated source raster so standard can tune R3 without affecting other tests.
        self.input_path = get_analysis_raster_path(settings.DATA_DIR, prefer_staging=True)
        if self.output_format == 'GDB':
            self.output_path = os.path.join(settings.DATA_DIR, "staging", "R3_clip_output_os.tif")
        else:
            self.output_path = os.path.join(settings.DATA_DIR, "R3_clip_output_os.tif")
        output_dir = os.path.dirname(self.output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        if not os.path.exists(self.input_path):
            cfg = settings.get_raster_config_for_test('R3')
            _create_analysis_raster_fallback(self.input_path, cfg.get('analysis_raster_size', settings.RASTER_CONFIG.get('analysis_raster_size')))
    
    def teardown(self):
        if self.output_path and os.path.exists(self.output_path):
            try:
                os.remove(self.output_path)
            except:
                pass
    
    def run_single(self):
        def _cleanup():
            if self.output_path and os.path.exists(self.output_path):
                try:
                    os.remove(self.output_path)
                except:
                    pass

        def _run_once():
            with rasterio.open(self.input_path) as src:
                input_width = int(src.width)
                input_height = int(src.height)
                src_data = src.read(1)
                if settings.DATA_SCALE == 'national_heavy':
                    src_data = src_data.astype(np.float32)
                input_min = float(np.min(src_data))
                input_max = float(np.max(src_data))
                expected_size = expected_clip_dimension(input_width, self.clip_ratio)
                start_x = max(0, int(round((input_width - expected_size) / 2.0)))
                start_y = max(0, int(round((input_height - expected_size) / 2.0)))
                window = Window(start_x, start_y, expected_size, expected_size)
                out_image = src.read(1, window=window)
                if settings.DATA_SCALE == 'national_heavy':
                    out_image = out_image.astype(np.float32)
                out_transform = src.window_transform(window)
                out_meta = src.meta.copy()

                out_meta.pop('nodata', None)
                out_meta.update({
                    'driver': 'GTiff',
                    'height': out_image.shape[0],
                    'width': out_image.shape[1],
                    'transform': out_transform,
                    'compress': None if settings.DATA_SCALE == 'national_heavy' else 'lzw'
                })

            with rasterio.open(self.output_path, 'w', **out_meta) as dst:
                dst.write(out_image, 1)

            clipped = out_image
            return _validated_raster_result(
                clipped,
                expected_size,
                expected_size,
                "clip_raster_dimensions",
                expected_min=input_min,
                expected_max=input_max
            )

        return _run_repeated_operation(self.repeat_count, _cleanup, _run_once)


class R4_RasterCalculator_OS(BaseBenchmark):
    """Benchmark: Raster Calculator using Rasterio/NumPy"""
    
    def __init__(self):
        super(R4_RasterCalculator_OS, self).__init__("R4_RasterCalculator_OS", "raster_os")
        self.output_format = 'GPKG'
        self.input_path = None
        self.output_path = None
        self.repeat_count = settings.get_workload_repeat_for_test('R4')
    
    def setup(self):
        # Use a dedicated source raster so standard can tune R4 without affecting other tests.
        self.input_path = get_analysis_raster_path(settings.DATA_DIR, prefer_staging=True)
        if self.output_format == 'GDB':
            self.output_path = os.path.join(settings.DATA_DIR, "staging", "R4_calc_output_os.tif")
        else:
            self.output_path = os.path.join(settings.DATA_DIR, "R4_calc_output_os.tif")
        output_dir = os.path.dirname(self.output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        if not os.path.exists(self.input_path):
            cfg = settings.get_raster_config_for_test('R4')
            _create_analysis_raster_fallback(self.input_path, cfg.get('analysis_raster_size', settings.RASTER_CONFIG.get('analysis_raster_size')))
    
    def teardown(self):
        if self.output_path and os.path.exists(self.output_path):
            try:
                os.remove(self.output_path)
            except:
                pass
    
    def run_single(self):
        def _cleanup():
            if self.output_path and os.path.exists(self.output_path):
                try:
                    os.remove(self.output_path)
                except:
                    pass

        def _run_once():
            with rasterio.open(self.input_path) as src:
                data = src.read(1).astype(np.float32)
                meta = src.meta.copy()
                input_width = int(src.width)
                input_height = int(src.height)
                input_min = float(np.min(data))
                input_max = float(np.max(data))

                result = (data * 2).astype(np.float32 if settings.DATA_SCALE == 'national_heavy' else np.uint8)

                meta.pop('nodata', None)
                meta.update({
                    'dtype': result.dtype,
                    'compress': None if settings.DATA_SCALE == 'national_heavy' else 'lzw'
                })

            with rasterio.open(self.output_path, 'w', **meta) as dst:
                dst.write(result, 1)

            return _validated_raster_result(
                result,
                input_width,
                input_height,
                "raster_calculator_dimensions",
                expected_min=input_min * 2.0,
                expected_max=input_max * 2.0
            )

        return _run_repeated_operation(self.repeat_count, _cleanup, _run_once)


if __name__ == '__main__':
    if not HAS_OS_LIBS:
        print("Open-source libraries not available. Please install:")
        print("  pip install rasterio numpy")
        sys.exit(1)
    
    print("Testing open-source raster benchmarks...")
    benchmarks = RasterBenchmarksOS.get_all_benchmarks()
    for bm in benchmarks:
        print("\nTest: {}".format(bm.name))
        try:
            stats = bm.run(num_runs=1, warmup_runs=0)
            print("  Success: {}".format(stats.get('success')))
            print("  Mean time: {:.4f}s".format(stats.get('mean_time', 0)))
        except Exception as e:
            print("  Error: {}".format(str(e)))
