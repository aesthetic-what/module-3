def get_multiplied_digits(number):
    str_number = str(number)
    for i in str_number:
        first = int(i)
        if len(str_number) != 1:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return first


f = int(input("Введите число: "))
print(get_multiplied_digits(f))
