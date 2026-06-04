# Nimbus — Houdini Pipeline Tool

**Nimbus** is a lightweight, artist-friendly Houdini pipeline toolkit for organizing projects, managing cache versions, rendering flipbooks, and submitting work to **HQueue** or **Deadline**.

**Repository:** https://github.com/FXTD-Pushkar/Nimbus

**Video Documentation (obj HDA):** https://www.youtube.com/playlist?list=PL4Pe_U0h-1m0u5-azS7nnViXO0EHMzuJ0

---

## ⚠️ License Compatibility

Nimbus is currently distributed as Houdini Indie (`.hdalc`) assets.

A Houdini Indie license is required to use the included HDAs.

---


## ✨ Features

### 📁 Project Management
- Project, sequence, and shot setup
- Automatic environment variable management
- Consistent folder structure generation

### 📦 Cache Management
- Auto versioning
- Version dropdown sync
- Approved cache system
- Cache browser and Cache Manager

### 🎞️ Flipbook Workflow
- Image sequence rendering
- Automatic MP4 generation
- FFmpeg integration
- Versioned review output

### 🚜 Farm Integration
- HQueue support
- Deadline support
- Multi-stage dependency workflows

### 🛠 Utilities
- Save Version
- Save Minor Version
- Hip File Browser
- Cache Manager
- VEX Snippet Manager
- Batch Render Tool

---

## 📦 Included HDAs

| HDA | Context | Description |
|-----|---------|-------------|
| **Nimbus** | OBJ | Project & shot manager |
| **Nimbus Cache** | SOP | Cache export and versioning |
| **ROP NimbusCache** | OUT | Dependency management & farm submission |

| File | Context |
|------|---------|
| `object_Nimbus.1.0.hdalc` | OBJ |
| `sop_nimbus_cache.1.0.hdalc` | SOP |
| `driver_ROP_NimbusCache.1.0.hdalc` | OUT |

---

## 🚀 Installation

Nimbus uses **Houdini Packages**. Install Nimbus on disk once, then each user adds a small **`nimbus.json`** in their own Houdini preferences folder.

### 1. Install Nimbus (any location)

Clone or extract the repository to **any path you prefer** (local drive, studio server, etc.):

| Platform | Example paths |
|----------|----------------|
| **Windows** | `D:/Pipeline/Nimbus`, `C:/Tools/Nimbus` |
| **Linux** | `/opt/nimbus`, `/home/you/tools/Nimbus` |
| **macOS** | `/Users/you/Tools/Nimbus` |
| **Studio / farm** | `P:/Pipeline/Nimbus`, `//server/pipeline/Nimbus` |

Use forward slashes in `nimbus.json` (Houdini accepts them on Windows).

**Folder structure** inside your chosen root:

```
<your-chosen-path>/Nimbus/
│
├── H20_5/          ← Houdini 20.5
│   ├── menus/
│   ├── otls/
│   └── scripts/
│
└── H21_0/          ← Houdini 21.0
    ├── menus/
    ├── otls/
    └── scripts/
```

Use only the subfolder for the Houdini version(s) you run.

---

### 2. Create `nimbus.json` (per user, per Houdini version)

**Do not commit user-specific paths.** Each artist creates this file on their own machine.

#### Where to save it

Houdini loads packages from:

```
<HOUDINI_USER_PREF_DIR>/packages/nimbus.json
```

`HOUDINI_USER_PREF_DIR` is **different for every user** (username, OneDrive, OS, Houdini version).

| Houdini | Typical location (Windows) |
|---------|----------------------------|
| **21.0** | `C:\Users\<USERNAME>\Documents\houdini21.0\packages\nimbus_h20.5.json` |
| **20.5** | `C:\Users\<USERNAME>\Documents\houdini20.5\packages\nimbus_h21.0.json` |

Paths vary by user, for example:

- `C:\Users\artist01\Documents\houdini21.0\packages\nimbus_h20.5.json`
- `C:\Users\artist01\OneDrive\Documents\houdini21.0\packages\nimbus_h21.0.json`

On **Linux / macOS**, use the matching folder under your home directory, for example:

- `~/houdini21.0/packages/nimbus_h21.0.json`
- `~/Library/Preferences/houdini/21.0/packages/nimbus_h21.0.json` (macOS — layout may vary by build)

Create the **`packages`** folder if it does not exist.

---

### 3. What to put in `nimbus.json`

Set **`NIMBUS_ROOT`** to the full path of the **version subfolder** (`H20_5` or `H21_0`) on disk — wherever you installed Nimbus. Only this value is install-specific; the other entries use `$NIMBUS_ROOT`.

#### Houdini 20.5

**File:** `Documents/houdini20.5/packages/nimbus_h20.5.json`

```json
{
    "env": [
        { "NIMBUS_ROOT": "D:/Nimbus/H20_5" },
        { "PYTHONPATH": "$NIMBUS_ROOT/scripts/python;&" },
        { "HOUDINI_OTLSCAN_PATH": "$NIMBUS_ROOT/otls;&" },
        { "HOUDINI_MENU_PATH": "$NIMBUS_ROOT/menus;&" }
    ]
}
```

#### Houdini 21.0

**File:** `Documents/houdini21.0/packages/nimbus_h21.0.json`

```json
{
    "env": [
        { "NIMBUS_ROOT": "D:/Nimbus/H21_0" },
        { "PYTHONPATH": "$NIMBUS_ROOT/scripts/python;&" },
        { "HOUDINI_OTLSCAN_PATH": "$NIMBUS_ROOT/otls;&" },
        { "HOUDINI_MENU_PATH": "$NIMBUS_ROOT/menus;&" }
    ]
}
```

| Setting | Meaning |
|---------|---------|
| **`nimbus.json` location** | Each user's **Documents → houdiniXX.X → packages** |
| **`NIMBUS_ROOT`** | Where Nimbus is installed (`.../H20_5` or `.../H21_0`) |

---

### 4. Restart Houdini

Packages load at startup. Restart Houdini after creating or editing `nimbus.json`.

---

## 🧭 Nimbus Menu

Nimbus adds a dedicated menu inside Houdini.

| Tool | Description |
|------|-------------|
| **Hip Open** | Open project and shot files quickly |
| **Save Version** | Create the next major scene version |
| **Save Minor Version** | Create minor revisions |
| **Nimbus Cache Manager** | Browse, refresh, approve, or delete cache versions |
| **VEX Snippet Manager** | Store and manage reusable VEX snippets |
| **Render Flipbook** | Image sequence + MP4 preview |

---

## 📁 Project Directory & Environment Variables

When you **select a project** from the Nimbus node (and set your scene / shot), Nimbus automatically:

1. Creates a standard folder layout under the project root  
2. Sets Houdini **global variables** (visible in **Edit → Aliases and Variables → Variables**)

The project root can be **any path you choose** when creating the project (local drive, server, etc.). Nimbus does not require a fixed drive or folder name.

### Example layout

If your project is saved at `D:/Houdini/NimbusDemo`, Nimbus configures:

```
D:/Houdini/NimbusDemo/          ← $JOB   (project root)
├── assets/                       ← $ASSET
├── cache/                        ← $CACHE
├── flipbook/                     ← $FLIPBOOK
├── hip/                          ← $HIP
│   └── <scene_name>/             ← per-shot folder (from Nimbus scene setting)
│       └── untitled.hiplc        ← $HIPFILE (initial scene file)
├── render/                       ← $RENDER
└── usd/                          ← $USD
```

### Environment variables set by Nimbus

| Variable | Points to | Purpose |
|----------|-----------|---------|
| **`$JOB`** | Project root | Main project directory |
| **`$HIP`** | `<project>/hip` | Scene / hip save location |
| **`$HIPFILE`** | `<project>/hip/<scene>/untitled.hiplc` | Current hip file path |
| **`$ASSET`** | `<project>/assets` | Assets |
| **`$CACHE`** | `<project>/cache` | Simulation / geometry caches |
| **`$FLIPBOOK`** | `<project>/flipbook` | Flipbook image sequences & reviews |
| **`$RENDER`** | `<project>/render` | Render output |
| **`$USD`** | `<project>/usd` | USD exports |

**Example values** (project at `D:/Houdini/PipelineTest`, scene `shot01`):

| Variable | Example value |
|----------|----------------|
| `JOB` | `D:/Houdini/NimbusDemo` |
| `ASSET` | `D:/Houdini/NimbusDemo/assets` |
| `CACHE` | `D:/Houdini/NimbusDemo/cache` |
| `FLIPBOOK` | `D:/Houdini/NimbusDemo/flipbook` |
| `HIP` | `D:/Houdini/NimbusDemo/hip` |
| `RENDER` | `D:/Houdini/NimbusDemo/render` |
| `USD` | `D:/Houdini/NimbusDemo/usd` |
| `HIPFILE` | `D:/Houdini/NimbusDemo/hip/shot01/untitled.hiplc` |

These variables are used across Nimbus tools (cache paths, flipbook output, farm submission, open-folder buttons, etc.).

### Project registry

All projects are stored in a single JSON file (per machine / user):

```
{HOME}/NimbusProjects/projects.json
```

Each entry stores the project **name**, **path**, and **FPS**. Selecting a project in the Nimbus HDA reloads that path and reapplies the folder structure and variables above.

---

## 💡 Basic Workflow

### 1. Create or select a project

Create a **Nimbus** node in OBJ context.

- **Add Project** — create a new project folder or register an existing one (pick any base directory you want)  
- **Project** dropdown — select a registered project  
- Set **Sequence**, **Shot**, and **Scene** as needed  

Nimbus applies the directory layout and environment variables described above automatically.

### 2. Create caches

Create a **Nimbus Cache** node.

**Supported formats:** BGEO, VDB, Alembic, USD, Niagara

Use **Save to Disk** or **Save to Disk in Background**.

### 3. Submit to farm

Create a **ROP NimbusCache** node to:

- Connect multiple cache stages
- Manage dependencies
- Submit to HQueue
- Submit to Deadline

### 4. Generate reviews

Launch **Nimbus → Render Flipbook**.

Outputs:

- Image sequence
- MP4 review file

---

## 🎞️ FFmpeg Setup

Nimbus uses FFmpeg to generate MP4 previews from image sequences.

1. Install FFmpeg.
2. Add its `bin` folder to your system **PATH** (install location varies).
3. Restart Houdini.

**Verify:**

```bash
ffmpeg -version
```

If FFmpeg is installed correctly, version information will be displayed. Nimbus detects FFmpeg from the system PATH automatically.

---

## ⚙️ Batch Render Tool

Nimbus includes a standalone **Batch Render Tool**.

**Features:**

- Load HIP files
- Discover Nimbus Cache nodes
- Execute multiple cache stages
- Auto versioning
- USD Husk support
- Background processing

**Ideal for:**

- Overnight caching
- Batch rendering
- Farm preflight testing

---

## 🚜 Farm Setup

For production, install Nimbus on a **shared path every worker can read**, for example:

```
P:/Pipeline/Nimbus/H21_0
```

```
//server/pipeline/Nimbus/H21_0
```

```
/opt/pipeline/nimbus/H21_0
```

Point each machine's `nimbus.json` **`NIMBUS_ROOT`** at that same shared version folder.

**Workers need access to:**

- HDAs (`$NIMBUS_ROOT/otls`)
- Python (`$NIMBUS_ROOT/scripts/python`)
- Project and cache locations defined by your Nimbus project

**Menu files** (`menus/`) are typically only required on artist workstations, not on headless farm blades.

Avoid pointing farm workers at a path only available on one artist's machine (personal drive or home folder).

---

## 🔍 Verification

In the Houdini **Python Source Editor**:

```python
import hou
print(hou.getenv("HOUDINI_USER_PREF_DIR"))
print(hou.getenv("NIMBUS_ROOT"))
```

```python
import nimbus_cache
import rop_nimbus_cache

print("Nimbus OK")
```

- **First block:** confirms your personal packages folder and `NIMBUS_ROOT`.
- **Second block:** confirms Python modules load.

---

## 🧩 Compatibility

| Component | Supported |
|-----------|-----------|
| Houdini 20.5 | ✅ |
| Houdini 21.0 | ✅ |
| Windows | ✅ |
| Linux | ✅ |
| HQueue | ✅ |
| Deadline | ✅ |

---

## 🤝 Contributing

Pull requests and suggestions are welcome. Use **Issues** for bug reports and feature ideas.

---

## 📜 License

Released under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Pushkar Deshpandey**  
FX Technical Director • Houdini Pipeline TD • Senior FX Artist
