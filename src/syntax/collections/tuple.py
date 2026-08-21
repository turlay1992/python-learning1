some_tuple = (1, 2, 3)
some_tuple2 = tuple(['a', 'b', 'c'])
some_tuple3 = tuple('hello')

# empty
empty_tuple = ()
# empty_tuple2 = tuple()

# creating variables by unpack
a, b, c = (1, 2, 3)

# swapping
d, e = 'Yes', 'No'

a, b = b, a

# variant 2
temp_variable = a

a = b
b = temp_variable
del temp_variable

a, b, *rest = range(10)
first, *middle, last = ('Igor', 'Mark', 'Lena', 'Zurab')

# Methods
some_tuple.count(1) # Пошук кількості входжень
some_tuple.index(1) # Пошук індекса першого входження

class_school = (('Igor', 10), ('Mark', 12), ('Lena', 8), ('Zurab', 11))
for st, mark in class_school:

    print(f'Student:{st}, mark:{mark}')
