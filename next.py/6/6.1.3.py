import tkinter as tk
from tkinter import filedialog

def show_image():
    image = tk.PhotoImage(file="6/this_is_a_cat.gif")
    image_label.config(image=image)
    image_label.image = image

root = tk.Tk()
root.title("CatHub.com")

question_label = tk.Label(root, text="Do you want to see a cat?")
question_label.pack(pady=50, padx=100)

button = tk.Button(root, text="show pic of cute cat", command=show_image)
button.pack(pady=0, padx=0)

image_label = tk.Label(root)
image_label.pack(pady=50)


root.mainloop()
