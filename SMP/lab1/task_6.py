var_start = 10
var_end = 30

for num in range(var_start, var_end + 1):
    if num % 7 == 0:
        print(f"Перше число, яке ділиться на 7: {num}")
        break
else:
    print("У діапазоні немає жодного числа, що ділиться на 7.")