"""
Windows DLL & Missing Files Bug Doctor
Author: AI Studio Assistant
Note: Must be run as Administrator (Right-click -> Run as Administrator)
"""

import os
import sys
import subprocess
import threading
import urllib.request
import tkinter as tk
from tkinter import messagebox, scrolledtext

class DLLBugDoctorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Windows DLL & Bug Doctor v1.0")
        self.root.geometry("700x520")
        self.root.config(bg="#0f172a") # Dark theme
        self.root.resizable(False, False)

        # Title Header
        title_label = tk.Label(
            root, 
            text="🛡️ Windows DLL & Bug Repair Assistant", 
            font=("Segoe UI", 15, "bold"), 
            bg="#0f172a", 
            fg="#38bdf8"
        )
        title_label.pack(pady=15)

        sub_label = tk.Label(
            root, 
            text="Fix missing .dll files, corrupted system files, and Windows bugs automatically.", 
            font=("Segoe UI", 10), 
            bg="#0f172a", 
            fg="#94a3b8"
        )
        sub_label.pack(anchor="w", padx=25, pady=(0, 10))

        # Action Buttons Frame
        btn_frame = tk.Frame(root, bg="#0f172a")
        btn_frame.pack(fill="x", padx=20, pady=5)

        self.create_btn(btn_frame, "🔍 Run SFC File Checker", self.run_sfc_scan, 0, 0)
        self.create_btn(btn_frame, "🛠️ Run DISM Image Repair", self.run_dism_repair, 0, 1)
        self.create_btn(btn_frame, "📦 Install VC++ Runtimes (Fix .DLL)", self.install_vc_redist, 1, 0)
        self.create_btn(btn_frame, "🛡️ Windows Defender Bug Scan", self.run_defender_scan, 1, 1)

        # Console Log Box
        console_frame = tk.Frame(root, bg="#0f172a")
        console_frame.pack(fill="both", expand=True, padx=20, pady=15)

        console_label = tk.Label(
            console_frame, 
            text="Diagnostic & Repair Console:", 
            font=("Segoe UI", 10, "bold"), 
            bg="#0f172a", 
            fg="#cbd5e1"
        )
        console_label.pack(anchor="w", pady=(0, 5))

        self.console = scrolledtext.ScrolledText(
            console_frame, 
            wrap=tk.WORD, 
            font=("Consolas", 10), 
            bg="#020617", 
            fg="#38bdf8", 
            insertbackground="white",
            relief="flat",
            bd=5
        )
        self.console.pack(fill="both", expand=True)
        self.log("[-] Ready. Click any repair tool above. (Make sure to run as Administrator!)\n")

    def create_btn(self, parent, text, command, row, col):
        btn = tk.Button(
            parent, 
            text=text, 
            command=command, 
            font=("Segoe UI", 10, "bold"), 
            bg="#1e293b", 
            fg="#ffffff", 
            activebackground="#334155",
            activeforeground="#38bdf8",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=12,
            pady=10
        )
        btn.grid(row=row, column=col, padx=8, pady=8, sticky="ew")
        parent.grid_columnconfigure(col, weight=1)

    def log(self, message):
        self.console.insert(tk.END, message + "\n")
        self.console.see(tk.END)

    def run_async(self, func):
        threading.Thread(target=func, daemon=True).start()

    # 1. SFC System File Checker
    def run_sfc_scan(self):
        def task():
            self.log("[*] Starting SFC (System File Checker)...")
            self.log("[*] Scanning for missing or corrupted system DLLs...")
            try:
                result = subprocess.run(["sfc", "/scannow"], capture_output=True, text=True)
                self.log(result.stdout)
                self.log("[+] SFC scan finished. Check results above.\n")
            except Exception as e:
                self.log(f"[!] Error running SFC: {e}\n")
        self.run_async(task)

    # 2. DISM Image Repair
    def run_dism_repair(self):
        def task():
            self.log("[*] Starting DISM Image Health Restore...")
            self.log("[*] Connecting to Windows Update to download clean system files...")
            try:
                result = subprocess.run(["dism", "/Online", "/Cleanup-Image", "/RestoreHealth"], capture_output=True, text=True)
                self.log(result.stdout)
                self.log("[+] DISM repair completed.\n")
            except Exception as e:
                self.log(f"[!] Error running DISM: {e}\n")
        self.run_async(task)

    # 3. Visual C++ Redistributable Fix (.dll missing error fix)
    def install_vc_redist(self):
        def task():
            self.log("[*] Downloading Microsoft Visual C++ Redistributable (fixes msvcp140.dll, vcruntime140.dll)...")
            url = "https://aka.ms/vs/17/release/vc_redist.x64.exe"
            installer = "vc_redist.x64.exe"
            try:
                urllib.request.urlretrieve(url, installer)
                self.log(f"[*] Downloaded {installer}. Starting silent installation...")
                subprocess.run([installer, "/install", "/quiet", "/norestart"])
                self.log("[+] Visual C++ Redistributable installed successfully! Please restart your PC.\n")
            except Exception as e:
                self.log(f"[!] Error installing VC++ Redistributable: {e}\n")
        self.run_async(task)

    # 4. Windows Defender Bug & Malware Scan
    def run_defender_scan(self):
        def task():
            self.log("[*] Triggering Windows Defender Quick Bug & Malware Scan...")
            defender_path = r"C:\Program Files\Windows Defender\MpCmdRun.exe"
            if not os.path.exists(defender_path):
                self.log("[!] Windows Defender command-line tool not found at default path.")
                return
            try:
                result = subprocess.run([defender_path, "-Scan", "-ScanType", "1"], capture_output=True, text=True)
                self.log(result.stdout)
                self.log("[+] Defender scan completed.\n")
            except Exception as e:
                self.log(f"[!] Error running Defender scan: {e}\n")
        self.run_async(task)

if __name__ == "__main__":
    root = tk.Tk()
    app = DLLBugDoctorApp(root)
    root.mainloop()
