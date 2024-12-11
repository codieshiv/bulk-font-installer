# Font Installer Script

This Python script automates the installation of fonts from a nested folder structure. It searches for font files (`.ttf`, `.otf`) inside a specified directory (and its subdirectories) and installs them into the system's font directory.

---

## **Features**
- Automatically traverses nested folders to find font files.
- Supports `.ttf` (TrueType Font) and `.otf` (OpenType Font) formats.
- Installs fonts to the system's font directory:
  - **Windows**: `C:\Windows\Fonts`
  - **macOS**: `~/Library/Fonts`
  - **Linux**: `~/.fonts`
- Registers fonts in the system's registry (Windows only).
- Resets the font cache (Windows only) for immediate recognition.

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

    ```
    C:\Users\shivt\Desktop\phtoshop\font\Free Font Pack by Befonts 21
    ├── Folder1
    │   └── Subfolder1
    │       └── font1.ttf
    ├── Folder2
    │   └── Subfolder2
    │       └── font2.otf
    └── ...
    ```

3. Place the Python script (`install_fonts.py`) in your desired directory, for example:
    ```
    C:\Users\shivt\Desktop\bol\install_fonts.py
    ```

4. Update the `source_directory` path in the script to point to your font folder:

    ```python
    source_directory = r"C:\Users\shivt\Desktop\phtoshop\font\Free Font Pack by Befonts 21"
    ```

---

## **Usage**

1. Open a terminal or command prompt.
   
2. Navigate to the directory where the script is saved:

    ```bash
    cd C:\Users\shivt\Desktop\bol
    ```

3. Run the script using Python:

    ```bash
    python install_fonts.py
    ```

The script will:
- Traverse through the nested folder structure.
- Locate all `.ttf` and `.otf` font files.
- Copy the font files to the system's font directory.
- If you're using **Windows**, it will also register the fonts in the system registry and refresh the font cache for immediate recognition.

---

## **Expected Output**
Once the script finishes, you’ll see a message like:

Font installation completed!

yaml
Copy code

---

## **Troubleshooting**

### **Permission Denied**

On **Windows**, run the script as an administrator:

1. Right-click on the Command Prompt or PowerShell and select **Run as Administrator**.
2. Navigate to the script directory and run the script:

    ```bash
    python install_fonts.py
    ```

### **Script Not Found**

Ensure the script file (`install_fonts.py`) is in the correct directory. If needed, specify the full path:

```bash
python "C:\Users\shivt\Desktop\bol\install_fonts.py"
Fonts Not Copied
Ensure the font files have .ttf or .otf extensions.
Verify the folder structure matches the expected format.
On Windows, ensure the font directory is correct (C:\Windows\Fonts).
Supported Platforms
Windows: Installs fonts to C:\Windows\Fonts.
macOS: Installs fonts to ~/Library/Fonts.
Linux: Installs fonts to ~/.fonts.
Contributing
Feel free to submit issues or pull requests if you encounter any problems or wish to improve the script.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Author
Your Name: codieshiv
GitHub Profile

javascript
Copy code

This markdown document will help users understand how to use the script, set it up, and troubleshoot common issues. You can save this content as `README.md` and share it with others who will use the script!
