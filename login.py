import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("RK POWER - Quotation System")
root.geometry("1100x700")
root.configure(bg="#f4f4f4")

# ---------------- UTIL ----------------
def clear():
    for widget in root.winfo_children():
        widget.destroy()

# ---------------- LOGIN PAGE ----------------
def login_page():
    clear()

    frame = tk.Frame(root, bg="white", padx=40, pady=40)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="RK POWER", font=("Arial", 28, "bold"), fg="red", bg="white").pack(pady=10)
    tk.Label(frame, text="Login", font=("Arial", 14), bg="white").pack(pady=5)

    tk.Label(frame, text="Email", bg="white").pack(anchor="w")
    email = tk.Entry(frame, width=40)
    email.pack(pady=5)

    tk.Label(frame, text="Password", bg="white").pack(anchor="w")
    password = tk.Entry(frame, width=40, show="*")
    password.pack(pady=5)

    def login():
        if email.get() and password.get():
            dashboard()
        else:
            messagebox.showerror("Error", "Enter Email and Password")

    tk.Button(frame, text="LOGIN", bg="#e74c3c", fg="white",
              width=25, command=login).pack(pady=15)

    tk.Button(frame, text="Create Account", command=lambda: messagebox.showinfo("Info","Feature Coming Soon")).pack()

# ---------------- DASHBOARD ----------------
def dashboard():
    clear()
    tk.Label(root, text="Dashboard", font=("Arial", 26, "bold")).pack(pady=20)

    frame = tk.Frame(root)
    frame.pack(pady=20)

    btn_style = {"width": 30, "height": 2, "font": ("Arial", 12)}

    tk.Button(frame, text="New Quotation", **btn_style, command=new_quotation).pack(pady=10)
    tk.Button(frame, text="Quotation History", **btn_style).pack(pady=10)
    tk.Button(frame, text="Logout", **btn_style, command=login_page).pack(pady=10)

# ---------------- NEW QUOTATION ----------------
def new_quotation():
    clear()

    tk.Label(root, text="New Quotation", font=("Arial", 24, "bold")).pack(pady=10)

    form = tk.Frame(root)
    form.pack(pady=10)

    def labeled_input(label, width=50):
        tk.Label(form, text=label).pack(anchor="w")
        e = tk.Entry(form, width=width)
        e.pack(pady=3)
        return e

    quote_no = labeled_input("Quotation No")
    company = labeled_input("Company Name")
    email = labeled_input("Company Email")
    phone = labeled_input("Company Phone")
    address = tk.Text(form, height=3, width=60)
    tk.Label(form, text="Company Address").pack(anchor="w")
    address.pack(pady=5)

    tk.Label(form, text="Kind Attention").pack(anchor="w")
    attention = tk.Entry(form, width=50)
    attention.pack(pady=3)

    today = datetime.now().strftime("%d-%m-%Y")
    tk.Label(form, text="Quotation Date").pack(anchor="w")
    date = tk.Entry(form, width=30)
    date.insert(0, today)
    date.pack(pady=3)

    # ---------------- ITEM TABLE ----------------
    tk.Label(root, text="Item Description", font=("Arial", 18, "bold")).pack(pady=10)

    table = tk.Frame(root)
    table.pack()

    headers = ["Sr", "Description", "Qty", "Rate", "Total"]
    for i, h in enumerate(headers):
        tk.Label(table, text=h, width=18, relief="solid").grid(row=0, column=i)

    rows = []

    def add_row():
        r = len(rows) + 1
        row = []

        tk.Label(table, text=str(r), width=18, relief="solid").grid(row=r, column=0)
        for c in range(1, 5):
            e = tk.Entry(table, width=18)
            e.grid(row=r, column=c)
            row.append(e)
        rows.append(row)

    def calculate_total():
        total = 0
        for r in rows:
            try:
                qty = float(r[1].get())
                rate = float(r[2].get())
                amount = qty * rate
                r[3].delete(0, tk.END)
                r[3].insert(0, str(amount))
                total += amount
            except:
                pass
        total_label.config(text=f"Grand Total : ₹ {total:.2f}")

    tk.Button(root, text="Add Row", command=add_row).pack(pady=5)
    tk.Button(root, text="Calculate Total", command=calculate_total).pack(pady=5)

    total_label = tk.Label(root, text="Grand Total : ₹ 0", font=("Arial", 14, "bold"))
    total_label.pack(pady=10)

    tk.Button(root, text="Save & Generate PDF", bg="green", fg="white",
              font=("Arial", 12), command=lambda: messagebox.showinfo("Saved", "Quotation Saved")).pack(pady=10)

    tk.Button(root, text="Back", command=dashboard).pack(pady=10)

# ---------------- START ----------------
login_page()
root.mainloop()
