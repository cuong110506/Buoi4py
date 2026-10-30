import pandas as pd

# =========================
# BAI 2.1 - DOC FILE CSV
# =========================

df = pd.read_csv("diem_sinh_vien.csv")

print("===== BAI 2.1: DOC CSV =====")

# Xem 5 dong dau tien
print(df.head())

# Xem so dong va so cot
print("Kich thuoc:", df.shape)

# Xem danh sach ten cot
print("Ten cac cot:", df.columns.tolist())


# =========================
# BAI 2.2 - THONG KE THEO MON HOC
# =========================

print("\n===== BAI 2.2: THONG KE =====")

# Tinh diem trung binh theo tung mon
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()

print("Diem trung binh tung mon:")
print(diem_trung_binh_mon)

# Diem trung binh toan bo
print("Diem trung binh toan bo:", df["diem"].mean())

# Diem cao nhat
print("Diem cao nhat:", df["diem"].max())

# Diem thap nhat
print("Diem thap nhat:", df["diem"].min())


# =========================
# BAI 2.3 - DIEM TRUNG BINH SINH VIEN
# =========================

print("\n===== BAI 2.3: THONG KE SINH VIEN =====")

# Tinh diem trung binh cua tung sinh vien
diem_tb_sv = df.groupby("ho_ten")["diem"].mean().round(2)

print("Diem trung binh tung sinh vien:")
print(diem_tb_sv)

# Loc sinh vien dat (diem >= 5)
sinh_vien_dat = diem_tb_sv[diem_tb_sv >= 5.0]

# Loc sinh vien khong dat (diem < 5)
sinh_vien_khong_dat = diem_tb_sv[diem_tb_sv < 5.0]

print("\nSinh vien dat:")
print(sinh_vien_dat)

print("\nSinh vien khong dat:")
print(sinh_vien_khong_dat)