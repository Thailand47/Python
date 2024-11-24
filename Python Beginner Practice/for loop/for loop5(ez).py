total = 0

for num in range(1, 41):
    if num % 4 == 0 and num % 6 == 0:
        total += 30
    if num % 4 == 0 and num % 6 == 1:
        total += 20
    if num % 6 == 0 and num % 4 == 1:
        total += 15

print(total)


