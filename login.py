import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# ================= DATABASE =================
conn = sqlite3.connect("rk_power.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT
)
""")

conn.commit()

# ================= ROOT =================
root = tk.Tk()
root.title("RK POWER")
root.geometry("1100x700")
root.configure(bg="#f4f4f4")

# ================= COMMON =================
def clear():
    for w in root.winfo_children():
        w.destroy()

# ================= LOGIN =================
def login_page():
    clear()

    frame = tk.Frame(root, bg="white", padx=40, pady=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="RK POWER", font=("Arial", 26, "bold"), fg="red").pack(pady=10)
    tk.Label(frame, text="Login", font=("Arial", 16)).pack()

    tk.Label(frame, text="Email").pack(anchor="w")
    email = tk.Entry(frame, width=35)
    email.pack(pady=5)

    tk.Label(frame, text="Password").pack(anchor="w")
    password = tk.Entry(frame, width=35, show="*")
    password.pack(pady=5)

    msg = tk.Label(frame, fg="red")
    msg.pack()

    def login():
        cur.execute("SELECT * FROM users WHERE email=? AND password=?", (email.get(), password.get()))
        user = cur.fetchone()
        if user:
            dashboard()
        else:
            msg.config(text="Wrong email or password")

    tk.Button(frame, text="LOGIN", bg="#e74c3c", fg="white", width=25, command=login).pack(pady=10)
    tk.Button(frame, text="Create Account", command=create_account).pack()

# ================= CREATE ACCOUNT =================
def create_account():
    clear()

    frame = tk.Frame(root, bg="white", padx=40, pady=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="Create Account", font=("Arial", 20)).pack(pady=10)

    tk.Label(frame, text="Name").pack(anchor="w")
    name = tk.Entry(frame, width=35)
    name.pack()

    tk.Label(frame, text="Email").pack(anchor="w")
    email = tk.Entry(frame, width=35)
    email.pack()

    tk.Label(frame, text="Password").pack(anchor="w")
    password = tk.Entry(frame, width=35, show="*")
    password.pack()

    def create():
        try:
            cur.execute("INSERT INTO users(name,email,password) VALUES (?,?,?)",
                        (name.get(), email.get(), password.get()))
            conn.commit()
            messagebox.showinfo("Success", "Account Created Successfully")
            login_page()
        except:
            messagebox.showerror("Error", "Email already exists")

    tk.Button(frame, text="Create Account", command=create).pack(pady=10)
    tk.Button(frame, text="Back", command=login_page).pack()

# ================= DASHBOARD =================
def dashboard():
    clear()
    tk.Label(root, text="Dashboard", font=("Arial", 26)).pack(pady=20)

    tk.Button(root, text="New Quotation", width=30, height=2, command=new_quotation).pack(pady=10)
    tk.Button(root, text="Logout", width=30, height=2, command=login_page).pack(pady=10)

# ================= NEW QUOTATION =================
def new_quotation():
    clear()

    tk.Label(root, text="New Quotation", font=("Arial", 22)).pack(pady=10)

    form = tk.Frame(root)
    form.pack()

    def field(label):
        tk.Label(form, text=label).pack(anchor="w")
        e = tk.Entry(form, width=50)
        e.pack(pady=4)
        return e

    q_no = field("Quotation Number")
    cname = field("Company Name")
    email = field("Company Email")
    phone = field("Company Phone")
    address = tk.Text(form, height=3, width=50)
    tk.Label(form, text="Company Address").pack(anchor="w")
    address.pack()
    attention = field("Kind Attention")

    tk.Label(form, text="Quotation Date").pack(anchor="w")
    date = tk.Entry(form)
    date.insert(0, datetime.now().strftime("%d-%m-%Y"))
    date.pack()

    # -------- TABLE ----------
    tk.Label(root, text="Item Description", font=("Arial", 18)).pack(pady=10)

    table = tk.Frame(root)
    table.pack()

    headers = ["Sr", "Description", "Qty", "Rate", "Total"]
    for i, h in enumerate(headers):
        tk.Label(table, text=h, width=15, relief="solid").grid(row=0, column=i)

    rows = []

    def add_row():
        r = len(rows) + 1
        row = []
        tk.Label(table, text=str(r), width=15, relief="solid").grid(row=r, column=0)
        for i in range(1, 5):
            e = tk.Entry(table, width=15)
            e.grid(row=r, column=i)
            row.append(e)
        rows.append(row)

    def calculate():
        total = 0
        for r in rows:
            try:
                qty = float(r[1].get())
                rate = float(r[2].get())
                amt = qty * rate
                r[3].delete(0, tk.END)
                r[3].insert(0, str(amt))
                total += amt
            except:
                pass
        total_lbl.config(text=f"Grand Total : ₹ {total:.2f}")

    tk.Button(root, text="Add Row", command=add_row).pack(pady=5)
    tk.Button(root, text="Calculate Total", command=calculate).pack(pady=5)

    total_lbl = tk.Label(root, text="Grand Total : ₹ 0", font=("Arial", 14, "bold"))
    total_lbl.pack(pady=10)

    tk.Button(root, text="Save & Finish", bg="green", fg="white").pack(pady=10)
    tk.Button(root, text="Back", command=dashboard).pack()

# ================= START =================
login_page()
root.mainloop()
