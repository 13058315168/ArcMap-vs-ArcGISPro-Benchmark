#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Prepare the China OSM benchmark cache from the Geofabrik PBF source."""
from __future__ import print_function, division, absolute_import

import argparse
import os
import sys

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

from utils.china_osm_package import ensure_china_osm_package


def parse_args():
    parser = argparse.ArgumentParser(description='Prepare the China OSM package cache')
    parser.add_argument('--cache-root', default=None, help='External cache root directory')
    parser.add_argument('--force', action='store_true', help='Rebuild cache even if it already exists')
    return parser.parse_args()


def main():
    args = parse_args()
    manifest = ensure_china_osm_package(cache_root=args.cache_root, force=args.force)
    print("China OSM package prepared")
    print("PBF: {}".format(manifest.get('pbf_path')))
    print("Theme root: {}".format(manifest.get('theme_package_root')))
    for name, path in sorted((manifest.get('theme_packages') or {}).items()):
        print("  {} -> {}".format(name, path))
    return 0


if __name__ == '__main__':
    sys.exit(main())
