# позиційні аргументи
def printing_positional_args(first, second):
    print(second, first, 'зміна позицій аргументів змінює порядок')
    print(first, second)


# if you have more then 2 atr
def sum_two_numbers(a, b, *args):
    return a + b + sum(args)

print(sum_two_numbers(1, 2, 3, 4, 5))
print(sum_two_numbers(1, 2, *range(10)))


# v2
def user_greetings(name, surname, *additional_information):
    return f"hello {name} {surname}\n your information is {additional_information}"  # але краще args

# ключові аргументи

def printing_positional_args(first, second):
    print(f'{first=}, {second=}')


printing_positional_args(first='First', second='Second')

def example_keyword(first=None, second='Second'):
    return first, second

print(example_keyword())

# можна комбінувати але позіційні перші
def example_keyword(first, second=None, third='Second'):
    return first, second, third

print(example_keyword('1'))

# а чи можна передати ключових більше ніж потрібно
def example_keyword(first, second=None, third='Second', **kwargs):
    for key, value in kwargs.items():
        print(f'{key=}, {value=}')
    
    return first, second, third, kwargs

print(example_keyword('1', 2, "Third", a="a1", b="b1"))

"""Positional-only і keyword-only маркери — цього немає прямого еквівалента в JS, 
і це специфічно для Python:"""

def f(a: int, b: int, /, c: int, d: int, *, e: int, f: int) -> int:
    return a + b + c + d + e + f
#        ^-------^  позиційні тільки       ^-------^ іменовані тільки
#          (до /)                            (після *)
#                  a, b, c, d - можна звичайно (позиційно чи іменовано, крім a,b)

# --------------------------------------------------------------
