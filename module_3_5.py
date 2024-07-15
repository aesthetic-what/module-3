def get_multiplied_digits(number):
    str_number = str(number)
    pr = 1
    for i in str_number:
        first = int(i)
        if int(i) > 0:
            pr *= first
    return pr


f = int(input("Введите число: "))
print(get_multiplied_digits(f))
