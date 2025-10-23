# Nimbus — Houdini Pipeline Tool

**Nimbus** is a lightweight, artist-friendly Houdini pipeline toolkit that helps organize projects, manage cache versions, and submit simulations or renders to farm (HQueue or Deadline).

It includes three HDAs you can use separately or together:

- **Nimbus (OBJ level)** – Project and shot manager  
- **Nimbus Cache (SOP level)** – Exports caches like `.bgeo.sc`, `.vdb`, `.abc`, `.usd`, or Niagara/VAT  
- **ROP NimbusCache (OUT level)** – Handles multi-stage caching, auto-versioning, and post-cache tasks (email, flipbook, ShotGrid, etc.)

---

## 🧭 Installation

1. **Download** the repository or ZIP file from GitHub.  
2. Copy the HDA files to your Houdini **otls** folder:   Documents/houdini21.0/otls
3. Copy all Python script files to:   Documents/houdini21.0/scripts/python/nimbus

4. Restart Houdini — Nimbus tools will now appear in the TAB menu.

---

## 📦 HDAs Included

| File | Context | Description |
|------|----------|-------------|
| **object_Nimbus.1.0.hdalc** | OBJ | Project and shot manager |
| **sop_nimbus_cache.1.0.hdalc** | SOP | Cache/export operator |
| **driver_ROP_NimbusCache.1.0.hdalc** | OUT | Multi-stage cache + farm integration |

---

## ⚙️ Key Features

- Simple project and shot setup  
- Automatic folder creation and versioning  
- Export multiple formats: `.bgeo.sc`, `.vdb`, `.abc`, `.usd`, Niagara/VAT  
- Farm submission (HQueue + Deadline)  
- Post-cache hooks: save `.hip`, email notify, flipbook to `/review`  
- Works with any renderer (Karma, Arnold, Mantra, Redshift)

---

## 💡 Basic Usage

1. **Add Nimbus (OBJ)** → Set your project, sequence, and shot folders.  
2. **Use Nimbus Cache (SOP)** → Choose export format and click **Save to Disk**   
3. **Use ROP NimbusCache (OUT)** → Combine multiple caches, manage versions, and **Submit to Farm**.

---

## 🧩 Compatibility

- **Houdini:** 20.0, 20.5, 21.x (tested)  
- **OS:** Windows (tested), Linux/macOS (coming soon)  
- **Farm:** HQueue, Deadline  
- **Renderers:** Karma, Mantra, Arnold, Redshift  

---

## 📁 Folder Layout

Documents/
└─ houdiniXX.X/        ← your Houdini version (e.g. houdini21.0)
   ├─ otls/
   │  ├─ object_Nimbus.1.0.hdalc
   │  ├─ sop_nimbus_cache.1.0.hdalc
   │  └─ driver_ROP_NimbusCache.1.0.hdalc
   └─ scripts/
      └─ python/
         └─ nimbus/
            ├─ versioning.py
            ├─ hooks.py
            ├─ hqueue_deadline.py
            ├─ utils.py
            └─ email_notify.py

Documents/houdini21.0/otls
Documents/houdini21.0/scripts/python/nimbus


---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
Use **Issues** for bug reports or new feature ideas.

---

## 📜 License

Released under the [MIT License](LICENSE)



