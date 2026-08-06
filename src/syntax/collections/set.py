# set Множина - Це невпорядкована колекція унікальних елементів.

# Two variants how to create
some_set1 = {"a", "b", "c", 2}
some_list1 = [1, 3, 4, 6, 8, 8, 8, 8]

some_set2 = set()
some_set3 = set(some_list1)

# frozenset
some_frozenset1 = frozenset()  # only way


# set from str
some_str = 'School Hillel'
some_set_from_str = set(some_str)

# set operators
len(some_set_from_str)
'2' not in some_set_from_str



# set methods
some_set3.clear()  # видаляє всі елементи із множини

some_set3.pop()  # видаляє довільний елемент

some_set3.discard('new elem')  # Видаляє елемент. Якщо його не було момилка не виникає.

some_set3.remove('new elem')  # Видаляє елемент. Якщо його не було помилка виникає.

some_set3.add('new elem')  # Додає елемент у множину. Якщо він вже є нічого не відбудеться.

some_set3.union(some_set1, some_set2)  # об'єднання множин.
# Аналог .union()
some_new_set = some_set1 | some_set2 | some_set3
some_set1 |= some_set2

some_set3.intersection(some_set1, some_set2)  # Створення нової множини, яка є перетином даних множин
some_set3 & some_set1 & some_set2



some_set3.difference(some_set1, some_set2)  # різниця множин. Повертає новий обʼєкт
some_set3 - some_set1 - some_set2


some_set3.isdisjoint(some_set1)  # Перевірка того, що множина some_set3 не має спільних елементів з множиною some_set1

some_set3.issubset(some_set1)  # перевіртка того , що усі елементи множини some_set3 є елементами множини some_set1
some_set3 <= some_set1


some_set3 < some_set1  #Перевірте, чи some_set3 є правильною підмножиною some_set1, тобто some_set3 <= some_set1 і some_set3 != some_set1.


some_set3.symmetric_difference(some_set1) # Створення нової множини, яка є симетричною різницею даних множин
some_set3 ^ some_set1
