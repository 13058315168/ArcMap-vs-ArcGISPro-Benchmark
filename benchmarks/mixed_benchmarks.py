# -*- coding: utf-8 -*-
"""
Mixed (vector-raster) benchmarks
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
from utils.raster_utils import create_constant_raster, spatial_analyst_available


def _get_raster_min_max(raster_path):
    """Return raster min/max values as floats."""
    min_value = float(arcpy.GetRasterProperties_management(raster_path, "MINIMUM")[0])
    max_value = float(arcpy.GetRasterProperties_management(raster_path, "MAXIMUM")[0])
    return min_value, max_value


class MixedBenchmarks(object):
    """Collection of mixed vector-raster benchmarks"""

    @staticmethod
    def get_all_benchmarks():
        """Get all mixed benchmark instances"""
        if not HAS_ARCPY:
            return []
        return [
            M1_PolygonToRaster(),
            M2_RasterToPoint(),
        ]


class M1_PolygonToRaster(BaseBenchmark):
    """Benchmark: Polygon to Raster Conversion"""
    
    def __init__(self):
        super(M1_PolygonToRaster, self).__init__("M1_PolygonToRaster", "mixed")
        self.input_fc = None
        self.output_raster = None
        self.cell_size = None
    
    def setup(self):
        arcpy.env.workspace = settings.DATA_DIR
        arcpy.env.overwriteOutput = True
        
        gdb_path = os.path.join(settings.DATA_DIR, settings.DEFAULT_GDB_NAME)
        self.input_fc = os.path.join(gdb_path, "test_polygons_a")
        # Use version-specific output to avoid lock conflicts between Py2/Py3
        py_version = "py2" if sys.version_info[0] < 3 else "py3"
        self.output_raster = os.path.join(settings.DATA_DIR, "M1_poly_to_ras_{}.tif".format(py_version))
        
        # Calculate cell size based on data extent
        raster_size = settings.RASTER_CONFIG['constant_raster_size']
        self.cell_size = 360.0 / raster_size
    
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

        input_desc = arcpy.Describe(self.input_fc)
        input_extent = input_desc.extent
        input_width = float(input_extent.XMax) - float(input_extent.XMin)
        input_height = float(input_extent.YMax) - float(input_extent.YMin)
        raster_size = int(settings.RASTER_CONFIG['constant_raster_size'])
        self.cell_size = max(input_width, input_height) / float(raster_size)
        expected_width = int(round(input_width / self.cell_size))
        expected_height = int(round(input_height / self.cell_size))
        
        # Polygon to raster conversion
        arcpy.PolygonToRaster_conversion(
            in_features=self.input_fc,
            value_field="poly_id",
            out_rasterdataset=self.output_raster,
            cell_assignment="CELL_CENTER",
            priority_field="NONE",
            cellsize=self.cell_size
        )

        desc = arcpy.Describe(self.output_raster)
        output_width = int(desc.width)
        output_height = int(desc.height)
        if output_width != expected_width or output_height != expected_height:
            raise RuntimeError(
                "M1_PolygonToRaster 鏍￠獙澶辫触: 鏈熸湜 {}x{}锛屽疄闄?{}x{}".format(
                    expected_width, expected_height, output_width, output_height
                )
            )

        _, max_value = _get_raster_min_max(self.output_raster)
        if max_value <= 0:
            raise RuntimeError("M1_PolygonToRaster 鏍￠獙澶辫触: 杈撳嚭鏍呮牸涓虹┖鎴栧叏閮?0")

        return {
            'output_width': output_width,
            'output_height': output_height,
            'cell_size': desc.meanCellWidth,
            'validation_metric': 'polygon_to_raster_dimensions',
            'validation_expected': "{}x{}; max>0".format(expected_width, expected_height),
            'validation_observed': "{}x{}; max={:.1f}".format(output_width, output_height, max_value),
            'validation_passed': True,
        }


class M2_RasterToPoint(BaseBenchmark):
    """Benchmark: Raster to Point Conversion"""
    
    def __init__(self):
        super(M2_RasterToPoint, self).__init__("M2_RasterToPoint", "mixed")
        self.input_raster = None
        self.output_fc = None
    
    def setup(self):
        arcpy.env.workspace = settings.DATA_DIR
        arcpy.env.overwriteOutput = True
        
        # Use file-based raster instead of GDB raster
        self.input_raster = os.path.join(settings.DATA_DIR, "constant_raster.tif")
        self.output_fc = os.path.join(settings.DATA_DIR, "M2_ras_to_point.shp")

        # Keep this benchmark runnable without generating the full vector dataset.
        expected_size = int(settings.RASTER_CONFIG['constant_raster_size'])
        needs_regen = True
        if arcpy.Exists(self.input_raster):
            try:
                desc = arcpy.Describe(self.input_raster)
                if int(getattr(desc, 'width', 0) or 0) == expected_size and int(getattr(desc, 'height', 0) or 0) == expected_size:
                    needs_regen = False
            except Exception:
                needs_regen = True

        if needs_regen:
            raster_size = int(settings.RASTER_CONFIG['constant_raster_size'])
            extent = "0 0 {0} {0}".format(raster_size)
            sr = arcpy.SpatialReference(settings.SPATIAL_REFERENCE)
            create_constant_raster(
                self.input_raster,
                cell_size=1,
                extent=extent,
                value=1,
                spatial_reference=sr,
                use_spatial_analyst=spatial_analyst_available()
            )

    def _get_input_raster_stats(self):
        """Return input raster dimensions and the expected output count."""
        desc = arcpy.Describe(self.input_raster)
        input_width = int(getattr(desc, 'width', 0) or 0)
        input_height = int(getattr(desc, 'height', 0) or 0)

        if input_width <= 0 or input_height <= 0:
            raise RuntimeError(
                "M2_RasterToPoint 无法读取输入栅格尺寸: {}".format(self.input_raster)
            )

        expected_size = int(settings.RASTER_CONFIG['constant_raster_size'])
        if input_width != expected_size or input_height != expected_size:
            raise RuntimeError(
                "M2_RasterToPoint 输入栅格尺寸不符合当前规模: 实际 {}x{}, 期望 {}x{}".format(
                    input_width, input_height, expected_size, expected_size
                )
            )

        expected_features = input_width * input_height
        return input_width, input_height, expected_features
    
    def teardown(self):
        if self.output_fc and arcpy.Exists(self.output_fc):
            try:
                arcpy.Delete_management(self.output_fc)
            except Exception:
                pass
    
    def run_single(self):
        # Delete if exists
        if arcpy.Exists(self.output_fc):
            arcpy.Delete_management(self.output_fc)

        input_width, input_height, expected_features = self._get_input_raster_stats()
        
        # Raster to point conversion. This should emit one point per valid raster cell.
        arcpy.RasterToPoint_conversion(
            in_raster=self.input_raster,
            out_point_features=self.output_fc,
            raster_field="Value"
        )
        
        count = int(arcpy.GetCount_management(self.output_fc)[0])
        if count != expected_features:
            raise RuntimeError(
                "M2_RasterToPoint 输出数量校验失败: 输入 {}x{} 期望 {} 个点, 实际 {} 个点".format(
                    input_width,
                    input_height,
                    expected_features,
                    count
                )
            )

        return {
            'features_created': count,
            'expected_features': expected_features,
            'input_width': input_width,
            'input_height': input_height,
            'validation_metric': 'raster_to_point_feature_count',
            'validation_expected': expected_features,
            'validation_observed': count,
            'validation_passed': True,
        }


if __name__ == '__main__':
    # Test individual benchmarks
    print("Testing Mixed Benchmarks...")
    
    benchmarks = MixedBenchmarks.get_all_benchmarks()
    for bm in benchmarks:
        print("\nTest: {}".format(bm.name))
        try:
            stats = bm.run(num_runs=1, warmup_runs=0)
            print("  Success: {}".format(stats.get('success')))
            print("  Mean time: {:.4f}s".format(stats.get('mean_time', 0)))
        except Exception as e:
            print("  Error: {}".format(str(e)))
