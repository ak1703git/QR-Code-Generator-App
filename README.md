# QR-Code-Generator-App
---

I was trying to generate some QR codes for my personal use when I went online to try various online tools. After a few free trial generations, rest were behind a paywall. This hampered my ability to make more QR codes. I then got the idea, why not use a simple python script to make your own QR code generator?

This project is a desktop-based **QR Code Generator** built with Python's Tkinter library. It allows users to convert text or URLs into high-quality QR codes, save them locally, and maintain a history of generated links.

---

## Code Breakdown

### 1. GUI Architecture with Tkinter

The application uses the `tkinter` framework to build the user interface.

* **The Root Window:** We initialize the main app with `root = Tk()`, setting a fixed geometry of  pixels and a custom icon for a professional feel.
* **Layout Management:** The `.pack()` method is used throughout to stack widgets (buttons, input boxes, and labels) vertically with custom padding (`pady`).

### 2. QR Code Generation Engine

The heart of the script lies in the `make_code_image` function:

* **`pyqrcode`:** This library handles the mathematical generation of the QR pattern based on the string retrieved from the `entry` box.
* **Image Conversion:** Since Tkinter cannot natively display all image formats, we use `PIL` (Pillow) to open the generated PNG and convert it into a `PhotoImage` object that the `image_label` can render.

### 3. File Handling & Persistence

The script provides a bridge between the application and your local file system:

* **`filedialog.asksaveasfilename`:** This provides a native "Save As" window, allowing users to choose their destination folder and filename.
* **Verification:** The `save_qr_image` function includes a safety check to ensure there is actually a generated code present before attempting to save, preventing potential crashes.

### 4. History Management (Toplevel Windows)

One unique feature of this app is the **Session History**:

* **Global List:** `SAVED_ENTRIES` acts as a temporary database for the current session.
* **`Toplevel()`:** When "Show History" is clicked, a second, independent window pops up containing a `Listbox`.
* **Event Binding:** Using `.bind("<Button-1>", select_entry)`, users can click a previous link in the list to automatically re-populate the main input box.

---

## 🛠️ How to Run

1. **Install Dependencies:**
You will need a few external libraries. Run the following command:
```bash
pip install pyqrcode pypng pillow

```


2. **Run the App:**
```bash
python qr_generator.py

```



---

## Future Improvements

* **Custom Styling:** Adding a color picker to allow users to change the QR code from standard black and white to custom colors.
* **Persistent Storage:** Upgrading the `SAVED_ENTRIES` list to a `SQLite` database or a `.json` file so that history isn't lost when the app is closed.
* **Error Correction Levels:** Adding options for "Low," "Medium," and "High" error correction to make codes more robust.
* **Bulk Generation:** An option to upload a CSV file and generate multiple QR codes at once.


## Dependencies & Requirements
To keep the project organized, you can create a requirements.txt file in your project folder with the following content:

**pypng==0.20220715.0**

**PyQRCode==1.2.1**

**Pillow==10.2.0**

Note: tkinter is usually pre-installed with Python. If you are on Linux and get a "Tkinter not found" error, you may need to install it via your package manager (e.g., sudo apt-get install python3-tk).

## Technical Architecture
To better understand how data moves through the application, here is a high-level view of the logic:

**Input Layer:** User types data into the Tkinter Entry widget.

**Processing Layer:** The make_code_image function grabs that string and uses pyqrcode to calculate the matrix.

**Storage Layer:** The result is temporarily saved as qr_code.png and archived in the SAVED_ENTRIES list.

**Display Layer:** PIL converts the image data for the GUI, and the Toplevel window provides a historical view of the session.

---
