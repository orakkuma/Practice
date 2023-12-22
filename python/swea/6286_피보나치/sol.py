a, b = 1, 1
fib = [a, b]

for _ in range(8):
    a, b = b, a + b
    fib.append(b)

print(fib)