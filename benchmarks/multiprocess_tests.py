# -*- coding: utf-8 -*-
"""
Multiprocess benchmark tests
Compatible with Python 2.7 and 3.x
"""
from __future__ import print_function, division, absolute_import
import sys
import os
import tempfile
import shutil
import math

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import arcpy
from config import settings
from benchmarks.multiprocess_benchmark import MultiprocessBenchmark


class MP_V1_CreateFishnet(MultiprocessBenchmark):
    """Multiprocess benchmark: Create Fishnet"""
    
    def __init__(self):
        super(MP_V1_CreateFishnet, self).__init__("MP_V1_CreateFishnet", "vector_multiprocess")
        self.rows = settings.VECTOR_CONFIG['fishnet_rows']
        self.cols = settings.VECTOR_CONFIG['fishnet_cols']
        self.output_fc = None
        self.temp_dir = None
    
    def setup(self):
        arcpy.env.workspace = settings.DATA_DIR
        arcpy.env.overwriteOutput = True
        
        # Main output
        self.output_fc = os.path.join(
            settings.DATA_DIR,
            "MP_V1_fishnet_output.shp"
        )
        
        # Temp directory for worker outputs
        self.temp_dir = tempfile.mkdtemp(prefix="mp_fishnet_")
    
    def teardown(self):
        # Clean up main output
        if self.output_fc and arcpy.Exists(self.output_fc):
            try:
                arcpy.Delete_management(self.output_fc)
            except Exception:
                pass
        
        # Clean up temp directory
        if self.temp_dir and os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except Exception:
                pass
    
    def run_single(self):
        """Single process version"""
        if arcpy.Exists(self.output_fc):
            arcpy.Delete_management(self.output_fc)
        
        arcpy.CreateFishnet_management(
            out_feature_class=self.output_fc,
            origin_coord="-180 -90",
            y_axis_coord="-180 -80",
            cell_width=0,
            cell_height=0,
            number_rows=self.rows,
            number_columns=self.cols,
            corner_coord="180 90",
            labels="NO_LABELS",
            template="",
            geometry_type="POLYGON"
        )
        
        sr = arcpy.SpatialReference(settings.SPATIAL_REFERENCE)
        arcpy.DefineProjection_management(self.output_fc, sr)
        
        count = int(arcpy.GetCount_management(self.output_fc)[0])
        return {'features_created': count, 'mode': 'single'}
    
    def run_multiprocess(self, num_workers):
        """Multiprocess version - partition by rows"""
        import multiprocessing
        
        # Calculate partition size
        rows_per_worker = self.rows // num_workers
        remainder = self.rows % num_workers
        
        # Prepare tasks
        tasks = []
        row_start = 0
        for worker_id in range(num_workers):
            # Distribute remainder rows to first few workers
            extra = 1 if worker_id < remainder else 0
            row_count = rows_per_worker + extra
            row_end = row_start + row_count
            
            output_path = os.path.join(
                self.temp_dir,
                "fishnet_worker_{}.shp".format(worker_id)
            )
            
            tasks.append((worker_id, self.rows, self.cols, row_start, row_end, output_path))
            self.temp_outputs.append(output_path)
            
            row_start = row_end
        
        # Run workers in parallel
        pool = multiprocessing.Pool(processes=num_workers)
        results = pool.map(_worker_fishnet, tasks)
        pool.close()
        pool.join()
        
        # Check results
        successful = [r for r in results if r.get('success')]
        if len(successful) != num_workers:
            errors = [r.get('error') for r in results if not r.get('success')]
            raise RuntimeError("Some workers failed: {}".format(errors))
        
        # Merge results
        if arcpy.Exists(self.output_fc):
            arcpy.Delete_management(self.output_fc)
        
        outputs_to_merge = [r['output'] for r in successful]
        arcpy.Merge_management(outputs_to_merge, self.output_fc)
        
        count = int(arcpy.GetCount_management(self.output_fc)[0])
        return {
            'features_created': count,
            'mode': 'multiprocess',
            'workers': num_workers,
            'partitions': len(successful)
        }


def _worker_fishnet(args):
    """Worker function for fishnet creation"""
    worker_id, total_rows, cols, row_start, row_end, output_path = args
    
    try:
        import arcpy
        arcpy.env.overwriteOutput = True
        
        # Calculate geometry
        total_width = 360.0
        total_height = 180.0
        cell_width = total_width / cols
        cell_height = total_height / total_rows
        
        origin_y = 90 - (row_start * cell_height)
        corner_y = 90 - (row_end * cell_height)
        num_rows = row_end - row_start
        
        arcpy.CreateFishnet_management(
            out_feature_class=output_path,
            origin_coord="-180 {}".format(origin_y),
            y_axis_coord="-180 {}".format(origin_y + 10),
            cell_width=cell_width,
            cell_height=cell_height,
            number_rows=num_rows,
            number_columns=cols,
            corner_coord="180 {}".format(corner_y),
            labels="NO_LABELS",
            template="",
            geometry_type="POLYGON"
        )
        
        sr = arcpy.SpatialReference(settings.SPATIAL_REFERENCE)
        arcpy.DefineProjection_management(output_path, sr)
        
        return {'success': True, 'worker_id': worker_id, 'output': output_path}
    except Exception as e:
        import traceback
        return {
            'success': False,
            'worker_id': worker_id,
            'error': str(e),
            'traceback': traceback.format_exc()
        }


class MP_V2_CreateRandomPoints(MultiprocessBenchmark):
    """Multiprocess benchmark: Create Random Points"""
    
    def __init__(self):
        super(MP_V2_CreateRandomPoints, self).__init__("MP_V2_CreateRandomPoints", "vector_multiprocess")
        self.num_points = settings.VECTOR_CONFIG['random_points']
        self.output_fc = None
        self.temp_dir = None
    
    def setup(self):
        arcpy.env.workspace = settings.DATA_DIR
        arcpy.env.overwriteOutput = True
        self.output_fc = os.path.join(settings.DATA_DIR, "MP_V2_random_points.shp")
        self.temp_dir = tempfile.mkdtemp(prefix="mp_random_points_")
    
    def teardown(self):
        if self.output_fc and arcpy.Exists(self.output_fc):
            try:
                arcpy.Delete_management(self.output_fc)
            except Exception:
                pass
        
        if self.temp_dir and os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except Exception:
                pass
    
    def run_single(self):
        """Single process version"""
        if arcpy.Exists(self.output_fc):
            arcpy.Delete_management(self.output_fc)
        
        arcpy.CreateRandomPoints_management(
            out_path=settings.DATA_DIR,
            out_name="MP_V2_random_points",
            constraining_extent="-180 -90 180 90",
            number_of_points_or_field=self.num_points,
            minimum_allowed_distance="0 DecimalDegrees"
        )
        
        count = int(arcpy.GetCount_management(self.output_fc)[0])
        return {'features_created': count, 'mode': 'single'}
    
    def run_multiprocess(self, num_workers):
        """Multiprocess version - partition by extent"""
        import multiprocessing
        
        # Divide points among workers
        points_per_worker = self.num_points // num_workers
        remainder = self.num_points % num_workers
        
        # Divide spatial extent (simple grid partition)
        tasks = []
        for worker_id in range(num_workers):
            extra = 1 if worker_id < remainder else 0
            num_points = points_per_worker + extra
            
            # Calculate sub-extent (partition longitude)
            lon_start = -180 + (360.0 / num_workers) * worker_id
            lon_end = -180 + (360.0 / num_workers) * (worker_id + 1)
            extent = "{} -90 {} 90".format(lon_start, lon_end)
            
            output_path = os.path.join(
                self.temp_dir,
                "random_points_worker_{}.shp".format(worker_id)
            )
            
            tasks.append((worker_id, num_points, extent, output_path))
            self.temp_outputs.append(output_path)
        
        # Run workers
        pool = multiprocessing.Pool(processes=num_workers)
        results = pool.map(_worker_random_points, tasks)
        pool.close()
        pool.join()
        
        # Merge results
        successful = [r for r in results if r.get('success')]
        if len(successful) != num_workers:
            raise RuntimeError("Some workers failed")
        
        if arcpy.Exists(self.output_fc):
            arcpy.Delete_management(self.output_fc)
        
        outputs_to_merge = [r['output'] for r in successful]
        arcpy.Merge_management(outputs_to_merge, self.output_fc)
        
        count = int(arcpy.GetCount_management(self.output_fc)[0])
        return {
            'features_created': count,
            'mode': 'multiprocess',
            'workers': num_workers
        }


def _worker_random_points(args):
    """Worker function for random points creation"""
    worker_id, num_points, extent, output_path = args
    
    try:
        import arcpy
        arcpy.env.overwriteOutput = True
        
        arcpy.CreateRandomPoints_management(
            out_path=os.path.dirname(output_path),
            out_name=os.path.basename(output_path).replace('.shp', ''),
            constraining_extent=extent,
            number_of_points_or_field=num_points,
            minimum_allowed_distance="0 DecimalDegrees"
        )
        
        return {'success': True, 'worker_id': worker_id, 'output': output_path}
    except Exception as e:
        import traceback
        return {
            'success': False,
            'worker_id': worker_id,
            'error': str(e),
            'traceback': traceback.format_exc()
        }


class MP_V3_Buffer(MultiprocessBenchmark):
    """Multiprocess benchmark: Buffer Analysis"""
    
    def __init__(self):
        super(MP_V3_Buffer, self).__init__("MP_V3_Buffer", "vector_multiprocess")
        self.input_fc = None
        self.output_fc = None
        self.temp_dir = None
        self.buffer_distance = "1 Kilometer"
    
    def setup(self):
        arcpy.env.workspace = settings.DATA_DIR
        arcpy.env.overwriteOutput = True
        
        # Use pre-generated buffer points as input
        gdb_path = os.path.join(settings.DATA_DIR, settings.DEFAULT_GDB_NAME)
        self.input_fc = os.path.join(gdb_path, "buffer_points")
        self.output_fc = os.path.join(settings.DATA_DIR, "MP_V3_buffer_output.shp")
        self.temp_dir = tempfile.mkdtemp(prefix="mp_buffer_")
    
    def teardown(self):
        if self.output_fc and arcpy.Exists(self.output_fc):
            try:
                arcpy.Delete_management(self.output_fc)
            except Exception:
                pass
        
        if self.temp_dir and os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except Exception:
                pass
    
    def run_single(self):
        """Single process version"""
        if arcpy.Exists(self.output_fc):
            arcpy.Delete_management(self.output_fc)
        
        arcpy.Buffer_analysis(
            in_features=self.input_fc,
            out_feature_class=self.output_fc,
            buffer_distance_or_field=self.buffer_distance,
            line_side="FULL",
            line_end_type="ROUND",
            dissolve_option="NONE"
        )
        
        count = int(arcpy.GetCount_management(self.output_fc)[0])
        return {'features_created': count, 'mode': 'single'}
    
    def run_multiprocess(self, num_workers):
        """Multiprocess version - partition by FID range"""
        import multiprocessing
        
        # Get total count
        total_count = int(arcpy.GetCount_management(self.input_fc)[0])
        count_per_worker = total_count // num_workers
        remainder = total_count % num_workers
        
        # Create tasks with FID ranges
        tasks = []
        fid_start = 1  # FID typically starts at 1
        for worker_id in range(num_workers):
            extra = 1 if worker_id < remainder else 0
            fid_count = count_per_worker + extra
            fid_end = fid_start + fid_count - 1
            
            output_path = os.path.join(
                self.temp_dir,
                "buffer_worker_{}.shp".format(worker_id)
            )
            
            tasks.append((
                worker_id,
                self.input_fc,
                output_path,
                fid_start,
                fid_end,
                self.buffer_distance
            ))
            self.temp_outputs.append(output_path)
            
            fid_start = fid_end + 1
        
        # Run workers
        pool = multiprocessing.Pool(processes=num_workers)
        results = pool.map(_worker_buffer, tasks)
        pool.close()
        pool.join()
        
        # Merge results
        successful = [r for r in results if r.get('success')]
        if len(successful) != num_workers:
            raise RuntimeError("Some workers failed")
        
        if arcpy.Exists(self.output_fc):
            arcpy.Delete_management(self.output_fc)
        
        outputs_to_merge = [r['output'] for r in successful]
        arcpy.Merge_management(outputs_to_merge, self.output_fc)
        
        count = int(arcpy.GetCount_management(self.output_fc)[0])
        return {
            'features_created': count,
            'mode': 'multiprocess',
            'workers': num_workers
        }


def _worker_buffer(args):
    """Worker function for buffer analysis"""
    worker_id, input_fc, output_path, fid_start, fid_end, buffer_distance = args
    
    try:
        import arcpy
        arcpy.env.overwriteOutput = True
        
        # Select features by FID range
        where_clause = "FID >= {} AND FID <= {}".format(fid_start, fid_end)
        temp_layer = "buffer_layer_{}".format(worker_id)
        arcpy.MakeFeatureLayer_management(input_fc, temp_layer, where_clause)
        
        arcpy.Buffer_analysis(
            in_features=temp_layer,
            out_feature_class=output_path,
            buffer_distance_or_field=buffer_distance,
            line_side="FULL",
            line_end_type="ROUND",
            dissolve_option="NONE"
        )
        
        # Clean up layer
        arcpy.Delete_management(temp_layer)
        
        return {'success': True, 'worker_id': worker_id, 'output': output_path}
    except Exception as e:
        import traceback
        return {
            'success': False,
            'worker_id': worker_id,
            'error': str(e),
            'traceback': traceback.format_exc()
        }


class MP_R1_CreateConstantRaster(MultiprocessBenchmark):
    """Multiprocess benchmark: Create Constant Raster"""
    
    def __init__(self):
        super(MP_R1_CreateConstantRaster, self).__init__("MP_R1_CreateConstantRaster", "raster_multiprocess")
        self.size = settings.RASTER_CONFIG['constant_raster_size']
        self.output_raster = None
        self.temp_dir = None
    
    def setup(self):
        arcpy.env.workspace = settings.DATA_DIR
        arcpy.env.overwriteOutput = True
        self.output_raster = os.path.join(settings.DATA_DIR, "MP_R1_constant_raster.tif")
        self.temp_dir = tempfile.mkdtemp(prefix="mp_raster_")
    
    def teardown(self):
        if self.output_raster and arcpy.Exists(self.output_raster):
            try:
                arcpy.Delete_management(self.output_raster)
            except Exception:
                pass
        
        if self.temp_dir and os.path.exists(self.temp_dir):
            try:
                shutil.rmtree(self.temp_dir)
            except Exception:
                pass
    
    def run_single(self):
        """Single process version"""
        if arcpy.Exists(self.output_raster):
            arcpy.Delete_management(self.output_raster)
        
        cell_size = 360.0 / self.size
        extent = "-180 -90 180 90"
        
        try:
            from arcpy.sa import CreateConstantRaster
            out_raster = CreateConstantRaster(1, "INTEGER", cell_size, extent)
            out_raster.save(self.output_raster)
        except:
            arcpy.CreateConstantRaster_sa(
                self.output_raster,
                1,
                "INTEGER",
                cell_size,
                extent
            )
        
        return {'raster_created': self.output_raster, 'mode': 'single'}
    
    def run_multiprocess(self, num_workers):
        """Multiprocess version - partition by rows"""
        import multiprocessing
        
        # Calculate partition size (by rows)
        rows_per_worker = self.size // num_workers
        remainder = self.size % num_workers
        
        cell_size = 360.0 / self.size
        
        tasks = []
        row_start = 0
        for worker_id in range(num_workers):
            extra = 1 if worker_id < remainder else 0
            row_count = rows_per_worker + extra
            row_end = row_start + row_count
            
            # Calculate extent for this partition
            y_start = 90 - (row_start * cell_size)
            y_end = 90 - (row_end * cell_size)
            extent = "-180 {} 180 {}".format(y_end, y_start)
            
            output_path = os.path.join(
                self.temp_dir,
                "raster_worker_{}.tif".format(worker_id)
            )
            
            tasks.append((worker_id, cell_size, extent, output_path))
            self.temp_outputs.append(output_path)
            
            row_start = row_end
        
        # Run workers
        pool = multiprocessing.Pool(processes=num_workers)
        results = pool.map(_worker_create_raster, tasks)
        pool.close()
        pool.join()
        
        # Mosaic results
        successful = [r for r in results if r.get('success')]
        if len(successful) != num_workers:
            raise RuntimeError("Some workers failed")
        
        if arcpy.Exists(self.output_raster):
            arcpy.Delete_management(self.output_raster)
        
        rasters_to_mosaic = [r['output'] for r in successful]
        arcpy.MosaicToNewRaster_management(
            input_rasters=";".join(rasters_to_mosaic),
            output_location=os.path.dirname(self.output_raster),
            raster_dataset_name_with_extension=os.path.basename(self.output_raster),
            pixel_type="8_BIT_UNSIGNED",
            cell_size=cell_size,
            number_of_bands=1
        )
        
        return {
            'raster_created': self.output_raster,
            'mode': 'multiprocess',
            'workers': num_workers
        }


def _worker_create_raster(args):
    """Worker function for raster creation"""
    worker_id, cell_size, extent, output_path = args
    
    try:
        import arcpy
        arcpy.env.overwriteOutput = True
        
        try:
            from arcpy.sa import CreateConstantRaster
            out_raster = CreateConstantRaster(1, "INTEGER", cell_size, extent)
            out_raster.save(output_path)
        except:
            arcpy.CreateConstantRaster_sa(
                output_path,
                1,
                "INTEGER",
                cell_size,
                extent
            )
        
        return {'success': True, 'worker_id': worker_id, 'output': output_path}
    except Exception as e:
        import traceback
        return {
            'success': False,
            'worker_id': worker_id,
            'error': str(e),
            'traceback': traceback.format_exc()
        }


def get_multiprocess_benchmarks():
    """Get all multiprocess benchmark instances"""
    return [
        MP_V1_CreateFishnet(),
        MP_V2_CreateRandomPoints(),
        MP_V3_Buffer(),
        MP_R1_CreateConstantRaster(),
    ]


if __name__ == '__main__':
    # Test multiprocess benchmarks
    print("Testing Multiprocess Benchmarks")
    print("=" * 60)
    
    # Test V1
    print("\nTesting MP_V1_CreateFishnet...")
    v1 = MP_V1_CreateFishnet()
    
    print("  Single process...")
    v1.setup()
    result_single = v1.run_single()
    v1.teardown()
    print("  Result:", result_single)
    
    print("  Multiprocess (4 workers)...")
    v1.setup()
    result_mp = v1.run_multiprocess(4)
    v1.teardown()
    print("  Result:", result_mp)
    
    print("\nAll tests completed!")
