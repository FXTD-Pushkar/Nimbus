# Nimbus — Houdini Pipeline Tool

**Nimbus** is a lightweight, artist-friendly Houdini pipeline toolkit that helps organize projects, manage cache versions, and submit simulations or renders to farm (HQueue or Deadline).

It includes three HDAs you can use separately or together:

- **Nimbus (OBJ level)** – Project and shot manager  
- **Nimbus Cache (SOP level)** – Exports caches like `.bgeo.sc`, `.vdb`, `.abc`, `.usd`, or Niagara
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

- Project/shot naming presets and environment variable mapping (HIP, USD, CACHE, REVIEW)
- Auto‑versioning with `ver_list` dropdown sync
- Cache orchestration per‑ext: `bgeo.sc`, `vdb`, `abc`, `usd` (+ Niagara)
- Farm submission: HQueue + Deadline
- Post‑cache hooks: save backup `.hip`, email notify, flipbook to /review
- SOP/ROP parameter sync and dynamic soppath resolution


---

## 💡 Basic Usage

1. **Add Nimbus (OBJ)** → Set your project, sequence, and shot folders.  
2. **Use Nimbus Cache (SOP)** → Choose export format and click **Save to Disk**   
3. **Use ROP NimbusCache (OUT)** → Combine multiple caches, manage versions, and **Submit to Farm**.
4. **Flipbook** → Use the flipbook UI. Nimbus saves an image sequence and, if FFmpeg is available, makes an .mp4.
🎬 FFmpeg for MP4 export

Nimbus calls FFmpeg like this:
```
ffmpeg -y -framerate <fps> -start_number <firstFrame> -i <sequence> \
  -vf scale=<evenW>:<evenH>:flags=lanczos,format=yuv420p \
  -c:v libx264 -preset medium -crf 18 <output>.mp4
```
I ensure even dimensions and yuv420p for broad player compatibility.<br>
Encoder is libx264 (H.264). Any recent FFmpeg with x264 works.

####How Nimbus finds FFmpeg
  If environment variable FFMPEG is set, Nimbus uses that path (recommended):
```
# houdini.env
FFMPEG="C:/ffmpeg/bin/ffmpeg.exe"
```
Otherwise Nimbus tries the command ffmpeg on your system PATH.

---

## 🧩 Compatibility

- **Houdini:** 20.0, 20.5, 21.x (tested)  
- **OS:** Windows (tested), Linux/macOS
- **Farm:** HQueue, Deadline  
 

---

## 📁 Folder Layout

```
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

Example paths:
Documents/houdini21.0/otls
Documents/houdini21.0/scripts/python/nimbus
```






---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
Use **Issues** for bug reports or new feature ideas.

---

## 📜 License

Released under the [MIT License](LICENSE)



