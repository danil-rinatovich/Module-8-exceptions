class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        Car.__is_valid_vin(vin)
        Car.__is_valid_numbers(numbers)

    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер',
                    f'Необходим int, ваш тип {type(vin_number)}')
        if 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера',
                    f'Диапазон: 1000000-9999999, ваше значение {vin_number}')
        return True

    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров',
                    f'Необходим str, ваш тип {type(numbers)}')
        if len(numbers) == 6:
            raise IncorrectCarNumbers('Неверная длина номера',
                    f'Необходимо 6, вы ввели {numbers} символов')
        return True

class IncorrectVinNumber:
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers:
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')