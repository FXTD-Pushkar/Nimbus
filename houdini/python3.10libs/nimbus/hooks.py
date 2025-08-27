# Copyright (c) 2025 Pushkar Deshpandey
# Licensed under the MIT License. See LICENSE for details.

import os, shutil, hou

def backup_hip(target_dir):
    try:
        hip = hou.hipFile.path()
        os.makedirs(target_dir, exist_ok=True)
        dst = os.path.join(target_dir, os.path.basename(hip))
        shutil.copy2(hip, dst)
        print(f"[Nimbus] Saved HIP copy to {dst}")
    except Exception as e:
        print(f"[Nimbus] backup_hip error: {e}")

def post_cache_email(to_addr, subject, body):
    # Placeholder stub for studio integration
    print(f"[Nimbus] Email → {to_addr}: {subject}")
