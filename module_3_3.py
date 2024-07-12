def print_params(a=1, b=3, c=2):
    print(a, b, c)

values_list = [123, 'Cup', True]
values_dict = {'a': 123, 'b': 'Cup', 'c': True}
values_list_2 = [123, 'Cup']
print_params(*values_list_2, 42)
print_params(*values_list)
print_params(**values_dict)
