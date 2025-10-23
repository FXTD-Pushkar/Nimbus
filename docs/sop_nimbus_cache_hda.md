# Nimbus Cache (SOP Level) — Cache & Export Operator

![Nimbus Cache HDA](../images/sop_nimbus_cache.png)
*The SOP-level HDA used for export/caching and version control.*

---

## 1️⃣ Purpose

**Nimbus Cache** is a SOP-level HDA designed to handle simulation and geometry caching with automatic version control, environment variable paths, and clean file naming.

Each time you trigger a cache, the tool automatically saves a backup copy of your current .hip file inside the same version directory — ensuring that every cache version is fully traceable to the exact Houdini setup used to generate it.

This makes it ideal for maintaining version-safe, reproducible simulations in both individual and small-team production workflows.

---

## 2️⃣ Quick Start

1. Drop **Nimbus Cache** in your SOP network after the node you want to cache.  
2. Pick **Extension** (e.g., `.bgeo.sc`) and set the **frame range**.  
3. Enable **Auto Versioning** (recommended), then **Save to Disk** (local) or create the **/out** ROP to send from OUT.

---

## 3️⃣ UI Reference

#### A) Naming & Paths
Parameter	Description
Name	Logical cache name used for folder and file naming.
Cache Path	Full resolved output path (read-only). Derived automatically from the OBJ Nimbus environment variables (e.g. $CACHE).
Cache Directory	Root directory for the cache files (usually $CACHE). You can browse or override this path if needed.
Extension	Defines the file format for cached output. NimbusCache supports the following export types:


  • .bgeo.sc — Standard Houdini geometry cache (fast & compressed). (Default option)
	
  • .vdb — Sparse volumetric data (smoke, fire, fog).
	
  • .abc — Alembic format for DCC interchange (e.g. Maya, Blender).
	
  • .usd — USD layer export (for Solaris or Unreal workflows).
	
  • .hbjson — Houdini Bake JSON (Niagara export for Unreal Engine).	

> Example Path
> E:/Houdini/NimbusDemo/cache/demo12/bgeo/nimbuscache/v003/nimbuscache_v003.$F4.bgeo.sc

💡 Tip:
Changing the extension automatically creates a corresponding subfolder (e.g. /bgeo/, /vdb/, /usd/) to keep cache formats organized.

---

### B) Versioning
| Control | What it does |
|---|---|
| **Auto Versioning** | Bumps to the next **major** version on save (e.g., `v003 → v004`). |
| **Version slider** | Manually preview/set a version. |
| **Latest Version** | Jumps to the highest existing version on disk. |
| **Approved Cache** | Optional flag to mark a version as approved ( visual cue for the team ). |

> **Naming reminder**  
> HIP naming uses **minor + major** (e.g., `_001_v014`). Cache versions typically track **major**: `v001`, `v002`, `v003…`.

---

### C) Caching (bgeo)
| Control | What it does |
|---|---|
| **Load from Disk** | Switches the node to read existing files instead of cooking upstream. |
| **Save to Disk** | Writes the cache now (foreground). |
| **Save to Disk in Background** | Spawns a background process; keeps the UI responsive. |
| **Cancel Cook** | Stops the current write. |
| **Evaluate As** | `Frame Range` (sequence) or a single frame. |
| **Start/End/Inc** | Cache range; defaults to scene range. |
| **Initialize Simulation OPs** | Forces a clean sim state before caching. |
| **Enable Checkpoints** | Writes intermittent frames for long sims (resume options depend on your setup). |

---

### D) Out Node (Farm Hand-off)
| Control | What it does |
|---|---|
| **Create /out node** | Builds a paired **ROP NimbusCache** in `/out` with this node wired in. |
| **ROP Node** | The created node’s path (e.g., `/out/cache_nimbuscache`). Submit from **/out** for HQueue/Deadline. |

---

### E) Load
| Control | What it does |
|---|---|
| **Object Merge This Node** | Creates an Object Merge pointing back to this cache output for easy reuse elsewhere. |

---

### F) Email Notification
| Control | What it does |
|---|---|
| **Send Email Notification** | Sends a simple “cache finished” email after completion. |
| **Email To** | Recipient(s) list. Useful for long sims or background writes. |

---

## 4️⃣ Output Examples

- Sequence:  

$CACHE/demo12/bgeo/nimbuscache/v003/nimbuscache_v003.$F4.bgeo.sc

Expands to:  

E:/Houdini/NimbusDemo/cache/demo12/bgeo/nimbuscache/v003/nimbuscache_v003.0031.bgeo.sc


- Switching to **Load from Disk** will read:  

.../v003/nimbuscache_v003.$F4.bgeo.sc


---

## 5️⃣ Best Practices

- Set **Project/Scene/Shot** on the **OBJ Nimbus** first — all paths resolve from there.  
- Keep **Auto Versioning** on; don’t overwrite previous caches.  
- Use **Background Save** for heavy sims while you continue look-dev.  
- Create the **/out** ROP when you’re ready to submit to farm (HQueue/Deadline).  
- Use **Load from Disk** after a successful cache to lock work and speed up the scene.

---

## 6️⃣ Troubleshooting

- **Path shows blank or wrong drive** → Check OBJ Nimbus and `$CACHE` variable.  
- **No files after save** → Confirm the frame range and that you’re not on **Load from Disk**.  
- **Farm cannot find files** → Ensure the cache directory is on a shared/network path visible to HQueue/Deadline workers.

---

**Next:** configure chained jobs and review hooks in the **ROP NimbusCache (OUT)** guide.






