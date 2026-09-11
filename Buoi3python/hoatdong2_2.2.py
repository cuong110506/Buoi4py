ma_tran = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# In theo tung hang
for hang in ma_tran:
    print(hang)

# In tung phan tu
for hang in ma_tran:
    for phan_tu in hang:
        print(phan_tu, end=" ")
    print()

# Tinh tong tat ca phan tu trong ma tran
tong = 0

for hang in ma_tran:
    for phan_tu in hang:
        tong = tong + phan_tu

print("Tong cac phan tu trong ma tran:", tong)
