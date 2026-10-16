import tkinter as tk

cua_so = tk.Tk()
cua_so.title("Vi du Listbox")
cua_so.geometry("300x250")

tk.Label(
    cua_so,
    text="Chon mon hoc:"
).pack(pady=5)

listbox_mon_hoc = tk.Listbox(
    cua_so,
    selectmode="single"
)

for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)

listbox_mon_hoc.pack(pady=10)

nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()

    if lua_chon:
        mon = listbox_mon_hoc.get(lua_chon[0])
        nhan_ket_qua.config(
            text=f"Mon da chon: {mon}"
        )
    else:
        nhan_ket_qua.config(
            text="Ban chua chon mon hoc!"
        )

tk.Button(
    cua_so,
    text="Xem mon da chon",
    command=xem_mon_da_chon
).pack(pady=5)

cua_so.mainloop()