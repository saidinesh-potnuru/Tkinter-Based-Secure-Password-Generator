import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError

        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()

        characters = ""
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid password length (positive integer).")

def copy_to_clipboard():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=digits_var).pack(anchor='w', padx=20)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack(anchor='w', padx=20)

tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

result_entry = tk.Entry(root, width=35, justify='center')
result_entry.pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196F3", fg="white").pack(pady=5)

root.mainloop()