def single_root_words(root_word, *other_words, same_words=None):
    if same_words == None:
        same_words = []

    for i in other_words: #создаем цикл проверки слов
        if i.lower().count(root_word.lower()) or root_word.lower().count(i.lower()): #условие, в котором сверяются слова с основным словом
            same_words.append(i) #если слово подходит, добавляется в список same_words
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')


print(result1)
print(result2)
