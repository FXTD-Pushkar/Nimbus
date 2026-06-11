# ⚡ Nimbus Batch Render UI

Nimbus Batch Render is a standalone desktop utility included with Nimbus for managing Houdini cache and render jobs outside the Houdini UI.

Built around Houdini's headless execution pipeline (`hython`, `hbatch`, and `husk`), the tool provides a centralized workflow for launching, monitoring, and resuming cache or render jobs from a single interface.

Nimbus Batch Render automatically discovers supported nodes inside a HIP file and allows artists to process multiple jobs while tracking progress, reviewing logs, and recovering interrupted caches.

---

# 🚀 Key Features

- Project-aware HIP file loading
- Automatic node discovery
- Live progress tracking
- Resume interrupted cache jobs
- Detailed logging
- Multi-node execution
- USD and Husk support
- Nimbus Cache integration
- ROP NimbusCache integration
- Solaris workflow support

---

# 📦 Supported Nodes

Nimbus Batch Render can discover and execute the following node types.

## SOP Context

- Nimbus Cache
- File Cache
- File Cache 2.0

## /out Context

- ROP NimbusCache
- Geometry ROP
- Alembic ROP
- USD ROP
- USD Render ROP
- Karma ROP

## Solaris

- LOP ROP Nodes
- USD Export Nodes
- Render Nodes

## Other

- Nested ROP Networks
- ROP Networks inside Geometry Objects

---

# 🚀 First-Time Setup

Perform this setup once per machine.

## Requirements

- Nimbus installed
- Houdini installed
- NIMBUS_ROOT configured
- Nimbus Batch Render installed

Folder structure:

```text
Nimbus/
│
├── H20_5/
│   ├── menus/
│   ├── otls/
│   └── scripts/
│
├── H21_0/
│   ├── menus/
│   ├── otls/
│   └── scripts/
│
└── Nimbus_Houdini_Batch_Render/
    ├── run_batchui.bat
    └── scripts/
        └── python/
```

## Launch

Run:

```text
run_batchui.bat
```

The Batch Render UI should open successfully.

> Tip:
>
> Houdini does not need to be running.
>
> Closing Houdini before launching Batch Render frees RAM and CPU resources for heavy simulations and rendering jobs.

---

# 🌙 Usage 1: Cache a Shot Overnight

## When to Use

Your FX setup is complete and you want to generate caches overnight.

## Steps

1. Launch Batch Render.
2. Select:
   - Project
   - Scene
   - HIP File
3. Click **Load HIP**.
4. Select the desired Nimbus Cache node.
5. Click **Render Selected**.

## Result

The cache begins processing immediately.

The UI displays:

- Current Frame
- Total Frames
- Progress Percentage
- Cache Size
- Status
- Log Output

When complete:

```text
Status: Completed
Progress: 100%
```

---

# 📦 Usage 2: Cache Multiple Nodes from a Single HIP

## When to Use

A HIP file contains multiple cache nodes such as:

- Smoke
- Fire
- Dust
- Debris
- Whitewater
- Rigid Bodies

## Steps

1. Load the HIP file.
2. Select multiple cache nodes.
3. Click **Render Selected**.

## Notes

Selected nodes execute in the order displayed within the UI.

Use the node filter to focus on a specific network.

Examples:

```text
/obj/fx
/obj/geo1
/obj/geo1/ropnet1
```

This helps simplify large production scenes.

---

# 🔄 Usage 3: Resume After Stop or Crash

## When to Use

A cache job was interrupted before completion.

Example:

```text
Frame 87 of 240
```

## Steps

1. Load the same HIP file.
2. Select the same cache node.
3. Click **Render Selected**.

## Result

Nimbus detects existing cache files and resumes automatically from:

```text
Frame 88
```

instead of restarting from frame 1.

Progress calculations include frames already written to disk.

> Important:
>
> Do not increase the cache version if you want to continue writing into the existing cache folder.

---

# ⚙️ Usage 4: ROP NimbusCache in /out

## When to Use

Cache jobs are driven through the `/out` context.

## Steps

1. Load the HIP file.
2. Select a `rop_nimbuscache` node.
3. Click **Render Selected**.

## Benefits

- Progress tracking
- Resume support
- Detailed logging
- Local validation before farm submission

This workflow is ideal for artists who prefer managing cache exports through `/out`.

---

# 🌳 Usage 5: Nested ROP Networks

## When to Use

ROP networks exist inside Geometry Objects.

Example:

```text
/obj/geo1/ropnet1
```

## Steps

1. Load the HIP file.
2. Expand the context tree.
3. Select the desired child ROP.
4. Click **Render Selected**.

Nimbus automatically scans nested ROP networks and displays them in the UI.

No additional configuration is required.

---

# 📁 Usage 6: Geometry and Alembic Exports

## When to Use

Exporting geometry caches from `/out`.

## Supported Nodes

- Geometry ROP
- Alembic ROP

## Steps

1. Load the HIP file.
2. Select the export node.
3. Click **Render Selected**.

The export is processed using Houdini's headless execution pipeline.

---

# 🌐 Usage 7: USD and Karma Rendering with Husk

## When to Use

Rendering USD workflows using Husk.

## Requirements

A valid USD file must already exist on disk.

## Steps

1. Enable:

```text
Prefer husk for USD ROPs
```

2. Select the USD or Karma render node.
3. Click **Render Selected**.

## Recommended For

- USD Render ROP
- Karma Render ROP

## Notes

Disable the Husk option if you want the render to use standard `hbatch` execution instead.

This option is intended for rendering USD-based workflows and is not required for SOP-level cache exports.

---

# ☀️ Usage 8: Solaris Workflows

## When to Use

Working inside Solaris (`/stage`).

## Steps

1. Load the HIP file.
2. Select the Solaris output node.

Example:

```text
/stage/usd_rop1
```

3. Click **Render Selected**.

Nimbus automatically detects supported Solaris output nodes.

Supported workflows include:

- USD Export
- Karma Render
- Solaris Render Pipelines

---

# 📊 Usage 9: Monitor Long Running Jobs

## When to Use

Large simulations or render jobs that may take several hours.

## Features

Select a node to view:

- Current Frame
- Total Frames
- Progress Percentage
- Cache Size
- Disk Usage
- Status
- Runtime Information
- Detailed Logs

All information updates in real time while the job is running.

This makes it easier to monitor overnight simulations and long-running render jobs.

---

# 📝 Logging

Nimbus Batch Render provides detailed logging for every job.

Log output includes:

- Frame Writes
- Cache Completion Messages
- Warnings
- Errors
- Husk Output
- HBatch Output
- Status Updates

Warnings and errors are highlighted for faster troubleshooting.

The log window is designed to help artists quickly identify failed frames, missing files, or configuration issues.

---

# 💡 Recommended Workflow

```text
Build FX
   ↓
Nimbus Cache
   ↓
Nimbus Batch Render
   ↓
Validate Output
   ↓
Farm Submission
```

This workflow allows artists to generate, monitor, resume, and validate cache or render jobs efficiently before sending work to HQueue, Deadline, Tractor, or other farm systems.

---

# 📌 Notes

- Houdini does not need to be open.
- Multiple cache nodes can be processed from a single HIP file.
- Existing cache files are detected automatically.
- Resume functionality works with Nimbus Cache and supported cache workflows.
- Batch Render is designed for local execution and pre-flight validation before farm submission.
- Large scenes benefit from running Batch Render independently from the main Houdini session.
- Progress calculations include existing cache files when resuming interrupted jobs.
