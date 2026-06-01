"""
nimbuscache - Houdini Caching and Automation Package

A modular package for managing cache versioning, paths, notifications, and approval
workflows in Houdini FX pipelines.

This package provides:
- Automated version management with intelligent path detection
- Email notifications for cache completion
- Cache approval and version tracking
- Support for multiple cache formats (bgeo, vdb, abc, usd, hbjson)
- Integration with Houdini ROP networks

Public API Functions:
- cache_dir() - Get the cache directory path
- cache_path(mode='path') - Build cache file paths
- auto_version(node, forced=False) - Auto-increment versions
- latest_version(kwargs) - Get latest cached version
- get_rop_version_list() - Generate version dropdown menu items
- email_notify_bg() - Send BGEO/VDB/ABC cache notification
- email_notify_bg_usd() - Send USD cache notification
- initcolour(self) - Initialize node color
- pre_cache_check(hda) - Validate cache settings
- save_cache_start_time(node) - Record cache start time
- approve_selected_version(kwargs) - Approve a cache version
- check_last_cached_frame() - Find last valid cached frame
- open_cache() - Open cache directory in file explorer
- open_usd() - Open USD directory in file explorer
"""

__version__ = "1.0.0"

# Import and expose public API functions
from .core import (
    cache_dir,
    cache_path,
    auto_version,
    latest_version,
    latest_version_usd,
    get_rop_version_list,
    get_usd_version_list,
    update_version_on_ext_change,
    on_version_change,
    on_ver_list_change,
    on_ver_list_usd_change,
    update_usd_version,
)


from .ops import (
    initcolour,
    get_ext_index,
    set_dop_checkpoint_path,
    check_last_cached_frame,
    create_usdimport_from_cache_path,
    create_object_merge_to_nimbus,
    save_hip_to_version_folder,
    start_background_cache,
    notify_background_cache_done,
    prerender,
    preframe,
    postframe,
    postwrite,
    postrender,
    wait_and_save_hip,
    open_directory,
    open_asset,
    open_cache,
    open_usd,
    create_rop_nimbuscache,
)

from .notify import (
    email_notify_bg,
    email_notify_bg_usd,
    pre_cache_check,
    save_cache_start_time,
)

from .approve import (
    approve_selected_version,
)

__all__ = [
    # Version
    "__version__",
    
    # Core functions
    "cache_dir",
    "cache_path",
    "auto_version",
    "latest_version",
    "latest_version_usd",
    "get_rop_version_list",
    "get_usd_version_list",
    "update_version_on_ext_change",
    "on_version_change",
    "on_ver_list_change",
    "on_ver_list_usd_change",
    "update_usd_version",
    
    # Operations
    "initcolour",
    "get_ext_index",
    "set_dop_checkpoint_path",
    "check_last_cached_frame",
    "create_usdimport_from_cache_path",
    "create_object_merge_to_nimbus",
    "save_hip_to_version_folder",
    "start_background_cache",
    "notify_background_cache_done",
    "prerender",
    "preframe",
    "postframe",
    "postwrite",
    "postrender",
    "wait_and_save_hip",
    "open_directory",
    "open_asset",
    "open_cache",
    "open_usd",
    "create_rop_nimbuscache",
    
    # Notifications
    "email_notify_bg",
    "email_notify_bg_usd",
    "pre_cache_check",
    "save_cache_start_time",
    
    # Approval
    "approve_selected_version",
]
