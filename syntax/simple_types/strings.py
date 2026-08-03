# methods
'some str'.upper()  # => 'SOME STR'
'SOME str'.lower()  # => 'some str'
'some str'.capitalize()  # => 'Some str'
'some str'.title()  # => 'Some Str'
'some str'.count('s')  # => 2
# замінює перший аргумент на другий н разів.
'some str'.replace('s', 'm', 1)  # замінює перший аргумент на другий н разів.
#  => 'some str'

'SoMe StR'.swapcase()  # => 'sOmE sTr'

# методи вирівнювання
'some str'.ljust(17, '#')  # => 'some str#########'
'some str'.rjust(17, '#')
'some str'.center(17, '#')

# методи видалення
'#####some str####'.lstrip('#')  # => 'some str####'
'#####some str####'.rstrip('#')
'#####some str####'.strip('#')

# методи розділення
'#####some str####'.split()  # => ['#####some', 'str####']

'file.name.zip'.rsplit('.', 1)  # => ['file.name', 'zip']
# а як що немає розширення?
'file.name.zip.bip'.partition('.')  # => ('file', '.', 'name.zip.bip')
'file.name.zip.bip'.rpartition('.')  # => ('file.name.zip', '.', 'bip')

# За допомогою Join можливо зʼєднати послідовність рядків.
"".join('Hello my Dear friend'.split())

# Оператор
'itvdn' in 'I\'am itvdn student'

# Пошук підрядка
'I\'am some student'.find('some')  # => 5
'I"am some student'.find('some', 3, 20)

# заміна підстроки
'Student of the Python course'.replace('Student', 'Hard working Student')
'Student of the Python course Student'.replace('Student', 'Hard working Student', 1)

# old
print("Hello dear %s %s your age is %d" % ('Mark', 'Dillan', 44))

name = 'Mark'
surname = 'Dillan'
age = 44

print("Hello dear %s %s your age is %d" % (name, surname, age))


# popular
print("Hello dear {0} {1} your age is {2}".format('Mark', 'Dillan', 44))
print("Hello dear {0} {1} your age is {2}".format(name, surname, age))
print(f"Hello dear {name} {surname} your age is {age}")