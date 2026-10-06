var_start = 1
var_end = 10

total_sum = 0

for num in range(var_start, var_end + 1):
    if num % 2 == 0:
        total_sum += num

print(f"Сума парних чисел у діапазоні від {var_start} до {var_end}: {total_sum}")