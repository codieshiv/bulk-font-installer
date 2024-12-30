import os
import shutil
import platform
import ctypes
import winreg
import time
from pathlib import Path

# Function to check if the script is running as administrator on Windows
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

# Function to trigger a font cache reset on Windows
def reset_font_cache():
    font_cache_service = "FontCache3.0.0.0"  # Service name for font cache
    os.system(f"sc stop {font_cache_service}")
    time.sleep(1)  # Wait for a second before restarting
    os.system(f"sc start {font_cache_service}")
    print("Font cache reset.")

# Relaunch the script as administrator
def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1)

# Path to your font folder
source_directory = r"C:\Users\shivt\Desktop\code\Free Font Pack by Befonts 39"  # Modify this path

# Determine the system's font directory based on the OS
if platform.system() == "Windows":
    fonts_directory = os.path.join(os.environ["WINDIR"], "Fonts")
    if not is_admin():
        print("Script is not running as administrator. Trying to relaunch as administrator.")
        run_as_admin()
    else:
        # Traverse through the nested folder structure and locate all .ttf and .otf font files
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                if file.endswith('.ttf') or file.endswith('.otf'):
                    font_path = os.path.join(root, file)
                    shutil.copy(font_path, fonts_directory)
                    print(f"Copied {font_path} to {fonts_directory}")

                    # Register the font in the system registry
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts", 0, winreg.KEY_SET_VALUE) as key:
                        winreg.SetValueEx(key, os.path.basename(file), 0, winreg.REG_SZ, file)

        reset_font_cache()
else:
    print("This script is designed to run on Windows.")
