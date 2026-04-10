# -*- coding: utf-8 -*-
"""
Helpers for deterministic synthetic benchmark shapes and expected counts.
Compatible with Python 2.7 and 3.x.
"""
from __future__ import print_function, division, absolute_import

import math


def factor_grid_dimensions(total_count):
    """Return exact integer grid dimensions whose product equals total_count.

    The returned pair is chosen to be as square as possible while still
    multiplying to the requested count. If no better factor exists, it falls
    back to ``1 x total_count``.
    """
    total_count = int(total_count or 0)
    if total_count <= 0:
        raise ValueError("total_count must be positive")

    root = int(math.sqrt(total_count))
    for rows in range(root, 0, -1):
        if total_count % rows == 0:
            cols = total_count // rows
            return rows, cols

    return 1, total_count


def expected_offset_grid_intersections(rows_a, cols_a, rows_b, cols_b):
    """Return expected intersect output count for two half-cell offset grids."""
    rows_a = int(rows_a or 0)
    cols_a = int(cols_a or 0)
    rows_b = int(rows_b or 0)
    cols_b = int(cols_b or 0)

    if rows_a <= 0 or cols_a <= 0 or rows_b <= 0 or cols_b <= 0:
        return 0

    return (rows_a + rows_b - 1) * (cols_a + cols_b - 1)
