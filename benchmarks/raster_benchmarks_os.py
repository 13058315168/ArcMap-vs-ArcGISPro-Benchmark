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
    from rasterio.warp import reproject, Resampling
    from rasterio.mask import mask
    from rasterio import features
    HAS_OS_LIBS = True
except ImportError:
    HAS_OS_LIBS = False

from config import settings
from benchmarks.base_benchmark import BaseBenchmark


def _constant_raster_bounds(size):
    """Return the synthetic local bounds used by raster benchmarks."""
    size = int(size)
    return 0.0, 0.0, float(size), float(size)


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
    
    def __init__(self):
        super(R1_CreateConstantRaster_OS, self).__init__("R1_CreateConstantRaster_OS", "raster_os")
        self.size = settings.RASTER_CONFIG['constant_raster_size']
        self.output_path = None
    
    def setup(self):
        self.output_path = os.path.join(settings.DATA_DIR, "R1_constant_raster_os.tif")
    
    def teardown(self):
        if self.output_path and os.path.exists(self.output_path):
            try:
                os.remove(self.output_path)
            except:
                pass
    
    def run_single(self):
        # Create constant raster using NumPy and Rasterio
        height = self.size
        width = self.size
        
        # Create transform (georeferencing)
        transform = from_bounds(*_constant_raster_bounds(self.size), width, height)
        
        # Create constant data
        data = np.ones((height, width), dtype=np.uint8)
        
        # Write to GeoTIFF
        profile = {
            'driver': 'GTiff',
            'height': height,
            'width': width,
            'count': 1,
            'dtype': data.dtype,
            'crs': 'EPSG:4326',
            'transform': transform,
            'compress': 'lzw'
        }
        
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


class R2_Resample_OS(BaseBenchmark):
    """Benchmark: Raster Resample using Rasterio"""
    
    def __init__(self):
        super(R2_Resample_OS, self).__init__("R2_Resample_OS", "raster_os")
        self.source_size = settings.RASTER_CONFIG['resample_source_size']
        self.target_size = settings.RASTER_CONFIG['resample_target_size']
        self.input_path = None
        self.output_path = None
    
    def setup(self):
        self.input_path = os.path.join(settings.DATA_DIR, "constant_raster.tif")
        self.output_path = os.path.join(settings.DATA_DIR, "R2_resample_output_os.tif")
        
        # Create input if not exists (don't teardown - keep for other tests)
        if not os.path.exists(self.input_path):
            r1 = R1_CreateConstantRaster_OS()
            r1.setup()
            r1.run_single()  # Keep the file, don't call teardown()
            self.input_path = r1.output_path
    
    def teardown(self):
        if self.output_path and os.path.exists(self.output_path):
            try:
                os.remove(self.output_path)
            except:
                pass
    
    def run_single(self):
        # Read input raster
        with rasterio.open(self.input_path) as src:
            data = src.read(1)
            src_crs = src.crs
            src_transform = src.transform
            
            # Calculate new transform
            dst_transform = from_bounds(*src.bounds, self.target_size, self.target_size)
            
            # Create output array
            dst_data = np.empty((self.target_size, self.target_size), dtype=data.dtype)
            
            # Reproject/resample
            reproject(
                source=data,
                destination=dst_data,
                src_transform=src_transform,
                src_crs=src_crs,
                dst_transform=dst_transform,
                dst_crs=src_crs,
                resampling=Resampling.nearest
            )
        
        # Write output
        profile = {
            'driver': 'GTiff',
            'height': self.target_size,
            'width': self.target_size,
            'count': 1,
            'dtype': dst_data.dtype,
            'crs': src_crs,
            'transform': dst_transform,
            'compress': 'lzw'
        }
        
        with rasterio.open(self.output_path, 'w', **profile) as dst:
            dst.write(dst_data, 1)
        
        return _validated_raster_result(
            dst_data,
            self.target_size,
            self.target_size,
            "resample_raster_dimensions",
            expected_min=1,
            expected_max=1
        )


class R3_Clip_OS(BaseBenchmark):
    """Benchmark: Raster Clip using Rasterio"""
    
    def __init__(self):
        super(R3_Clip_OS, self).__init__("R3_Clip_OS", "raster_os")
        self.clip_ratio = settings.RASTER_CONFIG['clip_ratio']
        self.input_path = None
        self.output_path = None
    
    def setup(self):
        self.input_path = os.path.join(settings.DATA_DIR, "constant_raster.tif")
        self.output_path = os.path.join(settings.DATA_DIR, "R3_clip_output_os.tif")
        
        # Create input if not exists (don't teardown - keep for other tests)
        if not os.path.exists(self.input_path):
            r1 = R1_CreateConstantRaster_OS()
            r1.setup()
            r1.run_single()  # Keep the file, don't call teardown()
            self.input_path = r1.output_path
    
    def teardown(self):
        if self.output_path and os.path.exists(self.output_path):
            try:
                os.remove(self.output_path)
            except:
                pass
    
    def run_single(self):
        # Clip raster
        with rasterio.open(self.input_path) as src:
            input_width = int(src.width)
            x_min = src.bounds.left + (src.bounds.right - src.bounds.left) * (1.0 - self.clip_ratio) / 2.0
            y_min = src.bounds.bottom + (src.bounds.top - src.bounds.bottom) * (1.0 - self.clip_ratio) / 2.0
            x_max = src.bounds.right - (src.bounds.right - src.bounds.left) * (1.0 - self.clip_ratio) / 2.0
            y_max = src.bounds.top - (src.bounds.top - src.bounds.bottom) * (1.0 - self.clip_ratio) / 2.0
            from shapely.geometry import box
            clip_geom = box(x_min, y_min, x_max, y_max)
            out_image, out_transform = mask(src, [clip_geom], crop=True)
            out_meta = src.meta.copy()
            
            # Update metadata
            out_meta.update({
                'driver': 'GTiff',
                'height': out_image.shape[1],
                'width': out_image.shape[2],
                'transform': out_transform,
                'compress': 'lzw'
            })
        
        # Write output
        with rasterio.open(self.output_path, 'w', **out_meta) as dst:
            dst.write(out_image)
        
        clipped = out_image[0]
        expected_size = int(round(input_width * self.clip_ratio))
        return _validated_raster_result(
            clipped,
            expected_size,
            expected_size,
            "clip_raster_dimensions",
            expected_min=1,
            expected_max=1
        )


class R4_RasterCalculator_OS(BaseBenchmark):
    """Benchmark: Raster Calculator using Rasterio/NumPy"""
    
    def __init__(self):
        super(R4_RasterCalculator_OS, self).__init__("R4_RasterCalculator_OS", "raster_os")
        self.input_path = None
        self.output_path = None
    
    def setup(self):
        self.input_path = os.path.join(settings.DATA_DIR, "constant_raster.tif")
        self.output_path = os.path.join(settings.DATA_DIR, "R4_calc_output_os.tif")
        
        # Create input if not exists (don't teardown - keep for other tests)
        if not os.path.exists(self.input_path):
            r1 = R1_CreateConstantRaster_OS()
            r1.setup()
            r1.run_single()  # Keep the file, don't call teardown()
            self.input_path = r1.output_path
    
    def teardown(self):
        if self.output_path and os.path.exists(self.output_path):
            try:
                os.remove(self.output_path)
            except:
                pass
    
    def run_single(self):
        # Read input
        with rasterio.open(self.input_path) as src:
            data = src.read(1).astype(np.float32)
            meta = src.meta.copy()
            input_width = int(src.width)
            input_height = int(src.height)
            
            # Perform calculation: Int(raster * 2)
            result = (data * 2).astype(np.uint8)
            
            # Update metadata
            meta.update({
                'dtype': result.dtype,
                'compress': 'lzw'
            })
        
        # Write output
        with rasterio.open(self.output_path, 'w', **meta) as dst:
            dst.write(result, 1)
        
        return _validated_raster_result(
            result,
            input_width,
            input_height,
            "raster_calculator_dimensions",
            expected_min=2,
            expected_max=2
        )


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
