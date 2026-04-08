# Bug Report: Benchmark log failures on Buffer, Intersect, and JSON export

**Date:** 2026-04-08
**Severity:** high
**Status:** fixed

## Symptom
- `1.log` showed `MP_V3_Buffer` failing during `Merge`.
- `MP_V4_Intersect` failed in the single-process path on larger data and then failed again in multiprocess mode.
- Python 2 result export crashed at the end with a JSON write error.

## Expected Behavior
- Buffer and Intersect multiprocess comparisons should finish without worker failures.
- Result export should write JSON, Markdown, and CSV in both Python 2.7 and Python 3.x.

## Reproduction Steps
1. Run the benchmark with vector multiprocess enabled.
2. Use a medium or tiny dataset with the intersect/buffer multiprocess tests.
3. Observe the worker failure or final JSON export crash.

## Root Cause Analysis

### Location
- **File:** `benchmarks/multiprocess_tests.py`
- **Function:** `MP_V3_Buffer.run_multiprocess`, `MP_V4_Intersect._run_partitioned_intersect`
- **File:** `utils/result_exporter.py`
- **Function:** `ResultExporter.export_json`

### Cause
- Buffer originally reused shared shapefile temp names and directories across iterations, which made the merge step vulnerable to leftover outputs and lock contention.
- The first intersect fix tried to prefilter `input_b` with `SelectLayerByLocation`, but ArcPy rejected the geometry predicate on non-simple geometry: `无法对非简单几何执行此操作`. The safer path is to partition `input_a` only and intersect each chunk against the full `input_b`.
- `export_json` used `json.dump` directly on a Python 2 UTF-8 text wrapper. In Python 2, that path can emit `str` instead of `unicode`, causing `write() argument 1 must be unicode, not str`.

### When Introduced
- These were introduced in the current release-hardening working tree before this fix; the intersect/export issues were not from a committed release tag.

## Proposed Fix

### Changes Required
1. Create an isolated per-iteration workspace for multiprocess Buffer and write partition outputs into a file geodatabase.
2. Keep multiprocess Intersect on A-partitions only, with unique temp outputs and no `SelectLayerByLocation` prefilter.
3. Serialize JSON explicitly and write Unicode safely in Python 2.

### Risks
- Intersect multiprocess remains slower than ideal on larger inputs, but it now completes reliably and preserves the benchmark output contract.

### Tests Needed
- Tiny vector multiprocess smoke run on Python 2.7.
- JSON export smoke on Python 3.x.

## Verification
- `python -m py_compile benchmarks\multiprocess_tests.py utils\result_exporter.py`
- Py2 tiny vector smoke completed with `16/16` successful benchmarks.
- Python 3 JSON export smoke wrote and re-read a UTF-8 JSON file successfully.
