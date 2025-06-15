import tkinter as tk
from tkinter import ttk, messagebox
from password_generator import generate_password
from strength_meter import evaluate_strength
# from user_auth import register_user, login_user
# from encryption import get_fernet

class PasswordManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("420x500")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)
        self.key = None

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.build_main()

   # def build_login(self):
    #    for widget in self.root.winfo_children():
     #       widget.destroy()

      #  tk.Label(self.root, text="Welcome to password Manager", font=("Segoe UI", 14, "bold"), fg="#89b4fa", bg="#1e1e2e").pack(pady=(20, 10))
       # tk.Label(self.root, text="Username", bg="#1e1e2e", fg="white").pack()
       # tk.Entry(self.root, textvariable=self.username_var).pack(pady=5)

   #     tk.Label(self.root, text="Master Password", bg="#1e1e2e", fg="white").pack()
    #    tk.Entry(self.root, textvariable=self.password_var, show="*").pack(pady=5)

     #   tk.Button(self.root, text="Login", command=self.login, bg="#89b4fa", fg="#1e1e2e").pack(pady=5)
      #  tk.Button(self.root, text="Register", command=self.register, bg="#a6e3a1", fg="#1e1e2e").pack()

#    def login(self):
 #       try:
  #          self.key = login_user(self.username_var.get(), self.password_var.get())
   #         self.build_main()
    #    except Exception as e:
     #       messagebox.showerror("Login Failed", str(e))

#    def register(self):
 #       try:
  #          self.key = register_user(self.username_var.get(), self.password_var.get())
   #         self.build_main()
    #    except Exception as e:
     #       messagebox.showerror("Registration Failed", str(e))

    def build_main(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.length_var = tk.StringVar(value="16")
        self.upper_var = tk.BooleanVar(value=True)
        self.lower_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)
        self.generated_password = tk.StringVar()
        self.strength_display = tk.StringVar()

        tk.Label(self.root, text="Password Generator", font=("Segoe UI", 14, "bold"), bg="#1e1e2e", fg="#89b4fa").pack(pady=(10, 5))
        tk.Label(self.root, text="Length", bg="#1e1e2e", fg="white").pack()
        tk.Entry(self.root, textvariable=self.length_var).pack(pady=5)

        opts = tk.Frame(self.root, bg="#1e1e2e")
        opts.pack()
        for text, var in [("Uppercase", self.upper_var), ("Lowercase", self.lower_var), ("Digits", self.digits_var), ("Symbols", self.symbols_var)]:
            tk.Checkbutton(opts, text=text, variable=var, bg="#1e1e2e", fg="white", selectcolor="#313244").pack(side="left", padx=1)

        tk.Button(self.root, text="Generate", command=self.generate, bg="#89b4fa", fg="#1e1e2e").pack(pady=6)

        tk.Entry(self.root, textvariable=self.generated_password, font=("Consolas", 12), justify="center", state="readonly").pack(pady=5)
        tk.Button(self.root, text="Copy", command=self.copy_to_clipboard, bg="#313244", fg="white").pack(pady=5)
        tk.Label(self.root, textvariable=self.strength_display, bg="#1e1e2e", fg="white").pack()

        tk.Button(self.root, text="About", command=self.show_about, bg="#a6e3a1", fg="#1e1e2e").pack(pady=5)

    def generate(self):
        try:
            password = generate_password(
                length=int(self.length_var.get()),
                use_upper=self.upper_var.get(),
                use_lower=self.lower_var.get(),
                use_digits=self.digits_var.get(),
                use_symbols=self.symbols_var.get()
            )
            self.generated_password.set(password)
            score, label = evaluate_strength(password)
            self.strength_display.set(f"Strength: {score}/5 — {label}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        pw = self.generated_password.get()
        if pw:
            self.root.clipboard_clear()
            self.root.clipboard_append(pw)
            self.root.update()

    def show_about(self):
        messagebox.showinfo("About", "Password Generator Created by Ruel Mumba")
