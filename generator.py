import tkinter as tk
import string
import random
from PIL import Image, ImageTk

root = tk.Tk()
canvas = tk.Canvas(root, width=700, height=400)
canvas.grid(columnspan=3, rowspan=3)

# Logo
logo = Image.open('lock.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


password_length = tk.IntVar()
password_characters = tk.StringVar()
generated_password = tk.StringVar()

def generate_password():
    length = password_length.get()
    characters = password_characters.get()

    character_list = []
    if "uppercase" in characters:
        character_list.extend(string.ascii_uppercase)
    if "lowercase" in characters:
        character_list.extend(string.ascii_lowercase)
    if "numbers" in characters:
        character_list.extend(string.digits)
    if "symbols" in characters:
        character_list.extend(string.punctuation)

    password = ''.join(random.choice(character_list) for _ in range(length))

    generated_password.set(password)

length_label = tk.Label(root, text="Password Length:")
length_label.grid()

length_entry = tk.Entry(root, textvariable=password_length)
length_entry.grid()

characters_label = tk.Label(root, text="Password Characters:")
characters_label.grid()

characters_uppercase = tk.Checkbutton(root, text="Uppercase", variable=password_characters, onvalue="uppercase")
characters_uppercase.grid()
characters_lowercase = tk.Checkbutton(root, text="Lowercase", variable=password_characters, onvalue="lowercase")
characters_lowercase.grid()
characters_numbers = tk.Checkbutton(root, text="Numbers", variable=password_characters, onvalue="numbers")
characters_numbers.grid()
characters_symbols = tk.Checkbutton(root, text="Symbols", variable=password_characters, onvalue="symbols")
characters_symbols.grid()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
generate_button.grid()

generated_label = tk.Label(root, text="Generated Password:")
generated_label.grid()

generated_entry = tk.Entry(root, textvariable=generated_password, state='readonly')
generated_entry.grid()

root.mainloop()
