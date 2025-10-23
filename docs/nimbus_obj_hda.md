# Nimbus (OBJ Level) — Project & Shot Manager

![Nimbus OBJ HDA](../images/obj_nimbus.png)
*Example: Nimbus node interface inside `/obj` level.*

---

## 🎯 Purpose

The **Nimbus (OBJ)** HDA is the core project manager.  
It helps artists define and manage the project structure, environment variables, and scene metadata.  
All Nimbus tools — like **Nimbus Cache (SOP)** and **ROP NimbusCache (OUT)** — read from the paths and project info set here.

---

## 🧭 Main Sections

---

### 🔹 1️⃣ Project Details

| **Parameter** | **Description** |
|----------------|-----------------|
| **Project / Scene / Shot** | Defines your project structure. The **Scene** field doesn’t strictly mean *sequence* — it can represent anything like a sequence, element, or FX category (e.g. `fire`, `destruction`, `water_interaction`).<br><br>**Example:** `Project = NimbusDemo`, `Scene = Fire`, `Shot = SH010` |
| **Enable Shot** | Enables shot-level folder creation. When disabled, caching and review folders are generated only at the scene level (useful for standalone FX or lookdev). |
| **Comment** | Optional text note for internal tracking or quick identification of tasks. |
| **Artist / Department** | Auto-filled or editable fields used for tagging caches, flipbooks, and renders. |
| **Project Details (📄)** | Opens the main project directory in your file browser to verify paths. |

---

### 🧩 2️⃣ File Controls

| **Control** | **Description** |
|--------------|-----------------|
| **Empty hip_file** | Displays the currently active HIP file. If no file is saved yet, the dropdown shows an empty entry. Once a versioned file is saved, it appears in the `ver_list` dropdown for easy access. |
| **Save / Version Up** | Saves the current `.hip` file in the project’s HIP directory and updates the version naming.<br><br>**Example:** `NimbusDemo_001_v001.hip` → where `001` = **minor version** and `v001` = **major version**. |
| **Version Up (Minor)** | Increments only the **minor** version part (`001` → `002`), keeping the **major** version (`v001`) the same.<br><br>**Example:** `NimbusDemo_001_v001.hip` → `NimbusDemo_002_v001.hip`. Useful for internal WIP saves before major publishes. |

---

### 📂 3️⃣ Directory Paths

| **Path** | **Description** |
|-----------|----------------|
| **Assets / Cache / USD / Flipbook / Render** | Auto-generated environment paths based on your project name and scene setup. Each path follows your base directory structure and can be accessed using Houdini’s environment variables. |
| **Example Syntax:** | `E:/Houdini/NimbusDemo/cache`<br><br>• `E:/Houdini` → Base directory where all projects are stored.<br>• `NimbusDemo` → Current project name (can be any project).<br>• `cache` → Folder where `.bgeo`, `.vdb`, `.abc`, or `.usd` files are saved. |
| **Folder Icon** | Opens the corresponding folder directly in your file browser for quick navigation. |

---


---

### 4️⃣ Flipbook Section
| Parameter | Description |
|------------|-------------|
| **Cook Flipbook** | Renders a quick scene preview using the selected camera. |
| **Valid Frame Range** | Uses global frame range or custom override. |
| **Camera Path** | Choose the render camera (default: `/obj/cam1`). |
| **Override Camera Resolution** | Enables custom resolution for the flipbook. |
| **Flipbook Path / MP4 Path** | Displays where flipbook images and MP4 previews will be saved. |
| **Available Flipbook** | Lists all flipbooks saved for the shot. |
| **Play / Delete Flipbook** | Open or remove existing flipbook renders. |

---

## 💡 Tips

- Always set **Project** and **Shot** first — all cache, USD, and review paths depend on it.  
- Use **Version Up** before starting any simulation or render — this keeps versions clean and traceable.  
- The **Flipbook** tool automatically stores outputs in `$REVIEW`.  
- Folder icons are shortcuts — they open cache or flipbook directories instantly.  

---

## 🧾 Example Folder Structure

