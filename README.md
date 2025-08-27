# Nimbus — Houdini Pipeline Tool

Nimbus is a lightweight, studio‑friendly Houdini pipeline toolkit that standardizes project structure,
caching, versioning, and farm submission (HQueue/Deadline). It ships as three HDAs so artists can adopt
only what they need:

- **Nimbus** _(OBJ level)_ — Project/session manager: scene metadata, paths, and global toggles.
- **Nimbus I/O ROP** _(SOP context)_ — Cache/export operator that writes bgeo.sc, vdb, abc, usd (and Niagara/VAT).
- **ROP NimbusCache** _(/out context)_ — Render/output orchestrator with farm integration, auto‑versioning,
  and post‑cache hooks (email, flipbook to review, ShotGrid, etc.).

> This repository is set up to **work via Houdini Packages** (recommended) or the classic `$HSITE/otls` path.

---

## Quick Start

### 1) Clone
```bash
git clone https://github.com/<YOUR-ORG-OR-USER>/nimbus.git
```

### 2) Install via Houdini Package (recommended)
Copy the package file into your Houdini `packages` directory:

- Windows: `%USERPROFILE%/Documents/houdini20.5/packages`
- Linux: `~/houdini20.5/packages`
- macOS: `~/Library/Preferences/houdini/20.5/packages`

Then rename `houdini/packages/nimbus.json.example` to `nimbus.json`
and edit the `path_root` to your cloned repo path.

### 3) Alternative: HSITE deployment
Point `$HSITE` to the repo root, or copy the `houdini/` content into your central `$HSITE`.
Nimbus HDAs will be discovered in `$HSITE/otls/Nimbus/`.

---

## HDAs included (placeholders here)

- `houdini/otls/Nimbus/Nimbus.hda` (OBJ)  
- `houdini/otls/Nimbus/NimbusIO_ROP.hda` (SOP)  
- `houdini/otls/Nimbus/ROP_NimbusCache.hda` (OUT)  

> This repo ships with **placeholders** for these assets so you can wire CI/CD first.
> Replace the `.placeholder` files with your real `.hda` binaries or an `HDAdefinitions` directory.

---

## Features

- Project/shot naming presets and environment variable mapping (HIP, USD, CACHE, REVIEW)
- Auto‑versioning with `ver_list` dropdown sync
- Cache orchestration per‑ext: `bgeo.sc`, `vdb`, `abc`, `usd` (+ Niagara/VAT)
- Farm submission: HQueue + Deadline
- Post‑cache hooks: save backup `.hip`, email notify, flipbook to /review, ShotGrid upload
- SOP/ROP parameter sync and dynamic soppath resolution
- Black‑box asset option (locked HDAs, no dive‑inside)

---

## Compatibility

- Houdini: 20.0–20.5+ (tested), 21.x (WIP)
- Platforms: Windows/Linux/macOS
- Renderers: Karma/Mantra/Arnold/Redshift (pipeline‑agnostic)

---

## Folder Layout

```
nimbus/
├─ README.md
├─ LICENSE
├─ CHANGELOG.md
├─ CONTRIBUTING.md
├─ .gitignore
├─ .gitattributes
├─ .github/
│  ├─ ISSUE_TEMPLATE/bug_report.md
│  ├─ ISSUE_TEMPLATE/feature_request.md
│  └─ PULL_REQUEST_TEMPLATE.md
├─ docs/
│  ├─ install.md
│  ├─ hdas.md
│  └─ faq.md
├─ houdini/
│  ├─ packages/
│  │  └─ nimbus.json.example
│  ├─ otls/
│  │  └─ Nimbus/
│  │     ├─ Nimbus.hda.placeholder
│  │     ├─ NimbusIO_ROP.hda.placeholder
│  │     └─ ROP_NimbusCache.hda.placeholder
│  ├─ python3.10libs/
│  │  └─ nimbus/
│  │     ├─ __init__.py
│  │     ├─ hooks.py
│  │     ├─ versioning.py
│  │     ├─ hqueue_deadline.py
│  │     └─ utils.py
│  └─ toolbar/
│     └─ Nimbus.shelf
└─ examples/
   ├─ demo_project/
   │  ├─ houdini.env.example
   │  └─ README.md
   └─ scripts/
      └─ post_cache_email_example.py
```

---

## Basic Usage

1. Drop **Nimbus (OBJ)** into your scene. Set Project/Seq/Shot and base directories (USD, CACHE, REVIEW).
2. In SOPs, use **Nimbus I/O ROP** to pick your export extension. Press **Save to Disk** to cache locally
   or enable **Submit to Farm** for HQueue/Deadline.
3. In `/out`, use **ROP NimbusCache** to orchestrate multi‑stage caches and enable hooks like:
   _auto‑version → backup hip → email → flipbook → ShotGrid_.

See [`docs/hdas.md`](docs/hdas.md) for parameter mapping and examples.

---

## Contributing

PRs welcome! Please read [`CONTRIBUTING.md`](CONTRIBUTING.md).  
Use Discussions for ideas and Issues for bugs/requests.

---

## License

[MIT](LICENSE)
