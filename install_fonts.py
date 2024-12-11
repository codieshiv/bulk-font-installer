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

# Path to your font folder
source_directory = r"C:\Users\shivt\Desktop\phtoshop\font\Free Font Pack by Befonts 21"  # Modify this path

# Determine the system's font directory based on the OS
if platform.system() == "Windows":
    fonts_directory = os.path.join(os.environ["WINDIR"], "Fonts")
    if not is_admin():
        print("Script is not running as administrator. Trying to relaunch as administrator
