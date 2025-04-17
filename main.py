import json
import os
import string
import secrets
import csv
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from crypto_utils import encrypt_data, decrypt_data, load_key

# === Constants ===
DATA_FILE = "passwords.enc"
KEY_FILE = "key.key"
show_password = False
current_theme = "flatly"  # default light theme

# === Load or create key ===
if not os.path.exists(KEY_FILE):
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
else:
    key = load_key(KEY_FILE)

# === Functions ===
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not email or not password:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    new_data = {website: {"email": email, "password": password}}

    if os.path.exists(DATA_FILE):
        try:
            data = decrypt_data(DATA_FILE, key)
        except:
            data = {}
    else:
        data = {}

    data.update(new_data)
    encrypt_data(DATA_FILE, data, key)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    messagebox.showinfo("Success", "Password saved!")

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(16))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

def toggle_password_visibility():
    global show_password
    show_password = not show_password
    password_entry.config(show="" if show_password else "*")
    toggle_btn.config(text="Hide" if show_password else "Show")

def view_all_passwords():
    if not os.path.exists(DATA_FILE):
        messagebox.showinfo("Info", "No data file found.")
        return

    try:
        data = decrypt_data(DATA_FILE, key)
    except:
        messagebox.showerror("Error", "Failed to read data.")
        return

    top = ttk.Toplevel()
    top.title("All Passwords")
    top.geometry("400x300")
    text = ttk.Text(top, wrap="word")
    for site, creds in data.items():
        text.insert(END, f"Website: {site}\nEmail: {creds['email']}\nPassword: {creds['password']}\n\n")
    text.pack(expand=True, fill=BOTH)
    text.config(state="disabled")

def export_to_csv():
    if not os.path.exists(DATA_FILE):
        messagebox.showinfo("Info", "No data file found.")
        return

    try:
        data = decrypt_data(DATA_FILE, key)
    except:
        messagebox.showerror("Error", "Failed to read data.")
        return

    with open("passwords_export.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Website", "Email", "Password"])
        for site, creds in data.items():
            writer.writerow([site, creds["email"], creds["password"]])

    messagebox.showinfo("Export", "Passwords exported to passwords_export.csv")

def toggle_theme():
    global current_theme
    if current_theme == "flatly":
        app.style.theme_use("darkly")
        current_theme = "darkly"
        theme_btn.config(text="🌞 Light Mode")
    else:
        app.style.theme_use("flatly")
        current_theme = "flatly"
        theme_btn.config(text="🌙 Dark Mode")

# === UI Setup ===
app = ttk.Window(themename=current_theme)
app.title("Password Manager")
app.geometry("420x450")
app.resizable(False, False)

# === Widgets ===
ttk.Label(app, text="Website:").grid(row=0, column=0, pady=5, sticky="w")
website_entry = ttk.Entry(app, width=30)
website_entry.grid(row=0, column=1, columnspan=2, pady=5, padx=10)

ttk.Label(app, text="Email/Username:").grid(row=1, column=0, pady=5, sticky="w")
email_entry = ttk.Entry(app, width=30)
email_entry.grid(row=1, column=1, columnspan=2, pady=5, padx=10)

ttk.Label(app, text="Password:").grid(row=2, column=0, pady=5, sticky="w")
password_entry = ttk.Entry(app, width=20, show="*")
password_entry.grid(row=2, column=1, pady=5)

toggle_btn = ttk.Button(app, text="Show", width=8, command=toggle_password_visibility, bootstyle="secondary")
toggle_btn.grid(row=2, column=2, pady=5, padx=5)

ttk.Button(app, text="Generate Password", command=generate_password, bootstyle="info").grid(row=3, column=1, columnspan=2, pady=10)

ttk.Button(app, text="Save", width=30, command=save_password, bootstyle="success").grid(row=4, column=1, columnspan=2, pady=5)
ttk.Button(app, text="View All", width=30, command=view_all_passwords, bootstyle="warning").grid(row=5, column=1, columnspan=2, pady=5)
ttk.Button(app, text="Export to CSV", width=30, command=export_to_csv, bootstyle="primary").grid(row=6, column=1, columnspan=2, pady=5)

theme_btn = ttk.Button(app, text="🌙 Dark Mode", width=30, command=toggle_theme, bootstyle="light")
theme_btn.grid(row=7, column=1, columnspan=2, pady=5)

app.mainloop()
