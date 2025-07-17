import tkinter as tk
from tkinter import ttk, messagebox
import secrets
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    safe_punctuation = "!@#$%^&*()-_=+[]:;,.?/~"
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    all_chars = lowercase + uppercase + digits + safe_punctuation

    lower = secrets.choice(lowercase)
    upper = secrets.choice(uppercase)
    digit = secrets.choice(digits)
    symbol = secrets.choice(safe_punctuation)

    remaining = ''.join(secrets.choice(all_chars) for _ in range(length - 4))
    password_list = list(lower + upper + digit + symbol + remaining)
    secrets.SystemRandom().shuffle(password_list)

    return ''.join(password_list)

def on_generate():
    try:
        length = int(length_var.get())
        if length < 8:
            messagebox.showwarning("Invalid Length", "Password length must be at least 8.")
            return
        password = generate_password(length)
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

def on_copy():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard.")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

# --- UI Setup ---
root = tk.Tk()
root.title("Password Generator")
root.geometry("360x240")
root.configure(bg="white")
root.resizable(False, False)

# macOS-style font & padding
font_title = ("Kanit", 14, "bold")
font_body = ("Kanit", 11)
pad_x = 20

style = ttk.Style()
style.theme_use("default")

# Style Buttons
style.configure("TButton",
                font=font_body,
                padding=6,
                relief="flat",
                background="#E5E5E5",
                foreground="black")
style.map("TButton",
          background=[("active", "#d0d0d0")])

password_var = tk.StringVar()
length_var = tk.StringVar(value="12")

# Widgets
ttk.Label(root, text="Secure Password Generator", font=font_title, background="white").pack(pady=(15, 10))

entry = ttk.Entry(root, textvariable=password_var, font=("FiraCode Nerd Font Mono", 12), justify="center", state="readonly", width=28)
entry.pack(pady=5)

frame = tk.Frame(root, bg="white")
frame.pack(pady=10)

ttk.Label(frame, text="Length:", font=font_body, background="white").pack(side="left", padx=(0, 5))
ttk.Entry(frame, textvariable=length_var, width=6, justify="center").pack(side="left")

ttk.Button(root, text="Generate Password", command=on_generate).pack(pady=5)
ttk.Button(root, text="Copy to Clipboard", command=on_copy).pack(pady=5)

# Remove window border for a more native look on macOS
root.update_idletasks()
root.overrideredirect(False)  # Set to True for no border (optionally)

root.mainloop()

