def personal_sum(numbers) -> ():
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
        else:
            return result, incorrect_data

def calculate_average(numbers):
    try:
        if not numbers:
            personal_sum(numbers)
    except ZeroDivisionError:
        return 0

    try:
        if isinstance(numbers, int):
            print('В numbers записан некорректный тип данных')
    except TypeError:
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')