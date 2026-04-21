# -*- coding: utf-8 -*-
"""
Vector data benchmarks using open-source libraries
Compatible with Python 3.x only
Uses GeoPandas, Shapely, and Pyogrio
"""
from __future__ import print_function, division, absolute_import
import sys
import os
import numpy as np
import tempfile
import shutil

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import open-source libraries
try:
    import geopandas as gpd
    from shapely.geometry import Polygon, Point, box
    from shapely.ops import unary_union
    import pyogrio
    HAS_OS_LIBS = True
except ImportError:
    HAS_OS_LIBS = False

from config import settings
from benchmarks.base_benchmark import BaseBenchmark
from utils.benchmark_inputs import (
    get_analysis_boundary_extent,
    get_analysis_crs,
    get_benchmark_gdb_path,
    get_input_feature_path_os,
)
from utils.benchmark_shapes import expected_offset_grid_intersections_from_counts
BUFFER_PROJECTED_CRS = "EPSG:3857"


def _analysis_extent(default_extent=(-500000.0, -500000.0, 500000.0, 500000.0)):
    """Return the projected benchmark extent used by the generated inputs."""
    extent = get_analysis_boundary_extent(settings.DATA_DIR)
    return extent or default_extent


def buffer_in_projected_crs(gdf, buffer_distance_meters, projected_crs=BUFFER_PROJECTED_CRS):
    """Buffer geometries in a projected CRS and return to the source CRS."""
    source_crs = gdf.crs
    if source_crs is None:
        raise RuntimeError("Input GeoDataFrame must define a CRS for buffer benchmarking")

    projected = gdf.to_crs(projected_crs)
    projected['geometry'] = projected.buffer(buffer_distance_meters)
    return projected.to_crs(source_crs)


def _validated_count_result(actual_count, expected_count, metric_name):
    """Return a validated benchmark payload for deterministic feature counts."""
    if int(actual_count) != int(expected_count):
        raise RuntimeError(
            "{} 鏍￠獙澶辫触: 鏈熸湜 {}锛屽疄闄?{}".format(metric_name, int(expected_count), int(actual_count))
        )

    return {
        'features_created': int(actual_count),
        'expected_features': int(expected_count),
        'validation_metric': metric_name,
        'validation_expected': int(expected_count),
        'validation_observed': int(actual_count),
        'validation_passed': True,
    }


def _run_repeated_operation(repeat_count, cleanup_fn, operation_fn):
    """Run the same logical benchmark operation multiple times."""
    repeat_count = max(1, int(repeat_count or 1))
    result = None
    for _ in range(repeat_count):
        if cleanup_fn is not None:
            cleanup_fn()
        result = operation_fn()
    return result


class VectorBenchmarksOS(object):
    """Collection of vector data benchmarks using open-source libraries"""
    
    @staticmethod
    def get_all_benchmarks():
        """Get all open-source vector benchmark instances"""
        if not HAS_OS_LIBS:
            return []
        return [
            V1_CreateFishnet_OS(),
            V2_CreateRandomPoints_OS(),
            V3_Buffer_OS(),
            V4_Intersect_OS(),
            V5_SpatialJoin_OS(),
            V6_CalculateField_OS(),
        ]


class V1_CreateFishnet_OS(BaseBenchmark):
    """Benchmark: Create Fishnet using GeoPandas"""
    
    def __init__(self, output_format='GPKG'):
        super(V1_CreateFishnet_OS, self).__init__("V1_CreateFishnet_OS", "vector_os")
        cfg = settings.get_vector_config_for_test('V1')
        self.rows = cfg['fishnet_rows']
        self.cols = cfg['fishnet_cols']
        self.repeat_count = settings.get_workload_repeat_for_test('V1')
        self.output_path = None
        self.extent = None
        self.crs = "EPSG:{}".format(get_analysis_crs(settings.DATA_DIR))
        self.output_format = output_format
    
    def setup(self):
        gdb_path = get_benchmark_gdb_path(settings.DATA_DIR)
        if self.output_format == 'GDB':
            self.output_path = os.path.join(gdb_path, "V1_fishnet_output_os")
        else:
            self.output_path = os.path.join(settings.DATA_DIR, "V1_fishnet_output_os.gpkg")
        self.extent = _analysis_extent()
    
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
            total_width = float(self.extent[2] - self.extent[0])
            total_height = float(self.extent[3] - self.extent[1])
            cell_width = total_width / self.cols
            cell_height = total_height / self.rows

            polygons = []
            for row in range(self.rows):
                for col in range(self.cols):
                    x_min = float(self.extent[0]) + col * cell_width
                    x_max = x_min + cell_width
                    y_max = float(self.extent[3]) - row * cell_height
                    y_min = y_max - cell_height

                    poly = box(x_min, y_min, x_max, y_max)
                    polygons.append(poly)

            gdf = gpd.GeoDataFrame(geometry=polygons, crs=self.crs)
            driver = "OpenFileGDB" if self.output_format == "GDB" else "GPKG"
            gdf.to_file(self.output_path, driver=driver)
            return _validated_count_result(len(polygons), self.rows * self.cols, "fishnet_feature_count")

        return _run_repeated_operation(self.repeat_count, _cleanup, _run_once)


class V2_CreateRandomPoints_OS(BaseBenchmark):
    """Benchmark: Create Random Points using GeoPandas"""
    
    def __init__(self, output_format='GPKG'):
        super(V2_CreateRandomPoints_OS, self).__init__("V2_CreateRandomPoints_OS", "vector_os")
        cfg = settings.get_vector_config_for_test('V2')
        self.num_points = cfg['random_points']
        self.repeat_count = settings.get_workload_repeat_for_test('V2')
        self.output_path = None
        self.extent = None
        self.crs = "EPSG:{}".format(get_analysis_crs(settings.DATA_DIR))
        self.output_format = output_format
    
    def setup(self):
        gdb_path = get_benchmark_gdb_path(settings.DATA_DIR)
        if self.output_format == 'GDB':
            self.output_path = os.path.join(gdb_path, "V2_random_points_os")
        else:
            self.output_path = os.path.join(settings.DATA_DIR, "V2_random_points_os.gpkg")
        self.extent = _analysis_extent()
    
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
            np.random.seed(42)  # For reproducibility
            x_coords = np.random.uniform(float(self.extent[0]), float(self.extent[2]), self.num_points)
            y_coords = np.random.uniform(float(self.extent[1]), float(self.extent[3]), self.num_points)

            points = [Point(x, y) for x, y in zip(x_coords, y_coords)]
            gdf = gpd.GeoDataFrame(geometry=points, crs=self.crs)

            driver = "OpenFileGDB" if self.output_format == "GDB" else "GPKG"
            gdf.to_file(self.output_path, driver=driver)
            return _validated_count_result(len(points), self.num_points, "random_point_count")

        return _run_repeated_operation(self.repeat_count, _cleanup, _run_once)


class V3_Buffer_OS(BaseBenchmark):
    """Benchmark: Buffer Analysis using GeoPandas"""

    def __init__(self, output_format='GPKG'):
        super(V3_Buffer_OS, self).__init__("V3_Buffer_OS", "vector_os")
        self.gdb_path = None
        self.input_layer = None
        self.output_path = None
        self.buffer_distance = 1000.0  # meters
        self.output_format = output_format
        self.repeat_count = settings.get_workload_repeat_for_test('V3')

    def setup(self):
        self.input_path, self.input_layer = get_input_feature_path_os("buffer_points", settings.DATA_DIR)
        gdb_path = get_benchmark_gdb_path(settings.DATA_DIR)
        if self.output_format == "GDB":
            self.output_path = os.path.join(gdb_path, "V3_buffer_output_os")
        else:
            ext = ".gpkg" if self.output_format == "GPKG" else ".shp"
            self.output_path = os.path.join(settings.DATA_DIR, "V3_buffer_output_os{}".format(ext))

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
            if self.input_layer:
                gdf = gpd.read_file(self.input_path, layer=self.input_layer)
            else:
                gdf = gpd.read_file(self.input_path)
            expected_count = len(gdf)

            gdf = buffer_in_projected_crs(gdf, self.buffer_distance)
            driver = "OpenFileGDB" if self.output_format == "GDB" else ("GPKG" if self.output_format == "GPKG" else "ESRI Shapefile")
            gdf.to_file(self.output_path, driver=driver)
            return _validated_count_result(len(gdf), expected_count, "buffer_feature_count")

        return _run_repeated_operation(self.repeat_count, _cleanup, _run_once)


class V4_Intersect_OS(BaseBenchmark):
    """Benchmark: Intersect Analysis using GeoPandas"""

    def __init__(self, output_format='GPKG'):
        super(V4_Intersect_OS, self).__init__("V4_Intersect_OS", "vector_os")
        self.gdb_path = None
        self.input_a_layer = None
        self.input_b_layer = None
        self.output_path = None
        self.output_format = output_format
        self.expected_features = None
        self.repeat_count = settings.get_workload_repeat_for_test('V4')

    def setup(self):
        self.input_a_path, self.input_a_layer = get_input_feature_path_os("test_polygons_a", settings.DATA_DIR)
        self.input_b_path, self.input_b_layer = get_input_feature_path_os("test_polygons_b", settings.DATA_DIR)
        gdb_path = get_benchmark_gdb_path(settings.DATA_DIR)
        if self.output_format == "GDB":
            self.output_path = os.path.join(gdb_path, "V4_intersect_output_os")
        else:
            ext = ".gpkg" if self.output_format == "GPKG" else ".shp"
            self.output_path = os.path.join(settings.DATA_DIR, "V4_intersect_output_os{}".format(ext))

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
            if self.input_a_layer:
                gdf_a = gpd.read_file(self.input_a_path, layer=self.input_a_layer)
            else:
                gdf_a = gpd.read_file(self.input_a_path)
            if self.input_b_layer:
                gdf_b = gpd.read_file(self.input_b_path, layer=self.input_b_layer)
            else:
                gdf_b = gpd.read_file(self.input_b_path)

            if self.expected_features is None:
                self.expected_features = expected_offset_grid_intersections_from_counts(len(gdf_a), len(gdf_b))

            result = gpd.overlay(gdf_a, gdf_b, how='intersection')
            driver = "OpenFileGDB" if self.output_format == "GDB" else ("GPKG" if self.output_format == "GPKG" else "ESRI Shapefile")
            result.to_file(self.output_path, driver=driver)
            return _validated_count_result(len(result), self.expected_features, "intersect_feature_count")

        return _run_repeated_operation(self.repeat_count, _cleanup, _run_once)


class V5_SpatialJoin_OS(BaseBenchmark):
    """Benchmark: Spatial Join using GeoPandas"""

    def __init__(self, output_format='GPKG'):
        super(V5_SpatialJoin_OS, self).__init__("V5_SpatialJoin_OS", "vector_os")
        self.gdb_path = None
        self.target_layer = None
        self.join_layer = None
        self.output_path = None
        self.output_format = output_format
        self.repeat_count = settings.get_workload_repeat_for_test('V5')

    def setup(self):
        self.target_path, self.target_layer = get_input_feature_path_os("spatial_join_points", settings.DATA_DIR)
        self.join_path, self.join_layer = get_input_feature_path_os("spatial_join_polygons", settings.DATA_DIR)
        gdb_path = get_benchmark_gdb_path(settings.DATA_DIR)
        if self.output_format == "GDB":
            self.output_path = os.path.join(gdb_path, "V5_spatial_join_output_os")
        else:
            ext = ".gpkg" if self.output_format == "GPKG" else ".shp"
            self.output_path = os.path.join(settings.DATA_DIR, "V5_spatial_join_output_os{}".format(ext))

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
            if self.target_layer:
                target = gpd.read_file(self.target_path, layer=self.target_layer)
            else:
                target = gpd.read_file(self.target_path)
            if self.join_layer:
                join = gpd.read_file(self.join_path, layer=self.join_layer)
            else:
                join = gpd.read_file(self.join_path)

            result = gpd.sjoin(target, join, how='left', predicate='within')
            result = result.loc[~result.index.duplicated(keep='first')]
            driver = "OpenFileGDB" if self.output_format == "GDB" else ("GPKG" if self.output_format == "GPKG" else "ESRI Shapefile")
            result.to_file(self.output_path, driver=driver)
            return _validated_count_result(len(result), len(target), "spatial_join_feature_count")

        return _run_repeated_operation(self.repeat_count, _cleanup, _run_once)


class V6_CalculateField_OS(BaseBenchmark):
    """Benchmark: Calculate Field using GeoPandas"""
    
    def __init__(self, output_format='GPKG'):
        super(V6_CalculateField_OS, self).__init__("V6_CalculateField_OS", "vector_os")
        self.gdb_path = None
        self.input_layer = None
        self.output_path = None
        self.output_format = output_format

    def setup(self):
        self.input_path, self.input_layer = get_input_feature_path_os("calculate_field_fc", settings.DATA_DIR)
        gdb_path = get_benchmark_gdb_path(settings.DATA_DIR)
        if self.output_format == 'GDB':
            self.output_path = os.path.join(gdb_path, "V6_calculate_field_os")
        else:
            self.output_path = os.path.join(settings.DATA_DIR, "V6_calculate_field_os.gpkg")

    def teardown(self):
        if self.output_path and os.path.exists(self.output_path):
            try:
                os.remove(self.output_path)
            except:
                pass

    def run_single(self):
        # Read input
        if self.input_layer:
            gdf = gpd.read_file(self.input_path, layer=self.input_layer)
        else:
            gdf = gpd.read_file(self.input_path)
        
        # Perform field calculation (vectorized)
        gdf['calc_field'] = gdf['poly_id'] * 2.5 + 100
        
        # Save output
        driver = "OpenFileGDB" if self.output_format == "GDB" else "GPKG"
        gdf.to_file(self.output_path, driver=driver)
        
        sample_values = []
        for _, row in gdf[['poly_id', 'calc_field']].head(5).iterrows():
            poly_id = int(row['poly_id'])
            calc_value = float(row['calc_field'])
            expected_value = poly_id * 2.5 + 100.0
            if abs(calc_value - expected_value) > 1e-6:
                raise RuntimeError(
                    "calculate_field_sample 鏍￠獙澶辫触: poly_id={} 鏈熸湜 {}锛屽疄闄?{}".format(
                        poly_id, expected_value, calc_value
                    )
                )
            sample_values.append("{}->{:.1f}".format(poly_id, calc_value))

        return {
            'features_processed': len(gdf),
            'expected_features': len(gdf),
            'validation_metric': 'calculate_field_samples',
            'validation_expected': "{} records; sample formula matches".format(len(gdf)),
            'validation_observed': "; ".join(sample_values),
            'validation_passed': True,
        }


if __name__ == '__main__':
    if not HAS_OS_LIBS:
        print("Open-source libraries not available. Please install:")
        print("  pip install geopandas shapely pyogrio")
        sys.exit(1)
    
    print("Testing open-source vector benchmarks...")
    benchmarks = VectorBenchmarksOS.get_all_benchmarks()
    for bm in benchmarks:
        print("\nTest: {}".format(bm.name))
        try:
            stats = bm.run(num_runs=1, warmup_runs=0)
            print("  Success: {}".format(stats.get('success')))
            print("  Mean time: {:.4f}s".format(stats.get('mean_time', 0)))
        except Exception as e:
            print("  Error: {}".format(str(e)))
