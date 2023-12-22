gugu = []
for i in range(2, 10):
    result = []
    for j in range(1, 10):
        num = i * j

        if num % 3 == 0 or num % 7 == 0:
            pass
        else:
            result.append(num)
    gugu.append(result)


print(gugu)

