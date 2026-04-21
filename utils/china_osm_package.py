# -*- coding: utf-8 -*-
"""Utilities for preparing a China-wide OSM benchmark package.

The repository uses the China OSM PBF as the authoritative upstream source.
This helper downloads the raw PBF into an external cache, then prepares a set
of theme-specific subpackages that can be consumed by both ArcGIS and
open-source benchmark runs.
"""
from __future__ import print_function, division, absolute_import

import json
import os
import shutil
import tempfile
from datetime import datetime

from config import settings


CHINA_PBF_SOURCE = {
    'slug': 'china',
    'label': 'China',
    'url': 'https://download.geofabrik.de/asia/china-latest.osm.pbf',
}

THEME_DEFS = {
    'roads': {
        'source_layers': ['lines', 'multilinestrings'],
        'filters': [('highway',)],
        'geometry_type': 'POLYLINE',
    },
    'buildings': {
        'source_layers': ['multipolygons'],
        'filters': [('building',)],
        'geometry_type': 'POLYGON',
    },
    'landuse': {
        'source_layers': ['multipolygons'],
        'filters': [('landuse',)],
        'geometry_type': 'POLYGON',
    },
    'pois': {
        'source_layers': ['points'],
        'filters': [('amenity',), ('shop',), ('tourism',), ('leisure',), ('office',), ('historic',), ('emergency',), ('railway',), ('man_made',)],
        'geometry_type': 'POINT',
    },
    'places': {
        'source_layers': ['points'],
        'filters': [('place',)],
        'geometry_type': 'POINT',
    },
}


def _ensure_dir(path):
    if path and not os.path.exists(path):
        os.makedirs(path)
    return path


def _china_cache_root(cache_root=None):
    if cache_root:
        return os.path.abspath(cache_root)
    national_root = getattr(settings, 'NATIONAL_OSM_CACHE_DIR', None)
    if national_root:
        return os.path.abspath(national_root)
    return os.path.join(getattr(settings, 'DATA_ROOT_DIR', r'C:\temp\arcgis_benchmark_data'), '_osm_cache', 'china')


def get_china_pbf_path(cache_root=None):
    root = _china_cache_root(cache_root)
    return os.path.join(root, CHINA_PBF_SOURCE['slug'], os.path.basename(CHINA_PBF_SOURCE['url']))


def get_china_total_package_dir(cache_root=None):
    root = _china_cache_root(cache_root)
    return os.path.join(root, CHINA_PBF_SOURCE['slug'], 'total')


def get_china_theme_package_dir(cache_root=None):
    root = _china_cache_root(cache_root)
    return os.path.join(root, CHINA_PBF_SOURCE['slug'], 'themes')


def get_china_package_manifest_path(cache_root=None):
    root = _china_cache_root(cache_root)
    return os.path.join(root, CHINA_PBF_SOURCE['slug'], 'china_package_manifest.json')


def _load_manifest(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r') as handle:
            return json.load(handle)
    except Exception:
        return {}


def _save_manifest(path, payload):
    _ensure_dir(os.path.dirname(path))
    with open(path, 'w') as handle:
        json.dump(payload, handle, indent=2, ensure_ascii=False, sort_keys=True)


def _cached_dataset_path_exists(path):
    if not path:
        return False
    if os.path.exists(path):
        return True
    lower_path = path.lower()
    marker = '.gdb'
    marker_index = lower_path.find(marker)
    if marker_index >= 0:
        gdb_path = path[:marker_index + len(marker)]
        return os.path.isdir(gdb_path)
    return False


def ensure_china_pbf_cache(cache_root=None, force=False):
    """Download the China OSM PBF into the external cache when needed."""
    from utils.osm_samples import download_file

    pbf_path = get_china_pbf_path(cache_root)
    if not force and os.path.exists(pbf_path) and os.path.getsize(pbf_path) > 0:
        return pbf_path

    _ensure_dir(os.path.dirname(pbf_path))
    print("  [China OSM] Downloading PBF source: {}".format(CHINA_PBF_SOURCE['url']))
    download_file(CHINA_PBF_SOURCE['url'], pbf_path)
    return pbf_path


def _import_optional_packages():
    try:
        import geopandas as gpd
    except Exception:
        gpd = None
    try:
        import pyogrio
    except Exception:
        pyogrio = None
    try:
        import pandas as pd
    except Exception:
        pd = None
    try:
        import arcpy
    except Exception:
        arcpy = None
    return gpd, pyogrio, pd, arcpy


def _normalize_columns(frame, theme_name):
    if frame is None or len(frame) == 0:
        return frame

    import pandas as pd  # local import for py2 safety

    frame = frame.copy()
    frame['theme'] = theme_name
    frame['osm_source'] = CHINA_PBF_SOURCE['label']
    keep_cols = []
    for name in ['theme', 'osm_source']:
        if name in frame.columns:
            keep_cols.append(name)

    for column in ['osm_id', 'name', 'highway', 'building', 'landuse', 'amenity', 'shop', 'tourism', 'leisure', 'office', 'historic', 'emergency', 'railway', 'man_made', 'place']:
        if column in frame.columns:
            keep_cols.append(column)

    if 'geometry' not in frame.columns:
        raise RuntimeError("Theme frame is missing geometry")
    keep_cols.append('geometry')
    return frame.loc[:, list(dict.fromkeys(keep_cols))]


def _frame_has_any(frame, columns):
    if frame is None or len(frame) == 0:
        return False
    for column in columns:
        if column in frame.columns:
            non_null = frame[column].notna()
            if bool(non_null.any()):
                return True
    return False


def _filter_theme_frame(frame, theme_name):
    if frame is None or len(frame) == 0:
        return frame
    if theme_name == 'roads':
        mask = frame['highway'].notna() if 'highway' in frame.columns else None
    elif theme_name == 'buildings':
        mask = frame['building'].notna() if 'building' in frame.columns else None
    elif theme_name == 'landuse':
        mask = frame['landuse'].notna() if 'landuse' in frame.columns else None
    elif theme_name == 'pois':
        candidates = ['amenity', 'shop', 'tourism', 'leisure', 'office', 'historic', 'emergency', 'railway', 'man_made']
        mask = None
        for column in candidates:
            if column in frame.columns:
                col_mask = frame[column].notna()
                mask = col_mask if mask is None else (mask | col_mask)
    elif theme_name == 'places':
        mask = frame['place'].notna() if 'place' in frame.columns else None
    else:
        mask = None

    if mask is None:
        return frame.iloc[0:0].copy()
    return frame.loc[mask].copy()


def _read_layer_frame(pyogrio, pbf_path, layer_name):
    try:
        return pyogrio.read_dataframe(pbf_path, layer=layer_name)
    except Exception as exc:
        raise RuntimeError("Failed to read OSM layer {} from {}: {}".format(layer_name, pbf_path, exc))


def _concat_frames(frames, gpd):
    frames = [frame for frame in frames if frame is not None and len(frame) > 0]
    if not frames:
        return None
    import pandas as pd
    combined = pd.concat(frames, ignore_index=True)
    if hasattr(gpd, 'GeoDataFrame'):
        return gpd.GeoDataFrame(combined, geometry='geometry', crs=frames[0].crs)
    return combined


def _write_temp_gpkg(frame, temp_root, layer_name, gpd):
    layer_dir = os.path.join(temp_root, layer_name)
    _ensure_dir(layer_dir)
    gpkg_path = os.path.join(layer_dir, "{}.gpkg".format(layer_name))
    if os.path.exists(gpkg_path):
        try:
            os.remove(gpkg_path)
        except Exception:
            pass
    frame.to_file(gpkg_path, layer=layer_name, driver='GPKG')
    return os.path.join(gpkg_path, layer_name)


def _ensure_gdb(gdb_path, arcpy):
    if os.path.isdir(gdb_path):
        return gdb_path
    parent = os.path.dirname(gdb_path)
    name = os.path.basename(gdb_path)
    _ensure_dir(parent)
    arcpy.CreateFileGDB_management(parent, name)
    return gdb_path


def _copy_vector_to_gdb(arcpy, source_dataset, gdb_path, feature_name):
    out_fc = os.path.join(gdb_path, feature_name)
    if arcpy.Exists(out_fc):
        arcpy.Delete_management(out_fc)
    arcpy.CopyFeatures_management(source_dataset, out_fc)
    return out_fc


def _feature_count(arcpy, feature_class):
    try:
        return int(arcpy.GetCount_management(feature_class).getOutput(0))
    except Exception:
        return 0


def build_china_theme_packages(cache_root=None, force=False):
    """Build theme subpackages derived from the China OSM PBF."""
    cache_root = _china_cache_root(cache_root)
    pbf_path = ensure_china_pbf_cache(cache_root=cache_root, force=force)
    manifest_path = get_china_package_manifest_path(cache_root)
    manifest = _load_manifest(manifest_path)
    if not force and manifest.get('theme_packages_ready') and os.path.exists(manifest.get('total_package_path', '')):
        themes = manifest.get('theme_packages') or {}
        theme_paths = list(themes.values())
        if themes and all(_cached_dataset_path_exists(path) for path in theme_paths):
            return manifest

    gpd, pyogrio, pd, arcpy = _import_optional_packages()
    if gpd is None or pyogrio is None:
        raise RuntimeError("Geopandas / Pyogrio are required to prepare the China OSM package")
    if arcpy is None:
        raise RuntimeError("ArcPy is required to convert the China package into GDB subpackages")

    package_root = os.path.join(cache_root, CHINA_PBF_SOURCE['slug'])
    total_package_dir = _ensure_dir(get_china_total_package_dir(cache_root))
    theme_root = _ensure_dir(get_china_theme_package_dir(cache_root))
    temp_root = tempfile.mkdtemp(prefix='china_osm_stage_')

    try:
        theme_packages = {}
        raw_layers = {}
        for raw_layer in ['points', 'lines', 'multilinestrings', 'multipolygons']:
            try:
                raw_frame = _read_layer_frame(pyogrio, pbf_path, raw_layer)
            except Exception as exc:
                print("  [China OSM] Warning: unable to read raw layer {}: {}".format(raw_layer, exc))
                continue
            if raw_frame is None or len(raw_frame) == 0:
                continue
            if getattr(raw_frame, 'crs', None) is None:
                raw_frame = raw_frame.set_crs(epsg=4326, allow_override=True)
            try:
                raw_frame = raw_frame.to_crs(3857)
            except Exception:
                pass
            raw_frame = _normalize_columns(raw_frame, raw_layer)
            raw_layers[raw_layer] = raw_frame

        # Write a lightweight raw package manifest so the cache is self-describing.
        _ensure_dir(total_package_dir)
        raw_manifest = {
            'source': CHINA_PBF_SOURCE,
            'pbf_path': pbf_path,
            'raw_layers': sorted(raw_layers.keys()),
            'generated_at': datetime.utcnow().isoformat(),
        }
        _save_manifest(os.path.join(total_package_dir, 'raw_manifest.json'), raw_manifest)

        for theme_name, theme_def in THEME_DEFS.items():
            frames = []
            for source_layer in theme_def.get('source_layers', []):
                source_frame = raw_layers.get(source_layer)
                if source_frame is None or len(source_frame) == 0:
                    continue
                filtered = _filter_theme_frame(source_frame, theme_name)
                if filtered is not None and len(filtered) > 0:
                    frames.append(filtered)

            theme_frame = _concat_frames(frames, gpd)
            if theme_frame is None or len(theme_frame) == 0:
                print("  [China OSM] Theme {} has no rows after filtering".format(theme_name))
                continue

            theme_frame = _normalize_columns(theme_frame, theme_name)
            theme_gdb = os.path.join(theme_root, "{}.gdb".format(theme_name))
            _ensure_gdb(theme_gdb, arcpy)
            existing_fc = os.path.join(theme_gdb, theme_name)
            if not force and arcpy.Exists(existing_fc) and _feature_count(arcpy, existing_fc) > 0:
                print("  [China OSM] Theme {} already exists, skipping".format(theme_name))
                theme_packages[theme_name] = existing_fc
                continue

            # Stage through GeoPackage so national OSM layers are not clipped by
            # the Shapefile 2GB DBF/SHP limit before ArcPy copies into GDB.
            source_dataset = _write_temp_gpkg(theme_frame, temp_root, theme_name, gpd)
            output_fc = _copy_vector_to_gdb(arcpy, source_dataset, theme_gdb, theme_name)
            theme_packages[theme_name] = output_fc

        manifest = {
            'source': CHINA_PBF_SOURCE,
            'pbf_path': pbf_path,
            'total_package_path': pbf_path,
            'total_package_dir': total_package_dir,
            'theme_package_root': theme_root,
            'theme_packages_ready': True,
            'theme_packages': theme_packages,
            'generated_at': datetime.utcnow().isoformat(),
        }
        _save_manifest(manifest_path, manifest)
        return manifest
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)


def ensure_china_osm_package(cache_root=None, force=False):
    """Ensure the China raw PBF and theme subpackages exist."""
    cache_root = _china_cache_root(cache_root)
    pbf_path = ensure_china_pbf_cache(cache_root=cache_root, force=force)
    manifest = build_china_theme_packages(cache_root=cache_root, force=force)
    if not manifest.get('pbf_path'):
        manifest['pbf_path'] = pbf_path
    return manifest
