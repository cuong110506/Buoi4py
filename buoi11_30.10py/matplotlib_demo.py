import matplotlib.pyplot as plt

# HOAT DONG 3.1: BIEU DO COT
mon_hoc = ["Toan", "Ly", "Hoa"]
diem_trung_binh = [7.0, 6.875, 7.25]

plt.figure(figsize=(6, 4))

plt.bar(mon_hoc, diem_trung_binh, color="skyblue")

plt.title("Diem trung binh theo mon hoc")
plt.xlabel("Mon hoc")
plt.ylabel("Diem trung binh")

plt.savefig("bieu_do_cot.png")
plt.show(block=False)


# HOAT DONG 3.2: BIEU DO DUONG
lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]

plt.figure(figsize=(6, 4))

plt.plot(
    lan_kiem_tra,
    diem_qua_cac_lan,
    marker="o",
    color="green"
)

plt.title("Xu huong diem qua cac lan kiem tra")
plt.xlabel("Lan kiem tra")
plt.ylabel("Diem")

plt.savefig("bieu_do_duong.png")
plt.show()