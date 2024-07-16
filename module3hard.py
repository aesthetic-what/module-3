def calculate_structure_sum(*data_):
    sum = 0
    for i in data_:
        if isinstance(i, str):
            sum += len(i)
        elif isinstance(i, int):
            sum += i
        elif isinstance(i, (list, tuple, set)):
            sum += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            for key, value in i.items():
                sum += calculate_structure_sum(key, value)

    return sum


data_structure = [
  [1, 2, 3, 4, 5],
  {'a': 4, 'b': 5, 'c': 6},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

res = calculate_structure_sum(data_structure)
print(res)
