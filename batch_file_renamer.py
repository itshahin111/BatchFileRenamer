import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder():
    folder = filedialog.askdirectory()
    folder_path.set(folder)
    if folder:
        load_extensions(folder)

def load_extensions(folder):
    # ফোল্ডারে যত ফাইল আছে সেগুলোর এক্সটেনশন বের করি
    exts = set(os.path.splitext(f)[1] for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)))
    for widget in ext_frame.winfo_children():
        widget.destroy()
    extensions.clear()

    if not exts:
        tk.Label(ext_frame, text="No files found in this folder.").pack(anchor="w")
        return

    for ext in sorted(exts):
        if ext:  # শুধু যেগুলোর এক্সটেনশন আছে
            var = tk.BooleanVar()
            extensions[ext] = var
            tk.Checkbutton(ext_frame, text=ext, variable=var).pack(anchor="w")

def rename_files():
    folder = folder_path.get()
    if not folder:
        messagebox.showerror("Error", "Please select a folder first.")
        return
    
    selected_exts = [ext for ext, var in extensions.items() if var.get()]
    if not selected_exts:
        messagebox.showerror("Error", "Please select at least one file format.")
        return
    
    base = base_name.get()
    if not base:
        messagebox.showerror("Error", "Please enter a base name.")
        return
    
    files = [f for f in os.listdir(folder) if os.path.splitext(f)[1] in selected_exts]
    files.sort()
    
    for i, file in enumerate(files, start=1):
        ext = os.path.splitext(file)[1]
        new_name = f"{base}{str(i).zfill(2)}{ext}"
        os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
    
    messagebox.showinfo("Success", f"{len(files)} files renamed successfully!")

root = tk.Tk()
root.title("Batch File Renamer")

folder_path = tk.StringVar()
base_name = tk.StringVar()

# Folder Select
tk.Label(root, text="Select Folder:").pack()
tk.Entry(root, textvariable=folder_path, width=40).pack()
tk.Button(root, text="Browse", command=select_folder).pack(pady=5)

# Dynamic File format checkboxes
tk.Label(root, text="Select File Formats:").pack()
ext_frame = tk.Frame(root)
ext_frame.pack(fill="both", expand=True)
extensions = {}

# Base name input
tk.Label(root, text="Base Name:").pack()
tk.Entry(root, textvariable=base_name, width=30).pack(pady=5)

# Rename button
tk.Button(root, text="Rename Files", command=rename_files, bg="green", fg="white").pack(pady=10)

root.mainloop()
