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

### 1️⃣ Project Details
| Parameter | Description |
|------------|-------------|
| **Project / Scene / Shot** | Define your show structure. Example: `Project = Demo`, `Scene = SQ010`, `Shot = SH030`. |
| **Enable Shot** | Enables shot-level folder creation. |
| **Comment** | Optional short description or note. |
| **Artist / Department** | Auto-filled or manually entered; used for tagging cache and render data. |
| **Project Details (📄)** | Opens your project path in the system file explorer. |

---

### 2️⃣ File Controls
| Control | Description |
|----------|-------------|
| **Empty hip_file** | Creates an empty `.hip` file under your current project folder. |
| **Save / Version Up** | Saves the current scene in your project’s `HIP` directory with proper versioning. |
| **Version Up (Minor)** | Increments only the minor version (e.g. `_v001` → `_v002`). Useful for quick test saves. |

---

### 3️⃣ Directory Paths
| Path | Description |
|------|-------------|
| **Assets / Cache / USD / Flipbook / Render** | Auto-generated paths based on the project structure. |
| | Example: `$CACHE` → `D:/Projects/Demo/SQ010/SH030/cache/` |
| | Folder icons open the location in your OS file browser. |

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

