# -*- coding: utf-8 -*-
"""
Task specification constants for the 6-core benchmark matrix.
Compatible with Python 2.7 and 3.x
"""
from __future__ import print_function, division, absolute_import

CORE_TASK_IDS = [
    "Buffer",
    "Intersect",
    "SpatialJoin",
    "Resample",
    "Clip",
    "PolygonToRaster",
]

# Region-oriented suite used by the Guangdong benchmark profile.
# This expands the legacy 6-core matrix with the remaining existing vector and
# raster benchmarks so the suite better reflects the paper-style workflow.
REGION_TASK_IDS = [
    "V1_CreateFishnet",
    "V2_CreateRandomPoints",
    "Buffer",
    "Intersect",
    "SpatialJoin",
    "V6_CalculateField",
    "R1_CreateConstantRaster",
    "Resample",
    "Clip",
    "R4_RasterCalculator",
    "PolygonToRaster",
    "M2_RasterToPoint",
]

NATIONAL_TASK_IDS = [
    "V1_CreateFishnet",
    "V2_CreateRandomPoints",
    "Buffer",
    "Intersect",
    "SpatialJoin",
    "R1_CreateConstantRaster",
    "Resample",
    "Clip",
    "PolygonToRaster",
    "M2_RasterToPoint",
]

ALL_TASK_IDS = list(dict.fromkeys(CORE_TASK_IDS + REGION_TASK_IDS + NATIONAL_TASK_IDS))

CORE_TASK_CATEGORIES = {
    "Buffer": "vector",
    "Intersect": "vector",
    "SpatialJoin": "vector",
    "Resample": "raster",
    "Clip": "raster",
    "PolygonToRaster": "mixed",
}

CORE_TASK_NAMES = {
    "Buffer": "Vector Buffer",
    "Intersect": "Overlay Intersect",
    "SpatialJoin": "Spatial Join",
    "Resample": "Raster Resample",
    "Clip": "Raster Clip/Mask",
    "PolygonToRaster": "Polygon to Raster",
}

# Mapping from core task id to legacy benchmark name used in the original suite.
# This allows the runner to instantiate the correct legacy benchmark class.
LEGACY_BENCHMARK_NAMES = {
    "V1_CreateFishnet": "V1_CreateFishnet",
    "V2_CreateRandomPoints": "V2_CreateRandomPoints",
    "Buffer": "V3_Buffer",
    "Intersect": "V4_Intersect",
    "SpatialJoin": "V5_SpatialJoin",
    "V6_CalculateField": "V6_CalculateField",
    "R1_CreateConstantRaster": "R1_CreateConstantRaster",
    "Resample": "R2_Resample",
    "Clip": "R3_Clip",
    "R4_RasterCalculator": "R4_RasterCalculator",
    "PolygonToRaster": "M1_PolygonToRaster",
    "M2_RasterToPoint": "M2_RasterToPoint",
}

# Legacy open-source suffix
LEGACY_BENCHMARK_NAMES_OS = {
    "V1_CreateFishnet": "V1_CreateFishnet_OS",
    "V2_CreateRandomPoints": "V2_CreateRandomPoints_OS",
    "Buffer": "V3_Buffer_OS",
    "Intersect": "V4_Intersect_OS",
    "SpatialJoin": "V5_SpatialJoin_OS",
    "V6_CalculateField": "V6_CalculateField_OS",
    "R1_CreateConstantRaster": "R1_CreateConstantRaster_OS",
    "Resample": "R2_Resample_OS",
    "Clip": "R3_Clip_OS",
    "R4_RasterCalculator": "R4_RasterCalculator_OS",
    "PolygonToRaster": "M1_PolygonToRaster_OS",
    "M2_RasterToPoint": "M2_RasterToPoint_OS",
}

FORMAT_EXTENSIONS = {
    "SHP": ".shp",
    "GPKG": ".gpkg",
    "GDB": "",  # feature class inside geodatabase
}

FORMAT_DRIVERS_OS = {
    "SHP": "ESRI Shapefile",
    "GPKG": "GPKG",
    "GDB": "OpenFileGDB",
}

ALL_SCALES = ["tiny", "small", "standard", "medium", "large"]
ALL_FORMATS = ["SHP", "GPKG", "GDB"]
ALL_COMPLEXITIES = ["simple", "medium", "complex"]
