thanks='Благодарю за внимание :-)'
def visitka(task, avtor):
    print(task)
    print(avtor)
    print()


visitka(task = 'Самостоятельная работа по уроку "Произвольное число параметров"', avtor = 'Студент Крылов Эдуард Васильевич')

def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    print(f'Исходные данные: {root_word} - {other_words}')
    return same_words


# Исходный код:
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print('Полученные однокоренные слова:', result1)
print('Полученные однокоренные слова:',result2)
print()
print(thanks)