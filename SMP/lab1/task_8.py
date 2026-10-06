raw_cars = "aUdi; bmW; pOrScHe; toYoTa; MeRcEdEs "

cars_list = raw_cars.split(";")

for i in range(len(cars_list)):
    brand = cars_list[i].strip()
    if brand.upper() == "BMW":
        cars_list[i] = "BMW"
    else:
        cars_list[i] = brand.capitalize()

cars_list = cars_list[1::2]

result_string = " // ".join(cars_list)

print(result_string)