# Bai 4.1 - Tinh giai thua
n = 5
giai_thua = 1
i = 1

while i <= n:
    giai_thua = giai_thua * i
    i += 1

print(f"Bai 1 :{n}! = {giai_thua}")


# Bai 4.2 - Tong cac chu so
so = 4527
so_tam = so
tong_chu_so = 0

while so_tam > 0:
    chu_so = so_tam % 10
    tong_chu_so += chu_so
    so_tam = so_tam // 10

print(f"Bai 2 :Tong cac chu so cua {so} la: {tong_chu_so}")