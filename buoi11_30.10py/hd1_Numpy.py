import numpy as np

# 1. Tạo danh sách điểm bằng Python
diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]

# 2. Chuyển list thành mảng NumPy
diem_array = np.array(diem_list)

print(type(diem_list), type(diem_array))

# 4. Phép toán vector hóa: cộng 0.5 cho toàn bộ mảng
diem_cong_them = diem_array + 0.5
print("Diem cong them:", diem_cong_them)

# 5. So sánh với cách sử dụng list thông thường
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print("Diem cong them list:", diem_cong_them_list)

print("Trung binh:", np.mean(diem_array))
print("Lon nhat:", np.max(diem_array))
print("Nho nhat:", np.min(diem_array))
print("Do lech chuan:", round(np.std(diem_array), 2))

ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)