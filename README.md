# **Font Installer Script**

This Python script automates the installation of fonts from a nested folder structure. It searches for font files (`.ttf`, `.otf`) inside a specified directory (and its subdirectories) and installs them into the system's font directory.

---

## **Features**
- Automatically traverses nested folders to find font files.
- Supports `.ttf` (TrueType Font) and `.otf` (OpenType Font) formats.
- Installs fonts to the system's font directory:
  - **Windows**: `C:\Windows\Fonts`
  - **macOS**: `~/Library/Fonts`
  - **Linux**: `~/.fonts`

---

## **Prerequisites**

### **Python Installation**
- Make sure Python 3.6 or higher is installed on your system.
- Download Python from [python.org](https://www.python.org/) if it’s not already installed.

### **Administrator Privileges**
- On **Windows**, you need to run the script as an administrator to install fonts.

---

## **Setup**

1. Clone or download this repository to your local machine.

2. Ensure the font files are stored in the correct folder structure. For example:

C:\Users\shivt\Desktop\phtoshop\font\Free Font Pack by Befonts 21
├── Folder1
│   └── Subfolder1
│       └── font1.ttf
├── Folder2
│   └── Subfolder2
│       └── font2.otf
└── ...

Copy

3. Place the Python script (`install_fonts.py`) in your desired directory, for example:
C:\Users\shivt\Desktop\bol\install_fonts.py

Copy

4. Update the `source_directory` path in the script to point to your font folder:
```python
source_directory = r"C:\Users\shivt\Desktop\phtoshop\font\Free Font Pack by Befonts 21"
Usage
Open a terminal or command prompt.

Navigate to the directory where the script is saved. For example:

Copy
cd C:\Users\shivt\Desktop\bol
Run the script using Python:

Copy
python install_fonts.py
The script will:

Traverse through the nested folder structure.
Locate all .ttf and .otf font files.
Copy the font files to the system's font directory.
Once the script finishes, you’ll see a message:

Copy
Font installation completed!
Troubleshooting
Permission Denied
On Windows, run the script as an administrator:
Right-click on the Command Prompt or PowerShell and select Run as Administrator.
Then, navigate to the script directory and run the script.
Script Not Found
Ensure the script file (install_fonts.py) is in the correct directory.
Use the full path to the script if necessary:
Copy
python "C:\Users\shivt\Desktop\bol\install_fonts.py"
Fonts Not Copied
Ensure the font files have .ttf or .otf extensions.
Verify the folder structure matches the expected format.
Supported Platforms
Windows: Installs fonts to C:\Windows\Fonts.
macOS: Installs fonts to ~/Library/Fonts.
Linux: Installs fonts to ~/.fonts.
Contributing
Feel free to submit issues or pull requests if you encounter any problems or wish to improve the script.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Author
Your Name: codieshiv https://github.com/codieshiv
