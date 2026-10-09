import tkinter as tk

# Ham xu ly khi nhan Submit
def xu_ly_submit():
    ho_ten = entry_ho_ten.get()
    tuoi = entry_tuoi.get()
    email = entry_email.get()

    nhan_ket_qua.config(
        text=f"Da nhan: {ho_ten} - {tuoi} tuoi - {email}"
    )

# Ham xoa noi dung cac o nhap
def xoa_thong_tin():
    entry_ho_ten.delete(0, tk.END)
    entry_tuoi.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    nhan_ket_qua.config(text="")

# Tao cua so chinh
cua_so = tk.Tk()
cua_so.title("Form nhap thong tin")
cua_so.geometry("400x280")
cua_so.resizable(False, False)

# Ho ten
tk.Label(cua_so, text="Ho ten:").grid(
    row=0, column=0, padx=10, pady=10, sticky="w"
)
entry_ho_ten = tk.Entry(cua_so, width=25)
entry_ho_ten.grid(row=0, column=1, padx=10, pady=10)

# Tuoi
tk.Label(cua_so, text="Tuoi:").grid(
    row=1, column=0, padx=10, pady=10, sticky="w"
)
entry_tuoi = tk.Entry(cua_so, width=25)
entry_tuoi.grid(row=1, column=1, padx=10, pady=10)

# Email
tk.Label(cua_so, text="Email:").grid(
    row=2, column=0, padx=10, pady=10, sticky="w"
)
entry_email = tk.Entry(cua_so, width=25)
entry_email.grid(row=2, column=1, padx=10, pady=10)

# Nut Submit
nut_submit = tk.Button(
    cua_so,
    text="Submit",
    command=xu_ly_submit
)
nut_submit.grid(
    row=3, column=0, padx=10, pady=15
)

# Nut Xoa
nut_xoa = tk.Button(
    cua_so,
    text="Xoa",
    command=xoa_thong_tin
)
nut_xoa.grid(
    row=3, column=1, padx=10, pady=15
)

# Nhan hien thi ket qua
nhan_ket_qua = tk.Label(
    cua_so,
    text="",
    font=("Arial", 11),
    fg="blue",
    wraplength=380
)
nhan_ket_qua.grid(
    row=4, column=0, columnspan=2, pady=10
)

# Chay chuong trinh
cua_so.mainloop()