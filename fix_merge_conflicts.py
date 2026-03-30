#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""修复Git合并冲突"""
import re

def fix_merge_conflicts(filename):
    """修复文件中的Git合并冲突"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 统计冲突标记数量
    head_count = len(re.findall(r'^<{7} HEAD', content, re.MULTILINE))
    print(f"发现 {head_count} 处合并冲突")

    # 简单的冲突解决策略：保留HEAD版本
    # 删除冲突标记和其他分支的内容
    patterns = [
        (r'^<{7} HEAD\s*\n', ''),  # 删除 <<<<<<< HEAD
        (r'^={7}\s*\n', ''),       # 删除 =======
        (r'^>{7} \w+\s*\n', '')    # 删除 >>>>>>> commit_hash
    ]

    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content, flags=re.MULTILINE)

    # 写入修复后的内容
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"已修复 {filename}")

if __name__ == "__main__":
    fix_merge_conflicts("benchmark_gui.py")
    print("合并冲突修复完成！")