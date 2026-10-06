var_start = 1
var_end = 20
total_result = 0

for num in range(var_start, var_end + 1):
    if num % 3 == 0 or num % 5 == 0:
        continue

    if num % 2 == 0:
        total_result += num ** 2
    else:
        total_result -= num

print(f"Результат: {total_result}")