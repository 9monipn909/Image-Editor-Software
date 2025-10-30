import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageEnhance

# Create main window
root = tk.Tk()
root.title("Python Image Editor")
root.geometry("900x700")
root.config(bg="#f0f0f0")

current_image = None
display_image = None

# Heading
label = tk.Label(root,
                 text="🖼️ Simple Image Editor",
                 font=("Arial", 20, "bold"),
                 bg="#f0f0f0")
label.pack(pady=10)

# Image display area
img_label = tk.Label(root, bg="#f0f0f0")
img_label.pack()

# Open Image
def open_image():
    global current_image, display_image
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_path:
        current_image = Image.open(file_path)
        resized = current_image.resize((500, 400))
        display_image = ImageTk.PhotoImage(resized)
        img_label.config(image=display_image)
        img_label.image = display_image

# Convert to Grayscale
def to_grayscale():
    global current_image, display_image
    if current_image:
        gray = current_image.convert("L")
        resized = gray.resize((500, 400))
        display_image = ImageTk.PhotoImage(resized)
        img_label.config(image=display_image)
        img_label.image = display_image

# Brightness Control
def adjust_brightness(value):
    global current_image, display_image
    if current_image:
        enhancer = ImageEnhance.Brightness(current_image)
        bright_img = enhancer.enhance(float(value))
        resized = bright_img.resize((500, 400))
        display_image = ImageTk.PhotoImage(resized)
        img_label.config(image=display_image)
        img_label.image = display_image

# Buttons and Slider
open_button = tk.Button(root,
                        text="📂 Open Image",
                        font=("Arial", 14),
                        command=open_image)
open_button.pack(pady=10)

gray_button = tk.Button(root,
                        text="🖤 Convert to Grayscale",
                        font=("Arial", 12),
                        command=to_grayscale)
gray_button.pack(pady=10)

brightness_slider = tk.Scale(root,
                             from_=0.5, to=2.0,
                             resolution=0.1,
                             orient="horizontal",
                             label="Adjust Brightness",
                             command=adjust_brightness)
brightness_slider.set(1.0)
brightness_slider.pack(pady=10)

root.mainloop()