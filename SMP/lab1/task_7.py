start_number = 1
end_number = 50

current = start_number
lucky_found = False

while current <= end_number:
    if current % 2 != 0:
        current += 1
        continue

    if current % 7 == 0 and current % 3 != 0:
        print(f'Знайдено "щасливе" число: {current}')
        lucky_found = True
        break

    current += 1

if not lucky_found:
    print('No "lucky" number was found in the range.')