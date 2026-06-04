"""
rop_nimbus_cache package - Stable API for NimbusCache ROP HDA.

This package provides all the functions needed for the NimbusCache ROP HDA
while maintaining backward compatibility with existing callbacks and scripts.
"""

# Import core functions
from .core import (
    sync_from_nimbus,
    sync_rop_version_from_dropdown,
    latest_version_button,
    version_up,
    version_up1,
    push_version_to_sop,
    resolve_soppath,
    update_soppath,
    get_rop_version_list,
    initcolour,
    switch_index_from_sop,
)

# Import operations functions
from .ops import (
    prerender_prepare,
    preframe_autoversion_for_child,
    postrender_sync_menu,
    save_cache_hip_postrender,
)

# Import utility functions (for internal use)
from .util import (
    _eval_str,
    _sync_version_menu,
    _force_frame_range,
    _refresh_paths_and_dirs,
    _pair_list,
    _get_scene,
    _get_sop_from_hda,
    _detect_ext,
    _get_cache_name,
    _cache_version,
    _highest_saved_version,
)

# Import constants
from .const import (
    EXT_TO_SUBDIR,
    VERSION_RX,
    EXT_TO_SWITCH_INDEX,
)

# Package version
__version__ = "1.0.0"

# Expose all public functions for direct import
__all__ = [
    # Core functions
    "sync_from_nimbus",
    "sync_rop_version_from_dropdown", 
    "latest_version_button",
    "version_up",
    "version_up1",
    "push_version_to_sop",
    "resolve_soppath",
    "update_soppath",
    "get_rop_version_list",
    "initcolour",
    "switch_index_from_sop",
    
    # Operations functions
    "prerender_prepare",
    "preframe_autoversion_for_child",
    "postrender_sync_menu",
    "save_cache_hip_postrender",
    
    # Constants
    "EXT_TO_SUBDIR",
    "VERSION_RX", 
    "EXT_TO_SWITCH_INDEX",
]
