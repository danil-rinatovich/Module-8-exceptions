class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        Car.__is_valid_vin(vin)
        Car.__is_valid_numbers(numbers)

    def __is_valid_vin(vin_number):
        if not isinstance(vin_number, int):
            print('Некорректный тип vin номер')
            raise IncorrectVinNumber
        if 1000000 <= vin_number <= 9999999:
            print('Неверный диапазон для vin номера')
            raise IncorrectVinNumber
        return True

    def __is_valid_numbers(numbers):
        if not isinstance(numbers, str):
            print('Некорректный тип данных для номеров')
            raise IncorrectCarNumbers
        if len(numbers) == 6:
            print('Неверная длина номера')
            raise IncorrectCarNumbers
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