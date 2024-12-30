import os
import shutil
import platform
import ctypes
import sys
import time
from pathlib import Path

# Function to check if the script is running as administrator on Windows
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

# Function to trigger a font cache reset on Windows
def reset_font_cache_windows():
    font_cache_service = "FontCache3.0.0.0"  # Service name for font cache
    os.system(f"sc stop {font_cache_service}")
    time.sleep(1)  # Wait for a second before restarting
    os.system(f"sc start {font_cache_service}")
    print("Font cache reset.")

# Relaunch the script as administrator on Windows
def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, __file__, None, 1)

# Function to reset font cache on Linux
def reset_font_cache_linux():
    os.system("fc-cache -f -v")
    print("Font cache reset.")

# Function to reset font cache on macOS
def reset_font_cache_mac():
    os.system("atsutil databases -remove")
    os.system("atsutil server -shutdown")
    os.system("atsutil server -ping")
    print("Font cache reset.")

# Path to your font folder
source_directory = r"C:\Users\shivt\Desktop\phtoshop\font\Free Font Pack by Befonts 21"  # Modify this path as needed

# Determine the system's font directory and copy fonts based on the OS
if platform.system() == "Windows":
    fonts_directory = os.path.join(os.environ["WINDIR"], "Fonts")
    if not is_admin():
        print("Script is not running as administrator. Trying to relaunch as administrator.")
        run_as_admin()
    else:
        for root, dirs, files in os.walk(source_directory):
            for file in files:
                if file.endswith('.ttf') or file.endswith('.otf'):
                    font_path = os.path.join(root, file)
                    shutil.copy(font_path, fonts_directory)
                    print(f"Copied {font_path} to {fonts_directory}")

        reset_font_cache_windows()

elif platform.system() == "Linux":
    fonts_directory = os.path.join(os.environ["HOME"], ".fonts")
    os.makedirs(fonts_directory, exist_ok=True)
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith('.ttf') or file.endswith('.otf'):
                font_path = os.path.join(root, file)
                shutil.copy(font_path, fonts_directory)
                print(f"Copied {font_path} to {fonts_directory}")

    reset_font_cache_linux()

elif platform.system() == "Darwin":  # macOS
    fonts_directory = os.path.join(os.environ["HOME"], "Library", "Fonts")
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith('.ttf') or file.endswith('.otf'):
                font_path = os.path.join(root, file)
                shutil.copy(font_path, fonts_directory)
                print(f"Copied {font_path} to {fonts_directory}")

    reset_font_cache_mac()

else:
    print("This script is designed to run on Windows, Linux, and macOS.")
