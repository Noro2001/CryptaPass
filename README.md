🔐 Password Manager

A simple, secure, and elegant password manager app with encryption, a modern GUI, and powerful features — all built in Python using ttkbootstrap and cryptography.

📆 Features

✅ Encrypted Password Storage (Fernet/AES)

🔑 Password Generator

👁️ Toggle Password Visibility

🌗 Light/Dark Theme Switcher

📤 Export to CSV

💻 Bootstrap-like UI with ttkbootstrap

📁 Project Structure

password-manager/
|
├── main.py               # GUI application logic
├── crypto_utils.py       # Encryption/decryption helper functions
├── key.key               # Auto-generated encryption key
├── passwords.enc         # Encrypted password database
├── passwords_export.csv  # Exported passwords (generated)
└── README.md             # This file

🚀 How to Run

1. Install Python

Download from https://www.python.org

2. Install Required Libraries

pip install cryptography ttkbootstrap

3. Run the App

python main.py

The UI will launch and you're ready to manage your passwords.

🧐 How It Works

All data is encrypted using Fernet (AES-based symmetric encryption)

A key is saved in key.key (generated if missing)

Passwords are securely written to passwords.enc

You can view, generate, and export passwords from the UI

🔒 Security Tips

Keep key.key safe — it's required to decrypt your data!

passwords.enc is encrypted and can be safely stored

Do NOT upload key.key or passwords.enc to GitHub

Always add sensitive files to .gitignore

📓 App Features Usage

✅ Save a Password

Fill in Website, Email/Username, and Password

Click "Save"

Your data is encrypted and stored securely

🔐 Generate a Password

Click "Generate Password"

A secure random password will appear in the field

👁️ Toggle Password Visibility

Click "Show/Hide" button to toggle masking

📂 View All Passwords

Click "View All"

A new window will display all decrypted passwords

📃 Export to CSV

Click "Export to CSV"

Passwords are saved to passwords_export.csv in plain text (for backup)

🌚/🌜 Theme Toggle

Click theme toggle to switch between Light and Dark modes

🤝 Final Notes

Built with ❤️ in Python

Ideal for beginners to learn about GUI, encryption, and data management

Extendable with features like:

Master password

Password strength checker

Cloud sync or local DB

Multi-user support

Need screenshots or a PDF version for submission? Just ask!

