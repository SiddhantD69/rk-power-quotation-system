import tkinter as tk
from tkinter import messagebox

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("RK POWER - Quotation System")
root.geometry("900x600")
root.configure(bg="#f4f4f4")

# ---------------- COMMON FUNCTIONS ----------------
def clear():
    for w in root.winfo_children():
        w.destroy()

# ================= LOGIN PAGE =================
def login_page():
    clear()

    frame = tk.Frame(root, bg="white", padx=40, pady=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="RK POWER", font=("Arial", 26, "bold"), fg="red", bg="white").pack(pady=10)
    tk.Label(frame, text="Secure Login", font=("Arial", 14), bg="white").pack(pady=5)

    tk.Label(frame, text="Email", bg="white").pack(anchor="w")
    email = tk.Entry(frame, width=35)
    email.pack(pady=5)

    tk.Label(frame, text="Password", bg="white").pack(anchor="w")
    password = tk.Entry(frame, show="*", width=35)
    password.pack(pady=5)

    def login():
        if email.get() and password.get():
            dashboard()
        else:
            messagebox.showerror("Error", "Enter login details")

    tk.Button(frame, text="LOGIN", bg="#e74c3c", fg="white",
              font=("Arial", 12), width=20, command=login).pack(pady=10)

    tk.Button(frame, text="Create New Account", fg="blue", bd=0).pack()

# ================= DASHBOARD =================
def dashboard():
    clear()

    tk.Label(root, text="Dashboard", font=("Arial", 26, "bold")).pack(pady=20)

    frame = tk.Frame(root)
    frame.pack(pady=20)

    btn_style = {"width": 30, "height": 2, "font": ("Arial", 12)}

    tk.Button(frame, text="New Quotation", **btn_style, command=new_quotation).pack(pady=8)
    tk.Button(frame, text="Quotation History", **btn_style).pack(pady=8)
    tk.Button(frame, text="Quotation Status", **btn_style).pack(pady=8)
    tk.Button(frame, text="Logout", **btn_style, command=login_page).pack(pady=8)

# ================= NEW QUOTATION =================
def new_quotation():
    clear()

    tk.Label(root, text="New Quotation", font=("Arial", 24, "bold")).pack(pady=15)

    form = tk.Frame(root)
    form.pack(pady=10)

    fields = [
        "Quotation Number",
        "Company Name",
        "Company Email",
        "Company Phone",
        "Company Address",
        "Kind Attention",
        "Quotation Date"
    ]

    entries = {}

    for label in fields:
        tk.Label(form, text=label, font=("Arial", 11)).pack(anchor="w")
        entry = tk.Entry(form, width=50)
        entry.pack(pady=4)
        entries[label] = entry

    def save_quotation():
        messagebox.showinfo("Saved", "Quotation Saved Successfully")

    tk.Button(root, text="Save Quotation", bg="#27ae60", fg="white",
              font=("Arial", 12), width=25, command=save_quotation).pack(pady=20)

    tk.Button(root, text="Back", command=dashboard).pack()

# ---------------- START APP ----------------
login_page()
root.mainloop()
