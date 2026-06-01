# Nimbus — Houdini Pipeline Tool

**Nimbus** is a lightweight, artist-friendly Houdini pipeline toolkit for organizing projects, managing cache versions, rendering flipbooks, and submitting work to **HQueue** or **Deadline**.

**Repository:** https://github.com/FXTD-Pushkar/Nimbus

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
| **21.0** | `C:\Users\<USERNAME>\Documents\houdini21.0\packages\nimbus.json` |
| **20.5** | `C:\Users\<USERNAME>\Documents\houdini20.5\packages\nimbus.json` |

Paths vary by user, for example:

- `C:\Users\artist01\Documents\houdini21.0\packages\nimbus.json`
- `C:\Users\artist01\OneDrive\Documents\houdini21.0\packages\nimbus.json`

On **Linux / macOS**, use the matching folder under your home directory, for example:

- `~/houdini21.0/packages/nimbus.json`
- `~/Library/Preferences/houdini/21.0/packages/nimbus.json` (macOS — layout may vary by build)

Create the **`packages`** folder if it does not exist.

---

### 3. What to put in `nimbus.json`

Set **`NIMBUS_ROOT`** to the full path of the **version subfolder** (`H20_5` or `H21_0`) on disk — wherever you installed Nimbus. Only this value is install-specific; the other entries use `$NIMBUS_ROOT`.

#### Houdini 20.5

**File:** `Documents/houdini20.5/packages/nimbus.json`

```json
{
    "env": [
        { "NIMBUS_ROOT": "D:/Pipeline/Nimbus/H20_5" },
        { "PYTHONPATH": "$NIMBUS_ROOT/scripts/python;&" },
        { "HOUDINI_OTLSCAN_PATH": "$NIMBUS_ROOT/otls;&" },
        { "HOUDINI_MENU_PATH": "$NIMBUS_ROOT/menus;&" }
    ]
}
```

#### Houdini 21.0

**File:** `Documents/houdini21.0/packages/nimbus.json`

```json
{
    "env": [
        { "NIMBUS_ROOT": "D:/Pipeline/Nimbus/H21_0" },
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

## 💡 Basic Workflow

### 1. Create a project

Create a **Nimbus** node in OBJ context.

Configure **Project**, **Sequence**, and **Shot**. Nimbus builds the folder structure and sets environment variables automatically.

Project registry:

```
{HOME}/NimbusProjects/projects.json
```

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
