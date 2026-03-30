#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Run all five scales sequentially with specified parameters
"""
from __future__ import print_function, division, absolute_import
import sys
import os
import subprocess
import time

# Test configuration
SCALES = ['tiny', 'small', 'standard', 'medium', 'large']
RUNS = 3
WARMUP = 0
MP_WORKERS = 4

def run_scale(scale):
    """Run benchmark for a single scale"""
    print("\n" + "="*70)
    print("Running scale: {}".format(scale.upper()))
    print("="*70)
    
    cmd = [
        sys.executable,
        "run_benchmarks.py",
        "--scale", scale,
        "--runs", str(RUNS),
        "--warmup", str(WARMUP),
        "--multiprocess",
        "--mp-workers", str(MP_WORKERS),
        "--opensource"
    ]
    
    print("Command: {}".format(" ".join(cmd)))
    print("-"*70)
    
    start_time = time.time()
    result = subprocess.call(cmd)
    elapsed = time.time() - start_time
    
    print("\nScale {} completed in {:.1f} seconds (exit code: {})".format(
        scale.upper(), elapsed, result))
    
    return result == 0

def main():
    print("="*70)
    print("ArcGIS Python Benchmark - All Scales Test")
    print("="*70)
    print("Configuration:")
    print("  Scales: {}".format(", ".join(SCALES)))
    print("  Runs: {}".format(RUNS))
    print("  Warmup: {}".format(WARMUP))
    print("  Multiprocess: Enabled ({} workers)".format(MP_WORKERS))
    print("  Open-source: Enabled")
    print("="*70)
    
    failed_scales = []
    
    for i, scale in enumerate(SCALES, 1):
        print("\n\n[{}/5] Starting {} scale...".format(i, scale.upper()))
        
        if not run_scale(scale):
            print("\n[ERROR] Scale {} FAILED!".format(scale.upper()))
            failed_scales.append(scale)
            # Continue with next scale instead of stopping
        
        # Small delay between scales
        if i < len(SCALES):
            print("\nWaiting 5 seconds before next scale...")
            time.sleep(5)
    
    # Summary
    print("\n" + "="*70)
    print("TEST COMPLETE")
    print("="*70)
    print("Completed: {}/5 scales".format(len(SCALES) - len(failed_scales)))
    if failed_scales:
        print("Failed: {}".format(", ".join(failed_scales)))
        return 1
    else:
        print("All scales passed!")
        return 0

if __name__ == '__main__':
    sys.exit(main())
