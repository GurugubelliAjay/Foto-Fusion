# For Building GUI
from tkinter import *
from tkinter import filedialog,messagebox,colorchooser
# For Comboboxes and PhotoImage
import ttkbootstrap as ttk
# For Image Processing
from PIL import Image,ImageTk,ImageFilter,ImageGrab,ImageOps
# Creating a Root

root=ttk.Window(themename='cosmo')
# Title
root.title('Foto Fusion - Image Editor')
# File Icon
icon = ttk.PhotoImage(file='Icon.png')
root.iconphoto(False,icon)
# Getting Screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Setting Geometry
root.geometry(f"{screen_width}x{screen_height}")
# Creating a icon
# Defining Global Variables
file_path=""
pen_size=5
pen_color='black'
# function to open the image file
def open_image():
    global file_path
    file_path= filedialog.askopenfilename(initialdir='/Users/gurugubelliajay/Documents/Project Files',title='Select a file',filetypes=(("jpg files",'*.jpg'),("all files",'*.*'),("jpeg files",'*.jpeg')))
    if file_path:
        global myimage,photo_image
        myimage = Image.open(file_path)
         # Convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        img_width, img_height = myimage.size
        # Calculate the dimensions to fit the image within the available space
        max_width = canvas.winfo_width()
        max_height = canvas.winfo_height()
        aspect_ratio = min(max_width / img_width, max_height / img_height)
        new_width = int(img_width * aspect_ratio)
        new_height = int(img_height * aspect_ratio)
        myimage = myimage.resize((new_width, new_height), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(myimage)
        # Clear the canvas before drawing the new image
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=photo_image)
# a global variable for checking the flip state of the image
is_flipped = False
def flip_image():
    try:
        global myimage, photo_image, is_flipped,file_path,rotation_angle
        if not is_flipped:
            # Open the image and flip it left and right
            myimage = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT)
            is_flipped = True
        else:
            # Reset the image to its original state
            myimage = Image.open(file_path)
            is_flipped = False
         # Convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        img_width, img_height = myimage.size
        # Calculate the dimensions to fit the image within the available space
        max_width = canvas.winfo_width()
        max_height = canvas.winfo_height()
        aspect_ratio = min(max_width / img_width, max_height / img_height)
        new_width = int(img_width * aspect_ratio)
        new_height = int(img_height * aspect_ratio)
        myimage = myimage.resize((new_width, new_height), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(myimage)
        # Clear the canvas before drawing the new image
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=photo_image)

    except:
        messagebox.showerror(title='Flip Image Error', message='Please select an image to flip!')

rotation_angle=0
def rotate_image():
    try:
        global myimage, photo_image, rotation_angle, file_path, canvas
        # Open the image and rotate it
        myimage = Image.open(file_path)
        myimage = myimage.rotate(rotation_angle + 90, expand=True)
        rotation_angle += 90
        # Reset image if angle is a multiple of 360 degrees
        if rotation_angle % 360 == 0:
            rotation_angle = 0
            myimage = Image.open(file_path)
        # Convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        img_width, img_height = myimage.size
        # Calculate the dimensions to fit the image within the available space
        max_width = canvas.winfo_width()
        max_height = canvas.winfo_height()
        aspect_ratio = min(max_width / img_width, max_height / img_height)
        new_width = int(img_width * aspect_ratio)
        new_height = int(img_height * aspect_ratio)
        myimage = myimage.resize((new_width, new_height), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(myimage)
        # Clear the canvas before drawing the new image
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=photo_image)
    except:
        messagebox.showerror(title='Rotate Image Error', message='Please select an image to rotate!')

# function for applying filters to the opened image file
def apply_filter(filter):
    global myimage, photo_image,rotation_angle,file_path,canvas
    try:
        # check if the image has been flipped or rotated
        if is_flipped:
            # flip the original image left and right
            flipped_image = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT)
            # rotate the flipped image
            myimage = flipped_image.rotate(rotation_angle)
            # apply the filter to the rotated image
            if filter == 'Default':
                myimage = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT).rotate(rotation_angle)
            elif filter == "Black and White":
                myimage = ImageOps.grayscale(myimage)
            elif filter == "Blur":
                myimage = myimage.filter(ImageFilter.BLUR)
            elif filter == "Contour":
                myimage = myimage.filter(ImageFilter.CONTOUR)
            elif filter == "Detail":
                myimage = myimage.filter(ImageFilter.DETAIL)
            elif filter == "Emboss":
                myimage = myimage.filter(ImageFilter.EMBOSS)
            elif filter == "Edge Enhance":
                myimage = myimage.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Sharpen":
                myimage = myimage.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                myimage = myimage.filter(ImageFilter.SMOOTH)        
            else:
                myimage = Image.open(file_path).transpose(Image.FLIP_LEFT_RIGHT).rotate(rotation_angle)

        elif rotation_angle != 0:
            # rotate the original image
            myimage = Image.open(file_path).rotate(rotation_angle)
            # apply the filter to the rotated image
            if filter=='Default':
                myimage = Image.open(file_path).rotate(rotation_angle)
            elif filter == "Black and White":
                myimage = ImageOps.grayscale(myimage)
            elif filter == "Blur":
                myimage = myimage.filter(ImageFilter.BLUR)
            elif filter == "Contour":
                myimage = myimage.filter(ImageFilter.CONTOUR)
            elif filter == "Detail":
                myimage = myimage.filter(ImageFilter.DETAIL)
            elif filter == "Emboss":
                myimage = myimage.filter(ImageFilter.EMBOSS)
            elif filter == "Edge Enhance":
                myimage = myimage.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Sharpen":
                myimage = myimage.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                myimage = myimage.filter(ImageFilter.SMOOTH)
            else:
                myimage = Image.open(file_path).rotate(rotation_angle)
        else:
            # apply the filter to the original image
            myimage = Image.open(file_path)
            if filter=='Default':
                myimage=Image.open(file_path)
            elif filter == "Black and White":
                myimage = ImageOps.grayscale(myimage)
            elif filter == "Blur":
                myimage = myimage.filter(ImageFilter.BLUR)
            elif filter == "Sharpen":
                myimage = myimage.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                myimage = myimage.filter(ImageFilter.SMOOTH)
            elif filter == "Emboss":
                myimage = myimage.filter(ImageFilter.EMBOSS)
            elif filter == "Detail":
                myimage = myimage.filter(ImageFilter.DETAIL)
            elif filter == "Edge Enhance":
                myimage = myimage.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Contour":
                myimage = myimage.filter(ImageFilter.CONTOUR)
        # Convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        img_width, img_height = myimage.size
        # Calculate the dimensions to fit the image within the available space
        max_width = canvas.winfo_width()
        max_height = canvas.winfo_height()
        aspect_ratio = min(max_width / img_width, max_height / img_height)
        new_width = int(img_width * aspect_ratio)
        new_height = int(img_height * aspect_ratio)
        myimage = myimage.resize((new_width, new_height), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(myimage)
        # Clear the canvas before drawing the new image
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=photo_image)
    except:
        messagebox.showerror(title='Error', message='Please select an image first!')

is_drawing = False  # Flag to indicate drawing mode
last_x = None
last_y = None

def start_drawing(event):
    global last_x, last_y, is_drawing
    last_x = event.x
    last_y = event.y
    is_drawing = True  

def draw(event):
    global last_x, last_y, is_drawing
    if is_drawing:
        if last_x is not None and last_y is not None:
            canvas.create_line(last_x, last_y, event.x, event.y, fill=pen_color, width=pen_size, tags="Line", capstyle=ttk.ROUND)
        last_x = event.x
        last_y = event.y

def stop_drawing(event):
    global last_x, last_y, is_drawing
    last_x = None
    last_y = None
    is_drawing = False

def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]

def erase_lines():
    canvas.delete("Line")
# the function for saving an image
def white_canvas():
        global myimage,photo_image,file_path
        file_path='/Users/gurugubelliajay/Documents/Project Files/White Background-2.jpg'
        myimage = Image.open(file_path)
         # Convert the PIL image to a Tkinter PhotoImage and display it on the canvas
        img_width, img_height = myimage.size
        # Calculate the dimensions to fit the image within the available space
        max_width = canvas.winfo_width()
        max_height = canvas.winfo_height()
        aspect_ratio = min(max_width / img_width, max_height / img_height)
        new_width = int(img_width * aspect_ratio)
        new_height = int(img_height * aspect_ratio)
        myimage = myimage.resize((new_width, new_height), Image.LANCZOS)
        photo_image = ImageTk.PhotoImage(myimage)
        # Clear the canvas before drawing the new image
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=photo_image)
def save_image():
    global file_path, is_flipped, rotation_angle
    if file_path:
        # create a new PIL Image object from the canvas
        myimage = ImageGrab.grab(bbox=(canvas.winfo_rootx(), canvas.winfo_rooty(), canvas.winfo_rootx() + canvas.winfo_width(), canvas.winfo_rooty() + canvas.winfo_height()))
        # check if the image has been flipped or rotated
        if is_flipped or rotation_angle % 360 != 0:
            # Resize and rotate the image
            # Convert the PIL image to a Tkinter PhotoImage and display it on the canvas
            img_width, img_height = myimage.size
            # Calculate the dimensions to fit the image within the available space
            max_width = canvas.winfo_width()
            max_height = canvas.winfo_height()
            aspect_ratio = min(max_width / img_width, max_height / img_height)
            new_width = int(img_width * aspect_ratio)
            new_height = int(img_height * aspect_ratio)
            myimage = myimage.resize((new_width, new_height), Image.LANCZOS)
            if is_flipped:
                myimage = myimage.transpose(Image.FLIP_LEFT_RIGHT)
            if rotation_angle % 360 != 0:
                myimage = myimage.rotate(rotation_angle)
            # update the file path to include the modifications in the file name
            file_path = file_path.split(".")[0] + "_mod.jpg"
        # apply any filters to the image before saving
        filter = filter_combobox.get()
        if filter:
            if filter == "Black and White":
                myimage = ImageOps.grayscale(myimage)
            elif filter == "Blur":
                myimage = myimage.filter(ImageFilter.BLUR)
            elif filter == "Sharpen":
                myimage = myimage.filter(ImageFilter.SHARPEN)
            elif filter == "Smooth":
                myimage = myimage.filter(ImageFilter.SMOOTH)
            elif filter == "Emboss":
                myimage = myimage.filter(ImageFilter.EMBOSS)
            elif filter == "Detail":
                myimage = myimage.filter(ImageFilter.DETAIL)
            elif filter == "Edge Enhance":
                myimage = myimage.filter(ImageFilter.EDGE_ENHANCE)
            elif filter == "Contour":
                myimage = myimage.filter(ImageFilter.CONTOUR)
            # Update the file path to include the filter in the file name
            file_path = file_path.split(".")[0] + "_" + filter.lower().replace(" ", "_") + ".jpg"
        # open file dialog to select save location and file type
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_path:
            if messagebox.askyesno(title='Save Image', message='Do you want to save this image?'):
                # save the image to a file
                myimage = myimage.convert("RGB")
                myimage.save(file_path)
                messagebox.showinfo(title='Saved Image',message='Successfully Saved !!')
def magic_button_click():
    start_label.destroy()
    magic_label.destroy()
    global left_frame,right_frame,photo,myphoto,canvas,separator,filter_label,image_filters,filter_combobox
    global image_icon,flip_icon,rotate_icon,color_icon,erase_icon,white_icon,save_icon
    global image_button,flip_button,rotate_button,color_button,erase_button,save_button,white_button
    # Left frame to display buttons
    left_frame = ttk.Frame(root, width=screen_width*1/3, height=screen_height*1/3)
    left_frame.pack(side="left", fill="y")
    right_frame=ttk.Frame(root,width=400,height=600)
    right_frame.pack(side='right',fill='y')

    photo = Image.open('Icon.png').resize((150,150))
    myphoto =ImageTk.PhotoImage(photo)
    photo_label=ttk.Label(right_frame,image=myphoto)
    photo_label.pack(padx=5,pady=30)
    # Right canvas for displaying the image
    separator = ttk.Separator(root, orient="vertical")
    separator.pack(side="left", fill="y")
    canvas = ttk.Canvas(root, width=screen_width, height=screen_height)
    # label
    filter_label = ttk.Label(left_frame, text="Select Filter:", background='white')
    filter_label.config(font=('Helvetica bold',20))
    filter_label.pack(padx=80, pady=20)
    # List of filters
    image_filters = ['Default',"Contour", "Black and White", "Blur", "Detail", "Emboss", "Edge Enhance", "Sharpen", "Smooth"]
    # Combobox for the filters
    filter_combobox = ttk.Combobox(left_frame, values=image_filters, width=15)
    filter_combobox.current(0)
    filter_combobox.pack(padx=80)
    filter_combobox.bind("<<ComboboxSelected>>", lambda event: apply_filter(filter_combobox.get()))
    # Loading the icons for the 4 buttons
    image_icon = ttk.PhotoImage(file = 'add.png').subsample(9,9)
    flip_icon = ttk.PhotoImage(file = 'flip.png').subsample(9,9)
    rotate_icon = ttk.PhotoImage(file = 'rotate.png').subsample(9,9)
    color_icon = ttk.PhotoImage(file = 'color.png').subsample(9,9)
    erase_icon = ttk.PhotoImage(file = 'erase.png').subsample(9,9)
    white_icon = ttk.PhotoImage(file = 'Canvas.png').subsample(9,9)
    save_icon = ttk.PhotoImage(file = 'saved.png').subsample(9,9)

    # Opening the image 
    image_button = ttk.Button(left_frame, image=image_icon,bootstyle='Light',command=open_image)
    image_button.pack(pady=10)
    add_label = ttk.Label(left_frame, text="Add Image", background='white')
    add_label.config(font=('Helvetica bold',10))
    add_label.pack(padx=10)
    # Flipping the image
    flip_button = ttk.Button(left_frame, image=flip_icon, bootstyle="light",command=flip_image)
    flip_button.pack(pady=10)
    flip_label = ttk.Label(left_frame, text="Flip Image", background='white')
    flip_label.config(font=('Helvetica bold',10))
    flip_label.pack(padx=10)
    # Rotating the image 
    rotate_button = ttk.Button(left_frame, image=rotate_icon, bootstyle="light",command=rotate_image)
    rotate_button.pack(pady=10)
    rotate_label = ttk.Label(left_frame, text="Rotate Image", background='white')
    rotate_label.config(font=('Helvetica bold',10))
    rotate_label.pack(padx=10)
    # Choosing pen color
    color_button = ttk.Button(left_frame, image=color_icon, bootstyle="light",command=change_color)
    color_button.pack(pady=10)
    paint_label = ttk.Label(left_frame, text="Paint", background='white')
    paint_label.config(font=('Helvetica bold',10))
    paint_label.pack(padx=10)
    # Erasing the lines drawn over the image file
    erase_button = ttk.Button(left_frame, image=erase_icon, bootstyle="light",command=erase_lines)
    erase_button.pack(pady=10)
    erase_label = ttk.Label(left_frame, text="Erase", background='white')
    erase_label.config(font=('Helvetica bold',10))
    erase_label.pack(padx=10)
    # White Canvas
    white_button = ttk.Button(left_frame, image=white_icon, bootstyle="light",command=white_canvas)
    white_button.pack(pady=10)
    white_label = ttk.Label(left_frame, text="White Canvas", background='white')
    white_label.config(font=('Helvetica bold',10))
    white_label.pack(padx=10)
    # Saving the image file
    save_button = ttk.Button(left_frame, image=save_icon, bootstyle="light",command=save_image)
    save_button.pack(pady=10)
    save_label = ttk.Label(left_frame, text="Save Image", background='white')
    save_label.config(font=('Helvetica bold',10))
    save_label.pack(padx=10)
    # Saving the canvas
    canvas.pack(padx=10,pady=100)
    # canvas.pack(padx=35,pady=100)
    # binding the Canvas to the B1-Motion event
    canvas.bind("<Button-1>", start_drawing)
    canvas.bind("<B1-Motion>", draw)
    canvas.bind("<ButtonRelease-1>", stop_drawing)

start_image = Image.open('Foto Fusion-2.png').resize((960,540))
start_logo = ImageTk.PhotoImage(start_image)

start_label = Label(root, image=start_logo)
start_label.pack(pady=80)

magic_image = Image.open('Start Magic-11.png').resize((360, 120))
magic_logo = ImageTk.PhotoImage(magic_image)

magic_label = Canvas(root, width=450, height=150)
magic_label.pack(padx=530)
magic_label.create_image(0, 0, anchor="nw", image=magic_logo)
magic_label.bind('<Button-1>', lambda event: magic_button_click())

root.mainloop()