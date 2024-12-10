import os
import shutil
import platform

# Path to your font folder
source_directory = r"C:\Users\shivt\Desktop\phtoshop\font\Free Font Pack by Befonts 22"

# Determine the system's font directory based on the OS
if platform.system() == "Windows":
    fonts_directory = os.path.join(os.environ["WINDIR"], "Fonts")
elif platform.system() == "Darwin":  # macOS
    fonts_directory = os.path.expanduser("~/Library/Fonts")
elif platform.system() == "Linux":
    fonts_directory = os.path.expanduser("~/.fonts")  # For most Linux distros
    os.makedirs(fonts_directory, exist_ok=True)  # Ensure the directory exists
else:
    raise OSError("Unsupported operating system")

# Supported font file extensions
font_extensions = (".ttf", ".otf")

# Traverse through the main directory
for folder_name in os.listdir(source_directory):
    folder_path = os.path.join(source_directory, folder_name)
    
    # Check if it's a folder
    if os.path.isdir(folder_path):
        # Look for subfolders inside the folder
        for subfolder_name in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, subfolder_name)
            
            # Ensure it's a subfolder
            if os.path.isdir(subfolder_path):
                # Loop through files in the subfolder
                for file_name in os.listdir(subfolder_path):
                    if file_name.lower().endswith(font_extensions):  # Check if it's a font file
                        font_path = os.path.join(subfolder_path, file_name)
                        try:
                            # Copy the font file to the system's font directory
                            shutil.copy(font_path, fonts_directory)
                            print(f"Installed: {file_name}")
                        except PermissionError:
                            print(f"Permission denied: Unable to install {file_name}. Run the script as an administrator.")
                        except Exception as e:
                            print(f"Error installing {file_name}: {e}")

print("Font installation completed!")
