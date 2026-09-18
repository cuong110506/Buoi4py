# Bai 5.1 - pass
diem = 6.5

if diem >= 8.0:
    pass
elif diem >= 5.0:
    print("Dat yeu cau")
else:
    pass

# Bai 5.2 - break
so = 29
la_so_nguyen_to = True

if so < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, so):
        if so % i == 0:
            la_so_nguyen_to = False
            break

print(f"{so} co phai so nguyen to khong? {la_so_nguyen_to}")
