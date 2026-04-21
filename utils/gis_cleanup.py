# -*- coding: utf-8 -*-
"""
ArcGIS cleanup helpers for workspace cache and file-based dataset artifacts.
Compatible with Python 2.7 and 3.x
"""
from __future__ import print_function, division, absolute_import
import os
import shutil
import time

HAS_ARCPY = False
arcpy = None


def _get_arcpy():
    """Import arcpy lazily so lightweight CLI paths can load this module."""
    global HAS_ARCPY, arcpy
    if arcpy is not None:
        return arcpy
    try:
        import arcpy as _arcpy
        arcpy = _arcpy
        HAS_ARCPY = True
    except Exception:
        HAS_ARCPY = False
        arcpy = None
    return arcpy


def clear_workspace_cache(workspace=None):
    """Release ArcPy workspace locks and optionally reset the active workspace."""
    _arcpy = _get_arcpy()
    if not HAS_ARCPY or _arcpy is None:
        return

    try:
        _arcpy.ClearWorkspaceCache_management()
    except Exception:
        pass

    if workspace is not None:
        try:
            _arcpy.env.workspace = workspace
        except Exception:
            pass
        try:
            _arcpy.env.scratchWorkspace = workspace
        except Exception:
            pass
    else:
        try:
            _arcpy.env.workspace = None
        except Exception:
            pass
        try:
            _arcpy.env.scratchWorkspace = None
        except Exception:
            pass


def is_file_gdb_workspace(path):
    """Return True when *path* is a real file geodatabase workspace."""
    if not path or not os.path.isdir(path):
        return False

    _arcpy = _get_arcpy()
    if not HAS_ARCPY or _arcpy is None:
        return str(path).lower().endswith('.gdb')

    try:
        desc = _arcpy.Describe(path)
        factory = getattr(desc, 'workspaceFactoryProgID', '') or ''
        if 'FileGDBWorkspaceFactory' in str(factory):
            return True
    except Exception:
        pass
    return False


def ensure_file_gdb(path):
    """Create a real file geodatabase at *path* if needed."""
    if not path:
        raise ValueError("GDB path is required")

    path = os.path.abspath(path)
    parent = os.path.dirname(path)
    name = os.path.basename(path)

    if is_file_gdb_workspace(path):
        return path

    if os.path.exists(path):
        try:
            shutil.rmtree(path, ignore_errors=True)
        except Exception:
            pass
        try:
            if os.path.isfile(path):
                os.remove(path)
        except Exception:
            pass

    if parent and not os.path.exists(parent):
        os.makedirs(parent)

    _arcpy = _get_arcpy()
    if not HAS_ARCPY or _arcpy is None:
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    _arcpy.CreateFileGDB_management(parent, name)
    return path


def _delete_file(path):
    """Delete a single file if it exists."""
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass


def remove_dataset_artifacts(path, retries=3, sleep_seconds=0.5):
    """Remove a dataset and common file-based sidecar artifacts."""
    if not path:
        return

    _arcpy = _get_arcpy()

    candidates = [path]
    base, ext = os.path.splitext(path)
    ext = ext.lower()

    if ext == '.shp':
        candidates.extend([
            base + '.shx',
            base + '.dbf',
            base + '.prj',
            base + '.cpg',
            base + '.sbn',
            base + '.sbx',
            base + '.xml',
            base + '.fix',
            path + '.xml',
        ])
    elif ext in ('.tif', '.tiff', '.img', '.jpg', '.jpeg'):
        candidates.extend([
            path + '.aux.xml',
            base + '.aux.xml',
            path + '.ovr',
            base + '.ovr',
            path + '.xml',
            base + '.xml',
            path + '.tfw',
            base + '.tfw',
            path + '.cpg',
            base + '.cpg',
        ])
    elif ext == '.gdb' and os.path.isdir(path):
        shutil.rmtree(path, ignore_errors=True)
        return

    for attempt in range(max(1, int(retries))):
        clear_workspace_cache()

        if HAS_ARCPY and _arcpy is not None:
            try:
                if _arcpy.Exists(path):
                    _arcpy.Delete_management(path)
            except Exception:
                pass

        for candidate in candidates:
            if candidate == path and os.path.isdir(candidate):
                shutil.rmtree(candidate, ignore_errors=True)
                continue
            _delete_file(candidate)

        if not os.path.exists(path) and not (HAS_ARCPY and _arcpy is not None and _arcpy.Exists(path)):
            break

        if attempt < int(retries) - 1:
            time.sleep(float(sleep_seconds))
