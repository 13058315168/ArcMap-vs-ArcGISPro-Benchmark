# -*- coding: utf-8 -*-
"""
Raster data benchmarks
Compatible with Python 2.7 and 3.x
"""
from __future__ import print_function, division, absolute_import
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import arcpy
    from arcpy.sa import *
    HAS_ARCPY = True
except ImportError:
    HAS_ARCPY = False
    arcpy = None

from config import settings
from benchmarks.base_benchmark import BaseBenchmark
from utils.raster_utils import create_constant_raster, double_raster, spatial_analyst_available


def _constant_raster_extent(size):
    """Return the synthetic local extent used by raster benchmarks."""
    size = int(size)
    return "0 0 {0} {0}".format(size)


def _get_raster_min_max(raster_path):
    """Return raster min/max values as floats."""
    min_value = float(arcpy.GetRasterProperties_management(raster_path, "MINIMUM")[0])
    max_value = float(arcpy.GetRasterProperties_management(raster_path, "MAXIMUM")[0])
    return min_value, max_value


def _validated_raster_result(raster_path, expected_width, expected_height, metric_name, expected_min=None, expected_max=None):
    """Validate raster dimensions and optional value range."""
    desc = arcpy.Describe(raster_path)
    actual_width = int(desc.width)
    actual_height = int(desc.height)

    if actual_width != int(expected_width) or actual_height != int(expected_height):
        raise RuntimeError(
            "{} 鏍￠獙澶辫触: 鏈熸湜 {}x{}锛屽疄闄?{}x{}".format(
                metric_name, int(expected_width), int(expected_height), actual_width, actual_height
            )
        )

    observed_value = "{}x{}".format(actual_width, actual_height)
    expected_value = "{}x{}".format(int(expected_width), int(expected_height))

    if expected_min is not None or expected_max is not None:
        min_value, max_value = _get_raster_min_max(raster_path)
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


class RasterBenchmarks(object):
    """Collection of raster data benchmarks"""

    @staticmethod
    def get_all_benchmarks():
        """Get all raster benchmark instances"""
        if not HAS_ARCPY:
            return []
        return [
            R1_CreateConstantRaster(),
            R2_Resample(),
            R3_Clip(),
            R4_RasterCalculator(),
        ]


class R1_CreateConstantRaster(BaseBenchmark):
    """Benchmark: Create Constant Raster"""
    
    def __init__(self):
        super(R1_CreateConstantRaster, self).__init__("R1_CreateConstantRaster", "raster")
        self.size = settings.RASTER_CONFIG['constant_raster_size']
        self.output_raster = None
    
    def setup(self):
        arcpy.env.workspace = settings.DATA_DIR
        arcpy.env.overwriteOutput = True
        
        self.output_raster = os.path.join(
            settings.DATA_DIR,
            "R1_constant_raster.tif"
        )
    
    def teardown(self):
        if self.output_raster and arcpy.Exists(self.output_raster):
            try:
                arcpy.Delete_management(self.output_raster)
            except Exception:
                pass
    
    def run_single(self):
        # Delete if exists
        if arcpy.Exists(self.output_raster):
            arcpy.Delete_management(self.output_raster)
        
        cell_size = 1
        extent = _constant_raster_extent(self.size)
        sr = arcpy.SpatialReference(settings.SPATIAL_REFERENCE)
        create_constant_raster(
            self.output_raster,
            cell_size=cell_size,
            extent=extent,
            value=1,
            spatial_reference=sr,
            use_spatial_analyst=spatial_analyst_available()
        )

        return _validated_raster_result(
            self.output_raster,
            self.size,
            self.size,
            "constant_raster_dimensions",
            expected_min=1,
            expected_max=1
        )


class R2_Resample(BaseBenchmark):
    """Benchmark: Raster Resample"""
    
    def __init__(self):
        super(R2_Resample, self).__init__("R2_Resample", "raster")
        self.source_size = settings.RASTER_CONFIG['resample_source_size']
        self.target_size = settings.RASTER_CONFIG['resample_target_size']
        self.input_raster = None
        self.output_raster = None
    
    def setup(self):
        arcpy.env.workspace = settings.DATA_DIR
        arcpy.env.overwriteOutput = True
        
        # Use file-based raster instead of GDB raster (GDB has issues with rasters)
        self.input_raster = os.path.join(settings.DATA_DIR, "constant_raster.tif")
        self.output_raster = os.path.join(settings.DATA_DIR, "R2_resample_output.tif")
        
        # Input raster should already exist from data generation
        # If not, create it with a license-safe fallback
        if not arcpy.Exists(self.input_raster):
            print("    Warning: input raster not found, creating fallback constant raster...")
            try:
                cell_size = 1
                extent = _constant_raster_extent(self.source_size)
                sr = arcpy.SpatialReference(settings.SPATIAL_REFERENCE)
                create_constant_raster(
                    self.input_raster,
                    cell_size=cell_size,
                    extent=extent,
                    value=1,
                    spatial_reference=sr,
                    use_spatial_analyst=spatial_analyst_available()
                )
            except Exception as e:
                # Python 2/3 compatible error printing
                try:
                    error_msg = str(e)
                except UnicodeEncodeError:
                    error_msg = unicode(e).encode('utf-8', errors='replace')
                print("    Error creating raster: {}".format(error_msg))
    
    def teardown(self):
        if self.output_raster and arcpy.Exists(self.output_raster):
            try:
                arcpy.Delete_management(self.output_raster)
            except Exception:
                pass
    
    def run_single(self):
        # Delete if exists
        if arcpy.Exists(self.output_raster):
            arcpy.Delete_management(self.output_raster)
        
        # Calculate new cell size
        new_cell_size = float(self.source_size) / float(self.target_size)
        
        # Resample
        arcpy.Resample_management(
            in_raster=self.input_raster,
            out_raster=self.output_raster,
            cell_size=new_cell_size,
            resampling_type="NEAREST"
        )
        
        result = _validated_raster_result(
            self.output_raster,
            self.target_size,
            self.target_size,
            "resample_raster_dimensions",
            expected_min=1,
            expected_max=1
        )
        result['cell_size'] = new_cell_size
        return result


class R3_Clip(BaseBenchmark):
    """Benchmark: Raster Clip"""
    
    def __init__(self):
        super(R3_Clip, self).__init__("R3_Clip", "raster")
        self.clip_ratio = settings.RASTER_CONFIG['clip_ratio']
        self.input_raster = None
        self.output_raster = None
        self.clip_extent = None
    
    def setup(self):
        arcpy.env.workspace = settings.DATA_DIR
        arcpy.env.overwriteOutput = True
        
        # Use file-based raster instead of GDB raster
        self.input_raster = os.path.join(settings.DATA_DIR, "constant_raster.tif")
        self.output_raster = os.path.join(settings.DATA_DIR, "R3_clip_output.tif")
        
        self.clip_extent = None
    
    def teardown(self):
        if self.output_raster and arcpy.Exists(self.output_raster):
            try:
                arcpy.Delete_management(self.output_raster)
            except Exception:
                pass
    
    def run_single(self):
        # Delete if exists
        if arcpy.Exists(self.output_raster):
            arcpy.Delete_management(self.output_raster)
        
        input_desc = arcpy.Describe(self.input_raster)
        input_width = int(input_desc.width)
        input_height = int(input_desc.height)
        extent = input_desc.extent
        x_range = float(extent.XMax) - float(extent.XMin)
        y_range = float(extent.YMax) - float(extent.YMin)
        clip_width = x_range * self.clip_ratio
        clip_height = y_range * self.clip_ratio
        x_min = float(extent.XMin) + (x_range - clip_width) / 2.0
        y_min = float(extent.YMin) + (y_range - clip_height) / 2.0
        x_max = x_min + clip_width
        y_max = y_min + clip_height
        self.clip_extent = "{} {} {} {}".format(x_min, y_min, x_max, y_max)

        # Clip raster
        arcpy.Clip_management(
            in_raster=self.input_raster,
            rectangle=self.clip_extent,
            out_raster=self.output_raster,
            nodata_value=None,
            clipping_geometry="NONE",
            maintain_clipping_extent="NO_MAINTAIN_EXTENT"
        )

        expected_width = int(round(input_width * self.clip_ratio))
        expected_height = int(round(input_height * self.clip_ratio))
        return _validated_raster_result(
            self.output_raster,
            expected_width,
            expected_height,
            "clip_raster_dimensions",
            expected_min=1,
            expected_max=1
        )


class R4_RasterCalculator(BaseBenchmark):
    """Benchmark: Raster Calculator"""
    
    def __init__(self):
        super(R4_RasterCalculator, self).__init__("R4_RasterCalculator", "raster")
        self.input_raster = None
        self.output_raster = None
    
    def setup(self):
        arcpy.env.workspace = settings.DATA_DIR
        arcpy.env.overwriteOutput = True
        
        # Use file-based raster instead of GDB raster
        self.input_raster = os.path.join(settings.DATA_DIR, "constant_raster.tif")
        self.output_raster = os.path.join(settings.DATA_DIR, "R4_calc_output.tif")
    
    def teardown(self):
        if self.output_raster and arcpy.Exists(self.output_raster):
            try:
                arcpy.Delete_management(self.output_raster)
            except Exception:
                pass
    
    def run_single(self):
        # Delete if exists
        if arcpy.Exists(self.output_raster):
            arcpy.Delete_management(self.output_raster)
        double_raster(self.input_raster, self.output_raster, use_spatial_analyst=spatial_analyst_available())

        input_desc = arcpy.Describe(self.input_raster)
        return _validated_raster_result(
            self.output_raster,
            int(input_desc.width),
            int(input_desc.height),
            "raster_calculator_dimensions",
            expected_min=2,
            expected_max=2
        )


if __name__ == '__main__':
    # Test individual benchmarks
    print("Testing Raster Benchmarks...")
    
    benchmarks = RasterBenchmarks.get_all_benchmarks()
    for bm in benchmarks:
        print("\nTest: {}".format(bm.name))
        try:
            stats = bm.run(num_runs=1, warmup_runs=0)
            print("  Success: {}".format(stats.get('success')))
            print("  Mean time: {:.4f}s".format(stats.get('mean_time', 0)))
        except Exception as e:
            # Python 2/3 compatible error printing
            try:
                error_msg = str(e)
            except UnicodeEncodeError:
                error_msg = unicode(e).encode('utf-8', errors='replace')
            print("  Error: {}".format(error_msg))
