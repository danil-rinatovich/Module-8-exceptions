def personal_sum(numbers) -> ():
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        if isinstance(numbers, (int, list, tuple, set, dict)):
            print('В numbers записан некорректный тип данных')
        return sum(personal_sum(numbers)) / (len(numbers))
    except ZeroDivisionError:
        return 0
    except TypeError:
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')

# Результат 1: 0
# Некорректный тип данных для подсчёта суммы - Строка
# Некорректный тип данных для подсчёта суммы - Ещё Строка
# Результат 2: 2.0
# В numbers записан некорректный тип данных
# Результат 3: None
# Результат 4: 26.5