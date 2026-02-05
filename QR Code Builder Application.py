"""this is the program file for a QR code generator"""

# The following is a list of libraries required in the QR code generator program
from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter as tk

root = Tk()
root.title("OR CODE GENERATOR")
root.iconbitmap('/Users/akshayvaidya/Documents/Python Practice Directory/download-icon-qr+code-1329858358127832045_32.ico')
root.geometry('500x500') # this sets the shape of the application window

# Creat a text input box
entry = Entry(root, width=50) # The entry function from Tkinter creates an entry box.
entry.pack(pady = 10)

# create an image label
image_label = tk.Label(root)
image_label.pack()

# Create an empty list GLOBAL LIST that will take all the saved links
SAVED_ENTRIES = []

def save_qr_image():
    """this function saves the generated QR code image to a selected folder with a specified name"""
    if image_label.image is None:
        entry.insert(0, "No QR Code to Save!")  # Check if there is an image to save
        return

    # Open a save dialog to choose the directory and file name
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        title="Save QR Code as..."
    )

    if file_path:
        # Save the QR code image as a PNG file
        img = Image.open("qr_code.png")  # Reopen the image from saved file
        img.save(file_path)
        entry.delete(0, END)
        entry.insert(0, "Image saved successfully!")

# Create and display the qr code image.
def make_code_image():
    """this function creates the image of a QR code"""
    qr_code_data = entry.get()
    qr_code = pyqrcode.create(qr_code_data)
    qr_code.png("qr_code.png", scale = 5)
    img = Image.open("qr_code.png")
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk

# Create a save function that will save link from the entry box.
def save_link():
    """this function saves entered links for future"""
    saved_links = entry.get()
    SAVED_ENTRIES.append(saved_links)
    entry.delete(0, tk.END)

# Create a show history function that showes a list of all saved links
def show_history():
    """this function show all the saved links"""
    history_window = tk.Toplevel()
    history_window.title("Saved Entries")

    listbox = tk.Listbox(history_window)
    listbox.pack(fill=tk.BOTH, expand=True)

    for saved_links in SAVED_ENTRIES:
        listbox.insert(tk.END, saved_links)

    def select_entry(event):
        selected_index = listbox.curselection()[0]
        selected_entry = SAVED_ENTRIES[selected_index]
        entry.delete(0, tk.END)
        entry.insert(0, selected_entry)
        history_window.destroy()  # Close the history window

    listbox.bind("<Button-1>", select_entry)

# All the major definition statements that are used in the code and tied to each button and perfrom specific tasks
def clear():
    """this function delets everthing from the entry box"""
    entry.delete(0, END)
    image_label.config(image=None)
    image_label.image = None
    
# All the buttong in the GUI

#This is a variable that is assigned a button that will generate the QR code when clicked
gen_qr = Button(root, text="Generate QR Code", command=make_code_image)
gen_qr.pack(pady=1)

# This is a variable that is assigned a button that will save the link to a list for future when clicked
save_to_list = Button(root, text="Save to History", command=save_link)
save_to_list.pack(pady=1)

# This is a variable that is assigned a button that will show the all saved links when clicked
history_list_popup = Button(root, text="Show Previous QR Code Links", command=show_history)
history_list_popup.pack(pady=1)

# This is a variable that is assigned a button that will clear the link in the dialogue box
clear_input = Button(root, text="Clear Link", command=clear)
clear_input.pack(pady=1)

#This is a variable that is assigned a button that will save the QR code image to PC when clicked
save_qr = Button(root, text="Save QR image", command=save_qr_image)
save_qr.pack(pady=1)


root.mainloop()