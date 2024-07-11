calls = 0

def count_calls(): #функция подсчета вызовов
    global calls
    calls += 1

def string_info(string): #функция принимающая текст
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search): #фун-я которая выводит True or false
    count_calls()
    string = string.lower()
    list_to_search = [words.lower() for words in list_to_search]
    return string in list_to_search

print(string_info('imagination'))
print(string_info('adobe photoshop'))
print(string_info('Urban'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('race', ['trace', 'racer']))
print(calls)