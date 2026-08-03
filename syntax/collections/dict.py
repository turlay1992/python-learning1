# Creating dict
example_dict = {'key': 'value'}

print(example_dict['key'])
print(example_dict.get('key'))
print(example_dict.get('not_exist_key')) # None


capital_cities = {
    'Venezuela': 'Caracas',
    'Nicaragua': 'Managua',
}
# v1
capital_cities = dict(Venezuela='Caracas', Nicaragua='Managua')
#v2
capital_cities = dict(
    [("Venezuela", "Caracas"), ("Nicaragua", "Managua")]
)
#v3
capital_cities = dict([["Ukraine", "Kiev"], ["USA", "Washington"]])
#v4
capital_cities = dict(1 = 'Kiev', USA = 'Washington')  # error should be str

#del
del capital_cities['Venezuela']
print(capital_cities)

# for with dict
for country in capital_cities:
    print(capital_cities[country])

# key with value
for country in capital_cities:
    print(f" {country}: { capital_cities[country]}")

# key with value
for country, capital in capital_cities:
    print(country,  capital)
    
    
capital_cities.clear()  # clear all elements in the dictionary
print(capital_cities)

# items
capital_cities.items()
print(capital_cities)

# pop
print(capital_cities.pop()) # видаляє пару ключ значення зі словника, повертає значення.
print(capital_cities)

# popitem
print(capital_cities.popitem()) # видаляє останню пару ключ значення зі словника, повертає значення. LIFO
print(capital_cities)

# update
capital_cities.update({'Brazil': 'Brasilia'}) #
print(capital_cities)

# values
capital_cities.values() #
print(capital_cities)

# setdefault
capital_cities = {}
capital_cities.setdefault('Romania', 'Bucharest' ) # Повертає значення, або як що ключа немає то повертає значення із аргументу.
print(capital_cities)

# fromkeys
any_dictionary= {}
days_name_list = ['Monday', 'Thuesday', 'Wednesday']
new_dictionary = any_dictionary.fromkeys(days_name_list, 'Day')
print(f'{any_dictionary=}')
print(f'{new_dictionary=}')


# task 1
# Порахувати за допомогою словника скільки разів елемент повторюється у списку.
classmates_name = ['Sergey', 'Igor', 'Tanya', 'Mark', 'Sergey', 'Mikhael', 'Sergey', 'Lena', 'Mark']  # вхідні данні

# answer = {}
# for name in classmates_name:
#    if name in answer.keys():
#       answer[name] += 1
#    else:
#       answer[name] = 1
#
# print(answer)

#v2
# answer = {}
# for name in classmates_name:
#    answer[name] = classmates_name.count(name)
#
# print(answer)

# пройдемося за словником, і вивести всі значення, які мають парний ключ.
# data_dict = {22: 'nice age',1: 'one', 33 :'any text',2: 'two',  3: '3', 5: 5, 6: '6', 9: 'end'}
# data_dict = {}.fromkeys(range(40), "Any value")
# for key, value in data_dict.items():
#    if key % 2 == 0:
#       print(value)

# Видалити всі ключі, значення яких починається з літери.
only_int_keys: dict = {1: 'value', 'key': 123, 2: 'value', 'key2': 123}
only_int_keys_copy: dict = only_int_keys.copy()
for k in only_int_keys.keys():
   if type(k) == str:
      del only_int_keys_copy[k]

print(only_int_keys_copy)