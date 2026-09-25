
def fibonacci_de_quy(n):
    if n <= 1:
        return n

    return (
        fibonacci_de_quy(n - 1)
        + fibonacci_de_quy(n - 2)
    )


print("\n10 so Fibonacci dau tien:")

for i in range(10):
    print(fibonacci_de_quy(i), end=" ")

print()


print("\nFibonacci thu 30:")
print(fibonacci_de_quy(30))