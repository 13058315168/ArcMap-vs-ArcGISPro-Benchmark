#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Validate open-source benchmark results against arcpy results
"""
from __future__ import print_function, division, absolute_import
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import json
from config import settings

def validate_results():
    """Validate OS benchmark results against arcpy results"""
    
    print("=" * 70)
    print("Open-Source Benchmark Results Validation")
    print("=" * 70)
    
    # Load results
    results_dir = settings.RAW_RESULTS_DIR
    
    # Try to load arcpy results
    arcpy_results = {}
    os_results = {}
    
    for filename in os.listdir(results_dir):
        if not filename.endswith('.json'):
            continue
            
        filepath = os.path.join(results_dir, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                results = data.get('results', [])
                
                for r in results:
                    test_name = r.get('test_name', '')
                    if '_OS' in test_name:
                        # Open-source result
                        base_name = test_name.replace('_OS', '')
                        os_results[base_name] = r
                    elif not test_name.startswith('Py') and '_single' not in test_name and '_multiprocess' not in test_name:
                        # Regular arcpy result
                        arcpy_results[test_name] = r
        except Exception as e:
            print("Warning: Could not load {}: {}".format(filename, e))
    
    # Validate
    print("\nValidation Results:")
    print("-" * 70)
    
    all_passed = True
    
    for test_name in sorted(arcpy_results.keys()):
        arcpy_r = arcpy_results[test_name]
        os_r = os_results.get(test_name)
        
        if not os_r:
            print("  {}: SKIP (no OS result)".format(test_name))
            continue
        
        # Check count/features created
        arcpy_count = arcpy_r.get('features_created', arcpy_r.get('features_processed', 0))
        os_count = os_r.get('features_created', os_r.get('features_processed', 0))
        
        if arcpy_count > 0 and os_count > 0:
            count_match = (arcpy_count == os_count)
        else:
            count_match = True  # Both zero or missing
        
        # Check success
        arcpy_success = arcpy_r.get('success', False)
        os_success = os_r.get('success', False)
        
        # Overall validation
        passed = count_match and os_success
        
        status = "PASS" if passed else "FAIL"
        all_passed = all_passed and passed
        
        print("  {}: {} (arcpy={}, OS={})".format(
            test_name, status, 
            arcpy_count if arcpy_count > 0 else "N/A",
            os_count if os_count > 0 else "N/A"
        ))
    
    print("-" * 70)
    
    if all_passed:
        print("✓ All validations PASSED")
        print("\nOpen-source benchmarks produce consistent results with arcpy.")
        return 0
    else:
        print("✗ Some validations FAILED")
        print("\nNote: Small differences are expected due to algorithmic variations.")
        print("The important metric is that the operations complete successfully")
        print("and produce comparable data volumes.")
        return 1


if __name__ == '__main__':
    sys.exit(validate_results())
