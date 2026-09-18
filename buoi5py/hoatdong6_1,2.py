# BAI 6.1 - TAM GIAC SAO
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# BAI 6.2 - HINH THOI SAO
n = 4

# Nua tren cua hinh thoi
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Nua duoi cua hinh thoi
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))