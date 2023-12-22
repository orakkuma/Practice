num = int(input())
result = []

for n in range(1, num+1):
    if num % n == 0:
        result.append(n)

print(result)