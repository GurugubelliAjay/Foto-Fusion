from tkinter import *
from tkinter import filedialog, messagebox, colorchooser
import ttkbootstrap as ttk
from PIL import Image, ImageTk, ImageFilter, ImageGrab, ImageOps

root = ttk.Window(themename='cosmo')
root.title('Foto Fusion - Image Editor')

icon = ttk.PhotoImage(file='Icon.png')
root.iconphoto(False, icon)

start_image = Image.open('Icon.png').resize((600, 600))
start_logo = ImageTk.PhotoImage(start_image)

start_label = Label(root, image=start_logo)
start_label.pack(pady=10)

magic_image = Image.open('Start Magic.png').resize((450, 150))
magic_logo = ImageTk.PhotoImage(magic_image)

def magic_button_click():
    # Place your button functionality here
    pass

magic_label = Canvas(root, width=450, height=150)
magic_label.pack()
magic_label.create_image(0, 0, anchor="nw", image=magic_logo)
magic_label.bind('<Button-1>', lambda event: magic_button_click())

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

root.mainloop()
