
## 📄 README.md (Updated with EXE instructions)

```markdown
# 📝 Batch File Renamer (Dynamic Extension Version)

A simple Python GUI tool to **batch rename files** inside a selected folder.  
👉 Unlike the fixed version, this tool **automatically detects available file extensions** in your selected folder and shows them as options for renaming.

---

## ✨ Features
- Select any folder
- Automatically detect all file formats (e.g., `.jpg`, `.png`, `.mp3`, `.pdf`, `.zip`, etc.)
- Choose file formats via checkboxes
- Enter a base name (e.g., `MyFile`)
- Renames files like:

```

MyFile01.jpg
MyFile02.jpg
MyFile03.jpg

````

---

## ⚙️ Requirements
- Python **3.8+** (only needed if you run the `.py` version)
- Tkinter (comes pre-installed with Python, but Linux users may need to install separately)

Linux (Debian/Ubuntu) users run:
```bash
sudo apt-get install python3-tk
````

Fedora:

```bash
sudo dnf install python3-tkinter
```

---

## 🚀 Setup & Run

### ▶️ Option 1: Run with Python

#### 1️⃣ Clone or Extract Project

If you downloaded the `.zip`:

```bash
unzip batch_file_renamer.zip
cd batch_file_renamer
```

Or if using GitHub:

```bash
git clone https://github.com/your-username/batch_file_renamer.git
cd batch_file_renamer
```

#### 2️⃣ Create Virtual Environment (venv)

Linux / macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows (CMD):

```cmd
python -m venv venv
venv\Scripts\activate
```

Windows (PowerShell):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

#### 3️⃣ Install Dependencies

For this project, Tkinter is the only requirement.
Still, create a `requirements.txt` for safety:

```txt
tk
```

Install with:

```bash
pip install -r requirements.txt
```

#### 4️⃣ Run the App

```bash
python batch_file_renamer.py
```

---

### ▶️ Option 2: Run the EXE (Windows Only)

If you have the `batch_file_renamer.exe` (inside the `dist/` folder after building with PyInstaller):

1. Go to the `dist` folder:

   ```
   dist/
      └── batch_file_renamer.exe
   ```

2. Double-click `batch_file_renamer.exe`
   👉 No need to install Python or Tkinter separately.

3. The GUI window will open directly. 🎉

---

## 🎯 How to Use

1. Run the program → A window will open.
2. Click **Browse** → Select your folder.
3. The program will scan and show all file extensions found in that folder.
4. Tick the file formats you want to rename.
5. Enter a **Base Name** (example: `MyFile`).
6. Click **Rename Files** → All files will be renamed sequentially.

---

## 📌 Example

Before:

```
photo.png
image.png
scan.png
```

After (Base Name = `Pic`):

```
Pic01.png
Pic02.png
Pic03.png
```

---

## ✅ Notes

* Only files with extensions are detected.
* Files are sorted alphabetically before renaming.
* Serial numbers are zero-padded (`01`, `02`, … `99`).
* `.exe` version works without installing Python (Windows only).

---

## 📜 License

Free to use and modify. 🚀

```

---

👉 এখন README তে **দুইটা রান করার পথ** আছে:  
1. Python দিয়ে (`.py` version)  
2. সরাসরি `.exe` ডাবল-ক্লিক করে (Windows users only)  

---

```
