# Copyright (c) 2025 Pushkar Deshpandey
# Licensed under the MIT License. See LICENSE for details.

def safe_eval_parm(node, name, default=None):
    p = node.parm(name)
    try:
        return p.eval() if p else default
    except Exception:
        return default
