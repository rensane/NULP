var_start = 1
var_end = 10
var_step = 1

total_mult = 1
has_odd = False

for num in range(var_start, var_end + 1, var_step):
    if num % 2 != 0:
        total_mult *= num
        has_odd = True

if not has_odd:
    total_mult = 0

print(f"Добуток непарних чисел у діапазоні: {total_mult}")