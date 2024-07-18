def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [123, 'Cup', True]
values_dict = {'a': 123, 'b': 'Cup', 'c': True}
values_list_2 = [123, 'Cup']
values_list_3 = [123]
list_ = []
print_params(list_)
print_params(*values_list_3)
print_params(*values_list_2, 42)
print_params(*values_list)
print_params(**values_dict)
print_params(b = 25)
print_params(c = [1,2,3])
