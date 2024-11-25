def add_everything_up(a: (int, float), b: str):
    try:
        a + b
    except TypeError:
        return str(a) + str(b)
    else:
        return round(a + b, 3)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))