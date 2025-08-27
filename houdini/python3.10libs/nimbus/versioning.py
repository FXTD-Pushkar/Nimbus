# Copyright (c) 2025 Pushkar Deshpandey
# Licensed under the MIT License. See LICENSE for details.

import os, re, glob, hou

def _find_versions(base, name, ext_subdir):
    pattern = os.path.join(base, ext_subdir, name, "v[0-9][0-9][0-9]")
    return sorted(glob.glob(pattern))

def next_version(base, name, ext_subdir):
    vers = _find_versions(base, name, ext_subdir)
    if not vers:
        return 1
    last = vers[-1].split("v")[-1]
    try:
        return int(last) + 1
    except Exception:
        return 1
